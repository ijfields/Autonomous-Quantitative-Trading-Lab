# OpenClaw Optimization & Cost Savings Tutorial — Save 97% on Cost — Complete Transcript Analysis

**Video Title:** OpenClaw Optimization & Cost Savings Tutorial - Save 97% on Cost
**Channel:** Tech With Tim
**Video ID:** lTXFv1Z0qfI
**Upload Date:** 2026-03-13
**Duration:** ~49m
**Speaker:** Tim (Tech With Tim)
**Platform:** YouTube

---

## EXECUTIVE SUMMARY

Detailed, step-by-step technical tutorial on reducing OpenClaw API costs from $100+/day to under $5/day (95%+ reduction). Covers five major optimization techniques: model routing via soul.md rules, session initialization optimization, local heartbeats via Ollama, prompt caching configuration, and context pruning. Also demonstrates token auditing tools. Tim credits Matt Ganzic for the original 90% savings methodology.

---

## KEY TOPICS

### 1. Model Routing (soul.md Rules)
- Default model: Claude Haiku 4.5 (cheapest)
- Sonnet 4.6: only for designing, reviewing, security, major decisions
- Opus 4.6: only when advanced reasoning is needed and Sonnet fails
- GPT 5 Mini / GPT 5.1: fallback when Anthropic rate limits
- Rules: never switch models mid-task unless rate-limited; never use premium for reading files or simple questions

### 2. Session Initialization
- At start: load ONLY soul.md, user.md, and today's memory file
- Do NOT auto-load: full conversation history, memory.md, session logs, past tool outputs
- For past context: run memory search first, return only relevant snippet
- End of session: write summary to memory (under 500 words, bullet points)

### 3. Local Heartbeat with Ollama
- Install Ollama on VPS (CPU-only mode)
- Pull Llama 3.2:3B (~2GB model)
- Configure heartbeat to use local model instead of paid API
- Heartbeat every 60 minutes — cost: completely free

### 4. Prompt Caching
- Add `"params": {"cache": {"type": "ephemeral"}}` to model configs
- Expensive models (Opus, Sonnet): `"cacheRetention": "long"` (1 hour TTL)
- Cheaper models (Sonnet 4.5): `"cacheRetention": "short"` (5 min TTL)
- Skip caching for Haiku (already cheap; cache write cost negates savings)
- Cached reads cost ~90% less

### 5. Context Pruning
- After 55 minutes inactivity, prune stale tool outputs and old messages
- Reduces token count in API requests

### Token Auditing Tools
- `/status`: current model, context window, compactions, runtime
- `/context list`: all files/tokens injected into prompts
- `/context detail`: granular token breakdown
- Usage tab in gateway: messages, tool calls, errors, avg tokens/message, cache hit rate

---

## TOOLS & PLATFORMS

| Tool | Purpose |
|------|---------|
| OpenClaw | Agent framework (gateway, JSON config, soul.md) |
| Hostinger | VPS provider (one-click OpenClaw install, KVM2 ~$7/month) |
| Docker | Containerized deployment |
| VS Code + Remote SSH | GUI editing of server files |
| Ollama | Local LLM runner for heartbeats |
| Llama 3.2:3B | Local heartbeat model |
| Claude Opus 4.6 / Sonnet 4.5/4.6 / Haiku 4.5 | Anthropic models (tiered usage) |
| GPT 5 Mini / GPT 5.1 | OpenAI fallback models |

---

## KEY TAKEAWAY

> The single biggest cost driver is using Opus 4.6 for every task — 90% of tasks can be handled by Haiku 4.5. Combined optimizations (model routing + session init + local heartbeats + prompt caching + context pruning) reduce costs from $100+/day to under $5/day. Always set monthly spending limits on API dashboards. Run OpenClaw on a VPS, never on your main computer.

*Analysis derived from: OpenClaw Optimization & Cost Savings Tutorial - Save 97% on Cost.txt*
