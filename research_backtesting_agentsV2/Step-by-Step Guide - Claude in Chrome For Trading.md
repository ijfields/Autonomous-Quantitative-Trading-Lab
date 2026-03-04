# Step-by-Step Guide: Claude in Chrome for Trading + Liquidation Bot Setup

**Source:** Moon Dev (YouTube)
**Video ID:** gvNCcrpzA9k
**Upload Date:** 2026-03-03

---

## What This Guide Covers

How to use Claude in Chrome for trading research workflows, run multiple Claude browser instances as parallel AI workers, and set up liquidation-based automated trading bots on Hyperliquid using Moon Dev's Mundave API for liquidation data.

---

## Part 1: Claude in Chrome for Trading Research

### Step 1: Install Claude in Chrome

1. Install the Claude in Chrome browser extension from the Chrome Web Store
2. Pin the extension to your toolbar for quick access
3. Sign in with your Anthropic account

### Step 2: Use Claude to Navigate Trading Platforms

1. Open a trading-relevant website (e.g., Polymarket, TradingView, exchange dashboard)
2. Activate Claude in Chrome
3. Give natural language commands:
   - "Find me the top 10 'no' bets on Polymarket"
   - "Read the roadmap on this page and summarize it"
   - "Navigate to the backtesting section and run a backtest"
4. Claude can click, scroll, read, and interact with the page directly

### Step 3: Run Multiple Claude Browser Instances

1. Open separate Chrome tabs for each task
2. Assign each Claude instance a specialized role:
   - **Tab 1:** Financial research (reading market data, analyzing charts)
   - **Tab 2:** Legal/compliance research
   - **Tab 3:** Marketing or content creation
   - **Tab 4:** Data collection and scraping
3. All instances run simultaneously and independently
4. Check back on each tab for completed work

**Key insight:** Claude in Chrome is "100x better" than OpenClaw for browser-specific tasks. OpenClaw is better for system-wide orchestration across files, terminals, and APIs.

---

## Part 2: Liquidation-Based Trading Bots

### Prerequisites

