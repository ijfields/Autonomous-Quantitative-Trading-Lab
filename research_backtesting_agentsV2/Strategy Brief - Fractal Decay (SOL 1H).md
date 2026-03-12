# Strategy Brief: Fractal Decay (SOL 1H)

## Source
- **Video:** Revealing my Method for How I Made the BEST Trading Strategy Ever. (Easy to Copy)
- **Channel:** Trade Tactics
- **Video ID:** 5LIoxuqNNsM
- **Date:** 2026-03-11

## Strategy Type
Trend / Momentum (Fractal-Based)

## Market
Solana (SOL), 1-hour chart

## Thesis
Scan for price structures at varying fractal depth levels, then apply a sigma-weighted decay filter to confirm a move is real before entering. The decay period filters out stale/old price structures.

## Parameters
| Parameter | Value |
|-----------|-------|
| Fractal depth | 5 |
| Decay period | 24 |
| Filter | Sigma-weighted decay |

## Performance (True Out-of-Sample: Mar 2025 – Mar 2026)
| Metric | Value |
|--------|-------|
| Sharpe Ratio | 1.21 |
| Sortino Ratio | 11.01 |
| Max Drawdown | 9% |

## Validation Methodology
3-tier walk-forward:
1. Training (2020 – Feb 2023): engine + Claude optimize parameters
2. Testing (2023 – Mar 2025): Claude ranks (engine blind)
3. True OOS (Mar 2025 – present): human only (both AI blind)

Plus bootstrapping (randomized candle order) for robustness.

## Next Steps (from video)
- Cross-timeframe testing (30-min chart)
- Cross-asset testing (other crypto pairs)
- Add regime filters and dynamic take-profits
- Convert to MT5 or PineScript

## Backtesting Priority
High — already validated with rigorous 3-tier methodology; needs cross-asset/timeframe confirmation before live deployment.

---

*Brief derived from: Revealing my Method for How I Made the BEST Trading Strategy Ever. (Easy to Copy).txt*
