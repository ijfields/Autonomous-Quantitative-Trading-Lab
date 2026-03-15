# Strategy Brief: Polymarket Liquidation Momentum Stinkbot

**Source Video:** Claude Code Polymarket Trading Bots
**Channel:** Moon Dev
**Video ID:** 1BbKTQOPOGQ

---

## Strategy Overview

A liquidation-momentum strategy for Polymarket's 5-minute binary BTC up/down markets. The bot monitors real-time BTC liquidation events from exchanges via the MoonDev API. When liquidations in a target dollar range occur, the bot uses the direction of the liquidation cascade as a momentum signal to bet on the 5-minute binary outcome, then hedges part of the position on Hyperliquid in the opposite direction.

## Entry Rules

1. **Data source:** MoonDev API liquidation feed (Hyperliquid, Binance, OKX aggregated).
2. **Trigger:** BTC liquidation events in the $25,000 to $100,000 range (the "sweet spot" -- front of the wave, not chasing large cascades).
3. **Direction:**
   - Long liquidations detected (longs getting stopped out) = bearish momentum signal = **buy "DOWN"** on Polymarket 5-minute BTC binary.
   - Short liquidations detected (shorts getting stopped out) = bullish momentum signal = **buy "UP"** on Polymarket 5-minute BTC binary.
4. **Entry method:** Place a stink bid (limit order) on the Polymarket binary contract, not a market order.

## Exit Rules

1. **Polymarket leg:** Hold to expiry. The 5-minute binary resolves automatically at the end of the window. No take profit or stop loss needed -- it is a binary outcome (win 100% or lose 100% of that leg).
2. **Hyperliquid hedge leg:** Closes based on the hedge parameters (inverse position at 3x leverage). The hedge offset is intended to reduce net loss on wrong-direction bets.

## Risk Management

1. **Hedge:** Once the Polymarket leg fills, immediately open an inverse hedge on Hyperliquid at 40% of position size with 3x leverage.
2. **Per-trade exposure:** Total exposure per trade is $25 (as configured in the demo).
3. **Binary risk structure:** You can never lose more than your bet on the Polymarket side (no liquidation cascades, no funding rates). On Hyperliquid, the 3x leverage hedge has its own risk parameters.
4. **The $25K-$100K liquidation threshold is arbitrary and not backtested.** This is an idea to test, not a proven edge.
5. **Without a real edge (>50% directional accuracy), the frequency of 288 trades/day will drain the account rapidly.** Even a 49% win rate is destructive at this scale.

## Market / Instrument

- **Primary:** Polymarket 5-minute BTC binary up/down markets (crypto prediction market).
- **Hedge:** Hyperliquid BTC perpetual futures (decentralized exchange).
- **Data:** MoonDev API (aggregated liquidation data from Hyperliquid, Binance, OKX).

## Timeframe

- 5-minute binary windows on Polymarket (288 opportunities per day).
- Effective leverage: approximately 2,400x compared to traditional perpetual futures.
- The 15-minute market variant has ~1,400x effective leverage with 96 opportunities per day.

## Key Notes

- **This is an experimental idea, not a proven strategy.** Moon Dev explicitly states: "Does that work? I don't know. We'll see."
- The effective leverage comparison (2,400x) is dramatic but the risk structure is fundamentally different from leveraged futures -- you lose 100% of each wrong bet.
- The "stink bid" approach (limit orders) is designed to get better entry prices than market orders.
- A community member reported success with a layered ML approach (XGBoost + Hidden Markov Model) on the 15-minute Polymarket, claiming ~100% return in 3 days.
- MACD was suggested as a potentially useful indicator for the 5-minute market, as simple indicators may work in new markets before more sophisticated strategies crowd them out.
- CVD (Cumulative Volume Delta) from tick data was discussed as a complementary order flow signal but is not directly integrated into this bot version.
- The full Lick Stinkbot code is available on Moon Dev's algo trading roadmap.
