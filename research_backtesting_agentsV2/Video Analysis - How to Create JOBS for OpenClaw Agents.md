# How to create JOBS for OpenClaw agents — Complete Transcript Analysis

**Video Title:** How to create JOBS for OpenClaw agents
**Channel:** Brian Casel
**Video ID:** uUN1oy2PRHo
**Upload Date:** 2026-02-25
**Duration:** ~21m
**Speaker:** Brian Casel (Builder Methods)
**Platform:** YouTube

---

## EXECUTIVE SUMMARY

Brian Casel presents a framework for treating OpenClaw agents as employees filling defined roles, not as reactive chat assistants. He built three supporting systems: BMHQ (custom Rails scheduling dashboard), codified processes (skills), and Brainown (markdown output manager). His 4 named agents run in a dedicated Telegram folder, each with recurring jobs defined in the task board. The key insight: agent roles have no minimum threshold — start with 1-2 recurring tasks at pennies per execution.

---

## KEY TOPICS

### The Three Systems

#### System 1: Scheduling (BMHQ)
- Custom Rails app running on Mac Mini alongside OpenClaw
- Kanban-style task board with views by status and by agent
- Task templates define recurring tasks (daily, 3x/day, 2x/week, monthly)
- Tasks have "pre-instructions" (prepended to every task) and specific instructions
- Dispatches directly to OpenClaw gateway API
- Agents report back via Telegram when done

#### System 2: Processes (Skills)
- Folders containing markdown + optional reference files and scripts
- "Operating manual" for each job
- Symlinked to Dropbox for cross-machine access
- Skills improve over time with Claude Code iteration
- "When you're improving your set of skills, you're literally making your team of agents better at their jobs"

#### System 3: Output Management (Brainown)
- Custom markdown editor/viewer integrating with Dropbox
- Agents produce markdown artifacts, send links via Telegram
- View/edit/create notes from mobile or desktop
- Daily notes compiled by "Gumbo" (general assistant agent)

### His Agent Setup
- 4 named agents in a dedicated Telegram folder
- "Gumbo": general assistant — intake, daily notes, activity capture
- Others handle marketing, development, content
- Each has specific recurring jobs in BMHQ

---

## TOOLS & PLATFORMS

| Tool | Purpose |
|------|---------|
| OpenClaw | Agent framework (Mac Mini) |
| Claude Code | Building tools and iterating on skills |
| BMHQ | Custom Rails scheduling dashboard |
| Brainown | Custom markdown editor/viewer |
| Telegram | Agent-to-human communication |
| Dropbox | File sync (restricted access for security) |
| GitHub | Code activity tracking |

---

## KEY TAKEAWAY

> The most powerful OpenClaw mental model is treating agents like employees filling defined roles. You need three systems: automated scheduling, codified processes (skills), and structured output management. Skills are the core lever for improving agent quality over time — invest in refining them. Agent roles have a dramatically lower threshold than human hires — start small at pennies per execution and scale.

*Analysis derived from: How to create JOBS for OpenClaw agents.txt*
