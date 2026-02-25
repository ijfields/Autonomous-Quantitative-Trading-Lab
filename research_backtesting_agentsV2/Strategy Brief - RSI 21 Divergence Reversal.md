# Strategy Brief: RSI(21) Divergence Reversal

## Overview
- **Type:** mean_reversion / reversal | **Style:** day_trade / swing_trade
- **Assets:** Any (demonstrated on 15-min chart; applicable to stocks, indices, forex, crypto)
- **Timeframes:** 15-minute (demonstrated), applicable to any timeframe
- **Confidence:** 0.65/1.0
- **Trader:** ChartCodes (YouTube channel)
- **Track Record:** No specific P&L or win rate provided; conceptual demonstration with chart examples

## Entry Logic (Plain English)
1. **Set RSI to 21 periods** (not standard 14) — produces fewer false signals based on speaker's years of market observation.
2. **Identify divergence:** Price makes higher highs while RSI(21) makes lower highs (bearish divergence) OR price makes lower lows while RSI(21) makes higher lows (bullish divergence).
3. **Wait for price action confirmation:** Divergence alone is a signal, NOT a trigger. You need:
   - Price breaks below support zone (bearish divergence) AND RSI breaks below the 50% level
   - Price breaks above resistance zone (bullish divergence) AND RSI breaks above the 50% level
4. **Enter on the confirmed breakdown/breakout.**

## Exit Logic
- **Target:** Previous order block (the origin zone of the prior significant move in the opposite direction)
- **Stop-Loss:** Slightly above the broken support zone (for shorts) or below the broken resistance zone (for longs)
- **Minimum R:R:** Not explicitly stated, but order block targets typically provide 2:1+ based on the examples shown

## Risk Management
- **Position Size:** Not specified
- **Stop placement:** Tight, just beyond the broken S/R zone
- **Key rule:** NEVER enter on divergence alone — always require price action confirmation (breakout/breakdown + RSI crossing 50)

## Filters
- **RSI 50% zone:** The key dividing line — above 50 = bullish, below 50 = bearish. RSI crossing this level confirms the regime change.
- **Support/Resistance:** Horizontal zones from swing highs/lows must be clearly defined before entry
- **No overbought/oversold entries:** Speaker explicitly warns against buying just because RSI is oversold or selling because RSI is overbought

## Missing Elements / Assumptions
### Missing:
- Specific timeframe recommendation (15-min demonstrated but speaker says "any timeframe")
- Position sizing rules
- Win rate or backtest data
- Max number of concurrent positions
- How to handle multiple divergence signals in quick succession
- Specific instruments recommended

### Assumptions:
- Standard divergence definition (higher highs/lower highs for bearish, lower lows/higher lows for bullish)
- Order blocks defined as the origin candle/zone of a significant directional move
- Support/resistance drawn from recent swing highs and lows
- Entry at market on confirmed breakdown/breakout

## Source Quotes
> "I use the RSI on a period of 21, not the standard 14"

> "The 50% zone is the most important level... above 50 is bullish, below 50 is bearish"

> "Never buy just because RSI is oversold — the market can stay oversold and keep dropping"

> "Divergence is a signal, NOT a trigger — requires confirmation"

## Lumibot Implementation Notes
- Use `self.get_historical_prices(asset, 100, "15min")` for 15-min chart data
- Calculate RSI with period=21 (custom, not default 14)
- Implement divergence detection: compare price swing highs/lows with RSI swing highs/lows over rolling window
- Implement support/resistance detection from swing points
- Entry trigger: divergence confirmed + price breaks S/R + RSI crosses 50
- Target: identify order blocks (large directional candles at prior reversal points)
- Suggested `sleeptime`: `"1M"` (1 minute) for 15-min chart monitoring
- **NEVER** use `self.get_data()` or `self.register_data()` — these are not valid Lumibot methods

## Next Steps
1. Feed `Strategy Spec - RSI 21 Divergence Reversal.json` into Jeremiah 1.5 pipeline
2. Review `missing_elements` — add position sizing and timeframe selection before code generation
3. Consider combining with Strategy 2 (RSI 50% Bounce) as a dual-mode system
