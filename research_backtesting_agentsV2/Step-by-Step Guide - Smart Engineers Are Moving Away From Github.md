# Step-by-Step Guide: Self-Hosting Git with Forgejo

**Source:** Mischa van den Burg (YouTube)
**Video ID:** pAQqkI0xMu4
**Upload Date:** 2026-03-03

---

## What This Guide Covers

How to replace GitHub with self-hosted Forgejo for full code sovereignty, including CI/CD pipelines, container registry, and repository mirroring.

---

## Step 1: Deploy Forgejo

Single command:
```bash
podman run -p 3000:3000 -p 2222:22 -v forgejo-data:/data forgejo/forgejo
```
(Replace `podman` with `docker` if preferred.)

- Web UI: `http://localhost:3000`
- SSH: port 2222
- Install wizard completes in seconds

---

## Step 2: Configure CI/CD (Actions Runner)

1. Forgejo includes a built-in Actions runner compatible with GitHub Actions syntax
2. Set up pipelines that trigger on commits/PRs
3. Example pipeline: checkout → build container image → push to Forgejo container registry → deploy via GitOps

---

## Step 3: Set Up Repository Mirroring

1. Navigate to Settings → Mirror in your Forgejo instance
2. Add public GitHub repository URLs you want to mirror
3. Forgejo periodically pulls full commit history
4. Maintains local backup even if original is taken down

---

## Step 4: Migrate Existing Repos

1. Clone your GitHub repos locally
2. Add Forgejo as a new remote
3. Push to Forgejo
4. Optionally keep GitHub as a secondary mirror

---

## Key Takeaway

> Self-hosting Git with Forgejo takes a single command and provides a complete GitHub-equivalent workflow: hosting, CI/CD, container registry, and repo mirroring. Your code stays under your control, free from AI training scanning and corporate pricing changes.

*Guide derived from: Smart Engineers Are Moving Away From Github, Here's Why..#.txt*
