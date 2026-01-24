import { NextRequest, NextResponse } from 'next/server';
import pool from '@/lib/db';

export async function GET(request: NextRequest) {
    const searchParams = request.nextUrl.searchParams;
    const page = parseInt(searchParams.get('page') || '1');
    const limit = parseInt(searchParams.get('limit') || '10');
    const status = searchParams.get('status');
    const assetType = searchParams.get('asset_type');
    const result = searchParams.get('result');

    const offset = (page - 1) * limit;

    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    const params: any[] = [];
    let paramIndex = 1;

    // 1. Build Base WHERE Clause (Table: strategy s)
    const conditions = ['1=1'];

    if (status) {
        conditions.push(`s.status = $${paramIndex++}`);
        params.push(status);
    }

    if (assetType) {
        conditions.push(`s.asset_type = $${paramIndex++}`);
        params.push(assetType);
    }

    // 2. Handle Result Filter (Table: best_backtest bb)
    // We handle this in the final query construction, but we prepare the param here
    let resultCondition = "";
    if (result) {
        resultCondition = `AND bb.result_rating = $${paramIndex++}`;
        params.push(result);
    }

    const whereClause = `WHERE ${conditions.join(' AND ')}`;

    // 3. Define Reusable CTE (Best Backtest Logic)
    // Selects the "Best" result for each strategy to determine its current state
    const bestBacktestCTE = `
        WITH best_backtest AS (
            SELECT DISTINCT ON (strategy_id)
                strategy_id,
                sharpe_ratio,
                sortino_ratio,    -- Added for Opus Ranking
                trades_count,     -- Added for Opus Ranking
                total_return_pct,
                daily_return_pct,
                max_drawdown_pct,
                backtest_period_days,
                result_rating, -- Added for filtering
                -- Calmar Ratio: Annualized Return / |Max Drawdown| (higher is better)
                CASE 
                    WHEN max_drawdown_pct IS NULL OR max_drawdown_pct = 0 THEN NULL
                    ELSE (daily_return_pct * 365) / ABS(max_drawdown_pct)
                END as calmar_ratio
            FROM backtestresult
            ORDER BY strategy_id, 
                     -- Prefer profitable backtests
                     CASE WHEN total_return_pct > 0 THEN 0 ELSE 1 END ASC,
                     -- Prefer meaningful trade count
                     CASE WHEN trades_count >= 5 THEN 0 ELSE 1 END ASC,
                     -- Then by risk-adjusted metrics
                     sortino_ratio DESC NULLS LAST,
                     sharpe_ratio DESC NULLS LAST
        )
    `;

    // 4. Main Query
    const query = `
        ${bestBacktestCTE}
        SELECT s.*, 
               (SELECT json_agg(b.* ORDER BY b.tested_at DESC) FROM backtestresult b WHERE b.strategy_id = s.id) as backtests,
               bb.sharpe_ratio as best_sharpe,
               bb.sortino_ratio as best_sortino,     -- New Field
               bb.trades_count as best_trades,       -- New Field
               bb.total_return_pct as best_return,
               bb.daily_return_pct as best_daily_return,
               bb.max_drawdown_pct as best_max_dd,
               bb.backtest_period_days as best_duration,
               bb.calmar_ratio as best_calmar,
               bb.result_rating as best_result
        FROM strategy s
        LEFT JOIN best_backtest bb ON s.id = bb.strategy_id
        ${whereClause}
        ${resultCondition}
        ORDER BY 
            -- Has any backtest data at all
            (bb.strategy_id IS NOT NULL) DESC,
            
            -- [OPUS RANKING V2 - PROFIT FIRST]
            
            -- 1. PROFITABILITY (Absolute requirement - unprofitable strategies ALWAYS rank below profitable ones)
            CASE 
                WHEN bb.total_return_pct > 0 THEN 0  -- Profitable = TOP
                WHEN bb.total_return_pct IS NOT NULL THEN 1  -- Unprofitable = BOTTOM
                ELSE 2  -- No data = VERY BOTTOM
            END ASC,
            
            -- 2. SIGNIFICANCE: Must have meaningful trade volume (>5 trades)
            CASE WHEN bb.trades_count >= 5 THEN 0 ELSE 1 END ASC,
            
            -- 3. EFFICIENCY: Downside Risk Adjusted (Sortino > Calmar/Sharpe for Crypto)
            bb.sortino_ratio DESC NULLS LAST,
            
            -- 4. CONSISTENCY: Fallback to Sharpe
            bb.sharpe_ratio DESC NULLS LAST,
            
            -- 5. MAGNITUDE: Raw profit (within profitable tier, higher profit wins)
            bb.total_return_pct DESC NULLS LAST,
            
            s.created_at DESC
        LIMIT $${paramIndex++} OFFSET $${paramIndex++}
    `;

    // Add limit and offset to params
    params.push(limit, offset);

    try {
        const res = await pool.query(query, params);

        // 5. Total Count Query (Must match filters)
        // We reuse the CTE and Filters to get accurate pagination counts
        const countParams = params.slice(0, params.length - 2); // Exclude limit/offset
        const countQuery = `
            ${bestBacktestCTE}
            SELECT COUNT(*) 
            FROM strategy s 
            LEFT JOIN best_backtest bb ON s.id = bb.strategy_id
            ${whereClause} 
            ${resultCondition}
        `;

        const countRes = await pool.query(countQuery, countParams);
        const total = parseInt(countRes.rows[0].count);

        return NextResponse.json({
            data: res.rows,
            pagination: {
                page,
                limit,
                total,
                totalPages: Math.ceil(total / limit)
            }
        });
    } catch (error) {
        console.error('Database Error:', error);
        // eslint-disable-next-line @typescript-eslint/no-explicit-any
        return NextResponse.json({ error: 'Internal Server Error', details: (error as any).message }, { status: 500 });
    }
}
