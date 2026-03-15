# Strategy Brief: Multiple EMA Reverse Scalper (Bollinger Mean Reversion)

**Source Video:** This Algorithm Predicts the Market with 92.567% accuracy (INSANE) (Trade Tactics)
**Video ID:** BJLBBrosaFM

---

## Strategy Overview

| Field | Value |
|-------|-------|
| Name | Multiple EMA Reverse Scalper |
| Type | Mean Reversion / Counter-Trend Scalp |
| Market | Solana 5-minute (also RNDR, MATIC, AGIX) |
| Timeframe | 5-minute chart |
| Direction | Counter-trend (fading Bollinger Band extremes) |
| Win Rate | 73% (backtested) |
| Max Drawdown | 30% (net) |
| Green Flag | Generalized — has settings for multiple coins |

---

## Entry Rules

1. **EMA Alignment:** All 5 EMAs must be aligned in the same direction (confirming a trend is in play)
2. **Bollinger Band Exit:** Wait for price to exit the Bollinger Band (upper for shorts, lower for longs)
3. **Elastic RSI Filter:** Additional confirmation from Elastic RSI indicator
4. **Entry:** Enter a counter-trend position, looking for a quick mean-reversion back inside the Bollinger Band

## Exit Rules

- **Take Profit:** Quick reversal back toward the mean (Bollinger midline)
- **Stop Loss:** Defined by strategy parameters (specific values posted in Trade Tactics Discord)

---

## Risk Parameters

| Metric | Value |
|--------|-------|
| Win Rate | 73% |
| Max Drawdown | 30% (net) — elevated |
| Sample Size | Not specified (appears larger than other strategies) |
| Multi-Asset | Yes (SOL, RNDR, MATIC, AGIX) |

---

## Vetting Checklist (from Video)

- [ ] Download PineScript from Trade Tactics Discord
- [ ] Configure exact posted settings
- [ ] Run TradingView backtest on target instrument
- [ ] Verify win rate and drawdown match expectations
- [ ] Run out-of-sample test (different time period)
- [ ] Run Monte Carlo simulation
- [ ] Paper trade for 2-4 weeks
- [ ] Only deploy live with -20% to -25% drawdown kill switch

---

## Automation Path

1. Run strategy on TradingView with alerts enabled
2. Connect alerts to Signal Swap via webhook
3. Signal Swap bridges to exchange (Apex Pro, Bybit, or Phemex)
4. Set position sizing and risk limits in Signal Swap
5. Monitor and cut at -20% to -25% drawdown

---

## Notes

- The 30% max drawdown is a red flag — stress test heavily before committing capital
- Multi-asset compatibility (SOL, RNDR, MATIC, AGIX) is a green flag for generalization
- Mean-reversion strategies tend to underperform in strong trending markets — consider a regime filter
- Speaker emphasizes this is NOT "set and forget" — ongoing bot management required

*Derived from: This Algorithm Predicts the Market with 92.567% accuracy (INSANE).txt*
