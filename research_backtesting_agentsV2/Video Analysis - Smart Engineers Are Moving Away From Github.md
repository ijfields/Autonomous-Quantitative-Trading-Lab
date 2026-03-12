# Smart Engineers Are Moving Away From Github, Here's Why... — Complete Transcript Analysis

**Video Title:** Smart Engineers Are Moving Away From Github, Here's Why...
**Channel:** Mischa van den Burg
**Video ID:** pAQqkI0xMu4
**Upload Date:** 2026-03-03
**Duration:** ~17m
**Speaker:** Mischa van den Burg
**Platform:** YouTube

---

## EXECUTIVE SUMMARY

Mischa van den Burg argues engineers should self-host Git infrastructure to retain code sovereignty. Microsoft/GitHub scans all repos (including private) for AI training, attempted to charge for self-hosted Actions runners (reversed after backlash), and centralized ownership means takedown risk. Forgejo (fork of Gitea, used by Codeberg and Dutch government) provides a complete GitHub-equivalent workflow: Git hosting, CI/CD with Actions runners, container registry, and repo mirroring — deployable with a single `podman run` command.

---

## KEY TOPICS

### Why Leave GitHub

| Concern | Detail |
|---------|--------|
| **AI training** | Microsoft scans all code (including private repos) for AI model training |
| **Pricing risk** | Attempted to charge for self-hosted Actions runners (Dec 15 announcement, reversed after backlash) |
| **Takedown risk** | Centralized platform = repos can disappear from lawsuits/takedowns |
| **Data sovereignty** | No control over how your code is used or monetized |

### Forgejo (Chosen Alternative)

- Fork of Gitea (which was commercialized after acquisition)
- "Guaranteed 100% free and open-source software forever"
- Used by **Codeberg** (nonprofit community-led GitHub alternative)
- **Dutch government** interested in adopting
- UI closely mirrors GitHub: commits, PRs, code browsing

### Self-Hosting Setup

- Single command: `podman run` (or `docker run`) exposing ports 3000 (web) and 2222 (SSH)
- Install wizard takes seconds
- Includes built-in **Actions runner** (CI/CD) for pipelines
- Built-in **container registry**
- **Repository mirroring**: periodically pulls public GitHub repos as local backup

### Alternatives Considered

| Alternative | Verdict |
|-------------|---------|
| **GitLab** | Feature-rich but overkill for personal use, complex to self-host on K8s |
| **Gitea** | Open source but acquired/commercialized, sparking Forgejo fork |

---

## TOOLS & PLATFORMS MENTIONED

| Tool/Platform | Purpose |
|---------------|---------|
| Forgejo | Self-hosted Git server (chosen) |
| Codeberg | Nonprofit GitHub alternative running on Forgejo |
| GitLab | Enterprise alternative (considered, rejected) |
| Gitea | Original project before Forgejo fork |
| Podman / Docker | Container runtime for deployment |
| Kubernetes | Hosting infrastructure |

---

## ACTIONABLE TAKEAWAYS

1. **Self-host Git for data sovereignty** — especially if you have private projects or proprietary code
2. **Forgejo is the recommended alternative** — single-command setup, full CI/CD, container registry
3. **Repository mirroring** preserves copies of public GitHub repos locally
4. **GitLab is overkill for individuals** — Forgejo is simpler and sufficient
5. **The pricing risk is real** — GitHub has shown willingness to monetize previously free features

---

*Analysis derived from: Smart Engineers Are Moving Away From Github, Here's Why..#.txt*
