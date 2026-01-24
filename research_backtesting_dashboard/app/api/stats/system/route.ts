import { NextResponse } from 'next/server';
import si from 'systeminformation';

export async function GET() {
    try {
        const [cpuLoad, mem, cpuSpeed] = await Promise.all([
            si.currentLoad(),
            si.mem(),
            si.cpuCurrentSpeed()
        ]);

        return NextResponse.json({
            cpu: {
                load: cpuLoad.currentLoad,
                speed: cpuSpeed.avg // Average speed in GHz across cores
            },
            memory: {
                active: mem.active, // Used RAM in bytes (excluding buffers/cache often better for "usage")
                total: mem.total,
                used: mem.used // actual used
            }
        });
    } catch (error) {
        console.error('System Stats Error:', error);
        return NextResponse.json({ error: 'Failed to fetch system stats' }, { status: 500 });
    }
}
