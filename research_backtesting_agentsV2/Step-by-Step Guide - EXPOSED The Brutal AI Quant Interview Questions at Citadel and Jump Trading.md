# Step-by-Step Guide: AI-Coded Trading Bot Optimization (Z-Score Oil Scalper)

**Source:** quantlabs (YouTube)
**Video ID:** R3HKc7ME56M
**Upload Date:** 2026-02-23

---

## What This Guide Covers
How to optimize an AI-coded Z-score scalping bot for the oil market, focusing on parameter tuning and backtest speed improvements. (Note: despite the video title referencing quant interview questions, the transcript covers trading bot optimization. Transcript is identical to zuZBI_ul5wM on the same channel.)

---

## Step 1: Tune the Z-Score Strategy for Scalping
1. Shorten the Z-score lookback period to 10 periods for faster reaction to price swings
2. Lower the entry threshold so the bot enters trades when the spread is "just starting to look stretched" rather than waiting for a larger move
3. Keep the 15-minute check-in cadence for position monitoring

## Step 2: Diagnose Backtest Speed Issues
1. Run a benchmark: time a one-week backtest and note the ETA
2. If the ETA is orders of magnitude too slow (e.g., 40 minutes instead of 40 seconds), flag for speed optimization
3. Check whether the slowdown is related to contract type -- continuous contracts may be faster than specific contract selection

## Step 3: Apply Speed Improvements Systematically
1. Create a speed improvement reference document (e.g., in a "Lumiot docs" folder)
2. Have the AI assistant read the document and follow all guidelines before proposing changes
3. Target 10-30x speed improvement as the benchmark
4. Make speed management automatic so it's not forgotten during strategy iteration

## Step 4: Extend to Other Markets
1. Ensure seconds-level futures data backtesting works correctly
2. Add cryptocurrency support with seconds-level data
3. Forex backtesting is lower priority and may not be supported on all brokers (Interactive Brokers noted as lacking this)

## Step 5: Validate and Iterate
1. Check logs after backtest completion to verify trades are being executed
2. Note that CSV logs may not exist until a backtest finishes -- you may need to wait for completion
3. Share results and get feedback (the presenter solicits comments on botsspot.trade)

---

## Key Takeaway

> AI assistants can iteratively optimize trading bot speed and parameters through natural language instructions, but you need a reference document with speed improvement guidelines so the AI follows a systematic approach rather than ad-hoc fixes.

*Guide derived from:  EXPOSED： The Brutal AI Quant Interview Questions at Citadel & Jump Trading! .txt*
