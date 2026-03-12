# Step-by-Step Guide: OpenClaw 3.8 Setup and Safety Configuration

**Source:** RoboNuggets (YouTube)
**Video ID:** MoKNM53PLS4
**Upload Date:** 2026-03-10

---

## What This Guide Covers

Key features and safety configuration for OpenClaw 3.7/3.8: Telegram topic routing, post-compaction survival sections, backup procedures, and model assignment.

---

## Step 1: Update to OpenClaw 3.8

1. Update your OpenClaw installation to the latest 3.8 release
2. Run `openclaw backup create` before updating (safety net)
3. Run `openclaw backup verify` to confirm backup integrity

---

## Step 2: Set Up Telegram Topic Routing

1. Create a Telegram group (e.g., "AI Studio")
2. Go to **More Settings → Manage Group → Topics → Enable**
3. Create topics for different workflows (e.g., General, Content, Development, Client Management)
4. Assign each topic:
   - **Different model** (e.g., Sonnet for General/cheap tasks, Opus for Development)
   - **Different skill subset** (avoid loading 40+ skills into one agent)
   - **Different system prompt** tailored to each workflow
5. Each topic gets its own isolated session, memory, and workspace

---

## Step 3: Configure Post-Compaction Survival Sections (Critical)

1. In your `agents.md` file, define sections that **must survive compaction**
2. Include all safety-critical instructions:
   - "Always confirm before taking destructive actions"
   - "Never access personal email/contacts"
   - "Never spend money without explicit approval"
3. Ask your OpenClaw to include these in the post-compaction sections
4. Test by filling context and verifying instructions persist after compaction

---

## Step 4: Security Best Practices

1. **Never run OpenClaw on your personal computer** — use a dedicated machine
2. **Never give OpenClaw personal email access** — set up a separate sandbox email
3. Use `/stop` command (not chat messages) to halt agent actions immediately
4. Review API key protection settings
5. If running on VPS, apply security hardening updates from 3.8

---

## Step 5: Install Compaction Plugins (Optional)

1. Install **Lossless Claw** plugin from GitHub for better context summarization
2. Configure **"Recent Turns Preserved"** setting to customize how many messages survive compaction

---

## Step 6: Configure New Models

1. Gemini 3.1 Flash Light — available as a fast/cheap option
2. GPT 5.4 — available as an alternative to Claude models
3. Assign models per Telegram topic based on cost/capability tradeoff

---

## Step 7: Regular Backup Schedule

1. Run `openclaw backup create` regularly (at least weekly)
2. Run `openclaw backup verify` after each backup
3. Archives configuration, agents, memory, and workspace

---

## Key Takeaway

> The most critical 3.8 feature is post-compaction survival sections — without them, safety instructions can be silently lost when context compacts, leading to dangerous autonomous behavior. Always sandbox OpenClaw on dedicated hardware with limited access.

*Guide derived from: OpenClaw's 3.8 Update is MASSIVE (Full Breakdown).txt*
