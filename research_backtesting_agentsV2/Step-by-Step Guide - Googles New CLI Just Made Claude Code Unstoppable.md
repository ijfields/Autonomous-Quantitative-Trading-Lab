# Step-by-Step Guide: Google Workspace CLI + Claude Code for Zero-Cost Automation

**Source:** Mark Kashef (YouTube)
**Video ID:** 1Z1aECGwJh0
**Upload Date:** 2026-03-09

---

## What This Guide Covers

How to install Google Workspace CLI and use it with Claude Code to automate Gmail, Calendar, Drive, Docs, Sheets, and Slides — replacing paid tools like Zapier.

---

## Prerequisites

- Node.js / npm installed
- Claude Code subscription
- Google account (personal or Workspace)

---

## Step 1: Install Google Workspace CLI

```bash
npm install -g @google-workspace/cli
```

---

## Step 2: Set Up OAuth Credentials

1. Use Kashef's "mega prompt" (linked in video description) — paste it into Claude Code
2. Claude Code + Chrome will automatically navigate the Google Cloud Console and set up OAuth
3. For business accounts: remove the "do not pause for confirmations" line so you can supervise each step
4. Authenticate once; credentials persist

---

## Step 3: Use Compound Workflow Prompts

### Email Prioritization
> "Read my last 20 Gmail messages, categorize each by priority (high/medium/low), and output to a color-coded Google Sheet."

### Weekly Meeting Report
> "Pull all calendar events for this week, count meetings/hours/top contacts, chain to last 30 emails by domain, produce a Google Slides Weekly Report."

### Auto Follow-Up on Stale Threads
> "Search Gmail for threads containing 'proposal', 'quote', 'invoice', or 'contract' from the last 30 days. If I sent the last email more than 5 days ago, draft a follow-up from this template: [template]."

### Meeting Brief Generator
> "Find my next calendar event with attendees, search Gmail for 14-day correspondence with those people, create a Google Doc Meeting Brief with context and suggested agenda."

### Drive Audit
> "Search Drive for files named 'draft', 'old', 'copy', 'backup', 'V1', 'V2', 'V3', 'final' variants. Output file name, type, last modified, size, and shareable link into a Google Sheet called 'Drive Audit'."

---

## Step 4: Build Skills for Repeated Workflows

1. Test a workflow as a one-off CLI prompt first
2. Once working, crystallize it as a Claude Code skill for reuse
3. Priority order: CLI (one-off) → Skills (repeated) → MCP (only if needed)

---

## Key Takeaway

> Google Workspace CLI + Claude Code replaces paid automation platforms with zero per-task cost. The only expense is token usage. Chain multiple Google services in a single prompt for compound workflows that would require multiple Zapier zaps.

*Guide derived from: Google's New CLI Just Made Claude Code Unstoppable.txt*
