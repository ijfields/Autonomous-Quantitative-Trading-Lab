# Video Analysis: I Wasted Hundreds of Hours on OpenClaw Until I Found These

**Speaker:** Craig Hewitt
**Channel:** Craig Hewitt
**Video ID:** MhLM-12ENOM
**Upload Date:** 2026-03-13
**Duration:** 13 min 17 sec

---

## Summary

Craig Hewitt shares seven hard-won lessons from approximately six weeks of daily OpenClaw usage for his business. He covers memory optimization through QMD (created by Shopify CEO Toby Lutke), model selection via OpenRouter to reduce costs, using Perplexity Sonar Pro as a superior search tool within OpenClaw, organizing specialized sub-agents under a primary router agent (his is named Janet), and building a "watchdog" service that automatically restarts the gateway when it crashes.

He also explains how to save money by routing the heartbeat function to a cheap model like Gemini Flash 3 instead of expensive models like Opus 4.6, and discusses using Google's new CLI for Google Drive integration so his agent can write content and drop it into a shared folder. Craig positions OpenClaw as a "second brain" and dispatcher for his business, while noting that Claude Code and Codex remain more valuable for actual code-building tasks.

## Key Topics
- OpenClaw memory optimization and QMD (Quantized Memory Documents)
- Model selection and cost optimization via OpenRouter
- Perplexity Sonar Pro as a search model replacement for Brave API
- Specialized sub-agent architecture (router + child agents)
- Watchdog service for automatic gateway restart
- Heartbeat model optimization (cheap models for health checks)
- Google CLI for Google Drive integration and content sharing
- Communication channels: Telegram vs Discord vs Slack

## Tools & Technologies Mentioned
- OpenClaw (AI agent platform)
- QMD (Quantized Memory Documents by Toby Lutke / Shopify)
- OpenRouter (model routing service)
- Perplexity Sonar Pro (search model)
- Gemini Flash 3 (cheap heartbeat model)
- Opus 4.6 (Anthropic model)
- Codex (OpenAI coding model)
- Claude Code
- Google CLI (Google Drive, Docs, Gmail, Calendar)
- Gogg (Peter Steinberger's Google Workspace tool)
- Telegram, Discord, Slack (communication integrations)
- GitHub (config backup)

## Strategies Found

No specific trading strategies with concrete entry/exit rules were presented. This video focuses on AI agent configuration and productivity optimization.

## Notable Quotes / Insights
- "OpenClaw has been called the most important software released maybe ever. Not by me, but by industry experts."
- "The real unlock is QMD" for solving OpenClaw's memory compaction problem.
- "You don't need to use Opus 4.6 or Codex 5.3 for everything. You should be picking and choosing how you use models for different things."
- "OpenRouter kind of manages all these models on their own... so you're not sending your data to an untrusted third party."
- "Watchdog basically pings every 5 minutes the gateway and if it's down it just restarts it automatically."
- "At the end of the day OpenClaw is a tool but... Claude Code and Codex are maybe more valuable even to me as a business person."

## Actionable Takeaways
1. Enable QMD in OpenClaw to significantly improve memory retention across sessions.
2. Use OpenRouter to route different tasks to appropriate models, reducing costs while maintaining quality.
3. Replace the default Brave search with Perplexity Sonar Pro for better search results within OpenClaw.
4. Organize agents in a parent-child hierarchy with a primary router agent delegating to specialized sub-agents.
5. Build a watchdog service that pings the gateway every few minutes and auto-restarts on failure, with Telegram notifications.
6. Switch the heartbeat model to a cheap option like Gemini Flash 3 to avoid burning expensive API credits on health checks.
7. Use Google CLI for content sharing between the agent's machine and your workspace via shared Google Drive folders.
