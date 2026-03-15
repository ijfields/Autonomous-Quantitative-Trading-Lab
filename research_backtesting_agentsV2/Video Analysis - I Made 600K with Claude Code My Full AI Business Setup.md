# I Made $600K with Claude Code. My Full AI Business Setup. — Complete Transcript Analysis

**Video Title:** I Made $600K with Claude Code. My Full AI Business Setup.
**Channel:** AI Chris Lee
**Video ID:** iesm1llYG9s
**Upload Date:** 2025-03-14
**Duration:** ~60m
**Speaker:** Chris Lee (founder, Execution Squad)
**Platform:** YouTube

---

## EXECUTIVE SUMMARY

Exhaustive structured tutorial on Claude Code from beginner to advanced, presented by Chris Lee, who built an AI consulting business to $600,000 in one year using Claude Code. Divided into a Beginner Track (Sections 1-5) covering installation, claude.md, screenshot loop workflow, permissions/plan mode, and full-stack app building, and an Advanced Track (Sections 6-9) covering context management/token economics, skills, MCP, and sub-agents. The video is a masterclass in Claude Code productivity techniques and cost optimization.

---

## KEY TOPICS

### Beginner Track

#### 1. Installation
- Requires Claude Pro plan
- Install via terminal, available in VS Code or AntiGravity (Google's IDE)

#### 2. claude.md (Project Brain)
- The most important concept — a file injected into every conversation before the first message
- Acts as persistent project rules across sessions
- Three layers: global, local, enterprise
- Best practices: keep under 200-500 lines, use bullet points, critical rules at top (primacy bias)
- Add rules when Claude makes the same mistake twice
- Never dump API docs into it

#### 3. Screenshot Loop Workflow
- "Task, Do, Verify" iterative loop
- Take full-page screenshot of design target (e.g., from golee.io)
- Paste into Claude Code with copied styles
- Compare side-by-side, iterate until matching
- Core workflow for building anything with AI

#### 4. Permissions and Plan Mode
- Four modes: Ask Before Edits (learning), Edit Automatically (daily driver), Plan Mode (read-only architecture), Bypass (power users)
- **Plan Mode is the "single biggest money-saver"** — building the wrong thing costs 10x more than planning
- Always plan before building

#### 5. Full Stack App Build
- Demo: proposal generator with login, e-signatures, Stripe payments
- Stack: Claude Code + Supabase (DB/auth) + Stripe (payments) + Netlify (deploy)
- Workflow: plan first → build → wire external services → deploy

### Advanced Track

#### 6. Context Management and Token Economics
Seven strategies:
1. Check /cost regularly
2. /clear when switching tasks
3. Manual /compact to control what survives compression
4. Add conciseness instructions to claude.md
5. Use cheaper models (Sonnet/Haiku) for sub-agents, reserve Opus for parent
6. Audit MCPs — they consume massive context
7. Write specific prompts; do research in plan mode before building

#### 7. Skills
- Reusable checklists + scripts that turn one-time work into permanent capability
- Extremely token-efficient: only front matter loads by default (~60-65 tokens)
- Self-improve over time as Claude encounters edge cases
- Example: lead scraping skill — 30 minutes manually → 87 seconds with skill

#### 8. MCP (Model Context Protocol)
- Third-party integrations: Gmail, ClickUp, Slack, Chrome browser control
- Fast to install but expensive to run (context overhead)
- Recommended workflow: install MCP → test → convert to skill for production
- Chrome Dev Tools MCP worth keeping permanently

#### 9. Sub-Agents
- Each has its own ephemeral context window
- Reliability math: 10 agents at 95% individual success = ~60% chance all succeed
- Rules: simple single-focused tasks, Sonnet/Haiku for sub-agents, write to files instead of returning large outputs to parent
- Agent Teams are experimental, ~7x token cost, can burn $10,000+/day

---

## TOOLS & PLATFORMS

| Tool | Purpose |
|------|---------|
| Claude Code | Core AI coding agent (the subject of the video) |
| Claude Pro Plan | Required for Claude Code access |
| AntiGravity | Google's AI coding platform |
| VS Code | IDE with Claude Code extension |
| Supabase | Database and authentication |
| Stripe | Payment processing |
| Netlify | Deployment/hosting |
| Figma | Design/prototyping |
| UX Pilot.ai | AI-powered mockup creation |
| Visily.ai | AI-powered mockup creation |
| golee.io | Website design browsing |
| 21st.dev | Pre-built component prompts |
| resizepng.com | Image resizing |
| MCPservers.org | MCP server directory |
| mcp.market | MCP marketplace |
| Google Sheets | Skill output target |

---

## CHRIS LEE'S KEY PRINCIPLES

1. **Claude Code is not a chatbot** — it's an agent that reads files, writes code, and ships products
2. **claude.md is the single most important file** — sets rules, reduces waste, improves quality
3. **Plan Mode before building** is the biggest money-saver
4. **Skills > MCPs** for token efficiency (dozens of skills cost less than a single MCP tool)
5. **Sub-agents need single-responsibility tasks** — reliability math punishes complexity
6. **Context management** (clear, compact, concise prompts, model selection) is the difference between efficient and wasteful usage
7. **"Screenshot Loop"** (task, do, verify) is the core iterative workflow

---

## KEY TAKEAWAY

> Claude Code is an agent, not a chatbot. The most impactful practices are: claude.md as a project brain (top priority), Plan Mode before building (biggest money-saver), Skills over MCPs for production (token efficiency), and strategic model selection for sub-agents (Sonnet/Haiku for workers, Opus for orchestrator). Chris Lee built a $600K consulting business in one year using these techniques.

*Analysis derived from: I Made $600K with Claude Code. My Full AI Business Setup..txt*
