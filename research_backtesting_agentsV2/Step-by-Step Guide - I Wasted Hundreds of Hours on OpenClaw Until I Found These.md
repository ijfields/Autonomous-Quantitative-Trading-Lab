# Step-by-Step Guide: I Wasted Hundreds of Hours on OpenClaw Until I Found These

**Source:** Craig Hewitt (YouTube)
**Video ID:** MhLM-12ENOM
**Upload Date:** 2026-03-13

---

## What This Guide Covers
How to set up a multi-agent Discord server with OpenClaw, giving each persistent AI agent its own identity, dedicated channel, and automatic conversation summarization.

---

## Step 1: Establish Your Agent Team Architecture
1. Define your main agent (e.g., "Henry" -- Chief of Staff) as the one you communicate with via Telegram
2. Define your persistent sub-agents, each leading a department (e.g., CTO, Researcher, Security, Social Media)
3. Tell your main agent to set up persistent agents -- these are agents with a heartbeat that wake up on intervals (every 30-60 minutes)
4. Configure each persistent agent with a heartbeat.md that instructs it to check the taskboard, think proactively, and execute tasks multiple times per day

## Step 2: Create a Discord Server
1. Open Discord and click the plus (+) button on the left sidebar
2. Click "Add a server" then "Create My Own"
3. Select "For me and my friends"
4. Name your server (e.g., "HQ Mission Control") and click Create

## Step 3: Create Discord Bot Applications for Each Agent
1. Navigate to discord.com/developers in your browser
2. Click "New Application"
3. Enter the agent's name (e.g., "Henry") and agree to the developer terms
4. Click Create and confirm you are human
5. Repeat this process for every agent in your team (one application per agent)

## Step 4: Configure Bot Permissions
1. In each application, go to the "Bot" tab
2. Scroll down to "Privileged Gateway Intents"
3. Toggle ON "Server Members Intent" (so the bot can see members)
4. Toggle ON "Message Content Intent" (so the bot can read and write messages)
5. Click "Save Changes"

## Step 5: Set Up OAuth2 Invite URLs
1. Go to the "OAuth2" section in the application settings
2. Under "Scopes," select "bot"
3. Under "Bot Permissions," select:
   - View Channels
   - Send Messages
   - Read Message History
4. For the MAIN agent only, also select "Manage Channels" (so it can create channels automatically)
5. Copy the generated URL at the bottom of the page

## Step 6: Invite Bots to Your Discord Server
1. Open the generated URL in a new browser tab
2. Select your Discord server from the dropdown
3. Click "Continue" then "Authorize"
4. Repeat for each agent bot application

## Step 7: Generate and Distribute Bot Tokens
1. Go back to each application in discord.com/developers
2. Navigate to the "Bot" tab
3. Click "Reset Token" and enter your Discord password
4. Copy the generated token
5. Send the token to your main agent (via Telegram or however you communicate with it)
6. Your main agent will use these tokens to connect each sub-agent to its Discord identity

## Step 8: Let the Main Agent Set Up Channels
1. Tell your main agent (with manage channels permission) to create dedicated channels for each department head
2. The main agent will create direct communication channels (e.g., #nexus, #ivy, #nox, #mr-x)
3. Each channel is accessible only to you and that specific agent -- the main agent does not have access to these direct channels
4. Also have the main agent create work channels (e.g., #dev, #research, #security, #social-media) and a #status channel

## Step 9: Configure Automatic Conversation Summaries
1. Instruct each agent that if 5 minutes pass after your last message, the conversation is considered over
2. Each agent should then post a detailed summary to its department work channel
3. Each agent should also post a one-liner update to the shared #status channel
4. This ensures the main agent (Chief of Staff) stays informed about all conversations without direct channel access

## Step 10: Test Your Setup
1. Go to a direct agent channel (e.g., #nexus) and send a message
2. Verify the agent responds with its correct identity
3. Wait 5 minutes and confirm the summary appears in the appropriate work channel and the status channel
4. Repeat for each agent

---

## Key Takeaway

> A multi-agent Discord server transforms OpenClaw from a single-bot conversation into a full team management system, with direct communication lines to each department head and automatic summarization that keeps everyone informed.

*Guide derived from: I Wasted Hundreds of Hours on OpenClaw Until I Found These.txt*
