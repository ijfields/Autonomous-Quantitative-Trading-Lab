# Step-by-Step Guide: I Tested AI Models to Code Trading Bots (The Results Will Shock You)

**Source:** quantlabs (YouTube)
**Video ID:** zuZBI_ul5wM
**Upload Date:** 2026-03-12

---

## What This Guide Covers

How to select the right AI model for generating trading bots from large news-driven prompts, compare LLM performance and cost, and adopt a systematic portfolio management approach where AI generates and deploys fresh trading bots in response to evolving market conditions.

---

## Step 1: Set Up the Trading Bot Environment

1. Get access to a futures/options trading API (Brian uses **Rithmic** for CME data).
2. Set up a Python-based project environment with:
   - Market data streaming
   - Order execution capability
   - Logging and reporting
3. Optionally, use the **Algo Trader Pro Blueprint** from hftcode.com as a starting point.
4. Ensure your environment supports running multiple bots simultaneously (e.g., via PowerShell or terminal multiplexing).

---

## Step 2: Generate Daily News Analysis

1. Use AI to generate comprehensive market analysis from the past 24 hours of trading news.
2. Brian produces 41-page PDF reports covering futures and options market conditions.
3. These reports become the prompt material for trading bot generation.
4. The analysis covers geopolitical events, market movements, specific instruments (Bitcoin, gold, oil, natural gas, VIX, treasuries), and strategy recommendations.

---

## Step 3: Choose the Right LLM for Bot Generation

Based on Brian's head-to-head testing with ~1,500-line prompts:

| Model | Cost | Speed | Quality | Large Prompt Support |
|-------|------|-------|---------|---------------------|
| **GLM 5** (Chinese) | Lowest | Slow | Good | Yes |
| **Codex 5.3** (OpenAI) | Moderate | Fastest | Good | Yes |
| **Claude 4.6** (Anthropic) | ~3x Codex | Moderate | Slightly more bots generated | Yes |
| **MiniMax** | Low | Moderate | N/A | **Breaks** on large prompts |
| **Qwen** | Low | Moderate | N/A | **Breaks** on large prompts |

**Recommendations:**
- **Cost-sensitive:** Use GLM 5 (cheapest, same quality as Codex, but slow)
- **Speed-sensitive:** Use Codex 5.3 (fastest generation, moderate cost)
- **Claude 4.6:** Not recommended -- pays 3x more for marginal benefit (e.g., generates one extra copper bot)
- **Avoid** MiniMax and Qwen for prompts over ~1,500 lines (communication breaks)

---

## Step 4: Generate Trading Bots from News Prompts

1. Feed your daily analysis report into the chosen LLM.
2. Use specific prompting to generate individual trading bots for each strategy identified in the news.
3. Example outputs from one day's Middle East war news:
   - Treasury / Fed stagflation curve trade
   - Bitcoin halving momentum strategy
   - Ethereum staking support (put sell combination)
   - COMEX gold geopolitical tail hedge
   - Crude oil breakout strategy
   - Natural gas EU gas cap reversion
4. Each bot is a standalone Python script with entry/exit logic, position sizing, and risk management.

---

## Step 5: Run Simulated Trading and Compare

1. Deploy all generated bots simultaneously against real market data in a simulated environment.
2. Let them run for at least one trading session (morning, overnight, or full day).
3. Use AI to generate comparison reports showing:
   - Net profit/loss per bot
   - Win ratio
   - Sharpe ratio
   - Maximum drawdown
   - Individual trade logs
4. Key findings from Brian's tests:
   - Bitcoin halving momentum was the top performer in the morning session
   - Natural gas mean-reversion had Sharpe 4.3 but extreme $36K drawdowns
   - VIX was the only consistent performer in severe down markets
   - Gold showed extreme drawdowns despite geopolitical catalysts

---

## Step 6: Act as a Systematic Portfolio Manager

1. Review results across all bots and identify which instruments and strategies are profitable **right now**.
2. Deploy capital only to the profitable bots; shut down or replace the losers.
3. Regenerate a new set of bots as market conditions evolve (potentially every few hours).
4. Think of this as being a **systematic portfolio manager**: your job is to decide which AI-generated strategy deserves capital allocation based on current conditions.
5. In the current volatile, geopolitically-driven market (March 2026), the tradable set was limited to: Bitcoin, gold, Treasury (ZN), and crude oil (NX).

---

## Step 7: Manage Costs and Scale

1. Track your AI API spending across all bot generation and analysis.
2. For high-frequency regeneration (multiple times per day), stick with GLM 5 to minimize costs.
3. For time-sensitive scenarios (breaking news, rapid market changes), pay the premium for Codex speed.
4. If using Python, JavaScript, or HTML, Chinese LLMs are competitive in quality.
5. For more advanced programming needs (C++, complex system design), Codex or Claude may produce better results.
6. Consider joining Brian's Quant Labs analytics group for access to the daily analysis reports and private chat.

---

## Key Takeaway

> "Systematic portfolio managers... this is easily by far the most important metric when it comes to what will be the future of quant trading." The future is not about building one perfect bot -- it is about using AI to generate many bots rapidly in response to news, testing them against real data, and only deploying the profitable ones while the market conditions that spawned them persist.

*Guide derived from: I Tested AI Models to Code Trading Bots (The Results Will Shock You).txt*
