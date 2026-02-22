# Step-by-Step Guide: 4 OpenClaws Are Building My Trading Bots Right Now

**Source:** Moon Dev (YouTube)
**Video ID:** TX5ViKbw0LU
**Upload Date:** 2026-02-20

## Prerequisites
- **Software:** OpenClaw TUI (two-eye interface), OpenCode Zen, Claude Code, Git/GitHub CLI, Python (with TA-Lib C library), Caffeine (keep-alive utility for Mac), Google Chrome Remote Desktop (optional for remote management)
- **Hardware:** 3-5 Mac Mini computers (M1 or newer recommended), primary workstation for oversight; speaker uses 4 Mac Minis plus his main computer for a total of 5 active machines
- **Accounts/API Keys:** GitHub account (one primary + one secondary "fork" account), OpenRouter API key ($200+ budget), MiniMax direct API key, Kimmy 2.5 (via OpenCode Zen), GLM 4.7 (via OpenCode Zen), Hyperliquid data layer node access, Google Drive (for shared notes/keys)
- **Knowledge:** Basic Git workflow (branching, PRs, forks), Python scripting, familiarity with OpenClaw agent platform, understanding of the RBI (Research/Backtest/Implement) system from Alex Finn's roadmap
- **Files/Data:** Access to the `mundave-ai-agents` GitHub repository (specifically the `RBI_agent_PP_multi` script and its `ideas.txt`), OpenRouter ENV key, GitHub personal access token (classic)

---

## Part 1: Multi-Agent GitHub Infrastructure Setup

### Step 1: Plan the Fork-Based GitHub Architecture
Alex Finn has 5 OpenClaw agents running on 5 separate Mac Mini computers. Rather than creating 5 separate GitHub accounts (which would require 5 separate email addresses), he adopts a **fork model** where one secondary GitHub account ("Cracker") forks the main repositories, and all agents push to branches within that fork.

- **Main GitHub (Mundave on YT):** Sacred, protected -- no agent ever pushes directly here
- **Secondary GitHub (Cracker):** Forks the main repos; all 4 agents work within this fork using branch prefixes
- Each agent gets a unique branch prefix (e.g., `agent-mash/`, `agent-killer/`, `agent-cash/`)
- PRs flow from Cracker's fork back to the main repo for review

> Speaker's tip: "One account, one fork. Zero new emails. Branches are cheap and unlimited. Agents can't collide if they stick to their prefix."

### Step 2: Generate a GitHub Personal Access Token (Classic)
Navigate to GitHub Settings > Developer Settings > Personal Access Tokens > Classic. Create a token with `repo`, `workflow`, and `read` scopes.

- Set expiration to "No expiration" for persistent agent access
- This single classic token will be shared across all agent machines
- Store it securely in Google Drive or a shared notes document for easy distribution
- Expected result: A token string you can copy to each machine

> Speaker's tip: "I'm going to give it to four. I'll have four cooking on this. I want to keep one of them freshy fresh."

### Step 3: Distribute the GitHub Token to Each Agent Machine
Physically or remotely access each Mac Mini running OpenClaw and provide the GitHub token. Alex Finn uses Google Drive as an intermediary since he cannot copy/paste directly between separate physical computers.

- Log into each machine's OpenClaw TUI
- Provide the token via typed input or Google Drive document
- Have each agent authenticate with GitHub: `gh auth login` or store the token in git config
- Expected result: Each agent confirms GitHub access

> Speaker's tip: "I can't copy from here to there, but I can copy from here to there. So I just write it one time in Google Drive and then send it over."

### Step 4: Establish Agent Rules and Identities
Send each agent a set of golden rules along with their unique identity. Alex Finn had Cracker (the lead agent) produce the final ruleset:

- **Agent Identity:** Each agent has a name (Mash, Killer, Cash) and a branch prefix
- **Golden Rules:**
  1. Never push to Mundave's main repo directly
  2. Never touch another agent's branches
  3. Never commit `.env` files or secrets
  4. Never force push
  5. PRs go to Cracker for review
  6. If stuck for 30 minutes, flag early
  7. If something breaks, create a fresh branch

- Have each agent confirm understanding by echoing back their name and rules
- Expected result: Each agent responds with "Rules locked. My name is [X]. Agent prefix is agent-[X]."

> Speaker's tip: "Please confirm you stored this and what your name is, and you will follow this process for GitHub."

### Step 5: Designate Agent Roles and Hierarchy
Alex Finn establishes a hierarchy: Cracker is the lead agent (hosted on machine "Slim"), and the other three (Mash, Killer, Cash) report to Cracker. A fourth machine (Gal) is kept on the bench as a reserve.

- Cracker has direct access to the main GitHub and controls the fork
- Sub-agents work within Cracker's fork using their prefixed branches
- All code must flow: Sub-agent branch > Cracker fork PR > Main repo
- Expected result: A clear chain of command for code contributions

---

