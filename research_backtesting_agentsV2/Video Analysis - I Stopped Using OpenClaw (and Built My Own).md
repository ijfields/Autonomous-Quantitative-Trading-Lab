# I Stopped Using OpenClaw (and Built My Own) — Complete Transcript Analysis

**Video Title:** I Stopped Using OpenClaw (and Built My Own)
**Channel:** Nath's Server
**Video ID:** gcRYKEOYaS0
**Upload Date:** 2026-03-08
**Duration:** ~15m
**Speaker:** Nath (self-hosted AI/homelab enthusiast)
**Platform:** YouTube

---

## EXECUTIVE SUMMARY

Nath critiques OpenClaw for being slow (~2.5 min per reply locally), expensive ($600-$800/month on Opus), token-heavy (30K-token context wrapper per message), and opaque about networking behavior (unexplained HTTPS tunnel to Telegram). He then demonstrates "Gerald" (Guy Executing Random Local Automation Duties), a fully local AI agent system he built in under 8 hours using n8n + Ollama + a custom macOS app, covering home automation, SSH server management, persistent memory, and Wikipedia lookups.

---

## KEY TOPICS

### OpenClaw Critique

| Issue | Detail |
|-------|--------|
| **Speed** | ~2.5 minutes per reply when running locally with Ollama |
| **Token overhead** | ~30,000-token context wrapper per message (skills, setup instructions) |
| **Cost (Opus 4.6)** | $600-$800/month at 50 messages/day |
| **Cost (GPT-4.1 Mini)** | $2-$20/day but degraded output quality |
| **Security** | "Vibe coded" (AI-generated code controlling other AI), several hundred known MCP server vulnerabilities |
| **Privacy** | Every prompt sends connected data (calendar, email, files) to Anthropic or OpenAI |
| **Unexplained behavior** | Configured HTTPS tunnel to Telegram without user specifying a reverse proxy |
| **Reliability** | Gets stuck in loops, needs human intervention to self-correct |
| **Documentation** | "Changes all the time" |

### Gerald: The Self-Built Alternative

**"Guy Executing Random Local Automation Duties"** — built in under 8 hours (vs. 10+ hours trying to get OpenClaw working locally).

### Gerald's Architecture

```
Custom macOS App → n8n Webhook → Orchestrator Workflow → Tool Sub-Workflows
                                        ↓
                                  Local LLMs (Ollama)
                                        ↓
                               PostgreSQL Vector Store
```

### Tech Stack

| Component | Technology |
|-----------|-----------|
| Orchestration | **n8n** (self-hosted, Cloudflare reverse proxy) |
| Local LLMs | **Ollama** (Qwen 2.5, Llama 3.2 3B, nomic-embed-text) |
| Vector database | **PostgreSQL** (persistent personal memory) |
| Chat frontend | **Custom macOS app** (Xcode + GitHub Copilot) |
| Messaging | **Telegram API** (webhook over HTTPS) |
| Smart home | **Home Assistant** |
| Remote server | **SSH** to Linux AI server (NVIDIA RTX 3080) |
| Knowledge | **Wikipedia** (built-in n8n node) |
| Hardware | **Mac Mini M4** (primary) + Linux AI server |

### Gerald's Tool Sub-Workflows

1. **SSH terminal** — Execute bash commands on Linux AI server (GPU usage, Ollama models, file creation)
2. **Wikipedia** — Real-time knowledge retrieval
3. **Home Assistant** — Control heating, hot water, lights, TV, smart home devices
4. **Manage Rules** — Store/delete long-term personal preferences in PostgreSQL via SQL
5. **Memory system** — Short-term (last ~10 messages) + long-term vector search (nomic-embed-text embeddings)

### Key Technical Details

- Gerald can iterate autonomously — if a tool call fails, the agent retries with alternative approaches
- A code node (written by Claude) strips out Qwen's internal "thinking" tags before responding
- Responds in under 1 second vs. OpenClaw's 2.5 minutes locally
- Zero API fees — all inference runs on local Ollama models

---

## TOOLS & PLATFORMS MENTIONED

| Tool/Platform | Purpose |
|---------------|---------|
| n8n | Self-hosted automation/workflow orchestration |
| Ollama | Local LLM inference server |
| Qwen 2.5 | Primary conversational model |
| Llama 3.2 (3B) | Memory retrieval + secondary agent model |
| nomic-embed-text | Vector embeddings for long-term memory |
| PostgreSQL | Vector store / persistent memory database |
| Home Assistant | Smart home control |
| Cloudflare | Reverse proxy, HTTPS, webhook security |
| Telegram | Messaging interface |
| Xcode / GitHub Copilot | macOS app development |
| MCP servers | Extensibility (e.g., connect Blender) |

---

## ACTIONABLE TAKEAWAYS

1. **n8n as OpenClaw alternative** — fully self-hosted orchestration with complete control over every workflow and data flow
2. **Token wrapping is the hidden cost** — 30K tokens per message is the root cause of both slowness (local) and expense (cloud API)
3. **Local-first eliminates API costs** — Ollama with small models (Qwen 2.5, Llama 3B) costs $0 in API fees
4. **Audit your AI agent's network behavior** — the unexplained HTTPS tunnel is a cautionary tale
5. **Modular sub-workflow architecture** mirrors OpenClaw skills but with full user transparency
6. **Build time was under 8 hours** — faster than getting OpenClaw working locally, with more control
7. **Set API spending limits immediately** if using any cloud-API-backed agent

---

*Analysis derived from: I Stopped Using OpenClaw (and Built My Own).txt*
