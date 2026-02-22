# 4 OpenClaws Are Building My Trading Bots Right Now - Complete Transcript Analysis

**Stream Title:** 4 OpenClaws Are Building My Trading Bots Right Now
**Date:** Estimated February 2026 (post-Feb 18 based on context; references Feb 17 API key date, references previous OpenClaw setup sessions)
**Duration:** ~3h47m (00:00:00 to 03:47:23)
**Speaker:** Moon Dev
**Channel:** Moon Dev
**Video ID:** TX5ViKbw0LU
**Upload Date:** 2026-02-20
**Platform:** YouTube (public stream with private Zoom companion at mundave.com)

---

## EXECUTIVE SUMMARY

This nearly four-hour live stream captures Moon Dev building out a multi-agent AI infrastructure for autonomous trading bot development in real time. The session begins with distributing daily API keys to private Zoom members, then pivots to the core task: configuring 4 OpenClaw agents running on 4 separate Mac Mini computers (named Cracker/Slim, Mash, Killer, and Cash, with a fifth machine "Gal" kept in reserve) to collaborate on a shared GitHub repository using a fork-based workflow. The stream documents the full process of generating GitHub tokens, distributing them across machines, establishing agent identity and rules, and deploying the RBI (Research/Backtest/Implement) multi-agent backtesting system.

A significant portion of the stream involves testing and comparing three LLM models -- MiniMax M2.5 (direct API), Kimmy 2.5 (via OpenCode Zen), and GLM 4.7 (via OpenCode Zen) -- revealing that MiniMax direct is fastest and most reliable but that Kimmy ultimately produces the best dashboard output. The session also includes debugging a user's Hyperliquid API errors, a tangential but spirited discussion about running for US president using AI agents, and multiple promotional segments for the lifetime all-access offer. The stream represents a milestone in Moon Dev's journey from single-machine development to coordinated multi-machine autonomous agent operation.

---

## TIMESTAMPED SEGMENTS WITH DESCRIPTIONS

### 00:00 - 00:05 | Opening & Daily Motivation
**Focus:** Stream kickoff with energy and daily routine philosophy
- Moon Dev opens with his signature motivational energy: "Build, baby, build. Learn, baby, learn so we can earn, baby, earn."
- References MLK Jr. as inspiration for continuous learning
- States he has five OpenClaws set up and wants to start assigning them tasks
- Mentions the GitHub setup as first priority, API key distribution as zeroth priority
- Confirms he is running Claude 4.6 (Opus)
- **Key quote:** "I've got five open claws here and I want to start assigning them some tasks because we're set up with the infrastructure."

### 00:05 - 00:10 | API Key Distribution & Membership Updates
**Focus:** Distributing daily Hyperliquid data layer API key and updating mundave.com
- SSHs into his Hyperliquid node to generate a new daily API key
- Explains the API key gives access to: Mundave app (positions viewer), Code tab, full data layer documentation
- Updates mundave.com page: changes masterclass duration from 45 minutes to 3 hours, removes "instant access" verbiage, renames "Quant App Beta" to "Mundave App"
- Emphasizes 24-hour key access, 90-day money-back guarantee, $5 daily entry
- Confirms removal of replays for daily members (lifetime members still get them)
- **Key quote:** "Each day I do update the key because this is an institutional grade key, something that is not going to be cheap, but I wanted to reward you for actually showing up."

### 00:10 - 00:20 | Hyperliquid Data Layer Deep Dive & Trading Philosophy
**Focus:** Explaining the value proposition of the Hyperliquid data layer API
- Demonstrates the API capabilities: liquidation levels across Binance/OKX/Hyperliquid, HLP (Hyperliquid market maker at $118M) position tracking, trader win/loss analysis, trade history for any address
- Explains his trading philosophy: trading around liquidations rather than predicting price
- Reports ~49% return over the past week using $10K max position size with 40x leverage through the Quant app
- States 99% of his 150K+ followers still trade by hand with 40x leverage -- the problem he is trying to solve
- Reveals he was recently hacked due to showing sensitive information on screen, leading to the private Zoom model
- API includes 55 endpoints with continuous monitoring, tick data for all tokens, smart money calls
- Compares his data to CoinGlass ($8,388/year for only 12 days of data) vs. his 18+ months included
- **Key quote:** "Nobody can predict price. And if you think you can, you're probably going to get smoked... instead of predicting price, I'm predicting which liquidation to buy."

