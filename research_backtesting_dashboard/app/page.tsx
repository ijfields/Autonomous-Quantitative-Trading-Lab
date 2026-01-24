import DashboardClient from "@/components/DashboardClient";
import PerformanceCharts from "@/components/PerformanceCharts";
import { Activity, Database, TrendingUp, AlertTriangle } from "lucide-react";


export default function Home() {
  return (
    <main className="min-h-screen bg-background p-8">
      <div className="max-w-7xl mx-auto space-y-8">
        <div className="flex justify-between items-center">
          <div>
            <h1 className="text-4xl font-bold tracking-tight">Research Dashboard</h1>
            <p className="text-muted-foreground mt-2">Agentic Backtesting Workflow V2</p>
          </div>
          <div className="flex items-center gap-2">
            <div className="h-2 w-2 rounded-full bg-green-500 animate-pulse"></div>
            <span className="text-sm font-medium">System Online</span>
          </div>
        </div>

        {/* Stats Section - Could be server rendered or client. Let's make it part of DashboardClient for single fetch or separate */}
        {/* I'll let DashboardClient handle it or create a DashboardStats component. 
            For now, let's keep it simple: DashboardClient covers the list. 
            I'll add the stats cards to DashboardClient or pass them in?
            Let's keep Home simple wrappers.
        */}

        <DashboardClient />
      </div>
    </main>
  );
}
