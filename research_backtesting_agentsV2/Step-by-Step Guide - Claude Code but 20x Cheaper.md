# Step-by-Step Guide: Set Up MiniMax as a 20x Cheaper Claude Code Backend

**Source:** Moon Dev (YouTube)
**Video ID:** UpCHVwTgpHY
**Upload Date:** 2026-03-05

---

## What This Guide Covers

How to replace Claude Code's default Anthropic backend with MiniMax M2.5, a Chinese AI model that's 10-20x cheaper ($10/month vs $200/month). Same Claude Code CLI interface, different model. Also covers switching between MiniMax and Claude, and using MiniMax with OpenClaw.

---

## Prerequisites

- **Claude Code** installed (`npm install -g @anthropic-ai/claude-code`)
- A web browser to sign up for MiniMax

---

## Step 1: Sign Up for MiniMax Coding Plan

1. Go to **platform.minimax.io** (or search "MiniMax coding plan")
2. Sign up for an account
3. Subscribe to one of the coding plans:
   - **$10/month:** 100 prompts per 5 hours
   - **$30/month:** 300 prompts per 5 hours
   - **$100/month:** 1,000 prompts per 5 hours
4. Start with the $10 plan — you probably won't hit 100 prompts in 5 hours

---

## Step 2: Get Your MiniMax API Key

1. Log in to your MiniMax account
2. Go to **Account → API Keys**
3. Click **Create New Secret**
4. Name it something like "claude-code"
5. Copy the API key — save it securely

---

## Step 3: Configure Claude Code to Use MiniMax

1. If you've never run Claude Code, run it once and quit (`Ctrl+C` twice) to create the config directory
2. Edit `~/.claude/settings.json` (or create it if it doesn't exist)
3. Add the MiniMax configuration:

```json
{
  "apiBaseUrl": "https://api.minimax.io/anthropic",
  "apiKey": "YOUR_MINIMAX_API_KEY",
  "model": "minimax-m2.5"
}
```

4. **Important:** Clear any conflicting environment variables:
```bash
unset ANTHROPIC_API_KEY
unset CLAUDE_API_KEY
```

---

## Step 4: Verify It Works

1. Open a new terminal (important — don't reuse old session)
2. Run `claude` as normal
3. You should see MiniMax M2.5 as the active model
4. Test with a simple prompt to confirm it responds

---

## Step 5: Set Up Easy Switching Between MiniMax and Claude

1. Save your MiniMax config:
```bash
cp ~/.claude/settings.json ~/.claude/settings.minimax.json
```

2. Save your original Claude config (if you have one):
```bash
cp ~/.claude/settings.json ~/.claude/settings.claude.json
```

3. To switch to MiniMax:
```bash
cp ~/.claude/settings.minimax.json ~/.claude/settings.json
```

4. To switch back to Claude:
```bash
cp ~/.claude/settings.claude.json ~/.claude/settings.json
```

5. Always open a fresh terminal after switching

---

## Step 6: Use MiniMax with OpenClaw (Optional)

- OpenClaw requires an AI model backend — Opus is too expensive for multiple agents running 24/7
- Point OpenClaw's model configuration to MiniMax instead
- MiniMax API pricing: $0.30/M input tokens, $1.20/M output tokens (vs Opus $5/$25)
- This makes running 5+ OpenClaw agents affordable

---

## Cost Comparison

| Plan | Monthly Cost | Per M Input Tokens | Per M Output Tokens |
|------|-------------|-------------------|-------------------|
| Claude Code (Opus) | $200 | $5.00 | $25.00 |
| Claude Code (Sonnet) | $100 | $3.00 | $15.00 |
| MiniMax Coding Plan | $10 | $0.30 | $1.20 |

**Savings:** 10-20x cheaper depending on usage pattern

---

## Quality Assessment

| Aspect | Rating |
|--------|--------|
| Code generation | Between Sonnet and Opus quality |
| Speed | Comparable to Claude |
| Context handling | Good for most tasks |
| Data privacy | Data goes to Chinese servers |
| Availability | No known rate limiting issues |

---

## Important Notes

- **Data privacy:** MiniMax is a Chinese company — your code and data are sent to their servers
- **Quality trade-off:** Not quite Opus-level, but very usable for most development tasks
- **Model origin:** MiniMax M2.5 is reportedly a distillation of Anthropic's models
- **Limits:** Prompt limits reset every 5 hours, not per day
- **Best use case:** Cost-sensitive development, OpenClaw multi-agent setups, when you've hit Claude limits

*Guide derived from: 🧠 Claude Code but 20x Cheaper.txt*
