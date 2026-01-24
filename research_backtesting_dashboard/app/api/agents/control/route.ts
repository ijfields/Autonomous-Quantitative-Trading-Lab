import { NextResponse } from 'next/server';
import { spawn, exec } from 'child_process';
import path from 'path';
import fs from 'fs';

// --- CONFIGURATION ---
// Read from environment variable, fallback to default for backwards compatibility
const PROJECT_ROOT = process.env.PROJECT_ROOT || "/home/rodrigo/Documents/research_backtesting_agents-Project/research_backtesting_agentsV2";
const VENV_PYTHON = path.join(PROJECT_ROOT, "venv/bin/python");
const RESET_SCRIPT = path.join(PROJECT_ROOT, "reset_strategy.py");
const RESET_DB_SCRIPT = path.join(PROJECT_ROOT, "reset_db.py");
const PM2_PATH = "/usr/local/bin/pm2"; // Absolute path to fix 'command not found'

// Hardware-aware concurrency limits
const MAX_LIMITS = {
    backtest: 5,  // Increased from 3 to 5 per user request
    research: 5   // Increased from 2 to 5 per user request
};

interface AgentInstance {
    id: number;
    pid: number;
    status: 'running' | 'stopped';
    startedAt: string;
    type: 'backtest' | 'research';
}

// In-memory state (Note: resets on server restart, process managers like PM2 keep this alive)
let agentInstances: { backtest: AgentInstance[], research: AgentInstance[] } = {
    backtest: [],
    research: []
};

// Helper: Find lowest available Instance ID (e.g., if 1 and 3 are running, return 2)
function findNextId(instances: AgentInstance[], maxLimit: number): number | null {
    const activeIds = new Set(instances.map(i => i.id));
    for (let i = 1; i <= maxLimit; i++) {
        if (!activeIds.has(i)) return i;
    }
    return null;
}

// Helper: Get script path based on type
function getScriptPath(type: 'backtest' | 'research') {
    return path.join(PROJECT_ROOT, type === 'backtest' ? "backtest_main.py" : "research_main.py");
}

// Helper: Get process stats (CPU%, RAM in MB)
function getProcessStats(pid: number): Promise<{ cpu: number, memory: number }> {
    return new Promise((resolve) => {
        exec(`ps -p ${pid} -o %cpu,rss --no-headers`, (err, stdout) => {
            if (err || !stdout) {
                resolve({ cpu: 0, memory: 0 });
                return;
            }
            const parts = stdout.trim().split(/\s+/);
            const cpu = parseFloat(parts[0]) || 0;
            const memoryKB = parseInt(parts[1]) || 0;
            resolve({
                cpu,
                memory: Math.round(memoryKB / 1024)
            });
        });
    });
}

// Helper: Execute command with promise
function execPromise(cmd: string): Promise<string> {
    return new Promise((resolve, reject) => {
        exec(cmd, (error, stdout) => {
            if (error) {
                // pgrep returns exit code 1 if not found, which is fine
                if (error.code === 1) resolve("");
                else reject(error);
            } else {
                resolve(stdout);
            }
        });
    });
}

// Helper: Discover running agents via process list
async function discoverAgents(type: 'backtest' | 'research'): Promise<AgentInstance[]> {
    const scriptName = type === 'backtest' ? "backtest_main.py" : "research_main.py";
    // ps -ef lists all processes. We grep for the script name.
    // We explicitly exclude 'grep' and 'ts-node' (if dev mode confuses things, though usually python is separate)
    try {
        const stdout = await execPromise(`ps -ef | grep "python.*${scriptName}" | grep -v grep`);
        const lines = stdout.split('\n').filter(line => line.trim());

        const instances: AgentInstance[] = [];

        for (const line of lines) {
            // Parse line: UID PID ... CMD
            // Example: rodrigo 12345 ... python backtest_main.py --instance-id 1
            const parts = line.trim().split(/\s+/);
            const pid = parseInt(parts[1]);

            // Extract instance ID using regex from the full line/command
            const match = line.match(/--instance-id\s+(\d+)/);
            if (match && pid) {
                const id = parseInt(match[1]);
                instances.push({
                    id,
                    pid,
                    status: 'running',
                    startedAt: new Date().toISOString(), // We can't easily get start time without more ps commands, defaulting to now/active
                    type
                });
            }
        }

        return instances.sort((a, b) => a.id - b.id);
    } catch (e) {
        console.error(`Discovery error for ${type}:`, e);
        return [];
    }
}

