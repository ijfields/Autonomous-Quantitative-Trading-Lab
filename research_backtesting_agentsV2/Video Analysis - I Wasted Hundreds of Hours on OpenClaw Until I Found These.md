# Video Analysis: I Wasted Hundreds of Hours on OpenClaw Until I Found These

**Speaker:** Nino (Vibe with AI)
**Channel:** Craig Hewitt
**Video ID:** MhLM-12ENOM
**Upload Date:** 2026-03-13
**Duration:** ~13 minutes

---

## Summary
Nino from the "Vibe with AI" channel walks through his multi-agent Discord setup powered by OpenClaw. He manages a team of five persistent AI agents -- Henry (Chief of Staff), Nexus (CTO), Ivy (Researcher), Nox (Security Officer), and Mr. X (Social Media) -- all running 24/7 on a Mac Mini. The video specifically addresses how to set up Discord so that each agent has its own identity and dedicated communication channel.

The core tutorial covers creating separate Discord bot applications for each agent via discord.com/developers, configuring permissions (view channel, send message, read message history, and manage channels for the main agent), generating OAuth2 invite URLs, and distributing bot tokens to the main agent. This allows the user to talk directly to any department head in its own channel, bypassing the limitation of only communicating through the main agent.

A key architectural insight is the 5-minute conversation summary system: after five minutes of inactivity, each agent automatically posts a detailed summary to its department work channel and a one-liner to a shared status channel. This ensures Henry (the main agent) stays informed about all conversations and actions across the team without needing direct access to every channel.

## Key Topics
- Multi-agent Discord server architecture with OpenClaw
- Persistent agents with heartbeat systems (waking up on intervals)
- Discord bot creation via discord.com/developers
- OAuth2 permissions and bot token management
- Direct communication channels to individual AI agents
- Automatic conversation summarization and cross-agent awareness
- Taskboard integration for proactive agent work

## Tools & Technologies Mentioned
- OpenClaw (AI agent platform)
- Discord (communication platform / bot hosting)
- Telegram (original communication channel)
- Mac Mini (hardware for running agents)
- discord.com/developers (bot management portal)

## Strategies Found
No specific trading strategies with concrete entry/exit rules were presented. This video focuses entirely on AI agent infrastructure and Discord setup.

## Notable Quotes / Insights
- "If you don't want to set up a sub agent that only gets called when executing a task, but you want to create agents that are awake 24/7, that have a heartbeat, they wake up continuously, think proactively and push your project forward -- you need to tell your main bot to set up persistent agents."
- "The problem is with OpenClaw and Discord, you can only set up one channel per agent. You cannot give multiple agents access to multiple channels."
- "I've set up in the configuration that if five minutes pass after my last message, they automatically have to assume the conversation is over for now and they have to post a detailed summary."

## Actionable Takeaways
1. Create separate Discord bot applications for each AI agent at discord.com/developers to give them individual identities
2. Give each bot the minimum permissions: view channel, send message, and read message history; give only the main agent the manage channels permission
3. Use persistent agents with heartbeat configurations to enable proactive work on intervals (every 30-60 minutes)
4. Set up automatic conversation summaries that post to department-specific work channels after a period of inactivity
5. Use a shared status channel with one-liner updates so the chief-of-staff agent can monitor all department activities at a glance
6. Let the main agent handle Discord channel creation and organization rather than setting it up manually
