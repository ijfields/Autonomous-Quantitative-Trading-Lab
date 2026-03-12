# Step-by-Step Guide: Building a Career-Grade Kubernetes Homelab (2026)

**Source:** Mischa van den Burg (YouTube)
**Video ID:** S7sJA51CxIo
**Upload Date:** 2026-03-10

---

## What This Guide Covers

How to build a Kubernetes homelab that doubles as a career asset for DevOps roles — including hardware selection, cluster architecture, database management, GitOps, monitoring, and self-hosted applications.

---

## Prerequisites

- Budget of $200-$600 for refurbished hardware (2-6 mini-PCs)
- Basic Linux command-line familiarity
- Willingness to learn Kubernetes fundamentals

---

## Step 1: Acquire Hardware

1. Buy 2-6 refurbished enterprise mini-PCs:
   - **HP EliteDesk 800 G2 Mini** (i5/16GB RAM) — ~$100-150 each
   - **Lenovo ThinkCentre** — similar price range
   - Or any mix of what you can find (even a ThinkPad laptop works)
2. Raspberry Pis are fine for learning but not recommended for hosting real workloads
3. You do NOT need rack servers — mini-PCs are quiet, cheap, and sufficient

---

## Step 2: Choose Your Kubernetes Distribution

### For Beginners: K3S
- Lightweight, simple setup, excellent ARM support
- Run: `curl -sfL https://get.k3s.io | sh -`
- Use for your first ~12 months

### For Advanced Users: Talos Linux
- Immutable OS purpose-built for Kubernetes
- No SSH — configured entirely via Talos API
- "Super secure" and completely hardened
- Migrate to this after you're comfortable with Kubernetes fundamentals

---

## Step 3: Design Two-Cluster Architecture

| Cluster | Purpose | What Runs Here |
|---------|---------|----------------|
| **Data cluster** (stateful) | Databases, Git server | PostgreSQL (CloudNative-PG), Forgejo |
| **App cluster** (stateless) | All applications | Apps, monitoring, automation |

- Apply infrastructure upgrades to the app cluster first
- Promote to data cluster only after validation

---

## Step 4: Deploy PostgreSQL with CloudNative-PG

1. Install the CloudNative-PG operator on your data cluster
2. Apply a YAML manifest to provision a PostgreSQL cluster
3. The operator handles: multi-instance setup, automatic backups to S3, WAL archiving
4. Use `cnpg` CLI plugin to inspect cluster health
5. Expose each database cluster as an external IP via Cilium load balancer IPAM

---

## Step 5: Set Up GitOps with Flux CD

1. Install Flux CD on both clusters
2. Point Flux at your Git repository containing all Kubernetes manifests
3. Use Kustomizations + Helm releases to manage deployments
4. Everything deployed from Git = your public portfolio for hiring managers
5. Monitor with `flux get kustomizations`

---

## Step 6: Configure Networking with Cilium

1. Install Cilium as your CNI (replaces default networking)
2. Configure as all-in-one: load balancer IPAM, ingress controller, Gateway API
3. Benefit: single tool replaces multiple networking components
4. eBPF-based = enterprise-grade, in-demand skill

---

## Step 7: Deploy Monitoring Stack

1. Install **kube-prometheus-stack** (Grafana + Prometheus)
2. Use **Grafana Alertmanager** for alerts (preferred over Prometheus Alertmanager)
3. Add **Uptime Kuma** for application uptime monitoring
4. Send alerts to Telegram for instant notifications

---

## Step 8: Self-Host Applications

Priority applications to deploy:

| App | Purpose |
|-----|---------|
| **Forgejo** | Self-hosted Git (mirrors GitHub repos) |
| **N8N** | Automation workflows |
| **Miniflux** | RSS reader (with AI scoring) |
| **Paperless-ngx** | OCR document management |
| **Homepage** | YAML-configured dashboard portal |
| **Audiobookshelf** | Audiobook + podcast management |
| **Linkding** | Bookmark manager |
| **Wallabag** | "Read later" article archiving |

---

## Step 9: Build a Quantified Self Pipeline (Optional but Impressive)

1. Wear a **Whoop** and/or **Oura Ring**, track activity with **Strava**
2. Create Kubernetes CronJobs that scrape wearable APIs
3. Store data in PostgreSQL (on your data cluster via CloudNative-PG)
4. Build Grafana dashboards: sleep, body composition, activity, cross-device comparisons
5. This project exercises: CronJobs, API integration, SQL, dashboarding

---

## Step 10: Automate with AI (Advanced)

1. Use N8N to build an **AI-powered PR auto-updater**:
   - Runs hourly, scans open GitHub PRs
   - Auto-merges low-risk dependency updates
   - Writes assessment for critical changes (manual review)
2. Build an **AI-curated RSS pipeline**:
   - Multiple Miniflux instances
   - AI scoring algorithm rates articles for relevance
   - Generates summaries with key takeaways

---

## Key Takeaway

> A Kubernetes homelab is not just a hobby — it's a demonstrable career asset. Refurbished enterprise mini-PCs ($100-150 each) running K3S or Talos with CloudNative-PG, Flux CD, and Cilium creates production-grade infrastructure that hiring managers respect. Make everything GitOps so your public repository IS your portfolio.

*Guide derived from: This Kubernetes Homelab is a DevOps Job Magnet (2026).txt*
