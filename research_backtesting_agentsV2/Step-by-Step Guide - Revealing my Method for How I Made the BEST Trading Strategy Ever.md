# Step-by-Step Guide: AI-Driven Overnight Strategy Discovery with 3-Tier Validation

**Source:** Trade Tactics (YouTube)
**Video ID:** 5LIoxuqNNsM
**Upload Date:** 2026-03-11

---

## What This Guide Covers

How to use Claude Opus + a Python trading engine to autonomously generate, test, and rank trading strategies overnight using a rigorous 3-tier walk-forward validation methodology.

---

## Prerequisites

- Python environment with backtesting libraries
- Claude Opus API access (or similar LLM)
- Historical price data (OHLCV) for target asset

---

## Step 1: Set Up the 3-Tier Data Split

| Tier | Range | Visibility | Purpose |
|------|-------|-----------|---------|
| **Training** | First ~60% of data | Engine + Claude | Parameter optimization |
| **Testing** | Next ~25% of data | Claude only (engine blind) | Strategy ranking |
| **True OOS** | Final ~15% of data | Human only (both AI blind) | Final unbiased confirmation |

Example for SOL 1H data (2020–2026):
- Training: 2020 – Feb 2023
- Testing: 2023 – Mar 2025
- True OOS: Mar 2025 – present

---

## Step 2: Configure Optimization Targets

Optimize for (in order of priority):
1. **Lowest max drawdown** — prevents selecting fragile strategies
2. **Highest Sharpe ratio** — rewards risk-adjusted returns

**NOT net profit** — this prevents the engine from selecting volatile outlier strategies.

---

## Step 3: Run Overnight Strategy Generation

1. Give Claude access to the training data
2. Instruct it to generate and test ~25 distinct strategy hypotheses
3. Each strategy is optimized on the training window
4. Claude ranks the top 5 using the testing window (which the engine cannot see)
5. Let this run overnight

---

## Step 4: Validate Top 5 on True Out-of-Sample

For each of the top 5 strategies:
1. Lock all parameters from the training phase
2. Apply unchanged to the true OOS data (Mar 2025 – present)
3. **Only you review this** — neither Claude nor the engine has seen this data
4. Check: Sharpe ratio, max drawdown, consistency, single-trade dependence

### Red Flags to Reject

- Max drawdown > 40%
- Most profit from a single trade (concentration risk)
- Win rate collapsed vs. training
- Sharpe ratio dropped by more than 50%

---

## Step 5: Additional Robustness Checks

### Bootstrapping
- Randomize/jumble candle order
- Re-run strategy on randomized data
- If performance holds, the edge is genuine (not pattern memorization)

### Cross-Asset Testing
- Run the winning strategy on other instruments
- Strategies that work across assets decay more slowly

### Cross-Timeframe Testing
- Test on adjacent timeframes (e.g., 30-min if developed on 1H)

---

## Step 6: Iterate and Improve

- Add **regime filters** to remove bad market conditions
- Implement **dynamic take-profit** levels
- Convert to MT5 or PineScript for live execution
- Continue monitoring for alpha decay

---

## Key Takeaway

> The 3-tier validation methodology (training → AI testing → human-only true OOS) is the most important contribution. It removes both engine overfitting AND AI selection bias. Any strategy surviving all three tiers with <15% max drawdown and >1.0 Sharpe is a genuine candidate. Optimize for drawdown and Sharpe, never profit alone.

*Guide derived from: Revealing my Method for How I Made the BEST Trading Strategy Ever. (Easy to Copy).txt*
