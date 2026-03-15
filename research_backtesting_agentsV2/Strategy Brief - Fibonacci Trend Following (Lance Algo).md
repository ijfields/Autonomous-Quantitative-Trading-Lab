# Strategy Brief: Fibonacci Trend Following (Lance Algo)

**Source Video:** This Algorithm Predicts the Market with 92.567% accuracy (INSANE) (Trade Tactics)
**Video ID:** BJLBBrosaFM

---

## Strategy Overview

| Field | Value |
|-------|-------|
| Name | Lance Algo |
| Type | Trend Following |
| Market | Crypto |
| Method | Fibonacci level crossings |
| Win Rate | 84.62% (backtested) |
| Max Drawdown | 3.65% |
| Total Trades | 65 |
| Performance | 22% profit in 1 month |

---

## Entry Rules

1. **Fibonacci Level Crossings:** Uses Fibonacci retracement/extension levels as signal triggers
2. **Trend Following:** Entries align with the direction of the prevailing trend
3. Specific Fibonacci parameters posted in Trade Tactics Discord

## Exit Rules

- Defined by strategy parameters (specifics in Discord)
- Risk management through position sizing

---

## Risk Parameters

| Metric | Value |
|--------|-------|
| Win Rate | 84.62% |
| Max Drawdown | 3.65% (very low) |
| Total Trades | 65 (moderate sample — needs more history) |
| 1-Month Return | 22% |

---

## Strengths

- Very low drawdown (3.65%) suggests tight risk management
- High win rate (84.62%) with reasonable trade count
- 22% monthly return is exceptional if sustainable

## Concerns

- 65 trades is a moderate sample — needs more history for confidence
- Specific Fibonacci parameters not publicly documented (Discord only)
- High returns often come with hidden tail risks
- Need to verify across different market regimes (trending vs ranging)

---

## Vetting Checklist

- [ ] Download PineScript from Trade Tactics Discord
- [ ] Configure exact posted settings
- [ ] Run TradingView backtest on multiple instruments
- [ ] Verify win rate and drawdown on out-of-sample data
- [ ] Run Monte Carlo simulation
- [ ] Walk-forward analysis across different time windows
- [ ] Paper trade for 2-4 weeks minimum
- [ ] Deploy with -20% to -25% drawdown kill switch

---

## Automation Path

1. Run strategy on TradingView with alerts
2. Connect to Signal Swap via webhook
3. Bridge to Apex Pro (no KYC), Bybit, or Phemex
4. Start with minimal position size
5. Scale up only after sustained live performance

*Derived from: This Algorithm Predicts the Market with 92.567% accuracy (INSANE).txt*
