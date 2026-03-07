# 5 AI Agents, 1 Discord Server — Complete Transcript Analysis

**Video Title:** 5 AI Agents, 1 Discord Server - Full Setup Guide
**Channel:** Vibe with AI
**Video ID:** GwSYhTrWWuA
**Upload Date:** 2026-03-06
**Duration:** ~13m16s (~796s)
**Speaker:** Nino (Vibe with AI)
**Platform:** YouTube

---

## EXECUTIVE SUMMARY

A step-by-step guide to setting up a multi-agent Discord server using OpenClaw, where each AI agent appears as a separate Discord bot with its own channel. Nino demonstrates his setup with 5 persistent agents — Henry (chief of staff), Nexus (CTO), Ivy (researcher), Nox (security officer), and Mr. X (social media) — all running 24/7 on a Mac Mini. Covers Discord developer portal setup, bot permissions, token management, persistent agent configuration with heartbeat files, and a communication protocol where agents auto-post conversation summaries to work channels after 5 minutes of inactivity so the chief of staff stays informed. **No trading strategies — pure AI agent architecture/DevOps content.**

---

## KEY TOPICS

### Agent Team Architecture

| Agent | Role | Department |
|-------|------|------------|
| Nino (human) | Founder/CEO | — |
| Henry | Chief of Staff (main bot) | All channels |
| Nexus | CTO | Dev channel |
| Ivy | Researcher | Research channel |
| Nox | Security Officer | Security channel |
| Mr. X | Social Media | Social media channel |

- **Henry** is the main OpenClaw bot — set up first, creates sub-agents
- Sub-agents are **persistent agents** — awake 24/7 with heartbeat files
- Each agent has a **heartbeat.md** telling it to wake up at intervals (30min, 45min, 1hr)
- Agents proactively check task boards, think about next steps, execute tasks 3-4 times/day
- Each persistent agent can create its own sub-agents for specific tasks

### Discord Developer Portal Setup

1. Go to `discord.com/developers`
2. Create a new application for each agent (5 total)
3. For each application:
   - Go to **Bot** settings → enable **Server Members Intent** and **Message Content Intent**
   - Go to **OAuth2** → select scope: **bot**
   - Set bot permissions:
     - All agents: **View Channels**, **Send Messages**, **Read Message History**
     - Main agent only: **Manage Channels** (so it can create channels for other agents)
4. Copy the generated OAuth2 URL → open in browser → authorize bot to your Discord server
5. Go back to **Bot** tab → **Reset Token** → copy token
6. Give the token to your main agent (via Telegram or direct message)

### Discord Channel Structure

| Category | Channels | Access |
|----------|----------|--------|
| General | General, briefing, status | Henry (main bot) |
| Work | Dev, research, security, social media | Henry reads summaries |
| Agents | Direct-Ivy, Direct-Nexus, Direct-Nox, Direct-MrX | Nino talks to each agent individually |

- **Limitation:** OpenClaw only supports one channel per agent in Discord
- Cannot give multiple agents access to the same channel
- Nino talks to each department head through their dedicated agent channel

### Communication Protocol

1. If 5 minutes pass after Nino's last message, agent assumes conversation is over
2. Agent posts a **detailed summary** of the conversation to their work channel (dev, research, security, social media)
3. Agent also posts a **one-liner** to the status channel
4. Henry (chief of staff) reads status channel for quick updates
5. If Henry needs more detail, he reads the specific work channel
6. **Result:** Nothing gets lost; Henry is always up to date on all agent activities

### Persistent Agent Configuration

- Tag agents as `persistent` in OpenClaw config
- Each persistent agent gets a `heartbeat.md` file with wake-up intervals
- Agents wake up, check task board, think proactively, execute tasks
- Department heads lead their departments and have meetings with Henry
- Sub-agents under each department head handle specific tasks

---

## TOOLS & PLATFORMS MENTIONED

| Tool/Platform | Purpose |
|---------------|---------|
| OpenClaw | AI agent framework (base system) |
| Discord | Multi-agent communication server |
| Telegram | Initial setup channel (talk to main agent) |
| Mac Mini | Hardware running all 5 agents 24/7 |
| Discord Developer Portal | Bot creation and permission management |
| GitHub | Agent has secure account with scoped tokens (teased for next episode) |

---

## STRATEGIES EXTRACTED

None (AI agent architecture — no trading strategies)

---

## ACTIONABLE TAKEAWAYS

1. **Create separate Discord applications** for each agent — each gets its own bot identity, avatar, and permissions
2. **Main agent needs Manage Channels permission** — it creates the channel structure for you
3. **Use persistent agents with heartbeat files** — agents wake up at intervals and proactively check task boards
4. **Implement the 5-minute summary protocol** — agents auto-post to work channels after conversation ends, keeping the chief of staff informed
5. **One channel per agent limitation** — OpenClaw doesn't support multiple agents sharing channels; design around this
6. **Tokens via main agent** — give each agent's Discord bot token to the main agent, which handles the integration
7. **Status channel for quick overview** — one-liners give at-a-glance team activity; detailed summaries live in department channels

*Analysis derived from: 5 AI Agents, 1 Discord Server - Full Setup Guide.txt*
