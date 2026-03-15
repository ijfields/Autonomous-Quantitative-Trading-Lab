# Video Analysis: Claude Code Polymarket Trading Bots

**Speaker:** Moon Dev
**Channel:** Moon Dev
**Video ID:** 1BbKTQOPOGQ
**Upload Date:** 2026-03-14
**Duration:** 2h 6m 19s

---

## Summary
Moon Dev streams a live coding and development session covering two major projects: a Polymarket binary-bet trading bot ("Liquidation Stink Bid Bot") and the MoonDev Arena, a free prediction contest platform. The stream is a working session where Moon Dev interacts with Claude Code / AI agents to build, debug, and deploy code in real time while explaining concepts to viewers.

The Polymarket bot strategy uses liquidation data from the MoonDev API (Hyperliquid and Binance liquidation feeds) to predict short-term BTC price direction on Polymarket's 5-minute binary up/down markets. When liquidations in the $25K-$100K range are detected, the bot places stink bids (limit orders below market price) on Polymarket in the direction of the liquidation cascade, then hedges 40% of the position on Hyperliquid in the opposite direction. Moon Dev provides an extensive breakdown of the "effective leverage" concept -- explaining why Polymarket 5-minute binary bets represent approximately 2,400x effective leverage compared to traditional perpetual futures, because the full payout is received for correctly predicting direction regardless of move magnitude.

The second half covers the MoonDev Arena, a free rolling daily contest where users submit Python prediction models that receive 60+ keys of live BTC market data every hour and predict price direction. Moon Dev works with his AI agent to audit historical API endpoints, configure 30-day and 90-day tick data access, and update the arena documentation. He also discusses a lifetime access offer for his trading education platform and answers community questions.

## Key Topics
- Polymarket 5-minute binary up/down markets
- Liquidation-based trading strategy (momentum following liquidation cascades)
- Effective leverage comparison: Polymarket binary bets (2,400x on 5-min) vs. Hyperliquid perpetual futures (40-50x)
- Stink bid execution (limit orders vs. market orders) on Polymarket
- Hedging Polymarket positions with Hyperliquid shorts/longs
- MoonDev Arena prediction contest (free, rolling daily, $1,795 credit prize)
- MoonDev API: liquidation data, position snapshots, tick data, smart money tracking
- Real-time coding with Claude Code / AI agents
- Proxy wallet setup for Polymarket API trading
- RBI process (Research, Back Test, Implement)
- Historical data endpoints audit and configuration

## Tools & Technologies Mentioned
- Claude Code (AI coding assistant)
- Polymarket (binary prediction markets)
- Hyperliquid (perpetual futures exchange)
- MoonDev API (liquidation data, position snapshots, tick data)
- MoonDev Arena (mundav.com/arena)
- Python (trading bot language)
- Cursor (IDE)
- SSH / remote server development
- Binance (liquidation data source)
- OKX (liquidation data source)

## Strategies Found
- **Liquidation Stink Bid Bot**: A momentum strategy that uses liquidation data to predict BTC direction on Polymarket 5-minute binary markets, with a Hyperliquid hedge. See Strategy Brief for details.

## Notable Quotes / Insights
- "On binary bets, you either win or lose the full amount. It doesn't matter if BTC goes up .001% or 5%. You get paid the same. The size of the move is irrelevant. Only the direction matters."
- "The five-minute binary markets represent approximately 2,425x effective leverage with 288 opportunities per day."
- "Without the edge, it's just a casino. With it, it's a printing press."
- "Simplicity: You don't care about take profits, stop losses, position sizing relative to volatility."
- "It's the RBI process -- Research, Back Test, and then Implement."
- "I believe code is a great equalizer."
- On the strategy: "This is an idea. It's not guaranteed to work by any means. I'm just a data dog like yourself testing ideas."
- "The play here isn't use 24,400x leverage on your whole account. It's bet tiny amounts with a proven edge hundreds of times a day and let the math compound."

## Actionable Takeaways
1. Study the effective leverage dynamics of Polymarket binary bets vs. perpetual futures -- the binary structure pays full return for any directional correctness regardless of move magnitude.
2. Use the MoonDev API liquidation data endpoints to detect liquidation cascades in real time for BTC trading signals.
3. Consider hedging Polymarket directional bets with an opposing position on Hyperliquid to reduce binary risk.
4. Apply the RBI (Research, Back Test, Implement) framework before deploying any trading bot live.
5. Explore the MoonDev Arena (mundav.com/arena) as a free platform to test prediction models against real BTC market data.
6. When using Polymarket's API, ensure your proxy wallet has USDC deposited by placing one small trade through the website first.
7. Keep position sizes small on binary markets -- the high effective leverage means total loss per trade, so bet tiny amounts with a proven edge.