## Part 2: Stream Observer Agent Configuration

### Step 6: Configure the Stream Observer (Whisper-Based Idea Generator)
On one machine (Slim/Cracker), Alex Finn runs a background Python script that uses internal Whisper to transcribe his live speech and then sends transcripts to MiniMax 2.5 for analysis.

- The script extracts the last 7 minutes of audio (previously 15 minutes, reduced for faster iteration)
- Whisper transcribes locally, then sends to OpenRouter with MiniMax M2.5
- The prompt instructs the model to: "Find the top two biggest opportunities from your live stream. Think 10M to 100M. Think 100x bigger than your first instinct and go bigger."
- Responses are parsed and written to CSV/MD files
- Run using: `python run_it.py` (or similar launcher in the TFlow environment)
- Expected result: Every 7 minutes, a new set of 2 ambitious idea summaries appear in the output files

> Speaker's tip: "If I have somebody that's always listening to me 24/7 and dissecting every 15 minutes, like what's the most fire thing that we could do to run it up to a billion?"

### Step 7: Remove Unnecessary Dashboard Tabs
The Stream Observer dashboard had a "current activity" tab that was producing confusing or off-topic results. Alex Finn asks the agent to remove it and focus on the core idea pipeline.

- Remove the current activity tab from the stream observer dashboard
- Confirm the transcript extraction pipeline is working correctly
- Verify the prompt at line 68 of the script matches your intended scope
- Expected result: Cleaner dashboard output focused on actionable ideas

---

## Part 3: Model Selection and OpenCode Configuration

### Step 8: Test and Compare LLM Models Across Agents
Alex Finn tests three models across his four agents to compare speed and quality:

1. **MiniMax M2.5 (Direct API):** Fastest, cleanest results. Connected directly to MiniMax API, not through OpenCode Zen. This is the recommended approach.
2. **Kimmy 2.5 (via OpenCode Zen):** Slower but functional. Eventually declared the winner for quality on the RBI dashboard task.
3. **GLM 4.7 (via OpenCode Zen):** Works through OpenCode but had long idle periods (6-7 minutes between responses).

- Key finding: MiniMax 2.5 through OpenCode Zen did NOT work -- only MiniMax M2.5 through direct API connection worked. The model name `minimax-2.5` failed but `minimax/MiniMax-M2.5` succeeded.
- Configuration: Update OpenClaw config TOML to specify the correct provider and model identifier
- If switching models, restart the OpenClaw daemon (gateway restart)
- Expected result: Each agent running on its assigned model and producing output

> Speaker's tip: "Miniax 2.5 direct so far has been a very clean experience... it's better to connect directly to Miniax than use Open Code."

### Step 9: Troubleshoot API Key and Model Errors
Common issues encountered during the stream:

- **"Invalid API key":** Verify the last 6 digits match what you expect. The key may be correct but the model name format is wrong.
- **"Can't recognize that model":** Case and spelling matter. `minimax-2.5` vs `MiniMax-M2.5` are different identifiers.
- **Unauthorized errors:** May indicate the wrong authorization header format (Bearer vs X-API-Key header).
- **Daemon restart:** Sometimes required after config changes: `openclaw daemon restart`

> Speaker's tip: "So she just had the spelling off. Case matters. Let me fix it."

---

## Part 4: Deploying the RBI Multi-Agent Backtesting System

### Step 10: Populate Ideas and Launch the RBI Agent
The RBI (Research/Backtest/Implement) system uses a multi-threaded Python script (`RBI_agent_PP_multi`) that reads trading strategy ideas from `ideas.txt` and runs parallel backtests.

- Navigate to the `mundave-ai-agents` GitHub repository on each agent
- Locate `RBI_agent_PP_multi/ideas.txt`
- Have each agent populate 10 trading strategy ideas (Jim Simons-caliber concepts)
- Set the OpenRouter key in the `.env` file
- Configure the model to use MiniMax 2.5 through OpenRouter
- Launch: `python RBI_agent_PP_multi.py`
- Expected result: 10 parallel threads begin researching and backtesting strategies

> Speaker's tip: "I want you to come up with 10 ideas of trading strategies and put them on that corresponding txt that feeds the RBI agent PP. And then change the model to use the open router mini max 2.5 and then run the RBI agent."

### Step 11: Build a Real-Time RBI Dashboard
Each agent is tasked with building a live dashboard to visualize the RBI process in real-time:

- Dashboard requirements:
  - Fun, colorful design (inspired by Pump.fun -- "slot machine type fun" but with real data)
  - Live activity feed showing what each backtest thread is working on
  - Hall of Fame section for completed backtests
  - No purple color
  - No oversized header -- only actionable data on screen
  - Auto-refill mechanism so the system never runs out of ideas
- Each agent builds their own version using their assigned model
- Expected result: A locally-hosted dashboard (localhost) with flashing updates, thread status, and completed backtest results

