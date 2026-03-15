# Step-by-Step Guide: How I use AI to build 24/7 trading strategies +773.97% Profit (My exact workflow)

**Source:** Trade Tactics (YouTube)
**Video ID:** 870mvc3ZeEQ
**Upload Date:** 2026-03-15

---

## What This Guide Covers

A complete workflow for using Claude Opus to generate, stress-test, and progressively deploy algorithmic crypto trading strategies overnight, with emphasis on avoiding overfitting through Monte Carlo simulations and bootstrap stability testing.

---

## Step 1: Set Up the Backtesting Engine

1. Install Python with the **vectorbt** library (backtesting framework) and **ta-lib** (technical indicators).
2. Build or configure a custom backtesting dashboard that supports:
   - Multiple strategy comparisons
   - Monte Carlo simulations (randomized candlestick sequences)
   - Bootstrap stability testing
   - In-sample vs out-of-sample data splitting
3. Grant Claude Code / Claude Opus access to this engine so it can run backtests autonomously.

---

## Step 2: Create a Baseline Strategy

1. Define a basic strategy configuration (entry rules, indicator parameters).
2. Run it on your training data to establish baseline metrics:
   - Sharpe ratio (volatility-adjusted risk-to-reward)
   - Sortino ratio
   - Win rate
   - Maximum drawdown
3. Example baseline: Sharpe 0.59, Win rate 43%.
4. This baseline is what Claude will try to beat.

---

## Step 3: Run Claude Overnight to Generate Variants

1. Open Claude Code in Visual Studio Code.
2. Instruct Claude to:
   - Try to beat the previous best strategy
   - Add/modify exit rules, chop filters, and indicator parameters
   - Compare results across variants
3. Let it run for 8-10 hours. Claude can generate 20-50+ completely different strategies overnight.
4. Each variant is a "stack" of trading rules that Claude builds iteratively.
5. Example result: Improved from Sharpe 0.59 to 1.31, drawdown from 21% to 15%, win rate from 43% to 64%.

---

## Step 4: Run Monte Carlo / Bootstrap Stress Tests

1. For each promising strategy variant, run thousands of Monte Carlo simulations:
   - Download the price data
   - Randomize (jumble) the candlestick order
   - Run the strategy on each randomized dataset
2. This tests whether the strategy is flexible enough to handle random price patterns, not just the one historical sequence.
3. Calculate **bootstrap stability scores**: in the worst 5% of simulations, how badly does the strategy perform?
4. Select for the highest Monte Carlo Sharpe ratio and highest bootstrap stability.
5. Discard strategies where randomized data causes catastrophic failure -- these are overfit.

---

## Step 5: Validate on Out-of-Sample Data

1. Withhold a portion of your price data (the "testing set") that Claude never sees during strategy generation.
2. Run each candidate strategy on this out-of-sample data.
3. Compare metrics between in-sample and out-of-sample:
   - Some degradation is expected and normal
   - Large drops in Sharpe, win rate, or dramatic increases in drawdown indicate overfitting
4. Example: A strategy with Sharpe 1.31 in-sample that drops to 0.62 out-of-sample may still be acceptable if the equity curve remains positive.

---

## Step 6: Test Across Multiple Instruments

1. Run the best strategies on different coins: Solana, Bitcoin, Ethereum.
2. Check if metrics hold across instruments:
   - If win rate drops significantly on other coins, the strategy may be overfit to one asset
   - A strategy that works on multiple coins is more generalized and trustworthy
3. Example observation: Solana strategy performed well on ETH (Sortino 23.7 in-sample) but win rates declined out-of-sample, suggesting Solana-specific optimization.

---

## Step 7: Deploy Progressively with Trust-Building

1. Connect the bot to a platform like Signal Swap using the "Create Bot" feature.
2. Start with paper trading or very small amounts ($25-$50-$100).
3. Monitor real forward performance over days/weeks.
4. Only increase allocation after the bot demonstrates consistent profitability with real signals.
5. If the strategy performs well on Signal Swap, you can publish it to the marketplace (developers receive 70% of subscriber revenue).

---

## Step 8: Iterate and Maintain

1. Continue generating new strategy variants with Claude and running stress tests.
2. Build a tree of all possible configurations across parameter sets and instruments.
3. Weight parameter sets by stability: some may be more robust in bootstrapping than others.
4. Add improvements over time: chop filters (turn off trading in choppy markets), sleep conditions, refined exit rules.
5. Monitor for degradation: if a live bot's performance starts declining, it may need recalibration or replacement.

---

## Key Takeaway

> "You want to raise the floor basically of how bad your bot could perform... If you don't do this, and I want to be firm here, there are a lot of people putting money into these bots and they're not doing this. And it's 100% overfit." The methodology is: generate many candidates with Claude, stress-test ruthlessly with Monte Carlo and bootstrap, validate on unseen data, deploy small, scale only with earned trust.

*Guide derived from: How I use AI to build 24/7 trading strategies +773.97% Profit (My exact workflow).txt*
