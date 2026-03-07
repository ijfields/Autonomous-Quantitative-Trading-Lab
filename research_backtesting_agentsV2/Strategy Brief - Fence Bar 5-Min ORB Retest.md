# Strategy Brief: Fence Bar 5-Min ORB Retest

## Source
- **Video:** How to Trade the First 5 Minutes (And Be Done by 10 AM)
- **Channel:** Trade Your Edge
- **Speaker:** Stephen (former market maker and arbitrage expert)
- **Video ID:** F9_uLdSYOrc
- **Upload Date:** 2026-03-05
- **Timestamp:** Full video (~30m53s)

---

## Strategy Overview

| Field | Value |
|-------|-------|
| Name | Fence Bar 5-Min ORB Retest |
| Type | breakout / trend_following |
| Style | day_trade |
| Asset | QQQ (applicable to any liquid equity/ETF/futures) |
| Timeframe | 5-minute |
| Direction | Both (long and short) |
| Session | 9:35 AM - ~10:30 AM ET |
| Risk-Reward | 2:1 (2R) |
| Active Time | 30-60 minutes/day |
| Confidence | 0.80 |
| Transcript Quality | high (clear, structured, multiple live examples with exact levels) |
| Automation Feasibility | HIGH |

---

## Core Concept

Mark the high and low of the first 5-minute candle after the open (the "fence"). Wait for a subsequent candle to close completely outside the fence, then enter on a retest (wick back into the fence that closes outside). Stop at ~50% into the fence, target 2x risk. Use the 20 SMA as directional context.

**Philosophy:** "The first candle captured everything the market was sorting out at the open. When you know how to use that boundary, you're not guessing anymore."

---

## Entry Logic

All conditions must be met sequentially:

### Signal 1: Fence Identification (9:35 ET)
- **Chart:** 5-minute
- **Logic:** Mark the high (top rail) and low (bottom rail) of the first 5-minute candle (9:30-9:35)
- **Purpose:** Defines the opening range — where buyers and sellers initially positioned

### Signal 2: Breakout Close
- **Chart:** 5-minute
- **Logic:** A candle **closes completely outside** the fence (body, not just wick)
- **Long trigger:** Close above top rail
- **Short trigger:** Close below bottom rail
- **Rule:** Wicks outside that close inside do NOT count

### Signal 3: Retest
- **Chart:** 5-minute
- **Logic:** After the breakout candle, a subsequent candle wicks **back into** the fence area and then **closes back outside**
- **Purpose:** Confirms the breakout level as support (longs) or resistance (shorts)
- **Entry:** Close of the retest candle

### Signal 4: Anchor Line Confirmation
- **Indicator:** 20-period SMA on 5-minute chart
- **Logic:** 20 SMA should be moving WITH the trade direction (or flat)
- **Filter:** If 20 SMA is moving AGAINST trade direction → reduce size or skip

### Signal 5: Risk-Reward Validation
- **Logic:** Stop-loss and target must yield at least 2:1 R:R
- **If distance from anchor is large:** Accept that 2R may not be reached; prepare for 1-1.5R

---

## Exit Logic

### Exit 1: Stop-Loss
- **Placement:** ~50% into the fence from the breakout side
- **Adjustment:** If there's a clear S/R level inside the fence (candle wicks, consolidation), use that instead
- **For large fences:** Don't use the full 50% — find a logical level closer to entry

### Exit 2: Profit Target (2R)
- **Level:** 2x the distance from entry to stop, measured in the trade direction
- **Method:** Measure risk distance, copy it twice above (longs) or below (shorts) entry

### Exit 3: Anchor Line Adjustment
- **When near 20 SMA:** Hold for full 2R with patience
- **When far from 20 SMA:** Take profit earlier (1.5-1.8R) if reversal signs appear
- **Hairpin turn far from 20:** Exit for ~1R

---

## Risk Management

| Parameter | Value |
|-----------|-------|
| Risk-Reward target | 2:1 (2R) |
| Stop-loss | ~50% into fence (or nearest S/R level) |
| Anchor line filter | 20 SMA must align with trade direction |
| Max trades per day | 1 (single opening setup) |
| Position sizing | Reduce when far from 20 SMA or anchor moving against trade |
| Time limit | Trade typically resolves within 30-90 min of entry |

---

## Filters

1. **Close outside, not wick** — candle body must finish outside the fence
2. **Retest required** — no retest = no trade (miss the move, keep the capital)
3. **20 SMA direction** — must be moving with or flat relative to trade direction
4. **Anchor distance** — far from 20 SMA = reduced expectations and size
5. **Time of day** — designed for 9:35-10:30 AM ET (opening volatility window)

---

## Missing / Unclear Elements

- **Exact instrument scope** — demonstrated on QQQ only; likely works on SPY, ES, NQ but not explicitly tested
- **Minimum fence size** — no mention of what happens with very small opening candles (low-volatility opens)
- **Maximum fence size** — large fences create wide stops; the 50% rule becomes impractical
- **Volume confirmation** — no volume analysis used
- **Multiple retests** — what if price retests the fence 2-3 times? Only first retest discussed
- **Gap behavior** — mentioned gaps affect anchor distance but no specific gap-size filter
- **News filter** — no mention of avoiding high-impact news days
- **Max daily loss** — no daily loss limit mentioned
- **Consecutive no-trigger days** — no discussion of what happens during low-volatility weeks

---

## Lumibot / Backtest Implementation Notes

| Consideration | Assessment |
|---------------|-----------|
| Data availability | HIGH — QQQ/SPY 5-min data widely available |
| Backtesting feasibility | HIGH — fully rule-based with clear definitions |
| Automatable components | Fence identification (first candle high/low), breakout detection (close outside), retest detection (wick in + close out), 20 SMA direction, R:R calculation |
| Discretionary components | Stop placement when fence is very large (S/R judgment within fence) |
| Key challenge | Retest detection — defining "wick into fence that closes outside" precisely |
| Suggested approach | First candle range → breakout = close outside ± buffer → retest = low/high crosses fence level but close remains outside → 20 SMA slope as filter → fixed 2R target |

---

## Source Quotes

> "The open is the noisiest part of the day. When you try to trade discovery, you're usually not reading the market correctly."

> "That first candle captured everything the market was sorting out at the open."

> "Most traders are taking this breakout and panicking because they think the trade is now going against them."

> "The fence gives you the levels. The anchor line gives you some context."

> "You don't need to be glued to the screen the entire day. You don't need a dozen indicators."

*Strategy extracted from: How to Trade the First 5 Minutes (And Be Done by 10 AM).txt*
