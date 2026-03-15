# Strategy Brief: Stablecoin Peg Arbitrage Bot
**Source Video:** Stop Backtesting! Use AI-Driven Algorithmic Trading Bots for Real Market Data
**Channel:** quantlabs
**Video ID:** 8yB1Igk5V4g

---

## Strategy Overview

A direction-independent stablecoin arbitrage bot that exploits pricing discrepancies between USDC and USDT perpetual futures using a box spread and reversal strategy. Because it trades the peg relationship between stablecoins rather than betting on crypto market direction, it is largely immune to broader market movements. This was the second-best performing bot out of 12 tested in Brian's forward-testing environment, producing a 75% win rate across 12 trades in one day.

## Entry Rules

1. **Peg deviation detection:** Monitor the price relationship between USDC and USDT perpetual contracts for deviations from the expected peg.
2. **Box spread construction:** When a sufficient deviation is detected, construct a box spread position across both stablecoin perpetuals.
3. **Reversal component:** The strategy also includes a reversal element (specific trigger not fully detailed in the video).

## Exit Rules

1. **Mean reversion to peg:** Close the box spread when the stablecoin prices converge back toward their expected peg relationship.
2. Exit mechanics are built into the box spread structure (the spread naturally resolves as peg restores).

## Risk Management

- **Direction independence:** The strategy does not depend on the direction of Bitcoin, Ethereum, or any other crypto asset.
- **Position sizing:** Not explicitly stated.
- **Geographic/regulatory note:** This strategy requires access to perpetual stablecoin markets for both USDC and USDT, which may not be available in all jurisdictions.

## Market / Instrument

- USDC perpetual futures
- USDT (Tether) perpetual futures
- Requires an exchange or API that supports both perpetual stablecoin contracts.

## Timeframe

- Intraday (12 trades completed in approximately one day).
- Trades are relatively frequent and short-duration.

## Key Notes

- **Simulated results (real market data, ~1 day):** $620 profit, 75% win rate, 12 trades.
- This was the **#2 performing bot** and the most consistent one (highest win rate) out of 12 tested.
- Brian specifically noted that this strategy is "not very dependent on the crypto market itself -- the condition of let's say the direction of Bitcoin or Ethereum. It's all independent, which is kind of what you want."
- The profit per trade is modest compared to the XRP Short Squeeze, but the high win rate and direction-independence make it attractive for steady income.
- A detailed coding breakdown was posted on Brian's blog (quantlabsnet.com).
- Access requirements may limit usability: not all exchanges/jurisdictions offer USDC and USDT perpetual contracts.
- The bot was 100% AI-generated using Python.
