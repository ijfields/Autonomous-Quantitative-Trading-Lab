# Step-by-Step Guide: OpenClaw Agent Deployment Patterns

**Source:** DeepStation AI (YouTube)
**Video ID:** awIfvN-NzBI
**Upload Date:** 2026-03-08

---

## What This Guide Covers

Three OpenClaw deployment patterns from a live Miami meetup: (1) building a CRM agent swarm with WhatsApp auto-response, (2) sandboxing agents with Night Shift + Firecracker microVMs, and (3) structuring persistent intent with the soul/user/memory three-file pattern.

---

## Pattern 1: CRM Agent Swarm (Michael Freeberg)

### Step 1: Set Up the Orchestrator
1. Choose a multi-agent framework: **CrewAI** (crewai.com, open-source) or alternatives (Agency framework)
2. Define agent roles: orchestrator, research agent, messaging agent, LinkedIn agent
3. Each agent has a specific task and the orchestrator routes work between them

### Step 2: Connect WhatsApp Messaging
1. Get a **second phone number** (never use your primary — risk of permanent ban)
2. Use **Baileys npm** package for WhatsApp Web connectivity (same library OpenClaw uses)
3. Run everything in **Docker Desktop** on a dedicated machine (Mac Mini recommended)
4. Note: This is a gray area — WhatsApp prefers you use their official Business API

### Step 3: Add AI Persona
1. Use **OpenAI 5.1 Codex** (or similar) for conversation responses
2. Create a video clone with **HeyGen** ($1/video) for personalized outreach
3. Use **11 Labs** for voice synthesis in multiple languages
4. Build in safeguards: content filtering for vulgar/inappropriate messages, privacy deletion command

### Step 4: Add Research and LinkedIn Automation
1. Use **People Data Labs** API for contact information lookup
2. Install **OpenClaw Chrome browser relay extension** for LinkedIn automation
3. Connect OpenClaw to your Chrome profile (already logged into LinkedIn)
4. Send instructions via **Tailscale** from orchestrator to OpenClaw instance

### Step 5: Monitor and Iterate
1. Set up **Grafana + Loki** for logging and cost tracking
2. Track LLM spending per API (OpenAI, 11 Labs, HeyGen credits)
3. Commit every change — vibe-coded apps break easily and can't self-repair
4. Create an architecture.md so you can understand what the AI built

---

## Pattern 2: Sandboxed Agent Deployment (Giani Carrillo — Night Shift)

### Step 1: Understand the Threat Model
1. Agents write their own code and take autonomous actions
2. Apply **defense-in-depth**: security policies at every boundary
3. Key policy points: ingress traffic (host), network bridge, file I/O, network I/O inside sandbox

### Step 2: Compile Night Shift Daemon
1. Clone the Night Shift repo (open-source, GitHub)
2. Compile: `go build -o nightshiftd main.go`
3. Configure `config.toml` with defaults:
   - `vCPUs: 2`
   - `memory: 512 MB`
   - `timeout: 300`
   - `max_concurrent_vms: 3`
   - `default_sandbox: firecracker`

### Step 3: Build the Agent Container
1. Create a Dockerfile that installs the PI coding agent (OpenClaw's underlying agent)
2. Add OCI spec labels for self-description:
   ```dockerfile
   LABEL protocol="v1"
   LABEL vcpus="2"
   LABEL memory="2024"
   LABEL timeout="600"
   LABEL sandbox="vm"    # "vm" = Firecracker, "container" = Docker
   ```
3. Build: `docker build -t pi-agent:latest .`

### Step 4: Deploy and Invoke
1. Start Night Shift daemon: `./nightshiftd --config config.toml`
2. Deploy agent via API: POST to `/deploy` with image ref and agent name
3. Create a run: POST to `/run` with task prompt
4. Stream events: GET `/stream/{run_id}` for real-time text deltas
5. Firecracker microVM boots its own kernel — complete hardware-level isolation

### Step 5: Choose Your Infrastructure
- **Bare metal (recommended):** AWS C5 Metal or any KVM-capable machine
- **Heterogeneous support:** Same node can run Firecracker, Kata containers, Docker, WASI runtimes
- **No GPU required** for the sandbox runtime itself

---

## Pattern 3: The Intent Era — Three-File Pattern (Alan Garcia)

### Step 1: Create the Soul File
1. Define the agent's value system: judgment, defaults, tone, boundaries
2. This is the agent's identity — what it believes, how it communicates
3. Keep it concise — soul files should use minimal context

### Step 2: Create the User File
1. Define who you are: role, preferences, constraints
2. Example: "Head of engineering. Prefers direct answers. Runs infrastructure on VPS, not local Mac Mini."
3. Include infrastructure details, communication preferences, working hours

### Step 3: Structure the Memory File
1. Accumulate decisions, context, and lessons learned across sessions
2. Encode **multi-year vision** — where the product should be in 2 years, working backwards
3. Include failure history and constraints (e.g., "never change the bind config on the local server")
4. When an agent crashes, the next agent reads memory and picks up where it left off

### Step 4: Monitor Context Usage
1. Set up a cron job to report context usage across all files
2. Track: memory (largest), agents, tools, soul, identity, user
3. Aim to stay well under context limits — compaction degrades quality

### Step 5: Manage Agent Lifecycle
1. Treat agents as **ephemeral** — they will crash, die, or be replaced
2. Intent (the three files) is what persists, not the agent itself
3. Use **self-referential links** (Slack message links, GitHub URLs) to help agents recover context
4. Use disposable credentials — revoke access when agents are replaced
5. Audit every skill and dependency — minimize surface area

---

## Key Takeaways

> **Michael Freeberg:** "I didn't write a single line of code. It was all me prompting it." — Vibe coding works for agent swarms, but commit everything and use test-driven development.

> **Giani Carrillo:** "Doing the right thing should be easy." — Sandbox your agents with hardware-level isolation; Night Shift makes deploying into Firecracker microVMs straightforward.

> **Alan Garcia:** "Do your agents actually know what you want?" — The winners in the next two years won't have better models; they'll have better judgment encoded into systems that carry that judgment forward.

*Guide derived from: OpenClaw： Demos, Agent Swarms, and Workflows 🦞.txt*
