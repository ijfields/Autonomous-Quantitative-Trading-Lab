# Strategy Brief: ES Micro Futures Unhealthy Move Reversal

## Source
- **Video:** Use This Strategy If You Only Have $4
- **Channel:** Riley Coleman
- **Speaker:** Riley Coleman
- **Video ID:** uvBwxFeX2dQ
- **Upload Date:** 2026-03-04
- **Timestamp:** Full video (~25m26s)

---

## Strategy Overview

| Field | Value |
|-------|-------|
| Name | ES Micro Futures Unhealthy Move Reversal |
| Type | reversal / mean_reversion |
| Style | day_trade |
| Asset | ES / MES futures (S&P 500) |
| Timeframe | 15-min (context) + 1-min (entry) |
| Direction | Both (long and short) |
| Session | 9:15 AM - ~11:00 AM ET |
| Risk-Reward | 1:3 target (minimum 1:2) |
| Active Time | 30-60 minutes/day |
| Confidence | 0.75 |
| Transcript Quality | high (clear, structured explanation with live trade example) |
| Automation Feasibility | MEDIUM |

---

## Core Concept

Identify key support/resistance zones on the 15-minute chart, wait for price to spike into these zones with an "unhealthy" (overextended) move, then trade the reversal once the 1-minute trend structure breaks. Simple price action — no indicators.

**Philosophy:** "I stopped trying to master the market and focused on one simple money-making pattern and repeated it every single day."

---

## Entry Logic

All 5 conditions must be met sequentially:

### Signal 1: Key Support/Resistance Zone
- **Chart:** 15-minute ES futures
- **Logic:** Price is at or entering a major S/R zone (swing high/low, trend line)
- **Setup:** Mark zones before market open (~9:15 AM ET)
- **Purpose:** Establishes areas where reversal probability is highest

### Signal 2: Unhealthy/Overextended Move
- **Chart:** 1-minute (observing), 15-minute (confirming)
- **Logic:** Price has spiked into the zone with big candlesticks, rapid movement
- **Definition:** Fast, extended move likely to reverse — "unhealthy" momentum
- **Direction:** If unhealthy move is UP → prepare for SHORT; if DOWN → prepare for LONG

### Signal 3: Trend Structure Break (1-Min)
- **Chart:** 1-minute
- **Logic (for short):** Higher-highs/higher-lows structure breaks — first lower low appears, followed by lower high
- **Logic (for long):** Lower-lows/lower-highs structure breaks — first higher high appears, followed by higher low
- **Rule:** Swings must be multi-candlestick (3+ bars), not single-candle blips

### Signal 4: Momentum Confirmation
- **Chart:** 1-minute
- **Logic:** Big directional candlestick breaks the previous swing low (shorts) or swing high (longs)
- **Optional:** Wait for pullback after break → re-break for extra confirmation (avoids "bait" moves)

### Signal 5: Risk-Reward Validation
- **Logic:** Calculate potential reward ÷ risk before entering
- **Minimum:** 1:2 (risk $100, target $200)
- **Ideal:** 1:3 (risk $100, target $300)
- **If R:R < 1:2:** No trade

---

## Exit Logic

### Exit 1: Stop-Loss
- **Placement:** Above/below the swing that confirmed the reversal
- **For shorts:** Above the lower-high swing
- **For longs:** Below the higher-low swing

### Exit 2: Initial Target
- **Level:** Start of the unhealthy move (where price was before the spike)
- **Logic:** This is where the overextension began — natural support/resistance

### Exit 3: Trailing Stop (Momentum Phase)
- **Trigger:** Price accelerates with big directional candlesticks
- **Method:** Trail stop to previous candlestick's high/low as each candle closes
- **Purpose:** Lock in profits while trend continues; automatic exit on reversal

### Exit 4: Major S/R Zone
- **Logic:** When price reaches a major support/resistance zone on the 15-min chart, expect a bounce
- **Action:** Tighten trailing stop or manually exit

### Exit 5: Break-Even Move
- **Logic:** After price approaches initial target, move stop to entry price
- **Purpose:** Eliminate risk of loss on trade

---

## Risk Management

| Parameter | Value |
|-----------|-------|
| Risk-Reward target | 1:3 (minimum 1:2) |
| Stop-loss | Above/below confirming swing |
| Starting risk per trade | $50 (micro contracts) |
| Maximum risk per trade | Scale up gradually ($1,500+ at advanced level) |
| Trailing stop | Previous candle high/low on momentum moves |
| Break-even | Move stop to entry when initial target approaches |
| Max trades per day | 1-2 (only at key S/R zones with unhealthy moves) |

---

## Filters

1. **Must be at a key S/R zone** — No trades in the middle of a range
2. **Unhealthy move required** — No trades on normal/slow price action
3. **Multi-candlestick swings only** — Single-candle lower highs don't count
4. **R:R must be at least 1:2** — Skip if the math doesn't work
5. **Time filter (implied):** 9:30 AM - ~11:00 AM ET (market open volatility window)

---

## Missing / Unclear Elements

- **Exact S/R zone definition** — How many touches required? How wide should the box be?
- **"Unhealthy move" quantification** — How many points/percent qualifies as unhealthy? ATR-based threshold?
- **Swing size definition** — How many candles minimum constitute a "legitimate" swing? (said "multiple" but no exact number)
- **Maximum stop-loss distance** — No hard cap mentioned on how far the stop can be from entry
- **Time-of-day cutoff** — No mention of when to stop looking for setups
- **News filter** — No mention of avoiding major news events (the $5K example was actually triggered by news)
- **Max daily loss** — No daily loss limit mentioned
- **Volume confirmation** — No volume analysis used

---

## Lumibot / Backtest Implementation Notes

| Consideration | Assessment |
|---------------|-----------|
| Data availability | HIGH — ES/MES 1-min and 15-min data widely available |
| Backtesting feasibility | MEDIUM — S/R zones and "unhealthy move" require discretionary judgment |
| Automatable components | S/R zone identification (swing highs/lows), trend structure break (HH/HL pattern recognition), R:R calculation |
| Discretionary components | "Unhealthy move" assessment, swing significance judgment, trailing stop management |
| Key challenge | Defining "unhealthy" computationally — could use ATR multiple, rate of change, or candlestick size relative to average |
| Suggested approach | Use ATR(14) on 15-min for S/R zones, RSI or rate-of-change for overextension, swing detection algorithm on 1-min, fixed 1:3 R:R |

---

## Source Quotes

> "Every time I tried to learn more strategies, add more indicators, or level up with something new, I actually made less money."

> "When the market makes a big move up like this, it's called an unhealthy move. And it's actually likely if it reverses, it reverses in a big way."

> "You're not looking for a one candlestick lower high... I need to have the market show some multiple candlesticks that make a swing."

> "I can't really go off the chart here, but I better be — if I'm risking $100, if my stop loss is up here, I better be getting like $200 or $300 if I'm right."

> "The best trades are when I jump in and it just works out pretty well in your favor."

*Strategy extracted from: Use This Strategy If You Only Have 4 Dollars.txt*
