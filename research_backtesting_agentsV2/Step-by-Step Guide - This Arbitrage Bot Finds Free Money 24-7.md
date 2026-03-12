# Step-by-Step Guide: Polymarket-Hyperliquid Liquidation Arbitrage Bot

**Source:** Moon Dev (YouTube)
**Video ID:** maH3jmlnEYs
**Upload Date:** 2026-03-11

---

## What This Guide Covers

How to build a liquidation-based statistical arbitrage bot that combines Polymarket 5-minute prediction markets with Hyperliquid perpetual futures for an asymmetrically hedged momentum strategy.

---

## Step 1: Set Up Data Sources

1. Use **Moon Dev's API** (mundav.com/docs) for aggregated liquidation data across exchanges
2. Alternative: **CoinGlass** (~$900/month)
3. Monitor real-time cumulative liquidation data for crypto assets

---

## Step 2: Understand the Liquidation Momentum Thesis

1. When leveraged traders get liquidated (e.g., 10x leverage + 10% adverse move), it creates forced selling/buying
2. One group of liquidations often triggers cascading liquidations in the same direction
3. This cascade creates exploitable directional momentum in 5-minute windows

---

## Step 3: Configure Entry Signals

1. Track cumulative **short liquidations** — when they exceed **$25,000** threshold:
   - Buy UP on Polymarket's 5-minute prediction market for that asset
2. Track cumulative **long liquidations** — when they exceed **$25,000** threshold:
   - Buy DOWN on Polymarket's 5-minute prediction market
3. The $25K threshold is a starting test value — optimize through incubation

---

## Step 4: Set Up the Asymmetric Hedge

1. Simultaneously take the **opposite position** on Hyperliquid perpetual futures
2. The hedge is NOT 1:1 — it's asymmetric:
   - Example: $100 on Polymarket (directional bet) : $80 on Hyperliquid (hedge)
3. The 20% unhedged portion is your edge
4. If the liquidation momentum thesis is correct → directional bet wins more than hedge costs
5. If entirely wrong → hedge limits losses

---

## Step 5: Handle 5-Minute Market Discovery

1. Polymarket 5-minute market URLs contain a Unix timestamp
2. Predict/construct the next market URL by calculating the next 5-minute timestamp
3. Automate this URL construction in your bot code

---

## Step 6: Deploy with Small Size (Incubation)

1. Start with **$15 per side** (or similarly small amount)
2. Follow the RBI framework:
   - **Research** → Google Scholar, books, podcasts
   - **Backtest** → OHLCV data against historical data
   - **Incubate** → Small live sizing to validate
3. Just because it works in backtest does NOT mean it works live
4. Monitor for several weeks before scaling

---

## Step 7: Build with Claude Code

1. Use Claude Code to write the bot logic
2. Core components: liquidation data polling, threshold detection, Polymarket order execution, Hyperliquid hedge execution, URL construction
3. Implement logging for all trades for later analysis

---

## Key Takeaway

> Liquidation data creates exploitable momentum cascades in crypto markets. By combining Polymarket's 5-minute binary markets with an asymmetric Hyperliquid hedge, you express a directional thesis while limiting downside. This is an experimental strategy in incubation — start with minimal sizing and validate before scaling.

*Guide derived from: This Arbitrage Bot Finds Free Money 24/7 (Polymarket to Hyperliquid).txt*
