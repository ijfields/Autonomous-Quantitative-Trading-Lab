# Strategy Brief: Polymarket Liquidation Stink Bid Bot

**Source Video:** Claude Code Polymarket Trading Bots
**Channel:** Moon Dev
**Video ID:** 1BbKTQOPOGQ

---

## Strategy Overview
A momentum-based automated trading strategy that monitors real-time BTC liquidation data from Hyperliquid and Binance exchanges via the MoonDev API. When liquidation cascades in a target size range are detected, the bot places stink bids (limit orders) on Polymarket's 5-minute binary up/down markets in the direction of the liquidation momentum, then immediately hedges a portion of the position on Hyperliquid. The thesis is that liquidation cascades create short-term momentum as cascading liquidations push price further in the same direction.

## Entry Rules
1. Monitor real-time BTC liquidation data from the MoonDev API (aggregated Hyperliquid + Binance).
2. Filter for liquidations in the $25,000 to $100,000 "sweet spot" range -- ignoring tiny liquidations (noise) and whale liquidations (already priced in).
3. When cumulative liquidations in the sweet spot reach approximately $25,000 (configurable threshold):
   - **Long liquidations detected** (longs getting wiped = bearish): Place a stink bid (limit order below market price) on the DOWN contract in the Polymarket 5-minute BTC binary market.
   - **Short liquidations detected** (shorts getting wiped = bullish): Place a stink bid on the UP contract in the Polymarket 5-minute BTC binary market.
4. Once the Polymarket stink bid fills, immediately place a hedge on Hyperliquid in the opposite direction at 3x leverage (40% of total exposure).

## Exit Rules
1. Binary market auto-resolves at the end of the 5-minute window -- no manual exit needed.
2. If BTC moves in the predicted direction (even by 1 cent), the full contract pays out (approximately 100% return).
3. If BTC moves against the predicted direction, the full bet amount is lost, but the Hyperliquid hedge captures partial profit from the opposing move.
4. The Hyperliquid hedge should be closed when the binary window resolves.

## Risk Management
- **Total exposure per trade**: $25 (default, configurable).
- **Hedge ratio**: 40% of exposure hedged on Hyperliquid in the opposite direction.
- **Hedge leverage**: 3x on Hyperliquid side.
- **Defined risk**: Maximum loss per trade is the full bet amount on Polymarket minus any hedge profit from Hyperliquid.
- **No liquidation risk on Polymarket side**: Binary bets have defined, capped downside.
- **Position sizing**: Bet tiny amounts -- the strategy relies on frequency and edge compounding, not large individual bets.
- **Win rate requirement**: Need above 50% accuracy on direction prediction to be profitable; at 288 bets per day, even 49% win rate drains fast.

## Market / Instrument
- **Primary**: Polymarket 5-minute BTC binary up/down markets
- **Hedge**: Hyperliquid BTC perpetual futures
- **Data source**: MoonDev API (BTC liquidations from Hyperliquid, Binance, OKX)

## Timeframe
- 5-minute binary windows (288 potential trades per day)
- Can also be applied to 15-minute binary markets (96 trades per day, approximately 1,400x effective leverage vs. 2,400x on 5-minute)

## Key Notes
- Moon Dev explicitly states this is an **untested idea**, not a proven strategy: "This is an idea. It's not guaranteed to work by any means."
- The $25K-$100K liquidation threshold is described as "arbitrary" and not backtested.
- The effective leverage on 5-minute binary markets is approximately 2,400x compared to traditional 50x leverage on Hyperliquid -- this is calculated from the binary payout structure where full return is received for any directional correctness regardless of move magnitude.
- Moon Dev's process is RBI: Research, Back Test, Implement. He recommends backtesting before going live.
- Polymarket recently increased fees on 15-minute markets; fee impact on profitability should be assessed.
- Moon Dev was hacked on a previous Hyperliquid account, highlighting the importance of key security and using fresh accounts.
- The strategy's edge depends entirely on whether liquidation data actually predicts short-term BTC direction -- this is the core hypothesis that must be validated through backtesting.
