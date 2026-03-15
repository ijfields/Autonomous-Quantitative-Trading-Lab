# Video Analysis: Claude Code Polymarket Trading Bots

**Speaker:** Moon Dev
**Channel:** Moon Dev
**Video ID:** 1BbKTQOPOGQ
**Upload Date:** 2026-03-14
**Duration:** 2 hrs 6 min 19 sec

---

## Summary

This is a long-form live stream where Moon Dev works on multiple projects simultaneously: a Polymarket trading bot (the "Lick Stinkbot"), the MoonDev Arena prediction competition platform, and a CVD (Cumulative Volume Delta) scanner tool. The stream is unstructured and conversational, mixing live coding, audience Q&A, product pitches, and real-time debugging.

The Polymarket bot strategy is the centerpiece. Moon Dev explains a liquidation-momentum approach for Polymarket's 5-minute binary BTC markets. The core thesis: when BTC liquidations in the $25K-$100K range occur, there is momentum in that direction. Long liquidations signal bearish momentum (buy "down" on Polymarket), and short liquidations signal bullish momentum (buy "up"). The bot places stink bids (limit orders) rather than market buys, and once the Polymarket leg fills, it immediately hedges 40% of the position on Hyperliquid in the opposite direction at 3x leverage. Moon Dev frames the effective leverage of Polymarket's 5-minute binary markets at approximately 2,400x compared to traditional leverage trading -- because binary bets pay 100% if you are right by even one cent, while leveraged perpetual futures pay proportionally to the size of the move.

A significant portion of the stream covers the MoonDev Arena -- a free prediction competition where users submit Python prediction models that receive hourly snapshots of BTC data (price ticks, Hyperliquid liquidations, Binance liquidations, positions near liquidation) and predict BTC direction. The daily winner receives a $1,795 MoonDev credit. Moon Dev works with Claude Code to audit historical data endpoints, build CSV downloads for 60 days of historical data, and update the arena documentation and website.

Moon Dev also has Claude Code build a real-time CVD scanner from tick data. He explains CVD (Cumulative Volume Delta) -- the running total of buying volume minus selling volume at the tick level -- and its four key signal patterns: price rising + CVD rising (healthy trend), price rising + CVD falling (divergence/reversal signal), price falling + CVD falling (healthy downtrend), price falling + CVD rising (accumulation signal). The scanner is built as a terminal-based tool with live updates.

## Key Topics

- Polymarket 5-minute binary BTC up/down markets
- Liquidation-momentum trading strategy ("Lick Stinkbot")
- Stink bids (limit orders) vs. market orders on Polymarket
- Hyperliquid inverse hedge (40% position, 3x leverage)
- Effective leverage comparison: ~2,400x on 5-min binary vs. 40-50x on Hyperliquid
- Binary bet mechanics: 100% payout for correct direction regardless of move size
- MoonDev Arena: free prediction competition with hourly BTC data snapshots
- Four data sources: BTC price ticks, Hyperliquid liquidations, Binance liquidations, positions near liquidation
- 60 days of historical data for model building
- CVD (Cumulative Volume Delta) scanner from tick data
- Order flow analysis: aggressive buyers vs. sellers
- CVD divergence detection for reversal signals
- Proxy wallet debugging on Polymarket
- MACD as a potential indicator for 5-minute binary markets
- ML approaches (XGBoost + Hidden Markov Model) mentioned by a viewer as profitable on 15-min Polymarket

## Tools & Technologies Mentioned

- Claude Code (used throughout for live coding and debugging)
- Polymarket (binary prediction markets -- 5-min and 15-min BTC up/down)
- Hyperliquid (perpetual futures exchange, used for hedging)
- MoonDev API (proprietary data layer with liquidation data, tick data, position snapshots)
- MoonDev Arena (mundav.com/arena -- prediction competition platform)
- MoonDev Quant App (downloadable trading app with liquidation-based entries and risk controls)
- Python (bot scripting language)
- Cursor (IDE, mentioned but Moon Dev primarily uses Claude Code)
- Gemini/Nano Banana (image generation for thumbnails)
- Rich library (Python terminal UI for flicker-free CVD scanner display)
- Docker (arena sandbox environment)
- Binance, OKX (exchange liquidation data sources)

## Strategies Found

1. **Lick Stinkbot (Liquidation Momentum on Polymarket):** When BTC liquidations in the $25K-$100K range occur, use the direction as a momentum signal to place stink bids on Polymarket's 5-minute binary market, then hedge 40% on Hyperliquid in the opposite direction.
2. **CVD Divergence Trading:** Use Cumulative Volume Delta from tick data to detect divergence between price direction and buying/selling aggression for reversal signals.
3. **ML approach (viewer mention):** XGBoost + Hidden Markov Model layered system for 5-minute Polymarket prediction, reported as profitable (~100% in 3 days).

## Notable Quotes / Insights

- "The five-minute binary markets -- you're looking at roughly 2,425x effective leverage... not 40x leverage. 2,500."
- "On a binary, you either win or lose the full amount. It doesn't matter if BTC goes up .001% or 5%. You get paid the same. The size of the move is irrelevant. Only the direction matters."
- "Without the edge, it's just a casino. With it, it's a printing press."
- "Nobody can predict price. And if you think you can, you're probably going to get smoked... So instead of predicting price, I'm predicting which liquidation to buy."
- "I believe code is a great equalizer."
- On new markets: "When new markets come across, some of the simplest strategies they do work."
- On CVD: "CVD is literally measuring who is more aggressive, buyers or sellers, and how that aggression accumulates over time."

## Actionable Takeaways

1. Polymarket's 5-minute binary BTC markets offer extreme effective leverage (~2,400x) compared to traditional perpetual futures -- the tradeoff is binary risk (lose everything or win 100%).
2. The liquidation-momentum strategy uses MoonDev API data to detect $25K-$100K liquidation events and ride the momentum direction on Polymarket, with a hedge on Hyperliquid.
3. CVD (Cumulative Volume Delta) from tick data provides institutional-grade order flow intelligence: track the running total of aggressive buying vs. selling to detect divergences and confirm trends.
4. The MoonDev Arena (mundav.com/arena) is a free competition where you can test BTC prediction models against 60 days of historical data and win credits.
5. For 5-minute binary markets specifically, simple indicators like MACD or ML models (XGBoost, Hidden Markov) may have an edge in these new markets where sophisticated strategies have not yet crowded out simple ones.
6. The key advantage of binary bets for beginners: no need for stop losses, take profits, or position sizing -- execution complexity is eliminated.
