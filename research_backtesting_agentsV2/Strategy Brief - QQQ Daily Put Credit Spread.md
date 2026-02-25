# Strategy Brief: QQQ Daily Put Credit Spread

## Overview
- **Type:** options_premium_selling | **Style:** day_trade (0-1 DTE)
- **Assets:** QQQ options
- **Timeframes:** Short-dated (0-1 DTE), daily income
- **Confidence:** 0.50/1.0
- **Trader:** Investment Gains (YouTube channel)
- **Track Record:** Single example trade shown; no aggregate statistics or account history

## Entry Logic (Plain English)
1. **Open the QQQ options chain** on your brokerage platform.
2. **Select a short-dated expiration** (same day or next day).
3. **Find a put strike with 80%+ probability of profit** (displayed on the options chain) — this will be below the current QQQ price.
4. **Sell that put** (this is the short leg).
5. **Buy a put $1 below** (this is the long leg / protection).
6. **Scale contracts** to hit your daily income target. Example: 6 contracts = ~$101 credit.

## Exit Logic
- **Primary:** Let expire worthless (max profit) — both puts expire OTM if QQQ stays above the sold strike
- **Stop-Loss:** Not specified — this is a critical missing element
- **Management:** Not specified — no guidance on what to do when the trade goes against you

## Risk Management
- **Spread Width:** $1 (1-point wide)
- **Max Loss per Contract:** $100 minus credit received (e.g., sell for $0.17 credit -> max loss $0.83 per share, $83 per contract)
- **Max Profit:** Credit received (e.g., ~$17 per contract, ~$101 for 6 contracts)
- **Probability:** 80%+ probability of profit by strike selection
- **Position Size:** Scale contracts to hit income target (example: 6 contracts for ~$100)

## Filters
- **Probability threshold:** Only sell puts at strikes with 80%+ probability of profit
- **Instrument:** QQQ options specifically
- **Expiration:** Short-dated (0-1 DTE preferred based on context)

## Missing Elements / Assumptions
### Missing:
- **Stop-loss rules** — no guidance on managing losing trades (critical gap)
- **DTE selection criteria** — no specific guidance on same-day vs next-day vs longer
- **Market condition filters** — no filter for high VIX, earnings, or trending markets
- **Max daily loss** — no cap on how many spreads or how much to risk per day
- **Position sizing relative to account** — only "scale to target income"
- **Time of day for entry** — not specified
- **What to do when QQQ gaps down through the strike** — no management plan
- **Any technical analysis or directional bias** — purely probability-based, no chart reading

### Assumptions:
- 80% probability of profit is a reasonable minimum threshold
- $1-wide spreads limit risk but require multiple contracts for meaningful income
- Brokerage displays probability of profit on options chain
- Trader monitors positions and can exit if needed (despite no rules given)
- Strategy is repeated daily for income generation

## Source Quotes
> "Go on QQQ, pick whatever strike date you want"

> "Find a put with over 80% probability of profit... sell that put, and then buy one $1 below"

> "Scale it to 6 contracts and you've got $101"

## Lumibot Implementation Notes
- Use Lumibot's options chain methods to fetch QQQ puts for nearest expiration
- Filter for puts with delta ~0.15-0.20 (proxy for 80%+ probability of profit)
- Construct vertical put credit spread: sell put at selected strike, buy put $1 below
- Scale contracts to target credit amount
- Hold to expiration — no active management in the basic version
- Consider adding: max loss exit if spread goes ITM, VIX filter, time-of-day entry window
- Suggested `sleeptime`: `"5M"` (5 minutes) — monitor position
- **NEVER** use `self.get_data()` or `self.register_data()` — these are not valid Lumibot methods

## Next Steps
1. Feed `Strategy Spec - QQQ Daily Put Credit Spread.json` into Jeremiah 1.5 pipeline
2. **Critical:** Add stop-loss rules before code generation — this strategy as presented has no risk management for losing trades
3. Consider adding a VIX or implied volatility filter
4. Consider adding a directional bias filter (e.g., QQQ above 200-day MA)
5. Backtest across different market environments (especially 2022 drawdown)
