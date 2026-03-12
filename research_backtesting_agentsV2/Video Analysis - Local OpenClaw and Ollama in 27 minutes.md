# Local OpenClaw & Ollama in 27 minutes — Complete Transcript Analysis

**Video Title:** Local OpenClaw & Ollama in 27 minutes
**Channel:** Keith AI
**Video ID:** n2a1FfqjHcU
**Upload Date:** 2026-03-10
**Duration:** ~28m
**Speaker:** Keith (Keith AI)
**Platform:** YouTube

---

## EXECUTIVE SUMMARY

Keith demonstrates running OpenClaw entirely locally using Ollama as the LLM backend — eliminating cloud API costs ($100-$200/month) and cloud dependency. Covers beginner setup (single machine) and advanced setup (Jetson Nano for OpenClaw + gaming laptop for Ollama). Recommends Qwen 3.5 9B as the best balance of speed and performance. Key configs: set context length to 16,000+ (default 4,000 is too small), use static IPs, enable Wake-on-LAN. Also covers using LM Studio for model discovery.

---

## KEY TOPICS

### Why Run Locally
- Cost: Cloud APIs cost $100-$200/month
- Privacy: All data stays on local network
- Reliability: No cloud dependency
- Policy: Some providers (Gemini, Claude) ban pro-plan users from using with OpenClaw

### Architecture Options
1. **Fully cloud** — OpenClaw on server calling cloud LLMs
2. **Fully local** — OpenClaw + Ollama on same machine/network
3. **Hybrid** — Local OpenClaw calling cloud LLMs

### Beginner Setup (Single Machine)
1. Install Ollama from ollama.com
2. Run `ollama run qwen3.5:9b`
3. Install OpenClaw: `ollama launch openclaw`
4. Set model to "no think" mode if using reasoning model
5. Verify at `127.0.0.1:18789`

### Advanced Setup (Multi-Machine)
- **Jetson Nano** (~$80-150) runs OpenClaw 24/7 (low power)
- **Gaming laptop** runs Ollama + model (GPU power)
- Connected via static IPs on local network
- Wake-on-LAN for power management

### Model Selection (Keith's Testing)
| Model | Quality | Speed | Verdict |
|-------|---------|-------|---------|
| Kimmy K 2.5 | Very good | Too slow | Rejected |
| LFM2 | Poor | Fast | Rejected |
| **Qwen 3.5 9B** | Good | Good | **Winner** |

### Critical Config
- Default context length: 4,000 tokens — **far too small**
- Set to 16,000+ minimum: `ollama run <model> --context 26000`

---

## TOOLS & PLATFORMS MENTIONED

| Tool/Platform | Purpose |
|---------------|---------|
| Ollama | Local LLM hosting and serving |
| LM Studio | Model discovery and comparison |
| OpenClaw | AI agent platform |
| Qwen 3.5 9B | Recommended local model |
| Jetson Nano | Low-power device for 24/7 OpenClaw |
| Tailscale | Secure remote access (mentioned, not demoed) |

---

## ACTIONABLE TAKEAWAYS

1. Local OpenClaw eliminates API costs but you become the sysadmin
2. Use LM Studio for model discovery, then run chosen model in Ollama
3. Start with single-machine setup; split to multi-machine when ready
4. Context length is critical — default 4,000 is far too small, aim for 16,000+
5. Set static IPs and Wake-on-LAN for robust, power-efficient operation
6. Check for new open-source models every 1-2 months — they improve rapidly

---

*Analysis derived from: Local OpenClaw & Ollama in 27 minutes.txt*
