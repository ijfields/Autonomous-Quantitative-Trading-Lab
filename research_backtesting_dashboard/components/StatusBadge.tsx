import { Badge } from "@/components/ui/badge";

export function StatusBadge({ status }: { status: string }) {
    if (!status) return <Badge variant="outline">Unknown</Badge>;

    const map: Record<string, "default" | "secondary" | "destructive" | "outline" | "success" | "warning" | "info"> = {
        "completed": "success",
        "failed": "destructive",
        "archived": "secondary",
        "researching": "info",
        "coding": "info",
        "scouted": "outline",
        "backtesting": "warning",
        "profitable": "success",
        "marginal": "warning",       // NEW: Yellow badge for weak-but-positive strategies
        "unprofitable": "destructive",
        "crashed": "destructive",
        "pending": "secondary",
    };

    const variant = map[status.toLowerCase()] || "default";

    return <Badge variant={variant} className="capitalize">{status.replace(/_/g, " ")}</Badge>;
}
