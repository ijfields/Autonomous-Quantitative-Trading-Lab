# Strategy Brief: Multi-Signal Breakout/Breakdown Scanner

## Overview
Scans 131+ crypto and HIP3 symbols on 15-minute candles over 7 days using a multi-signal scoring system. Combines Bollinger Band breaches, Donchian Channel extremes, volume spikes, RSI, and rate of change to identify high-conviction breakouts and breakdowns.

## Classification
- **Type:** Breakout / Momentum Scanner
- **Assets:** 95 crypto perpetuals + 36 HIP3 traditional asset symbols
- **Timeframe:** 15-minute candles, 7-day lookback
- **Exchange:** Hyperliquid (crypto + HIP3)

## Signal Scoring (+2 points each)

| Signal | Breakout Condition | Breakdown Condition |
|--------|-------------------|---------------------|
| Bollinger Band | Close > upper band | Close < lower band |
| Donchian Channel (7-day) | At rolling 7-day high | At rolling 7-day low |
| Volume Spike | Volume > 2x average | Volume > 2x average |
| RSI | Overbought (>70) | Oversold (<30) |
| Rate of Change | Strong positive momentum | Strong negative momentum |

## Score Interpretation
- **0–2:** No actionable signal
- **4–6:** Moderate breakout/breakdown — monitor
- **8–10:** Strong multi-signal confirmation — high conviction entry

## Data Sources
- **Primary:** Mundev API (tracked symbols with sufficient history)
- **Backfill:** Direct Hyperliquid API (when Mundev lacks 7 days of data)
- **Parallel:** 10 threads for API calls

## Entry Rules
1. Run scanner on cycle (e.g., every 15 minutes or hourly)
2. Rank all symbols by breakout/breakdown score
3. Enter positions on symbols scoring 6+ with trend confirmation
4. Use liquidation level data to refine entry timing

## Exit Rules
- Not explicitly defined in the stream — scanner feeds into separate execution bots
- Suggested: Trail stop or fixed target based on ATR/volatility

## Risk Management
- Scanner is detection only — separate risk controls on execution bots
- Max 3% daily portfolio loss (Moon Dev's standard)
- Fixed position sizing per trade

## Edge / Alpha Source
- Multi-signal confluence reduces false breakout rate
- 131+ symbol coverage catches moves across entire crypto + traditional asset universe
- HIP3 symbols (stocks, commodities) offer less-watched breakout opportunities

## Results Shown During Stream
- ETH detected in breakdown
- RLC breakout (+27%)
- ZRO breakout detected

## Confidence: 0.60
Well-established technical signals combined into a scoring system. Effectiveness depends on execution strategy layered on top. Breakout-based systems have mixed long-term performance in crypto but multi-signal scoring mitigates false signals.

---
*Source: Moon Dev — AI Trading Bots Trading 24/7 (VKaJcKNj-qM)*
