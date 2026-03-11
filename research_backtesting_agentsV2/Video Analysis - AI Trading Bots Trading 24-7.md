# AI Trading Bots Trading 24/7 — Complete Transcript Analysis

**Video Title:** AI Trading Bots Trading 24/7
**Channel:** Moon Dev
**Video ID:** VKaJcKNj-qM
**Upload Date:** 2026-03-10
**Duration:** ~107m (~6442s)
**Speaker:** Moon Dev
**Platform:** YouTube (live stream)

---

## EXECUTIVE SUMMARY

A live coding stream where Moon Dev runs three Claude Code (Opus 4.6) instances simultaneously to build and debug multiple AI trading bots. The session covers three major construction projects: (1) a breakout/breakdown scanner across 131 symbols (95 crypto + 36 HIP3) using multi-signal scoring (Bollinger Bands, Donchian Channels, volume spikes, RSI, rate of change), (2) a Polymarket-Hyperliquid statistical arbitrage bot that buys cheap 5-minute binary options while hedging on Hyperliquid perps with a "liquidation unleash" trigger, and (3) updates to the Mundev API to add HIP3 tick data. Moon Dev also debugs memory leaks in existing bots, discusses his Solana token scanner, promotes his Algo Trade Camp, and shares his philosophy on automated trading as the only viable path for retail.

---

## KEY TOPICS

### Live Bot Portfolio (Running During Stream)

| Bot | Exchange | Description | Status |
|-----|----------|-------------|--------|
| Liquidation Momentum Bot | Hyperliquid | Buys at liquidation levels, 24/7 | Running, profitable (+5 net on session) |
| Bot 26 (Solana Follow-List) | Solana | Token scanner, buys trending tokens early | Running, memory leak fixed |
| 5-Minute Copy Bot | Polymarket | Copies whale wallet "K9 Commandant" ($5K→$400K) | Running |
| Liquidations Bot (5-min) | Polymarket | Trades around liquidation events using Mundev API | Running |
| Breakout/Breakdown Scanner | Hyperliquid + HIP3 | Multi-signal breakout detection across 131 symbols | Built during stream |
| Stat Arb Bot | Polymarket + Hyperliquid | Delta-neutral binary + perp hedge with unleash trigger | Built during stream |

### Breakout/Breakdown Scanner

- **Data:** 15-minute candles over 7 days
- **Coverage:** 95 crypto symbols + 36 HIP3 symbols = 131 total
- **Multi-signal scoring (+2 points each for heavy signals):**

| Signal | Description |
|--------|-------------|
| Bollinger Band breach | Price closes above upper or below lower band |
| Donchian Channel (7-day) | Rolling high/low breach — at literal 7-day extreme |
| Volume spike | Volume exceeds 2x average |
| RSI | Overbought/oversold levels |
| Rate of Change | Momentum confirmation |

- **Data sources:** Mundev API primary, direct Hyperliquid API as backfill when Mundev lacks 7 days of history
- **Findings during stream:** ETH in breakdown signal, RLC breakout (+27%), ZRO breakout

### Polymarket-Hyperliquid Statistical Arbitrage Bot

| Parameter | Value |
|-----------|-------|
| Leg 1 (Polymarket) | 5-minute BTC up/down binary market, $15 position |
| Leg 2 (Hyperliquid) | Partial inverse hedge, $10 minimum (always round to $10.01) |
| Total exposure | ~$25 per trade pair |
| Hedge ratio | 20–50% (not 1:1 due to nonlinear binary payoff) |
| Delta neutral intent | If BTC dumps, Polymarket loss offset by Hyperliquid short profit |
| Unleash trigger | Remove hedge when liquidation cascade data signals a big move |
| Timing constraint | Hyperliquid position must open/close within same 5-minute window |
| Cost considerations | Funding rates + spread on Hyperliquid eat into guaranteed spread |

### 5-Minute Copy Bot (Polymarket)

- Copies whale wallet "K9 Commandant" who turned $5K into $400K
- Polls target wallet every 10 seconds for new positions
- Filters to 5-minute markets only
- Skips expired, resolved, or stale positions
- Buys both sides (up and down), mirroring target's asymmetric strategy
- Combined cost under $1 per pair

### Liquidation Momentum Bot

- Runs on Hyperliquid 24/7
- Monitors where other traders get liquidated, then buys at those levels
- Uses Mundev API to track HLP positions (started $1K → now $118M)
- Risk controls: max % of account per trade, max 3% daily loss
- Session P&L: +3, +3, -0.38, +2.4, -2.8, +11, +3, +4 = ~+5 net

### Solana Token Scanner Bot

- Runs 24/7 scanning Solana for trending tokens
- Buys tokens early to see what "flows to the top"
- Costs a couple hundred dollars per month to operate
- "Very very profitable" during Solana season; currently taking losses
- Kept running for research purposes

### Memory Leak Debugging

