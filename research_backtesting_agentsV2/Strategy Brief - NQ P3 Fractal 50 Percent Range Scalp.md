# Strategy Brief: NQ Multi-Timeframe P3 Fractal Scalp (50% Range Rebalancing)

## Overview
- **Type:** reversal / mean_reversion | **Style:** day_trade (scalp to intraday)
- **Assets:** NQ (NASDAQ 100 futures); ES used for divergence confirmation only
- **Timeframes:** Daily, H4, H1 (fractal alignment required)
- **Confidence:** 0.80/1.0

## Entry Logic (Plain English)
1. On the daily chart, mark the current dealing range (swing high to swing low) and identify the 50% equilibrium level. Determine whether price is expected to wick above the previous day high (bearish) or below the previous day low (bullish).
2. On the H4 chart, mark the previous 4-hour candle's high and low. Identify 50% of this range. Look for the H4 P3 (Power of Three / AMD) to align with the daily P3 -- i.e., both timeframes should be expecting manipulation in the same zone.
3. On the H1 chart, mark the 9:00 AM EST hour high and low. Wait for the hourly P3 to align with both the daily and H4 P3.
4. At approximately 10:00 AM EST, look for price to manipulate above the 9:00 AM hour high (for shorts) or below the hour low (for longs). This is the "manipulation" phase.
5. Confirm with SMT divergence: compare NQ and ES. For a bearish setup, ES should sweep the high while NQ fails to sweep it (showing relative weakness on NQ). For a bullish setup, ES sweeps the low while NQ fails.
6. Identify an inversion level in the manipulation zone -- a previous gap or imbalance that acted as support, now flipped to resistance (for shorts), or vice versa.
7. Enter via sell stop below the inversion level, OR limit order at retap of the inversion after initial breakdown.

## Exit Logic
- **Take Profit:** 50% of the dealing range (the equilibrium level of the next range). This is the "base hit" -- default target for every trade. Hit this and walk away.
- **Trailing Stop (discretionary):** If price blasts through the 50% target with high momentum, trail stop to the 50% level and continue trailing on structural breaks. Only after building intuition through reps.
- **Stop Loss:** At the SMT divergence point (above the manipulation high for shorts, below for longs). If this level is breached, the model is invalidated.
- **Break Even:** Move stop to break even when (a) the hourly candle flips in your direction, or (b) the 15-minute structural level is broken in your direction. "Right or right out."

## Risk Management
- **Position Size:** Not specified numerically -- Kane trades multiple NQ contracts, started from micros
- **Max Risk Per Trade:** Distance from entry to divergence point (stop loss)
- **Risk/Reward:** Variable -- base hit approximately 1:1 to 2:1; runners can reach 3:1+ with trailing
- **Max Daily Loss:** Not explicitly stated; implied 1-2 trade attempts before walking away
- **Additional Rules:**
  - Maximum 2 attempts per session (re-entry allowed if model not invalidated)
  - Primary window: 9:15 AM - 11:30 AM EST only
  - Secondary window: ~2:00 PM EST (H4 P3 rotation)
  - Avoid trading the 9:30 AM open without confirmation
  - Kane avoids Mondays and Fridays (personal preference, not a hard rule)
  - Break-even trades are expected and desirable -- they combat the reversal risk
  - Aggressive break-even management is what makes the model profitable

## Filters
- **Market Conditions:** All three timeframes (Daily, H4, H1) must show P3 alignment. No entry if any timeframe diverges.
- **Time Filters:** 10:00 AM EST is the primary manipulation time. 9:15-11:30 AM EST is the active window. Asian range (overnight) noted as low-probability -- sweep of one side signals direction.
- **Divergence Filters:** SMT divergence between NQ and ES required. Dual SMT (divergence at both highs and lows) is the A+ setup.
- **Volume Filters:** Not explicitly used as a filter; momentum/volume is used for discretionary trailing decisions only.

## Missing Elements / Assumptions
### Missing:
- Quantitative definition of "50% of the range" tolerance (exact 50% vs. a zone like 45-55%)
- Exact SMT divergence measurement criteria (how many ticks/points difference qualifies)
- Specific position sizing formula (dollar risk per trade or % of account)
- Maximum number of contracts per trade
- Daily loss limit in dollar or percentage terms
- Precise definition of when an inversion level is "clean" enough to trade
- How to handle days when no P3 alignment occurs across all three timeframes
- Whether partial profit taking is used (e.g., scale out at 50%, hold runner)
- Specific Asian range sweep rules (mentioned but not formalized)

### Assumptions:
- NQ futures are the primary instrument; model is fractal and applies to other liquid assets
- ES is the divergence confirmation instrument; no other indices used
- 10:00 AM EST is a statistical tendency, not a guarantee -- some days manipulation occurs earlier or later
- "50% of the range" is approximate -- price may reach 48% or 55% and still qualify
- Break-even trades will comprise a significant portion of all trades (this is by design)
- The discretionary component (intuition) accounts for approximately 20-30% of the edge
- Reps (repetitions over months) are required to develop the intuition portion
- Prop firm rules may constrain position sizing and daily loss limits

## Source Quotes
> "All I want to see is price rebalance into 50% of the range and then continue with the trend."

> "I don't need a big move. I just need to grab that base hit every single day and then I'm done."

> "You either need to be right or right out."

> "I look for the divergences between the two because it shows relative weakness on a single asset."

> "So you're trading the H1 PO3 inside of a H4 P3 inside of a daily P3."

> "I think a robot could pick up the model... the reality is that I think the discretion is my edge."

> "Base hits have made me millions of dollars in the market."

> "People that don't do this correctly that pick up my model will consistently tell me the model is not profitable."

> "This is a 12 setup. It's the best ever. SMT 4-hour high trading above into discount with that inversion straight into discount."

## Lumibot Implementation Notes
- Use `self.get_historical_prices("NQ", 200, "minute")` for intraday 1-minute bars to construct H1 and sub-hourly candles
- Use separate calls for ES data to compute SMT divergence: compare NQ swing highs/lows vs ES swing highs/lows
- Range detection: identify swing highs and lows on daily/H4/H1 candles; compute 50% (midpoint) of each range
- P3 alignment check: verify that all three timeframes show the manipulation wick forming in the same directional zone
- SMT divergence: compare the highest high on NQ vs ES within a time window (e.g., 9:00-10:30 AM); if ES makes a higher high but NQ does not, flag bearish divergence
- Inversion detection: identify fair value gaps (FVGs) from recent price action; track whether price has returned to and closed through the gap (flipping support to resistance)
- Break-even logic: monitor hourly candle close -- if the candle body flips direction after entry, move stop to entry price + commission buffer
- Entry execution: sell stop order at inversion level minus buffer; cancel if not triggered by 11:30 AM
- **Automation challenge:** The discretionary component (intuition, "feel" for momentum) is approximately 20-30% of the edge and cannot be fully automated. The mechanical portion (P3 alignment, SMT divergence, inversion entry, break-even management) IS automatable. Consider a semi-automated approach: bot identifies setups and sends alerts, human confirms and executes.
