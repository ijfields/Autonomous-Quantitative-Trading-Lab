# Step-by-Step Guide: Claude Code Remote Control (Access Sessions from Your Phone)

**Source:** Moon Dev (YouTube)
**Video ID:** 8kgUkgyLlbc
**Upload Date:** 2026-02-26

---

## What This Guide Covers

How to use Claude Code's Remote Control feature to start a coding session locally in your terminal and continue it from your phone or any other device. This allows you to step away from your desk while Claude continues working.

---

## Prerequisites

- **Claude Code** installed and running
- **Anthropic Max plan** (Remote Control is rolling out to Max users as a research preview)
- **Claude app** on your phone (iOS/Android) OR access to **claude.ai/code** in a browser

---

## Step 1: Start a Claude Code Session

1. Open your terminal
2. Navigate to your project directory
3. Launch Claude Code: `claude`
4. Begin your work as normal (give Claude a task, let it start working)

---

## Step 2: Enable Remote Control

1. In the Claude Code CLI, type: `/remote-control`
2. Claude will generate a unique URL for this session
3. **Save this URL** -- there is currently no dashboard to view active remote sessions

**Note:** The session is tied to your Anthropic account. Only someone logged into your account can access the link.

---

## Step 3: Access from Your Phone

1. Open the **Claude app** on your phone (or go to **claude.ai/code** in a mobile browser)
2. Paste the remote control URL or navigate to it
3. You now have full access to the Claude Code session:
   - See what Claude is working on
   - Send new prompts
   - Use voice input to command Claude
   - Review output and approve actions

---

## Step 4: Use Voice Commands (Optional)

1. On the Claude app, tap the microphone icon
2. Speak your command (e.g., "Go ahead and build me a backtest from our templates")
3. Claude will execute the voice command just like a typed prompt

---

## Step 5: Multiple Remote Sessions

1. Open another terminal tab (Ctrl+Shift+5 in VS Code)
2. Launch Claude Code: `claude`
3. Run `/remote-control` to get a second URL
4. Repeat for as many sessions as needed
5. Access each session via its unique URL on your phone

**Current limitation:** There's no list view of active remote sessions. You must save each URL manually.

---

## Key Notes

| Feature | Status |
|---------|--------|
| Availability | Max plan users (research preview) |
| Command | `/remote-control` |
| Security | Account-tied (requires your Anthropic login) |
| Voice input | Supported via Claude app |
| Multiple sessions | Supported (one URL per session) |
| Session list/dashboard | Not yet available |
| MCP servers | Stay connected while remote |
| Local environment | Stays connected -- Claude accesses your files |

*Guide derived from: Claude Code's New Secret Feature Nobody Is Talking About (Remote Control).txt*
