# Step-by-Step Guide: 10 Gigabit Home Network for $10

**Source:** jakkuh (YouTube)
**Video ID:** 5FWWVdCwb5s
**Upload Date:** 2026-03-10

---

## What This Guide Covers

How to upgrade to 10 Gigabit Ethernet using existing Cat 5e cabling and a $10 Intel X540-T2 network card from eBay.

---

## Step 1: Check Existing Cabling

1. Identify Cat 5e cables already in your walls
2. Cat 5e is rated for 1 Gbps but works at 10 Gig when terminated properly

---

## Step 2: Terminate Cables Properly

1. Use **keystone jacks** (toolless type) with **B termination standard**
2. Keep untwisted pairs to **~1/4 inch** (not 6 inches)
3. Use pliers to press wires fully into contacts
4. This is the single most important step for 10 Gig over Cat 5e

---

## Step 3: Install Intel X540-T2

1. Buy Intel X540-T2 on eBay (~$10, dual-port 10GbE)
2. Requires at least a PCIe x4 slot (x1 only gives ~500 MB/s)
3. Replace stock fan with a Noctua fan (stock is usually noisy/dead)

---

## Step 4: Install Drivers

1. Intel removed X540-T2 drivers from product page
2. Download the **"complete driver pack for Intel Ethernet adapters"** from Intel
3. Install via Device Manager → Browse computer → select extracted folder → include subfolders

---

## Step 5: Test and Verify

1. Expected: 800-900 MB/s bidirectional file transfers
2. Shortfall from theoretical 1250 MB/s is SSD speed and Windows overhead, not the network
3. For direct NAS-to-PC: use two X540-T2 cards with static IPs — no switch needed

---

## Optional: Add a 10GbE Switch

1. **Mokerlink 6-port** (4x RJ45, 2x SFP+) to share 10 Gig across multiple devices

---

## Key Takeaway

> 10 Gigabit networking costs ~$20 if you have Cat 5e in the walls. The secret is proper cable termination — keep untwisted pairs to 1/4 inch at keystone jacks. Cat 5e handles 10 Gig in real-world conditions.

*Guide derived from: I made my internet 10X FASTER for $10.txt*
