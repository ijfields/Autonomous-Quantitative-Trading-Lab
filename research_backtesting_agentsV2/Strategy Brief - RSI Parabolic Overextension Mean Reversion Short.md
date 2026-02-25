# Strategy Brief: RSI Parabolic Overextension Mean Reversion Short

## Source
**Video**: "The 1 Most Profitable RSI Strategy Used by Our Traders (Made Our Firm Millions)"
**Presenters**: Garrett Dryen & Tim Belden (SMB Capital)
**Channel**: SMB Capital

---

## Strategy Overview

The RSI Parabolic Overextension Mean Reversion Short is a proprietary desk strategy used by SMB Capital traders. It identifies outlier blow-off tops in stocks, ETFs, and commodities by using a custom-tuned RSI indicator across multiple timeframes. When an instrument becomes unsustainably overextended -- evidenced by RSI(20) exceeding 80 on daily, intermediate (130-min), and short-term (30-min) charts simultaneously -- traders short the opening range breakdown on a gap-up day to capture the violent mean reversion snapback.

This strategy is categorized as **mean reversion** and is the firm's most profitable playbook, generating millions in P&L per year. The setup is rare (1-2 A+ opportunities per quarter) but high-conviction when all confirmation checks align.

---

## Core Concept

The strategy exploits the tendency of parabolic price moves to reverse violently once they become unsustainable. The key insight is that **acceleration** (not just extension) is the critical variable. A stock trending linearly upward may continue indefinitely, but one where the slope itself is increasing is approaching a blow-off. Multi-timeframe RSI alignment is the practical measurement of this acceleration.

---

## Entry Rules

1. **Daily RSI(20) > 80** -- confirms the instrument is overextended on the higher timeframe
2. **130-minute RSI(20) > 80** -- confirms intermediate-term acceleration
3. **30-minute RSI(20) > 80** -- confirms short-term parabolic behavior
4. **3+ consecutive days up** -- sustained buying pressure reaching exhaustion
5. **Gap-up into the trade day** -- the final burst of euphoria
6. **Opening range breakdown** -- price breaks below the first 5-15 minutes range, triggering the short entry
7. **Optional weekly RSI(20) confirmation** -- additional check in favor

---

## Exit Rules

- **Stop-loss**: Above the opening range high or session high
- **Invalidation exit**: If price reclaims the opening range and makes new highs, exit immediately
- **Profit target**: Mean reversion toward the nearest key moving average or prior consolidation zone
- **Day trade bias**: Close position by end of session unless the instrument is fundamentally overvalued (in which case a swing may be warranted)

---

## Risk Management

- **Position sizing by setup grade**: A+ (all checks confirmed) = full size; B (most checks) = half size; Speculative stab (early signal) = minimal size
- **Small stabs on front side**: May take 1-2 probe trades before the actual top occurs -- keep these small
- **Never overstay**: If the trade invalidates, exit. Blow-off tops that fail to reverse squeeze shorts violently
- **Trade frequency discipline**: Only 1-2 A+ setups per quarter. If trading this weekly, the quality bar is too low

---

## RSI Configuration

| Parameter | Default | Strategy Setting |
|-----------|---------|-----------------|
| Period/Length | 14 | **20** |
| Overbought | 70 | **80** |
| Oversold | 30 | **20** |
| Timeframes | Single | **Daily + 130-min + 30-min** |

---

## Applicable Instruments

- **Commodities ETFs**: SLV (silver), GLD (gold)
- **High-beta stocks**: MSTR, SMCI, Beyond Meat
- **Any instrument with parabolic blow-off characteristics**
- **Commodities note**: Metals and energy tend to extend further than stocks; adjust patience accordingly

---

## Historical Examples (from video)

| Instrument | Outcome | Notes |
|-----------|---------|-------|
| SLV (Silver) | Millions in desk P&L | Christmas week; gap-up + flush; overnight calls + stock short |
| GLD (Gold) | Major day trade win | Same pattern; came off then consolidated and later made new highs |
| MSTR | Significant desk trade | Multi-timeframe RSI alignment at the top |
| SMCI | "Biggest trade ever" for some | 0-DTE puts $1 to $30; opening range breakdown entry |

---

## Quant Model Design (from discussion)

Tim and Garrett propose an automated model with these inputs:
1. **ATRs from 5-day low** -- measures how far price has traveled from recent low
2. **RSI(20) > 80 on multiple timeframes** -- the core overextension signal
3. **Consecutive days up (3+)** -- sustained directional momentum
4. **Gap-up filter** -- requires a gap-up into the trade day
5. **Opening range breakdown entry** -- the specific trigger mechanism

They agree the multi-timeframe RSI requirement and the gap-up filter are essential for profitability.

---

## Key Quotes

> "No other setup has made more money on the desk than this strategy."

> "I'm changing the length from 14 to 20. I want it to be longer. And I like to change the thresholds to 80 and 20."

> "We don't want it just to be up a lot. We want to see it start to accelerate."

> "Those default settings are for normal stocks. We are looking for a devious child that's going to get kicked out of the kindergarten class."

> "You might get one or two a quarter. But when you break down your P&L at the end of the quarter, a huge percent of it came from a trade like this."
