import { NextRequest, NextResponse } from 'next/server';
import pool from '@/lib/db';

export async function GET(request: NextRequest, { params }: { params: { id: string } }) {
    const id = params.id;

    try {
        const query = `
            SELECT s.*, 
                   (SELECT json_agg(b.*) FROM backtestresult b WHERE b.strategy_id = s.id) as backtests,
                   (SELECT json_agg(se.*) FROM strategyembedding se WHERE se.strategy_id = s.id) as embedding
            FROM strategy s
            WHERE s.id = $1
        `;

        const res = await pool.query(query, [id]);

        if (res.rows.length === 0) {
            return NextResponse.json({ error: 'Strategy not found' }, { status: 404 });
        }

        return NextResponse.json(res.rows[0]);
    } catch (error) {
        console.error('Database Error:', error);
        // eslint-disable-next-line @typescript-eslint/no-explicit-any
        return NextResponse.json({ error: 'Internal Server Error', details: (error as any).message }, { status: 500 });
    }
}

export async function DELETE(request: NextRequest, { params }: { params: { id: string } }) {
    const id = params.id;

    try {
        // Delete in order of foreign key dependencies
        // 1. Delete backtest results
        await pool.query('DELETE FROM backtestresult WHERE strategy_id = $1', [id]);

        // 2. Delete strategy embeddings
        await pool.query('DELETE FROM strategyembedding WHERE strategy_id = $1', [id]);

        // 3. Delete the strategy itself
        const result = await pool.query('DELETE FROM strategy WHERE id = $1 RETURNING id', [id]);

        if (result.rowCount === 0) {
            return NextResponse.json({ error: 'Strategy not found' }, { status: 404 });
        }

        return NextResponse.json({ status: 'deleted', id: parseInt(id) });
    } catch (error) {
        console.error('Delete Error:', error);
        // eslint-disable-next-line @typescript-eslint/no-explicit-any
        return NextResponse.json({ error: 'Failed to delete strategy', details: (error as any).message }, { status: 500 });
    }
}
