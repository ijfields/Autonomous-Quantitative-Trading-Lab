# Step-by-Step Guide: Replace Cloud Cameras with Self-Hosted ONVIF + Frigate

**Source:** Dad, the engineer (YouTube)
**Video ID:** Cc1ribAQK5g
**Upload Date:** 2026-03-03

---

## What This Guide Covers

How to replace cloud-connected security cameras (Ring, Nest, Arlo, etc.) with self-hosted ONVIF cameras and Frigate NVR to reclaim privacy, eliminate subscriptions, and gain full control of your video data. Includes camera selection, NVR setup, network security, and remote access.

---

## Prerequisites

- Old PC or server hardware (can repurpose existing unused hardware)
- Basic networking knowledge (VLANs, firewall rules)
- Home network with a capable router

---

## Step 1: Choose ONVIF-Compliant Cameras

1. Select cameras based on your needs:
   - **Budget ($15-$30):** Basic no-name ONVIF cameras — functional but may have security concerns (mitigated by network isolation)
   - **Mid-range ($50-$100):** Reolink, Amcrest — solid 4K, reliable
   - **Premium ($200+):** Axis, Hikvision with 25x optical zoom, thermal imaging
2. For doorbells: Reolink Video Doorbell or Amcrest AD410
3. For floodlights: ONVIF-compatible floodlight cameras available
4. Mix and match brands/tiers freely — ONVIF standard ensures interoperability

---

## Step 2: Set Up Your NVR Server

1. Repurpose an old PC or set up a dedicated server
2. Install **Proxmox** for virtualization (optional but recommended)
3. Install **Frigate** (free, open-source NVR):
   - Handles camera feeds
   - AI-powered local detection (people, cars, dogs)
   - No cloud dependency
4. Alternatives: Blue Iris (commercial), iSpy, Shinobi, ZoneMinder

---

## Step 3: Connect and Configure Cameras

1. Mount cameras physically and connect to your network (PoE or Wi-Fi)
2. Set up cameras via their web interface or app
3. Attach camera feeds to Frigate NVR
4. Configure in Frigate:
   - Notification rules
   - Recording schedules
   - Object detection zones
   - Motion sensitivity

---

## Step 4: Secure Your Camera Network

1. Create a **separate VLAN** for cameras — isolate from your trusted network
2. Set **firewall rules** to block cameras from accessing the internet
3. Even sketchy cheap cameras become safe when they can't call home
4. Only your NVR server should communicate with cameras

---

## Step 5: Set Up Mobile Viewing

1. Install **Home Assistant** on your server
2. Connect Frigate to Home Assistant
3. Access camera feeds from your phone via the Home Assistant app
4. Configure notifications for detected events

---

## Step 6: Enable Remote Access

1. Install **Tailscale** on your server and devices
2. Access your camera system securely from anywhere
3. No port forwarding needed — Tailscale creates encrypted tunnels
4. Everything required is under your control — no router capability dependencies

---

## Cost Comparison

| Setup | 3 Cameras Year 1 | Year 2+ | Privacy |
|-------|-------------------|---------|---------|
| Ring/Nest (cloud) | $300-$900 cameras + $100 subscription | $100/year | Company controls data |
| ONVIF + Frigate (self-hosted) | $150-$300 cameras + $0-$200 server | $0/year | You control data |

**Note:** Year 1 self-hosted cost may be higher if buying server hardware, but ongoing costs are near zero.

---

## Why Switch

| Cloud Camera Problem | Self-Hosted Solution |
|---------------------|---------------------|
| Employees viewing your footage | Data never leaves your network |
| AWS outage = no security | Local storage, always recording |
| Subscription fees forever | One-time hardware cost |
| Product sunsetting | ONVIF standard, vendor-agnostic |
| Data retention mystery | You control retention policies |
| No end-to-end encryption | Data stays on your LAN |
| Vendor lock-in | Mix and match any ONVIF camera |

*Guide derived from: Get rid of your Ring, Arlo, Tapo, Blink (or other cloud cameras) and reclaim your privacy!.txt*
