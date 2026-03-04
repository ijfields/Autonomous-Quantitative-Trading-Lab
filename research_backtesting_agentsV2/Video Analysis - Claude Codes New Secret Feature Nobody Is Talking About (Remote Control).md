# Claude Code's New Secret Feature Nobody Is Talking About (Remote Control) - Complete Transcript Analysis

**Video Title:** Claude Code's New Secret Feature Nobody Is Talking About (Remote Control)
**Channel:** Moon Dev
**Video ID:** 8kgUkgyLlbc
**Upload Date:** 2026-02-26
**Duration:** ~7m59s
**Speaker:** Moon Dev (Alex Finn)
**Platform:** YouTube

---

## EXECUTIVE SUMMARY

A quick reaction and live test of Anthropic's newly released Claude Code "Remote Control" feature, which allows developers to start a Claude Code session locally in their terminal and then continue it from their phone via the Claude app or claude.ai/code. Moon Dev tests the feature in real-time: enabling it with `/remote-control`, accessing the session from his phone, sending prompts (making a brick breaker game, voice-commanding a backtest), and testing multiple simultaneous remote sessions. He compares it favorably to OpenClaw's Telegram integration (his previous favorite feature for remote AI access) and strongly advocates Mac over Ubuntu for running agents. The video ends with a brief pitch for the Mundave Lifetime All Access offer (15 hours remaining).

No trading strategies are presented -- this is a feature review/demo.

---

## KEY TOPICS

### Claude Code Remote Control Feature
- **Command:** `/remote-control` in Claude Code CLI
- **Access:** Rolling out to Max plan users as a research preview
- **How it works:**
  1. Start a Claude Code session locally in your terminal
  2. Run `/remote-control` -- generates a shareable link
  3. Open the link on your phone via Claude app or claude.ai/code
  4. Continue the session from your phone with full access to the local environment
- **Local environments stay connected** -- MCP servers keep running
- **Voice input works** -- Moon Dev successfully used voice on his phone to command Claude
- **Multiple sessions**: Can run `/remote-control` on multiple Claude Code instances simultaneously
- **Security note:** Moon Dev wonders if anyone with the link can access the session. Confirms it's tied to the Anthropic account (must be logged in).

### Live Test Results
1. **Brick breaker game**: Prompted from phone → Claude built and launched it on local web ✓
2. **Voice backtest command**: Used voice input to ask Claude to create a new backtest from existing templates ✓
3. **Multiple remote sessions**: Successfully enabled remote control on multiple terminal instances ✓

### Comparison to OpenClaw
- Moon Dev's favorite OpenClaw feature was Telegram integration (remote agent control)
- Claude Code's remote control is "game changing" and "so much smoother"
- Strongly prefers Mac over Ubuntu/Windows for agent workflows
- Claims Ubuntu/Windows implementations are "janky" compared to Mac

### Current Limitation
- Cannot see a list of active remote sessions from the phone side
- Must save the link manually when enabling remote control

---

## TOOLS & PLATFORMS MENTIONED

| Tool | Purpose |
|------|---------|
| Claude Code | AI coding agent (CLI) |
| Claude Code Remote Control | New feature -- access local sessions from phone |
| Claude App (mobile) | Phone interface for remote control |
| claude.ai/code | Web interface for remote control |
| OpenClaw | Previous solution for remote agent access (via Telegram) |
| Mundave App | Moon Dev's custom app |

---

## ACTIONABLE TAKEAWAYS

1. **Enable with `/remote-control`** in any Claude Code session on the Max plan
2. **Sessions are account-tied** -- the link requires your Anthropic login (not publicly accessible)
3. **Voice works** -- can command Claude Code via phone voice input through the Claude app
4. **Multiple sessions supported** -- run `/remote-control` in each terminal instance
5. **No session list yet** -- save the remote control links manually; there's no dashboard to view active sessions
6. **Replaces OpenClaw's Telegram use case** for remote AI agent control

*Analyzed from: Claude Code's New Secret Feature Nobody Is Talking About (Remote Control).txt*
