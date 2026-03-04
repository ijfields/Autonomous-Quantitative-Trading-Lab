# Claude in Chrome For Trading - Complete Transcript Analysis

**Video Title:** Claude in Chrome For Trading
**Channel:** Moon Dev
**Video ID:** gvNCcrpzA9k
**Upload Date:** 2026-03-03
**Duration:** ~3h28m
**Speaker:** Moon Dev
**Platform:** YouTube (livestream)

---

## EXECUTIVE SUMMARY

A 3.5-hour livestream where Moon Dev demonstrates the Claude in Chrome browser extension for trading workflows, launches three automated liquidation-based trading bots on Hyperliquid, updates his Electron-based Quant App (Mundave App), explores Anthropic Academy's 13 free courses on Claude Code skills/MCP, discusses geopolitical events (Iran/US conflict) and their market implications (oil, gold, crypto), and delivers an extended sales pitch for his Algo Trade Camp lifetime all-access package ($1,795). The session showcases a multi-AI-instance workflow where several Claude browser agents run simultaneously as specialized "employees" while Moon Dev codes via separate Claude Code terminals.

---

## KEY TOPICS

### Claude in Chrome Extension

- **What it is:** Browser extension that lets Claude interact directly with web pages (click, scroll, navigate, read content)
- **Demo use cases:**
  - Navigating Polymarket to find top 10 "no" bets
  - Running backtests in-browser
  - Reading the Mundave roadmap page
- **Comparison to OpenClaw:** Claude in Chrome is "100x better" for browser-specific tasks
- **Multi-instance workflow:** Multiple Claude browser tabs as parallel "employees" — one doing legal research, one marketing, one financial research — all simultaneously
- **Limitation:** Best for browser-native tasks; OpenClaw better for system-wide multi-tool orchestration

### Liquidation-Based Trading Bots (3 Launched Live)

#### Bot 1: Liquidation Market Maker (Mean Reversion)
- **Strategy:** Fade the crowd when one side is heavily stacked near liquidation
- **Entry conditions (3 required):**
  1. Skew threshold met (one-sided liquidation buildup)
  2. Price within 48-hour range zone
  3. Aggregate position size exceeds minimum
- **Risk management:**
  - Stop-loss: 25% (modified down from 50% during stream)
  - Max loss per trade: 25% of margin
  - Position size: 95% of balance
  - 1% from price to position = $95
- **Tracking:** CSV auto-logging of every entry/exit

#### Bot 2: Hyper Momentum (Cascade Riding)
- **Strategy:** Ride liquidation cascades — enter with momentum when mass liquidations trigger
- **Key finding:** 300-second minimum hold produces 64% win rate vs 36% under 5 minutes
- **Take profit:** 10%
- **Stop-loss:** 10%
- **Position size:** 95% of balance

#### Bot 3: Liquidation Momentum RP (Reverse Protection)
- **Strategy:** Same core logic as Hyper Momentum but filters out bad entries BEFORE taking them (pre-entry filter) rather than using time delay to solve bad entries
- **Running on:** Account 2 (separate from Bots 1 and 2)
- **Risk parameters:** Similar to Hyper Momentum (TP 10%, SL 10%)

### Mundave App / Quant App (Electron)

- **Platform:** Electron (same tech as VS Code, Discord, Slack, Figma, Notion)
- **Features demonstrated:**
  - Position tracking (crypto and HIP3/pre-market perps now separated)
  - Data downloading (server-side bug fixed during stream)
  - Trade history for any Hyperliquid wallet address
  - Liquidation level visualization (Binance, OKX, Hyperliquid)
  - HLP (Hyperliquid market maker) trade tracking
  - Smart money call analysis
- **Updates made during stream:**
  - API endpoints split: crypto-only, HIP3-only, and combined "all"
  - Dropdown defaults to crypto, with 5-item recents section
  - Data download bug fixed (server-side response handling)
  - New version pushed (v1.777)
- **Auto-update discussion:** Discord model (private update server via Electron Updater with generic endpoint, not public GitHub releases)

### Gamified Coding Dashboard
- **2-minute decay bar:** Drains from 120 to zero, resets and loops forever
- **Points system:** Score tracks productivity, penalty on decay timeout (subtract 1 point, never goes negative)
- **15-minute efficiency pop-up:** Fires on schedule for self-assessment
- **Lock-out:** Only manual — no auto lock-out or score-zero kill switch

