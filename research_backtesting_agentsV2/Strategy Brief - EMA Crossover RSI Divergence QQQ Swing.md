# Strategy Brief: 5/11/18 EMA Crossover + RSI(11) Divergence QQQ Swing

## Overview
- **Type:** trend_following / swing_trade | **Style:** swing_trade (multi-day to multi-week holds)
- **Assets:** QQQ, QLD (2x leveraged), TQQQ (3x leveraged)
- **Timeframes:** Daily chart
- **Confidence:** 0.75/1.0
- **Trader:** Matt (EquiPredict Analytics — equipredict.com)
- **Track Record:** Bar-by-bar walkthrough of several months of 2024 QQQ price action demonstrating entries/exits; no aggregate statistics provided

## Entry Logic (Plain English)
### Buy Entry:
1. **EMA Crossover:** 5 EMA crosses above 11 EMA, then both cross above 18 EMA. All three EMAs pointing northeast.
2. **RSI Confirmation:** RSI(11) breaks above recent RSI peaks (above 60-65 zone). RSI rising in same direction as price = genuine bullish momentum.
3. **Entry Method — Aggressive:** Enter at the crossover candle.
4. **Entry Method — Conservative (1-2-3 Pullback):**
   - Move 1: Initial move up after crossover
   - Move 2: Pullback to test support (look for hammer candle)
   - Move 3: Continuation bounce — enter on the bounce
5. **Air Gap Check:** Do NOT enter if price is extended far above the 18 EMA (large "air gap"). Wait for price to consolidate back toward the 18 EMA.

### Sell/Exit:
1. **Sell Signal:** Bearish RSI divergence — price making higher highs while RSI(11) makes lower highs.
2. **Sell Trigger:** Price breaks a short-term uptrend line AFTER divergence appears.
3. **Additional confirmation:** 5 and 11 EMA curling downward.
4. **Combined divergence + trigger = exit to cash.**

## Exit Logic
- **Stop-Loss:** Below the most recent swing low (example: entry at 409, stop at 390-392)
- **Trailing Stop:** Raise stop as price advances — move to just below the most recent significant candle (example: raise from 392 to 403 as price moves from 409 to 423)
- **Take Profit:** When bearish divergence + uptrend line break fires (sell trigger)

## Risk Management
- **Position Size:** Not specified (speaker uses QQQ, QLD, or TQQQ based on conviction)
- **Stop:** Below recent swing low — gives room for normal pullbacks
- **Trail method:** Manual trailing based on significant candle lows
- **Key rule:** Distinguish between signals (divergence warns) and triggers (price confirms) — never trade on signals alone

## Filters
- **Air Gap:** Do NOT enter when price is extended far above the 18 EMA — elevated pullback risk
- **EMA Alignment:** All three EMAs must point in the same direction (northeast for buys)
- **RSI Direction:** RSI must be moving in the same direction as price (RSI rising with price = genuine move)
- **RSI Overbought:** RSI > 80 is bullish momentum, NOT a sell signal (common beginner mistake)
- **RSI Middle Zone (40-60):** Provides little useful information — RSI works best at extremes

## Missing Elements / Assumptions
### Missing:
- Exact air gap threshold (distance from price to 18 EMA that is "too far")
- Position sizing relative to account
- Whether to use QQQ vs QLD vs TQQQ and when
- Specific EMA type confirmation (assumed exponential)
- How to handle conflicting signals (e.g., EMA bullish but RSI divergence appearing)
- Maximum holding period
- Performance statistics (win rate, avg return)

### Assumptions:
- EMAs are exponential (explicitly stated)
- RSI calculated on 11 periods
- Daily chart only (no intraday confirmation needed)
- Short-term uptrend lines drawn manually connecting recent lows
- Hammer candle = standard definition (lower wick 2x+ body, small upper wick)
- "Air gap" is a visual assessment, not quantified

## Source Quotes
> "5 EMA is the fastest — first to react; 11 EMA confirms; 18 EMA defines the primary trend"

> "RSI overbought means strong bullish momentum, not time to sell"

> "Never buy when there's a large air gap between price and the 18 EMA"

> "Always distinguish between signals and triggers — never trade on signals alone"

> "Use the 1-2-3 pullback pattern for lower-risk entries after EMA crossovers"

## Lumibot Implementation Notes
- Use `self.get_historical_prices("QQQ", 200, "day")` for daily chart data
- Calculate 5, 11, 18 EMAs using pandas `ewm()` method
- Calculate RSI with period=11
- Implement divergence detection: compare price swing highs with RSI swing highs over rolling window
- Air gap filter: calculate distance between close price and 18 EMA as percentage; reject entries above threshold (suggest 5-8% for QQQ based on visual examples)
- Entry: all 3 EMAs slope positive + RSI > 60 + air gap < threshold
- Exit: RSI divergence detected + price breaks below trendline (could approximate with price < 5 EMA for automation)
- Trailing stop: track swing lows, move stop to most recent swing low
- Suggested `sleeptime`: `"1D"` (daily) — end-of-day analysis only
- **NEVER** use `self.get_data()` or `self.register_data()` — these are not valid Lumibot methods

## Next Steps
1. Feed `Strategy Spec - EMA Crossover RSI Divergence QQQ Swing.json` into Jeremiah 1.5 pipeline
2. Quantify the "air gap" threshold — backtest different percentages (3%, 5%, 8% above 18 EMA)
3. Consider automating the trendline break as price closing below the 5 EMA for simplicity
4. Test on QQQ first, then QLD/TQQQ for leveraged variants
