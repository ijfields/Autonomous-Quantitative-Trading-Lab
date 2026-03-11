# Strategy Brief: Polymarket-Hyperliquid Statistical Arbitrage

## Overview
Delta-neutral strategy pairing Polymarket 5-minute BTC binary options with partial inverse hedges on Hyperliquid perpetual futures. Runs hedged by default, with an "unleash" trigger that removes the hedge during liquidation cascades to capture directional moves.

## Classification
- **Type:** Statistical Arbitrage / Delta-Neutral with Directional Trigger
- **Asset:** BTC (5-minute binary + perpetual futures)
- **Timeframe:** 5-minute windows
- **Exchanges:** Polymarket (binary leg) + Hyperliquid (hedge leg)

## Entry Rules
1. Buy 5-minute BTC up/down binary on Polymarket ($15 position)
2. Immediately open partial inverse hedge on Hyperliquid perp ($10.01 minimum)
3. Hedge ratio: 20–50% (not 1:1 — binary payoff is nonlinear vs linear perp)
4. Both legs must open within the same 5-minute window

## Exit Rules
- **Default (hedged):** Both positions expire/close within the 5-minute window — small guaranteed spread
- **Unleash trigger:** When Mundev API signals a liquidation cascade:
  - Close Hyperliquid hedge
  - Let winning Polymarket leg run to expiry
  - Captures directional move from cascade

## Position Sizing
| Parameter | Value |
|-----------|-------|
| Polymarket leg | $15 |
| Hyperliquid hedge | $10.01 (minimum, always round up) |
| Total exposure | ~$25 per pair |
| Max Polymarket loss | $15 (capped by binary structure) |

## Risk Management
- Binary option structure caps max loss per leg
- Hedge absorbs adverse moves when running delta-neutral
- Funding rate + spread on Hyperliquid erode guaranteed spread
- Only go directional (unleash) when liquidation data provides conviction

## Edge / Alpha Source
- Liquidation cascade data from Mundev API (tracks $118M HLP vault positions)
- Asymmetry: small guaranteed income when hedged, large upside when unleashed
- 5-minute windows limit time exposure

## Requirements
- Polymarket account
- Hyperliquid account
- Mundev API key (or equivalent liquidation data)
- Automated execution (manual timing within 5-min windows is impractical)

## Confidence: 0.55
Novel strategy presented during live stream — conceptually sound but limited live track record shown. Dependent on quality of liquidation cascade signal timing.

---
*Source: Moon Dev — AI Trading Bots Trading 24/7 (VKaJcKNj-qM)*