### Mundave API / Hyperliquid Data Layer
- **What it provides:**
  - All liquidation levels across exchanges (Binance, OKX, Hyperliquid)
  - HLP (Hyperliquid's market maker) trade-by-trade tracking
  - Win/loss analysis for any Hyperliquid trader address
  - Position data with crypto vs HIP3 separation
  - 18 months of historical liquidation data
- **Pricing context:** Claims Coin Glass charges $900/month for 12 days of similar data
- **Access:** Via private Zoom streams ($5/day or lifetime offer)

### Anthropic Academy (13 Free Courses)
- **Discussed courses:**
  - Claude Code in Action (CLI automation)
  - Building with the API (full API guide)
  - Introduction to Agent Skills
  - Intro to MCP
  - Building MCP Servers and Clients in Python
  - MCP Advanced Topics
  - AI Fluency Framework and Foundations
- **Moon Dev's assessment:** Claude Code in Action, API, and MCP courses are "heavy hitters" for building autonomous agents

### Claude Code Skills Discussion
- **Skills mentioned:**
  - GSD ("Get Stuff Done") — "significantly multiply your output"
  - Ora Superpowers — "putting Claude Code on steroids" when paired with GSD
  - Skill Creator Skill — creates new skills from recurring workflows
  - CL Memory — tree of branching folders for niche/specific memories
  - REM Sleep — background sub-agent reads conversation transcript and stores info
  - Recall — background sub-agent retrieves stored context
- **Key insight:** Skills are folders of instructions (SKILL.md) that activate automatically based on description matching, unlike CLAUDE.md (always loaded) or slash commands (explicit invocation)

### Geopolitical / Market Analysis
- **Iran/US conflict (Day 4 as of March 3):**
  - Decapitation strike killed Iran's Supreme Leader
  - Iran retaliating: missile strikes on GCC, Dubai airports closed
  - Strait of Hormuz "effectively paralyzed" — blocks 20% of world's oil supply
- **Market implications:**
  - Oil (CL): Up 8% to $83, analysts see Brent at $100-$150 if Hormuz stays blocked
  - Strategy: Long oil/gas extended, short Mag 7 leaders (Moon Dev disagrees — "buy Mag 7 till the day I die")
  - Iran's goal: Bankrupt the West by disrupting petrodollar cycle
  - GCC sovereign wealth fund divestment could trigger US stock market depression
- **Dexter:** Mentioned by community member as "Claude Code for Financial Research" — autonomous financial research agent

### Solana Bot Updates
- **40x winner** on "what the dog doing" meme coin
- Copy bot running with $1 position size
- Rent reclamation from old Solana positions

---

## TIMESTAMPED SEGMENTS (Approximate)

| Timestamp | Topic |
|-----------|-------|
| 0:00-0:30 | Stream intro, Claude in Chrome extension demo begins |
| 0:30-1:00 | Polymarket navigation demo, OpenClaw vs Claude in Chrome comparison |
| 1:00-1:20 | Multiple Claude browser instances as employees, Solana bot 40x update |
| 1:20-1:40 | Liquidation Market Maker bot setup and launch, P&L calculations |
| 1:40-2:00 | Hyper Momentum bot setup and launch, 300s hold finding |
| 2:00-2:10 | Gamified coding dashboard (decay bar, points system) |
| 2:10-2:20 | Third bot (Liquidation Momentum RP) setup and launch |
| 2:20-2:30 | Electron app discussion (auto-update like Discord), Mundave app updates |
| 2:30-2:40 | API endpoint separation (crypto vs HIP3), documentation updates |
| 2:40-2:50 | Iran/US war analysis, oil market implications, Strait of Hormuz |
| 2:50-3:00 | Anthropic Academy courses, Claude Code skills discussion |
| 3:00-3:28 | Algo Trade Camp sales pitch, Q&A, sign-off |

---

## TOOLS & PLATFORMS MENTIONED

| Tool/Platform | Purpose |
|---------------|---------|
| Claude in Chrome | Browser extension for AI-powered web interaction |
| Claude Code | Terminal-based AI coding agent |
| OpenClaw | Open-source AI agent framework (compared unfavorably for browser tasks) |
| Electron | Desktop app framework (Quant App built on this) |
| Hyperliquid | Crypto exchange (primary trading venue) |
| Mundave API | Custom Hyperliquid data layer (liquidations, positions, HLP) |
| Mundave App (Quant App) | Electron desktop app for position tracking and data analysis |
| Polymarket | Prediction market (demonstrated with Claude in Chrome) |
| Coin Glass | Liquidation data provider (expensive alternative to Mundave API) |
| Interactive Brokers | Broker for stocks/forex/futures data |
| Data Bento | Paid market data provider (NQ data alternative) |
| Cherry Servers | VPS hosting for production bots |
| Anthropic Academy | Free courses on Claude Code, MCP, API |
| Dexter | Financial research agent (mentioned by community) |
| TradeZella / Apex | Trading platforms/prop firms (mentioned in passing) |
| GSD / Ora Superpowers | Claude Code skills for productivity |

---

## STRATEGIES EXTRACTED

### 1. Liquidation Market Maker Bot (Mean Reversion)

| Parameter | Value |
|-----------|-------|
| Type | Mean reversion |
| Market | Crypto (Hyperliquid) |
| Data dependency | Mundave API (liquidation levels) |
| Entry signals | Skew threshold + 48h price zone + aggregate size |
| Stop-loss | 25% of margin |
| Position size | 95% of balance |
| Tracking | CSV auto-log |
| Automation feasibility | HIGH (already automated, requires Mundave API) |

### 2. Hyper Momentum Bot (Cascade Riding)

| Parameter | Value |
|-----------|-------|
| Type | Momentum / trend following |
| Market | Crypto (Hyperliquid) |
| Data dependency | Mundave API (liquidation cascades) |
| Key rule | 300-second minimum hold (64% vs 36% win rate) |
| Take profit | 10% |
| Stop-loss | 10% |
| Position size | 95% of balance |
| Automation feasibility | HIGH (already automated, requires Mundave API) |

### 3. Liquidation Momentum RP (Reverse Protection)

| Parameter | Value |
|-----------|-------|
| Type | Momentum with pre-entry filter |
| Market | Crypto (Hyperliquid) |
| Differentiation | Filters bad entries before taking them (vs time delay) |
| Take profit | ~10% |
| Stop-loss | ~10% |
| Automation feasibility | HIGH (already automated, requires Mundave API) |

### 4. Capitulation Long-Only Bot (Conceptual)

| Parameter | Value |
|-----------|-------|
| Type | Long-only accumulation |
| Trigger | Mass liquidation events detected via API |
| Philosophy | Buy when everyone else panics |
| Timeframe | Swing (5-6 triggers per year) |
| Target | BTC, Amazon, or any long-conviction asset |
| Automation feasibility | MEDIUM (requires liquidation data feed) |

---

## ACTIONABLE TAKEAWAYS

1. **Claude in Chrome > OpenClaw for browser tasks** — If your workflow involves web scraping, form filling, or navigating web apps, Claude in Chrome is far more effective than OpenClaw
2. **Multi-Claude-instance workflow** — Run multiple Claude browser tabs as specialized workers (research, legal, marketing) while Claude Code handles terminal/coding tasks
3. **300-second minimum hold rule** — For momentum-based liquidation trades, holding at least 5 minutes dramatically improves win rate (64% vs 36%)
4. **Pre-entry filtering > time delay** — The RP bot's approach of filtering bad entries before execution outperforms the time-delay approach to avoiding bad entries
5. **95% position sizing with tight stops** — Moon Dev's bots use near-full-balance positions with 10-25% stop-losses (extremely aggressive, high-risk)
6. **Separate data endpoints by asset class** — When building trading apps, keep crypto, pre-market perps, and other asset types in separate API endpoints to avoid data contamination
7. **Electron for cross-platform trading tools** — VS Code, Discord, and Slack all use Electron; viable for building custom trading dashboards
8. **Anthropic Academy courses** — Free resource for learning Claude Code skills, MCP server building, and API integration
9. **Claude Code Skills** — GSD + Ora Superpowers combination recommended for maximum productivity; Skill Creator Skill for automating recurring workflows
10. **Capitulation bot concept** — For long-only investors: automate buying during mass liquidation events (5-6x/year) instead of buying at arbitrary prices

---

## CONTENT BREAKDOWN

| Category | Approximate % |
|----------|--------------|
| Claude in Chrome demo & multi-agent workflow | 15% |
| Bot setup & launch (3 liquidation bots) | 20% |
| Quant App / Mundave API updates | 15% |
| Geopolitical analysis (war, oil, markets) | 10% |
| Claude Code skills & Anthropic Academy | 10% |
| Sales pitch (Algo Trade Camp lifetime offer) | 25% |
| Community interaction / tangents | 5% |

*Analyzed from: Claude in Chrome For Trading.txt*
