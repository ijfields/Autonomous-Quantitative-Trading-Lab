"use client";

import { useEffect, useState, useCallback } from "react";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Cpu, MemoryStick } from "lucide-react";
import { AreaChart, Area, ResponsiveContainer, YAxis } from 'recharts';

interface SystemData {
    timestamp: number;
    cpuLoad: number; // %
    memUsed: number; // GB
}

export default function SystemMonitor() {
    const [history, setHistory] = useState<SystemData[]>([]);
    const [current, setCurrent] = useState<{
        cpu: { load: number; speed: number };
        memory: { active: number; total: number };
    } | null>(null);

    const fetchData = useCallback(async () => {
        try {
            const res = await fetch('/api/stats/system');
            const data = await res.json();
            if (data.cpu) {
                const now = Date.now();
                const memUsedGB = data.memory.active / (1024 * 1024 * 1024);

                setCurrent(data);
                setHistory(prev => {
                    const newData = [
                        ...prev,
                        {
                            timestamp: now,
                            cpuLoad: data.cpu.load,
                            memUsed: memUsedGB
                        }
                    ];
                    // Keep last 30 points (approx 60s if polling 2s)
                    return newData.slice(-30);
                });
            }
        } catch (e) {
            console.error("Monitor Fetch Error", e);
        }
    }, []);

    useEffect(() => {
        fetchData();
        const interval = setInterval(fetchData, 2000);
        return () => clearInterval(interval);
    }, [fetchData]);

    if (!current) return null;

    const memTotalGB = current.memory.total / (1024 * 1024 * 1024);
    const memPercent = (current.memory.active / current.memory.total) * 100;

    return (
        <div className="grid gap-4 md:grid-cols-2 mt-4">
            {/* CPU Card */}
            <Card>
                <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                    <CardTitle className="text-sm font-medium">CPU Usage</CardTitle>
                    <Cpu className="h-4 w-4 text-blue-500" />
                </CardHeader>
                <CardContent>
                    <div className="flex justify-between items-end mb-4">
                        <div>
                            <div className="text-2xl font-bold">{current.cpu.load.toFixed(1)}%</div>
                            <p className="text-xs text-muted-foreground">{current.cpu.speed.toFixed(2)} GHz</p>
                        </div>
                    </div>

                    <div className="h-[100px] w-full mt-2">
                        <ResponsiveContainer width="100%" height="100%">
                            <AreaChart data={history}>
                                <defs>
                                    <linearGradient id="cpuGradient" x1="0" y1="0" x2="0" y2="1">
                                        <stop offset="5%" stopColor="#3b82f6" stopOpacity={0.3} />
                                        <stop offset="95%" stopColor="#3b82f6" stopOpacity={0} />
                                    </linearGradient>
                                </defs>
                                <YAxis domain={[0, 100]} hide />
                                <Area
                                    type="monotone"
                                    dataKey="cpuLoad"
                                    stroke="#3b82f6"
                                    fillOpacity={1}
                                    fill="url(#cpuGradient)"
                                    isAnimationActive={false}
                                />
                            </AreaChart>
                        </ResponsiveContainer>
                    </div>
                    <p className="text-[10px] text-muted-foreground text-center mt-2">60 Second History</p>
                </CardContent>
            </Card>

            {/* RAM Card */}
            <Card>
                <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                    <CardTitle className="text-sm font-medium">Memory Usage</CardTitle>
                    <MemoryStick className="h-4 w-4 text-purple-500" />
                </CardHeader>
                <CardContent>
                    <div className="flex justify-between items-end mb-4">
                        <div>
                            <div className="text-2xl font-bold">{memPercent.toFixed(1)}%</div>
                            <p className="text-xs text-muted-foreground">
                                {(current.memory.active / (1024 * 1024 * 1024)).toFixed(1)} / {memTotalGB.toFixed(1)} GB
                            </p>
                        </div>
                    </div>

                    <div className="h-[100px] w-full mt-2">
                        <ResponsiveContainer width="100%" height="100%">
                            <AreaChart data={history}>
                                <defs>
                                    <linearGradient id="memGradient" x1="0" y1="0" x2="0" y2="1">
                                        <stop offset="5%" stopColor="#a855f7" stopOpacity={0.3} />
                                        <stop offset="95%" stopColor="#a855f7" stopOpacity={0} />
                                    </linearGradient>
                                </defs>
                                <YAxis domain={[0, memTotalGB]} hide />
                                <Area
                                    type="monotone"
                                    dataKey="memUsed"
                                    stroke="#a855f7"
                                    fillOpacity={1}
                                    fill="url(#memGradient)"
                                    isAnimationActive={false}
                                />
                            </AreaChart>
                        </ResponsiveContainer>
                    </div>
                    <p className="text-[10px] text-muted-foreground text-center mt-2">60 Second History</p>
                </CardContent>
            </Card>
        </div>
    );
}
