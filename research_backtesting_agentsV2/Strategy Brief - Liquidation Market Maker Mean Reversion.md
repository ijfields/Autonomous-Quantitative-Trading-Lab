# Strategy Brief: Liquidation Market Maker Mean Reversion

## Source
- **Video:** Claude in Chrome For Trading
- **Channel:** Moon Dev
- **Speaker:** Moon Dev
- **Video ID:** gvNCcrpzA9k
- **Upload Date:** 2026-03-03
- **Timestamp:** ~1:20:00 - 1:50:00

---

## Strategy Overview

| Field | Value |
|-------|-------|
| Name | Liquidation Market Maker Mean Reversion |
| Type | mean_reversion |
| Style | day_trade / swing |
| Asset | Crypto perpetual futures (Hyperliquid) |
| Timeframe | Tick/real-time (liquidation event-driven) |
| Direction | Both (long and short) |
| Confidence | 0.55 |
| Transcript Quality | low (livestream, informal, parameters scattered) |
| Automation Feasibility | HIGH (already automated by Moon Dev) |

---

## Core Concept

Fade the crowd when one side of the market is heavily stacked near liquidation levels. When liquidation imbalance (skew) reaches a threshold, enter the opposite direction expecting mean reversion as the crowded side gets washed out.

**Philosophy:** "The crowd gets liquidated. We fade them."

---

## Entry Logic

All 3 conditions must be true simultaneously:

### Signal 1: Liquidation Skew Threshold
- **Data source:** Mundave API liquidation levels
- **Logic:** One-sided liquidation buildup detected — either longs or shorts are heavily dominant
- **Direction:** Enter OPPOSITE to the crowded side (if longs stacked → go short, if shorts stacked → go long)
- **Threshold:** Not explicitly specified (proprietary)

### Signal 2: 48-Hour Price Zone
- **Logic:** Current price must be within the 48-hour price range
- **Purpose:** Avoids entering at extreme extensions where momentum may override mean reversion

### Signal 3: Aggregate Position Size
- **Logic:** Total aggregate position size of the crowded side exceeds a minimum threshold
- **Purpose:** Ensures enough "fuel" for a liquidation cascade that will push price back toward mean

---

## Exit Logic

### Exit 1: Stop-Loss
- **Type:** Percentage of margin
- **Value:** 25% (reduced from original 50% during live session)
- **Note:** Max loss per trade is 25% of margin

### Exit 2: Take Profit
- **Type:** Not explicitly defined in transcript
- **Implied:** Mean reversion target — when price returns toward the balanced zone

---

## Risk Management

| Parameter | Value |
|-----------|-------|
| Position size | 95% of balance |
| Stop-loss | 25% of margin |
| Max loss per trade | 25% |
| Distance: 1% from price | ~$95 position size |

**WARNING:** 95% position sizing is extremely aggressive. With a 25% stop-loss on margin, a single losing trade loses ~25% of total account balance. This is high-risk.

---

## Filters

1. **Skew must be one-sided** — No entry if liquidation levels are balanced
2. **Price must be within 48h range** — No entry at range extremes
3. **Minimum aggregate size** — No entry on thin liquidation buildup

---

## Missing / Unclear Elements

- **Exact skew threshold** — Not disclosed (proprietary parameter)
- **Take profit level** — Not explicitly stated
- **48-hour range definition** — Unclear if this means price is between the high and low of the last 48 hours, or within a percentile
- **Aggregate size minimum** — Not disclosed
- **Cooldown between trades** — Not mentioned
- **Maximum concurrent positions** — Not discussed
- **Which assets/pairs** — Not specified (presumably major crypto perps on Hyperliquid)

---

## Data Dependencies

| Data | Source | Availability |
|------|--------|--------------|
| Liquidation levels | Mundave API | Paid (Moon Dev lifetime offer) |
| Position aggregates | Mundave API | Paid |
| Price data | Hyperliquid exchange | Free |
| 48-hour price range | Derived from price data | Free |

**Critical dependency:** This strategy CANNOT be replicated without access to liquidation data. Mundave API or Coin Glass ($900/month) are the primary sources.

---

## Lumibot / Backtest Implementation Notes

| Consideration | Assessment |
|---------------|-----------|
| Data availability | BLOCKED — Requires proprietary Mundave API for liquidation data |
| Backtesting feasibility | LOW — Historical liquidation data not widely available |
| Alternative data | Coin Glass API (expensive), on-chain Hyperliquid node |
| Exchange support | Hyperliquid only (CCXT may support) |
| Replication difficulty | HIGH — Proprietary signals, crypto-only, API-gated |

---

## Source Quotes

> "Fade the crowd when one side is heavily stacked near liquidation."

> "Max loss trade SL 25... 10% on margin... 1% from price position 95."

> "Both P&L calculations are correct."

*Strategy extracted from: Claude in Chrome For Trading.txt (lines ~1320-1600)*
