# Step-By-Step Using Claude Code to Auto-Generate & Backtest Trading Strategies - Complete Transcript Analysis

**Video Title:** Step-By-Step Using Claude Code to Auto-Generate & Backtest Trading Strategies (Secret Easy Method)
**Channel:** Trade Tactics
**Video ID:** PGpGvR3NT74
**Upload Date:** 2026-02-28
**Duration:** ~27m43s
**Speaker:** Unidentified host of Trade Tactics channel
**Platform:** YouTube

---

## EXECUTIVE SUMMARY

A step-by-step tutorial on using Claude Code (Opus 4.6, with optional "Droid" system prompt wrapper) to build a complete local backtesting engine from scratch using Python and VectorBT. The speaker walks through the entire pipeline: downloading price data (Binance/crypto, with Interactive Brokers mentioned for stocks/forex/gold), splitting into in-sample and out-of-sample sets, calculating indicators locally (TA-lib), running backtests through VectorBT, and displaying results in a dashboard. A simple EMA crossover is used as the demonstration strategy. The speaker emphasizes local execution speed (up to 1,000 parameter combinations per second vs. TradingView's slow server-side processing), robustness testing via Monte Carlo/bootstrapping simulations, and the importance of minimizing drawdown and Sharpe ratio over maximizing net profit. Live trading deployment is briefly covered via PineScript translation + TradingView webhooks or SignalSwap.io.

No specific trading strategies are presented -- this is a framework/infrastructure tutorial. The EMA crossover used is explicitly a baseline test, not a recommended strategy.

---

## KEY TOPICS

### 1. Development Environment Setup
- **Visual Studio Code** as the IDE (alternatives: Cursor, AntiGravity)
- **Claude Code** installed via Anthropic documentation (Windows + Mac)
- **Droid** wrapper (optional): injects enhanced system prompts for Claude Opus 4.6, ranked on Terminal Bench at 69.9%
- Claude Opus 4.6 can spawn sub-agents working in parallel
- Multiple terminals (Ctrl+Shift+5) for parallel Claude instances

### 2. CLAUDE.md System Prompt
- `/init` command creates the system prompt file
- Sent with every prompt to give Claude project context
- Crucial for project understanding across sessions
- Speaker builds a custom CLAUDE.md defining the full pipeline structure

### 3. Backtesting Pipeline (6 Steps)
1. **Data Fetching**: Download price data from exchange (Binance for crypto, Interactive Brokers for stocks/forex/gold). Smart incremental CSV fetching (only downloads new data since last run).
2. **Data Splitting**: In-sample (training, ~60%) and out-of-sample (testing). Can further split into a third "human-only" validation set that Claude never sees -- eliminates AI look-ahead bias.
3. **Indicator Calculation**: All indicators built locally in Python (TA-lib for standard ones like EMA/ATR/RSI/MACD; custom logic for complex indicators). No reliance on TradingView's server-side calculations.
4. **Signal Generation**: Plug indicators through the trading logic pipeline to generate buy/sell signals.
5. **In-Sample Backtesting**: Run parameter optimization. Pass/fail based on metrics (Sharpe ratio, max drawdown).
6. **Out-of-Sample Validation**: Final verification on unseen data. Only strategies that pass both stages go to the dashboard.

### 4. VectorBT Engine
- Python backtesting library, significantly faster than BackTrader
- Speaker's own custom engine is "a little bit faster than VectorBT" but for tutorials VectorBT works fine
- Can process ~700-800K candles (10-min ETH chart) in 15-20 seconds locally vs. much longer on TradingView
- CPU-bound (not GPU) -- multi-threading recommended
- Up to 1,000 parameter combinations per second with optimization

### 5. Dashboard Output
- Top 3 winning parameter sets displayed with full metrics
- Equity graph + drawdown graph
- Strategy selector dropdown
- Built by Claude Opus in essentially one prompt (with minor direction)
- Metrics shown: net profit, max drawdown, Sharpe ratio

### 6. Robustness Testing (Mentioned, Not Built in Tutorial)
- **Monte Carlo simulations**: Randomize/jumble candlestick order
- **Bootstrapping**: Resample data with replacement
- **Noise injection**: Add chop/low-volatility periods to stress test
- **Multi-period splitting**: Test on 2017 dump, 2020 cycle, etc. separately
- Goal: find the most flexible parameter set that handles any market condition

### 7. Live Trading Deployment
- **PineScript translation**: Ask Claude to convert Python strategy to PineScript
- **TradingView alerts**: Paste PineScript, set up webhook alerts
- **SignalSwap.io**: The speaker's platform -- paste webhook URL, connect exchange (Bybit, Apex, Pinex)
- **Local execution**: Possible but risky (requires machine to be on 24/7, potential slippage)
- TradingView has 99.9% uptime vs. local machine risks

### 8. Key Optimization Advice
- **Never maximize net profit alone** -- minimize drawdown first, then maximize Sharpe ratio
- Sharpe ratio factors in both downside risk and upside
- Use all CPU cores for parallel processing
- Cache data to avoid redundant disk reads
- Withhold data from Claude to prevent AI look-ahead bias

---

## TOOLS & PLATFORMS MENTIONED

| Tool | Purpose |
|------|---------|
| Claude Code (Opus 4.6) | AI agent for building the entire system |
| Droid | System prompt wrapper for enhanced Claude behavior |
| Visual Studio Code | IDE / terminal |
| VectorBT | Python backtesting engine |
| TA-lib | Python indicator library (EMA, RSI, MACD, ATR, etc.) |
| TradingView | Chart visualization, PineScript, webhook alerts |
| Binance | Crypto price data source |
| Interactive Brokers | Stocks/forex/gold price data (Global API) |
| SignalSwap.io | Webhook-based live trading platform (speaker's product) |
| Trade Tactics Discord | Free community for trading bot builders |

---

## ACTIONABLE TAKEAWAYS

1. **One-prompt Claude Code setup**: A single well-crafted prompt to Claude Opus 4.6 can scaffold an entire backtesting pipeline (data fetching → indicators → engine → dashboard)
2. **Local > TradingView for speed**: Local Python + VectorBT processes 700K+ candles in seconds vs. minutes on TradingView
3. **In-sample/out-of-sample split is essential**: 60% training, reserve testing data, optionally withhold a third "human-only" set from Claude
4. **Minimize drawdown, not maximize profit**: Sharpe ratio is the target metric
5. **Monte Carlo + bootstrapping** add robustness testing (not covered in detail but recommended as next step)
6. **Multiple Claude instances in parallel** (Ctrl+Shift+5 for new terminals) can work on different parts of the codebase simultaneously
7. **CLAUDE.md is crucial** -- use `/init` to create project context that persists across sessions

*Analyzed from: Step-By-Step Using Claude Code to Auto-Generate & Backtest Trading Strategies (Secret Easy Method).txt*