### 00:20 - 00:27 | Stream Observer Agent & Whisper Transcription Setup
**Focus:** Configuring the background AI listener that transcribes and analyzes his speech
- Launches a Python script on one machine that runs continuously during the stream
- Uses internal Whisper for local transcription, then sends to OpenRouter with MiniMax M2.5
- Every 15 minutes (later reduced to 7), it extracts audio, transcribes, and generates the top 2 "biggest opportunities" discussed
- Prompt instructs: "Think 100x bigger than your first instinct. Go bigger." Targets $100M minimum use cases
- Reviews early output: "Autonomous liquidation arbitrage engine" and "Institutional smart money mirror platform" -- acknowledges they seem off-topic due to the inflated prompt
- Removes the "current activity" tab from the Stream Observer dashboard to reduce noise
- **Key quote:** "If I have somebody that's always listening to me 24/7 and dissecting every 15 minutes, like what's the most fire thing that we could do to run it up to a billion?"

### 00:27 - 00:36 | GitHub Architecture Planning (Fork Model)
**Focus:** Designing a multi-agent GitHub collaboration workflow
- Core challenge: 5 agents on 5 machines need to collaborate on shared repos without stepping on each other
- Considers options: separate GitHub accounts per agent (rejected -- too many emails), shared single account with branch prefixes (adopted)
- Settles on fork model: Cracker's GitHub forks Mundave's main repos; all agents push to Cracker's fork using their own branch prefixes
- Agent names established: Cracker (lead, on Slim), Mash, Killer, Cash; Gal benched
- Golden rules defined: never push to main, never touch another agent's branches, never commit secrets, never force push, PRs go to Cracker for review, flag blockers after 30 minutes
- Compares to how open-source projects work with hundreds of contributors
- **Key quote:** "One account, one fork. Zero new emails. Branches are cheap and unlimited. Agents can't collide if they stick to their prefix."

### 00:36 - 00:44 | Tangent: Presidential Campaign Discussion
**Focus:** Moon Dev asks Claude to draft a multi-cycle presidential campaign plan
- Discusses his qualifications: US-born, 36 years old, meets constitutional requirements
- Asks Claude to produce an actionable plan spanning 2028 (age 38) through 2040 (age 50)
- Plans to assign one OpenClaw agent to work on this campaign indefinitely
- Phases outlined: foundation/identity/platform, digital presence, exploratory committee, FEC registration
- Returns focus to the GitHub setup after the tangent
- **Key quote:** "I just hate the state of America right now... give me a plan that I'll send to this AI that has full access to a computer and can work on this for the next 50 years if needed."

### 00:44 - 01:00 | GitHub Token Generation & Distribution
**Focus:** Creating and distributing the GitHub personal access token across machines
- Navigates to GitHub Developer Settings on Cracker's account
- Creates a classic personal access token with repo, workflow, and read scopes; no expiration
- Names the token and begins distributing to all machines
- Notes the challenge of working across separate physical computers (no shared clipboard)
- Uses Google Drive as an intermediary for sharing keys between machines
- Discovers some existing repos on Cracker's GitHub: mundave-ai-agents, mundave-social-arbitrage, mundave-liquidation-trading-boss, mundave-ai-sdk
- Reserves Gal (5th machine) on the bench; distributes to Cracker, Mash, Killer, and Cash
- **Key quote:** "So gal is not going to be touched. Not going to be touched. We're going to cook these three here."

