# Step-by-Step Guide: Building a Raspberry Pi 5 NAS with AI Brain

**Source:** Mayukh Builds (YouTube)
**Video ID:** upUtCCpO_0w
**Upload Date:** 2026-03-11

---

## What This Guide Covers

How to build a self-hosted NAS on a Raspberry Pi 5 with Nextcloud, Tailscale for remote access, and a local AI agent (Qwen 3.5 via Ollama) for smart file search.

---

## Step 1: Acquire Hardware
| Component | Spec | Cost |
|-----------|------|------|
| Raspberry Pi 5 | 8GB version | ~$80 |
| Power brick | 25W (don't underpay here) | ~$15 |
| NVMe SSD | Any M.2 NVMe (8TB used in video) | Varies |
| NVMe hat | Frenov adapter | ~$15-18 CAD |

## Step 2: Assemble and Flash OS
1. Attach the NVMe hat to the Pi via ribbon connector (handle carefully — fragile)
2. Flash Raspberry Pi OS to a micro SD card
3. Boot from SD card and SSH into the Pi

## Step 3: Boot from NVMe SSD
1. Change boot order to NVMe: `sudo raspi-config` → Advanced → Boot Order
2. Clone SD card to NVMe SSD
3. **Important:** For drives >2TB, RPI Clone tool fails — use manual copy+format workaround
4. Remove SD card and verify NVMe-only boot via SSH

## Step 4: Install Nextcloud
1. Install via Snap: `sudo snap install nextcloud`
2. Access via browser at the Pi's local IP
3. Set up user accounts and file sync
4. Sync with Mac, iPhone, Windows devices

## Step 5: Install Tailscale for Remote Access
1. Install Tailscale: `curl -fsSL https://tailscale.com/install.sh | sh`
2. Authenticate with your Tailscale account
3. Access your NAS from anywhere in the world via VPN mesh
4. No port forwarding or dynamic DNS needed

## Step 6: Add AI Brain (Ollama + Qwen 3.5)
1. Install Ollama: `curl -fsSL https://ollama.com/install.sh | sh`
2. Pull the model: `ollama pull qwen3.5:8b`
3. Set up the orchestrator with a "tool chest" (file search, list, read commands)
4. Deploy a simple HTML chat interface
5. Natural language queries: "What is this file about?", "How much storage do we have?"

---

## Key Takeaway

> A Raspberry Pi 5 + NVMe SSD replaces paid cloud storage ($10-50/month) with a fully self-hosted NAS running on 15-20W. Nextcloud + Tailscale provides file sync across all devices, accessible from anywhere. A local 8B model adds basic AI-powered search — limited on Pi hardware but functional as a proof of concept.

*Guide derived from: I Gave My Raspberry Pi 5 NAS an AI Brain!.txt*
