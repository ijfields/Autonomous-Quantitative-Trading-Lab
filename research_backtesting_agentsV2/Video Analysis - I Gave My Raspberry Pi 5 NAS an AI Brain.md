# I Gave My Raspberry Pi 5 NAS an AI Brain! — Complete Transcript Analysis

**Video Title:** I Gave My Raspberry Pi 5 NAS an AI Brain!
**Channel:** Mayukh Builds
**Video ID:** upUtCCpO_0w
**Upload Date:** 2026-03-11
**Duration:** ~16m
**Speaker:** Mayukh (Mayukh Builds)
**Platform:** YouTube

---

## EXECUTIVE SUMMARY

Mayukh demonstrates building a pocket-sized self-hosted NAS using a Raspberry Pi 5 (8GB) with an 8TB NVMe SSD, then adds a local AI agent powered by Qwen 3.5 (8B) via Ollama. The system replaces paid cloud storage (Google Drive, OneDrive, iCloud — $10-50/month) with Nextcloud + Tailscale for anywhere access, and adds AI-powered file search and summarization. All running on just 15-20W of power.

---

## KEY TOPICS

### Hardware Setup
| Component | Spec |
|-----------|------|
| Board | Raspberry Pi 5 (8GB) |
| Power | 25W brick (don't use underpowered ones) |
| Storage | 8TB NVMe M.2 SSD |
| Adapter | Frenov NVMe hat (~$15-18 CAD) |
| Power Draw | 15-20W total |

### Software Stack
1. Raspberry Pi OS (flashed to micro SD, then cloned to NVMe)
2. **Nextcloud** (via Snap) — open-source iCloud/Google Drive replacement
3. **Tailscale** — VPN mesh network for access from anywhere
4. **Ollama** — local LLM runtime
5. **Qwen 3.5 (8B)** — local AI model for file search/summarization

### AI Agent Architecture
- Static HTML chat UI → orchestrator → Qwen 3.5 via Ollama
- Orchestrator has "tool chest": search files, list properties, read files, list recent files
- Natural language queries: "What is this file about?", "Do we have more storage?"

### Known Issue
- RPI Clone tool by Jeff Curling fails for drives >2TB — requires manual workaround

---

## TOOLS & PLATFORMS

| Tool | Purpose |
|------|---------|
| Raspberry Pi 5 | Compute platform |
| Nextcloud | Self-hosted cloud storage |
| Tailscale | VPN for remote access |
| Ollama | Local LLM runtime |
| Qwen 3.5 (8B) | Local AI model |
| Frenov NVMe hat | Pi-to-SSD adapter |

---

## KEY TAKEAWAY

> A Raspberry Pi 5 + NVMe SSD can serve as a fully self-hosted NAS with Nextcloud + Tailscale providing iCloud-like functionality accessible from anywhere, completely free after the ~$200-300 hardware cost. A local 8B parameter model adds basic AI-powered file search and summarization, though capabilities are limited on Pi hardware. All running on 15-20W.

*Analysis derived from: I Gave My Raspberry Pi 5 NAS an AI Brain!.txt*
