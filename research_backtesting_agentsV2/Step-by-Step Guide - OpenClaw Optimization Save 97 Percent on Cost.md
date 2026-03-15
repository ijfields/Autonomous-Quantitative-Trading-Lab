# Step-by-Step Guide: Reducing OpenClaw API Costs by 97%

**Source:** Tech With Tim (YouTube)
**Video ID:** lTXFv1Z0qfI
**Upload Date:** 2026-03-13

---

## What This Guide Covers

Five optimization techniques to reduce OpenClaw costs from $100+/day to under $5/day, plus token auditing tools.

---

## Step 1: Set Up Model Routing in soul.md
1. Set default model to Claude Haiku 4.5 (cheapest)
2. Add rules: use Sonnet 4.6 only for designing, reviewing, security, major decisions
3. Add rules: use Opus 4.6 only when Sonnet fails on advanced reasoning
4. Add fallback: GPT 5 Mini / GPT 5.1 when Anthropic rate limits
5. Rule: "Never switch models mid-task unless you hit a rate limit"
6. Rule: "Never use a premium model for writing, reading files, or simple questions"

## Step 2: Optimize Session Initialization in soul.md
1. At session start, load ONLY: soul.md, user.md, and today's memory file
2. Do NOT auto-load: full conversation history, memory.md, session logs, past tool outputs
3. For past context: run memory search first, return only relevant snippet
4. End of every session: write summary to memory (under 500 words, bullet points)

## Step 3: Set Up Local Heartbeat with Ollama
1. Install Ollama on your VPS: `curl -fsSL https://ollama.com/install.sh | sh`
2. Pull a small model: `ollama pull llama3.2:3b` (~2GB)
3. Configure OpenClaw heartbeat to use local model instead of paid API
4. Set heartbeat interval to 60 minutes
5. Cost: completely free (local inference)

## Step 4: Enable Prompt Caching
1. Add `"params": {"cache": {"type": "ephemeral"}}` to model configs in openclaw.json
2. Expensive models (Opus, Sonnet): set `"cacheRetention": "long"` (1 hour TTL)
3. Cheaper models (Sonnet 4.5): set `"cacheRetention": "short"` (5 min TTL)
4. Skip caching for Haiku (already cheap; cache write cost negates savings)
5. Cached reads cost ~90% less than uncached

## Step 5: Configure Context Pruning
1. Add `"contextPruning"` section to defaults in openclaw.json
2. After 55 minutes of inactivity, prune stale tool outputs and old messages
3. Reduces token count in all subsequent API requests

## Step 6: Audit Your Token Usage
1. `/status` — current model, context window, compactions, runtime
2. `/context list` — all files/tokens injected into prompts
3. `/context detail` — granular token breakdown
4. Usage tab in gateway — messages, tool calls, errors, avg tokens/message, cache hit rate
5. Ask OpenClaw to generate a full cost audit report

## Step 7: Set Safety Limits
1. Set monthly spending limits on API provider dashboards
2. Disable automatic recharge
3. Run OpenClaw on a VPS in an isolated environment, never on your main computer

---

## Key Takeaway

> The single biggest cost driver is using Opus 4.6 for every task — 90% of tasks can be handled by Haiku 4.5. Combined optimizations achieve 95%+ cost reduction. Always set spending limits and run on a VPS.

*Guide derived from: OpenClaw Optimization & Cost Savings Tutorial - Save 97% on Cost.txt*