### 01:00 - 01:20 | Agent Authentication & OpenClaw TUI Setup
**Focus:** Getting each agent machine authenticated and running OpenClaw TUI
- Launches OpenClaw TUI on each machine: `openclaw tui`
- Encounters issues: Killer's API key shows invalid, one machine running MiniMax 2.1 instead of 2.5
- Discovers model name spelling/casing matters: `minimax-2.5` fails but correct model identifier works
- Updates each machine's OpenClaw config to use the correct model
- Mash is on Kimmy 2.5, Killer initially fails on MiniMax 2.5, Cash set up on free tier initially
- Sends GitHub token to each agent, confirms Cracker as the lead with direct access to main GitHub
- Has Cracker review and finalize the agent rules before distributing to sub-agents
- **Key quote:** "She just had the spelling off. Case matters. Let me fix it."

### 01:20 - 01:40 | Agent Identity Confirmation & Model Selection Discussion
**Focus:** Confirming each agent understands their rules and debating LLM model choice
- Each agent confirms receipt of rules and their identity:
  - Mash: "Rules locked. Prefix is agent-mash. Never touch main. Never force push."
  - Cash: "My name is Cash. Branch prefix agent-cash. PRs go to you."
  - Killer: "My name is Killer. Agent killer. Reporting for duty."
- Chat discussion on model selection: MiniMax M2.5 vs Kimmy 2.5 vs GLM 4.7
- Kenny from chat recommends Kimmy; others suggest GLM is strong
- Moon Dev decides to test multiple: two on Kimmy 2.5, two on different models
- MiniMax 2.5 through OpenCode Zen consistently fails; works only through direct API
- Discusses why paying for API models is better than running local (3x speed advantage, VC-subsidized pricing)
- **Key quote:** "M2.5, Kimmy 2.5, or GLM 4.7. So maybe what I'll do is I'll just test them."

### 01:40 - 01:52 | Debugging MiniMax 2.5 & Cross-Machine Config
**Focus:** Troubleshooting why MiniMax 2.5 works on one machine but not others
- Moon Dev identifies the discrepancy: Slim/Cracker has MiniMax 2.5 working via direct API, while other machines fail through OpenCode Zen
- Asks Cracker to produce step-by-step instructions for how her MiniMax connection is configured
- Verifies API key by comparing last 6 digits across machines -- keys match
- Discovers the issue is the routing path: direct MiniMax API vs OpenCode Zen routing
- Tries switching models: GLM 4.7 works through OpenCode, Kimmy 2.5 works through OpenCode, but MiniMax 2.5 only works direct
- Chat member Art provides guidance on MiniMax model naming conventions
- **Key quote:** "So, confirmed. Miniax 2.5 through open code just doesn't work. Miniax direct is the only way."

### 01:52 - 02:00 | Break & Market Check
**Focus:** Mid-stream break with market commentary
- Announces a 5-7 minute bathroom break after confirming all 4 agents are set up on GitHub
- Quick check on BTC 5-minute chart; notes high volatility
- Amazon up 2%; comments "So hard to hand trade"
- Conducts a "throw a 1 in the chat if you're still active" check -- confirms ~15 active viewers
- Returns from break ready to deploy the RBI system
- **Key quote:** "We are all set up on GitHub across four different open claws. Now, now they can cook all day."

### 02:00 - 02:15 | RBI System Introduction & Deployment
**Focus:** Setting up the RBI multi-agent backtesting pipeline on each machine
- Explains the RBI system: Research, Backtest, Implement -- available on mundave.com/roadmap
- Plans to set up both the R and B phases on all four machines
- Distributes the OpenRouter API key ($200 budget) to each agent
- Instructs Cracker to: populate 10 trading strategy ideas in `ideas.txt`, configure MiniMax 2.5 through OpenRouter, then launch `RBI_agent_PP_multi`
- Cracker produces a poem about the process: "We don't just trade, we print money. Research, backtest, validate, implement, execute, profit, accumulate."
- Instructs each subsequent agent (Mash, Killer, Cash) to clone the repo, store the OpenRouter key in `.env`, and prepare to run the RBI agent
- **Key quote:** "I want you to come up with 10 ideas of trading strategies and put them on that corresponding txt that feeds the RBI agent PP."