// Helper: Gracefully stop an agent by PID (SIGTERM → wait → SIGKILL)
async function stopAgentByPid(pid: number, instanceId: number): Promise<boolean> {
    console.log(`🛑 Stopping agent #${instanceId} (PID: ${pid})...`);

    try {
        // First: SIGTERM for graceful shutdown (gives agents chance to cleanup)
        exec(`pkill -TERM -P ${pid}`);  // Children
        try { process.kill(pid, 'SIGTERM'); } catch { }

        // Also kill any temp_backtests scripts that might be orphaned
        exec(`pkill -9 -f "strat_${pid}"`); // Clean up strategy runners

        // Poll for death (Wait up to 2 seconds)
        let dead = false;
        for (let i = 0; i < 10; i++) {
            const stillAlive = await new Promise(resolve => {
                try {
                    process.kill(pid, 0); // Throws if process doesn't exist
                    resolve(true);
                } catch {
                    resolve(false);
                }
            });

            if (!stillAlive) {
                dead = true;
                break;
            }
            await new Promise(r => setTimeout(r, 200));
        }

        // If still alive, SIGKILL
        if (!dead) {
            console.warn(`Force killing PID ${pid}...`);
            exec(`pkill -9 -P ${pid} 2>/dev/null`);
            try { process.kill(pid, 'SIGKILL'); } catch { }
        }

        return true;
    } catch (e) {
        console.error(`Kill error for PID ${pid}:`, e);
        return false;
    }
}

export async function GET() {
    // Dynamic discovery instead of memory state
    const backtestAgents = await discoverAgents('backtest');
    const researchAgents = await discoverAgents('research');

    // Enrich instances with real-time stats
    const enrichedData = {
        backtest: await Promise.all(backtestAgents.map(async (agent) => {
            const stats = await getProcessStats(agent.pid);
            return { ...agent, ...stats };
        })),
        research: await Promise.all(researchAgents.map(async (agent) => {
            const stats = await getProcessStats(agent.pid);
            return { ...agent, ...stats };
        }))
    };

    return NextResponse.json({
        instances: enrichedData,
        limits: MAX_LIMITS
    });
}

