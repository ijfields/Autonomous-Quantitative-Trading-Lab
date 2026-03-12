# Step-by-Step Guide: Building 24/7 Trading Bots (Hyperliquid + Polymarket + Solana)

**Source:** Moon Dev (YouTube)
**Video ID:** hNRN7-Q8PKE
**Upload Date:** 2026-03-10

---

## What This Guide Covers

Five trading bot architectures demonstrated in a live coding session: Liquidation Momentum (Hyperliquid), Polymarket-Hyperliquid Statistical Arbitrage, Polymarket Whale Copy Bot, Multi-Signal Breakout Scanner, and Solana Memecoin Copy Scanner.

---

## Prerequisites

- Python (conda/virtual environment)
- Hyperliquid account with API keys
- Polymarket account with CLOB access
- Solana wallet and RPC endpoint
- Moon Dev API access (for liquidation data and tick data)

---

## Bot 1: Liquidation Momentum Bot (Hyperliquid)

### Thesis
Hyperliquid's HLP vault turned $1K into $118M by taking the other side of liquidations. Replicate this edge at smaller scale.

### Implementation
1. Connect to Moon Dev API for liquidation levels (Binance, OKX, Hyperliquid)
2. Monitor HLP vault positions (entry, exit, current holdings)
3. When a liquidation level is hit, enter a position in alignment with HLP
4. Use `ThreadPoolExecutor` with 10 threads for parallel wallet/API checks
5. Run on 10-minute cycles with sleep between cycles

### Risk Controls
- Max X% of account per trade
- Daily 3% loss cap — hard-coded stop
- Run multiple accounts simultaneously for diversification

### Memory Management (Critical for 24/7)
- Add `gc.collect()` at end of each cycle
- Explicitly delete DataFrames after use: `del df`
- Clean up CSV reads in `fetch_transactions_from_follow_list()` and `check_single_wallet()`

---

## Bot 2: Polymarket-Hyperliquid Statistical Arbitrage

### Thesis
Delta-neutral arbitrage: buy cheap optionality on 5-minute binary markets, hedge with perpetual futures.

### Step 1: Polymarket Leg
1. Buy BOTH sides of 5-minute BTC up/down binary market
2. Combined cost under $1 per pair
3. Use CLOB `get_allowance` for balance (NOT on-chain USDC check)

### Step 2: Hyperliquid Hedge
1. Take partial inverse perp position
2. Hedge ratio: 20-50% (NOT 1:1 — binary payoff is nonlinear vs. linear perp)
3. Starting sizing: $15 Polymarket side, $10 minimum Hyperliquid side
4. **Always round UP to $10.01** — rounding down to $9.99 causes rejection

### Step 3: Unleash Trigger
1. Monitor Moon Dev API for liquidation cascade forming
2. When cascade signals directional move, remove the hedge
3. Let the winning binary leg run to expiry unhedged

### Key Gotchas
- Hedge cost: funding rates + spread eat into guaranteed spread
- Minimum order: Hyperliquid enforces $10 minimum per trade
- Timing: Hyperliquid position opens/closes within same 5-minute window as Polymarket binary

---

## Bot 3: Polymarket 5-Minute Whale Copy Bot

### Setup
1. Target wallet: identify a profitable Polymarket trader (e.g., K9 Commandant: $5K→$400K)
2. Poll target wallet every 10 seconds for new positions
3. Filter to only 5-minute expiry markets
4. Skip expired, resolved, and stale positions

### Execution
1. Mirror target's positions — buy both sides (up and down)
2. Cost under $1 per pair
3. Hold to expiry
4. Track P&L automatically

### Variant: Liquidations Bot 5-Min
- Same structure but uses Moon Dev API liquidation signals instead of copying a whale
- 15-minute BTC up/down signal generation

---

## Bot 4: Multi-Signal Breakout/Breakdown Scanner

### Data Collection
1. Collect 15-minute candle data for top 95 crypto symbols by volume (~64 actively scanned)
2. Also collect top 10 HIP3 symbols (Hyperliquid pre-launch futures)
3. Use 7-day lookback window
4. Fallback to direct Hyperliquid API for HIP3 backfill when primary API has insufficient history

### Signal Detection (Point-Based Scoring)

| Signal | Type | Points |
|--------|------|--------|
| **Bollinger Band breach** | Core | +2 |
| **Donchian Channel breach** (7-day) | Core | +2 |
| **Volume spike** (>2x average) | Confirmation | +1 |
| **RSI extreme** | Confirmation | +1 |
| **Rate of Change (ROC)** | Confirmation | +1 |

### Output
- Top 10 breakouts (highest combined score)
- Top 10 breakdowns (highest combined score)
- Manual or automated execution based on confluence

---

## Bot 5: Solana Memecoin Copy Scanner

### Purpose
Research/discovery tool — NOT a profit-first bot.

### Architecture
1. **Main scanner:** Watch follow-list wallets via API, buy tokens based on algorithm filtering
2. **Sell losers bot:** Closes bad positions automatically
3. **Refunds bot:** Claims Solana account close refunds (rent reclamation)

### Execution
- $1 position sizes (research scale only)
- Review tokens manually: check last trade time (16 seconds ago = active; 16 minutes ago = stale)
- Tokens that "float to the top" get human attention for scaling

### Risk Warning
- Most tokens are rug pulls — acknowledged as riskiest strategy
- Only profitable during active "Solana season"
- Currently runs at cost (couple hundred $/month) as a scanner

---

## Risk Management Framework (All Bots)

1. **Daily 3% max drawdown** — hard-coded into every bot
2. **Position size caps** — maximum % of account per trade
3. **Small research positions** — $1 Solana, $10-$15 Polymarket
4. **Delta-neutral hedging** where applicable
5. **Never 40x leverage** — most retail traders blow up this way
6. **RBI Process:** Research → Backtest → Implement/Incubate
7. **Guardian Agent** monitoring system resources 24/7
8. **Never print API keys/private keys** in terminal output

---

## Key Takeaway

> Liquidation-based trading is a proven edge at institutional scale (HLP: $1K→$118M). Combine it with cheap optionality on Polymarket binaries ($1 max risk per pair), multi-signal breakout scanning, and whale copy bots as research tools. Hard-code risk controls (3% daily max loss, position size caps), manage memory for 24/7 operation, and always follow RBI: Research, Backtest, Implement.

*Guide derived from: I Built 3 Trading Bots That Run 24⧸7 (Here's What They Made While I Slept).txt*
