# Step-by-Step Guide: Multi-Agent Discord Server with OpenClaw

**Source:** Vibe with AI / Nino (YouTube)
**Video ID:** GwSYhTrWWuA
**Upload Date:** 2026-03-06

---

## What This Guide Covers

How to set up a Discord server where multiple OpenClaw AI agents appear as separate bots, each with their own channel, identity, and role. Enables managing a full AI agent team (chief of staff, CTO, researcher, security, social media) through Discord with automatic conversation summaries and proactive task execution.

---

## Prerequisites

- **OpenClaw** installed and running with a main agent
- **Telegram** access to your main agent (for initial setup)
- A **Discord account**
- Hardware to run agents 24/7 (Mac Mini, server, etc.)

---

## Step 1: Create Your Discord Server

1. Open Discord
2. Click the **+** button on the left sidebar
3. Select **Create My Own** → **For me and my friends**
4. Name it (e.g., "HQ Mission Control")
5. Click **Create**

---

## Step 2: Create Discord Applications for Each Agent

Repeat for each agent (e.g., 5 times):

1. Go to **discord.com/developers/applications**
2. Click **New Application**
3. Name it after your agent (e.g., "Henry", "Nexus", "Ivy")
4. Agree to Discord Developer Terms → Click **Create**

---

## Step 3: Configure Bot Permissions

For each application:

1. Go to the **Bot** tab in the left sidebar
2. Scroll down to **Privileged Gateway Intents**
3. Toggle ON:
   - **Server Members Intent** (see members)
   - **Message Content Intent** (read/write messages)
4. Click **Save Changes**

---

## Step 4: Generate Invite URLs

For each application:

1. Go to **OAuth2** tab
2. Under **Scopes**, check **bot**
3. Under **Bot Permissions**, check:
   - **View Channels**
   - **Send Messages**
   - **Read Message History**
   - **Manage Channels** (ONLY for your main agent — allows it to create channels)
4. Copy the **Generated URL** at the bottom
5. Open the URL in a new browser tab
6. Select your Discord server → Click **Continue** → **Authorize**

---

## Step 5: Get Bot Tokens

For each application:

1. Go back to the **Bot** tab
2. Click **Reset Token** → confirm with your Discord password
3. Copy the token immediately (you won't see it again)
4. Give the token to your main agent via Telegram:
   - "Here is the Discord token for [agent name]: [token]"

---

## Step 6: Configure Persistent Agents in OpenClaw

Tell your main agent to set up persistent sub-agents:

1. Each agent should be tagged as **persistent** in the OpenClaw config
2. Create a **heartbeat.md** for each agent with instructions:
   ```
   Wake up every 30 minutes
   Check the task board for assigned tasks
   Think proactively about how to push your department forward
   Execute tasks 3-4 times per day
   Report to Henry (chief of staff) as needed
   ```
3. Each persistent agent runs 24/7 and wakes at the specified interval

---

## Step 7: Set Up Channel Structure

Tell your main agent (with Manage Channels permission):

> "Create the following channels on Discord:
> - General channels: #general, #briefing, #status
> - Work channels: #dev, #research, #security, #social-media
> - Agent channels: #direct-nexus, #direct-ivy, #direct-nox, #direct-mrx
>
> Give each agent access only to their direct channel. Give yourself (Henry) access to all general and work channels but NOT the agent channels."

**Note:** OpenClaw supports only one channel per agent — design accordingly.

---

## Step 8: Implement the 5-Minute Summary Protocol

Configure each agent with this rule:

> "If 5 minutes pass after the last message from me (Nino), assume the conversation is over. Then:
> 1. Post a detailed summary of our conversation to your work channel (e.g., #dev for Nexus)
> 2. Post a one-liner to the #status channel
> This ensures Henry can stay informed without reading every conversation."

---

## Channel Flow Diagram

```
You (human)
  ├── Talk to Henry in #general or Telegram
  ├── Talk to Nexus in #direct-nexus
  ├── Talk to Ivy in #direct-ivy
  ├── Talk to Nox in #direct-nox
  └── Talk to Mr. X in #direct-mrx

After 5 min silence:
  Nexus → posts summary to #dev + one-liner to #status
  Ivy → posts summary to #research + one-liner to #status
  Nox → posts summary to #security + one-liner to #status
  Mr. X → posts summary to #social-media + one-liner to #status

Henry reads #status for quick overview
Henry reads work channels for details
```

---

## Quick Reference: Bot Permissions

| Agent Type | View Channels | Send Messages | Read History | Manage Channels |
|-----------|:---:|:---:|:---:|:---:|
| Main (Henry) | Yes | Yes | Yes | Yes |
| Department heads | Yes | Yes | Yes | No |

---

## Recommended Agent Roles

| Agent | Role | Heartbeat | Key Responsibility |
|-------|------|-----------|-------------------|
| Henry | Chief of Staff | Always on | Coordination, task delegation, status monitoring |
| Nexus | CTO | 30 min | Development, PR reviews, code quality |
| Ivy | Researcher | 45 min | Research, analysis, data gathering |
| Nox | Security Officer | 1 hr | Security audits, vulnerability checks |
| Mr. X | Social Media | 30 min | Content creation, engagement, scheduling |

*Guide derived from: 5 AI Agents, 1 Discord Server - Full Setup Guide.txt*
