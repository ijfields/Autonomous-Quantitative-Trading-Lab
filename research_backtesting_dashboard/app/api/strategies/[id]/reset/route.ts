import { NextRequest, NextResponse } from 'next/server';
import pool from '@/lib/db';

export async function POST(request: NextRequest, { params }: { params: { id: string } }) {
    const idStr = params.id;
    const id = parseInt(idStr, 10);

    if (isNaN(id)) {
        return NextResponse.json({ error: 'Invalid ID provided' }, { status: 400 });
    }

    let client;
    try {
        client = await pool.connect();
        try {
            await client.query('BEGIN');

            // 1. Delete all backtests for this strategy
            await client.query('DELETE FROM backtestresult WHERE strategy_id = $1', [id]);

            // 2. Update strategy status to 'READY_FOR_CODE' (Uppercase as per DB Enum)
            const updateQuery = `
                UPDATE strategy 
                SET status = 'READY_FOR_CODE' 
                WHERE id = $1 
                RETURNING *
            `;
            const res = await client.query(updateQuery, [id]);

            await client.query('COMMIT');

            if (res.rows.length === 0) {
                return NextResponse.json({ error: 'Strategy not found' }, { status: 404 });
            }

            return NextResponse.json({
                success: true,
                message: 'Strategy reset for coding',
                strategy: res.rows[0]
            });
        } catch (error) {
            await client.query('ROLLBACK');
            console.error('Transaction Error:', error);
            throw error;
        } finally {
            client.release();
        }
    } catch (error) {
        console.error('Database Error:', error);
        // eslint-disable-next-line @typescript-eslint/no-explicit-any
        const errorMessage = (error as any).message || String(error);
        return NextResponse.json({
            error: `Internal Server Error: ${errorMessage}`,
            details: errorMessage
        }, { status: 500 });
    }
}
