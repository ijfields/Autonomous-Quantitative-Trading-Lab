# Step-by-Step Guide: Building Multi-Signal Breakout Scanner & Polymarket Stat Arb Bot

**Source:** Moon Dev (YouTube)
**Video ID:** VKaJcKNj-qM
**Upload Date:** 2026-03-10

---

## What This Guide Covers

How to build a multi-signal breakout/breakdown scanner across crypto and HIP3 symbols, and a Polymarket-Hyperliquid statistical arbitrage bot with a liquidation cascade "unleash" trigger — as demonstrated in Moon Dev's live coding session.

---

## Prerequisites

- Python environment with trading libraries
- Hyperliquid account and API access
- Polymarket account
- Mundev API key (or equivalent liquidation data source)
- Claude Code or similar AI coding assistant (optional but accelerates development)

---

## Part 1: Multi-Signal Breakout/Breakdown Scanner

### Step 1: Define Symbol Universe

1. Collect all active crypto perpetual symbols from Hyperliquid (95+)
2. Add HIP3 traditional asset symbols (36 — stocks, commodities, indices)
3. Total universe: 131+ symbols scanned per cycle

### Step 2: Fetch 15-Minute Candle Data

1. Pull 7 days of 15-minute candle data for each symbol
2. Primary source: Mundev API for tracked symbols
3. Backfill: Direct Hyperliquid API when Mundev lacks 7 days of history
4. Use 10 parallel threads for API calls to speed up data collection

### Step 3: Implement Multi-Signal Scoring

Each signal contributes +2 points to a breakout/breakdown score:

| Signal | Breakout Trigger | Breakdown Trigger |
|--------|-----------------|-------------------|
| **Bollinger Band** | Close above upper band | Close below lower band |
| **Donchian Channel (7-day)** | At rolling 7-day high | At rolling 7-day low |
| **Volume Spike** | Volume > 2x average | Volume > 2x average |
| **RSI** | Overbought (>70) | Oversold (<30) |
| **Rate of Change** | Strong positive momentum | Strong negative momentum |

**Scoring:**
- 0–2 points: No signal
- 4–6 points: Moderate breakout/breakdown
- 8–10 points: Strong multi-signal confirmation

### Step 4: Output and Alerts

1. Sort results by score (highest first)
2. Separate breakouts from breakdowns
3. Display with colorized terminal output (termcolor library)
4. Use results to feed into automated trading bots the next session

**Example output from stream:** ETH detected in breakdown, RLC breakout (+27%), ZRO breakout

---

## Part 2: Polymarket-Hyperliquid Statistical Arbitrage Bot

### Step 1: Understand the Structure

Two simultaneous positions create a hedged trade:

```
Leg 1 (Polymarket): Buy 5-minute BTC binary option (up or down)
    → Max loss capped at position size ($15)
    → Max gain = payout minus cost

Leg 2 (Hyperliquid): Partial inverse hedge on BTC perp
    → If Polymarket bet is "BTC up", Hyperliquid leg is short
    → If Polymarket bet is "BTC down", Hyperliquid leg is long
```

### Step 2: Size the Positions

| Parameter | Value |
|-----------|-------|
| Polymarket position | $15 |
| Hyperliquid hedge | $10 minimum (always round to $10.01) |
| Hedge ratio | 20–50% (NOT 1:1 — binary payoff is nonlinear) |
| Total exposure | ~$25 per trade pair |

**Critical:** Hyperliquid rejects orders below $10. Always send $10.01 to avoid $9.99 rounding rejection.

### Step 3: Timing Constraints

1. Polymarket 5-minute binary bet opens
2. Immediately open Hyperliquid hedge within the same 5-minute window
3. Both positions must close within the same window
4. Monitor funding rates and spread on Hyperliquid — these eat into the guaranteed spread

### Step 4: The Liquidation Unleash Trigger

This is the alpha edge:

1. Run delta-neutral (hedged) by default
2. Monitor Mundev API for **liquidation cascade signals**
3. When a cascade is detected:
   - **Remove the hedge** (close Hyperliquid position)
   - **Let the winning Polymarket leg run** to expiry
4. The cascade provides directional conviction to go from neutral to directional

### Step 5: Cost Considerations

- Polymarket spread on 5-minute markets
- Hyperliquid funding rate (can be positive or negative)
- Hyperliquid trading fees
- Net: small guaranteed spread when hedged, larger upside when unleashed during cascades

---

## Part 3: Whale Copy Bot (Polymarket)

### Step 1: Identify Target Wallet

- Example: "K9 Commandant" wallet that turned $5K into $400K
- Track wallet address on Polymarket

### Step 2: Implement Polling

1. Poll target wallet every **10 seconds** for new positions
2. Filter to **5-minute markets only**
3. Skip expired, resolved, or stale positions
4. Buy **both sides** (up and down) to mirror the whale's asymmetric strategy
5. Combined cost under $1 per pair

### Step 3: Position Management

- Hold all positions to expiry
- Track P&L per position and cumulative
- No manual intervention needed

---

## Part 4: Memory Management for Long-Running Bots

### Problem
Bots running 24/7 accumulate memory from DataFrames and thread pools not being garbage collected between cycles (e.g., 331 MB after several hours).

### Fix
1. Explicitly delete DataFrames after each cycle: `del df; gc.collect()`
2. Clean up thread pool executors between cycles
3. Monitor memory usage with a guardian agent or periodic logging
4. Set maximum cycle count before forced restart

---

## Key Risk Controls

| Control | Setting |
|---------|---------|
| Max account risk per trade | Fixed % of account |
| Max daily loss | 3% |
| Position sizing | Fixed dollar amounts (not percentage-based leverage) |
| Leverage | Avoid 40x — Moon Dev's core philosophy |

---

## Key Takeaway

> The edge is not in predicting price direction — it's in predicting where liquidations will occur and positioning around them. Build scanners to identify when multi-signal breakouts align, use Polymarket-Hyperliquid stat arb for delta-neutral income, and "unleash" directional bets only when liquidation cascade data provides conviction. Automate everything — manual trading at 40x leverage is a losing game.

*Guide derived from: 🧠 AI Trading Bots Trading 24⧸7.txt*
