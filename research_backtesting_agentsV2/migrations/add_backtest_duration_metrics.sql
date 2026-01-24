-- Migration: Add backtest duration metrics
-- Created: 2026-01-17
-- Purpose: Add temporal context to backtest results for proper return interpretation

ALTER TABLE backtestresult 
ADD COLUMN IF NOT EXISTS backtest_period_days INTEGER,
ADD COLUMN IF NOT EXISTS daily_return_pct NUMERIC,
ADD COLUMN IF NOT EXISTS weekly_return_pct NUMERIC,
ADD COLUMN IF NOT EXISTS annualized_return_pct NUMERIC;

-- Add helpful comments
COMMENT ON COLUMN backtestresult.backtest_period_days IS 'Duration of backtest in days';
COMMENT ON COLUMN backtestresult.daily_return_pct IS 'Average daily return (total_return / days)';
COMMENT ON COLUMN backtestresult.weekly_return_pct IS 'Average weekly return (total_return / weeks)';
COMMENT ON COLUMN backtestresult.annualized_return_pct IS 'Annualized return (total_return * 365 / days)';
