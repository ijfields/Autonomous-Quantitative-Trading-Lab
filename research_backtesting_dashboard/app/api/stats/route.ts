import { NextResponse } from 'next/server';
import pool from '@/lib/db';

export async function GET() {
    try {
        // Run queries in parallel for efficiency
        const [statusCounts, resultCounts, assetCounts, backtestedCount, rejectedCount, crashedCount] = await Promise.all([
            pool.query(`SELECT status, COUNT(*) as count FROM strategy GROUP BY status`),
            pool.query(`SELECT result_rating, COUNT(DISTINCT strategy_id) as count FROM backtestresult GROUP BY result_rating`),
            pool.query(`SELECT asset_type, COUNT(*) as count FROM strategy GROUP BY asset_type`),
            pool.query(`SELECT COUNT(DISTINCT strategy_id) as count FROM backtestresult`),
            pool.query(`SELECT COUNT(*) as count FROM strategy WHERE status = 'REJECTED'`),
            pool.query(`SELECT COUNT(DISTINCT strategy_id) as count FROM backtestresult WHERE result_rating = 'CRASHED'`)
        ]);

        return NextResponse.json({
            status: statusCounts.rows,
            results: resultCounts.rows,
            assets: assetCounts.rows,
            backtestedStrategies: backtestedCount.rows[0].count,
            rejectedCount: rejectedCount.rows[0].count,
            crashedCount: crashedCount.rows[0].count
        });
    } catch (error) {
        console.error('Database Error:', error);
        return NextResponse.json({ error: 'Internal Server Error' }, { status: 500 });
    }
}
