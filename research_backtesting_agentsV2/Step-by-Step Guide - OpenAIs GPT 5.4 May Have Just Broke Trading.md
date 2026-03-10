# Step-by-Step Guide: Testing AI Models for Automated Trading Strategy Generation

**Source:** Moon Dev (YouTube)
**Video ID:** zmoAR8Xn0vI
**Upload Date:** 2026-03-06

---

## What This Guide Covers

How to set up and test different AI models (GPT 5.4, Claude, MiniMax) for automated trading strategy generation using the RBI (Research, Backtest, Incubate) pipeline with parallel processing.

---

## Prerequisites

- Python environment with backtesting.py installed
- API keys for at least one LLM provider (OpenAI, Anthropic, Open Router)
- Historical market data (25+ data sources recommended)
- Open Router account (for easy model switching)

---

## Step 1: Set Up Open Router for Multi-Model Testing

1. Create an Open Router account
2. Add API credits
3. Configure your trading bot to use Open Router as the API endpoint
4. This allows you to swap models without changing code — just change the model ID

**Why Open Router:** Test GPT 5.4, Claude, MiniMax, and others through a single API gateway.

---

## Step 2: Understand the RBI Pipeline

| Stage | What It Does | Output |
|-------|-------------|--------|
| **R** (Research) | AI scans data sources for patterns | List of potential strategy ideas |
| **B** (Backtest) | AI writes backtest code, runs against historical data | Win rate, Sharpe ratio, drawdown metrics |
| **I** (Incubate) | Promotes passing strategies to paper trading | Live paper-trade results |

**Pass criteria:** Strategy must exceed 50% on target metric (configurable).

---

## Step 3: Configure Parallel Processing (PP Multi)

For higher throughput:

1. Set up 5 parallel backtest workers
2. Feed each worker different data sources (25 total ÷ 5 = 5 per worker)
3. Run simultaneously to test multiple strategies at once
4. Aggregate results and filter for passing strategies

**Benefit:** 5x faster strategy discovery compared to serial processing.

---

## Step 4: Test GPT 5.4 Regular

| Setting | Value |
|---------|-------|
| Model ID | `gpt-5.4` (via Open Router) |
| Cost | $2.50 input / $15.00 output per 1M tokens |
| Use case | Standard strategy generation and backtest code |

1. Point your RBI agent to GPT 5.4 regular
2. Run a full cycle across all 25 data sources
3. Record results: strategies generated, pass/fail rates, code quality
4. Note any errors or unusual outputs

---

## Step 5: Test GPT 5.4 Pro (with Token Fix)

| Setting | Value |
|---------|-------|
| Model ID | `gpt-5.4-pro` (via Open Router) |
| Cost | $30.00 input / $180.00 output per 1M tokens |
| Critical fix | Remove or significantly increase `max_output_tokens` |

**Known issue:** GPT 5.4 Pro's reasoning consumes all output tokens, leaving nothing for actual response.

**Fix:** Do NOT set a low `max_output_tokens` limit. Either:
- Remove the parameter entirely
- Set it to a very high value (e.g., 16,000+)

---

## Step 6: Test Budget Alternatives

### MiniMax ($10/month Coding Plan)
- Flat-rate pricing — no per-token costs
- Good for high-volume backtesting where token costs add up
- Test same strategies to compare quality vs. cost

### Cost Comparison for 1,000 Backtest Runs

| Model | Estimated Cost | Quality |
|-------|---------------|---------|
| GPT 5.4 | ~$15-30 | Good |
| GPT 5.4 Pro | ~$180-360 | Unknown (needs more testing) |
| Claude Opus 4.6 | ~$45-75 | High |
| MiniMax | $10 flat | Needs evaluation |

---

## Step 7: Evaluate Results Over Time

Do NOT judge a model from a single session. Moon Dev's evaluation framework:

1. **Run for 1 full week** — minimum evaluation period
2. **Track metrics per model:**
   - Total strategies generated
   - Pass rate (% exceeding 50% threshold)
   - Code quality (does it run without errors?)
   - Cost per passing strategy
3. **Compare across models** using the same data sources and criteria
4. **Consider cost efficiency:** A cheaper model that finds 1 strategy per $10 beats an expensive model that finds 1 per $100

---

## Step 8: Promote Winners to Incubation

For any strategy that passes backtesting:

1. Move to paper trading (incubation stage)
2. Run for 2-4 weeks minimum
3. Compare paper results to backtest expectations
4. If paper trading confirms: deploy with small real capital
5. Scale up gradually

---

## Model Selection Quick Reference

| Need | Best Choice |
|------|------------|
| Highest quality code | Claude Opus 4.6 |
| Budget bulk testing | MiniMax ($10/month) |
| Balanced cost/quality | GPT 5.4 regular |
| Complex reasoning tasks | GPT 5.4 Pro (with token fix) |
| Easy model switching | Open Router (any model) |

---

## Key Takeaway

> Don't commit to one AI model for trading strategy generation. Use Open Router to A/B test multiple models against the same data. Evaluate over a full week, track cost per passing strategy, and let the numbers decide — not hype.

*Guide derived from: OpenAIs GPT 5.4 May Have Just Broke Trading.txt*