- Bot 26 accumulated 331 MB from data frames not being garbage collected between 10-minute cycles
- Thread pools not properly cleaned up
- Fixed by adding explicit garbage collection and DataFrame cleanup

### Model Switching Issues

- Accidentally got stuck on MiniMax 2.5 due to environment variable overrides
- Spent time debugging and switching back to Opus 4.6
- MiniMax: $10/month vs Opus: $200/month — cheaper but less capable

---

## TOOLS & PLATFORMS MENTIONED

| Tool/Platform | Purpose |
|---------------|---------|
| Claude Code (Opus 4.6) | Primary AI coding assistant — 3 instances running simultaneously |
| MiniMax 2.5 | Alternative cheaper LLM ($10/month), tested during stream |
| DeepSeek | Alternative LLM option configured with Claude Code |
| Hyperliquid | Decentralized perp futures exchange — main trading venue |
| HIP3 | Hyperliquid's traditional assets section (stocks, commodities) |
| Polymarket | Prediction/binary options market — 5-minute BTC bets |
| Mundev API | Custom Hyperliquid data layer — liquidation data, HLP tracking, tick data (166 crypto + 10 HIP3 symbols) |
| HLP ($118M vault) | Hyperliquid Liquidity Provider — Moon Dev tracks all positions |
| Solana | Blockchain for token scanner bots |
| Python (TFlow environment) | Runtime for all bots |
| Guardian Agent | AI agent monitoring computer resources |
| Voice-listening Agent | Listens to speech and generates ideas |
| Short-video Agent | Finds highlights from streams, creates clips |
| Fireflies.ai | AI meeting recorder (kicked from stream for privacy) |
| Algo Trade Camp ($1,795) | Moon Dev's course — 4 Polymarket bots, lifetime access |
| Mundev API key (18 months) | Included with course — liquidation data valued at ~$10K |
| Daily Zoom ($5) | Private live streams with screen visible |

---

## KEY NUMBERS

| Metric | Value |
|--------|-------|
| HLP vault size | $118 million (from $1K seed) |
| Active symbols scanned | 131 (95 crypto + 36 HIP3) |
| HIP3 tick data symbols | 10 (top by volume) |
| Crypto tick data symbols | 166 |
| Stat arb exposure per trade | ~$25 ($15 Polymarket + $10 Hyperliquid) |
| Hyperliquid minimum trade | $10 (must send $10.01 to avoid rejection) |
| K9 Commandant whale | $5K → $400K |
| Bot 26 memory leak | 331 MB accumulated |
| Bot cycle time | 10 minutes |
| API threads | 10 parallel |
| Polymarket portfolio | $546 ($470 balance + $70 cash) |
| Algo Trade Camp price | $1,795 (lifetime, 90-day money back) |
| Completion rate | 50% of enrollees |
| Moon Dev followers | 150K+ (100K YouTube, 50K Twitter) |
| John Arnold reference | $750M for Enron in 2001, $3B total, youngest billionaire by 2007 |

---

## PHILOSOPHY & INSIGHTS

- **"Code is the great equalizer"** — anyone can build what institutions have
- **99% of followers still hand-trade at 40x leverage** — Moon Dev sees this as doomed
- **Liquidation data is the real edge** — Hyperliquid opened up financial system order flow
- **Alpha decay** — can't give away plug-and-play bots; the edge disappears when everyone runs them
- **Automated trading is the only way** — manual trading doesn't scale
- **John Arnold model:** Inch-wide, mile-deep focus; emotional detachment; consistent compounding
- **Chasing Jim Simons' $31 billion legacy**

---

## ACTIONABLE TAKEAWAYS

1. **Multi-signal breakout scanner** — combine Bollinger Bands, Donchian Channels, volume spikes, RSI, and rate of change across 131+ symbols for high-confidence breakout detection
2. **Stat arb between Polymarket and Hyperliquid** — buy cheap 5-min binary options, hedge with partial perp position, unleash during liquidation cascades
3. **Copy whale wallets on Polymarket** — poll every 10 seconds, filter to 5-minute markets, buy both sides
4. **Trade around liquidation levels** — use HLP position data and liquidation cascade signals as entry triggers
5. **Always round up to $10.01 on Hyperliquid** — $9.99 gets rejected at minimum
6. **Fix memory leaks in long-running bots** — explicit garbage collection and DataFrame cleanup between cycles
7. **Use Mundev API as backfill source** — primary for tracked symbols, fall back to direct Hyperliquid API for symbols with insufficient history

---

## SOURCE QUOTES

> "Code is a great equalizer."

> "99% of you are still hand trading with 40x leverage."

> "We don't predict price — we predict which liquidation to buy."

> "Alpha decay is real. I can't just hand you a plug-and-play bot."

> "Hyperliquid opened up the financial system's order flow. That's the edge."

*Analysis derived from: 🧠 AI Trading Bots Trading 24⧸7.txt*
