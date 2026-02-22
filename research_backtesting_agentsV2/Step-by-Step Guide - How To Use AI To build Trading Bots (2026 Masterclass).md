# Step-by-Step Guide: How To Use AI To Build Trading Bots (2026 Masterclass)

**Source:** Moon Dev (YouTube)
**Video ID:** 3AmL2qcXB5k
**Upload Date:** 2026-01-23

## Prerequisites
- **Software:** Cursor IDE (free tier), Claude Code (terminal-based), Python with backtesting.py library, WhisperFlow (voice-to-text for faster prompting), Git/GitHub, CCXT library (for exchange connections)
- **Hardware:** Computer with terminal access; optionally a VPS/cloud server (Cherry Servers, Hetzner, Vultr, or Kaboot) for 24/7 bot operation (~$50/month)
- **Accounts/API Keys:** Anthropic API key (for Claude Code), OpenRouter or Claude subscription, Hyperliquid account + data layer API key (from mundave.com/docs), GitHub account
- **Knowledge:** Basic Python (or willingness to learn with AI), understanding of trading concepts (leverage, stop-loss, take-profit), willingness to transition from hand trading to algorithmic trading
- **Data:** Access to the Hyperliquid data layer (55+ endpoints: liquidations, positions, whale wallets, order flow, HLP market maker positions, Binance/OKX/Bybit liquidations), Google Scholar for research papers

---

## The RBI System (Research → Backtest → Implement)

This is the speaker's core framework, repeated throughout the 3h33m stream:

| Phase | Action | Time Investment |
|-------|--------|-----------------|
| **R — Research** | Find trading strategy ideas from books, papers, podcasts, YouTube, data analysis, TikTok social arbitrage | Ongoing, daily |
| **B — Backtest** | Code backtests in Python (backtesting.py) to see if strategies work historically | Used to take 8 hours; now minutes with Claude Code |
| **I — Implement** | Build bot with tiny size, run live, iterate. Only implement strategies that pass backtesting | Small size first, scale only after live validation |

> Speaker's tip: "One out of 10 winning backtests is good. Step on the gas. Jim Simons ramped up a net worth of $31 billion. If you think you're going to go one for two, you're cooked."

---

## Part 1: Research — Finding Trading Strategy Ideas

### Step 1: Build an Idea Backlog from Multiple Sources
Maintain a running list of trading strategy ideas (speaker uses Apple Notes).

**Where to find ideas:**
- **Google Scholar:** Search "mean reversion strategy," "trading strategy," etc. for PhD papers
- **Books:** Market Wizards series (all 3-4 books), Chat with Traders podcast (300+ trader interviews), speaker's full book list on the roadmap
- **YouTube/Podcasts:** Listen during commutes, walks, etc. — always be absorbing ideas
- **Proprietary data:** Hyperliquid data layer (liquidations, whale positions, order flow, HLP market maker data)
- **TradingView indicators:** Grab Pine Script code for any indicator → convert to Python for backtesting
- **TikTok/Social arbitrage:** Find consumer trends before Wall Street (e.g., Abercrombie, Crocs, Celsius)

- Expected result: A backlog of 10-30+ strategy ideas to test

### Step 2: Access the Hyperliquid Data Layer
Navigate to mundave.com/docs for API documentation and endpoints.

**Key data available:**
- HIP3 liquidations (last 24 hours, by asset class — including stocks, forex, futures)
- All user positions (19,000+ active wallets with addresses, position sizes, liquidation distances)
- Whale tracking, smart money wallets, order flow
- HLP market maker positions (7 strategies, grew from $1,000 to $183M)
- Binance, OKX, Bybit liquidation data
- Tick data (OHLCV for all symbols including stocks: Apple, AMD, Costco, Google, Anthropic)

- Run examples from the GitHub repo: `python [example_script].py`
- Expected result: Real-time data feeds for idea generation

