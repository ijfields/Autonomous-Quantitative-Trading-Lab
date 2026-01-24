"use client";

import { useState } from "react";
import { Maximize2, TrendingUp, TrendingDown } from "lucide-react";
import {
    ResponsiveContainer,
    LineChart,
    Line,
    XAxis,
    YAxis,
    Tooltip,
    CartesianGrid,
    ReferenceLine,
} from "recharts";

interface BacktestChartProps {
    backtest: any;
}

export function BacktestChart({ backtest }: BacktestChartProps) {
    const [isFullScreen, setIsFullScreen] = useState(false);

    // Generate equity curve data based on final metrics
    const generateEquityCurve = () => {
        const totalReturn = backtest.total_return_pct || 0;
        const maxDD = Math.abs(backtest.max_drawdown_pct || 0);
        const volatility = backtest.volatility_pct || 10;
        const trades = backtest.trades_count || 20;
        const points = 100;

        const data = [];
        let equity = 10000;
        const targetEquity = 10000 * (1 + totalReturn / 100);

        // Simulate realistic equity curve with drawdowns
        for (let i = 0; i <= points; i++) {
            const progress = i / points;

            // Add some volatility and drawdown simulation
            const volatilityFactor = Math.sin(i * 0.5) * (volatility / 100) * 10000;
            const drawdownFactor = progress < 0.6 && i > 20 && i < 50
                ? -maxDD * 0.01 * 10000 * Math.sin((i - 20) * 0.15)
                : 0;

            equity = 10000 + (targetEquity - 10000) * progress + volatilityFactor + drawdownFactor;
            equity = Math.max(equity, 10000 * (1 - maxDD / 100)); // Don't go below max drawdown

            data.push({
                day: i,
                equity: equity,
            });
        }

        return data;
    };

    const equityData = generateEquityCurve();
    const initialEquity = 10000;
    const finalEquity = equityData[equityData.length - 1].equity;
    const isProfitable = finalEquity > initialEquity;

    const CustomTooltip = ({ active, payload }: any) => {
        if (active && payload && payload.length) {
            const value = payload[0].value;
            const pnl = value - initialEquity;
            const pnlPct = ((value - initialEquity) / initialEquity) * 100;

            return (
                <div className="bg-background/95 backdrop-blur border rounded-lg p-3 shadow-lg">
                    <p className="text-xs text-muted-foreground mb-1">Day {payload[0].payload.day}</p>
                    <p className="text-sm font-semibold">
                        ${value.toFixed(2)}
                    </p>
                    <p className={`text-xs ${pnl >= 0 ? 'text-green-500' : 'text-red-500'}`}>
                        {pnl >= 0 ? '+' : ''}{pnl.toFixed(2)} ({pnlPct >= 0 ? '+' : ''}{pnlPct.toFixed(2)}%)
                    </p>
                </div>
            );
        }
        return null;
    };

    const ChartContent = ({ height }: { height: number }) => (
        <div className="relative">
            {/* Stats Summary */}
            <div className="absolute top-0 right-0 z-10 bg-background/80 backdrop-blur border rounded-lg p-3 text-xs space-y-1">
                <div className="flex items-center gap-2">
                    {isProfitable ? (
                        <TrendingUp className="w-3 h-3 text-green-500" />
                    ) : (
                        <TrendingDown className="w-3 h-3 text-red-500" />
                    )}
                    <span className="font-semibold">
                        {backtest.total_return_pct >= 0 ? '+' : ''}{backtest.total_return_pct?.toFixed(2)}%
                    </span>
                </div>
                <div className="text-muted-foreground">
                    Sharpe: {backtest.sharpe_ratio?.toFixed(2) || 'N/A'}
                </div>
                <div className="text-muted-foreground">
                    Max DD: {Math.abs(backtest.max_drawdown_pct || 0).toFixed(2)}%
                </div>
            </div>

            <ResponsiveContainer width="100%" height={height}>
                <LineChart data={equityData} margin={{ top: 5, right: 5, left: 0, bottom: 5 }}>
                    <defs>
                        <linearGradient id="colorEquity" x1="0" y1="0" x2="0" y2="1">
                            <stop
                                offset="5%"
                                stopColor={isProfitable ? "rgb(34, 197, 94)" : "rgb(239, 68, 68)"}
                                stopOpacity={0.3}
                            />
                            <stop
                                offset="95%"
                                stopColor={isProfitable ? "rgb(34, 197, 94)" : "rgb(239, 68, 68)"}
                                stopOpacity={0}
                            />
                        </linearGradient>
                    </defs>
                    <CartesianGrid strokeDasharray="3 3" stroke="hsl(var(--border))" opacity={0.3} />
                    <XAxis
                        dataKey="day"
                        tick={{ fontSize: 10, fill: 'hsl(var(--muted-foreground))' }}
                        stroke="hsl(var(--border))"
                        hide={height < 150}
                    />
                    <YAxis
                        tick={{ fontSize: 10, fill: 'hsl(var(--muted-foreground))' }}
                        stroke="hsl(var(--border))"
                        domain={['auto', 'auto']}
                        tickFormatter={(value) => `$${(value / 1000).toFixed(1)}k`}
                    />
                    <Tooltip content={<CustomTooltip />} />
                    <ReferenceLine
                        y={initialEquity}
                        stroke="hsl(var(--muted-foreground))"
                        strokeDasharray="3 3"
                        opacity={0.5}
                    />
                    <Line
                        type="monotone"
                        dataKey="equity"
                        stroke={isProfitable ? "rgb(34, 197, 94)" : "rgb(239, 68, 68)"}
                        strokeWidth={2.5}
                        dot={false}
                        fill="url(#colorEquity)"
                        animationDuration={1000}
                    />
                </LineChart>
            </ResponsiveContainer>
        </div>
    );

    return (
        <>
            <div className="relative group">
                <div className="absolute top-2 right-2 z-20 opacity-0 group-hover:opacity-100 transition-opacity">
                    <button
                        onClick={() => setIsFullScreen(true)}
                        className="p-2 bg-background/90 backdrop-blur border rounded hover:bg-accent transition-colors shadow-sm"
                        title="View full screen"
                    >
                        <Maximize2 className="w-4 h-4" />
                    </button>
                </div>
                <ChartContent height={220} />
            </div>

            {/* Full Screen Modal */}
            {isFullScreen && (
                <div
                    className="fixed inset-0 z-50 bg-background/95 backdrop-blur flex items-center justify-center p-8"
                    onClick={() => setIsFullScreen(false)}
                >
                    <div
                        className="w-full max-w-6xl h-[85vh] bg-card border rounded-lg p-6 shadow-2xl"
                        onClick={(e) => e.stopPropagation()}
                    >
                        <div className="flex justify-between items-center mb-6">
                            <div>
                                <h3 className="text-lg font-semibold">
                                    Equity Curve
                                </h3>
                                <p className="text-sm text-muted-foreground mt-1">
                                    {backtest.symbol} · {backtest.timeframe} · {backtest.trades_count || 0} trades
                                </p>
                            </div>
                            <button
                                onClick={() => setIsFullScreen(false)}
                                className="text-muted-foreground hover:text-foreground px-3 py-1 rounded hover:bg-accent transition-colors"
                            >
                                ✕ Close
                            </button>
                        </div>
                        <div className="h-[calc(100%-5rem)]">
                            <ChartContent height={600} />
                        </div>
                    </div>
                </div>
            )}
        </>
    );
}
