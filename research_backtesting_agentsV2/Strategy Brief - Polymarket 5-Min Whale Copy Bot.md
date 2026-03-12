# Strategy Brief: Polymarket 5-Min Whale Copy Bot

## Source
- **Video:** I Built 3 Trading Bots That Run 24/7 (Here's What They Made While I Slept)
- **Channel:** Moon Dev
- **Video ID:** hNRN7-Q8PKE
- **Date:** 2026-03-10

## Strategy Type
Copy Trading / Binary Options

## Market
Polymarket (5-minute BTC up/down binary markets)

## Thesis
Copy a proven whale wallet's positions on Polymarket's 5-minute binary markets. Target: K9 Commandant ($5K → $400K documented performance). Buy both sides (up and down) for sub-$1 risk per pair and ride the whale's asymmetric edge.

## Entry Rules
1. Poll target whale wallet every 10 seconds
2. Filter new positions to 5-minute expiry markets ONLY
3. Skip expired, resolved, and stale positions
4. Buy BOTH sides (up and down) when new position detected
5. Combined cost under $1 per pair

## Exit Rules
1. Hold all positions to expiry (5-minute duration)
2. No early exit — binary markets settle automatically

## Position Sizing
- Under $1 per pair (up + down combined)
- Sub-$1 max loss per trade

## Risk Management
- Maximum loss capped at $1 per pair by binary structure
- No leverage involved
- Automatic P&L tracking

## Variant: Liquidations Bot 5-Min
- Replaces whale copying with Moon Dev API liquidation signals
- Uses 15-minute BTC up/down signal generation
- Same execution mechanics (buy both sides, hold to expiry)

## Technical Requirements
- Polymarket CLOB API access
- Balance check via `get_allowance` (NOT on-chain USDC)
- 10-second polling interval
- Stale position filtering logic
- Target wallet address for K9 Commandant

## Key Considerations
- Whale may go inactive or change strategy at any time
- Latency between whale's trade and copy execution reduces edge
- 5-minute markets have limited liquidity windows
- Track whale's current P&L to detect strategy changes

## Performance Reference
- K9 Commandant: $5K → $400K on Polymarket (whale being copied)

## Backtesting Priority
Medium — requires historical Polymarket position data for target wallet + slippage modeling for copy delay

---

*Brief derived from: I Built 3 Trading Bots That Run 24⧸7 (Here's What They Made While I Slept).txt*
