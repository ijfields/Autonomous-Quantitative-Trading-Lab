# Step-by-Step Guide: OpenClaw 3.13 + FREE GLM-4.7-Flash Claude Opus Local AI

**Source:** Julian Goldie SEO (YouTube)
**Video ID:** 70MEfCwuyZA
**Upload Date:** 2026-03-14

---

## What This Guide Covers
How to update OpenClaw to version 3.13 with live browser control, and how to run a free local AI model (GLM-4.7-Flash distilled from Claude Opus 4.5) using LM Studio.

---

## Step 1: Update OpenClaw to 3.13
1. Open your OpenClaw chat interface.
2. Type "update" in the chat.
3. Wait a few minutes for the gateway to reset.
4. Verify the update completed by checking the version display.

## Step 2: Enable Live Chrome Session Attachment
1. This is the headline feature of OpenClaw 3.13 -- your AI agent can now browse with your real logged-in browser session.
2. Two new browser profiles are available:
   - **Profile User**: Uses your real browser session on your screen.
   - **Chrome Relay**: Uses a special extension to connect more smoothly.
3. Enable the feature via the settings toggle described in the changelog.
4. No extensions or extra setup required -- just one toggle.
5. Your AI agent can now see your Gmail, dashboards, and other logged-in tools.

## Step 3: Configure Docker Timezone (If Using Docker)
1. Set the environment variable `openclaw_tz` in your Docker configuration.
2. Use any standard timezone string (e.g., `America/New_York`, `Asia/Bangkok`).
3. Both the gateway container and CLI container will lock to that timezone.
4. This fixes timestamp bugs and tasks running at wrong times.

## Step 4: Download and Install LM Studio
1. Go to the LM Studio website and download the installer for your OS.
2. Install LM Studio on your machine (Mac, Windows, or Linux).

## Step 5: Download the GLM-4.7-Flash Claude Opus Model
1. Open LM Studio.
2. Go to the model search section.
3. Search for "GLM 4.7 flash opus" or "GLM 4.7 claude opus."
4. Browse the available versions (multiple quantizations available).
5. Download a version appropriate for your hardware (the model is approximately 18 GB).
6. Wait for the download to complete.

## Step 6: Run the Model Locally
1. In LM Studio, click "Use in new chat" on the downloaded model.
2. Wait for the model to load.
3. Start chatting -- the model runs entirely on your machine.
4. No API keys, no subscriptions, no data leaving your machine.

## Step 7: Apply the Distilled Edge Framework
1. **Use the local model when:**
   - Input contains data you don't want on cloud servers
   - You need to run the same task repeatedly at volume without paying for tokens
   - Speed is more important than maximum quality
   - You want to experiment and iterate freely
2. **Use cloud models when:**
   - Highest possible quality is non-negotiable
   - Complex multi-step reasoning chains push the limits of a 30B parameter model
   - Tasks require real-time web access

## Step 8: Connect Local Models to OpenClaw (Optional)
1. Local models like GLM-4.7-Flash can be used to power OpenClaw via Ollama.
2. Configure OpenClaw to point to your local model endpoint.
3. This gives you a free AI agent powered by local reasoning.

---

## Key Takeaway

> OpenClaw 3.13's live Chrome session attachment transforms what your AI agent can do on the web, while GLM-4.7-Flash distilled from Claude Opus 4.5 brings strong reasoning to your local machine for free -- use the Distilled Edge Framework to know when each approach fits best.

*Guide derived from: OpenClaw 3.13 + FREE GLM-4.7-Flash Claude Opus Local AI [70MEfCwuyZA].en.vtt*
