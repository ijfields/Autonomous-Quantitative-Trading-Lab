"use client";

import { useEffect, useState } from "react";
import { useParams, useRouter } from "next/navigation";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { StatusBadge } from "@/components/StatusBadge";
import { formatDuration, formatPercentage } from "@/lib/utils";
import { ArrowLeft, Code, BarChart3, Activity, AlertTriangle, FileText, ChevronDown, ChevronUp, RotateCcw, Trash2 } from "lucide-react";
import Link from "next/link";
import { BacktestChart } from "@/components/BacktestChart";
import { SimpleAlertDialog } from "@/components/ui/simple-alert-dialog";

interface StrategyDetail {
    id: number;
    name: string;
    description: string;
    status: string;
    asset_type: string;
    created_at: string;
    logic_steps?: string[];
    symbols?: string[];
    timeframes?: string[];
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    backtests?: any[];
}

export default function StrategyDetailsPage() {
    const params = useParams();
    const router = useRouter();
    const [strategy, setStrategy] = useState<StrategyDetail | null>(null);
    const [loading, setLoading] = useState(true);
    const [selectedBacktest, setSelectedBacktest] = useState<any | null>(null);
    const [hoveredBacktest, setHoveredBacktest] = useState<number | null>(null);
    const [expandedChart, setExpandedChart] = useState<number | null>(null);
    const [expandedLog, setExpandedLog] = useState<number | null>(null);

    // Reset Dialog State
    const [showResetDialog, setShowResetDialog] = useState(false);
    const [isResetting, setIsResetting] = useState(false);

    // Delete Dialog State
    const [showDeleteDialog, setShowDeleteDialog] = useState(false);
    const [isDeleting, setIsDeleting] = useState(false);

    useEffect(() => {
        if (!params.id) return;
        fetch(`/api/strategies/${params.id}`)
            .then(res => res.json())
            .then(data => {
                if (data.error) throw new Error(data.error);
                // Sort backtests by Sharpe ratio (best first)
                if (data.backtests) {
                    data.backtests.sort((a: any, b: any) => {
                        // 1. Profitability
                        const profitA = (a.total_return_pct || 0) > 0;
                        const profitB = (b.total_return_pct || 0) > 0;
                        if (profitA !== profitB) return profitA ? -1 : 1;

                        // 2. Significant Trades (>5)
                        const sigA = (a.trades_count || 0) >= 5;
                        const sigB = (b.trades_count || 0) >= 5;
                        if (sigA !== sigB) return sigA ? -1 : 1;

                        // 3. Sortino
                        const sortinoA = a.sortino_ratio ?? -Infinity;
                        const sortinoB = b.sortino_ratio ?? -Infinity;
                        if (sortinoA !== sortinoB) return sortinoB - sortinoA;

                        // 4. Sharpe
                        const sharpeA = a.sharpe_ratio ?? -Infinity;
                        const sharpeB = b.sharpe_ratio ?? -Infinity;
                        return sharpeB - sharpeA;
                    });
                }
                setStrategy(data);
            })
            .catch(err => console.error(err))
            .finally(() => setLoading(false));
    }, [params.id]);

    const handleReset = () => {
        setShowResetDialog(true);
    };

    const confirmReset = async () => {
        if (!strategy) return;
        setIsResetting(true);
        try {
            const res = await fetch(`/api/strategies/${strategy.id}/reset`, { method: 'POST' });
            if (res.ok) {
                window.location.reload();
            } else {
                const data = await res.json();
                alert(`Failed to reset: ${data.error || 'Unknown error'}`);
            }
        } catch (error) {
            console.error(error);
            alert("Error resetting strategy");
        } finally {
            setIsResetting(false);
        }
    };

    const handleDelete = () => {
        setShowDeleteDialog(true);
    };

    const confirmDelete = async () => {
        if (!strategy) return;
        setIsDeleting(true);
        try {
            const res = await fetch(`/api/strategies/${strategy.id}`, { method: 'DELETE' });
            if (res.ok) {
                router.push('/');
            } else {
                const data = await res.json();
                alert(`Failed to delete: ${data.error || 'Unknown error'}`);
            }
        } catch (error) {
            console.error(error);
            alert("Error deleting strategy");
        } finally {
            setIsDeleting(false);
        }
    };

    if (loading) return <div className="p-8 text-center">Loading strategy details...</div>;
    if (!strategy) return <div className="p-8 text-center text-red-500">Strategy not found</div>;

    // Extract indicators from logic_steps
    const indicators = strategy.logic_steps
        ?.filter(step => step.includes('[DATA]'))
        .map(step => step.replace('[DATA]', '').trim()) || [];

    return (
        <main className="min-h-screen bg-background p-8">
            <div className="max-w-6xl mx-auto space-y-8">
                {/* Header */}
                <div>
                    <Link href="/" className="inline-flex items-center text-sm text-muted-foreground hover:text-foreground mb-4">
                        <ArrowLeft className="w-4 h-4 mr-2" /> Back to Dashboard
                    </Link>
                    <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
                        <div>
                            <h1 className="text-3xl font-bold tracking-tight">{strategy.name}</h1>
                            <div className="flex items-center gap-3 mt-2">
                                <StatusBadge status={strategy.status} />
                                <span className="text-muted-foreground">•</span>
                                <span className="text-sm text-muted-foreground">ID: {strategy.id}</span>
                                <span className="text-muted-foreground">•</span>
                                <span className="text-sm text-muted-foreground">{new Date(strategy.created_at).toLocaleString()}</span>
                                <button
                                    onClick={handleReset}
                                    className="ml-2 inline-flex items-center gap-1 px-2 py-1 text-xs font-medium text-muted-foreground hover:text-destructive hover:bg-destructive/10 rounded transition-colors"
                                >
                                    <RotateCcw className="w-3 h-3" />
                                    Reset
                                </button>
                                <button
                                    onClick={handleDelete}
                                    className="ml-1 inline-flex items-center gap-1 px-2 py-1 text-xs font-medium text-muted-foreground hover:text-red-500 hover:bg-red-500/10 rounded transition-colors"
                                >
                                    <Trash2 className="w-3 h-3" />
                                    Delete
                                </button>
                            </div>
                        </div>
                    </div>
                </div>

                <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
                    {/* Sidebar */}
                    <div className="space-y-6">
                        <Card>
                            <CardHeader>
                                <CardTitle className="text-lg">Configuration</CardTitle>
                            </CardHeader>
                            <CardContent className="space-y-4">
                                <div>
                                    <h4 className="text-sm font-medium mb-1">Asset Type</h4>
                                    <span className="text-sm text-muted-foreground capitalize">{strategy.asset_type}</span>
                                </div>
                                <div>
                                    <h4 className="text-sm font-medium mb-2">Symbols</h4>
                                    <div className="flex flex-wrap gap-2">
                                        {strategy.symbols?.map(s => <span key={s} className="text-xs bg-primary/10 px-2 py-1 rounded">{s}</span>)}
                                    </div>
                                </div>
                                <div>
                                    <h4 className="text-sm font-medium mb-2">Timeframes</h4>
                                    <div className="flex flex-wrap gap-2">
                                        {strategy.timeframes?.map(t => <span key={t} className="text-xs bg-secondary px-2 py-1 rounded">{t}</span>)}
                                    </div>
                                </div>
                            </CardContent>
                        </Card>

                        {indicators.length > 0 && (
                            <Card>
                                <CardHeader>
                                    <CardTitle className="text-lg flex items-center gap-2">
                                        <Activity className="w-4 h-4" />
                                        Indicators Used
                                    </CardTitle>
                                </CardHeader>
                                <CardContent>
                                    <ul className="space-y-2 text-sm text-muted-foreground">
                                        {indicators.map((ind, i) => (
                                            <li key={i} className="list-disc list-inside">{ind}</li>
                                        ))}
                                    </ul>
                                </CardContent>
                            </Card>
                        )}
                    </div>

                    {/* Main Content */}
                    <div className="lg:col-span-2 space-y-6">
                        <Card>
                            <CardHeader>
                                <CardTitle>Description</CardTitle>
                            </CardHeader>
                            <CardContent>
                                <p className="text-muted-foreground whitespace-pre-wrap">{strategy.description}</p>
                            </CardContent>
                        </Card>

                        <Card>
                            <CardHeader>
                                <CardTitle className="flex items-center gap-2"><Code className="w-5 h-5" /> Logic Steps</CardTitle>
                            </CardHeader>
                            <CardContent>
                                {strategy.logic_steps && strategy.logic_steps.length > 0 ? (
                                    <ul className="space-y-2 text-sm">
                                        {strategy.logic_steps.map((step, i) => (
                                            <li key={i} className="text-muted-foreground">
                                                <span className="font-mono text-xs bg-primary/10 px-2 py-0.5 rounded mr-2">
                                                    {step.match(/\[([^\]]+)\]/)?.[1] || i + 1}
                                                </span>
                                                {step.replace(/\[([^\]]+)\]\s*/, '')}
                                            </li>
                                        ))}
                                    </ul>
                                ) : (
                                    <p className="text-sm text-muted-foreground italic">No structured logic steps available.</p>
                                )}
                            </CardContent>
                        </Card>

                        {/* Backtest History */}
                        <Card>
                            <CardHeader>
                                <CardTitle className="flex items-center gap-2">
                                    <BarChart3 className="w-5 h-5" />
                                    Backtest History
                                    <span className="text-sm font-normal text-muted-foreground">(Ordered: Best → Worst)</span>
                                </CardTitle>
                            </CardHeader>
                            <CardContent className="space-y-4">
                                {strategy.backtests && strategy.backtests.length > 0 ? (
                                    strategy.backtests.map((bt: any) => (
                                        <div
                                            key={bt.id}
                                            className="border rounded-lg overflow-hidden transition-all"
                                            onMouseEnter={() => setHoveredBacktest(bt.id)}
                                            onMouseLeave={() => setHoveredBacktest(null)}
                                        >
                                            <div className="p-4 space-y-3">
                                                <div className="flex justify-between items-start">
                                                    <div className="flex items-center gap-2 flex-wrap">
                                                        <StatusBadge status={bt.result_rating || 'pending'} />
                                                        <span className="text-xs text-muted-foreground">{new Date(bt.tested_at).toLocaleString()}</span>
                                                        {bt.symbol && (
                                                            <span className="text-xs bg-primary/10 px-2 py-0.5 rounded font-mono">{bt.symbol}</span>
                                                        )}
                                                        {bt.timeframe && (
                                                            <span className="text-xs bg-secondary px-2 py-0.5 rounded font-mono">{bt.timeframe}</span>
                                                        )}
                                                        {bt.backtest_period_days && (
                                                            <span className="text-xs bg-accent px-2 py-0.5 rounded">
                                                                {formatDuration(bt)}
                                                            </span>
                                                        )}
                                                    </div>
                                                    <div className="flex gap-2">
                                                        {hoveredBacktest === bt.id && (
                                                            <button
                                                                onClick={() => setExpandedChart(expandedChart === bt.id ? null : bt.id)}
                                                                className="text-xs px-2 py-1 bg-secondary text-secondary-foreground rounded hover:opacity-80 transition-opacity"
                                                            >
                                                                {expandedChart === bt.id ? 'Hide Chart' : 'Show Chart'}
                                                            </button>
                                                        )}
                                                        {bt.code && (
                                                            <button
                                                                onClick={() => setSelectedBacktest(selectedBacktest?.id === bt.id ? null : bt)}
                                                                className="text-xs px-2 py-1 bg-primary text-primary-foreground rounded hover:opacity-80"
                                                            >
                                                                {selectedBacktest?.id === bt.id ? 'Hide Code' : 'View Code'}
                                                            </button>
                                                        )}
                                                    </div>
                                                </div>

                                                <div className="grid grid-cols-2 md:grid-cols-8 gap-3 text-sm bg-accent/5 p-3 rounded">
                                                    <div>
                                                        <div className="text-xs text-muted-foreground">Return</div>
                                                        <div className={bt.total_return_pct > 0 ? "text-green-500 font-bold" : "text-red-500"}>
                                                            {formatPercentage(bt.total_return_pct)}
                                                        </div>
                                                    </div>
                                                    <div>
                                                        <div className="text-xs text-muted-foreground">Daily Return</div>
                                                        <div className={bt.daily_return_pct > 0 ? "text-green-500 font-bold" : "text-red-500"}>
                                                            {formatPercentage(bt.daily_return_pct)}
                                                        </div>
                                                    </div>
                                                    <div>
                                                        <div className="text-xs text-muted-foreground">Sharpe</div>
                                                        <div className="font-semibold">{(() => {
                                                            const val = Number(bt.sharpe_ratio);
                                                            return isNaN(val) ? "-" : val.toFixed(2);
                                                        })()}</div>
                                                    </div>
                                                    <div>
                                                        <div className="text-xs text-muted-foreground">Sortino</div>
                                                        <div className="font-semibold">{(() => {
                                                            const val = Number(bt.sortino_ratio);
                                                            return isNaN(val) ? "-" : val.toFixed(2);
                                                        })()}</div>
                                                    </div>
                                                    <div>
                                                        <div className="text-xs text-muted-foreground">Win Rate</div>
                                                        <div>{formatPercentage(bt.win_rate)}</div>
                                                    </div>
                                                    <div>
                                                        <div className="text-xs text-muted-foreground">Trades</div>
                                                        <div>{bt.trades_count || 0}</div>
                                                    </div>
                                                    <div>
                                                        <div className="text-xs text-muted-foreground">Max DD</div>
                                                        <div className="text-red-500">{formatPercentage(bt.max_drawdown_pct)}</div>
                                                    </div>
                                                    <div>
                                                        <div className="text-xs text-muted-foreground">Duration</div>
                                                        <div>{bt.backtest_period_days || "-"} Days</div>
                                                    </div>
                                                </div>
                                            </div>

                                            {/* Expandable Chart */}
                                            {expandedChart === bt.id && (
                                                <div className="px-4 pb-4 border-t bg-muted/20">
                                                    <div className="pt-4">
                                                        <h4 className="text-sm font-semibold mb-3 flex items-center gap-2">
                                                            <BarChart3 className="w-4 h-4" />
                                                            Equity Curve
                                                        </h4>
                                                        <BacktestChart backtest={bt} />
                                                    </div>
                                                </div>
                                            )}

                                            {selectedBacktest?.id === bt.id && bt.code && (
                                                <div className="px-4 pb-4 border-t">
                                                    <div className="pt-3">
                                                        <h4 className="text-sm font-semibold mb-2 flex items-center gap-2">
                                                            <Code className="w-4 h-4" />
                                                            Strategy Code
                                                        </h4>
                                                        <pre className="bg-muted p-4 rounded text-xs overflow-x-auto max-h-96">
                                                            <code>{bt.code}</code>
                                                        </pre>
                                                    </div>
                                                </div>
                                            )}

                                            {/* Crashed/Error Section */}
                                            {(bt.result_rating === 'CRASHED' || bt.error_message) && (
                                                <div className="px-4 pb-4 border-t border-red-900/30">
                                                    <div className="pt-3 space-y-3">
                                                        {/* Crash Banner */}
                                                        <div className="flex items-center gap-2 text-red-400">
                                                            <AlertTriangle className="w-4 h-4" />
                                                            <span className="text-sm font-semibold">Backtest Crashed</span>
                                                        </div>

                                                        {/* Error Message */}
                                                        {bt.error_message && (
                                                            <div className="bg-red-950/30 border border-red-900/50 rounded-lg p-3">
                                                                <div className="text-xs text-red-300 font-medium mb-1">Error Message:</div>
                                                                <div className="text-sm text-red-400 font-mono">
                                                                    {bt.error_message}
                                                                </div>
                                                            </div>
                                                        )}

                                                        {/* Execution Log */}
                                                        {bt.execution_log && (
                                                            <div>
                                                                <button
                                                                    onClick={() => setExpandedLog(expandedLog === bt.id ? null : bt.id)}
                                                                    className="flex items-center gap-2 text-xs text-muted-foreground hover:text-foreground transition-colors"
                                                                >
                                                                    <FileText className="w-3 h-3" />
                                                                    View Execution Log
                                                                    {expandedLog === bt.id ? <ChevronUp className="w-3 h-3" /> : <ChevronDown className="w-3 h-3" />}
                                                                </button>
                                                                {expandedLog === bt.id && (
                                                                    <pre className="mt-2 bg-muted p-3 rounded text-xs overflow-x-auto max-h-64 text-muted-foreground">
                                                                        {bt.execution_log}
                                                                    </pre>
                                                                )}
                                                            </div>
                                                        )}

                                                        {/* Code for crashed backtest */}
                                                        {bt.code && bt.result_rating === 'CRASHED' && (
                                                            <div>
                                                                <button
                                                                    onClick={() => setSelectedBacktest(selectedBacktest?.id === bt.id ? null : bt)}
                                                                    className="flex items-center gap-2 text-xs text-muted-foreground hover:text-foreground transition-colors"
                                                                >
                                                                    <Code className="w-3 h-3" />
                                                                    {selectedBacktest?.id === bt.id ? 'Hide Failed Code' : 'View Failed Code'}
                                                                    {selectedBacktest?.id === bt.id ? <ChevronUp className="w-3 h-3" /> : <ChevronDown className="w-3 h-3" />}
                                                                </button>
                                                            </div>
                                                        )}
                                                    </div>
                                                </div>
                                            )}
                                        </div>
                                    ))
                                ) : (
                                    <div className="text-center py-12 text-muted-foreground bg-accent/5 rounded-lg border border-dashed">
                                        {strategy.status === 'FAILED' ? (
                                            <div className="space-y-2">
                                                <AlertTriangle className="w-8 h-8 mx-auto text-red-400 mb-2" />
                                                <h3 className="font-semibold text-foreground">Strategy Generation Failed</h3>
                                                <p className="text-sm max-w-md mx-auto">
                                                    This strategy failed during the initial generation or validation phase,
                                                    so no backtests were initialized.
                                                </p>
                                                <p className="text-xs text-muted-foreground mt-2">
                                                    Possible causes: Syntax errors in generated code, missing optional dependencies, or validation timeouts.
                                                </p>
                                            </div>
                                        ) : (
                                            <p className="text-sm">No backtests recorded yet.</p>
                                        )}
                                    </div>
                                )}
                            </CardContent>
                        </Card>
                    </div>
                </div>
            </div>

            <SimpleAlertDialog
                isOpen={showResetDialog}
                onClose={() => setShowResetDialog(false)}
                onConfirm={confirmReset}
                title="Reset Strategy"
                description="Are you sure you want to reset this strategy? This will delete all backtests and return it to 'Ready for Code' state. This action cannot be undone."
                variant="destructive"
                confirmText="Reset Strategy"
                isLoading={isResetting}
            />

            <SimpleAlertDialog
                isOpen={showDeleteDialog}
                onClose={() => setShowDeleteDialog(false)}
                onConfirm={confirmDelete}
                title="Delete Strategy"
                description="Are you sure you want to permanently delete this strategy and all its backtests? This action cannot be undone."
                variant="destructive"
                confirmText="Delete Forever"
                isLoading={isDeleting}
            />
        </main>
    );
}