export async function POST(req: Request) {
    try {
        const body = await req.json();
        const { action, agentType, instanceId } = body;

        // --- RESET ACTION (Clean Backtests) ---
        if (action === 'reset') {
            return new Promise((resolve) => {
                const process = spawn(VENV_PYTHON, [RESET_SCRIPT], {
                    cwd: PROJECT_ROOT
                });

                process.on('close', (code) => {
                    if (code === 0) {
                        resolve(NextResponse.json({ status: 'success', message: 'Backtests Cleaned' }));
                    } else {
                        resolve(NextResponse.json({ status: 'error', message: 'Clean Failed' }, { status: 500 }));
                    }
                });
            });
        }

        // --- RESET DATABASE ACTION (Nuclear) ---
        if (action === 'reset-database') {
            return new Promise((resolve) => {
                // Pass 'yes' via stdin to auto-confirm
                const process = spawn(VENV_PYTHON, [RESET_DB_SCRIPT], {
                    cwd: PROJECT_ROOT
                });

                // Auto-confirm the reset
                process.stdin?.write('yes\n');
                process.stdin?.end();

                process.on('close', (code) => {
                    if (code === 0) {
                        resolve(NextResponse.json({ status: 'success', message: 'Database Reset Complete' }));
                    } else {
                        resolve(NextResponse.json({ status: 'error', message: 'Database Reset Failed' }, { status: 500 }));
                    }
                });
            });
        }

        // --- KILL ALL ACTION (Uses same logic as individual Stop) ---
        if (action === 'kill-all') {
            console.log("☢️ NUCLEAR: KILL ALL AGENTS INITIATED");

            try {
                // === PHASE 1: Discover all running agents ===
                console.log("🔍 Phase 1: Discovering running agents...");
                const backtestAgents = await discoverAgents('backtest');
                const researchAgents = await discoverAgents('research');
                const allAgents = [...backtestAgents, ...researchAgents];

                console.log(`  Found ${allAgents.length} agents to stop`);

                // === PHASE 2: Stop PM2 managed agents (prevent auto-restart) ===
                try {
                    const jlist = await execPromise(`${PM2_PATH} jlist`);
                    const processes = JSON.parse(jlist);
                    const agentsToStop = processes
                        .filter((p: any) => p.name.includes('backtest_agent') || p.name.includes('research_agent'))
                        .map((p: any) => p.pm_id);

                    if (agentsToStop.length > 0) {
                        console.log(`  Stopping PM2 IDs: ${agentsToStop.join(', ')}`);
                        await execPromise(`${PM2_PATH} stop ${agentsToStop.join(' ')}`);
                    }
                } catch (e) {
                    console.warn("PM2 selective stop failed:", e);
                }

                // === PHASE 3: Gracefully stop each agent (reusing stop logic) ===
                console.log("🛑 Phase 2: Gracefully stopping agents...");
                let stoppedCount = 0;
                for (const agent of allAgents) {
                    const success = await stopAgentByPid(agent.pid, agent.id);
                    if (success) stoppedCount++;
                }
                console.log(`  Stopped ${stoppedCount}/${allAgents.length} agents`);

                // === PHASE 4: Database Cleanup for Orphaned Strategies ===
                console.log("🧹 Phase 3: Cleaning up orphaned strategies in database...");
                const pool = (await import('@/lib/db')).default;

                // Reset strategies stuck in research phase
                const researchReset = await pool.query(`
                    UPDATE strategy 
                    SET status = 'SCOUTED' 
                    WHERE status = 'RESEARCHING'
                `);
                console.log(`  - Reset ${researchReset.rowCount} researching → scouted`);

                // Reset strategies stuck in coding/backtesting phase
                const codeReset = await pool.query(`
                    UPDATE strategy 
                    SET status = 'READY_FOR_CODE' 
                    WHERE status IN ('CODING', 'FETCHING_DATA', 'BACKTESTING')
                `);
                console.log(`  - Reset ${codeReset.rowCount} coding/backtesting → ready_code`);

                // Delete partial backtest results for strategies that were reset
                const deletedResults = await pool.query(`
                    DELETE FROM backtestresult 
                    WHERE strategy_id IN (
                        SELECT id FROM strategy 
                        WHERE status = 'READY_FOR_CODE'
                    )
                `);
                console.log(`  - Deleted ${deletedResults.rowCount} orphaned backtest results`);

                return NextResponse.json({
                    status: 'success',
                    message: `Stopped ${stoppedCount} agents. Cleaned up ${(researchReset.rowCount || 0) + (codeReset.rowCount || 0)} orphaned strategies and ${deletedResults.rowCount || 0} partial backtests.`
                });

            } catch (error) {
                console.error("Kill-All failed:", error);
                return NextResponse.json({ error: "Failed to execute Kill-All" }, { status: 500 });
            }
        }

        // --- DELETE JUNK ACTION (Remove Rejected, Failed, or Crashed based on junkType) ---
        if (action === 'delete-junk') {
            const { junkType } = body; // 'failed' | 'crashed' | 'rejected'

            // Import db pool
            const pool = (await import('@/lib/db')).default;

            try {
                // Start a transaction
                const client = await pool.connect();
                try {
                    await client.query('BEGIN');

                    let strategyIdsResult;

                    // Build query based on junk type
                    if (junkType === 'failed') {
                        strategyIdsResult = await client.query(`
                            SELECT id FROM strategy WHERE status = 'FAILED'
                        `);
                    } else if (junkType === 'crashed') {
                        strategyIdsResult = await client.query(`
                            SELECT DISTINCT s.id FROM strategy s
                            INNER JOIN backtestresult br ON s.id = br.strategy_id
                            WHERE br.result_rating = 'CRASHED'
                        `);
                    } else if (junkType === 'rejected') {
                        strategyIdsResult = await client.query(`
                            SELECT id FROM strategy WHERE status = 'REJECTED'
                        `);
                    } else {
                        // Fallback: delete all junk (legacy behavior)
                        strategyIdsResult = await client.query(`
                            SELECT DISTINCT s.id FROM strategy s
                            LEFT JOIN backtestresult br ON s.id = br.strategy_id
                            WHERE s.status IN ('REJECTED', 'FAILED')
                               OR br.result_rating = 'CRASHED'
                        `);
                    }

                    const strategyIds = strategyIdsResult.rows.map((r: { id: number }) => r.id);

                    if (strategyIds.length === 0) {
                        await client.query('COMMIT');
                        client.release();
                        return NextResponse.json({ status: 'success', message: `No ${junkType || 'junk'} strategies found`, deleted: 0 });
                    }

                    // 2. Delete backtests for these strategies
                    await client.query(`DELETE FROM backtestresult WHERE strategy_id = ANY($1)`, [strategyIds]);

                    // 3. Delete embeddings for these strategies
                    await client.query(`DELETE FROM strategyembedding WHERE strategy_id = ANY($1)`, [strategyIds]);

                    // 4. Delete the strategies
                    await client.query(`DELETE FROM strategy WHERE id = ANY($1)`, [strategyIds]);

                    await client.query('COMMIT');
                    client.release();

                    return NextResponse.json({
                        status: 'success',
                        message: `Deleted ${strategyIds.length} ${junkType || 'junk'} strategies`,
                        deleted: strategyIds.length
                    });
                } catch (e) {
                    await client.query('ROLLBACK');
                    client.release();
                    throw e;
                }
            } catch (error) {
                console.error('Delete junk error:', error);
                return NextResponse.json({ error: `Failed to delete ${junkType || 'junk'} strategies` }, { status: 500 });
            }
        }

        if (!['backtest', 'research'].includes(agentType)) {
            return NextResponse.json({ error: "Invalid agent type" }, { status: 400 });
        }

        const type = agentType as 'backtest' | 'research';

        // Get current state via discovery
        const currentAgents = await discoverAgents(type);

        // --- START ACTION ---
        if (action === 'start') {
            // Check limits
            if (currentAgents.length >= MAX_LIMITS[type]) {
                return NextResponse.json({
                    error: `Max limit reached for ${type} agents (${MAX_LIMITS[type]})`
                }, { status: 429 });
            }

            // Get ID
            const nextId = findNextId(currentAgents, MAX_LIMITS[type]);
            if (!nextId) {
                return NextResponse.json({ error: "No available instance slots" }, { status: 500 });
            }

            console.log(`🚀 Starting ${type} agent instance #${nextId}...`);

            // Logs
            const logDir = path.join(PROJECT_ROOT, "logs");
            if (!fs.existsSync(logDir)) fs.mkdirSync(logDir);

            const outLog = fs.openSync(path.join(logDir, `${type}_agent_${nextId}_startup.log`), 'w');
            const errLog = fs.openSync(path.join(logDir, `${type}_agent_${nextId}_error.log`), 'w');

            // Spawn
            const process = spawn(VENV_PYTHON, [
                getScriptPath(type),
                '--instance-id', nextId.toString()
            ], {
                cwd: PROJECT_ROOT,
                detached: true,
                stdio: ['ignore', outLog, errLog]
            });

            process.unref();

            const newInstance: AgentInstance = {
                id: nextId,
                pid: process.pid || 0,
                status: 'running',
                startedAt: new Date().toISOString(),
                type
            };

            return NextResponse.json({
                status: "started",
                instance: newInstance
            });
        }

        // --- STOP ACTION ---
        if (action === 'stop') {
            if (!instanceId) {
                return NextResponse.json({ error: "Instance ID required" }, { status: 400 });
            }

            const instance = currentAgents.find(i => i.id === instanceId);
            if (!instance) {
                return NextResponse.json({ error: "Instance not found (maybe already stopped?)" }, { status: 404 });
            }

            console.log(`🛑 Stopping ${type} agent instance #${instanceId} (PID: ${instance.pid})...`);

            try {
                // 1. Kill entire process tree (all descendants, not just direct children)
                // Using --full to match command line and -g to kill process group
                const scriptName = type === 'backtest' ? 'backtest_main.py' : 'research_main.py';

                // First: SIGTERM for graceful shutdown (gives agents chance to cleanup)
                exec(`pkill -TERM -P ${instance.pid}`);  // Children
                process.kill(instance.pid, 'SIGTERM');    // Parent

                // Also kill any temp_backtests scripts that might be orphaned
                exec(`pkill -9 -f "strat_${instance.pid}"`); // Clean up strategy runners

                // Poll for death (Wait up to 2 seconds)
                let dead = false;
                for (let i = 0; i < 10; i++) {
                    // Check if process exists (kill -0)
                    const stillAlive = await new Promise(resolve => {
                        try {
                            // process.kill(..., 0) throws if process doesn't exist (permission ok usually since own user)
                            // Returns true if signal sent (alive), throws if not found
                            process.kill(instance.pid, 0);
                            resolve(true);
                        } catch (e) {
                            resolve(false);
                        }
                    });

                    if (!stillAlive) {
                        dead = true;
                        break;
                    }
                    await new Promise(r => setTimeout(r, 200));
                }

                // If still alive, SIGKILL
                if (!dead) {
                    console.warn(`Force killing PID ${instance.pid}...`);
                    exec(`pkill -9 -P ${instance.pid} 2>/dev/null`);
                    try { process.kill(instance.pid, 'SIGKILL'); } catch { }
                }

            } catch (e) {
                console.error("Kill error:", e);
            }

            return NextResponse.json({
                status: "stopped",
                instanceId
            });
        }

        return NextResponse.json({ error: "Invalid action" }, { status: 400 });

    } catch (error) {
        console.error("API Error:", error);
        return NextResponse.json({ error: "Internal Server Error" }, { status: 500 });
    }
}
