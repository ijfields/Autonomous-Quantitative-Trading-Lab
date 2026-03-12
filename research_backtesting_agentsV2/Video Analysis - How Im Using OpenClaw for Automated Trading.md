# How I'm Using OpenClaw for Automated Trading (crypto & prediction markets) — Complete Transcript Analysis

**Video Title:** How I'm Using OpenClaw for Automated Trading (crypto & prediction markets)
**Channel:** Coin Bureau Trading
**Video ID:** Oh94XVXkZPM
**Upload Date:** 2026-02-06
**Duration:** ~23m
**Speaker:** Aaron Disher (The Better Traders)
**Platform:** YouTube

---

## EXECUTIVE SUMMARY

Aaron Disher demonstrates using OpenClaw on a dedicated Mac Mini to build a multi-strategy Polymarket trading dashboard. Eight strategies are described ranging from indicator-based (TBT Divergence, TBO Trend Following) to event-driven (Mention Markets, Counter-Trend vs. AI Crowd) to pure arbitrage (buy both sides for <$1.00). All strategies are currently paper trading. Bearish crypto thesis (BTC to $49K) frames Polymarket as a cycle-independent alternative.

---

## KEY TOPICS

### OpenClaw Trading Setup

- Dedicated **Mac Mini** for security (not personal computer)
- Brain dump first: feed OpenClaw your trading experience, interests, goals, strategies, successful accounts to study
- **Cron jobs** for recurring tasks: 9 AM market updates, security audits, price scraping, news scanning
- **Supervisor-agent model**: assign specialized sub-agents for different tasks

### Eight Strategies on the Dashboard

| # | Strategy | Type | Detail |
|---|----------|------|--------|
| 1 | **TBT Divergence** | Contrarian/mean-reversion | Proprietary indicator on 15-min Polymarket crypto charts |
| 2 | **TBO Trend Following** | Trend | Proprietary cloud overlay indicator on 4-hour charts |
| 3 | **Late Entry** | Momentum | Enter in last 3-4 min of 15-min resolution window in direction of prevailing trend |
| 4 | **Counter-Trend vs AI Crowd** | Contrarian | Trade against AI-driven bot consensus; agents crawl web for news/sentiment |
| 5 | **Mention Markets** | Event-driven | Agents study political figures' speech patterns to predict keyword mentions |
| 6 | **Market Maker Bot** | Market-making | Provide liquidity on both sides of Polymarket contracts |
| 7 | **Arbitrage** | Risk-free | Buy both Up and Down when total cost < $1.00 |
| 8 | **Sports Scanner** | Niche scanning | Scan low-volume sports/esports markets for mispriced odds |

### Polymarket as Alternative Venue

- Bearish crypto thesis: BTC heading to $49K
- Polymarket offers cycle-independent opportunities (event markets, mention markets, sports)
- 15-minute crypto resolution windows enable rapid strategy testing

---

## TOOLS & PLATFORMS MENTIONED

| Tool/Platform | Purpose |
|---------------|---------|
| OpenClaw | AI agent for dashboard building, cron jobs, strategy development |
| Polymarket | Primary prediction market venue |
| Kalshi | Alternative prediction market (mentioned, not actively used) |
| TradingView | Charting with proprietary TBO/TBT indicators |
| Mac Mini | Dedicated hardware for OpenClaw |

---

## ACTIONABLE TAKEAWAYS

1. **Brain dump before building** — feed comprehensive context (experience, goals, strategies) to OpenClaw before assigning tasks
2. **Cron jobs for automation** — schedule recurring market updates, security audits, and price scraping
3. **Reverse-engineer successful wallets** — copy profitable Polymarket addresses and have the bot study their edge
4. **Late Entry strategy is most explicit** — enter in last 3-4 min of 15-min window in direction of prevailing trend
5. **Arbitrage when both sides < $1.00** — guaranteed profit regardless of outcome
6. **Paper trade everything first** — Aaron himself is paper trading all strategies
7. **Dedicated machine for security** — never run OpenClaw on your personal computer
8. **Consider LLC structure** — write off hardware, API costs, subscriptions

---

*Analysis derived from: How I'm Using OpenClaw for Automated Trading (crypto & prediction markets).txt*
