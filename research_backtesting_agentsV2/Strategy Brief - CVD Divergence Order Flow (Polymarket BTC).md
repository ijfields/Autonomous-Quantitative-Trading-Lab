# Strategy Brief: CVD Divergence Order Flow (Polymarket BTC)

**Source Video:** Claude Code Polymarket Trading Bots
**Channel:** Moon Dev
**Video ID:** 1BbKTQOPOGQ

---

## Strategy Overview

Use Cumulative Volume Delta (CVD) computed from tick-level data to detect divergences between price direction and aggressive buying/selling pressure. Divergences signal potential reversals or continuation failures that can inform directional bets on Polymarket's 5-minute or 15-minute BTC binary markets.

## Entry Rules

1. **Data source:** Tick data from MoonDev API (Hyperliquid tick feed with buy/sell side and size for each tick).
2. **Compute CVD:** For each tick, delta = buy_volume - sell_volume. CVD = cumulative sum of all deltas.
3. **Divergence detection:** Compare the slope of price vs. the slope of CVD over a lookback period.
4. **Bullish entry (buy "UP" on Polymarket):**
   - Price falling + CVD flat or rising = divergence. Buyers are stepping in aggressively but price still drops, indicating passive sell wall absorption and potential accumulation/reversal.
   - CVD rate of change shows sudden positive spike at a support level.
5. **Bearish entry (buy "DOWN" on Polymarket):**
   - Price rising + CVD flat or falling = divergence. Price is going up but sellers are more aggressive, suggesting the move is driven by short covering or thin ask-side liquidity, not real demand.
   - CVD rate of change shows sudden negative spike at a resistance level.
6. **Trend confirmation filter (optional):** Only take longs if CVD slope is positive over the lookback; only take shorts if negative.

## Exit Rules

1. On Polymarket binary: hold to expiry (5-minute or 15-minute window). Binary outcome -- no partial exits.
2. If used on Hyperliquid perpetuals instead: exit on CVD re-convergence with price, or use a fixed risk/reward based on recent ATR.

## Risk Management

1. Binary bets on Polymarket have defined risk: you can never lose more than the bet amount.
2. Size each bet as a small fraction of the account to survive losing streaks inherent to binary outcomes.
3. CVD divergence is a probabilistic signal, not a guarantee. Confirm with additional context (key support/resistance levels, liquidation data).
4. Sudden CVD spikes (large market orders hitting the book) are institutional footprints and provide stronger signals than gradual divergence.

## Market / Instrument

- **Primary:** Polymarket 5-minute or 15-minute BTC binary up/down markets.
- **Alternative:** Hyperliquid BTC perpetual futures.
- **Data:** MoonDev API tick data (includes side field: buy or sell, and size for each tick).

## Timeframe

- CVD computed from tick data, resampled to any desired timeframe (1-second, 1-minute, 5-minute, etc.).
- Applied to 5-minute binary windows (288 per day) or 15-minute windows (96 per day).

## Key Notes

- This strategy was discussed conceptually during the stream and a CVD scanner was built live, but it has not been backtested or deployed in production.
- CVD requires tick-level data with buy/sell side attribution. Standard OHLCV candle data is insufficient.
- The MoonDev API provides tick data for BTC (and a few other symbols) from Hyperliquid's data layer.
- Python implementation: each tick includes a `side` field (buy/sell) and `size`. Compute delta per tick, accumulate, and optionally resample.
- Moon Dev emphasizes that tick data provides an edge most retail traders do not have: "Since we have tick data, nobody else has tick data. You can't get tick data like this."
- Use Python's Rich library for a flicker-free terminal CVD scanner display (avoids the clear-and-repaint flicker problem).
