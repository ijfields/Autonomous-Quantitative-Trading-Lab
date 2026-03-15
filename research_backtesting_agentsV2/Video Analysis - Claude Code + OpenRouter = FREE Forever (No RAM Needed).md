# Video Analysis: Claude Code + OpenRouter = FREE Forever (No RAM Needed)

**Speaker:** Efran
**Channel:** Efran | AI Automation
**Video ID:** Shkx096xonQ
**Upload Date:** 2026-03-11
**Duration:** 5 min 37 sec

---

## Summary

Efran demonstrates how to run Claude Code completely for free by connecting it to free cloud-hosted models through OpenRouter, eliminating the need for local RAM or paid API subscriptions. He explains that even the smallest coding-oriented models like QPOS require 14 GB of VRAM to run locally, which exceeds the base RAM on many computers (e.g., a 16 GB Mac Mini), making local hosting impractical for most users.

The tutorial walks through creating a settings.json file with an OpenRouter API key and model identifier, then launching Claude Code. When the initial free model (Qwen Coder) encounters rate-limiting ("too many requests"), Efran shows how to switch to OpenRouter's "free models router," which automatically selects from available free models to improve success rates. He also compares pricing, noting that MiniMax 2.5 (ranked #1 for programming) costs 30 cents per million input tokens versus Opus 4.6 at $5 per million input tokens.

## Key Topics
- Running Claude Code for free without local model hosting
- OpenRouter as a model routing layer for accessing free and paid models
- RAM requirements for local AI models (QPOS: 14 GB, Qwen 3/40B: 290 GB)
- OpenRouter free models router for automatic model selection
- Cost comparison between free, budget, and premium models
- settings.json configuration for Claude Code with OpenRouter

## Tools & Technologies Mentioned
- Claude Code (Anthropic CLI)
- OpenRouter (model routing API)
- QPOS / Qwen Coder (free models)
- OpenRouter free models router (auto-selects available free models)
- MiniMax 2.5 (budget coding model, ranked #1 in programming)
- Opus 4.6 (premium Anthropic model)
- Cursor (code editor / IDE)
- Ollama (local LLM hosting, mentioned as alternative)
- VS Code / AntiGravity (alternative editors mentioned)

## Strategies Found

No specific trading strategies with concrete entry/exit rules were presented. This video is a technical tutorial on running Claude Code for free.

## Notable Quotes / Insights
- "If your computer doesn't have a lot of RAM, you will still be able to run Claude Code for free."
- "If we run [Qwen 3/40B] on our computer, it will consume 290 gigs of RAM, which will be more expensive than using cloud API."
- "If we use the free model router, we are going to have a lot more success. And pretty much all our requests will be going through."
- "The performance of these free models is not going to be as good as Anthropic models."
- MiniMax 2.5 pricing: 30 cents / 95 cents per million tokens (input/output) vs Opus 4.6 at $5 / $25 per million tokens.

## Actionable Takeaways
1. Create a `settings.json` file in your project folder with the OpenRouter API key and desired model name to connect Claude Code to OpenRouter.
2. Sign up for OpenRouter (free) and generate an API key from Settings > API Keys.
3. If a specific free model hits rate limits, switch to the "free models router" which automatically rotates through available free models.
4. For better quality at low cost, use MiniMax 2.5 (requires OpenRouter credits) at roughly 1/17th the cost of Opus 4.6.
5. No local GPU or high RAM is needed since all inference runs on OpenRouter's cloud infrastructure.
