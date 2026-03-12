# Strategy Brief: Polymarket-Hyperliquid Liquidation Arbitrage

## Source
- **Video:** This Arbitrage Bot Finds Free Money 24/7 (Polymarket to Hyperliquid)
- **Channel:** Moon Dev
- **Video ID:** maH3jmlnEYs
- **Date:** 2026-03-11

## Strategy Type
Statistical Arbitrage / Liquidation Momentum (Asymmetric Hedge)

## Market
Crypto — Polymarket 5-minute prediction markets + Hyperliquid perpetual futures

## Thesis
Leveraged trader liquidations create cascading momentum. When cumulative liquidations exceed a threshold, take the momentum direction on Polymarket's 5-minute binary market and partially hedge on Hyperliquid perps. The asymmetric hedge ratio captures the edge when the thesis is correct while limiting losses when wrong.

## Entry Rules
1. Monitor real-time cumulative liquidation data across exchanges
2. When cumulative **short liquidations** exceed **$25,000**: buy UP on Polymarket 5-min market
3. When cumulative **long liquidations** exceed **$25,000**: buy DOWN on Polymarket 5-min market
4. Simultaneously open **opposite** position on Hyperliquid perpetual futures

## Hedge Logic
- Hedge is **asymmetric** (NOT 1:1)
- Example ratio: $100 Polymarket directional : $80 Hyperliquid hedge
- 20% unhedged portion = the edge from liquidation cascade momentum
- If thesis correct: directional bet wins more than hedge costs
- If thesis wrong: hedge limits losses

## Exit Rules
- Polymarket 5-minute markets auto-resolve at expiration
- Hyperliquid hedge closed simultaneously upon Polymarket resolution

## Position Sizing
- Incubation phase: $15 per side
- Scale only after validated through live incubation

## Risk Management
- Asymmetric hedge provides built-in downside protection
- $25K liquidation threshold is a configurable test parameter
- RBI framework: Research → Backtest → Incubate with small size

## Key Parameters
| Parameter | Value |
|-----------|-------|
| Liquidation threshold | $25,000 (configurable) |
| Timeframe | 5-minute cycles |
| Hedge ratio | ~80% (asymmetric) |
| Incubation size | $15 per side |

## Data Sources
- Moon Dev API (mundav.com/docs) — free liquidation data aggregation
- CoinGlass — alternative (~$900/month)

## Technical Note
Polymarket 5-minute market URLs contain Unix timestamps. Bot must calculate next timestamp to construct the market URL for the upcoming 5-minute window.

## Backtesting Priority
Medium-High — experimental strategy in incubation phase. Already deployed with small size. Needs historical liquidation + Polymarket data for proper backtesting. Related to existing Polymarket 5-Min Whale Copy Bot and Liquidation Momentum strategies.

---

*Brief derived from: This Arbitrage Bot Finds Free Money 24/7 (Polymarket to Hyperliquid).txt*
