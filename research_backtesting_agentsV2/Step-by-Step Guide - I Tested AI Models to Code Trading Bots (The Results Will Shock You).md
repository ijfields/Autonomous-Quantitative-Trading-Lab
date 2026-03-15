# Step-by-Step Guide: I Tested AI Models to Code Trading Bots (The Results Will Shock You)

**Source:** quantlabs (YouTube)
**Video ID:** zuZBI_ul5wM
**Upload Date:** 2026-03-12

---

## What This Guide Covers
Workflow for using AI to develop and optimize trading bots, with a focus on backtest speed optimization and Z-score-based scalping parameter tuning. Note: the transcript is limited (mostly screen-share content), so this guide covers what is discernible from the narrated portions.

---

## Step 1: Set Up Your Trading Bot Development Environment
1. Use a platform like botsspot.trade for AI-driven trading bot development
2. Connect to your broker (e.g., Interactive Brokers) for market data access
3. Ensure your backtesting framework supports the asset classes you plan to trade (futures, crypto, forex)
4. Note: Interactive Brokers may not support Forex backtesting -- plan accordingly

## Step 2: Define Your Strategy Parameters
1. Choose a strategy framework -- the video demonstrates a Z-score-based mean-reversion/scalping approach
2. Set the Z-score lookback period (the video uses 10 periods for fast reaction to price swings)
3. Define entry sensitivity -- a lower threshold makes the bot "more scalpy" by entering when the spread is just starting to stretch rather than waiting for a larger move
4. Set a check-in cadence for monitoring (the video uses 15-minute intervals)

## Step 3: Use AI to Generate and Refine the Bot Code
1. Describe your strategy to the AI assistant in plain language
2. Ask it to generate the initial bot code
3. Review the output and provide feedback on behavior you observe
4. Iterate: tell the AI to adjust parameters, improve logic, or fix issues
5. Example: "Make this more scalpy by letting it jump into trades when the spread is just starting to look stretched"

## Step 4: Optimize Backtest Speed
1. Create a speed improvement guidelines document in your project docs folder
2. When backtest performance is too slow, direct the AI to read and follow those guidelines
3. Target benchmarks: a one-week backtest should take seconds, not minutes
4. Aim for 10-30x speed improvement through code optimization
5. Use continuous contracts for faster futures backtesting (avoids the overhead of contract-specific data selection)
6. Ensure the AI makes speed management automatic so optimizations are not forgotten

## Step 5: Validate and Debug the Bot
1. Run the backtest and check if the bot is actually executing trades
2. If no trades appear, direct the AI to check the logs for what is happening
3. Wait for the backtest to finish before inspecting log files (CSV logs may not exist mid-run)
4. Analyze results and iterate on the strategy parameters

## Step 6: Extend to Additional Asset Classes
1. After the primary strategy works on one asset (e.g., oil futures), extend to:
   - Seconds-level futures backtesting for higher-resolution signals
   - Cryptocurrency markets with seconds-level data support
   - Forex (lower priority; may require a different broker or data source)
2. Ensure each asset class has proper data handling and speed optimization

---

## Key Takeaway

> AI-assisted trading bot development allows you to iterate rapidly by describing desired behavior in plain language, but backtest speed optimization and systematic debugging are critical -- document your improvement guidelines and target 10-30x speed gains to make development cycles practical.

*Guide derived from: I Tested AI Models to Code Trading Bots (The Results Will Shock You).txt*