### 02:15 - 02:30 | Dashboard Building (Cracker/Slim)
**Focus:** Building a real-time dashboard to visualize the RBI backtesting process
- Cracker (MiniMax 2.5 direct) starts building a dashboard alongside running the RBI agent
- Requirements: fun design, real-time data, flashing updates when threads complete, purple prohibited
- Dashboard initially crashes ("Dash refuses connection") but is rebuilt
- Instructs: "Build some sort of cron or autonomous thing to keep going all day" so ideas auto-refill
- Notes Cracker figured out auto-refill for `ideas.txt` -- "she's going to auto refill that ideas.txt"
- References Notion toggle lists as his preferred organizational tool; expresses love for returning to Notion
- Parallel deployment: sends same dashboard prompt to Mash (Kimmy 2.5) and Killer (GLM 4.7)
- **Key quote:** "Make it feel fun like a slot machine. But no goofy stuff. Just fire updates of what they are doing."

### 02:30 - 02:45 | API Debugging for User (Adam) & Data Layer Pricing
**Focus:** Diagnosing a user's Hyperliquid API errors using Cracker
- Chat member Adam reports 403 Forbidden errors on three API endpoints
- Moon Dev uses Cracker to test all endpoints with the user's API key
- Findings: (1) API only accepts X-API-Key header format, not Authorization Bearer; (2) bulk Binance liquidation download requires Quant Elite tier access
- Demonstrates the self-healing monitoring system catching transient failures
- Compares CoinGlass pricing: $8,388/year for 12 days of 1-minute liquidation data vs. his 18+ months included with Quant Elite
- Transitions into the lifetime offer pitch, detailing the $48,000 stated value: algo trade camp, AI masterclasses, Solana copybot course, Polymarket bots, Quantite (300+ backtests), Mundave Vault, API key for life, 2 GitHubs with 20+ AI agents
- **Key quote:** "12 days of data. I got 18 months plus that you get at mundave.com/docs."

### 02:45 - 03:05 | Lifetime Offer Pitch & Personal Story
**Focus:** Extended promotion of the $1,500 lifetime all-access offer with origin story
- Details the offer at mundave.com/go: one-time $1,500 payment (or 3-payment plan), 90-day money-back guarantee
- Shares his origin story: met an algo trader doing $1B/day in volume while apartment hunting; the trader was casually smoking on the couch with his computer running bots
- Discusses his journey from getting liquidated on leverage to learning to code to 5 years of algo trading
- Emphasizes code as a "great equalizer" -- worst case you learn a valuable skill
- Reveals he spent $2K on an app-building course in college, burned $15K on a first app that failed, then ran up millions
- Compares running local AI models ($40/month savings) vs API models (3x faster): "I value my time at $1,000 an hour"
- States he shares everything in private Zoom and distills it into courses for the lifetime package
- **Key quote:** "I was like, oh snap... he's like, 'Oh, I'm an algo trader. I do a billion dollars a day in volume.' And this was the same time where I was trading with leverage just getting liquidated."

### 03:05 - 03:15 | RBI Dashboard Comparison Across Models
**Focus:** Comparing the three model outputs side-by-side
- Returns to check on all three agents' dashboard builds:
  - **MiniMax 2.5 (Cracker/Slim):** Fastest, cleanest. Auto-refill working. Live activity feed running. "Miniax 2.5 direct so far has been a very clean experience."
  - **Kimmy 2.5 (Mash):** Slow (47 minutes idle at one point due to GitHub clone credential failure), but when working, produces the best-looking dashboard with "shaky" animations
  - **GLM 4.7 (Killer):** Functional but had 6-7 minute idle gaps. Produced a workable RBI dashboard after delays.
- Mash (Kimmy 2.5) had the prettiest output but was slowest
- MiniMax wins on speed; Kimmy eventually declared winner for quality/aesthetics
- All three have "Hall of Fame" sections for completed backtests
- **Key quote:** "Top left -- that's Miniax direct. Top right -- Kimmy. And down here, GLM stuck like a scaredy pants."

