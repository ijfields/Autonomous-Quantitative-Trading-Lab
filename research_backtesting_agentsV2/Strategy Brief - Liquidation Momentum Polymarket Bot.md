# Strategy Brief: Liquidation Momentum Polymarket Bot (Hourly Lick Momentum)

## Overview
- **Type:** momentum | **Style:** day_trade
- **Assets:** Polymarket prediction markets (crypto)
- **Timeframes:** 1hour
- **Confidence:** 0.35/1.0

## Strategy Concept

An hourly bot running on Polymarket that uses liquidation data ("licks") from Hyperliquid as momentum signals. The bot checks every hour for liquidation-driven momentum and enters positions on prediction markets, holding until market expiration. Built the day before this stream, it produced strong early results in its first 24 hours of live trading.

### Live Performance (24-hour results reported on stream):
| Metric | Value |
|--------|-------|
| Total Trades | 21 (out of 24 hourly windows) |
| Wins | 17 |
| Win Rate | 89.5% |
| Profit | 12.16% (in dollars) |
| Hours with No Trades | 3 |
| Initial Position Size | $2.50 |
| Scaled Position Size | $5.00 |

## Entry Logic (Plain English)
1. Every hour, check liquidation data ("licks") via the Mundav API
2. When liquidation events create a **directional momentum signal**, enter a position on a Polymarket prediction market
3. Exact signal definition **not described** in this transcript — built in a prior session

## Exit Logic
- **Expiration Hold:** Positions are held until the Polymarket market expires/resolves
- **No early exit rules described** — no take profit, stop loss, or trailing stop mentioned

## Risk Management
- **Position Size:** $2.50 (initial incubation) → $5.00 (scaled after 21 trades)
- **Max Risk Per Trade:** Not specified (small dollar amounts suggest incubation phase)
- **Max Daily Loss:** Not specified
- **Risk/Reward:** Not specified
- **Additional Rules:**
  - Scale slowly — speaker explicitly says doubling size is where he "always always always get smoked"
  - RBI approach: incubate with small size, prove it works, then scale

## Filters
- **Market Conditions:** Requires active liquidation events on Hyperliquid
- **Time Filters:** Hourly evaluation — 3 out of 24 hours produced no trades (bot doesn't force trades)
- **Volume Filters:** Not specified

## Missing Elements / Assumptions

### Missing (Critical):
- What specific liquidation metric triggers a trade (total liquidation value? rate of change? direction?)
- How Hyperliquid liquidation data maps to Polymarket prediction market positions
- Direction logic — how does "lick momentum" determine YES vs NO on Polymarket
- Which Polymarket markets the bot trades (crypto price markets? event markets?)
- Maximum concurrent positions
- Market selection criteria
- Polymarket API integration details (CLOB API?)
- The actual bot code (built in a prior session, not shown here)

### Assumptions:
- "Licks" = liquidation events on Hyperliquid, used as momentum signals
- Hourly timeframe = bot evaluates once per hour
- "Holding until expiration" = Polymarket binary outcome resolution
- $2.50-$5.00 sizing = early incubation/validation phase
- 89.5% win rate on 21 trades is promising but not statistically significant
- The bot was built during the Opus 4.6 session or between sessions

## Source Quotes
> "we've been running that new bot here for 24 hours. And essentially, it's the hourly one with the licks."

> "It's like lick momentum or something."

> "So, boom. This bot is crushing it. Here's the breakdown. Liquidation momentum, 21 trades, taken out 24. Three hours had no trades. Okay. 17 wins. So, 89.5% win rate, 12.16% profit or dollars profit. Strategy is clearly working."

> "So, let's go ahead and increase that size up to $5. This is when I always always always get smoked."

> "Holding until expiration."

## Lumibot Implementation Notes
- Use `self.get_historical_prices(asset, 24, "1hour")` for candle data if backtesting
- Access OHLCV data via the `.df` property on the returned Bars object
- Key indicators needed: Liquidation momentum signal from Mundav API, Polymarket CLOB API integration
- Suggested `sleeptime`: `"1H"` (1 hour)
- **NEVER** use `self.get_data()` or `self.register_data()` — these are not valid Lumibot methods
- **Critical:** This strategy requires external API integration (Mundav API for liquidation data + Polymarket API for order execution)
- **Warning:** Lumibot may not natively support Polymarket — custom broker integration likely needed
- **Warning:** Too incomplete for Jeremiah pipeline without the actual bot code from the prior session

## Next Steps
1. **Priority:** Locate the actual bot code built in the prior session (likely in the speaker's Polymarket trading bot GitHub or the session before the Opus 4.6 video)
2. The 89.5% win rate on 21 trades needs a larger sample — continue monitoring before scaling further
3. The speaker's GitHub should contain the Polymarket bot framework with this strategy
4. Consider cross-referencing with the **Liquidation Gap Bot v1** and **Liquidation Acceleration Bot** specs from prior sessions — they share the same Mundav API liquidation data foundation
5. If code is found, update this spec and feed into Jeremiah 1.5 pipeline:
   - Path: `C:\Users\ijfie\CodeJeramiah_1.5\CodeJeramiah_1.5`

---

# Strategy Brief: X API Tweet Count Velocity Indicator (Concept Only)

## Overview
- **Type:** momentum | **Style:** swing
- **Assets:** Crypto tokens (unspecified)
- **Timeframes:** 1hour, 1day
- **Confidence:** 0.15/1.0

## Strategy Concept

A conceptual idea (not implemented) to use the X/Twitter API's tweet count endpoint to measure the "velocity" of a cryptocurrency token. By tracking the volume of tweets mentioning a token over time, the speaker envisions detecting momentum spikes that could predict price moves — particularly for shitcoins during crypto season.

### Test Results (from stream):
- Keyword "AI" tested: 26,000 peak hourly mentions
- Daily breakdown showed volume declining
- Speaker sees potential for detecting "peaking up" moments

## Entry Logic (Plain English)
1. Monitor tweet count volume for a crypto token keyword over 30 days
2. When hourly/daily mention volume shows **acceleration** (velocity rising), that's a potential entry signal
3. Exact threshold **not defined** — purely conceptual

## Exit Logic
- **Not defined** — implied: exit when tweet volume declines

## Risk Management
- **Not defined** — this is a concept, not a strategy

## Missing Elements / Assumptions

### Missing (Everything):
- Entry threshold, exit rules, position sizing, risk management, specific tokens, combination with price data, backtesting methodology, false positive handling

### Assumptions:
- This is an idea, not an implemented strategy
- Would need price data combination for actual trading
- X API cost ($5+ per significant query) may make continuous monitoring impractical
- Speaker concluded OpenClaw browser scraping is cheaper than X API

## Source Quotes
> "the velocity of a token. See what I'm saying?"

> "this could be a solid use case for like crypto following different tokens maybe."

> "That could be like for a shitcoin. We're seeing 'oh, it's peaking up now.'"

## Next Steps
1. This is too conceptual for Jeremiah pipeline — needs significant development first
2. Could be combined with the speaker's existing liquidation strategies as an additional confirmation signal
3. Explore free alternatives (OpenClaw browser scraping) before investing in X API costs
4. Would need historical tweet data + price data correlation study before implementation

*Extracted from: feb 11 - zoom call replay.txt*
