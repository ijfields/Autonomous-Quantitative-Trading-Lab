# Strategy Brief: Liquidation Momentum Stink Bid (Polymarket + Hyperliquid)

## Overview
Trades Polymarket 5-minute BTC binary markets based on real-time liquidation cascade signals. Places discounted limit orders ("stink bids") at 30% below ask when $25K–$100K in liquidations fire in one direction, then hedges 40% on Hyperliquid perps.

## Classification
- **Type:** Event-Driven / Liquidation Momentum
- **Assets:** BTC (5-minute binary + perpetual futures)
- **Timeframe:** 5-minute windows, 15-second scan cycle
- **Exchanges:** Polymarket (signal trade) + Hyperliquid (hedge)

## Entry Rules
1. Monitor BTC liquidation events across all exchanges (Mundev API)
2. **Signal trigger:** $25,000–$100,000 in liquidations in one direction
   - $25K+ long liquidations → bearish → buy "Down" on Polymarket
   - $25K+ short liquidations → bullish → buy "Up" on Polymarket
3. The $100K max threshold catches the FRONT END of the cascade (not the middle/back when the move is already priced in)
4. Place a **stink bid** (limit order) at **30% below current ask** on Polymarket
5. Auto-cancel if < 60 seconds remain in the 5-minute market window

## Hedge Rules
After Polymarket fill, immediately take the **inverse position on Hyperliquid** at **40% of Polymarket position size**:
- Bought "Down" on Polymarket → go LONG BTC perp on Hyperliquid
- Bought "Up" on Polymarket → go SHORT BTC perp on Hyperliquid

## Position Sizing
| Parameter | Value |
|-----------|-------|
| Polymarket leg | 60% of total exposure |
| Hyperliquid hedge | 40% of total exposure |
| Test size | $15 Polymarket side |
| Cycle time | 15 seconds |

## Exit Rules
- Polymarket positions expire at end of 5-minute window
- Hyperliquid hedge closed simultaneously
- No manual intervention in normal operation

## Risk Management
- Binary structure caps max Polymarket loss at position size
- Stink bid at 30% discount provides additional margin of safety
- $100K max threshold prevents entering during exhausted cascades
- Auto-cancel with < 60 seconds prevents illiquid end-of-window fills

## Edge / Alpha Source
- Liquidation cascades create predictable short-term momentum
- Front-end timing ($25K–$100K window) catches the move before it's fully priced in
- Stink bid captures volatile price dips that occur during cascades
- Mundev API provides all-exchange liquidation data (Hyperliquid + Binance + OKX)

## Key Variables
```python
pullback_amount = 0.30          # 30% below ask
liquidation_threshold_min = 25000   # Minimum to trigger
liquidation_threshold_max = 100000  # Maximum (front end only)
min_time_left = 60              # Cancel if < 60 seconds left
```

## Historical Performance (Polymarket bots, similar approach)
Individual trade returns: 186%, 170%, 3345%, 241%, 186%, 117%, 113%

## Predecessor
Replaced copy-trading of K9 Commandant wallet ($2K→$700K, now inactive). Copy-trading proved fragile — whale switched wallets.

## Confidence: 0.55
Novel strategy built live on stream. Liquidation-based edge is well-established in Moon Dev's other bots, but the stink bid + Polymarket combination is new and has limited live track record.

---
*Source: Moon Dev — Automated Trading Bot Factory, March 11, 2026 (F8us7omGq8U)*
