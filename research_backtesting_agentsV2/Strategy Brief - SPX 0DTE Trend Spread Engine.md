# Strategy Brief: SPX 0DTE Trend Spread Engine

## Source
- **Video:** SPX 0DTE Credit Spread Strategy | Trend Spread Engine
- **Channel:** Stock Market Options Trading (AlphaCrunching)
- **Video ID:** vcKwWAguOm0
- **Date:** 2026-03-11

## Strategy Type
Options Income / Trend-Following (Time-Optimized)

## Market
SPX index options — 0DTE credit spreads

## Thesis
Not all intraday time windows are equal for 0DTE credit spreads. By ranking time slots using a rolling 90-day performance lookback, you trade only the highest-probability windows in the direction of the prevailing trend.

## Entry Rules
1. Identify top 5 time slots from weekly 90-day performance report
2. At each selected time slot (10:00 AM – 3:00 PM ET), assess prevailing trend
3. **Bearish trend** → sell call credit spread above the market
4. **Bullish trend** → sell put credit spread below the market
5. Use strikes posted by the engine for each time slot

## Exit Rules
1. Let spreads expire worthless (0DTE — same-day expiration)
2. No explicit stop-loss mentioned (inherent max loss = spread width - credit)

## Key Parameters
| Parameter | Value |
|-----------|-------|
| Time slots | 15-30 min intervals, 10:00 AM – 3:00 PM ET |
| Lookback period | Rolling 90 days |
| Top slots traded | 5 |
| Best win rate (example) | 10:30 AM: 91.8% expired worthless |
| Direction filter | Trend-following (bull → put spreads, bear → call spreads) |

## Risk Management
- Max loss capped at spread width minus credit received
- Weekly re-evaluation ensures only currently strong time slots are traded
- Rolling 90-day window adapts to changing market regimes

## Backtesting Priority
High — systematic, well-defined rules with time-of-day optimization. The rolling lookback + trend direction filter is fully backtestable with SPX options data.

---

*Brief derived from: SPX 0DTE Credit Spread Strategy | Trend Spread Engine.txt*
