# Step-by-Step Guide: Using Agency Agents with Claude Code for Parallel Sub-Agents

**Source:** FuturMinds (YouTube)
**Video ID:** f3rDD5I53Bk
**Upload Date:** 2026-03-12

---

## What This Guide Covers

How to use the Agency Agents open-source repo (30K GitHub stars) to create structured AI personas and run them as parallel sub-agents in Claude Code with persistent memory.

---

## Step 1: Get the Repo
1. Go to the Agency Agents GitHub repository
2. Fork and clone it to your local machine
3. Review the ~120 persona files across divisions: marketing, engineering, sales, design, QA, game dev

## Step 2: Install into Claude Code
1. Run the setup command to transform agent files into sub-agent directories
2. The setup places persona files at the correct path for Claude Code to discover them
3. Verify: you should be able to reference agents by name in your prompts

## Step 3: Use a Single Agent
1. Reference an agent by name or tag the .md file in your prompt
2. Example: "Using the Content Strategist agent, create a B2B SaaS content marketing strategy"
3. The structured persona produces ~60-70% better output than a generic prompt

## Step 4: Run Multi-Agent Orchestration
1. Tell Claude Code to launch multiple sub-agents in parallel
2. Example: "Launch three sub-agents simultaneously — one for UX layout research, one for content strategy, one for SEO requirements"
3. Claude acts as the orchestrator, routing tasks to the right specialist
4. Results from all agents are collected and synthesized

## Step 5: Customize for Long-Term Value
1. Pick an agent close to your needs
2. Customize: change personality, colors, add custom tools
3. Set a specific model: `model: your_model_name`
4. Add persistent memory: `memory: project`
5. Persistent memory gives the agent a directory that survives across conversations, learning from your patterns and terminology

## Step 6: Iterate and Improve
1. Quality varies across the 120 personas — some are thin
2. Test against generic prompts to verify improvement
3. Add domain-specific knowledge to your customized agents
4. The repo is a starting point — fork and evolve, not a finished product

---

## Key Takeaway

> Structured AI personas produce measurably better output (~60-70% improvement). The real power: using Claude Code to run them as parallel sub-agents with persistent memory. Fork, customize, and iterate for best results.

*Guide derived from: This Free Repo Replaces Your Entire Team ｜ Agency Agents + Claude Code.txt*
