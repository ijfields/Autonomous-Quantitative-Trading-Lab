# Step-by-Step Guide: OpenClaw Discord Setup — How To Connect OpenClaw Bot To DISCORD

**Source:** How To Financial (YouTube)
**Video ID:** u22_aE1Bbt8
**Upload Date:** 2026-02-01

## Prerequisites
- **Software:** OpenClaw (ClawBot) already installed on a device (VPS recommended for safety)
- **Accounts:** Discord account, Discord Developer Portal access
- **Knowledge:** Basic terminal/command line familiarity, OpenClaw setup wizard experience
- **Reference:** Full OpenClaw setup guide video (linked in speaker's pinned comment) — this video only covers the Discord connection portion

---

## Part 1: Create a Discord Bot

### Step 1: Open the Discord Developer Portal
Navigate to the Discord Developer Portal (Applications section).

- Go to the Applications menu
- Click **New Application** in the top right
- Choose a name for your bot (e.g., "OpenClaw 2")
- Check the box agreeing to Discord's developer terms of service
- Click **Create**
- Complete any verification prompts
- Expected result: A new application page with your bot's settings

### Step 2: Get the Bot Token
Navigate to the **Bot** section in the left-hand menu.

- Click **Reset Token** to generate a new token
- Click **Yes, do it!** to confirm
- Complete Discord account verification if prompted
- **Important:** Copy the token immediately — you can only see it once. If you miss it, you'll need to create another bot
- Expected result: A bot token string copied to your clipboard

> Speaker's tip: "You can only see this token once. And if you miss it, you would need to create another bot."

---

## Part 2: Create and Configure a Discord Server

### Step 3: Create a Discord Server
In the Discord app, create a new server for your bot.

- Click **Add Server** (the "+" icon in the left sidebar)
- Select **Create My Own**
- Choose **For me and my friends**
- Name your server (e.g., "OpenClaw Server")
- Click **Create**
- Expected result: A new Discord server with a default #general channel

### Step 4: Generate the Bot Invite URL
Return to the Discord Developer Portal to create an invite link.

- Navigate to your application settings
- Click on **OAuth2** in the left menu
- Scroll down to the **OAuth2 URL Generator** section
- Under **Scopes**, select **bot**
- Under **Bot Permissions**, select **Administrator** (highest general permission)
- Copy the generated URL at the bottom of the page
- Expected result: A URL that will invite your bot to a server

### Step 5: Invite the Bot to Your Server
Paste the invite URL into your browser.

- The URL opens Discord's bot authorization page
- Select the server you just created from the **Add to Server** dropdown
- Click **Continue**
- Confirm the **Administrator** permission
- Click **Authorize**
- Complete any CAPTCHA verification
- Expected result: The bot appears as a member in your Discord server

> Speaker's tip: "As you can see the bot that we created has joined the server."

---

## Part 3: Connect Discord to OpenClaw

### Step 6: Enter the Bot Token in OpenClaw Setup
Return to your terminal where the OpenClaw setup wizard is running.

- At the communication channel selection step, use arrow keys to select **Discord**
- Press **Enter**
- Wait for the short guide text to load (may take a few seconds)
- Paste your bot token when prompted
- Press **Enter**
- Expected result: OpenClaw accepts the token and moves to channel configuration

### Step 7: Configure Discord Channel Access
Set which channels the bot can access.

- When asked about Discord channel access, select **Yes**
- Choose **Allow list (recommended)** — this restricts the bot to specific channels
- Enter the channel path in the format: `ServerName/channel-name`
  - Example: `OpenClaw Server/general`
- Press **Enter**
- Expected result: Channel configured, Discord section of setup complete

> Speaker's tip: "I only have the general channel. So I will just write my server name which is OpenClaw Server and then /general."

---

## Common Pitfalls
- **Token visibility:** The bot token is shown only once after creation. Copy it immediately or you'll need to reset and generate a new one.
- **Server selection:** Make sure to select the correct server when authorizing the bot — if you have multiple Discord servers, double-check the dropdown.
- **Permission level:** The video uses Administrator permission for simplicity. For production use, you may want to limit permissions to only Send Messages, Read Message History, and Embed Links.
- **Channel name format:** When configuring allowed channels, use the exact format `ServerName/channel-name` (case-sensitive).
- **VPS recommended:** The speaker emphasizes installing OpenClaw on a VPS rather than a personal computer for security and uptime.

---

## Resources Mentioned
- **Discord Developer Portal** — Where you create and manage Discord bots and applications
- **OpenClaw / ClawBot** — AI agent platform with terminal-based setup wizard
- **Full OpenClaw setup guide** — Referenced as prerequisite (linked in speaker's pinned comment)

---

## Summary
This ~6-minute tutorial walks through connecting OpenClaw (ClawBot) to Discord as a communication channel. The process involves three main phases: (1) creating a Discord bot in the Developer Portal and copying its one-time-visible token, (2) creating a Discord server and inviting the bot via OAuth2 URL with Administrator permissions, and (3) pasting the token into OpenClaw's setup wizard and configuring allowed channel access using an allow-list. The speaker notes this covers only the Discord connection portion — viewers should follow the full setup guide for complete OpenClaw installation.

*Extracted from: OpenClaw Discord Setup- How To Connect OpenClaw Bot To DISCORD.txt*