> Speaker's tip: "I want it visually fun as [expletive] and I want real data that is useful coming through. Don't hold back on design."

### Step 12: Enable Autonomous Idea Refilling
The RBI system stops when it runs out of ideas. Alex Finn asks each agent to build an auto-refill mechanism:

- When `ideas.txt` runs low, the agent should autonomously generate new trading strategy ideas
- Use a cron job or autonomous loop to keep the pipeline running indefinitely
- The system should never show "waiting for idea" -- it should always be processing
- Expected result: Fully autonomous backtesting that runs 24/7 without manual intervention

> Speaker's tip: "System is fully autonomous now. She's going to keep running. Beautiful."

---

## Part 5: API Monitoring and User Support

### Step 13: Monitor and Debug the Hyperliquid Data Layer API
Alex Finn runs a monitoring system that checks all 55 API endpoints continuously. When a user (Adam) reports 403 errors, he uses Cracker to diagnose:

- Two issues found:
  1. **Authorization header format:** The API only accepts `X-API-Key` header, not `Authorization: Bearer` format
  2. **Tier access:** Bulk Binance liquidation downloads require Quant Elite access (key ending in `_QE`)
- Self-healing mechanisms are in place for transient failures
- Use the monitoring dashboard to verify endpoint health before escalating

> Speaker's tip: "She says the key is valid, but there's two distinct issues... The API only accepts X-API header. Authorization bearer is not supported."

---

## Common Pitfalls
- **Model name spelling/casing:** MiniMax models have very specific identifier formats. `minimax-2.5` may fail where `MiniMax-M2.5` succeeds. Always verify the exact model string.
- **OpenCode Zen vs Direct API:** Not all models work through OpenCode Zen's routing. MiniMax 2.5 only worked via direct API connection during this stream.
- **Agent collisions on GitHub:** Without branch prefix discipline, agents will overwrite each other's work. Enforce the `agent-[name]/` prefix convention strictly.
- **Copy-paste across machines:** You cannot copy/paste between separate physical Mac Minis. Use Google Drive, shared Notion docs, or another intermediary.
- **TA-Lib C library:** The RBI backtesting scripts require TA-Lib, which needs the C library installed first. On Mac: `brew install ta-lib` before `pip install TA-Lib`.
- **Free model rate limits:** Free-tier models (MiniMax free) will hit rate limits quickly with parallel agents. Budget for paid API access.
- **Forgot to restart daemon:** After changing models in OpenClaw config, a daemon restart may be required. The gateway restart command was needed intermittently.

---

## Resources Mentioned
- **mundave.com** -- Main site for private Zoom access ($5/day), API keys, and the Mundave app
- **mundave.com/docs** -- API documentation for the Hyperliquid data layer (55+ endpoints)
- **mundave.com/roadmap** -- Algo trading roadmap with RBI system explanation
- **mundave.com/go** -- Lifetime all-access offer ($1,500 one-time payment)
- **OpenClaw TUI** -- Terminal-based AI agent interface (preferred over the older chat interface)
- **OpenCode Zen** -- Multi-model router supporting Kimmy 2.5, GLM 4.7, and others
- **MiniMax M2.5** -- Chinese open-source LLM, connected via direct API for best results
- **Kimmy 2.5** -- Alternative LLM accessed through OpenCode Zen
- **GLM 4.7** -- Alternative LLM accessed through OpenCode Zen
- **models.dev** -- Comprehensive open-source database of LLM model identifiers
- **Hyperliquid** -- Decentralized exchange with transparent liquidation data; HLP market maker vault at $118M
- **CoinGlass** -- Liquidation data provider ($8,388/year for 12 days of data vs. Alex Finn's 18+ months)
- **Notion** -- Used for toggle-list-based project management and roadmap organization
- **Google Drive** -- Used as intermediary for sharing keys/configs across physical machines
- **Pump.fun** -- Referenced as design inspiration for making trading dashboards fun and engaging

---

## Summary
This ~3h47m live stream documents Alex Finn's process of setting up a multi-agent AI infrastructure for autonomous trading bot development. He configures 4 OpenClaw agents across 4 separate Mac Mini computers, establishes a fork-based GitHub workflow so agents can collaborate without stepping on each other's code, tests three different LLM models (MiniMax M2.5, Kimmy 2.5, GLM 4.7) for speed and quality, and deploys his RBI (Research/Backtest/Implement) multi-agent backtesting system on each machine. The session includes extensive troubleshooting of API keys and model configurations, building real-time dashboards to monitor backtesting progress, and configuring a Stream Observer agent that uses Whisper to transcribe his speech and generate ambitious trading strategy ideas every 7 minutes. The key takeaway is that MiniMax 2.5 via direct API outperformed other models in speed and quality, while the fork-based GitHub model with agent branch prefixes provides a scalable collaboration pattern for 5 to 500 autonomous agents.

*Extracted from: 4 OpenClaws Are Building My Trading Bots Right Now.txt*
