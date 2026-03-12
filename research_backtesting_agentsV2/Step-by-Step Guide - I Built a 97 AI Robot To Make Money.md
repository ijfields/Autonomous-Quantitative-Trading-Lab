# Step-by-Step Guide: Building a $97 Physical OpenClaw AI Agent

**Source:** Jaxon Poulton (YouTube)
**Video ID:** L5hWai_0qIY
**Upload Date:** 2026-03-06

---

## What This Guide Covers

How to build a pocket-sized, voice-controlled OpenClaw device for under $100 and the three money-making experiments tested with it.

---

## Step 1: Acquire Hardware (~$97)

| Part | Approximate Cost |
|------|-----------------|
| Raspberry Pi Zero | ~$15-25 |
| Wisplay board (display + speakers) | ~$40-50 |
| PiSugar battery pack | ~$25-30 |
| 128 GB micro SD card | ~$10 |

---

## Step 2: Assemble and Configure

1. Attach Wisplay board to Pi Zero (expect backwards-screwing issues)
2. Install PiSugar battery pack
3. Flash OS to 128 GB micro SD card (smaller cards are insufficient)
4. **Critical:** Connect to 2.4 GHz Wi-Fi only — Pi Zero cannot use 5 GHz
5. Install OpenClaw on the device
6. Expect ~5 days of troubleshooting for a non-technical builder

---

## Step 3: Choose a Money-Making Experiment

### Option A: Cold Email Outreach (Most Viable)
1. Set up a Gmail account for the bot
2. Identify target businesses (chiropractors, niche local shops)
3. Voice-command the bot to draft and send outreach emails
4. Manually approve each email before sending (safety measure)
5. Offer a service (e.g., $500 AI outreach setup)

### Option B: Prediction Market Trading (Proof of Concept)
1. Fund a prediction market account with small amount ($10)
2. Provide API keys to the bot (do this on a separate computer)
3. Command: scrape Reddit/Twitter for information, make trades
4. Monitor P&L and system resources (will max CPU/GPU)

### Option C: Marketplace Arbitrage (Not Viable)
- Facebook Marketplace bot detection blocks login entirely
- UI-based automation on anti-bot platforms does not work

---

## Key Warnings

- **Voice-only interaction is very slow** — every command cycles through speak → process → respond
- **Backend compute is separate** — the Pi Zero is just the interface; heavy computation runs on a laptop
- **Human oversight required** — do not let the bot send emails or make trades unsupervised
- **Results were poor** — net -$0.83 on trading, $0 on outreach, $0 on marketplace

---

## Key Takeaway

> A sub-$100 physical AI agent is buildable and can autonomously execute trades via API, but voice-only interaction is painfully slow, bot detection blocks UI automation on major platforms, and backend compute still requires a full laptop. This is a proof of concept, not a profit machine — yet.

*Guide derived from: I Built a $97 AI Robot To Make Money.txt*
