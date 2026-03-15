# Step-by-Step Guide: Mastering Claude Code from Beginner to Advanced

**Source:** AI Chris Lee (YouTube)
**Video ID:** iesm1llYG9s
**Upload Date:** 2025-03-14

---

## What This Guide Covers

Complete Claude Code workflow from installation through advanced techniques (skills, MCPs, sub-agents), based on Chris Lee's experience building a $600K AI consulting business in one year.

---

## Step 1: Install Claude Code

1. Get a Claude Pro plan (required for Claude Code access)
2. Install Claude Code via terminal
3. Choose your IDE: VS Code (with Claude Code extension) or AntiGravity (Google's AI IDE)
4. Verify installation by running Claude Code in a project directory

---

## Step 2: Create Your claude.md (Project Brain)

1. Create a `claude.md` file in your project root
2. This file is injected into every conversation before the first message
3. Keep it under 200-500 lines
4. Use bullet points for clarity
5. Put critical rules at the top (primacy bias — models pay most attention to what comes first)
6. Add rules when Claude makes the same mistake twice
7. **Never** dump API docs into claude.md — link to them or use MCP instead
8. Three layers available: global (~/.claude/claude.md), local (project root), enterprise

---

## Step 3: Master the Screenshot Loop (Task, Do, Verify)

1. Find a design reference (golee.io, Figma, existing site)
2. Take a full-page screenshot of the target design
3. Paste the screenshot into Claude Code with any relevant styles
4. Let Claude generate the code
5. Compare side-by-side with the target
6. Iterate: point out differences, let Claude fix them
7. Repeat until satisfied — this is the core iterative workflow for everything

---

## Step 4: Use Plan Mode Before Building

1. Switch to Plan Mode (read-only — Claude can explore code but not edit)
2. Describe your project architecture and goals
3. Let Claude analyze the codebase and propose an approach
4. Review the plan, ask questions, refine
5. Once approved, switch to Edit mode and build
6. **Plan Mode is the "single biggest money-saver"** — building the wrong thing costs 10x more than planning

---

## Step 5: Build a Full-Stack App

1. Start in Plan Mode to design the architecture
2. Choose your stack (video uses Supabase for DB/auth, Stripe for payments, Netlify for deployment)
3. Build features incrementally — one at a time
4. Wire external services (Stripe, Supabase) with Claude's help
5. Deploy to hosting (Netlify, Vercel, etc.)
6. Test thoroughly before shipping

---

## Step 6: Manage Context and Costs

Seven strategies for token efficiency:
1. Check `/cost` regularly to monitor spending
2. Use `/clear` when switching tasks (prevents context pollution)
3. Use manual `/compact` to control what survives compression
4. Add conciseness instructions to claude.md ("be concise, no preamble")
5. Use cheaper models (Sonnet/Haiku) for sub-agents, reserve Opus for the parent
6. Audit MCPs — they consume massive context even when not actively used
7. Write specific prompts; do research in Plan Mode before building

---

## Step 7: Build Skills for Repeatable Tasks

1. Identify tasks you do repeatedly (scraping, formatting, deployment, etc.)
2. Create a skill: a reusable checklist + script that turns one-time work into permanent capability
3. Skills are extremely token-efficient — only front matter loads by default (~60-65 tokens)
4. Skills self-improve over time as Claude encounters edge cases
5. Example: a lead scraping skill reduced 30-minute manual work to 87 seconds

---

## Step 8: Install MCPs Strategically

1. Browse MCP directories: MCPservers.org, mcp.market, GitHub modelcontextprotocol/servers
2. Install relevant MCPs (Gmail, ClickUp, Slack, Chrome browser control)
3. **Warning:** MCPs are fast to install but expensive to run (context overhead)
4. Recommended workflow: install MCP → test it → convert to a skill for production
5. Keep Chrome Dev Tools MCP permanently — it's worth the context cost

---

## Step 9: Use Sub-Agents Effectively

1. Understand reliability math: 10 agents at 95% success = only ~60% all succeed
2. Give each sub-agent a single, focused task
3. Use Sonnet/Haiku for sub-agents (cheaper), Opus for the parent agent
4. Don't return large outputs to parent — write results to files instead
5. Agent Teams are experimental: ~7x token cost, can burn $10,000+/day
6. Start with simple sub-agent patterns before attempting Agent Teams

---

## Key Takeaway

> Claude Code is an agent, not a chatbot. The highest-impact practices: claude.md as a project brain (always first), Plan Mode before building (biggest money-saver), Skills over MCPs for production (token efficiency), and strategic model selection for sub-agents. Master these four and you'll be in the top tier of Claude Code users.

*Guide derived from: I Made $600K with Claude Code. My Full AI Business Setup..txt*
