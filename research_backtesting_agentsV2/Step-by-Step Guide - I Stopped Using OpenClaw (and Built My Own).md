# Step-by-Step Guide: Building a Self-Hosted AI Agent with n8n + Ollama (OpenClaw Alternative)

**Source:** Nath's Server (YouTube)
**Video ID:** gcRYKEOYaS0
**Upload Date:** 2026-03-08

---

## What This Guide Covers

How to build "Gerald" — a fully local, zero-API-cost AI agent using n8n, Ollama, and PostgreSQL that replaces OpenClaw for home automation, server management, and personal AI assistant tasks.

---

## Prerequisites

- A computer capable of running local LLMs (Mac Mini M4 or Linux with NVIDIA GPU recommended)
- Docker or bare-metal installation of n8n
- Basic familiarity with webhooks and workflow automation

---

## Step 1: Install Core Infrastructure

1. Install **Ollama** and pull required models:
   - `qwen2.5` — primary conversational/agent model
   - `llama3.2:3b` — memory retrieval model
   - `nomic-embed-text:latest` — vector embeddings
2. Install **n8n** (self-hosted) and expose via **Cloudflare** reverse proxy for HTTPS webhook access
3. Set up **PostgreSQL** with vector extension for long-term memory storage

---

## Step 2: Build the Orchestrator Workflow

1. Create an n8n webhook node that receives messages from your chat frontend
2. Connect to an AI Agent node using Ollama (Qwen 2.5) as the LLM
3. Configure short-term memory buffer (last ~10 messages)
4. Add a code node to strip model "thinking" tags from responses before returning them

---

## Step 3: Add Tool Sub-Workflows

Each tool is a separate n8n workflow called by the orchestrator:

### SSH Terminal Tool
- Uses n8n SSH node to execute bash commands on a remote server
- Example: check GPU usage, list running Ollama models, create files

### Wikipedia Tool
- Built-in n8n Wikipedia node for real-time knowledge retrieval

### Home Assistant Integration
- Connect to Home Assistant API
- Control heating, hot water, lights, TV, and smart home devices

### Manage Rules Sub-Workflow
- SQL insert/delete operations on PostgreSQL
- Stores long-term personal preferences and rules
- Agent can autonomously add new rules based on conversation

---

## Step 4: Implement Long-Term Memory

1. Use `nomic-embed-text` via Ollama to generate vector embeddings
2. Store embeddings in PostgreSQL vector store
3. On each user message, query vector store for relevant past context
4. Use a dedicated Llama 3.2 instance for memory retrieval (keeps main model context clean)

---

## Step 5: Build the Chat Frontend

**Option A: Custom macOS app** (Xcode + GitHub Copilot)
- Native app that sends messages to n8n webhook
- Works on phone and MacBook

**Option B: Telegram bot** (simpler)
- Use n8n Telegram node
- Connect via Cloudflare-secured webhook

---

## Step 6: Add MCP Servers for Extensibility

- n8n supports MCP (Model Context Protocol) connections
- Add integrations like Blender, file systems, or custom APIs
- Each MCP server becomes an available tool for the orchestrator

---

## Key Advantages Over OpenClaw

| Gerald (n8n + Ollama) | OpenClaw |
|-----------------------|----------|
| <1 second response | ~2.5 min locally |
| $0 API cost | $600-$800/month (Opus) |
| Full data control | Data sent to Anthropic/OpenAI |
| Minimal token overhead | ~30K token wrapper per message |
| Transparent networking | Unexplained tunnels possible |
| Built in <8 hours | 10+ hours to configure locally |

---

## Key Takeaway

> For technically inclined users, n8n + Ollama provides a fully self-hosted, zero-cost AI agent with complete transparency over data flow and networking. The tradeoff is capability — local small models are less powerful than Opus or GPT-4 — but for home automation, server management, and simple lookups, they are more than sufficient.

*Guide derived from: I Stopped Using OpenClaw (and Built My Own).txt*
