# Step-by-Step Guide: Self-Hosting XMPP with Prosody on NixOS

**Source:** tony (YouTube)
**Video ID:** XwMWUZYUTvM
**Upload Date:** 2026-02-26

---

## What This Guide Covers

Two paths: the 5-minute "normie path" using a public XMPP server, and the full self-hosting path with NixOS + Prosody including federation and Matrix bridging.

---

## Normie Path (5 Minutes)

1. Go to xmpp.org → Getting Started → Public Provider List
2. Register on a public server (e.g., jabbers.one) — username + password only
3. Download **Gajim** (desktop) or use **Converse.js** (browser)
4. Join group chats by address (e.g., `room@conference.server.com`)

---

## Self-Hosting Path

### Step 1: Hardware

- Any old laptop, ThinkPad, or mini-PC
- A domain name and internet connection
- No VPS required

### Step 2: NixOS Configuration (xmpp.nix)

Configure Prosody with:
- Domain variables (main, MUC conference, upload)
- SSL/TLS via Let's Encrypt (ACME)
- HTTP file sharing (100 MB upload limit)
- MUC (multi-user chat rooms)
- Modules: roster, SASL, TLS, dialback, disco, carbons, PEP, MAM, ping, HTTP file upload
- Registration disabled (create accounts via `prosodyctl adduser`)

### Step 3: nginx Reverse Proxy

- Serve ACME challenges on port 80
- Return 404 for all other HTTP routes

### Step 4: Open Firewall Ports

| Port | Purpose |
|------|---------|
| 80 | ACME/HTTP challenges |
| 443 | HTTPS file uploads |
| 5222 | XMPP client connections |
| 5269 | XMPP server-to-server federation |
| 5281 | Prosody HTTP upload |

### Step 5: Deploy

```bash
sudo nixos-rebuild switch
prosodyctl adduser yourname@yourdomain.com
```

### Step 6 (Optional): Matrix Bridge

- Install Matrix bridge on your XMPP server
- Join Matrix rooms from Gajim without needing a separate Matrix client

---

## Key Takeaway

> XMPP's relay-based federation model avoids the content-replication liability of Matrix (your server never stores other servers' content). Self-hosting with NixOS + Prosody is a single configuration file, runs on any hardware, and the protocol is battle-tested for 25+ years.

*Guide derived from: XMPP is the End Game of Chat Protocols (2027 Edition).txt*
