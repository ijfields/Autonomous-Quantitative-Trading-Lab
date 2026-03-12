# I Built 3 Trading Bots That Run 24/7 (Here's What They Made While I Slept) — Complete Transcript Analysis

**Video Title:** I Built 3 Trading Bots That Run 24/7 (Here's What They Made While I Slept)
**Channel:** Moon Dev
**Video ID:** hNRN7-Q8PKE
**Upload Date:** 2026-03-10
**Duration:** ~111m
**Speaker:** Moon Dev (Mundav)
**Platform:** YouTube

---

## EXECUTIVE SUMMARY

A live coding/building stream where Moon Dev runs and debugs multiple trading bots simultaneously across Hyperliquid, Polymarket, and Solana. Five distinct strategies are demonstrated: (1) Liquidation Momentum Bot on Hyperliquid perpetual DEX, (2) Polymarket-Hyperliquid Statistical Arbitrage combining binary outcomes with perp hedging, (3) Polymarket 5-Minute Whale Copy Bot mirroring K9 Commandant ($5K→$400K), (4) Multi-Signal Breakout/Breakdown Scanner covering 166 crypto symbols + HIP3, and (5) Solana Memecoin Copy Scanner as a research tool. Major debugging includes memory leaks in bot_26.py, Polymarket balance check errors, and HIP3 endpoint issues.

---

## KEY TOPICS

### Strategy 1: Liquidation Momentum Bot (Hyperliquid)

| Parameter | Value |
|-----------|-------|
| **Thesis** | Replicate HLP vault edge ($1K→$118M) by buying/selling around liquidation levels |
| **Data source** | Moon Dev API — liquidation levels from Binance, OKX, Hyperliquid |
| **Entry trigger** | Specific liquidation level is hit |
| **Risk controls** | Max X% of account per trade; 3% daily loss cap |
| **Implementation** | Python (bot_26.py), ThreadPoolExecutor with 10 threads, 10-minute cycles |
| **Accounts** | 3 running simultaneously |
| **Session P&L** | +3, +3, -0.38, +2.4, -2.8, +11, +3, +4 ≈ +5 net |

**Debugging:** Memory leak — DataFrames not garbage collected between cycles, CSV files read repeatedly. Fixed with `gc.collect()`, explicit DataFrame deletion.

### Strategy 2: Polymarket-Hyperliquid Statistical Arbitrage

| Parameter | Value |
|-----------|-------|
| **Thesis** | Delta-neutral stat arb: buy cheap 5-minute binary options + hedge with perps |
| **Leg 1 (Polymarket)** | Buy BOTH sides of 5-min BTC up/down binary (~$1 total per pair) |
| **Leg 2 (Hyperliquid)** | Partial inverse position as hedge (NOT 1:1 — binary payoff is nonlinear) |
| **Hedge ratio** | 20-50% (40% nominal = 80% effective with 50/50 allocation) |
| **Sizing** | $15 Polymarket / $10 minimum Hyperliquid |
| **Unleash trigger** | Remove hedge when liquidation cascade signals directional move |
| **Hold** | To expiry on binary side |
| **Key gotcha** | Hyperliquid minimum $10 — always round UP to $10.01, never down |
| **Balance check** | Use CLOB `get_allowance`, not on-chain USDC (returns $0) |

### Strategy 3: Polymarket 5-Minute Whale Copy Bot

| Parameter | Value |
|-----------|-------|
| **Target wallet** | K9 Commandant ($5K→$400K on Polymarket) |
| **Polling** | Every 10 seconds for new positions |
| **Filter** | Only 5-minute expiry markets; skip expired/resolved/stale |
| **Action** | Buy both sides (up and down), mirroring target's asymmetric approach |
| **Cost** | Under $1 per pair |
| **Hold** | To expiry |
| **Variant** | Liquidations Bot 5-Min — uses Moon Dev API signals instead of whale copying |

### Strategy 4: Multi-Signal Breakout/Breakdown Scanner

| Parameter | Value |
|-----------|-------|
| **Timeframe** | 15-minute candles, 7-day lookback |
| **Coverage** | 166 crypto symbols (filtered to top 95 by volume, ~64 actively scanned) + 10 HIP3 symbols |
| **Core signals (+2 pts each)** | Bollinger Band breach, Donchian Channel breach (7-day rolling) |
| **Confirmation signals** | Volume spike (>2x average), RSI, Rate of Change (ROC) |
| **Output** | Top 10 breakouts + top 10 breakdowns |
| **Data** | Moon Dev API for tick data; direct Hyperliquid API for HIP3 backfill |
| **Example signals** | ETH breakdown, RLC breakup (+27%), ZRO breakup |

### Strategy 5: Solana Memecoin Copy Scanner

| Parameter | Value |
|-----------|-------|
| **Function** | Research/discovery tool, not pure profit bot |
| **Method** | Watch follow-list wallets via API, buy tokens based on algorithm |
| **Position size** | $1 (research scale) |
| **Companion bots** | "Sell losers" bot + "refunds" bot (Solana account close/rent reclamation) |
| **Performance** | "Very profitable when Solana season was here"; currently costs couple hundred $/month as scanner |
| **Risk** | Most tokens are rug pulls — acknowledged as riskiest strategy |

---

## TECHNICAL IMPLEMENTATION

| Component | Detail |
|-----------|--------|
| **Language** | Python (tflow conda environment) |
| **AI coding** | Claude Code Opus 4.6 (3 instances simultaneously) |
| **Data layer** | Moon Dev API (liquidations, HLP tracking, tick data, 166 symbols + 10 HIP3) |
| **APIs** | Hyperliquid (direct), Polymarket CLOB, Solana RPC |
| **Repos** | 1 public (Hyperliquid data layer) + 2 private |
| **Multi-account** | At least 3 Hyperliquid accounts tracked |
| **Supporting agents** | Guardian Agent (resource monitoring), voice-listening agent, content agent |

---

## RISK MANAGEMENT

- **Daily loss limit:** 3% of account value maximum drawdown
- **Position sizing cap:** Max X% of account per single trade
- **Small research positions:** $1 Solana scanner, $10-$15 Polymarket stat arb
- **Delta-neutral hedging:** Polymarket binary + Hyperliquid perp shorts
- **Capped binary downside:** $1 max loss per Polymarket pair
- **Leverage discipline:** Warns against 40x leverage — 99% of followers still hand-trade with it
- **RBI System:** Research → Backtest → Implement/Incubate — never deploy without this process

---

## PERFORMANCE NUMBERS

| Metric | Value |
|--------|-------|
| Liquidation bots (session) | ~+5 net across trades |
| K9 Commandant (whale target) | $5K→$400K on Polymarket |
| HLP vault | $1K seed → $118M |
| John Arnold (inspiration) | 100%+ annualized returns for 10 years, made Enron $750M in 2001 |

---

## TOOLS & PLATFORMS MENTIONED

| Tool/Platform | Purpose |
|---------------|---------|
| Hyperliquid | Perpetual futures trading, HLP monitoring, liquidation data |
| Polymarket | Binary outcome markets (5-minute BTC up/down) |
| Solana | Memecoin trading, copy bot |
| Claude Code (Opus 4.6) | AI coding assistant (3 instances simultaneously) |
| MiniMax 2.5 | Budget alternative to Claude ($10/mo vs $200/mo) |
| Moon Dev API | Custom institutional-grade data node |
| Python (tflow env) | Bot runtime |
| VS Code | Code editor |
| GitHub | 1 public + 2 private repos |
| OpenClaw | Referenced as separate AI agent tool |

---

## ACTIONABLE TAKEAWAYS

1. **Liquidation-based trading is a proven edge** — HLP vault proves concept at $118M scale
2. **Stat arb across Polymarket + Hyperliquid is viable** — buy both sides of cheap binaries, hedge with fractional perps
3. **Multi-signal breakout scanning** — combine BB + Donchian as primary, volume/RSI/ROC as confirmation
4. **Copy bots work as research tools** — $1 positions discover trends; human judgment scales winners
5. **Memory management matters for 24/7 bots** — explicitly delete DataFrames, add `gc.collect()`
6. **Risk controls must be hard-coded** — daily 3% max loss, position size caps, leverage limits built into bot
7. **Environment variable hygiene** — model overrides can silently persist; open new terminals to clear
8. **RBI (Research, Backtest, Implement)** is the workflow — never skip to live trading

---

*Analysis derived from: I Built 3 Trading Bots That Run 24⧸7 (Here's What They Made While I Slept).txt*
