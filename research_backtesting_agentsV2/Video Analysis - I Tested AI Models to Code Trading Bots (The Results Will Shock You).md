# Video Analysis: I Tested AI Models to Code Trading Bots (The Results Will Shock You)

**Speaker:** quantlabs (presenter not named in transcript)
**Channel:** quantlabs
**Video ID:** zuZBI_ul5wM
**Upload Date:** 2026-03-12
**Duration:** ~25 minutes

---

## Summary
This video captures a live screen-share session where the presenter works through backtesting and optimizing an AI-coded trading bot. The transcript is notably short (78 lines) relative to the 25-minute runtime, suggesting most of the content was conveyed through visual screen demonstrations rather than narration. What is captured shows the presenter working on speed optimization for a trading strategy backtest, communicating with an AI assistant to improve performance.

The discussion centers on a scalping-oriented strategy for the oil market that uses Z-score-based spread analysis. The presenter adjusts parameters to make the bot "more scalpy" by lowering the entry threshold and shortening the Z-score lookback period to 10 periods for faster reaction to price swings. A significant portion of the captured dialogue involves troubleshooting backtest speed -- the presenter notes that a one-week backtest has an ETA of 40 minutes when it should take 40 seconds, and requests a 10-30x speed improvement.

The presenter also discusses plans for extending the backtesting platform to handle seconds-level futures data and cryptocurrency, mentions the Lumiot docs folder for speed improvement guidelines, and references the platform botsspot.trade.

## Key Topics
- AI-coded trading bot development and optimization
- Z-score-based spread/mean-reversion scalping strategy
- Backtest speed optimization (targeting 10-30x improvement)
- Oil market trading bot
- Seconds-level futures backtesting
- Cryptocurrency backtesting support
- Interactive Brokers limitations for Forex backtesting
- Continuous contracts vs. specific contract picking in futures
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
1. When backtesting is too slow, document speed improvement guidelines in a reference doc (like the Lumiot docs folder) and have AI follow those guidelines systematically
2. Target 10-30x speed improvement for backtests by optimizing code rather than accepting slow execution
3. For Z-score-based scalping, shorten the lookback period to react faster to quick price swings
4. Consider continuous contracts for faster futures backtesting; specific contract selection may require additional optimization
5. Check out botsspot.trade for an AI-driven trading bot development platform
6. Be aware that Interactive Brokers may not support Forex backtesting
