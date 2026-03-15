# Step-by-Step Guide: Backtesting an Opening Range Breakout + FVG Strategy

**Source:** LuxAlgo (YouTube)
**Video ID:** wqgAwEO2oi0
**Upload Date:** 2025-03-14

---

## What This Guide Covers

How to build, backtest, and evaluate an Opening Range Breakout + Fair Value Gap strategy using AI-powered PineScript generation — and why this particular strategy fails in isolation.

---

## Step 1: Define the Opening Range

1. Open TradingView on the 1-minute chart for your target instrument (video uses GBP/JPY)
2. At 9:30 AM EST, mark the high and low of the first 5-minute candle
3. This defines the "opening range" — the breakout zone

---

## Step 2: Identify the Fair Value Gap (FVG)

1. Wait for a candle to break through the opening range high or low
2. An FVG forms when the body of the breakout candle leaves a gap between the high of candle 1 and the low of candle 3 (in a 3-candle sequence)
3. The FVG must form through the range level to be valid

---

## Step 3: Enter the Trade

1. After the FVG forms through the opening range level, wait for price to retest the FVG zone
2. Enter on the next candle after the retest
3. Maximum wait: 20 bars after the breakout — if no retest occurs, the setup expires

---

## Step 4: Set Stop Loss and Take Profit

1. **Stop Loss:** Place at the low (for longs) or high (for shorts) of the initial breakout candle
2. **Take Profit:** Set at 2:1 risk-to-reward ratio (2× the stop distance)

---

## Step 5: Build the Strategy with AI Code Generation

1. Open Looks Quant (LuxAlgo's AI PineScript tool) or a similar code generator
2. Describe the indicator in stages:
   - First: 5-minute opening range projection onto the 1-minute chart
   - Second: FVG detection within the range
   - Third: Entry/exit rules
3. Review and refine the generated PineScript code
4. Convert the indicator into a strategy script (adds order execution logic)

---

## Step 6: Backtest on TradingView

1. Add the strategy to a TradingView chart
2. Set the backtest period (video uses 365 days)
3. Run the strategy tester
4. Review results: win rate, profit factor, max drawdown, total trades

---

## Step 7: Evaluate the Results

1. **This strategy failed the backtest** — it was not profitable over 365 days on GBP/JPY
2. The setup itself is valid but cannot work "in isolation"
3. Consider adding filters: trend direction, volume confirmation, session timing, additional confluence
4. A strategy that sounds logical and looks good on a few cherry-picked examples can still fail systematically

---

## Key Takeaway

> Always backtest before trading live. This "winning" strategy — ORB + FVG with a clean 2:1 R:R — failed a 365-day backtest. Visual setups from YouTube thumbnails can be deceiving. AI tools like Looks Quant make rapid prototyping and backtesting accessible, but the data decides whether a strategy is viable.

*Guide derived from: I Backtested This ＂Winning＂ Strategy.txt*