### 03:15 - 03:30 | Kimmy Wins & Dashboard Refinement
**Focus:** Iterating on dashboard design and declaring model preferences
- Moon Dev reverses his initial MiniMax preference: "Kimmy for the win. Kimmy for the win, baby."
- Reasons: Kimmy's dashboard has real-time agent logs, better visual design, and proper status tracking
- Requests refinements: remove all purple, add a fun output log on the left sidebar, replace generic "18 parallel" text with live cards showing what each thread is processing
- Notes that having separate physical computers means no resource competition between agents
- Instructs agents to contain their code within the agents section of the AI agents GitHub, using their own folders (matching what Cracker and Killer did)
- Reflects on the novelty of working with 3-4 computers simultaneously: "Have you ever seen this before? I haven't. I've never used three different computers at the same time."
- **Key quote:** "Having multiple computers, dude. This is really, really interesting workflow that I've never had in my entire life. Nobody's had this."

### 03:30 - 03:40 | Autonomous Operation & Final Tinkering
**Focus:** Achieving fully autonomous RBI operation
- Confirms: "System is fully autonomous now. She's going to keep running."
- One agent has auto-refill working -- new ideas are generated and fed into the pipeline without manual intervention
- Encounters TA-Lib C library dependency issue on one machine
- Handles chat requests about custom TradingView indicators in Python backtests (yes, covered in Algo Trade Camp, Pine Script to Python conversion)
- Models.dev mentioned by chat as a comprehensive open-source database of LLM model identifiers
- Requests dashboard improvements: more color, better visibility of what agents are actively processing
- Notes completed backtests are starting to appear in the Hall of Fame sections
- **Key quote:** "She has access to one of the most powerful GitHubs when it comes to AI agents in the entire world."

### 03:40 - 03:47 | Closing & Sign-Off
**Focus:** Wrapping up the stream with final reflections
- Acknowledges going approximately one hour over planned time
- Plans to continue tinkering offline but cuts the public stream
- Announces he will likely be back tomorrow morning (wakes at 4:30-5:00 AM, starts around 9:10 AM)
- Final promotion: mundave.com/go for lifetime access
- Encourages checking emails, Discords, and Twitters
- Signs off with signature: "777. I believe in you. Get it, dude. Get it."
- **Key quote:** "I'm going try to keep it at three hours... I'll probably go to bed about 8:30 and wake up about 4:30, 5, and be kind of itching to get here."

---

## COMPREHENSIVE SUMMARY - 25 KEY BULLET POINTS

1. **Multi-machine agent architecture:** Moon Dev successfully configured 4 OpenClaw agents on 4 separate Mac Mini computers (Cracker/Slim, Mash, Killer, Cash) with a 5th (Gal) kept in reserve, establishing what he calls a groundbreaking workflow of managing multiple AI-equipped computers simultaneously.

2. **Fork-based GitHub collaboration:** Adopted an open-source-style fork model where Cracker's GitHub account forks the main repos, all agents push to prefixed branches within the fork, and PRs flow upstream -- avoiding the need for 5 separate email accounts and GitHub registrations.

