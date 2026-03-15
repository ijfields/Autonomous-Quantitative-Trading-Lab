# I Built an AI Agent Army with Openclaw to Make 1M/year — Complete Transcript Analysis

**Video Title:** I Built an AI Agent Army with Openclaw to Make 1M/year
**Channel:** Dubibubii
**Video ID:** 3hgXhB_Wy2U
**Upload Date:** 2026-02-28
**Duration:** ~14m
**Speaker:** Doobie (Dubibubii)
**Platform:** YouTube

---

## EXECUTIVE SUMMARY

Doobie describes his autonomous "App Factory" — a system of 11 AI agents managed by OpenClaw agent "Sheldon" that builds, tests, monetizes, and submits iOS apps to the App Store around the clock. The system built 7 apps in a single afternoon using less than 5% of OpenClaw's context window. He reports $46,000 generated in one month with 10,000+ followers. The key breakthrough was solving context bloat by building infrastructure in Claude Code and having OpenClaw just orchestrate.

---

## KEY TOPICS

### The 9-Step App Pipeline

| Step | What Happens | Model Used |
|------|-------------|-----------|
| 1. Research | Scans Reddit/X for pain points and complaints | — |
| 2. Idea Validation | Cross-references App Store for high demand / low competition | — |
| 3. One-Pager | Documents research, pain points, target user, monetization | — |
| 4. Building | Writes all Swift/SwiftUI code from single prompt | Claude Opus 4.6 |
| 5. Code Review | Independent review for crashes, missing features, bugs | Codex 5.3 |
| 6. Quality Gates | 6 checks, scored out of 10, must score 8+ to proceed | — |
| 7. Monetization | Chooses free trial or premium model via Apple StoreKit | — |
| 8. App Store Packaging | Description, keywords, screenshots, icon (Nano Banana Pro), onboarding | — |
| 9. Submission | Queued in batches (Apple limits 5 in review per account) | — |

### Context Bloat Solution (3 Failed Attempts)
1. Used OpenClaw for everything → context full in 2 days
2. Stripped to only building apps → one iOS app consumed entire context
3. **Success:** Built infrastructure in Claude Code, OpenClaw (Sheldon) just orchestrates, sub-agents manage their own context

### The 4 Models Used
- **Claude Opus 4.6:** Builder (writes Swift/SwiftUI code)
- **Codex 5.3:** Reviewer (independent code quality verification)
- **Gemini Flash:** Powers AI features inside the apps
- **Sonnet 4.6:** Fast routing, logging, metadata, quick decisions

### Market Context
- Global app market: $300B/year, 14% annual growth, expected $1T by 2035
- 1.4 billion iPhone users, only 2 million apps
- Example revenue: "make you taller" app = $90K/month; snoring recorder = $400K/month
- Case studies: James (30 apps, $60K/month), David (58 failed apps, 59th = Widget Smith, 131M downloads, $200K/month)

### Marketing Pipeline (Planned)
- Multiple TikTok/Instagram accounts across content categories
- AI generates native content autonomously
- Uses Larry skill (Oliver Henry) — generated 8M views in one week via autonomous TikTok slideshows
- Votion generates demo/promo videos inside Claude Code

---

## TOOLS & PLATFORMS

| Tool | Purpose |
|------|---------|
| OpenClaw | Orchestrator ("Sheldon") |
| Claude Code | Infrastructure builder |
| Claude Opus 4.6 | App code generation |
| Codex 5.3 | Independent code review |
| Gemini Flash | In-app AI features |
| Sonnet 4.6 | Fast routing/decisions |
| Apple StoreKit | Payment processing (15% cut via small business program) |
| Nano Banana Pro | AI icon generation |
| Votion | Demo video generation |
| Larry skill | Autonomous TikTok slideshow agent |

---

## KEY TAKEAWAY

> "Don't rely on conversation history for important state. Always write it to files." The critical architectural insight: build infrastructure in Claude Code and have OpenClaw orchestrate from the top using sub-agents that manage their own context. Use separate models for building (Opus 4.6) vs reviewing (Codex 5.3) to avoid bias. Quality gates (score 8+/10, 3 failures = human escalation) prevent shipping broken apps. The factory runs on ~$1,000/month in AI tokens.

*Analysis derived from: I Built an AI Agent Army with Openclaw to Make 1M⧸year.txt*
