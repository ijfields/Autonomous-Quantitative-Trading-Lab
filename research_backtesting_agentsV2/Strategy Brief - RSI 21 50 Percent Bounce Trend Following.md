# Strategy Brief: RSI(21) 50% Bounce Trend Following

## Overview
- **Type:** trend_following / continuation | **Style:** day_trade / swing_trade
- **Assets:** Any (demonstrated on 15-min chart; applicable to stocks, indices, forex, crypto)
- **Timeframes:** 15-minute (demonstrated), applicable to any timeframe
- **Confidence:** 0.65/1.0
- **Trader:** ChartCodes (YouTube channel)
- **Track Record:** No specific P&L or win rate provided; conceptual demonstration with chart examples

## Entry Logic (Plain English)
1. **Set RSI to 21 periods** (not standard 14).
2. **Identify established uptrend** (for longs) — series of higher highs and higher lows.
3. **Wait for pullback:** Price pulls back to former resistance level that is now acting as support (role reversal).
4. **Confirm with RSI:** RSI(21) bounces off the 50% zone (doesn't break below it in an uptrend).
5. **Optional confluence:** Fibonacci 61.8% retracement level aligns with the support zone.
6. **Wait for confirmation candle:** Bullish confirmation candle closes at the support zone.
7. **Enter** at the close of the 15-minute confirmation candle.

## Exit Logic
- **Stop-Loss:** Just below the confirmation candle / support zone
- **Target:** Minimum 2:1 risk/reward (e.g., $50 risk -> $100 target)
- **Continuation:** When price breaks the prior high after entry, consider adding a second position for trend continuation

## Risk Management
- **Position Size:** Not specified
- **Risk/Reward:** Minimum 2:1 (explicitly stated)
- **Stop placement:** Tight, just below the support zone and confirmation candle
- **Adding to winners:** Additional long position when price breaks above prior high

## Filters
- **Trend confirmation:** Established uptrend with clear higher highs/higher lows required before looking for entries
- **RSI 50% bounce:** RSI must hold above 50 during pullback (if it breaks below 50, the trend may be reversing — switch to Strategy 1)
- **Role reversal:** Former resistance must be tested as support
- **Fibonacci confluence (optional):** 61.8% retracement aligning with the support zone adds confidence

## Missing Elements / Assumptions
### Missing:
- Specific timeframe recommendation
- Position sizing rules
- Win rate or backtest data
- How to define "established uptrend" (minimum number of swing highs/lows)
- When to stop adding continuation positions
- Bearish version (shorting pullbacks to resistance in downtrend) not fully detailed

### Assumptions:
- Confirmation candle = bullish candle that closes above the support zone (e.g., hammer, engulfing)
- Role reversal = former resistance level now acts as support (tested and held)
- Fibonacci drawn from the most recent significant swing low to swing high
- 15-minute candle close used for entry timing

## Source Quotes
> "The 50% zone is the most critical level... above 50 is bullish"

> "Stack multiple confluences — divergence + support/resistance + Fibonacci + RSI 50 bounce"

> "Use order blocks as targets — they represent levels where institutional buying/selling originated"

## Lumibot Implementation Notes
- Use `self.get_historical_prices(asset, 100, "15min")` for 15-min chart data
- Calculate RSI with period=21
- Implement trend detection: series of higher highs/higher lows (minimum 2 consecutive)
- Identify support/resistance zones from prior swing points
- Detect role reversal: price approaches former resistance from above
- Fibonacci retracement calculation: 61.8% of last swing
- Entry trigger: bullish confirmation candle at support + RSI > 50 + optional Fib 61.8% alignment
- Continuation trigger: price breaks prior swing high -> add position
- Suggested `sleeptime`: `"1M"` (1 minute) for 15-min chart monitoring
- **NEVER** use `self.get_data()` or `self.register_data()` — these are not valid Lumibot methods

## Next Steps
1. Feed `Strategy Spec - RSI 21 50 Percent Bounce Trend Following.json` into Jeremiah 1.5 pipeline
2. Review `missing_elements` — define minimum trend criteria and position sizing before code generation
3. Consider pairing with RSI(21) Divergence Reversal as a dual-mode system (trend vs. reversal)
