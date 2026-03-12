# Step-by-Step Guide: Liquidation Momentum Stink Bid Bot + Multi-Timeframe Breakout Scanner

**Source:** Moon Dev (YouTube)
**Video ID:** F8us7omGq8U
**Upload Date:** 2026-03-11

---

## What This Guide Covers

How to build a Polymarket-Hyperliquid liquidation stink bid bot and a multi-timeframe breakout scanner, plus the RBI (Research, Backtest, Incubate) framework for automated trading — as demonstrated in Moon Dev's live coding session.

---

## Prerequisites

- Python environment
- Polymarket account
- Hyperliquid account
- Mundev API key (moondev.com/docs) or equivalent liquidation data source
- Pandas library

---

## Part 1: Liquidation Momentum Stink Bid Bot

### Step 1: Set Up Liquidation Data Feed

1. Connect to Mundev API for real-time liquidation data (all exchanges: Hyperliquid, Binance, OKX)
2. Monitor BTC liquidation events specifically
3. Track both long and short liquidation totals in rolling windows

### Step 2: Define Signal Parameters

| Parameter | Value | Purpose |
|-----------|-------|---------|
| `liquidation_threshold_min` | $25,000 | Minimum liquidation volume to trigger signal |
| `liquidation_threshold_max` | $100,000 | Maximum — catches front end of cascade, not middle/back |
| `pullback_amount` | 0.30 (30%) | How far below ask to place stink bid |
| `min_time_left` | 60 seconds | Cancel orders if less than 1 min remaining |

### Step 3: Determine Direction

```
IF $25K+ long liquidations fired → Market is bearish → Buy "Down" on Polymarket
IF $25K+ short liquidations fired → Market is bullish → Buy "Up" on Polymarket
```

The $100K max threshold is critical: by the time $100K+ has been liquidated, the momentum move is already underway — you want the front end.

### Step 4: Find the Active Polymarket Market

- Polymarket 5-minute BTC markets have timestamp-based URLs (e.g., `17732358800`)
- Predict the next 5-minute window's timestamp programmatically
- Construct the market URL automatically each cycle

### Step 5: Place the Stink Bid

1. Get the current ask price for the target side (e.g., "Down" at 50 cents)
2. Place a limit order at 30% below: 50 × (1 - 0.30) = 35 cents
3. This captures price dips during volatile liquidation events
4. If less than 60 seconds remain in the market window, cancel the order

### Step 6: Hedge on Hyperliquid

After Polymarket fill:

| Polymarket Position | Hyperliquid Hedge |
|--------------------|-------------------|
| Bought "Down" | Go LONG BTC perp at 40% of Polymarket size |
| Bought "Up" | Go SHORT BTC perp at 40% of Polymarket size |

**Position split:** 60% Polymarket / 40% Hyperliquid

### Step 7: Configure Bot Cycle

- Run on **15-second cycles** (not 5-minute — need to catch fast-moving liquidation events)
- Track all trades in a CSV using Pandas
- Test with $15 on one side initially

---

## Part 2: Multi-Timeframe Breakout Scanner

### Step 1: Define Timeframes and Data

| Timeframe | Bars Needed |
|-----------|-------------|
| 5-minute | 1,969 bars |
| 1-hour | Aggregated from 5-min |
| 4-hour | Aggregated from 5-min |
| 6-hour | Aggregated from 5-min |
| Daily | Aggregated from 5-min |

**Rolling approach:** Fetch 5-min data once, then aggregate to derive larger timeframes. This dramatically reduces API calls.

### Step 2: Fetch Data

1. Pull from Mundev API (primary) for tracked symbols
2. Fall back to direct Hyperliquid API for missing data
3. Include HIP3 symbols (traditional assets on Hyperliquid)

### Step 3: Calculate Breakout/Breakdown per Timeframe

For each symbol on each timeframe, determine if it's in a breakout (new high) or breakdown (new low) using your preferred signals (Bollinger, Donchian, volume, RSI, etc.).

### Step 4: Score Confluence

1. Count how many timeframes show a breakout or breakdown for each symbol
2. Sort by confluence score (highest first)
3. **3+ timeframe agreement = high conviction**
4. **5/5 timeframe agreement = "undisputed" signal**

### Step 5: Output and Act

- Display results in a Pandas table
- Highest-confluence symbols feed into automated trading bots
- Example from stream: HYPE at 5/5 confluence, natural gas flagged, 10 symbols at 3/3

### Standalone Version

A single-file, zero-import version was also created for sharing/teaching — useful as a starting template.

---

## Part 3: RBI Framework (Research, Backtest, Incubate)

### Research
- **Google Scholar** — academic trading strategy papers
- **Market Wizards** (3-4 volumes) — required reading
- **Chat with Traders podcast** — required listening
- **YouTube** — strategy videos and live streams
- **Personal observations** — patterns you notice in live markets

### Backtest
- Get OHLCV historical data (Mundev API: 5-min resolution, 100+ weeks for crypto)
- Test strategy against historical data programmatically
- Don't trust TradingView backtests alone — build your own
- Look for edge that persists across different time periods

### Incubate
- Build a bot that trades SMALL in live markets
- Past performance ≠ future results
- Start with $15 on one side
- Monitor for at least 3+ weeks before scaling
- Track every trade in CSV for analysis

---

## Part 4: Solana Token Account Refund Recovery

1. After trading on Solana, token accounts accumulate (each trade opens one)
2. Run a "sell losers" command to close losing positions
3. Run a refund tool that closes all open token accounts
4. Collect SOL rent deposits back (~$10 USDC per batch in this session)
5. This is free money sitting in unused accounts

---

## AI Agent Economics

| Machines | Rate | Daily | Annual |
|----------|------|-------|--------|
| 1 | $1.50/hr | $36 | $13,140 |
| 7 | $1.50/hr | $252 | $92,000 |
| 100 | $1.50/hr | $3,600 | $1.3M |

**Threshold:** If an AI agent can generate more than $1.50/hour consistently, it becomes economically viable to scale across many machines.

---

## Key Takeaway

> The K9 Commandant wallet going dark ($2K→$700K then disappeared) demonstrates why copy-trading is fragile. Build your own signals instead. Use liquidation cascades as the directional trigger, place stink bids 30% below ask to catch volatile dips, hedge 40% on the inverse exchange, and always incubate small before scaling. Multi-timeframe breakout confluence (3+ timeframes agreeing) provides the highest-conviction entries.

*Guide derived from: March 11 - Automated Trading Bot Factory.txt*
