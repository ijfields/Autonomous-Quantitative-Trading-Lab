import { type ClassValue, clsx } from "clsx";
import { twMerge } from "tailwind-merge";

export function cn(...inputs: ClassValue[]) {
    return twMerge(clsx(inputs));
}

// eslint-disable-next-line @typescript-eslint/no-explicit-any
export function formatDuration(params: any): string {
    if (!params) return "N/A";

    // Check for backtest_period_days (from backtest result)
    if (params.backtest_period_days) return `${params.backtest_period_days} Days`;

    // Check for explicit 'days'
    if (params.days) return `${params.days} Days`;

    // Check for start/end dates
    if (params.start_date && params.end_date) {
        const start = new Date(params.start_date);
        const end = new Date(params.end_date);
        const diffTime = Math.abs(end.getTime() - start.getTime());
        const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
        return `${diffDays} Days`;
    }

    return "Unknown";
}

export function formatCurrency(value: number | undefined | null) {
    if (value === undefined || value === null) return "-";
    return new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: 'USD',
    }).format(value);
}

export function formatPercentage(value: number | undefined | null) {
    if (value === undefined || value === null) return "-";
    return `${value.toFixed(2)}%`;
}
