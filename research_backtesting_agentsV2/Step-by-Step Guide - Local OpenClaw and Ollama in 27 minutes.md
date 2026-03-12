# Step-by-Step Guide: Running OpenClaw Locally with Ollama

**Source:** Keith AI (YouTube)
**Video ID:** n2a1FfqjHcU
**Upload Date:** 2026-03-10

---

## What This Guide Covers

How to run OpenClaw entirely on local hardware using Ollama as the LLM backend — eliminating cloud API costs and dependency.

---

## Beginner Setup (Single Machine)

### Step 1: Install Ollama
1. Go to ollama.com and download installer
2. Install on your machine (supports Windows, Mac, Linux)

### Step 2: Pull and Run a Model
1. Run `ollama run qwen3.5:9b` (Keith's recommended model)
2. Set context length: `ollama run qwen3.5:9b --context 26000`
3. **Critical:** Default context is 4,000 tokens — far too small. Set to 16,000+ minimum

### Step 3: Install and Configure OpenClaw
1. Install OpenClaw: `ollama launch openclaw`
2. If using a reasoning model, set to "no think" mode
3. Verify running at `127.0.0.1:18789`

---

## Advanced Setup (Multi-Machine)

### Step 1: Choose Hardware
1. **Jetson Nano** (~$80-150) — runs OpenClaw 24/7 at low power
2. **Gaming laptop** — runs Ollama + model (needs GPU for inference speed)

### Step 2: Network Configuration
1. Assign **static IPs** to both machines on local network
2. Enable **Wake-on-LAN** on the gaming laptop for power management
3. Point OpenClaw on the Jetson to the gaming laptop's Ollama endpoint

### Step 3: Optional Remote Access
1. Install **Tailscale** for secure remote access to your local OpenClaw instance

---

## Model Selection Guide

| Model | Quality | Speed | Verdict |
|-------|---------|-------|---------|
| Kimmy K 2.5 | Very good | Too slow | Rejected |
| LFM2 | Poor | Fast | Rejected |
| **Qwen 3.5 9B** | Good | Good | **Winner** |

### Model Discovery Workflow
1. Use **LM Studio** to browse and compare available models
2. Once you find a good model, run it in Ollama for production use
3. Check for new open-source models every 1-2 months — they improve rapidly

---

## Key Takeaway

> Local OpenClaw eliminates $100-$200/month in API costs but you become the sysadmin. Start with a single-machine setup, use Qwen 3.5 9B, and always set context length to 16,000+ tokens. Split to multi-machine when ready for 24/7 operation.

*Guide derived from: Local OpenClaw & Ollama in 27 minutes.txt*
