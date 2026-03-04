# Step-by-Step Guide: Build a Local Backtesting Engine with Claude Code + VectorBT

**Source:** Trade Tactics (YouTube)
**Video ID:** PGpGvR3NT74
**Upload Date:** 2026-02-28

---

## What This Guide Covers

How to use Claude Code (Opus 4.6) to build a complete local backtesting pipeline from scratch: downloading price data, splitting into training/testing sets, calculating indicators, running backtests via VectorBT, and displaying results in a dashboard. The entire system is built with minimal manual coding -- Claude does the heavy lifting.

---

## Prerequisites

- **Visual Studio Code** installed (or Cursor / AntiGravity)
- **Claude Code** installed (via Anthropic docs -- `npm install -g @anthropic-ai/claude-code` or equivalent)
- **Python** installed with pip
- **Anthropic Max plan** (for Claude Opus 4.6)
- Optional: **Droid** wrapper for enhanced system prompts (available on Terminal Bench)

---

## Step 1: Set Up Your Project Folder

1. Create a new empty folder for your backtesting project
2. Open VS Code → open terminal (Ctrl + `)
3. Navigate to your folder: `cd /path/to/your/folder`
4. Launch Claude Code: type `claude` and press Enter
5. Optional: use `droid` instead for the Droid wrapper with enhanced system prompts

---

## Step 2: Build the CLAUDE.md System Prompt

1. Run `/init` in Claude Code to create the CLAUDE.md file
2. Or write a detailed initial prompt defining your pipeline:
   - **Step 1:** Download price data (source: Binance for crypto, Interactive Brokers for stocks/forex/gold)
   - **Step 2:** Split into in-sample (training ~60%) and out-of-sample (testing)
   - **Step 3:** Calculate indicators (using TA-lib for standard indicators)
   - **Step 4:** Run backtests through VectorBT
   - **Step 5:** Display results in a dashboard
   - **Step 6:** Test and debug until working
3. The CLAUDE.md file is sent with every prompt, giving Claude persistent project context

---

## Step 3: Let Claude Build the Framework

With one well-crafted prompt, Claude Opus 4.6 will:

1. **Explore the codebase** (empty at this point)
2. **Build the system prompt / project structure**
3. **Create the data fetcher**: Downloads OHLCV data from the exchange, stores as CSV
4. **Implement smart incremental fetching**: Only downloads new data since last run
5. **Build indicator calculations**: TA-lib for EMA, RSI, MACD, ATR, etc.
6. **Set up VectorBT backtesting engine**: Signal generation → backtest execution → metrics
7. **Create the dashboard**: Equity curve, drawdown graph, top 3 parameter sets, strategy selector

Let Claude run -- it will install dependencies, create files, and debug errors automatically.

---

## Step 4: Optimize for Performance

Ask Claude to:

1. **Use all CPU cores** for parallel backtesting (multi-threading)
2. **Cache downloaded data** so it doesn't re-fetch from disk every run
3. **Rewrite the backtester** for efficiency -- VectorBT is fast but can be optimized further
4. **Set up performance monitoring** (optional): measure where time is spent, identify bottlenecks

**Performance expectation:** Up to 1,000 parameter combinations per second locally vs. 15-20 seconds per run on TradingView for 700K+ candles.

---

## Step 5: Data Splitting for Robustness

1. **In-sample (training):** ~60% of data -- Claude optimizes parameters on this
2. **Out-of-sample (testing):** ~30% -- Claude validates on this
3. **Human-only holdout (optional):** ~10% -- Claude **never sees this data**. You run the final verification manually to eliminate AI look-ahead bias.

**Key principle:** Every time you run a deep backtest, you're showing all the data at once. Splitting prevents overfitting.

---

## Step 6: Set Correct Optimization Targets

Tell Claude:
- **Do NOT maximize net profit** -- this leads to overfitting
- **Minimize max drawdown first** -- survival is more important than returns
- **Maximize Sharpe ratio** -- it factors in both upside and downside risk
- **Reject any parameter combo** that performs well in-sample but fails out-of-sample

---

## Step 7: Add Robustness Testing (Advanced)

Ask Claude to add:

1. **Monte Carlo simulations**: Randomize/jumble candlestick order, rerun backtests
2. **Bootstrapping**: Resample data with replacement
3. **Noise injection**: Add artificial chop / low-volatility periods
4. **Multi-period testing**: Test on specific market regimes (2017 crash, 2020 cycle, 2022 bear market)
5. **Sleep detection**: Algorithm should auto-detect low-volatility/choppy periods and stop trading

Goal: Find the most flexible parameter set that handles ANY market condition with acceptable drawdown.

---

## Step 8: Deploy for Live Trading (Optional)

### Option A: TradingView Webhooks
1. Ask Claude to translate the Python strategy to PineScript
2. Paste PineScript into TradingView's Pine Editor
3. Set up alerts with webhook URL
4. 99.9% uptime via TradingView's servers

### Option B: SignalSwap.io
1. Create a bot on SignalSwap.io
2. Connect your exchange (Bybit, Apex, Pinex)
3. Copy the webhook URL
4. Ask Claude to send signals to the webhook from Python

### Option C: Local Python Execution
1. Ask Claude to set up direct exchange connectivity (CCXT or exchange API)
2. Run the strategy locally
3. **Warning:** Signals only work when your machine is on and connected. Risk of missed signals, lag, slippage.

---

## Step 9: Iterate and Enhance

From the dashboard, you can now:
1. Ask Claude to **build more complex strategies** (combine indicators, add filters)
2. **Copy TradingView indicators**: Paste any PineScript indicator and ask Claude to translate to Python
3. **Stack strategies**: Run multiple strategies simultaneously
4. **Set benchmarks**: Define minimum Sharpe ratio and max drawdown -- Claude loops until benchmarks are met
5. **Let Claude run overnight**: It can test thousands of parameter combinations while you sleep

---

## Quick Reference: Pipeline Flow

```
1. Data Fetching (Binance / IB / CCXT)
        ↓
2. Data Splitting (in-sample / out-of-sample / human holdout)
        ↓
3. Indicator Calculations (TA-lib + custom)
        ↓
4. Signal Generation (entry/exit logic)
        ↓
5. In-Sample Backtest (VectorBT)
        ↓
6. Pass/Fail Metrics Check (Sharpe, drawdown)
        ↓
7. Out-of-Sample Validation
        ↓
8. Dashboard (top performers displayed)
        ↓
9. [Optional] Monte Carlo / Robustness Testing
        ↓
10. [Optional] Live Deployment (PineScript / webhook)
```

---

## Key Metrics to Monitor

| Metric | Target |
|--------|--------|
| Max Drawdown | As low as possible (< 20% ideal) |
| Sharpe Ratio | > 1.0 (higher is better) |
| Net Profit | Secondary to Sharpe and drawdown |
| In-Sample vs Out-of-Sample Consistency | Results should be similar (no overfitting) |
| Monte Carlo Worst Case | Should still be acceptable |

*Guide derived from: Step-By-Step Using Claude Code to Auto-Generate & Backtest Trading Strategies (Secret Easy Method).txt*