- **Hyperliquid account** with funds deposited
- **Mundave API key** (available via Moon Dev's Zoom streams or lifetime offer)
- **Python** installed with required libraries
- **VPS server** recommended for production (Cherry Servers, Contabo, Hetzner, etc.)

### Step 4: Understand the Liquidation Data Layer

Moon Dev's Mundave API provides:
- **Liquidation levels** across exchanges (Binance, OKX, Hyperliquid)
- **Position data** separated by crypto and HIP3 (pre-market perps)
- **HLP tracking** (Hyperliquid's market maker trades)
- **Trade history** for any wallet address on Hyperliquid
- **18 months** of historical liquidation data

API endpoints (as updated during stream):
```
/positions.json       → All positions (crypto + HIP3)
/positions_crypto.json → Crypto perpetuals only
/positions_hip3.json  → HIP3/pre-market perps only
```

### Step 5: Set Up the Liquidation Market Maker Bot (Mean Reversion)

**Strategy:** Fade the crowd when one side is heavily stacked near liquidation.

**Entry conditions (ALL 3 required):**
1. **Skew threshold met** — One-sided liquidation buildup detected (longs or shorts heavily dominant)
2. **48-hour price zone** — Current price is within the 48-hour price range (not at extremes)
3. **Aggregate position size** — Total position size exceeds minimum threshold

**Risk parameters:**
| Parameter | Value |
|-----------|-------|
| Position size | 95% of balance |
| Stop-loss | 25% of margin |
| Max loss per trade | 25% |

**Tracking:** Bot auto-logs every entry/exit to CSV file.

### Step 6: Set Up the Hyper Momentum Bot (Cascade Riding)

**Strategy:** Ride liquidation cascades — enter with momentum when mass liquidations trigger.

**Critical rule:** Minimum hold time of 300 seconds (5 minutes).
- Trades held 300+ seconds: **64% win rate**
- Trades held under 5 minutes: **36% win rate**

**Risk parameters:**
| Parameter | Value |
|-----------|-------|
| Position size | 95% of balance |
| Take profit | 10% |
| Stop-loss | 10% |
| Minimum hold | 300 seconds |

### Step 7: Set Up the Liquidation Momentum RP Bot (Reverse Protection)

**Strategy:** Same core logic as Hyper Momentum but with pre-entry filtering instead of time delay.

**Key difference from Hyper Momentum:**
- Hyper Momentum: Takes the trade, then uses time delay (300s hold) to solve bad entries
- RP version: Filters out bad entries BEFORE taking them (pre-entry quality check)

**Risk parameters:** Same as Hyper Momentum (10% TP, 10% SL, 95% position size)

**Run on a separate account** to isolate P&L tracking from other bots.

### Step 8: Launch and Track Bots

1. Run each bot from terminal: `python bot_script.py`
2. Each bot auto-logs trades to CSV:
   - `liquidation_mm_trades.csv`
   - `hyper_momentum_trades.csv`
   - `liq_momentum_rp_trades.csv`
3. Check results the next day via CSV or Google Sheets
4. Monitor for errors during incubation period

---

## Part 3: Moon Dev's Bot Development Workflow

### Step 9: Follow the Research → Backtest → Incubate → Deploy Pipeline

```
1. Research
   └── Find ideas from books, papers, streams, community
        ↓
2. Backtest
   └── Validate strategy works on historical data
        ↓
3. Incubate (Small Size, On Screen)
   └── Run live with small positions
   └── Fix bugs as they appear
   └── Monitor P&L daily
        ↓
4. Deploy (Server)
   └── Move proven bot to VPS server
   └── Reason 1: Uptime (power outages, internet drops)
   └── Reason 2: Prevent tinkering with working system
```

**Key insight:** The incubation stage serves two purposes — testing profitability AND catching bugs. Only move to server after both are validated.

### Step 10: Build a Capitulation Long-Only Bot (Conceptual)

For long-term investors who want algorithmic entries:

1. **Set up liquidation data feed** via Mundave API
2. **Define "mass liquidation" threshold** — large aggregate liquidation events (5-6 per year)
3. **When threshold triggers:** Auto-buy your long-conviction asset (BTC, SPY, AMZN, etc.)
4. **Philosophy:** Buy when everyone else is panicking and getting liquidated
5. **Advantage over DCA:** You accumulate at capitulation prices instead of arbitrary intervals

---

## Quick Reference: Claude in Chrome vs OpenClaw

| Feature | Claude in Chrome | OpenClaw |
|---------|-----------------|----------|
| Browser interaction | Excellent (native) | Limited |
| File system access | None | Full |
| Multi-tool orchestration | Browser only | System-wide |
| Multi-agent scaling | Multiple tabs | Agent swarms |
| Setup complexity | Extension install | Full server setup |
| Best for | Web scraping, research, form filling | Coding, file ops, API chains |

---

## Key Tools Mentioned

| Tool | Purpose |
|------|---------|
| Claude in Chrome | Browser-based AI agent |
| Claude Code | Terminal AI coding agent |
| Mundave API | Liquidation data layer for Hyperliquid |
| Mundave App (Quant App) | Electron desktop app for trade monitoring |
| Electron | Cross-platform desktop app framework |
| Cherry Servers / VPS | Production bot hosting |
| Anthropic Academy | Free Claude Code/MCP/API courses |
| GSD + Ora Superpowers | Claude Code skills for productivity |
| Dexter | Financial research agent (third-party) |

---

## Recommended Claude Code Skills

| Skill | Purpose |
|-------|---------|
| GSD (Get Stuff Done) | Multiplies coding output |
| Ora Superpowers | Enhances Claude Code capabilities (pair with GSD) |
| Skill Creator Skill | Auto-creates new skills from recurring workflows |
| CL Memory | Branching folder tree for persistent niche memories |
| REM Sleep | Background sub-agent that reads and stores conversation context |
| Recall | Background sub-agent that retrieves stored context |

*Guide derived from: Claude in Chrome For Trading.txt*
