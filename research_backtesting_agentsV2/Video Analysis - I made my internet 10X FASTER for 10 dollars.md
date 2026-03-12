# I made my internet 10X FASTER for $10 — Complete Transcript Analysis

**Video Title:** I made my internet 10X FASTER for $10
**Channel:** jakkuh
**Video ID:** 5FWWVdCwb5s
**Upload Date:** 2026-03-10
**Duration:** ~14m
**Speaker:** Jake (jakkuh)
**Platform:** YouTube

---

## EXECUTIVE SUMMARY

Jake demonstrates upgrading a home network to 10 Gigabit Ethernet on a budget using existing Cat 5e cabling and an Intel X540-T2 10GbE network card ($10 on eBay). Achieved ~900 MB/s bidirectional file transfers over Cat 5e with 3 patch points across ~80 ft — proving Cat 5e works at 10 Gig speeds when terminated properly. Key: keep untwisted pairs to ~1/4 inch at keystone jacks.

---

## KEY TOPICS

### Hardware
| Component | Cost | Detail |
|-----------|------|--------|
| Intel X540-T2 | ~$10 (eBay) | Dual-port 10GbE PCIe Gen 2 x8; needs at least x4 slot |
| Cat 5e (existing) | $0 | Already in walls — rated for 1 Gbps, works at 10 Gig |
| Mokerlink switch | ~$varies | 6-port 10GbE (4x RJ45, 2x SFP+) |
| Noctua fan | ~$5 | Replaces noisy/dead stock X540-T2 fan |

### Setup Process
1. Identify existing Cat 5e cabling in walls
2. Terminate properly with keystone jacks (B standard, ~1/4 inch untwisted pairs)
3. Trace cables with Klein probe tool
4. Install Intel X540-T2 in PCIe slot (min x4)
5. Install drivers: download "complete driver pack for Intel Ethernet adapters"
6. Test: achieved 800-900 MB/s over Cat 5e

### Key Technical Insight
- Cat 5e handles 10GbE in real-world conditions if terminated properly
- 60 ft run with 3 separate connections still achieved near line-rate speeds
- The shortfall from theoretical 1250 MB/s is SSD speed limits and Windows overhead, not the network

---

## TOOLS & HARDWARE MENTIONED

| Tool/Hardware | Purpose |
|---------------|---------|
| Intel X540-T2 | 10GbE network card |
| Klein probe tool | Cable tracing (800-1000 Hz tone) |
| Keystone jacks (toolless) | Permanent wall installations |
| Mokerlink 10GbE switch | Multi-device 10 Gig sharing |
| UGreen DXP6011 AIS NAS | 6-bay NAS (sponsor) |

---

## ACTIONABLE TAKEAWAYS

1. 10 Gigabit networking for ~$20 total if you have Cat 5e in walls
2. Proper cable termination is the key — keep untwisted pairs as short as possible
3. For direct NAS-to-PC: two X540-T2 cards + static IPs, no switch needed
4. Intel removed X540-T2 drivers from product page — download complete Intel Ethernet adapter driver pack

---

*Analysis derived from: I made my internet 10X FASTER for $10.txt*