> Speaker's tip: "As an algorithmic trader, you're always trying to get an edge. One of the best edges you can get is have data that others don't have."

---

## Part 2: AI Workflow — Claude Code Masterclass

### Step 3: Set Up Your AI Coding Environment
The speaker's 2026 AI toolkit progression:

1. **Beginner:** ChatGPT on web → copy/paste code (2023 era)
2. **Intermediate:** Cursor IDE (free fork of VS Code with built-in AI) — good starting point, supports all models (Opus, Sonnet, GPT, Grok)
3. **Advanced:** Claude Code in terminal — the speaker's primary tool

- Install Claude Code on your terminal
- Set up WhisperFlow (whisperflow.ai) for voice-to-text prompting — goes from 70 WPM typing to 152 WPM speaking
- Expected result: Ability to talk to Claude Code and have it write backtests, build bots, and debug in real time

> Speaker's tip: "I kind of look at these like slot machines... one caution — they want you to keep using their service. Your planning has to be really good."

### Step 4: Use Claude Code Shortcuts and Autonomous Mode
Set up terminal shortcuts to save time.

- **Shortcut:** Set `C` to run `claude --dangerously-skip-permissions` (autonomous mode — no yes/no confirmations)
- **Shortcut:** Set `T` to activate your conda TFlow environment
- Tell Claude to set these up: "Can you make a shortcut so whenever I type C, it activates claude --dangerously-skip-permissions?"
- **Caution:** Autonomous mode skips all permission prompts — use at your own risk
- Expected result: One-letter terminal shortcuts for instant Claude Code and environment activation

### Step 5: Use Multi-Agent Parallel Backtesting
Launch multiple Claude Code agents simultaneously.

- Tell Claude: "Launch five different agents to test five different backtest ideas based off of this liquidation data, run them in parallel"
- Each agent independently researches and codes a different backtest variation
- Can have 3+ Claude Code projects open simultaneously, each with multiple agents
- Expected result: 5-10 backtests running in parallel instead of sequentially

### Step 6: Use Plan Mode for Big Projects
Before large prompts, activate Plan Mode to save time and reduce bugs.

- Press **Shift+Tab** repeatedly until it says "Plan Mode"
- Claude will plan out the full project before executing any code
- Review the plan, request edits, go back and forth until aligned
- Then execute — saves hours of debugging from poorly-communicated prompts
- Expected result: Higher quality first-pass code with fewer iterations

> Speaker's tip: "Plan mode has saved me so many hours of work because our prompts aren't perfect."

### Step 7: Set Up Sub-Agents for Specialized Tasks
Create specialized agents that know how to perform specific tasks.

- Tell Claude: "Set me up a sub agent that has this backtesting template"
- Sub-agents can specialize in: backtesting, research, bot building
- Give them your backtesting.py template code and RBI roadmap as context
- Expected result: Specialized agents that produce better results for specific tasks

---

## Part 3: Backtesting

### Step 8: Choose the Right Backtesting Framework
Use Python-based backtesting tools, NOT TradingView.

| Tool | Recommendation |
|------|----------------|
| **backtesting.py** | Speaker's preferred choice — clean, simple |
| **BackTrader** | Solid alternative |
| **VectorBT** | Solid alternative |
| **TradingView** | DO NOT use for backtesting — suffers from repainting (indicators change historical values after the fact) |

- **TradingView hack:** Use TradingView ONLY to grab Pine Script code for indicators, then convert to Python
- Example: Search for "QQE mod" indicator on TradingView → copy the Pine Script code → feed to Claude Code to convert to Python and integrate with your data
- Expected result: Backtests in Python that don't suffer from repainting bias

### Step 9: Run and Evaluate Backtests
Use Claude Code to rapidly iterate on backtests.

**Example from the stream:**
- Prompt: "Create two backtests: one that longs after $5M liquidations, one that shorts. Print the stats."
- Claude Code produces both backtests in minutes (used to take 8 hours manually)
- Results: One trash strategy, one profitable — this is expected (1 in 10 win rate is good)

