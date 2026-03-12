# March 11 - Automated Trading Bot Factory — Complete Transcript Analysis

**Video Title:** Automated Trading Bot Factory
**Channel:** Moon Dev
**Video ID:** F8us7omGq8U
**Upload Date:** 2026-03-11
**Duration:** ~2h+ (live stream)
**Speaker:** Moon Dev
**Platform:** YouTube (live stream)

---

## EXECUTIVE SUMMARY

Moon Dev's daily live coding stream where he builds and iterates on multiple trading systems using Claude Code. The main build is a "Liquidation Momentum Stink Bid" bot that trades Polymarket 5-minute BTC binary markets based on liquidation cascade signals from his Mundev API, with partial Hyperliquid hedge — replacing a previous copy-trading strategy after the target wallet (K9 Commandant, $2K→$700K) went dark. He also builds a multi-timeframe breakout scanner (5 timeframes, all Hyperliquid tokens), adds features to his custom Electron desktop app (recent files via git), runs Solana refund recovery, and shares his vision of scaling AI agents across 7+ computers at $1.50/hour each ($92K/year).

---

## KEY TOPICS

### Liquidation Momentum Stink Bid Bot (Main Build)

The K9 Commandant wallet ($2K→$700K) went inactive, forcing a pivot from copy-trading to building an algorithmic signal.

| Parameter | Value |
|-----------|-------|
| Instruments | Polymarket 5-min BTC binary + Hyperliquid BTC perp |
| Signal source | Mundev API — BTC liquidation events (all exchanges combined) |
| Signal trigger | $25K–$100K liquidations in one direction (front end of cascade, not middle/back) |
| Direction logic | $25K+ long liquidations = bearish → buy "Down" on Polymarket; $25K+ short liquidations = bullish → buy "Up" |
| Entry method | Stink bid (limit order) at 30% below current ask on Polymarket |
| Order cancellation | Auto-cancel if < 1 minute remaining in the 5-min market |
| Hedge | Inverse position on Hyperliquid at 40% of position size |
| Position split | 60% Polymarket / 40% Hyperliquid |
| Cycle time | 15 seconds |
| Test size | $15 on one side |
| Bot name | "Poly-Hyper Lick StinkBot" |
| Key variables | `pullback_amount=0.30`, `liquidation_threshold_min=25000`, `liquidation_threshold_max=100000`, `min_time_left=60` |

**Finding Polymarket 5-min markets:** Market URL contains a timestamp (e.g., `17732358800`). Bot predicts the next 5-min window's timestamp to construct the URL programmatically.

### Multi-Timeframe Breakout Scanner

| Parameter | Value |
|-----------|-------|
| Timeframes | 5 (5-min, 1-hour, 4-hour, 6-hour, daily) |
| Data source | Mundev API + Hyperliquid API + HIP3 |
| Bar count | 1,969 bars at 5-minute |
| Instruments | All Hyperliquid-listed tokens (futures + stocks) |
| Signal | Confluence score — tokens breaking out/down on 3+ timeframes |
| Rolling approach | Fetches 5-min data and aggregates to larger timeframes (reduces API calls) |
| Output | Pandas table sorted by confluence score |

**Results during stream:**
- HYPE: 5/5 timeframe confluence (breakout) — "undisputed king"
- Natural gas also flagged
- 10 symbols at 3/3 confluence
- Standalone single-file version (zero imports) also created for sharing

### Quant App Liquidation Trading (Hand-Assisted)

| Parameter | Value |
|-----------|-------|
| Instrument | Hyperliquid perpetuals |
| Leverage | 40x |
| Max position size | $10,000 |
| Max daily loss | 3% of account |
| Performance | $4,900 return on $10K max size (~49% weekly) |
| Track record | 3+ weeks profitable without blowup |
| Edge | HLP ($118M market maker vault) position monitoring |

### Desktop App Updates (Electron — v1.38→v1.39)

- Added "recent files" feature: right-click on project in Code tab shows 5 most recently edited files
- Uses `git status` (uncommitted) + `git log --name-only` (recently committed) under the hood
- Filters out non-code files (CSVs, .DS_Store, .gitignore)
- 3 AI agents consulted on UX approach — all recommended right-click context menu
- Clicking a file pastes full path into active terminal/agent chat
- New .exe and .dmg builds created

### Solana Bot Management

- Ran "sell losers" command on Solana trading bot
- Used "refund tool" to close token accounts and reclaim SOL rent deposits (~$10 USDC recovered)
- Key insight: every Solana trade opens a token account; closing them returns a refund

### AI Agent Infrastructure Vision

| Metric | Value |
|--------|-------|
| Current computers | 5 operational, 2 arriving (7 total) |
| Economics threshold | If agent generates > $1.50/hour, scalable to millions |
| 7 machines at $1.50/hr | $252/day = $92,000/year |
| AI tools running | Claude Code (6 instances simultaneously), OpenClaw |

### Geopolitical/Market Commentary

