# Step-by-Step Guide: I Wasted Hundreds of Hours on OpenClaw Until I Found These

**Source:** Craig Hewitt (YouTube)
**Video ID:** MhLM-12ENOM
**Upload Date:** 2026-03-13

---

## What This Guide Covers

Seven practical optimizations for OpenClaw that improve memory, reduce costs, increase reliability, and streamline multi-agent workflows based on six weeks of daily business use.

---

## Step 1: Optimize Memory with QMD

1. Go to the OpenClaw docs on memory optimization settings.
2. Point your claw at the docs and ask it to optimize memory storage and capacity.
3. Install **QMD** (Quantized Memory Documents), created by Shopify CEO Toby Lutke.
   - Send the QMD documentation link to your claw and say: "Hey, I want to enable QMD. Make it happen."
4. QMD acts as a sidecar that combines multiple ranking and search mechanisms for context retrieval.
5. This takes memory from "average" to "pretty good" -- the single biggest unlock for long-running sessions.

---

## Step 2: Use OpenRouter for Model Selection

1. Sign up at OpenRouter and get an API key.
2. Configure OpenClaw to route API calls through OpenRouter.
3. Select different models for different tasks:
   - Expensive tasks (complex reasoning): Opus 4.6 or similar
   - Cheap tasks (heartbeat, simple queries): Gemini Flash 3 or open-source Chinese models
4. Benefit: open-source models like DeepSeek run on OpenRouter's infrastructure, so your data stays with a trusted US-based provider rather than being sent to China directly.

---

## Step 3: Replace Brave Search with Perplexity Sonar Pro

1. Get a Perplexity API key (Sonar Pro search model).
2. In OpenClaw config, add this as the search model via OpenRouter.
3. Create a skill or rule: "When I ask you to search for something, use the Perplexity Sonar Pro model."
4. This provides dramatically better search results than the default Brave API, closer to what you get from Google.

---

## Step 4: Set Up Specialized Sub-Agents

1. Start with one primary agent (Craig's is named "Janet") as the main router and touchpoint.
2. Create specialized sub-agents for specific domains:
   - **Content agent** -- handles writing and content creation
   - **Ops and finance agent** -- handles operations and financial tasks
   - **Building/coding agent** -- routes to Codex CLI in headless mode via GitHub (creates issues, does work, creates PRs)
3. Each sub-agent can have its own skills, memory, and specific instructions.
4. The primary agent decides which sub-agent to delegate to.
5. Craig recommends this parent-child hierarchy over a flat organization (where you context-switch between channels for each agent).

---

## Step 5: Build a Watchdog Service

1. Create a simple service that pings the OpenClaw gateway every 5 minutes.
2. If the gateway is down, the watchdog automatically restarts it.
3. On successful restart (or failure detection), send a notification via Telegram.
4. Send this concept to your OpenClaw and say "Hey, just do this" -- it can build the watchdog itself.
5. This is critical because OpenClaw frequently breaks when you change models, rules, skills, agents, or upgrade versions.
6. Back up your OpenClaw config to GitHub daily as an additional safety net.

---

## Step 6: Use a Cheap Model for the Heartbeat

1. In the OpenClaw config, find the heartbeat settings (runs every 1-2 minutes by default).
2. Add the model identifier for a cheap model (e.g., Gemini Flash 3) via OpenRouter.
3. Set the config: "For heartbeat, use this model, please."
4. The heartbeat is a basic health check ("are you awake?") that does not need an expensive model like Opus 4.6.
5. This alone can save significant money on API costs over time.

---

## Step 7: Integrate Google CLI for Content Sharing

1. Install the new official Google CLI (replaces the previous "Gogg" tool by Peter Steinberger).
2. Your agent can now interact with Google Drive, Docs, Gmail, and Calendar natively.
3. Set up a shared Google Drive folder between your agent's machine and your own workspace.
4. When the agent creates content (blog posts, articles, reports), it drops them into the shared folder.
5. This eliminates the need to SSH into the agent's machine to retrieve content.
6. Alternative communication channels:
   - **Telegram** -- easiest for a single main agent
   - **Discord with topic channels** -- best for multiple agents with separate responsibilities
   - **Slack** -- rich content preview but requires paid subscription

---

## Key Takeaway

> "OpenClaw is a tool, but there are other tools in our arsenal. Claude Code and Codex are maybe more valuable even to me as a business person who's building real things." The biggest wins come from memory (QMD), cost control (OpenRouter + cheap heartbeat models), reliability (watchdog), and organizational clarity (parent-child agent hierarchy).

*Guide derived from: I Wasted Hundreds of Hours on OpenClaw Until I Found These.txt*