**Robustness tests to run on winners:**
1. Signal permutation test (shuffle signals randomly — if random beats real, edge isn't real)
2. Parameter sensitivity (does it work across a range of parameters?)
3. Transaction cost buffer (at what fee level does it break even?)

- Expected result: Identified winning strategies with validated edges

### Step 10: Use the Autonomous RBI Agent Loop
Deploy the speaker's automated backtesting agent for 24/7 idea processing.

- Navigate to the `mundave-ai-agents` GitHub repo → `RBI_agent` folder
- Populate `ideas.txt` with strategy ideas
- Run: `python RBI_agent.py`
- The agent automatically: researches each idea → codes a backtest → debugs the backtest → reports results → moves to next idea
- Runs indefinitely on a loop
- Expected result: Hands-off backtesting that processes ideas while you sleep

---

## Part 4: Implementation — Building and Running Bots

### Step 11: Follow the Bot Building Checklist
The speaker's step-by-step checklist for every bot:

1. **Implement risk controls** — stop-loss, position limits
2. **Implement the strategy** — entry/exit logic
3. **Use limit orders** (not market orders) — market orders cost 3x more in fees
4. **Check position before new orders** — cancel existing orders before placing new ones
5. **Decimal adjustments** — every exchange has different decimal requirements
6. **Set up a while loop** — bot runs continuously, not just once
7. **TINY SIZE** — start with ~$10 positions. Scale only after live validation

> Speaker's tip: "Even good traders lose just because of fees. With 40x leverage and 5 trades/day, you blow up in 31 days just from fees. A bot with limit orders extends that to 717 days."

### Step 12: Deploy Bots to Cloud Servers
Run bots 24/7 on a VPS without keeping your computer on.

- Choose a VPS provider: Cherry Servers (speaker's choice), Hetzner, Vultr, or Kaboot
- Cost: ~$50/month
- Connect via SSH: `ssh [your-ip-address]`
- Run Claude Code on the server for remote development
- Expected result: Bots running 24/7/365 independent of your local machine

### Step 13: Iterate and Improve Live Bots
Continuously monitor, tweak, and re-backtest.

**Example from the stream (Stat Arb bots):**
- 4 bots running for 1 week: 1 profitable (market neutral), 3 losing
- Speaker's response: "One out of four is good. Let's keep tweaking."
- Changes made: Tighten stop-loss from default to -6%, keep take-profit the same
- Created new versions (e.g., `run_regular_2.py`) rather than modifying winners
- Track starting balances in Apple Notes for clean performance comparison
- Expected result: Gradual improvement through data-driven iteration

---

## Part 5: Social Arbitrage Research

### Step 14: Build a TikTok Social Arbitrage Agent
Automate the process of finding consumer trends before Wall Street.

- Concept: Search TikTok for tags like "sold out everywhere," "super expensive," "finally got my hands on"
- These reveal consumer trends (Abercrombie, Crocs, Celsius) weeks/months before Wall Street prices them in
- Build an agent using Selenium to scrape TikTok search results → organize in CSV
- Use Claude Code plan mode to design the system
- Inspired by the Dumb Money YouTube channel (Chris Camilleri) — 10x annual returns from social arbitrage
- Expected result: Daily automated reports of emerging consumer trends to trade

---

## Common Pitfalls
- **Trading by hand:** The speaker's strongest conviction — hand trading is gambling. Even perfect traders lose to fees with leverage. Automate or stop trading.
- **Skipping backtesting:** Building bots without testing = losing money. Always R→B→I in order.
- **Using TradingView for backtesting:** Repainting indicators make backtests look better than reality. Use Python.
- **Big position sizes on untested bots:** Start with $10 positions. Scale only after weeks of live validation.
- **AI "slot machine" loop:** Claude/AI tools incentivize you to keep prompting. Use Plan Mode to plan first, execute once.
- **Market orders:** Cost 3x more than limit orders. Always use limit orders in bots.
- **Expecting 100% win rate on backtests:** 1 out of 10 winning backtests is GOOD. Most ideas fail.
- **Forgetting to cancel existing orders:** Before entering a new position, always cancel all pending orders first.

---

## Strategies Tested During Stream

| # | Strategy | Return | Sharpe | Status |
|---|----------|--------|--------|--------|
| 1 | V8 Pullback (liquidation-based) | 3,418% | 4.13 | Passed robustness — ready for implementation |
| 2 | Lick Ratio Momentum (QQE + liquidations) | 101% | 1.66 | Passed robustness — ready for implementation |
| 3 | 500K Momentum | 58% | — | Passed robustness — ready for implementation |
| 4 | Regular Stat Arb | Profitable | — | Live with tiny size, market neutral |
| 5 | Copula Stat Arb | Losing | — | Live, adjusting stop-loss to -6% |
| 6 | Gaussian Stat Arb | Losing | — | Live, adjusting stop-loss to -6% |
| 7 | Fourier Stat Arb | Losing | — | Live, adjusting stop-loss to -6% |

---

## Resources Mentioned
- **mundave.com/docs** — Hyperliquid data layer API documentation (55+ endpoints)
- **mundave.com/roadmap** — Full RBI system roadmap with book list, backtesting templates, bot checklist
- **mundave.com/go** — Lifetime all-access offer ($1,500 one-time: Algo Trade Camp + AI masterclasses + Solana bot course + Polymarket bot course + Quantite + API keys + GitHub access)
- **mundave.com/funding** — Funded trader program ($1,000 funding with 40x leverage on Hyperliquid, no profit splits)
- **backtesting.py** — Python backtesting library (speaker's preferred tool)
- **CCXT** — Python library connecting to all major exchanges (Binance, Coinbase, Bybit, Kraken, etc.)
- **Claude Code** — Anthropic's terminal-based AI coding agent
- **Cursor** — AI-powered fork of VS Code (free tier available)
- **WhisperFlow** — Voice-to-text tool (whisperflow.ai) — 152 WPM vs 70 WPM typing
- **Cherry Servers** — VPS provider for 24/7 bot hosting (~$50/month)
- **Google Scholar** — Academic papers on trading strategies
- **TradingView** — ONLY for grabbing indicator code (Pine Script) — do NOT use for backtesting
- **HLP (Hyperliquid Liquidity Provider)** — Market maker vault, grew from $1,000 to $183M
- **Chris Camilleri / Dumb Money** — Social arbitrage trading channel (TikTok trend → stock picks)

---

## Summary
This ~3h33m live stream is a comprehensive masterclass on transitioning from hand trading to algorithmic trading using AI. Moon Dev (Alex Finn) covers his complete 2026 workflow: the RBI system (Research → Backtest → Implement), his AI toolkit (Claude Code with WhisperFlow voice input, multi-agent parallel backtesting, Plan Mode for complex projects, autonomous mode shortcuts), the Hyperliquid data layer giving access to liquidation data, whale positions, and market maker analytics that "Wall Street doesn't want you to have." He demonstrates building multiple backtests in real-time (used to take 8 hours, now takes minutes), evaluates 4 live stat arb bots (1 profitable, 3 being iterated), runs robustness tests on 3 winning strategies (V8 Pullback at 3,418% return, Lick Ratio Momentum at 101%, 500K Momentum at 58%), and introduces social arbitrage research using TikTok trends. The core message: stop trading by hand (it's gambling with compounding fee drain), become a quant, use AI to research and backtest at scale, deploy bots with tiny size, and iterate. The stream also includes a sales pitch for the Algo Trade Camp ($1,500 lifetime access) in the final hour.

*Extracted from: How To Use AI To build Trading Bots (2026 Masterclass).txt*
