# Strategy Brief: SPX Iron Butterfly (SMB Capital)

## Source
- **Video:** How to Trade the Butterfly - The Core Strategy of Our Trading Desk
- **Channel:** SMB Capital
- **Video ID:** FNKIDMBPcaI
- **Date:** 2019-08-19

## Strategy Type
Options Income / Neutral

## Market
SPX index options (cash-settled, $100 per point)

## Thesis
Collect a large upfront credit by selling ATM calls and puts, protected by equidistant OTM wings. Profit when SPX stays near center strike through expiration.

## Entry Rules
1. Sell ATM call + ATM put at same strike (nearest to current SPX price)
2. Buy OTM call above (center + wing width) and OTM put below (center - wing width)
3. Standard wing width: 25 points
4. Target: collect credit ≥ 3:1 vs. margin required

## Exit Rules
1. Professional approach: exit or start closing before expiration
2. If held to expiration: cash settlement at $100 per point of ITM intrinsic value
3. Modify mid-trade if price moves significantly (adjust wings, roll, partial close)

## Position Sizing
- Size based on margin/buying power, not notional
- Example: 10 contracts = $5,600 margin, $19,400 credit

## Risk Management
- Max loss = wing width - credit received (capped and known at entry)
- Risk/reward: 3:1 to 10:1 depending on structure
- Not every trade will be successful — this was an ideal outcome example

## Key Metrics (Example Trade)
| Metric | Value |
|--------|-------|
| SPX at entry | 2815 |
| Wings | 25 points |
| Credit | $19,400 |
| Margin | $5,600 |
| SPX at expiry | 2810.90 |
| Net profit | $15,300 |

## Backtesting Priority
Medium — well-established institutional strategy; primary value is in execution and mid-trade management rather than signal generation.

---

*Brief derived from: How to Trade the Butterfly - The Core Strategy of Our Trading Desk.txt*
