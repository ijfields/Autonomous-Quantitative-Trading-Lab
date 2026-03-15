# Step-by-Step Guide: Creating JOBS for OpenClaw Agents

**Source:** Brian Casel (YouTube)
**Video ID:** uUN1oy2PRHo
**Upload Date:** 2026-02-25

---

## What This Guide Covers

A framework for treating OpenClaw agents as employees with recurring responsibilities, built on three systems: scheduling, processes (skills), and output management.

---

## Step 1: Shift Your Mindset
1. Stop thinking "tasks" — start thinking "jobs"
2. A job is a recurring need with a predictable cadence
3. Unlike human hires, agent roles have no minimum threshold — start with 1-2 recurring tasks at pennies per execution
4. Two categories: (1) things you currently do that you want off your plate, (2) missed opportunities that weren't getting done

## Step 2: Map Your Business Processes
1. Use Claude as a thought partner (voice recordings, long conversations)
2. Map out every recurring workflow in your business
3. Identify which workflows can be codified into skills
4. Prioritize by frequency and time cost

## Step 3: Build a Scheduling System
1. Build or use a task management dashboard (Brian built BMHQ in Rails)
2. Create task templates for recurring work (daily, 3x/day, weekly, monthly)
3. Define "pre-instructions" (prepended to every task) and specific instructions
4. Dispatch tasks to OpenClaw gateway API automatically
5. Set up Telegram notifications for completed tasks

## Step 4: Codify Processes as Skills
1. Create skill folders with markdown files + optional reference files and scripts
2. Each skill is an "operating manual" for a particular job
3. Symlink skills to Dropbox for cross-machine access
4. Iterate and improve skills with Claude Code
5. "When you're improving your set of skills, you're literally making your team of agents better at their jobs"

## Step 5: Set Up Output Management
1. Agents produce markdown artifacts — need a way to review them
2. Build or use a markdown viewer with Dropbox integration
3. Set up mobile access for reviewing agent output on the go
4. Have a general assistant agent compile daily notes

## Step 6: Create Named Agents
1. Set up 3-4 named agents in a dedicated Telegram folder
2. Assign each agent specific recurring jobs from the task board
3. Keep agent roles separate from human contacts for clarity
4. Start with one general assistant, then add specialists

---

## Key Takeaway

> The most powerful OpenClaw mental model: agents are employees filling defined roles. You need three systems: automated scheduling, codified processes (skills), and structured output management. Invest in refining skills — they are the core lever for improving agent quality over time.

*Guide derived from: How to create JOBS for OpenClaw agents.txt*
