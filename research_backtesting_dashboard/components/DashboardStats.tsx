"use client";

import { useEffect, useState } from "react";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Activity, BarChart3, TrendingUp, AlertTriangle, CheckCircle, XCircle, Skull, Trash2 } from "lucide-react";
import { SimpleAlertDialog } from "@/components/ui/simple-alert-dialog";
import SystemMonitor from "./SystemMonitor";

interface StatsData {
    status: { status: string; count: string }[];
    results: { result_rating: string; count: string }[];
    assets: { asset_type: string; count: string }[];
    backtestedStrategies?: string;
    rejectedCount?: string;
    crashedCount?: string;
}

interface DashboardStatsProps {
    onFilterChange: (filters: { status?: string; result?: string }) => void;
}

export default function DashboardStats({ onFilterChange }: DashboardStatsProps) {
    const [stats, setStats] = useState<StatsData | null>(null);

    useEffect(() => {
        fetch('/api/stats')
            .then(res => res.json())
            .then(data => setStats(data))
            .catch(err => console.error('Failed to fetch stats:', err));
    }, []);

    // --- Agent Control Hooks (Must be top level) ---
    interface AgentInstance {
        id: number;
        status: string;
        startedAt: string;
        cpu?: number;
        memory?: number;
    }

    interface AgentState {
        backtest: AgentInstance[];
        research: AgentInstance[];
    }

    interface AgentLimits {
        backtest: number;
        research: number;
    }

    const [agentState, setAgentState] = useState<AgentState>({ backtest: [], research: [] });
    const [limits, setLimits] = useState<AgentLimits>({ backtest: 3, research: 2 });
    const [loadingAgent, setLoadingAgent] = useState<string | null>(null);
    const [isResetDialogOpen, setIsResetDialogOpen] = useState(false);
    const [isDbResetDialogOpen, setIsDbResetDialogOpen] = useState(false);
    const [isDeleteFailedDialogOpen, setIsDeleteFailedDialogOpen] = useState(false);
    const [isDeleteCrashedDialogOpen, setIsDeleteCrashedDialogOpen] = useState(false);
    const [isDeleteRejectedDialogOpen, setIsDeleteRejectedDialogOpen] = useState(false);
    const [isKillAllDialogOpen, setIsKillAllDialogOpen] = useState(false);

    const handleKillAllConfirm = async () => {
        setLoadingAgent('kill-all');
        try {
            const res = await fetch('/api/agents/control', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ action: 'kill-all' })
            });
            const data = await res.json();
            if (data.error) {
                alert('Kill All failed: ' + data.error);
            } else {
                window.location.reload();
            }
        } catch (e) {
            console.error(e);
            alert('Kill All request failed');
        } finally {
            setLoadingAgent(null);
            setIsKillAllDialogOpen(false);
        }
    };

    const handleResetConfirm = async () => {
        setLoadingAgent('reset');
        try {
            const res = await fetch('/api/agents/control', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ action: 'reset' })
            });
            const data = await res.json();
            if (data.error) {
                alert('Reset failed: ' + data.error);
            } else {
                window.location.reload();
            }
        } catch (e) {
            console.error(e);
            alert('Reset request failed');
        } finally {
            setLoadingAgent(null);
            setIsResetDialogOpen(false);
        }
    };

    const handleDbResetConfirm = async () => {
        setLoadingAgent('db-reset');
        try {
            const res = await fetch('/api/agents/control', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ action: 'reset-database' })
            });
            const data = await res.json();
            if (data.error) {
                alert('Database reset failed: ' + data.error);
            } else {
                window.location.reload();
            }
        } catch (e) {
            console.error(e);
            alert('Database reset request failed');
        } finally {
            setLoadingAgent(null);
            setIsDbResetDialogOpen(false);
        }
    };

    const handleDeleteJunkConfirm = async (junkType: 'failed' | 'crashed' | 'rejected') => {
        setLoadingAgent(`delete-${junkType}`);
        try {
            const res = await fetch('/api/agents/control', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ action: 'delete-junk', junkType })
            });
            const data = await res.json();
            if (data.error) {
                alert(`Delete ${junkType} failed: ` + data.error);
            } else {
                // Refresh specific stats or reload
                window.location.reload();
            }
        } catch (e) {
            console.error(e);
            alert('Delete request failed');
        } finally {
            setLoadingAgent(null);
            setIsDeleteFailedDialogOpen(false);
            setIsDeleteCrashedDialogOpen(false);
            setIsDeleteRejectedDialogOpen(false);
        }
    };

    const fetchAgentStatus = () => {
        fetch('/api/agents/control')
            .then(res => res.json())
            .then(data => {
                if (!data.error) {
                    setAgentState(data.instances);
                    setLimits(data.limits);
                }
            })
            .catch(err => console.error('Agent Status Error:', err));
    };

    useEffect(() => {
        fetchAgentStatus();
        const interval = setInterval(fetchAgentStatus, 3000); // Poll every 3s for stats
        return () => clearInterval(interval);
    }, []);

    // --- Agent Render Helpers ---
    const startAgent = async (type: 'backtest' | 'research') => {
        setLoadingAgent(type);
        try {
            const res = await fetch('/api/agents/control', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ action: 'start', agentType: type })
            });
            const data = await res.json();
            if (data.error) alert(data.error);
            // Poll will update UI
        } catch (e) {
            console.error(e);
        } finally {
            setLoadingAgent(null);
        }
    };

    const stopAgent = async (type: 'backtest' | 'research', id: number) => {
        setLoadingAgent(`stop-${type}-${id}`);
        try {
            const res = await fetch('/api/agents/control', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ action: 'stop', agentType: type, instanceId: id })
            });
            const data = await res.json();
            if (data.error) alert(data.error);
            // Poll will update UI
        } catch (e) {
            console.error(e);
        } finally {
            setLoadingAgent(null);
        }
    };

    // Helper to render agent grid
    const renderAgentGrid = (type: 'backtest' | 'research', title: string) => {
        const instances = agentState[type] || [];
        const limit = limits[type] || 1;

        return (
            <div className="flex flex-col gap-2 min-w-[250px] flex-1">
                <div className="flex items-center justify-between border-b pb-1 mb-1">
                    <span className="text-sm font-medium">{title}</span>
                    <span className="text-xs text-muted-foreground bg-secondary px-2 py-0.5 rounded-full">
                        {instances.length}/{limit} Active
                    </span>
                </div>

                <div className="space-y-2">
                    {/* Active Instances */}
                    {instances.map(inst => (
                        <div key={inst.id} className="flex items-center justify-between bg-card p-2 rounded border shadow-sm animate-in fade-in slide-in-from-left-2">
                            <div className="flex items-center gap-3">
                                <div className="relative shrink-0">
                                    <div className="w-2.5 h-2.5 rounded-full bg-green-500 animate-pulse" />
                                    <div className="absolute inset-0 rounded-full bg-green-500 animate-ping opacity-20" />
                                </div>
                                <div>
                                    <span className="text-xs font-semibold block">Agent #{inst.id}</span>
                                    {(inst.cpu !== undefined || inst.memory !== undefined) && (
                                        <span className="text-[10px] text-muted-foreground block">
                                            CPU: {inst.cpu?.toFixed(1)}% | Mem: {inst.memory}MB
                                        </span>
                                    )}
                                </div>
                            </div>
                            <button
                                onClick={() => stopAgent(type, inst.id)}
                                disabled={!!loadingAgent}
                                className="shrink-0 text-[10px] text-red-600 bg-red-50 hover:bg-red-100 hover:text-red-700 px-2 py-1 rounded border border-red-100 transition-colors"
                            >
                                {loadingAgent === `stop-${type}-${inst.id}` ? '...' : 'Stop'}
                            </button>
                        </div>
                    ))}

                    {/* Start Button */}
                    {instances.length < limit && (
                        <button
                            onClick={() => startAgent(type)}
                            disabled={!!loadingAgent}
                            className="w-full flex items-center justify-center gap-2 py-2 text-xs border border-dashed border-primary/20 text-muted-foreground hover:bg-primary/5 hover:text-primary hover:border-primary/50 rounded transition-all group"
                        >
                            <span className="text-lg leading-none mb-0.5 group-hover:scale-110 transition-transform">+</span>
                            Start New {type === 'research' ? 'Researcher' : 'Backtester'}
                        </button>
                    )}
                </div>
            </div>
        );
    };

    if (!stats) return null;

    const totalStrategies = stats.status.reduce((acc, curr) => acc + parseInt(curr.count), 0);
    const profitableCount = stats.results.find(r => r.result_rating?.toLowerCase() === 'profitable')?.count || 0;
    const failedCount = stats.status.reduce((acc, curr) => {
        const s = curr.status?.toLowerCase();
        if (s === 'failed' || s === 'crashed' || s === 'error') return acc + parseInt(curr.count);
        return acc;
    }, 0);

    const researchingCount = stats.status.reduce((acc, curr) => {
        const s = curr.status?.toLowerCase();
        // Research Agents handle: researching, coding, and freshly scouted
        if (s === 'researching' || s === 'coding' || s === 'scouted') return acc + parseInt(curr.count);
        return acc;
    }, 0);

    const backtestingCount = stats.status.reduce((acc, curr) => {
        const s = curr.status?.toLowerCase();
        // Backtest Agents handle: backtesting
        if (s === 'backtesting') return acc + parseInt(curr.count);
        return acc;
    }, 0);

    return (
        <div className="space-y-6">
            <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-5">
                <Card className="cursor-pointer hover:bg-accent/50 transition-colors col-span-1" onClick={() => onFilterChange({ status: '' })}>
                    <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                        <CardTitle className="text-sm font-medium">Total Strategies</CardTitle>
                        <Activity className="h-4 w-4 text-muted-foreground" />
                    </CardHeader>
                    <CardContent>
                        <div className="text-2xl font-bold">{totalStrategies}</div>
                        <p className="text-xs text-muted-foreground">all stages</p>
                    </CardContent>
                </Card>

                <Card
                    className="cursor-pointer hover:bg-accent/50 transition-colors col-span-1"
                    onClick={() => onFilterChange({ result: 'PROFITABLE', status: '' })}
                >
                    <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                        <CardTitle className="text-sm font-medium">Profitable</CardTitle>
                        <TrendingUp className="h-4 w-4 text-green-500" />
                    </CardHeader>
                    <CardContent>
                        <div className="text-2xl font-bold">{profitableCount}</div>
                        <p className="text-xs text-muted-foreground">found strategies</p>
                    </CardContent>
                </Card>

                <Card
                    className="cursor-pointer hover:bg-accent/50 transition-colors col-span-1 border-blue-200"
                    onClick={() => onFilterChange({ status: 'researching', result: '' })}
                >
                    <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                        <CardTitle className="text-sm font-medium">Active Research</CardTitle>
                        <BarChart3 className="h-4 w-4 text-blue-500" />
                    </CardHeader>
                    <CardContent>
                        <div className="text-2xl font-bold">{researchingCount}</div>
                        <p className="text-xs text-muted-foreground">scouted / coding</p>
                    </CardContent>
                </Card>

                <Card
                    className="cursor-pointer hover:bg-accent/50 transition-colors col-span-1 border-purple-200"
                    onClick={() => onFilterChange({ status: 'backtesting', result: '' })}
                >
                    <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                        <CardTitle className="text-sm font-medium">Active Backtest</CardTitle>
                        <CheckCircle className="h-4 w-4 text-purple-500" />
                    </CardHeader>
                    <CardContent>
                        <div className="text-2xl font-bold">{backtestingCount}</div>
                        <p className="text-xs text-muted-foreground">in progress</p>
                    </CardContent>
                </Card>

                <Card className="cursor-pointer hover:bg-accent/50 transition-colors col-span-1">
                    <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                        <CardTitle className="text-sm font-medium">Completed</CardTitle>
                        <CheckCircle className="h-4 w-4 text-muted-foreground" />
                    </CardHeader>
                    <CardContent>
                        <div className="text-2xl font-bold">{stats.backtestedStrategies || 0}</div>
                        <p className="text-xs text-muted-foreground">finished backtests</p>
                    </CardContent>
                </Card>
            </div>

            {/* Second Row: Problem Cards */}
            <div className="grid gap-4 md:grid-cols-3">
                <Card
                    className="cursor-pointer hover:bg-accent/50 transition-colors border-red-200"
                    onClick={() => onFilterChange({ status: 'FAILED', result: '' })}
                >
                    <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                        <CardTitle className="text-sm font-medium">Generation Failed</CardTitle>
                        <AlertTriangle className="h-4 w-4 text-red-500" />
                    </CardHeader>
                    <CardContent>
                        <div className="text-2xl font-bold">{failedCount}</div>
                        <p className="text-xs text-muted-foreground">strategies needing attention</p>
                    </CardContent>
                </Card>

                <Card
                    className="cursor-pointer hover:bg-accent/50 transition-colors border-gray-300"
                    onClick={() => onFilterChange({ status: 'REJECTED', result: '' })}
                >
                    <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                        <CardTitle className="text-sm font-medium">Rejected</CardTitle>
                        <XCircle className="h-4 w-4 text-gray-500" />
                    </CardHeader>
                    <CardContent>
                        <div className="text-2xl font-bold">{stats.rejectedCount || 0}</div>
                        <p className="text-xs text-muted-foreground">duplicate strategies</p>
                    </CardContent>
                </Card>

                <Card
                    className="cursor-pointer hover:bg-accent/50 transition-colors border-red-300"
                    onClick={() => onFilterChange({ result: 'CRASHED', status: '' })}
                >
                    <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                        <CardTitle className="text-sm font-medium">Crashed</CardTitle>
                        <Skull className="h-4 w-4 text-red-600" />
                    </CardHeader>
                    <CardContent>
                        <div className="text-2xl font-bold">{stats.crashedCount || 0}</div>
                        <p className="text-xs text-muted-foreground">execution failures</p>
                    </CardContent>
                </Card>
            </div>

            {/* System Monitor Area (CPU/RAM Graphs) */}
            <SystemMonitor />

            {/* Multi-Agent Control Center (Spans full width) */}
            <Card className="bg-muted/30 border-muted">
                <CardHeader className="py-3 border-b bg-card rounded-t-lg">
                    <CardTitle className="text-sm font-medium flex items-center gap-2">
                        <Activity className="w-4 h-4 text-primary" />
                        Agent Control Center
                    </CardTitle>
                </CardHeader>
                <CardContent className="py-4">
                    <div className="flex flex-col lg:flex-row gap-8">
                        {renderAgentGrid('research', 'Research Agents (Low Memory)')}

                        <div className="hidden lg:block w-px bg-border my-2" />

                        {renderAgentGrid('backtest', 'Backtest Agents (High Memory)')}

                        <div className="hidden lg:block w-px bg-border my-2" />

                        {/* Danger Zone */}
                        <div className="flex flex-col justify-center gap-3 lg:ml-auto lg:w-[260px]">
                            <div className="text-sm font-medium flex items-center gap-2 text-destructive">
                                <AlertTriangle className="w-4 h-4" />
                                Danger Zone
                            </div>
                            <button
                                onClick={() => setIsKillAllDialogOpen(true)}
                                disabled={!!loadingAgent}
                                className="w-full px-4 py-2 text-xs font-bold rounded border border-red-500 bg-red-600 text-white hover:bg-red-700 transition-all shadow-sm flex items-center justify-center gap-2 animate-pulse hover:animate-none"
                            >
                                <Skull className="w-4 h-4" />
                                {loadingAgent === 'kill-all' ? 'TERMINATING...' : 'KILL ALL AGENTS'}
                            </button>
                            <button
                                onClick={() => setIsResetDialogOpen(true)}
                                disabled={!!loadingAgent}
                                className="w-full px-4 py-2 text-xs font-semibold rounded border border-orange-200 bg-orange-50 text-orange-600 hover:bg-orange-600 hover:text-white transition-all shadow-sm"
                            >
                                {loadingAgent === 'reset' ? 'Cleaning...' : 'Clean All Backtests'}
                            </button>
                            <div className="flex gap-2">
                                <button
                                    onClick={() => setIsDeleteFailedDialogOpen(true)}
                                    disabled={!!loadingAgent}
                                    className="flex-1 px-2 py-2 text-[10px] font-semibold rounded border border-red-200 bg-red-50 text-red-600 hover:bg-red-600 hover:text-white transition-all shadow-sm flex items-center justify-center gap-1"
                                >
                                    <Trash2 className="w-3 h-3" />
                                    {loadingAgent === 'delete-failed' ? '...' : 'Failed'}
                                </button>
                                <button
                                    onClick={() => setIsDeleteCrashedDialogOpen(true)}
                                    disabled={!!loadingAgent}
                                    className="flex-1 px-2 py-2 text-[10px] font-semibold rounded border border-red-300 bg-red-50 text-red-700 hover:bg-red-700 hover:text-white transition-all shadow-sm flex items-center justify-center gap-1"
                                >
                                    <Skull className="w-3 h-3" />
                                    {loadingAgent === 'delete-crashed' ? '...' : 'Crashed'}
                                </button>
                                <button
                                    onClick={() => setIsDeleteRejectedDialogOpen(true)}
                                    disabled={!!loadingAgent}
                                    className="flex-1 px-2 py-2 text-[10px] font-semibold rounded border border-gray-300 bg-gray-50 text-gray-600 hover:bg-gray-600 hover:text-white transition-all shadow-sm flex items-center justify-center gap-1"
                                >
                                    <XCircle className="w-3 h-3" />
                                    {loadingAgent === 'delete-rejected' ? '...' : 'Rejected'}
                                </button>
                            </div>
                            <button
                                onClick={() => setIsDbResetDialogOpen(true)}
                                disabled={!!loadingAgent}
                                className="w-full px-4 py-2 text-xs font-semibold rounded border border-red-200 bg-red-50 text-red-600 hover:bg-red-600 hover:text-white transition-all shadow-sm"
                            >
                                {loadingAgent === 'db-reset' ? 'Resetting...' : '⚠️ Reset Database'}
                            </button>
                        </div>
                    </div>
                </CardContent>
            </Card>

            <SimpleAlertDialog
                isOpen={isKillAllDialogOpen}
                onClose={() => setIsKillAllDialogOpen(false)}
                onConfirm={handleKillAllConfirm}
                title="☢️ NUCLEAR: KILL ALL AGENTS?"
                description="This will FORCE STOP all running agents (Backtest & Research) including PM2 processes and any zombie scripts. Use this if agents are stuck or doubling up."
                confirmText="YES, KILL EVERYTHING"
                variant="destructive"
                isLoading={loadingAgent === 'kill-all'}
            />

            <SimpleAlertDialog
                isOpen={isResetDialogOpen}
                onClose={() => setIsResetDialogOpen(false)}
                onConfirm={handleResetConfirm}
                title="Clean All Backtests?"
                description="This will delete all backtest results and reset strategy statuses. Strategies will remain but need to be re-backtested."
                confirmText="Yes, Clean Backtests"
                variant="destructive"
                isLoading={loadingAgent === 'reset'}
            />

            <SimpleAlertDialog
                isOpen={isDbResetDialogOpen}
                onClose={() => setIsDbResetDialogOpen(false)}
                onConfirm={handleDbResetConfirm}
                title="⚠️ NUCLEAR: Reset Entire Database?"
                description="This will DROP ALL TABLES and recreate them. ALL strategies, backtests, and data will be permanently deleted. This cannot be undone!"
                confirmText="Yes, Destroy Everything"
                variant="destructive"
                isLoading={loadingAgent === 'db-reset'}
            />

            <SimpleAlertDialog
                isOpen={isDeleteFailedDialogOpen}
                onClose={() => setIsDeleteFailedDialogOpen(false)}
                onConfirm={() => handleDeleteJunkConfirm('failed')}
                title="Delete Failed Strategies?"
                description="This will permanently delete all strategies with FAILED status along with their backtests. This cannot be undone!"
                confirmText="Yes, Delete Failed"
                variant="destructive"
                isLoading={loadingAgent === 'delete-failed'}
            />

            <SimpleAlertDialog
                isOpen={isDeleteCrashedDialogOpen}
                onClose={() => setIsDeleteCrashedDialogOpen(false)}
                onConfirm={() => handleDeleteJunkConfirm('crashed')}
                title="Delete Crashed Strategies?"
                description="This will permanently delete all strategies that crashed during backtesting along with their results. This cannot be undone!"
                confirmText="Yes, Delete Crashed"
                variant="destructive"
                isLoading={loadingAgent === 'delete-crashed'}
            />

            <SimpleAlertDialog
                isOpen={isDeleteRejectedDialogOpen}
                onClose={() => setIsDeleteRejectedDialogOpen(false)}
                onConfirm={() => handleDeleteJunkConfirm('rejected')}
                title="Delete Rejected Strategies?"
                description="This will permanently delete all REJECTED (duplicate) strategies. This cannot be undone!"
                confirmText="Yes, Delete Rejected"
                variant="destructive"
                isLoading={loadingAgent === 'delete-rejected'}
            />
        </div>
    );
}
