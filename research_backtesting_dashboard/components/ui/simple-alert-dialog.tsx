import React from 'react';
import { AlertTriangle, X } from 'lucide-react';

interface SimpleAlertDialogProps {
    isOpen: boolean;
    onClose: () => void;
    onConfirm: () => void;
    title: string;
    description: string;
    confirmText?: string;
    cancelText?: string;
    isLoading?: boolean;
    variant?: 'default' | 'destructive';
}

export function SimpleAlertDialog({
    isOpen,
    onClose,
    onConfirm,
    title,
    description,
    confirmText = "Confirm",
    cancelText = "Cancel",
    isLoading = false,
    variant = 'default'
}: SimpleAlertDialogProps) {
    if (!isOpen) return null;

    return (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/50 backdrop-blur-sm animate-in fade-in duration-200">
            <div className="bg-background border rounded-lg shadow-lg w-full max-w-md mx-4 p-6 space-y-4 animate-in zoom-in-95 duration-200">
                <div className="flex flex-col space-y-2 text-center sm:text-left">
                    <div className="flex items-center gap-2 font-semibold text-lg">
                        {variant === 'destructive' && <AlertTriangle className="w-5 h-5 text-red-500" />}
                        {title}
                    </div>
                    <p className="text-sm text-muted-foreground">
                        {description}
                    </p>
                </div>

                <div className="flex flex-col-reverse sm:flex-row sm:justify-end gap-2">
                    <button
                        onClick={onClose}
                        disabled={isLoading}
                        className="px-4 py-2 text-sm font-medium border rounded-md hover:bg-accent transition-colors disabled:opacity-50"
                    >
                        {cancelText}
                    </button>
                    <button
                        onClick={onConfirm}
                        disabled={isLoading}
                        className={`px-4 py-2 text-sm font-medium rounded-md text-white transition-colors disabled:opacity-50 flex items-center justify-center gap-2 ${variant === 'destructive'
                            ? 'bg-red-600 hover:bg-red-700'
                            : 'bg-primary hover:bg-primary/90'
                            }`}
                    >
                        {isLoading && <div className="w-4 h-4 border-2 border-white/30 border-t-white rounded-full animate-spin" />}
                        {confirmText}
                    </button>
                </div>
            </div>
        </div>
    );
}