- US-Israeli conflict day 12 (started Feb 28, 2026)
- IRGC/Strait of Hormuz blockade (20-21M barrel/day choke point)
- Brent crude: hit $119 on days 2-3 → down to $88 by March 10
- Oil and BTC moving inversely — "that's a pattern"
- SPR coordinated release still possible

### Mundev API Data Layer

- All liquidation levels (Hyperliquid, Binance, OKX)
- HLP trade tracking and position data
- Win/loss analysis by wallet address
- Tick data for all tokens
- Top 10 closest liquidations to execution
- Position data for any Hyperliquid address
- Recently added HIP3 tick data
- Valued at $1,000+/month (CoinGlass comparable: $900/month)
- Free API key dropped during each stream

---

## TOOLS & PLATFORMS MENTIONED

| Tool/Platform | Purpose |
|---------------|---------|
| Claude Code ($200/month Max plan) | Primary AI coding assistant — 6 instances simultaneously |
| Mundev API (moondev.com/docs) | Custom Hyperliquid data layer — liquidations, HLP, tick data |
| Hyperliquid | Main trading venue — perpetuals |
| Polymarket | 5-minute BTC binary markets |
| Binance / OKX / Bybit | Liquidation data sources (via Mundev API) |
| Gemini | Thumbnail/image generation exclusively |
| Cling | AI video generation |
| Comfy UI / Stable Diffusion | Local image/video generation |
| Claude in Chrome | Browser automation (Google Sheets, email, research) |
| OpenClaw + Codex 5.2/5.4 | Alternative AI coding setup |
| Minimax | Alternative AI model |
| CoinGlass | Competitor liquidation data ($900/month) |
| Moon Dev Quant App (Electron) | Custom desktop app — v1.39, .exe + .dmg |
| Pandas | Trade tracking via CSV |
| Solana | Token scanner + refund tool |
| Google Scholar | Academic trading strategy papers |

---

## KEY NUMBERS

| Metric | Value |
|--------|-------|
| Weekly trading performance | $4,900 on $10K max (~49%) |
| Polymarket bot win examples | 186%, 170%, 3345%, 241%, 186%, 117%, 113% |
| HLP vault size | $118 million |
| K9 Commandant run | $2K → $700K (now inactive) |
| Liquidation data (during stream) | 822K short liquidations in 10 min (all exchanges) |
| HYPE liquidation example | $1.7M at risk at $36 |
| Breakout scanner bars | 1,969 at 5-min |
| Breakout confluence | 1 symbol at 5/5, 10 symbols at 3/3 |
| Solana refund | ~$10 USDC recovered |
| Computers | 5 operational + 2 arriving = 7 total |
| AI agent target economics | $1.50/hr × 7 machines = $92K/year |
| Cloud plan value | $200/month ≈ $2,000 API equivalent |
| App version | 1.38 → 1.39 |
| Algo Trade Camp price | $1,795 lifetime (or 2× $949) |
| Brent crude range | $119 → $88 |
| Career internet income | Since eBay 2006 (20 years) |
| Estimated spent on developers | $1 million+ |

---

## RBI FRAMEWORK (Research, Backtest, Incubate)

1. **Research** — Find strategies from: Google Scholar papers, Market Wizards books (3-4 volumes), Chat with Traders podcast, YouTube, personal observations
2. **Backtest** — Get OHLCV historical data (Mundev API: 5-min resolution, 100+ weeks). Test strategy against history. Don't trust TradingView backtests alone.
3. **Incubate** — Build a bot that trades SMALL in live markets. Past performance ≠ future results. Deploy with $15 on one side.

---

## ACTIONABLE TAKEAWAYS

1. **Liquidation stink bid strategy** — Use $25K–$100K liquidation cascades as directional signal, place 30% pullback limit orders on Polymarket, hedge 40% on Hyperliquid
2. **Multi-timeframe breakout confluence** — Scan 5 timeframes simultaneously; highest-conviction entries are 3+ timeframe agreement
3. **K9 Commandant wallet went dark** — Copy-trading single wallets is fragile; build your own signals
4. **Solana refund recovery** — Close unused token accounts to reclaim SOL rent deposits
5. **Polymarket URL prediction** — Construct 5-min market URLs from timestamps for automated discovery
6. **AI agent economics** — If agent generates > $1.50/hr, scaling across machines becomes highly profitable
7. **Desktop app productivity** — Use git status/log as "recent files" source (no watchers needed, ~60 lines)
8. **Oil-BTC inverse pattern** — Monitor during geopolitical events

---

## SOURCE QUOTES

> "We don't predict price — we predict which liquidation to buy."

> "If an AI agent can generate more than $1.50 an hour, it becomes scalable to millions of agents."

> "Just because it worked in the past does not mean it works going forward. That's why we incubate small."

> "I've spent an estimated $1 million on developers over my career. Now I use Claude Code instead."

> "This is the biggest opportunity we've ever seen."

*Analysis derived from: March 11 - Automated Trading Bot Factory.txt*
