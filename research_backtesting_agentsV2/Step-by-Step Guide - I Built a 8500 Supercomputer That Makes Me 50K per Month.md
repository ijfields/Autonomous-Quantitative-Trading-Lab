# Step-by-Step Guide: Building an $8,500 Home Server for AI and Automation

**Source:** Lead Gen Jay (YouTube)
**Video ID:** cJ886HHGsRM
**Upload Date:** 2025-03-14

---

## What This Guide Covers

How to build a self-hosted home server that replaces $2,000+/month in cloud and AI API costs, running local AI models, workflow automation, email verification, web scraping, and web hosting — all on open-source software.

---

## Step 1: Acquire the Hardware

| Component | Spec | Why |
|-----------|------|-----|
| CPU | AMD Ryzen 9 (16 cores, 32 threads) | Handles heavy parallel workloads |
| RAM | 128 GB | Run multiple AI models simultaneously |
| Storage | 14 TB | Store scraped data, backups, media |
| GPU | NVIDIA RTX 5090 | Local AI inference at near-API quality |
| OS | Unraid | Web-based server management |

- **Total cost:** ~$8,500
- **Parts list:** Speaker shares via Amazon Storefront (link in video)
- **Key advantage over Mac Mini/Studio:** Every component is individually upgradeable

---

## Step 2: Install Unraid

1. Unraid is the server OS — think "macOS for servers" with a web UI
2. Install on a USB drive (Unraid boots from USB)
3. Access via browser at `zeus.local` on your local network
4. Also accessible via SSH for remote management
5. Claude Code can SSH into the server to configure and manage everything

---

## Step 3: Set Up Docker Containers

1. Unraid has a built-in Docker management interface
2. Each application runs in its own container — isolated, easy to manage
3. Install containers for your core stack (see next steps)
4. Containers auto-restart on server reboot

---

## Step 4: Install Local AI Models (Ollama + Open WebUI)

1. Install Ollama container — hosts AI models locally
2. Install Open WebUI container — provides a ChatGPT-like interface for your local models
3. Download models: DeepSeek, Llama, Mistral (via Ollama)
4. **80% of daily AI tasks** (summarization, email personalization, cold email writing) run fine on local models
5. Only use paid APIs (Claude, GPT) for the 20% requiring frontier reasoning
6. **Savings:** $800-$1,500/month in API costs eliminated

---

## Step 5: Set Up Workflow Automation (n8n)

1. Install n8n container (open-source Zapier/Make alternative)
2. Build automations: lead scraping → email verification → personalization → outreach
3. n8n can run millions of executions per month on your local server
4. No per-execution pricing like cloud alternatives
5. Automations run 24/7 without monthly fees

---

## Step 6: Install Open-Source SaaS Replacements

| Paid SaaS | Open-Source Replacement | Savings |
|-----------|----------------------|---------|
| Vercel/Netlify | Coolify | Web hosting, free |
| Email verification services | Reacher | Hundreds of thousands of verifications/day |
| Google Maps data | Google Maps Scraper | 24/7 scraping, ~15M businesses |
| BuiltWith | BuiltWith alternative | Tech stack analysis |
| Dropbox/Google Drive | Zeus's 14TB local storage | File storage |
| Digital Ocean / AWS | Zeus itself | Hosting |

---

## Step 7: Host Websites and Apps

1. Install Coolify (open-source Vercel replacement)
2. Deploy WordPress sites, custom apps, client dashboards
3. All hosted locally — no monthly hosting fees
4. Set up domain routing to point to your server

---

## Step 8: Run the Server 24/7

1. Server runs headless — no monitor or keyboard needed
2. Access entirely via browser (Unraid web UI) or SSH
3. Set up automatic security updates and monitoring
4. Server doubles as a revenue generator: client automations hosted on it as part of your service offering

---

## Step 9: Use Claude Code for Server Management

1. Claude Code can SSH into your server
2. Ask Claude to configure services, troubleshoot issues, manage containers
3. Makes the system accessible to non-technical users
4. "Claude, install Reacher on Zeus and configure it for email verification"

---

## Key Takeaway

> An $8,500 home server can eliminate $2,000+/month in cloud hosting and AI API costs while running your entire business infrastructure. The key insight: 80% of AI tasks don't need frontier models — local models on Ollama handle them fine. Build the infrastructure now because today's state-of-the-art models will run on hardware like this within a year. Unlike Mac Mini/Studio, every component is upgradeable.

*Guide derived from: I Built a $8,500 Supercomputer That Makes Me $50K⧸Month.txt*
