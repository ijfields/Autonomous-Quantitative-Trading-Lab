# Google's New CLI Just Made Claude Code Unstoppable — Complete Transcript Analysis

**Video Title:** Google's New CLI Just Made Claude Code Unstoppable
**Channel:** Mark Kashef
**Video ID:** 1Z1aECGwJh0
**Upload Date:** 2026-03-09
**Duration:** ~14m
**Speaker:** Mark Kashef
**Platform:** YouTube

---

## EXECUTIVE SUMMARY

A walkthrough of Google Workspace CLI (`gws`) — a free command-line interface providing programmatic access to the entire Google ecosystem (Gmail, Calendar, Drive, Docs, Sheets, Slides, Meet). When paired with Claude Code, it replaces paid automation platforms like Zapier and Make.com. Five compound workflow prompts are demonstrated, from email prioritization to meeting brief generation. The only running cost is token usage.

---

## KEY TOPICS

### Google Workspace CLI (`gws`)
- Free CLI tool from Google (github.com/googleworkspace/cli)
- 101 built-in skills and recipes
- Provides programmatic access to Gmail, Calendar, Drive, Docs, Sheets, Slides, Meet
- Install: `npm install -g @google-workspace/cli`
- Zero per-zap or per-credit charges — only token costs

### Recommended Priority Order
1. **CLI** for one-off tasks
2. **Skills** for crystallized/repeated tasks
3. **MCP** only if needed

### Five Prompt Examples Demonstrated

1. **Email Prioritization** — Read last 20 Gmail messages, categorize by priority, output to color-coded Google Sheet
2. **Meeting-to-Slides** — Pull calendar events, count meetings/hours/top contacts, chain to last 30 emails by domain, produce Google Slides "Weekly Report"
3. **Needle-in-Haystack Email Search + Auto Follow-Up** — Search Gmail for "proposal/quote/invoice/contract" from last 30 days; if user sent last email >5 days ago, draft follow-up from template
4. **Meeting Brief Doc** — Find next calendar event with attendees, search Gmail for 14-day correspondence, create Google Doc with context and suggested agenda
5. **Google Drive Audit** — Search for files named "draft/old/copy/backup/V1/V2/V3/final"; output to Google Sheet "Drive Audit"

### OAuth Setup
- Kashef provides a "mega prompt" that lets Claude Code handle the full Google Cloud OAuth setup automatically via Claude and Chrome browser automation
- For business/company accounts: remove "do not pause for confirmations" line for supervised setup

---

## TOOLS & PLATFORMS MENTIONED

| Tool/Platform | Purpose |
|---------------|---------|
| Google Workspace CLI (`gws`) | Free CLI for Google ecosystem |
| Claude Code | Agentic coding environment that executes `gws` commands |
| Claude and Chrome | Browser automation for OAuth setup |
| npm | Global package install |
| Zapier / Make.com | Paid alternatives being replaced |

---

## ACTIONABLE TAKEAWAYS

1. Install `gws` globally and authenticate once — Claude Code can then orchestrate any Google service combination in a single prompt
2. Chain multiple Google services (Calendar + Gmail + Docs/Sheets/Slides) for compound workflows
3. Replace paid Zapier/Make.com automations with this free stack
4. Use Kashef's mega prompt (linked in video description) for automated OAuth credential setup

---

*Analysis derived from: Google's New CLI Just Made Claude Code Unstoppable.txt*
