# Step-by-Step Guide: Building a Persistent Memory System for AI Agents (OpenBrain)

**Source:** AI News & Strategy Daily | Nate B Jones (YouTube)
**Video ID:** japT66frdhM
**Upload Date:** 2025-03-14

---

## What This Guide Covers

How to build "OpenBrain" — a personal database system that gives ALL your AI tools (Claude, ChatGPT, OpenClaw) persistent memory across sessions, with both agent and human interfaces, hosted entirely for free.

---

## Step 1: Set Up Supabase (Data Layer)

1. Create a free account at supabase.com
2. Create a new project
3. Design your first table (e.g., "household_knowledge"):
   - Columns: id, category, key, value, notes, created_at, updated_at
4. The table is your single source of truth — both humans and AI agents will read/write here
5. No sync layer, no middleware, no export needed

---

## Step 2: Connect MCP to Supabase (Agent Interface)

1. Install the Supabase MCP server in your AI tool (Claude Code, ChatGPT, OpenClaw)
2. Configure it with your Supabase project URL and API key
3. Test: ask your AI to "save my WiFi password as XYZ" — it should write to the table
4. Test: ask "what's my WiFi password?" — it should read from the table
5. The AI agent now has persistent memory across sessions

---

## Step 3: Build a Web Interface (Human Door)

1. Ask Claude or ChatGPT to generate a small web app that reads/writes to your Supabase table
2. Use a simple framework (React, plain HTML/JS, or whatever the AI generates)
3. Deploy for free on Vercel:
   - Push code to GitHub
   - Connect to Vercel
   - Deploy with one click
4. Bookmark on your phone for mobile access
5. Alternative shortcut: use Lovable (SaaS tool) to build the interface visually

---

## Step 4: Build Practical Use Cases

### Household Knowledge Base
- Paint colors, plumber contacts, WiFi passwords, kids' shoe sizes
- Log conversationally — AI categorizes automatically
- Table: category | key | value | notes

### Professional Relationship Manager
- Track contacts, last interaction date, conversation notes
- AI flags neglected relationships (no contact in 90+ days)
- Suggests warm re-introductions based on context
- Cross-references LinkedIn and conference notes

### Job Search Dashboard
- Multi-table: applications, interviews, resume versions, contact networks
- AI detects patterns across interviews (common questions, topics)
- Track pipeline stages: applied → phone screen → interview → offer

### Home Maintenance Tracker
- Warranty dates, service dates, contractor contacts
- AI sends proactive alerts for expiring warranties
- Log maintenance conversationally — AI categorizes and schedules

---

## Step 5: Apply the Five Design Principles

Use these to identify new "agent-susceptible" problems to solve:

1. **Agent bridges time** — linking events across months/years that humans forget
2. **Agent sees across categories** — cross-referencing tables humans wouldn't think to connect
3. **Scattered information** — data spread across apps, notes, conversations, emails
4. **Human-agent loop** — agent surfaces insight → human decides → agent executes
5. **Data visualization** — visual interface makes agent insights accessible to non-technical users

---

## Step 6: Scale Without OpenClaw

1. You do NOT need OpenClaw to get value from this system
2. Any AI tool with MCP support (Claude, ChatGPT) can read/write to the database
3. OpenClaw adds autonomous monitoring (e.g., "check warranty dates daily and alert me") but is optional
4. As AI models improve, your data automatically becomes more valuable — smarter models reason better over the same tables
5. The system is model-agnostic and future-proof

---

## Key Takeaway

> The fundamental design: make the database table the single source of truth, accessed by agents via MCP and by humans via a simple web UI. No sync, no export, no middleware. The entire system (Supabase free tier + Vercel free tier) costs $0 to host. Start with one table (household knowledge), prove the concept, then expand to relationships, job search, maintenance, or any domain where information is scattered across time and tools.

*Guide derived from: One Simple System Gave All My AI Tools a Memory. Here's How..txt*
