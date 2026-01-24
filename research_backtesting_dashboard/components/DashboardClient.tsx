"use client";

import { useEffect, useState, useCallback } from "react";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { StatusBadge } from "@/components/StatusBadge";
import DashboardStats from "@/components/DashboardStats";
import { formatDuration, formatPercentage } from "@/lib/utils";
import { SimpleAlertDialog } from "@/components/ui/simple-alert-dialog";
import Link from "next/link";
import { Filter, Loader2, RotateCcw, Trash2 } from "lucide-react";

interface Strategy {
    id: number;
    name: string;
    status: string;
    asset_type: string;
    created_at: string;
    best_calmar?: number;
    best_sortino?: number;
    best_max_dd?: number;
    best_daily_return?: number;
    best_duration?: number;
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    backtests?: any[];
}

export default function DashboardClient() {
    const [strategies, setStrategies] = useState<Strategy[]>([]);
    const [loading, setLoading] = useState(true);
    const [filters, setFilters] = useState({
        status: "",
        asset_type: "",
        result: "",
        searchTerm: "",
    });
    const [sortBy, setSortBy] = useState<{ field: string; direction: 'asc' | 'desc' } | null>(null);

    // Reset Dialog State
    const [resetStrategyId, setResetStrategyId] = useState<number | null>(null);
    const [isResetting, setIsResetting] = useState(false);

    // Delete Dialog State
    const [deleteStrategyId, setDeleteStrategyId] = useState<number | null>(null);
    const [isDeleting, setIsDeleting] = useState(false);

    const fetchStrategies = useCallback(async () => {
        setLoading(true);
        const params = new URLSearchParams();
        if (filters.status) params.append("status", filters.status);
        if (filters.asset_type) params.append("asset_type", filters.asset_type);
        if (filters.result) params.append("result", filters.result);

        try {
            const res = await fetch(`/api/strategies?${params.toString()}`);
            const data = await res.json();
            let strategies = data.data || [];

            // Client-side search filtering
            if (filters.searchTerm) {
                const searchLower = filters.searchTerm.toLowerCase();
                strategies = strategies.filter((s: Strategy) =>
                    s.name.toLowerCase().includes(searchLower)
                );
            }

            // Client-side sorting
            if (sortBy) {
                strategies = [...strategies].sort((a, b) => {
                    const aBacktest = a.backtests?.[0];
                    const bBacktest = b.backtests?.[0];

                    let aVal: number, bVal: number;
                    switch (sortBy.field) {
                        case 'return':
                            aVal = aBacktest?.total_return_pct ?? -Infinity;
                            bVal = bBacktest?.total_return_pct ?? -Infinity;
                            break;
                        case 'dailyReturn':
                            aVal = aBacktest?.daily_return_pct ?? -Infinity;
                            bVal = bBacktest?.daily_return_pct ?? -Infinity;
                            break;
                        case 'sharpe':
                            aVal = aBacktest?.sharpe_ratio ?? -Infinity;
                            bVal = bBacktest?.sharpe_ratio ?? -Infinity;
                            break;
                        case 'sortino':
                            aVal = aBacktest?.sortino_ratio ?? -Infinity;
                            bVal = bBacktest?.sortino_ratio ?? -Infinity;
                            break;
                        case 'calmar':
                            // Calculate Calmar: (Daily Return * 365) / |Max Drawdown|
                            const aCalmar = aBacktest?.daily_return_pct && aBacktest?.max_drawdown_pct
                                ? (aBacktest.daily_return_pct * 365) / Math.abs(aBacktest.max_drawdown_pct)
                                : -Infinity;
                            const bCalmar = bBacktest?.daily_return_pct && bBacktest?.max_drawdown_pct
                                ? (bBacktest.daily_return_pct * 365) / Math.abs(bBacktest.max_drawdown_pct)
                                : -Infinity;
                            aVal = aCalmar;
                            bVal = bCalmar;
                            break;
                        case 'winrate':
                            aVal = aBacktest?.win_rate ?? -Infinity;
                            bVal = bBacktest?.win_rate ?? -Infinity;
                            break;
                        case 'trades':
                            aVal = aBacktest?.trades_count ?? -Infinity;
                            bVal = bBacktest?.trades_count ?? -Infinity;
                            break;
                        default:
                            return 0;
                    }

                    return sortBy.direction === 'asc' ? aVal - bVal : bVal - aVal;
                });
            }

            setStrategies(strategies);
        } catch (error) {
            console.error("Failed to fetch strategies", error);
        } finally {
            setLoading(false);
        }
    }, [filters, sortBy]);

    useEffect(() => {
        fetchStrategies();
    }, [fetchStrategies]);

    const handleSort = (field: string) => {
        setSortBy(prev => {
            if (prev?.field === field) {
                return prev.direction === 'desc' ? { field, direction: 'asc' } : null;
            }
            return { field, direction: 'desc' };
        });
    };

    const handleReset = (e: React.MouseEvent, id: number) => {
        e.preventDefault();
        e.stopPropagation();
        setResetStrategyId(id);
    };

    const confirmReset = async () => {
        if (!resetStrategyId) return;
        setIsResetting(true);
        try {
            const res = await fetch(`/api/strategies/${resetStrategyId}/reset`, { method: 'POST' });
            if (res.ok) {
                fetchStrategies();
                setResetStrategyId(null);
            } else {
                const data = await res.json();
                alert(`Failed to reset: ${data.error || 'Unknown error'}`);
            }
        } catch (error) {
            console.error("Error resetting strategy:", error);
            alert("Failed to reset strategy due to network error");
        } finally {
            setIsResetting(false);
        }
    };

    const handleDelete = (e: React.MouseEvent, id: number) => {
        e.preventDefault();
        e.stopPropagation();
        setDeleteStrategyId(id);
    };

    const confirmDelete = async () => {
        if (!deleteStrategyId) return;
        setIsDeleting(true);
        try {
            const res = await fetch(`/api/strategies/${deleteStrategyId}`, { method: 'DELETE' });
            if (res.ok) {
                fetchStrategies();
                setDeleteStrategyId(null);
            } else {
                const data = await res.json();
                alert(`Failed to delete: ${data.error || 'Unknown error'}`);
            }
        } catch (error) {
            console.error("Error deleting strategy:", error);
            alert("Failed to delete strategy due to network error");
        } finally {
            setIsDeleting(false);
        }
    };

    return (
        <div className="space-y-6">
            {/* Stats */}
            <DashboardStats onFilterChange={(newFilters) => setFilters(prev => ({ ...prev, ...newFilters }))} />

            {/* Filters */}
            <Card>
                <CardHeader className="pb-3">
                    <div className="flex items-center justify-between">
                        <CardTitle className="text-lg flex items-center gap-2">
                            <Filter className="w-5 h-5" /> Filters
                        </CardTitle>
                        {(filters.status || filters.asset_type || filters.result || filters.searchTerm) && (
                            <button
                                onClick={() => setFilters({ status: "", asset_type: "", result: "", searchTerm: "" })}
                                className="text-xs px-2 py-1 bg-destructive/10 text-destructive rounded hover:bg-destructive/20"
                            >
                                Clear All
                            </button>
                        )}
                    </div>
                </CardHeader>
                <CardContent className="space-y-4">
                    {/* Search Input */}
                    <div className="relative">
                        <input
                            type="text"
                            placeholder="Search strategies..."
                            value={filters.searchTerm}
                            onChange={(e) => setFilters({ ...filters, searchTerm: e.target.value })}
                            className="w-full p-2 pl-8 border rounded bg-background text-sm"
                        />
                        <Filter className="w-4 h-4 absolute left-2 top-3 text-muted-foreground" />
                    </div>

                    {/* Active Filters Display */}
                    {(filters.status || filters.asset_type || filters.result || filters.searchTerm) && (
                        <div className="flex flex-wrap gap-2 text-xs">
                            {filters.searchTerm && (
                                <span className="bg-primary/10 px-2 py-1 rounded flex items-center gap-1">
                                    Running agents consume significant RAM. On a 16GB machine, it&apos;s recommended to keep total concurrency under 5-8 agents.
                                    The &quot;Smart&quot; model (Gemini 2.0 Flash) is used for coding, while lighter models handle research.
                                </span>
                            )}
                            {filters.status && (
                                <span className="bg-secondary px-2 py-1 rounded">
                                    Status: {filters.status}
                                </span>
                            )}
                            {filters.asset_type && (
                                <span className="bg-secondary px-2 py-1 rounded">
                                    Asset: {filters.asset_type}
                                </span>
                            )}
                            {filters.result && (
                                <span className="bg-secondary px-2 py-1 rounded">
                                    Result: {filters.result}
                                </span>
                            )}
                        </div>
                    )}

                    {/* Filter Dropdowns */}
                    <div className="flex gap-4 flex-wrap">
                        <select
                            className="p-2 border rounded bg-background flex-1 min-w-[150px]"
                            value={filters.status}
                            onChange={(e) => setFilters({ ...filters, status: e.target.value })}
                        >
                            <option value="">All Statuses</option>
                            <option value="COMPLETED">Completed</option>
                            <option value="FAILED">Failed</option>
                            <option value="backtesting">Backtesting</option>
                            <option value="researching">Researching</option>
                            <option value="REJECTED">Rejected</option>
                        </select>

                        <select
                            className="p-2 border rounded bg-background flex-1 min-w-[150px]"
                            value={filters.asset_type}
                            onChange={(e) => setFilters({ ...filters, asset_type: e.target.value })}
                        >
                            <option value="">All Assets</option>
                            <option value="crypto">Crypto</option>
                            <option value="stock">Stock</option>
                            <option value="index">Index</option>
                        </select>

                        <select
                            className="p-2 border rounded bg-background flex-1 min-w-[150px]"
                            value={filters.result}
                            onChange={(e) => setFilters({ ...filters, result: e.target.value })}
                        >
                            <option value="">All Outcomes</option>
                            <option value="PROFITABLE">Profitable</option>
                            <option value="UNPROFITABLE">Unprofitable</option>
                            <option value="CRASHED">Crashed</option>
                        </select>
                    </div>


                </CardContent>
            </Card>

            {/* Sortable Headers */}
            {strategies.length > 0 && (
                <div className="flex gap-2 text-xs text-muted-foreground items-center justify-end flex-wrap">
                    <span>Sort by:</span>
                    <button
                        onClick={() => handleSort('return')}
                        className={`px-2 py-1 rounded hover:bg-accent ${sortBy?.field === 'return' ? 'bg-accent font-semibold' : ''}`}
                    >
                        Return {sortBy?.field === 'return' && (sortBy.direction === 'desc' ? '↓' : '↑')}
                    </button>
                    <button
                        onClick={() => handleSort('dailyReturn')}
                        className={`px-2 py-1 rounded hover:bg-accent ${sortBy?.field === 'dailyReturn' ? 'bg-accent font-semibold' : ''}`}
                    >
                        Daily {sortBy?.field === 'dailyReturn' && (sortBy.direction === 'desc' ? '↓' : '↑')}
                    </button>
                    <button
                        onClick={() => handleSort('calmar')}
                        className={`px-2 py-1 rounded hover:bg-accent ${sortBy?.field === 'calmar' ? 'bg-accent font-semibold' : ''}`}
                    >
                        Calmar {sortBy?.field === 'calmar' && (sortBy.direction === 'desc' ? '↓' : '↑')}
                    </button>
                    <button
                        onClick={() => handleSort('sortino')}
                        className={`px-2 py-1 rounded hover:bg-accent ${sortBy?.field === 'sortino' ? 'bg-accent font-semibold' : ''}`}
                    >
                        Sortino {sortBy?.field === 'sortino' && (sortBy.direction === 'desc' ? '↓' : '↑')}
                    </button>
                    <button
                        onClick={() => handleSort('sharpe')}
                        className={`px-2 py-1 rounded hover:bg-accent ${sortBy?.field === 'sharpe' ? 'bg-accent font-semibold' : ''}`}
                    >
                        Sharpe {sortBy?.field === 'sharpe' && (sortBy.direction === 'desc' ? '↓' : '↑')}
                    </button>
                    <button
                        onClick={() => handleSort('winrate')}
                        className={`px-2 py-1 rounded hover:bg-accent ${sortBy?.field === 'winrate' ? 'bg-accent font-semibold' : ''}`}
                    >
                        Win Rate {sortBy?.field === 'winrate' && (sortBy.direction === 'desc' ? '↓' : '↑')}
                    </button>
                    <button
                        onClick={() => handleSort('trades')}
                        className={`px-2 py-1 rounded hover:bg-accent ${sortBy?.field === 'trades' ? 'bg-accent font-semibold' : ''}`}
                    >
                        Trades {sortBy?.field === 'trades' && (sortBy.direction === 'desc' ? '↓' : '↑')}
                    </button>
                </div>
            )}

            {/* Strategies List */}
            <div className="grid grid-cols-1 gap-4">
                {loading ? (
                    <div className="flex justify-center p-10"><Loader2 className="animate-spin" /></div>
                ) : strategies.length === 0 ? (
                    <div className="text-center p-10 text-muted-foreground">
                        No strategies found matching your filters{filters.searchTerm && ` or search term "${filters.searchTerm}"`}.
                    </div>
                ) : (
                    strategies.map((strat) => {
                        const hasBacktest = strat.backtests && strat.backtests.length > 0;

                        // Find the BEST backtest (highest Sharpe ratio), not the latest by date
                        let bestBacktest = null;
                        if (hasBacktest) {
                            bestBacktest = strat.backtests!.reduce((best, current) => {
                                if (!best) return current;

                                // 1. Priority: Profitability
                                const currentProfit = (current.total_return_pct || 0) > 0;
                                const bestProfit = (best.total_return_pct || 0) > 0;
                                if (currentProfit && !bestProfit) return current;
                                if (!currentProfit && bestProfit) return best;

                                // 2. Priority: Significant Trades (>5)
                                const currentSig = (current.trades_count || 0) >= 5;
                                const bestSig = (best.trades_count || 0) >= 5;
                                if (currentSig && !bestSig) return current;
                                if (!currentSig && bestSig) return best;

                                // 3. Priority: Sortino
                                const currentSortino = current.sortino_ratio ?? -Infinity;
                                const bestSortino = best.sortino_ratio ?? -Infinity;
                                if (currentSortino > bestSortino) return current;
                                if (currentSortino < bestSortino) return best;

                                // 4. Priority: Sharpe
                                const currentSharpe = current.sharpe_ratio ?? -Infinity;
                                const bestSharpe = best.sharpe_ratio ?? -Infinity;
                                if (currentSharpe > bestSharpe) return current;

                                // Fallback: Total Return
                                if ((current.total_return_pct || 0) > (best.total_return_pct || 0)) return current;

                                return best;
                            }, null);
                        }

                        return (
                            <Link href={`/strategies/${strat.id}`} key={strat.id} className="block transition-transform hover:scale-[1.01]">
                                <Card className="hover:bg-accent/5 transition-colors cursor-pointer border-transparent hover:border-border">
                                    <CardContent className="p-6 flex flex-col md:flex-row justify-between gap-4 items-start md:items-center">
                                        <div className="space-y-1">
                                            <div className="flex items-center gap-2">
                                                <h3 className="font-semibold text-lg">{strat.name}</h3>
                                                <StatusBadge status={strat.status} />
                                                {bestBacktest && (
                                                    <StatusBadge status={bestBacktest.result_rating || 'pending'} />
                                                )}
                                                <button
                                                    onClick={(e) => handleReset(e, strat.id)}
                                                    className="ml-2 p-1 text-muted-foreground hover:text-foreground hover:bg-destructive/10 hover:text-destructive rounded transition-all"
                                                    title="Reset Backtests & Status"
                                                >
                                                    <RotateCcw className="w-4 h-4" />
                                                </button>
                                                <button
                                                    onClick={(e) => handleDelete(e, strat.id)}
                                                    className="p-1 text-muted-foreground hover:text-red-500 hover:bg-red-500/10 rounded transition-all"
                                                    title="Delete Strategy"
                                                >
                                                    <Trash2 className="w-4 h-4" />
                                                </button>
                                            </div>
                                            <div className="text-sm text-muted-foreground flex gap-4">
                                                <span>{strat.asset_type}</span>
                                                <span>•</span>
                                                <span>{new Date(strat.created_at).toLocaleDateString()}</span>
                                                {bestBacktest && (
                                                    <>
                                                        <span>•</span>
                                                        <span className="font-mono text-xs bg-secondary px-1 py-0.5 rounded">Duration: {formatDuration(bestBacktest)}</span>
                                                    </>
                                                )}
                                            </div>
                                        </div>

                                        {bestBacktest && (
                                            <div className="grid grid-cols-4 gap-4 text-sm min-w-[300px]">
                                                <div className="flex flex-col">
                                                    <span className="text-muted-foreground text-xs">Return</span>
                                                    <span className={bestBacktest.total_return_pct > 0 ? "text-green-500 font-bold" : "text-red-500"}>
                                                        {formatPercentage(bestBacktest.total_return_pct)}
                                                    </span>
                                                </div>
                                                <div className="flex flex-col">
                                                    <span className="text-muted-foreground text-xs">Daily Return</span>
                                                    <span className={bestBacktest.daily_return_pct > 0 ? "text-green-500 font-bold" : "text-red-500"}>
                                                        {formatPercentage(bestBacktest.daily_return_pct)}
                                                    </span>
                                                </div>
                                                <div className="flex flex-col">
                                                    <span className="text-muted-foreground text-xs">Calmar</span>
                                                    <span className={(strat.best_calmar || 0) > 0 ? "text-green-500 font-bold" : "text-muted-foreground"}>
                                                        {strat.best_calmar ? strat.best_calmar.toFixed(3) : "-"}
                                                    </span>
                                                </div>
                                                <div className="flex flex-col">
                                                    <span className="text-muted-foreground text-xs">Sortino</span>
                                                    <span className={(strat.best_sortino || 0) > 0 ? "text-green-500 font-bold" : "text-muted-foreground"}>
                                                        {strat.best_sortino ? strat.best_sortino.toFixed(3) : "-"}
                                                    </span>
                                                </div>
                                                <div className="flex flex-col">
                                                    <span className="text-muted-foreground text-xs">Sharpe</span>
                                                    <span>{bestBacktest.sharpe_ratio?.toFixed(2) || "-"}</span>
                                                </div>
                                                <div className="flex flex-col">
                                                    <span className="text-muted-foreground text-xs">Win Rate</span>
                                                    <span>{formatPercentage(bestBacktest.win_rate)}</span>
                                                </div>
                                                <div className="flex flex-col">
                                                    <span className="text-muted-foreground text-xs">Max DD</span>
                                                    <span className="text-red-500">{formatPercentage(bestBacktest.max_drawdown_pct)}</span>
                                                </div>
                                                <div className="flex flex-col">
                                                    <span className="text-muted-foreground text-xs">Trades</span>
                                                    <span>{bestBacktest.trades_count || 0}</span>
                                                </div>
                                            </div>
                                        )}
                                    </CardContent>
                                </Card>
                            </Link>
                        );
                    })
                )}
            </div>

            <SimpleAlertDialog
                isOpen={!!resetStrategyId}
                onClose={() => setResetStrategyId(null)}
                onConfirm={confirmReset}
                title="Reset Strategy"
                description="Are you sure you want to reset this strategy? This will delete all backtests and return it to 'Ready for Code' state. This action cannot be undone."
                variant="destructive"
                confirmText="Reset Strategy"
                isLoading={isResetting}
            />

            <SimpleAlertDialog
                isOpen={!!deleteStrategyId}
                onClose={() => setDeleteStrategyId(null)}
                onConfirm={confirmDelete}
                title="Delete Strategy"
                description="Are you sure you want to permanently delete this strategy and all its backtests? This action cannot be undone."
                variant="destructive"
                confirmText="Delete Forever"
                isLoading={isDeleting}
            />
        </div>
    );
}
