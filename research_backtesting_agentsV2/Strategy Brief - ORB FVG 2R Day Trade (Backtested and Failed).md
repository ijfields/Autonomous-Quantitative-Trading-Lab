# Strategy Brief: Opening Range Breakout + Fair Value Gap 2:1 R:R Day Trade

## ⚠️ STATUS: FAILED IN BACKTESTING — NOT PROFITABLE IN ISOLATION

**Source Video:** I Backtested This "Winning" Strategy (LuxAlgo)
**Video ID:** wqgAwEO2oi0

---

## Strategy Overview

| Field | Value |
|-------|-------|
| Name | ORB + FVG 2R Day Trade |
| Type | Day Trade (Breakout + Retest) |
| Market | GBP/JPY (tested), applicable to other pairs |
| Timeframe | 1-minute chart (5-minute for opening range) |
| Session | 9:30 AM EST market open |
| Backtest Result | **NOT PROFITABLE** over 365 days |

---

## Entry Rules

1. At 9:30 AM EST, mark the high and low of the first 5-minute candle (Opening Range)
2. Drop to the 1-minute chart
3. Wait for a Fair Value Gap (FVG) to form through the opening range high or low
4. Enter on the next candle after price retests the FVG zone
5. Maximum wait: 20 bars after the breakout — setup expires if no retest

## Exit Rules

- **Stop Loss:** Low (for longs) or high (for shorts) of the initial breakout candle
- **Take Profit:** 2:1 risk-to-reward ratio (2× the stop distance)

---

## Backtest Results (365 Days, GBP/JPY)

| Metric | Result |
|--------|--------|
| Profitable | **NO** |
| Period | 1 year |
| Instrument | GBP/JPY |
| Platform | TradingView (PineScript) |

---

## Why It Failed

The speaker explicitly states the strategy "does not work in isolation." Possible missing elements:
- Trend direction filter (only trade in direction of larger trend)
- Volume confirmation
- Session/time-of-day filter
- Additional confluence (support/resistance, VWAP, etc.)
- The FVG + ORB combination alone is insufficient for edge

---

## Key Lesson

> Always backtest before trading live. Strategies that look clean on cherry-picked examples can fail systematically. This strategy's *setup* is valid, but it needs additional filters to become viable.

*Derived from: I Backtested This ＂Winning＂ Strategy.txt*
