# Step-by-Step Guide: Lumibot Backtesting Speed Optimization

**Source:** Lumiwealth / Moon Dev (YouTube)
**Video ID:** QfA65W5-abs
**Upload Date:** 2026-02-27

---

## What This Guide Covers

How to optimize Lumibot backtesting speed from ~40 minutes per week of data down to seconds-level performance, using AI-assisted parameter tuning and documented speed improvement techniques.

---

## Prerequisites

- Lumibot installed and configured
- Existing strategy code (e.g., mean reversion / Z-score based)
- Interactive Brokers account (for futures data)
- Lumibot docs folder with speed improvement documentation

---

## Step 1: Read Speed Improvement Documentation

1. Navigate to your Lumibot docs folder
2. Find the speed improvement guide/document
3. Follow all listed optimization instructions before making custom changes

---

## Step 2: Use Continuous Contracts for Futures

- Continuous contracts backtest significantly faster than individual contract selection
- Switch from contract-by-contract picking to continuous futures contracts where possible

---

## Step 3: Tune Strategy Parameters for Speed

| Parameter | Change | Effect |
|-----------|--------|--------|
| Z-score lookback | Reduce to 10 periods | Faster reaction to price swings |
| Spread threshold | Lower entry threshold | More "scalpy" — enters trades earlier |
| Check-in cadence | Keep at 15 minutes | Steady execution rhythm |

---

## Step 4: Prioritize Data Optimization

1. **Futures:** Target 10-30x improvement with seconds-level data
2. **Crypto:** Ensure seconds-level data works and is fast
3. **Forex:** Lower priority; Interactive Brokers doesn't support forex backtesting

---

## Step 5: Check Logs After Backtests

- If no trades triggered, check logs to understand why
- Logs CSV is only generated after backtest completes
- Review entry/exit conditions and data availability

---

## Key Insight

> Use AI voice prompting to rapidly iterate: describe what you want changed, let AI modify the code, re-run the backtest. This turns a manual coding cycle into a conversation.

*Guide derived from: AI Trading Bot： MASSIVE Speed Boost for Backtesting! #shorts.txt*
