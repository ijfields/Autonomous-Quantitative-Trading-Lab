# How to build an army of OpenClaw agents — Complete Transcript Analysis

**Video Title:** How to build an army of OpenClaw agents
**Channel:** Alex Finn
**Video ID:** Rjd1LqF9cG4
**Upload Date:** 2026-03-12
**Duration:** ~18m
**Speaker:** Alex Finn
**Platform:** YouTube

---

## EXECUTIVE SUMMARY

Alex Finn walks through his personal setup of 10 OpenClaw agents operating 24/7 and teaches viewers how to replicate it incrementally. Core philosophy: start with one orchestrator + one sub-agent, master it, then layer on additional sub-agents one at a time. Covers model selection for cost efficiency (right model per task type), Mission Control dashboard setup, reverse prompting for agent suggestions, and advocates local AI hardware as the long-term future for always-on agent swarms.

---

## KEY TOPICS

### The "AI Organization" Concept
- Finn frames himself as "CEO of his own AI company" with 10 OpenClaw agents running continuously
- Agents write newsletters, build apps, script videos, find trending topics, deliver breaking news
- "Working 100x more efficiently" with always-on agent organization

### Starting Small: One Sub-Agent at a Time
- Strongly advises against spinning up many agents at once
- Start with **one orchestrator + one sub-agent**, then layer incrementally
- Recommended first sub-agent: a **coding sub-agent** (useful even for non-coders)
- Do not add more than two sub-agents in your first week

### Model Selection for Cost Efficiency
| Task | Recommended Model | Why |
|------|-------------------|-----|
| Orchestration | Opus 4.6 ("Henry") | Best reasoning for coordination |
| Coding | ChatGPT 5.4 | Best coding model, cost-efficient |
| Research/Writing | Qwen 3.5, Kimmy, or local models | Cheap for text-heavy tasks |

- Key: "Don't just use one model for everything" — using Claude for all tasks is "wildly expensive"
- Open Router for accessing cheap models

### Advantages of Sub-Agents over Multiple OpenClaws
- **Parallel work:** OpenClaw can spin up to 5 sub-agents at a time
- **Clean context windows:** Each sub-agent gets its own context, preventing orchestrator confusion
- **Failure protection:** If a sub-agent crashes, orchestrator diagnoses/fixes. If main crashes while doing 20 things, "everything's toast"
- **Auto-archive:** Completed sub-agents get shut down and cleaned up

### Mission Control Dashboard
- **Team Screen / Org Chart:** Shows each agent, their model, responsibilities
- **Calendar Screen:** All scheduled tasks and cron jobs across agents
- **Office View (optional):** 2D pixel-art visualization of agents working in real time

### Reverse Prompting
- Instead of telling AI what to do, ask: "Based on what you know about me, my goals, my workflows, what sub-agents should we spin up?"
- Orchestrator knows user's history and suggests best sub-agents

### Future: Local AI Hardware
- Finn runs 3 Mac Studios, DJX Spark, Mac Mini (~$40K in hardware)
- Start small: one computer, one model (Qwen 3.5), one task
- Upfront hardware cost, then zero ongoing token costs, running 24/7

---

## TOOLS & PLATFORMS MENTIONED

| Tool/Platform | Purpose |
|---------------|---------|
| OpenClaw | Primary agent framework (orchestrator + sub-agents) |
| Claude / Opus 4.6 | Recommended orchestrator model |
| ChatGPT 5.4 | Recommended coding sub-agent model |
| Qwen 3.5 / Kimmy | Cheap models for research/writing |
| Open Router | Platform to access cheap models |
| Nano Banana | AI image generation (for visual sub-agents) |
| Mac Studio / Mac Mini / DJX Spark | Local AI hardware |
| Mission Control | OpenClaw dashboard for monitoring agents |

---

## ACTIONABLE TAKEAWAYS

1. Start with one orchestrator (Opus 4.6) + one coding sub-agent (ChatGPT 5.4) — let the orchestrator handle configuration
2. Use model-per-task assignment to control costs: expensive for orchestration, cheap for research/writing
3. Build a Mission Control dashboard with Team Screen + Calendar Screen minimum
4. Use reverse prompting to have your orchestrator suggest which sub-agents to add next
5. Limit to two new sub-agents per week to avoid overwhelm
6. Consider local AI hardware to eliminate ongoing token costs for always-on tasks

---

*Analysis derived from: How to build an army of OpenClaw agents.txt*
