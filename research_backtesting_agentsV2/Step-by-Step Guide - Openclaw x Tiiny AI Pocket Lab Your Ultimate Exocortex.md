# Step-by-Step Guide: Running Local AI Agents on Tiiny AI Pocket Lab

**Source:** Tiiny AI (YouTube)
**Video ID:** yLeHazF6N4g
**Upload Date:** 2026-03-06

---

## What This Guide Covers

How to set up TinyBot (an OpenClaw-based local AI agent) on Tiiny AI Pocket Lab hardware for offline, zero-cost AI automation.

---

## Prerequisites

- Tiiny AI Pocket Lab hardware (or similar local compute device)
- Open model (GLM Flash or equivalent)
- OpenClaw framework installed
- Discord bot token (for Discord management use case)

---

## Step 1: Set Up the Hardware

1. Get a Tiiny AI Pocket Lab (via Kickstarter or retail)
2. Install TinyBot agent system (built on OpenClaw)
3. Load an open model (GLM Flash recommended)
4. No cloud account needed — everything runs locally

---

## Step 2: File Organizing & Local RAG

1. Point TinyBot at a directory with mixed files (PDFs, docs, slides)
2. TinyBot automatically organizes, indexes, and builds a knowledge base
3. Query the knowledge base naturally: "Summarize the key points from [document]"
4. All processing stays on-device — no data leaves your network

---

## Step 3: Web Data Collection

1. Give TinyBot a web collection task (e.g., "Collect all posts from X about [topic] in last 15 days")
2. TinyBot executes multi-step workflow: search → navigate → extract → compile
3. Results saved as structured table to local filesystem
4. Typical time: ~6 minutes for moderate tasks

---

## Step 4: Discord Management with Escalation

1. Connect TinyBot to your Discord server via bot token
2. TinyBot monitors and answers general questions automatically
3. Complex questions trigger WhatsApp message to human for approval
4. After approval, answer is posted back to Discord
5. Enables 24/7 coverage without constant human monitoring

---

## Key Takeaway

> Local AI agents eliminate API costs and keep data private. For teams that need always-on AI assistants but can't afford cloud API fees or have privacy requirements, running open models on dedicated hardware is a viable alternative.

*Guide derived from: Openclaw x Tiiny AI Pocket Lab: Your Ultimate Exocortex.txt*