3. **Agent identity and golden rules:** Each agent received a unique name, branch prefix, and a set of 7 golden rules (never push to main, never touch others' branches, never commit secrets, never force push, PRs to Cracker, flag blockers at 30 min, fresh branch on breaks). Each confirmed understanding before receiving tasks.

4. **Stream Observer agent:** A Whisper-based Python script runs continuously, transcribing the last 7 minutes of audio and sending it to MiniMax M2.5 to identify the "top two biggest opportunities" with a prompt that demands "Think 100x bigger." Results are written to CSV/MD files.

5. **MiniMax M2.5 direct API superiority:** Through extensive testing, MiniMax M2.5 connected via direct API was found to be fastest and most reliable. The same model through OpenCode Zen's routing layer consistently failed, making direct connection the recommended approach.

6. **Kimmy 2.5 quality winner:** Despite being slower, Kimmy 2.5 (via OpenCode Zen) produced the best-quality dashboard output with real-time agent logs, better visual design, and proper status tracking. Moon Dev ultimately declared "Kimmy for the win."

7. **GLM 4.7 as a functional middle ground:** GLM 4.7 worked through OpenCode Zen but had 6-7 minute idle gaps between responses. It produced workable output but was neither the fastest nor the highest quality.

8. **RBI multi-agent backtesting deployment:** The RBI (Research/Backtest/Implement) system was deployed across all 4 machines, each running 10+ parallel threads that research and backtest trading strategies autonomously using ideas from `ideas.txt`.

9. **Real-time dashboard construction:** Each agent built its own real-time dashboard to visualize the RBI process -- showing active threads, ideas being tested, completed backtests in a "Hall of Fame," and live activity feeds. Design requirements: fun/colorful (Pump.fun-inspired), no purple, actionable data only.

10. **Autonomous idea refilling:** Moon Dev achieved a key milestone: agents can autonomously generate new trading strategy ideas when `ideas.txt` runs low, enabling 24/7 operation without manual intervention.

11. **Hyperliquid data layer API value:** The custom-built Hyperliquid node provides tick data for all tokens, liquidation levels across exchanges, HLP market maker position tracking, and trader win/loss analysis -- valued at $1,000+/month and compared favorably to CoinGlass ($8,388/year for only 12 days of data).

12. **Trading philosophy (liquidation-based):** Rather than predicting price, Moon Dev's approach predicts which liquidation events to trade around, using Hyperliquid's transparent on-chain data. Reports ~49% weekly return using 40x leverage with the Quant app's built-in risk controls.

13. **API debugging in real-time:** When user Adam reported 403 errors, Moon Dev used Cracker to diagnose two issues: wrong authorization header format (Bearer vs X-API-Key) and tier-gated endpoint access for bulk liquidation data.

14. **Cross-machine key distribution workflow:** Since separate physical Mac Minis have no shared clipboard, Moon Dev uses Google Drive as an intermediary to share API keys, GitHub tokens, and configuration snippets between machines.

15. **OpenClaw TUI preference:** Moon Dev strongly prefers the TUI (terminal user interface) version of OpenClaw over the older chat interface, calling the previous version "embarrassing" and "whack."

16. **Cost framework for AI agents:** Each machine requires: OpenRouter API budget (~$200), MiniMax direct API key, OpenCode Zen subscription, and ongoing compute costs. Moon Dev argues that paying for API-based AI is always better than running local models because VC-subsidized pricing gives 3x speed advantage.

17. **Security concerns and private Zoom model:** After being hacked due to showing sensitive information on a public YouTube stream, Moon Dev moved to a model where YouTube gets a screen-blocked view while private Zoom members ($5/day) see full code and get daily API keys.

18. **Model naming gotcha:** A critical debugging lesson -- LLM model identifiers are case-sensitive and format-specific. `minimax-2.5` fails where `MiniMax-M2.5` succeeds. The exact model string must match the provider's specification.

19. **Chat community dynamics:** Moon Dev describes the "dichotomy of the chat" -- half the messages are fire engineering insights from advanced developers spotting optimization opportunities in real-time, while the other half are basic customer support questions. He values both but notes the whiplash.

20. **Presidential campaign tangent:** In a characteristic aside, Moon Dev asks Claude to draft a multi-cycle presidential campaign plan (2028-2040), expressing intent to assign an OpenClaw agent to work on it indefinitely. While not a trading topic, it demonstrates his "think 100x bigger" philosophy.

21. **Origin story as motivation:** Moon Dev recounts meeting an algo trader doing $1B/day in volume while apartment hunting, inspiring his pivot from hand trading to coding. He spent $2K on an app course in college, built and failed a $15K app, then built a successful app business before transitioning to algo trading.

22. **TA-Lib dependency issue:** One machine failed to install dependencies because TA-Lib's Python package requires the C library to be pre-installed -- a common pitfall for backtesting environments on new machines.

23. **Notion toggle lists:** Moon Dev returned to Notion for project management after a stint with a custom solution, declaring toggle lists "the killer application" for organizing nested information.

24. **Scaling vision (5 to 500):** The current 4-agent setup is explicitly designed as a proof-of-concept for scaling to 500 machines. Moon Dev notes: "I'm glad I didn't do 500 right away" -- the repetitive setup process for even 4 machines revealed workflow bottlenecks.

25. **Lifetime offer economics:** The $1,500 one-time offer includes Algo Trade Camp, AI masterclasses, Solana/Polymarket bot courses, Quantite (300+ backtests, $300/month value), 2 GitHubs with 100+ backtests and 20+ AI agents, Mundave Vault (removed YouTube videos), and lifetime API access -- positioned as 5 years of knowledge distilled for the price of "what you'd lose in one bad trading day."

---

## TOOLS & TECHNOLOGIES USED

### AI/LLM Platforms
- **OpenClaw TUI** -- Terminal-based AI agent platform for autonomous computer operation; each Mac Mini runs an instance
- **OpenCode Zen** -- Multi-model LLM router supporting Kimmy 2.5, GLM 4.7, and others; preferred for flexibility
- **MiniMax M2.5 (Direct API)** -- Chinese open-source LLM; fastest and cleanest for backtesting tasks when connected directly
- **Kimmy 2.5 (via OpenCode)** -- Alternative LLM; slower but best dashboard quality output
- **GLM 4.7 (via OpenCode)** -- Alternative LLM; functional but with idle-gap issues
- **Claude 4.6 (Opus)** -- Used on Moon Dev's primary workstation for planning and architecture decisions
- **Whisper (local)** -- Speech-to-text for the Stream Observer agent pipeline
- **OpenRouter** -- API routing service connecting to multiple LLM providers; $200 budget allocated

### Development Tools
- **GitHub (Classic PAT)** -- Fork-based collaboration model with branch prefixes for multi-agent work
- **Python** -- Primary language for RBI backtesting scripts, Stream Observer, and dashboards
- **TA-Lib (C library + Python wrapper)** -- Technical analysis library required for backtesting
- **Google Drive** -- Key/config sharing intermediary between separate physical machines
- **Notion** -- Project management with toggle lists for roadmap and task organization

### Infrastructure
- **Mac Mini (x5)** -- Named Slim, Mash, Killer, Cash, Gal; each running macOS with Caffeine keep-alive
- **SSH** -- Used to access the Hyperliquid data layer node
- **Hyperliquid Node** -- Custom-built data layer with 55+ API endpoints for liquidation/position data
- **Google Chrome Remote Desktop** -- Referenced for remote machine management

### Trading/Data
- **Hyperliquid** -- Decentralized exchange providing transparent liquidation data; HLP vault at $118M
- **Quant App (Mundave App)** -- Custom trading app with position viewer, liquidation-based entry signals, and risk controls
- **CoinGlass** -- Referenced as competitor for liquidation data ($8,388/year for 12 days)
- **Pump.fun** -- Referenced as design inspiration for making financial dashboards fun

---

## KEY PROMPTS USED WITH CLAUDE/WHISPER FLOW

### Prompt #1: Multi-Agent GitHub Architecture
**Context:** ~00:27 - First interaction planning the multi-machine workflow
**Exact Prompt:** > "I have one main or two main GitHubs I would like to share with all five of them. But if that GitHub is using my Gmail to log in, how do I go ahead and make a new GitHub for each of them?"
**Result:** Claude suggested the fork model -- one GitHub account per agent, each forking the main repos. Moon Dev refined this to a single secondary account (Cracker) with all agents sharing it via branch prefixes.

### Prompt #2: Presidential Campaign Plan
**Context:** ~00:36 - Tangential but illustrative of "think big" philosophy
**Exact Prompt:** > "Give me a structure here to a 2-year chase of this that extends to 6 years just in case... actionable plan that I will send to an AI that has its own computer that will work on this campaign for the rest of time being because I'm only 36."
**Result:** Claude produced a multi-cycle plan (2028/2032/2036/2040) with phases including FEC registration, exploratory committee formation, digital presence, and PAC setup.

### Prompt #3: Agent GitHub Rules (Refined by Cracker)
**Context:** ~01:10 - Having the lead agent (Cracker) finalize the collaboration rules
**Exact Prompt:** > "Here's a plan that hasn't been run by you yet. I want you to update the plan... I'm trying to think of a multi-way to work with 4 other computers... here's the plan that me and another AI came up with, but this is your chance to give me the final plan because you're the big dog. You're queen alpha."
**Result:** Cracker tightened the rules: fixed wrong repo names, added clarity on which repo agents work in, specified branch naming conventions (agent-[name]/), and defined the PR workflow.

### Prompt #4: Stream Observer Idea Generation
**Context:** ~00:22 - Background Whisper-to-LLM pipeline prompt
**Exact Prompt:** > "Find the top two biggest opportunities from your live stream. Think 10M to 100M. Think 100x bigger than your first instinct and go bigger."
**Result:** Generated ideas like "Autonomous liquidation arbitrage engine" and "Institutional smart money mirror platform" -- inflated beyond what was actually discussed but aligned with the ambitious framing.

### Prompt #5: RBI Dashboard Build
**Context:** ~02:15 - Instructing agents to build visualization dashboards
**Exact Prompt:** > "Build me a dashboard that is super fun, updates every action and will be a bit chaotic because of the multiple threads. But that's good. I want it visually fun as [expletive] and I want real data that is useful coming through. Don't hold back on design. Use purple -- actually no purple."
**Result:** Three different dashboards built by three different models. MiniMax produced the fastest; Kimmy produced the most visually appealing with proper activity feeds.

### Prompt #6: RBI Strategy Ideas Generation
**Context:** ~03:15 - Instructing GLM 4.7 to populate ideas and launch the pipeline
**Exact Prompt:** > "I want you to build a system that populates 10 ideas there of trading strategies Jim Simons would test and then launch the RBI agent PP multi to run. But first, make a slot machine type fun pump fun hella colors tracker dashboard where I can see the ideas the RBI agent is working on and the stats it gets from the final backtest."
**Result:** GLM 4.7 began building but had delays; eventually produced a functional dashboard with RBI agent integration.

---

## CRITICAL INSIGHTS

### Infrastructure Architecture
- The fork-based GitHub model with agent branch prefixes is a scalable pattern for multi-agent AI collaboration, borrowing directly from open-source development practices
- Cross-machine key distribution is a genuine bottleneck when working with separate physical computers -- Google Drive as intermediary is a pragmatic workaround
- The 5-machine setup is explicitly a proof-of-concept for 500; workflow bottlenecks at 5 machines (repetitive config, manual token distribution) would need automation before scaling

### LLM Model Comparison (Empirical Findings)
- **Speed ranking:** MiniMax M2.5 (direct) >> GLM 4.7 (OpenCode) > Kimmy 2.5 (OpenCode)
- **Quality ranking:** Kimmy 2.5 >= MiniMax M2.5 > GLM 4.7 (for dashboard/UI generation tasks)
- **Reliability ranking:** MiniMax direct > Kimmy OpenCode > GLM OpenCode (GLM had unexplained idle gaps)
- Critical finding: Same model (MiniMax 2.5) behaves differently through different routing paths -- direct API works, OpenCode Zen routing fails

### Trading Strategy Philosophy
- Moon Dev's core edge is not price prediction but liquidation prediction -- using Hyperliquid's transparent on-chain data to trade around forced liquidation events
- The Quant app adds "bumpers" to manual trading: max position size, daily loss limit (3%), liquidation-aware entries
- The RBI system (Research/Backtest/Implement) is positioned as the scalable automated approach, with multiple machines running parallel strategy discovery 24/7

### Community & Business Dynamics
- The "dichotomy of the chat" -- simultaneously receiving advanced engineering insights and basic support questions -- is identified as a signal of multi-level audience engagement
- The private Zoom model ($5/day or $1,500 lifetime) emerged from a security incident (hacking) and now serves as both a revenue model and quality filter
- Moon Dev explicitly values pushing people out ("90-day money-back guarantee is for both of us") to maintain a committed community

---

*Analysis compiled from ~3h47m transcript. Speaker uses Whisper Flow to interact with Claude Code throughout. Stream includes repeated promotional segments and motivational tangents characteristic of Moon Dev's live format.*
