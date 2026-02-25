# Video Analysis: I built a Pocket AI Agent with Pico Claw on Raspberry Pi Zero

**Speaker:** HillPhantom (El Phantom)
**Channel:** HillPhantom
**Video ID:** UgxSTEA8BQY
**Upload Date:** 2026-02-24
**Duration:** ~17 minutes

---

## Overview
A walkthrough of installing Pico Claw — an ultra-lightweight OpenClaw fork using under 10MB of memory — on a Raspberry Pi Zero 2W. The speaker covers the Pico Claw project (by Scipede, a hardware company), compares it to OpenClaw (100MB+) and Nanobot, demonstrates the full installation process via SSH, configures it with Open Router + Miniax model, and shows it working (building a webpage, answering questions). Includes security warnings about OpenClaw and discussion of edge computing potential with GPIO pins, cameras, and battery power.

---

## Key Concepts

### Pico Claw vs. OpenClaw
| Feature | OpenClaw | Nanobot | Pico Claw |
|---------|----------|---------|-----------|
| Memory | 100MB+ | ~100MB | <10MB |
| Startup | Slow | Moderate | <1 second |
| Hardware cost | Mac Mini+ | Mac Mini+ | $10 device |

### Edge Computing ("EdgeClaw")
- Raspberry Pi Zero + Wi-Fi chip enables portable AI agent
- GPIO pins → sensors, cameras, battery power, solar
- Fits in a pocket (Hackberry Pi Zero form factor with physical keyboard)
- USB stick form factor possible — plug into offline servers as RAG

### Open Source Ecosystem
- Peter Steinberger created OpenClaw, open-sourced it before "signing with OpenAI"
- Forks like Pico Claw and Nanobot emerged from the open-source code
- Pico Claw by Scipede (hardware company) — also sells $10 devices and KVM switches

### API Provider Issues
- Only Open Router worked reliably (not direct OpenAI or Anthropic)
- Anthropic actively blocking/banning third-party applications
- Open Router acts as a proxy to connect to any model (Miniax, etc.)
- Brave API recommended for web search (2,000 free calls/day)

---

## Installation Steps (Raspberry Pi Zero 2W)

| Step | Action |
|------|--------|
| 1 | Install Git and Go |
| 2 | `wget` the ARM64 release from GitHub |
| 3 | `tar` to extract |
| 4 | `chmod` for permissions |
| 5 | Run `./picoclaw` to initialize |
| 6 | Edit config JSON: set model (Miniax), API base (Open Router), API key |
| 7 | Run `./picoclaw agent` to start interactive session |
| 8 | Optional: Configure Telegram/Discord integration |
| 9 | Optional: Docker container for extra sandboxing |

---

## Tools & Platforms
| Tool | Purpose |
|------|---------|
| Pico Claw | Lightweight OpenClaw fork (<10MB) |
| Raspberry Pi Zero 2W | Edge hardware ($15-20) |
| Open Router | API proxy to connect to any model |
| Miniax 2 | Model used (via Open Router) |
| Brave API | Free web search (2,000 calls/day) |
| Docker | Optional sandboxing for security |
| Hackberry Pi Zero | Physical keyboard device for mobile use |
| Scipede | Hardware company behind Pico Claw |

---

## Actionable Takeaways
1. Pico Claw enables running an OpenClaw-like agent on $10 hardware with <10MB memory
2. Use Open Router as the API provider — direct Anthropic/OpenAI connections are unreliable with third-party tools
3. Brave API provides 2,000 free web search calls per day — excellent for agent web browsing
4. Consider Docker containers for extra security isolation when running any OpenClaw variant
5. Edge computing opens new use cases: battery-powered agents, sensor integration, pocket-sized AI
6. Security warning: OpenClaw (and forks) represent significant security vulnerabilities — be very careful with permissions and access

*Analyzed from: I built a Pocket AI Agent with Pico Claw on Raspberry Pi Zero.txt*
