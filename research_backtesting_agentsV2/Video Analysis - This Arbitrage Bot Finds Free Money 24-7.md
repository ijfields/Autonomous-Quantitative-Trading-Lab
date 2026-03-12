# This Arbitrage Bot Finds Free Money 24/7 (Polymarket to Hyperliquid) — Complete Transcript Analysis

**Video Title:** This Arbitrage Bot Finds Free Money 24/7 (Polymarket to Hyperliquid)
**Channel:** Moon Dev
**Video ID:** maH3jmlnEYs
**Upload Date:** 2026-03-11
**Duration:** ~13m
**Speaker:** Moon Dev
**Platform:** YouTube

---

## EXECUTIVE SUMMARY

Moon Dev demonstrates a liquidation-based statistical arbitrage bot combining Polymarket 5-minute prediction markets with Hyperliquid perpetual futures. The strategy: when cumulative short liquidations exceed $25K, buy UP on Polymarket's 5-min market and hedge short on Hyperliquid (asymmetric — e.g., $100 Polymarket, $80 Hyperliquid). The 20% unhedged portion represents the edge from liquidation cascade momentum. Shows past bot results: 186%, 170%, 3345%, 241%. Currently in incubation phase with $15 per side.

---

## KEY TOPICS

### Liquidation Momentum Thesis
- When leveraged traders get liquidated (10x leverage + 10% adverse move = forced liquidation), cascading momentum follows
- One group of liquidations often triggers more in the same direction
- This creates exploitable directional momentum windows

### Strategy Architecture

| Component | Detail |
|-----------|--------|
| Signal source | Cumulative liquidation data across exchanges |
| Long threshold | Short liquidations > $25,000 → buy UP on Polymarket |
| Short threshold | Long liquidations > $25,000 → buy DOWN on Polymarket |
| Hedge leg | Opposite position on Hyperliquid perpetual futures |
| Hedge ratio | Asymmetric (e.g., $100 Polymarket : $80 Hyperliquid) |
| Timeframe | 5-minute cycles (Polymarket resolution) |
| Current sizing | $15 per side (incubation) |

### Data Sources
- Moon Dev's own API (mundav.com/docs) — aggregates liquidation data across exchanges
- Alternative: CoinGlass (~$900/month)

### 5-Min Market URL Construction
- Polymarket 5-minute market URL contains a Unix timestamp
- Bot predicts/constructs next market URL by calculating next timestamp

### Past Bot Results (Various Bots)
- 186%, 170%, 3345%, 241%, 186%, 117%, 113%

### RBI Framework
1. **Research** — Google Scholar papers, books (Market Wizards), podcasts (Chat with Traders), YouTube
2. **Backtest** — OHLCV data against historical data
3. **Incubate** — Deploy with small size to test live (backtest ≠ live performance)

---

## TOOLS & PLATFORMS MENTIONED

| Tool/Platform | Purpose |
|---------------|---------|
| Claude Code | Bot development |
| Polymarket | 5-minute prediction markets |
| Hyperliquid | Decentralized perpetual futures (hedge leg) |
| Moon Dev API (mundav.com/docs) | Liquidation data aggregation |
| CoinGlass | Alternative liquidation data (~$900/month) |
| Google Scholar | Strategy research |

---

## ACTIONABLE TAKEAWAYS

1. Liquidation data is a signal source for momentum trading
2. Asymmetric hedging expresses a thesis with limited downside
3. Polymarket 5-minute markets offer rapid iteration for strategy testing
4. Always start with small size when moving from backtest to live
5. This is in incubation phase — not a proven strategy

---

## TRADING STRATEGIES IDENTIFIED

**Polymarket-Hyperliquid Liquidation Momentum Arbitrage** — Concrete strategy with specific entry signals (liquidation threshold), instruments (Polymarket 5-min + Hyperliquid perps), hedge ratio concept (asymmetric), and timeframe (5-min cycles). See Strategy Brief for full details.

---

*Analysis derived from: This Arbitrage Bot Finds Free Money 24/7 (Polymarket to Hyperliquid).txt*
