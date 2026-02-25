# Video Analysis: Set up a multi-agent team using OpenClaw in Discord

**Speaker:** Alex Finn
**Channel:** Alex Finn
**Video ID:** vxpuLIA17q4
**Upload Date:** 2026-02-24
**Duration:** ~33 minutes

---

## Overview
A comprehensive tutorial on building a multi-agent OpenClaw operating system inside Discord. Alex Finn demonstrates his production workflow: automated trending tweet alerts, research pipelines, script writing, thumbnail generation, stock research, competitor analysis, daily digests, direct agent lines, and project-specific channels. The video covers setup from scratch, model selection, cost optimization, device recommendations, security best practices, and finding custom use cases through "reverse prompting."

---

## Key Concepts

### Discord as Multi-Agent OS
- Discord's channel structure enables parallel agent workflows impossible in Telegram/WhatsApp/iMessage
- Each channel = separate context for a project, workflow, or agent
- Pinned documents and research reports stay organized per channel
- The speaker previously "hated Discord" but now considers it "built for OpenClaw"

### Automated Workflow Chains
- Trending tweets channel (every 2 hours) → Research channel (stories behind tweets) → Script channel (YouTube scripts in speaker's voice) → Thumbnail channel (concepts for approved scripts)
- Each step is a different sub-agent triggered by cron jobs staggered 30 minutes apart
- Approval/feedback system: checkmark or X on scripts trains the model over time

### Model Architecture: Brain vs. Muscles
- **Brain (orchestrator):** Anthropic ($200/mo) or ChatGPT ($20/mo) — the smart model that coordinates
- **Muscles (sub-agents):** Cheaper Chinese models (Miniax 2.5, Kim K 2.5) or local models for dirty work
- Local models on Mac Studios = unlimited usage for the cost of energy

### Reverse Prompting
- Ask your AI: "Based on everything you know about me, what advanced multi-agent automations can we create in Discord?"
- The AI suggests custom workflows based on your history — more valuable than copying someone else's setup

---

## Workflows Demonstrated

| # | Workflow | Automation | Frequency |
|---|---------|-----------|-----------|
| 1 | Trending Tweet Alerts | Finds trending X posts in user's niche | Every 2 hours |
| 2 | Story Research | Researches stories behind trending tweets | 30 min after alerts |
| 3 | Script Writing | Writes YouTube scripts from research | 30 min after research |
| 4 | Thumbnail Concepts | Generates thumbnail ideas for approved scripts | On approval |
| 5 | Stock Research | AI buildout companies with competitive moats | Daily 7:00 AM |
| 6 | Competitor Research | Trending YouTube videos about OpenClaw | Daily 8:00 AM |
| 7 | Daily Digest | Summary of all agent activity | End of day |
| 8 | Coding Agent (Charlie) | Builds features for SaaS projects 24/7 | Continuous loop |
| 9 | App Prototype Builder | Builds prototypes from trending stories | On trigger |

---

## Tools & Platforms
| Tool | Purpose |
|------|---------|
| OpenClaw | Core AI agent framework |
| Discord | Multi-agent operating system / interface |
| X (Twitter) API | Trending post detection (pay-as-you-go) |
| YouTube API | Competitor video research (free) |
| Anthropic API | Brain/orchestrator model ($200/mo) |
| ChatGPT | Alternative brain ($20/mo) |
| Miniax 2.5 / Kim K 2.5 | Cheap sub-agent models |
| Local models (Gemma) | Free sub-agent compute |
| Mac Mini ($600) | Recommended minimum device |
| Mac Studio | Advanced setup with local models |
| Nano Banana Pro | Thumbnail generation |
| Vibe Coding Academy | Speaker's community/boot camp |

---

## Actionable Takeaways
1. Discord's channel structure is the best platform for multi-agent OpenClaw — enables parallel workflows impossible elsewhere
2. Use cron jobs to chain workflows: tweets → research → scripts → thumbnails, each triggered 30 minutes apart
3. Use Anthropic or ChatGPT as the "brain" orchestrator, cheaper models as "muscles" for sub-agents
4. Never let anyone into your Discord server — your agent has full access to your digital life
5. Don't give agents write access to email/messaging channels (no autonomous outbound communication)
6. Use reverse prompting to discover custom workflows: "Based on everything you know about me, what automations can we create?"
7. Mac Mini ($600) is the best value device for OpenClaw — avoid VPS (too expensive to scale memory)
8. Stay up to date on OpenClaw versions for security patches

*Analyzed from: Set up a multi-agent team using OpenClaw in Discord.txt*
