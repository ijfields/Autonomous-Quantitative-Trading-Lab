# Step-by-Step Guide: I built a Pocket AI Agent with Pico Claw on Raspberry Pi Zero

**Source:** HillPhantom (YouTube)
**Video ID:** UgxSTEA8BQY
**Upload Date:** 2026-02-24

## Prerequisites
- **Hardware:** Raspberry Pi Zero 2W ($15-20), power supply, microSD card, Wi-Fi access
- **Tools:** SSH client, terminal access to Pi
- **Accounts:** Open Router API key, Brave API key (free, 2,000 calls/day)
- **Knowledge:** Basic Linux command line, SSH

---

## Understanding Pico Claw

### Step 1: Know the Landscape
| Feature | OpenClaw | Nanobot | Pico Claw |
|---------|----------|---------|-----------|
| Memory | 100MB+ | ~100MB | <10MB |
| Startup | Slow | Moderate | <1 second |
| Hardware cost | Mac Mini+ | Mac Mini+ | $10 device |

Pico Claw is an ultra-lightweight OpenClaw fork by Scipede (a hardware company). It runs on devices with as little as 10MB of memory.

---

## Installation on Raspberry Pi Zero 2W

### Step 2: Install Prerequisites
```bash
sudo apt update && sudo apt install git
```
- Install Git and Go (if not already present)

### Step 3: Download Pico Claw
```bash
wget [ARM64 release URL from GitHub]
```
- Download the ARM64 release binary from the Pico Claw GitHub repository

### Step 4: Extract and Set Permissions
```bash
tar -xzf picoclaw-arm64.tar.gz
chmod +x picoclaw
```

### Step 5: Initialize Pico Claw
```bash
./picoclaw
```
- First run creates the configuration files

### Step 6: Configure the Model and API
Edit the config JSON file:
- **Model:** Set to Miniax (or your preferred model via Open Router)
- **API Base:** Set to Open Router endpoint
- **API Key:** Your Open Router API key

### Step 7: Start the Agent
```bash
./picoclaw agent
```
- This starts an interactive agent session on the Pi

---

## API Provider Configuration

### Step 8: Use Open Router (Recommended)
- Direct OpenAI and Anthropic connections are unreliable with third-party tools
- Anthropic is actively blocking/banning third-party applications
- Open Router acts as a proxy to connect to any model (Miniax, etc.)

### Step 9: Configure Web Search
- Sign up for Brave API (free, 2,000 calls/day)
- Configure as the web search provider in Pico Claw
- Enables agent web browsing capability

---

## Optional Enhancements

### Step 10: Add Docker Sandboxing
- Install Docker on the Pi for extra security isolation
- Run Pico Claw inside a container
- Important: OpenClaw variants represent significant security vulnerabilities

### Step 11: Configure Integrations
- **Telegram:** Set up bot integration for mobile access
- **Discord:** Configure Discord integration for channel-based interaction

---

## Edge Computing Use Cases

### Step 12: Explore Portable AI
- **GPIO pins:** Connect sensors, cameras, battery power, solar panels
- **Hackberry Pi Zero:** Physical keyboard form factor — fits in a pocket
- **USB stick form factor:** Plug into offline servers as RAG (retrieval-augmented generation)
- **Battery power:** Portable, untethered AI agent

---

## Common Pitfalls
- **Using direct Anthropic/OpenAI API connections:** These are unreliable with third-party tools — use Open Router instead
- **Skipping Docker:** OpenClaw variants have significant security vulnerabilities — use containers for isolation
- **Expecting full OpenClaw capabilities:** Pico Claw is lightweight by design — some features are trimmed
- **Ignoring security:** Be very careful with permissions and access on any OpenClaw variant

---

## Summary
Pico Claw enables running an OpenClaw-like agent on $10 hardware with <10MB memory and <1 second startup. Use Open Router as the API provider (direct Anthropic/OpenAI connections are unreliable). Brave API provides 2,000 free web search calls per day. Consider Docker containers for security isolation. Edge computing opens new use cases: battery-powered agents, sensor integration, and pocket-sized AI.

*Extracted from: I built a Pocket AI Agent with Pico Claw on Raspberry Pi Zero.txt*
