# Step-by-Step Guide: Walk-Forward Backtesting with Claude Code

**Source:** AI Pathways (YouTube)
**Video ID:** lIMu8ysJW68
**Upload Date:** 2026-03-08

---

## What This Guide Covers

How to use Claude Code to build an institutional-grade walk-forward backtesting engine that exposes curve fitting and produces honest performance metrics.

---

## Prerequisites

- VS Code with Claude Code extension installed
- Python environment (Claude Code handles dependency installation)

---

## Step 1: Prompt Claude Code to Build the Engine

Provide a detailed specification:
```
Build a professional walk-forward trading app in Python using Streamlit, Plotly, and Yahoo Finance.
- Asset: SPY, date range January 2018 to present
- Strategy: RSI crossover (to be upgraded later)
- Walk-forward engine: 12-month rolling training window, 3-month blind test window
- Evaluation: stitch only the out-of-sample returns
- Risk management: include 0.1% exchange fee and slippage
- UI: fold-by-fold progress, best parameters per fold, traditional vs walk-forward equity curves
```

---

## Step 2: Understand the Walk-Forward Folds

For each fold:
1. **Training (12 months):** Optimizer searches parameter combinations, targeting lowest max drawdown + highest Sharpe ratio
2. **Blind test (3 months):** Best parameters locked and applied to completely unseen data
3. **Advance:** Window moves forward by 3 months, repeat

For 2018–2024: produces **19 folds** total.

---

## Step 3: Read the Dashboard

| Metric | What It Tells You |
|--------|-------------------|
| **Traditional backtest return** | The inflated, curve-fit number |
| **Walk-forward return** | The honest, stitched OOS number |
| **Return degradation** | % of traditional return that was fake |
| **Best parameters per fold** | If parameters vary wildly between folds, the edge may be unstable |

---

## Step 4: Avoid Look-Ahead Bias

**Critical for signal processing filters:**
- `filtfilt` (scipy default) applies filter bidirectionally — **uses future prices**
- `lfilter` applies forward-only — **no future data leaks**
- Explicitly instruct Claude Code: "Use lfilter, NOT filtfilt"

---

## Step 5: Iterate Strategy Hypotheses

1. Run walk-forward on initial strategy (e.g., RSI crossover)
2. Observe reality check (likely 75%+ return degradation)
3. Prompt Claude Code to swap in new strategy (e.g., ATR + Butterworth)
4. Re-run walk-forward
5. Compare degradation across strategies
6. Repeat until you find a strategy with minimal degradation

---

## Step 6: Validate Surviving Strategies

For strategies showing genuine walk-forward performance:
- Test on different assets (cross-asset robustness)
- Test on different timeframes
- Add regime filters to remove bad market conditions
- Implement dynamic position sizing

---

## Key Takeaway

> Traditional backtests are fantasy — 75%+ of the return is typically curve fitting. Walk-forward analysis with 12-month train / 3-month blind test folds produces honest metrics. Use Claude Code to build the engine in minutes, always include transaction costs (0.1%+), and use `lfilter` not `filtfilt` to prevent look-ahead bias.

*Guide derived from: How To Backtest Properly With Claude Code (MUST WATCH).txt*
