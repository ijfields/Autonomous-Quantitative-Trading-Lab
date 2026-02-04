"use client";

import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { AlertTriangle, Clock, Zap, XCircle, AlertCircle } from "lucide-react";

interface AgentError {
    type: string;
    message: string;
    timestamp: string;
}

interface AgentInstance {
    id: number;
    type: 'backtest' | 'research';
    recentErrors?: AgentError[];
}

interface ErrorFeedProps {
    agents: {
        backtest: AgentInstance[];
        research: AgentInstance[];
    };
}

export default function ErrorFeed({ agents }: ErrorFeedProps) {
    // Aggregate all errors from all agents
    const allErrors: Array<AgentError & { agentId: number; agentType: string }> = [];

    // Collect errors from research agents
    for (const agent of agents.research || []) {
        for (const error of agent.recentErrors || []) {
            allErrors.push({
                ...error,
                agentId: agent.id,
                agentType: 'research'
            });
        }
    }

    // Collect errors from backtest agents
    for (const agent of agents.backtest || []) {
        for (const error of agent.recentErrors || []) {
            allErrors.push({
                ...error,
                agentId: agent.id,
                agentType: 'backtest'
            });
        }
    }

    // Sort by timestamp descending (most recent first)
    allErrors.sort((a, b) => new Date(b.timestamp).getTime() - new Date(a.timestamp).getTime());

    // Take only the last 10 errors
    const recentErrors = allErrors.slice(0, 10);

    // Get icon and color based on error type
    const getErrorStyle = (type: string) => {
        switch (type) {
            case 'rate_limit':
                return {
                    icon: <Zap className="w-3.5 h-3.5" />,
                    bg: 'bg-yellow-50',
                    border: 'border-yellow-200',
                    text: 'text-yellow-700',
                    label: 'Rate Limit'
                };
            case 'json_parse':
                return {
                    icon: <XCircle className="w-3.5 h-3.5" />,
                    bg: 'bg-orange-50',
                    border: 'border-orange-200',
                    text: 'text-orange-700',
                    label: 'Parse Error'
                };
            case 'system_error':
            case 'coder_error':
                return {
                    icon: <AlertTriangle className="w-3.5 h-3.5" />,
                    bg: 'bg-red-50',
                    border: 'border-red-200',
                    text: 'text-red-700',
                    label: 'System Error'
                };
            case 'db_error':
                return {
                    icon: <AlertCircle className="w-3.5 h-3.5" />,
                    bg: 'bg-red-50',
                    border: 'border-red-200',
                    text: 'text-red-700',
                    label: 'Database Error'
                };
            default:
                return {
                    icon: <AlertTriangle className="w-3.5 h-3.5" />,
                    bg: 'bg-gray-50',
                    border: 'border-gray-200',
                    text: 'text-gray-700',
                    label: type
                };
        }
    };

    // Format timestamp to relative time
    const formatTime = (timestamp: string) => {
        const date = new Date(timestamp);
        const now = new Date();
        const diffMs = now.getTime() - date.getTime();
        const diffMins = Math.floor(diffMs / 60000);

        if (diffMins < 1) return 'Just now';
        if (diffMins < 60) return `${diffMins}m ago`;
        if (diffMins < 1440) return `${Math.floor(diffMins / 60)}h ago`;
        return date.toLocaleString();
    };

    if (recentErrors.length === 0) {
        return null; // Don't render if no errors
    }

    return (
        <Card className="border-yellow-200 bg-yellow-50/30">
            <CardHeader className="py-3 border-b">
                <CardTitle className="text-sm font-medium flex items-center gap-2">
                    <AlertTriangle className="w-4 h-4 text-yellow-600" />
                    Recent Errors
                    <span className="text-xs text-muted-foreground font-normal">
                        ({recentErrors.length} in last session)
                    </span>
                </CardTitle>
            </CardHeader>
            <CardContent className="py-3">
                <div className="space-y-2 max-h-[200px] overflow-y-auto">
                    {recentErrors.map((error, idx) => {
                        const style = getErrorStyle(error.type);
                        return (
                            <div
                                key={`${error.agentType}-${error.agentId}-${idx}`}
                                className={`flex items-start gap-3 p-2 rounded border ${style.bg} ${style.border}`}
                            >
                                <div className={`shrink-0 mt-0.5 ${style.text}`}>
                                    {style.icon}
                                </div>
                                <div className="min-w-0 flex-1">
                                    <div className="flex items-center gap-2 mb-0.5">
                                        <span className={`text-[10px] font-semibold ${style.text}`}>
                                            {style.label}
                                        </span>
                                        <span className="text-[10px] text-muted-foreground">
                                            {error.agentType === 'research' ? 'Research' : 'Backtest'} #{error.agentId}
                                        </span>
                                        <span className="text-[10px] text-muted-foreground flex items-center gap-1 ml-auto">
                                            <Clock className="w-2.5 h-2.5" />
                                            {formatTime(error.timestamp)}
                                        </span>
                                    </div>
                                    <p className="text-[11px] text-gray-600 truncate" title={error.message}>
                                        {error.message}
                                    </p>
                                </div>
                            </div>
                        );
                    })}
                </div>
            </CardContent>
        </Card>
    );
}
