# Step-by-Step Guide: Claude Code 2.0 Key Features

**Source:** WorldofAI (YouTube)
**Video ID:** ShTxTquBDxY
**Upload Date:** 2026-03-13

---

## What This Guide Covers

Key new Claude Code features and how to use them: `/btw` side questions, `/loop` scheduling, desktop scheduled tasks with Telegram, structured memory, voice mode, Excel/PowerPoint sync, and effort levels.

---

## Feature 1: `/btw` — Quick Side Questions
1. During a long-running task, type `/btw` followed by your question
2. Claude answers without adding it to the conversation history
3. Use for quick lookups that shouldn't derail current work

## Feature 2: `/loop` — Session-Level Cron
1. Type `/loop` and specify an interval and prompt
2. Claude Code executes the prompt on that recurring schedule
3. Example: "Every 30 minutes, summarize recently merged PRs"
4. Note: session-level only — stops when session ends

## Feature 3: Desktop Scheduled Tasks + Telegram
1. Create scheduled tasks in Claude Desktop App (persistent while computer is awake)
2. To add Telegram delivery:
   - Create a bot via **BotFather** on Telegram
   - Add bot credentials to your `.env` file
   - Add "send the output to Telegram" at the end of task prompts
3. Use cases: daily code reviews, dependency updates, morning briefings

## Feature 4: Structured Memory Format
1. When writing to MEMORY.md or auto-memory, use this template:
   - **Rule/Fact:** What the memory is
   - **Why:** The reason or motivation
   - **How:** When/how it should influence Claude's behavior
2. This improves cross-session context retention

## Feature 5: Voice Mode
1. Toggle with `/v` command
2. Now generally available to all Claude Code users
3. Speak to your agent instead of typing

## Feature 6: Effort Levels
1. At session start, choose: **low**, **medium**, **high**, or **max**
2. Controls reasoning depth, work duration, and cost
3. Use low for quick tasks, max/ultra for deep work

## Feature 7: Multi-Agent Code Review
1. Available on **Team and Enterprise** plans only
2. Costs ~$15-$25 per run
3. Deep review catching bugs human reviewers miss
4. Same system Anthropic runs on internal PRs

---

## Key Takeaway

> The `/btw` command and structured memory format are the most impactful everyday features — they solve context pollution and cross-session amnesia, the two most common frustrations with AI coding agents.

*Guide derived from: Claude Code 2.0 MASSIVE Upgrade! (Game Changer).txt*
