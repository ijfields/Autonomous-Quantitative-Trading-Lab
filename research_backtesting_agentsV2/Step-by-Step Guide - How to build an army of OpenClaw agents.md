# Step-by-Step Guide: Building an Army of OpenClaw Agents

**Source:** Alex Finn (YouTube)
**Video ID:** Rjd1LqF9cG4
**Upload Date:** 2026-03-12

---

## What This Guide Covers

How to incrementally build a multi-agent OpenClaw setup — from one orchestrator to 10+ always-on agents — with model selection for cost efficiency.

---

## Step 1: Set Up Your Orchestrator
1. Use **Opus 4.6** as your orchestrator model (Alex's orchestrator is named "Henry")
2. If kicked off OOTH, fall back to **Sonnet via API**
3. Let the orchestrator handle all configuration — do not manually edit config files

## Step 2: Add Your First Sub-Agent (Coding)
1. Tell your orchestrator: "Build a sub-agent for coding tasks using ChatGPT 5.4"
2. ChatGPT 5.4 is described as the best coding model and very cost-efficient
3. Master this one sub-agent before adding more

## Step 3: Add a Research Sub-Agent
1. Prompt: "Build a sub-agent for all research activities. Every morning at 8 AM, search the web for trending news about [your topic]. Use Qwen 3.5."
2. This creates a cron-scheduled task visible on your calendar
3. Use cheap models (Qwen 3.5, Kimmy, Open Router) for research — not Claude

## Step 4: Build Your Mission Control
1. **Team Screen:** Org chart showing each agent, their model, and responsibilities
2. **Calendar Screen:** All scheduled tasks and cron jobs across all agents
3. **Office View (optional):** Fun pixel-art visualization of agents working
4. Let the orchestrator build these dashboards for you via natural language

## Step 5: Use Reverse Prompting to Expand
1. Ask your orchestrator: "Based on what you know about me, my goals, my workflows, what sub-agents should we spin up?"
2. The orchestrator suggests agents based on your actual conversation history
3. Add no more than **2 new sub-agents per week**

## Step 6: Scale with Model-Per-Task Assignment
| Task Type | Model | Cost |
|-----------|-------|------|
| Orchestration | Opus 4.6 | Premium |
| Coding | ChatGPT 5.4 | Mid-tier |
| Research/Writing | Qwen 3.5 / local | Cheap/free |

## Step 7 (Optional): Move to Local Hardware
1. Start with one device running one model (e.g., Qwen 3.5 on Mac Mini)
2. Upfront cost, then zero ongoing token fees, running 24/7
3. Scale to multiple devices as agent count grows

---

## Key Takeaway

> Start with one orchestrator and one sub-agent. Master it. Then layer incrementally. Use the right model for each task to control costs. The orchestrator should configure everything — never manually edit config files.

*Guide derived from: How to build an army of OpenClaw agents.txt*
