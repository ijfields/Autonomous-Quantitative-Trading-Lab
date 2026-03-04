# Strategy Brief: Hyper Momentum Liquidation Cascade

## Source
- **Video:** Claude in Chrome For Trading
- **Channel:** Moon Dev
- **Speaker:** Moon Dev
- **Video ID:** gvNCcrpzA9k
- **Upload Date:** 2026-03-03
- **Timestamp:** ~1:40:00 - 2:10:00

---

## Strategy Overview

| Field | Value |
|-------|-------|
| Name | Hyper Momentum Liquidation Cascade |
| Type | momentum |
| Style | day_trade |
| Asset | Crypto perpetual futures (Hyperliquid) |
| Timeframe | Tick/real-time (liquidation event-driven) |
| Direction | Both (long and short) |
| Confidence | 0.60 |
| Transcript Quality | low (livestream, informal, scattered details) |
| Automation Feasibility | HIGH (already automated by Moon Dev) |

---

## Core Concept

Ride liquidation cascades rather than fading them. When mass liquidations trigger on one side, enter WITH the momentum direction (opposite to the liquidated side) and hold for a minimum duration to capture the cascade effect.

**Philosophy:** "Ride the liquidation cascade" — the opposite approach to the Liquidation Market Maker bot.

---

## Entry Logic

### Signal 1: Liquidation Cascade Detection
- **Data source:** Mundave API liquidation data (real-time)
- **Logic:** Mass liquidation event detected — significant volume of positions being force-closed
- **Direction:** Enter WITH the cascade direction (if longs are getting liquidated → go short, if shorts are getting liquidated → go long)

---

## Exit Logic

### Exit 1: Take Profit
- **Value:** 10%
- **Type:** Percentage gain on position

### Exit 2: Stop-Loss
- **Value:** 10%
- **Type:** Percentage loss on position

### Exit 3: Minimum Hold Rule (Critical)
- **Value:** 300 seconds (5 minutes)
- **Logic:** Do NOT exit before 300 seconds regardless of conditions
- **Performance impact:**
  - Trades held 300+ seconds: **64% win rate**
  - Trades held under 5 minutes: **36% win rate**
- **Reason:** Early exits get caught in noise; the full cascade takes ~5 minutes to play out

---

## Risk Management

| Parameter | Value |
|-----------|-------|
| Position size | 95% of balance |
| Take profit | 10% |
| Stop-loss | 10% |
| Minimum hold | 300 seconds |
| Risk/Reward | 1:1 (but 64% win rate at 300s+ hold) |

**Expected value at 64% win rate, 1:1 R:R:**
- Per 100 trades: 64 wins × 10% - 36 losses × 10% = +28% net (before fees/slippage)

**WARNING:** 95% position sizing is extremely aggressive. A 10% stop-loss means losing ~10% of total account on each losing trade.

---

## Variant: Liquidation Momentum RP (Reverse Protection)

A third bot variant was also launched during the stream:

| Feature | Hyper Momentum | Momentum RP |
|---------|---------------|-------------|
| Bad entry handling | Time delay (300s min hold) | Pre-entry filter (block before execution) |
| Core logic | Same | Same |
| TP/SL | 10%/10% | ~10%/~10% |
| Account | Account 1 | Account 2 (isolated) |

**RP advantage:** Filtering bad entries before execution should theoretically produce better results than holding through bad entries for 5 minutes.

---

## Filters

1. **Liquidation cascade must be active** — No entry during quiet markets
2. **300-second hold rule** — Mandatory minimum hold after entry

---

## Missing / Unclear Elements

- **Cascade detection threshold** — What volume/speed of liquidations constitutes a "cascade"?
- **Maximum concurrent positions** — Not discussed
- **Cooldown between trades** — Not mentioned
- **Asset selection** — Which crypto pairs are traded?
- **RP filter criteria** — What pre-entry checks does the Reverse Protection variant use?
- **Slippage handling** — 95% position sizing on volatile cascades could face significant slippage
- **Time-of-day filters** — No mention of session-specific rules

---

## Data Dependencies

| Data | Source | Availability |
|------|--------|--------------|
| Liquidation cascade events | Mundave API | Paid (Moon Dev lifetime offer) |
| Real-time price data | Hyperliquid exchange | Free |
| Position sizing data | Account balance query | Free |

**Critical dependency:** Requires real-time liquidation event data from Mundave API. Cannot be replicated with standard price data alone.

---

## Lumibot / Backtest Implementation Notes

| Consideration | Assessment |
|---------------|-----------|
| Data availability | BLOCKED — Requires proprietary Mundave API for liquidation cascade data |
| Backtesting feasibility | LOW — Historical tick-level liquidation data extremely rare |
| Alternative data | On-chain Hyperliquid node (requires running your own) |
| Exchange support | Hyperliquid only |
| Replication difficulty | HIGH — Proprietary signals, crypto-only, API-gated |
| Key finding to preserve | **300-second minimum hold rule** — applicable to any momentum strategy |

---

## Transferable Insight: Minimum Hold Time

The 300-second minimum hold finding may apply beyond liquidation trading:

- **In any momentum strategy:** Early exits (under 5 minutes) often get caught in noise
- **Testable hypothesis:** For any momentum entry signal, does enforcing a minimum hold time improve win rate?
- **Applicable to:** ORB breakouts, TTM Squeeze breakouts, news-driven momentum

---

## Source Quotes

> "300 second SL has a cool down... what's the TP on the 300? 10 and 10. 10 and 10."

> "64% win rate [with 300s hold] vs 36% under 5 min."

> "Same core logic [as Hyper Momentum] but instead of solving bad entries with time delay, it's filtering out bad entries before."

*Strategy extracted from: Claude in Chrome For Trading.txt (lines ~1540-1770)*
