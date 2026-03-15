# Video Analysis: EXPOSED -- The Brutal AI Quant Interview Questions at Citadel & Jump Trading

**Speaker:** quantlabs (presenter not named in transcript)
**Channel:** quantlabs
**Video ID:** R3HKc7ME56M
**Upload Date:** 2026-02-23
**Duration:** ~33 minutes

---

## Summary
Despite the video title suggesting quant interview questions at Citadel and Jump Trading, the transcript captures a screen-share session where the presenter works on optimizing an AI-coded trading bot for the oil market. The transcript is very short (78 lines) relative to the 33-minute runtime, indicating most content was conveyed through on-screen visuals rather than narration.

The presenter adjusts a Z-score-based scalping strategy, shortening the lookback period to 10 periods to make the bot "more scalpy" and react faster to price swings. A significant portion of the discussion involves backtest speed optimization -- the presenter notes a one-week backtest has a 40-minute ETA when it should take 40 seconds, and requests a 10-30x improvement. The presenter communicates with an AI assistant to implement these changes, referencing a speed improvement document in a "Lumiot docs folder."

**Note:** The transcript content is identical to video zuZBI_ul5wM ("I Tested AI Models to Code Trading Bots") on the same channel. YouTube likely served the same auto-generated subtitles for both videos, or the channel reposted the same content under different titles.

## Key Topics
- AI-coded trading bot development and optimization
- Z-score-based spread/mean-reversion scalping strategy for oil
- Backtest speed optimization (targeting 10-30x improvement)
- Interactive Brokers limitations for Forex backtesting
- Seconds-level futures data backtesting
- Cryptocurrency backtesting support
- Continuous contracts vs. specific contract selection in futures
- The botsspot.trade platform

## Tools & Technologies Mentioned
- botsspot.trade (trading bot platform)
- Interactive Brokers (broker, noted as lacking Forex backtesting)
- Lumiot (documentation folder for speed improvement guidelines)
- AI assistant (used for code generation and optimization)
- CSV logging for backtests

## Strategies Found
The transcript references a Z-score-based scalping strategy for oil markets but provides only fragmentary details:
- Uses Z-score lookback of 10 periods (shortened for faster reaction)
- Entry when the spread is "just starting to look stretched" (lower threshold for scalping)
- 15-minute check-in cadence maintained
- However, the strategy lacks sufficient detail for a standalone Strategy Brief -- no specific entry thresholds, exit rules, position sizing, or stop-loss levels are articulated in the transcript.

## Notable Quotes / Insights
- "This makes the bot more scalpy by letting it jump into trades when the spread is just starting to look stretched rather than waiting for an extra move."
- "This strategy that we're running here is like way too slow. We need to make it at least like 10 times faster... The ETA is 40 minutes for a one-week back test. Like it should be more like 40 seconds."
- "Pretty crazy. You can just like talk to AI and just tell it like make this faster. And that's basically what I've been doing and it's been really working well."

## Actionable Takeaways
1. When backtesting is too slow, document speed improvement guidelines in a reference doc and have AI follow those guidelines systematically
2. Target 10-30x speed improvement for backtests by optimizing code rather than accepting slow execution
3. For Z-score-based scalping, shorten the lookback period to react faster to quick price swings
4. Consider continuous contracts for faster futures backtesting; specific contract selection may require additional optimization
5. Check out botsspot.trade for an AI-driven trading bot development platform
6. Be aware that Interactive Brokers may not support Forex backtesting
