# AI Trading Bot: MASSIVE Speed Boost for Backtesting! — Complete Transcript Analysis

**Video Title:** AI Trading Bot: MASSIVE Speed Boost for Backtesting! #shorts
**Channel:** Lumiwealth
**Video ID:** QfA65W5-abs
**Upload Date:** 2026-02-27
**Duration:** ~2.5m (~144s)
**Speaker:** Moon Dev (appears on Lumiwealth channel)
**Platform:** YouTube (Short)

---

## EXECUTIVE SUMMARY

A short clip showing Moon Dev working on speed improvements for a Lumibot-based trading bot. The bot's backtesting is running too slowly — a one-week backtest takes 40 minutes when it should take ~40 seconds. He discusses using AI (voice-driven prompting) to refine strategy parameters and optimize speed, including reading a speed improvement document from the Lumibot docs folder. Key changes shown: lowering Z-score lookback to 10 periods for faster reaction, adjusting spread thresholds for more scalp-like entries, and targeting 10-30x speed improvements for futures backtesting.

---

## KEY TOPICS

### Speed Problems
- Current ETA: 40 minutes for a one-week futures backtest
- Target: 40 seconds (10-30x improvement needed)
- Continuous contracts got a speed boost; individual contract picking still slow

### Strategy Adjustments via AI
- Made bot "more scalpy" — enter trades when spread is just starting to stretch
- Shortened Z-score lookback to 10 periods for faster reaction to price swings
- Kept 15-minute check-in cadence
- Used voice-to-AI prompting (Whisper Flow) to direct changes

### Speed Improvement Priorities
1. 10-30x speed improvement for current strategy
2. Seconds-level futures backtesting
3. Fast crypto backtesting with seconds-level data
4. Forex trading (lower priority)

### Interactive Brokers Note
- Forex backtesting not supported on Interactive Brokers
- Speed improvements need to focus on futures and crypto first

---

## TOOLS & PLATFORMS MENTIONED

| Tool/Platform | Purpose |
|---------------|---------|
| Lumibot | Backtesting framework |
| Interactive Brokers | Broker for futures data |
| botsspot.trade | Moon Dev's platform |

---

## ACTIONABLE TAKEAWAYS

1. **Read the speed improvement docs** in the Lumibot docs folder before optimizing
2. **Continuous contracts** backtest faster than individual contract picking
3. **Voice-driven AI prompting** can rapidly iterate on strategy parameters
4. **Check logs** after backtests finish to understand why no trades were triggered

---

## SOURCE QUOTES

> "Pretty crazy. You can just like talk to AI and just tell it like make this faster."

> "The ETA is 40 minutes for a one-week backtest. Like it should be more like 40 seconds."

*Analysis derived from: AI Trading Bot： MASSIVE Speed Boost for Backtesting! #shorts.txt*
