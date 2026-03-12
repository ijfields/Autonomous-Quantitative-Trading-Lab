# This Kubernetes Homelab is a DevOps Job Magnet (2026) — Complete Transcript Analysis

**Video Title:** This Kubernetes Homelab is a DevOps Job Magnet (2026)
**Channel:** Mischa van den Burg
**Video ID:** S7sJA51CxIo
**Upload Date:** 2026-03-10
**Duration:** ~24m
**Speaker:** Mischa van den Burg
**Platform:** YouTube

---

## EXECUTIVE SUMMARY

A full walkthrough of Mischa van den Burg's 3-year-old Kubernetes homelab, designed as a deliberate career asset for DevOps roles. Covers two-cluster architecture (Mimir for stateful/data, Yotenheim for stateless/apps), Talos Linux as immutable OS, CloudNative-PG running 12 PostgreSQL clusters, Flux CD for GitOps, Cilium for eBPF networking, a quantified-self pipeline scraping Whoop/Oura/Strava into Grafana dashboards, and N8N automations including AI-powered PR auto-merging.

---

## KEY TOPICS

### Cluster Architecture

| Cluster | Purpose | Workloads |
|---------|---------|-----------|
| **Mimir** | Data/stateful | 12 PostgreSQL clusters (CloudNative-PG), Forgejo (self-hosted Git) |
| **Yotenheim** | Applications/stateless | All apps, serves as staging for infrastructure upgrades |

- Upgrades are applied to Yotenheim first, promoted to Mimir after validation

### K3S vs Talos Linux

| Feature | K3S | Talos Linux |
|---------|-----|-------------|
| **Best for** | Beginners | Advanced users |
| **Setup** | Simple, lightweight | Immutable OS, no SSH, API-only config |
| **ARM support** | Excellent (Raspberry Pi) | Yes |
| **Security** | Standard Linux | Completely hardened, no shell access |
| **Mischa's use** | First year | Past 2 years (current) |

### CloudNative-PG (12 PostgreSQL Clusters)

- Pushes back against "databases shouldn't run on Kubernetes" — calls it one of the most common K8s workloads
- Workflow: Apply YAML manifest → operator provisions multi-instance PostgreSQL with automatic S3 backups
- `cnpg` CLI plugin for health inspection, backup status, WAL archiving
- Each cluster exposed as external IP via Cilium load balancer IPAM
- Used professionally and in homelab for years

### Flux CD (GitOps)

- Manages entire homelab from Git — creates a public portfolio for hiring managers
- Uses Kustomizations + Helm releases
- CLI-driven: `flux get kustomizations`
- All infrastructure-as-code, version controlled

### Cilium (eBPF Networking)

- All-in-one CNI: load balancer IPAM, ingress, Gateway API
- Enterprise-grade, eBPF-based — used by major companies
- Single tool replaces multiple networking components

### Quantified Self Pipeline

```
Whoop / Oura Ring / Strava → CronJob Scrapers → PostgreSQL (CloudNative-PG) → Grafana Dashboards
```

- Kubernetes CronJobs scrape wearable APIs
- Data stored in self-hosted PostgreSQL on Mimir cluster
- SQL queries build Grafana dashboards: sleep, body composition, activity, cross-device comparisons
- Scraper code publicly available on GitHub

### N8N Automation Highlights

- **AI-powered GitHub PR auto-updater:** Runs hourly, scans open PRs, classifies risk level
  - Low-risk dependency updates → auto-merged
  - Critical infrastructure changes (e.g., Cilium upgrades) → writes assessment for manual review
- **AI-curated RSS content:** Multiple Miniflux instances, AI scoring algorithm rates articles for relevance, generates summaries

---

## HARDWARE

| Hardware | Notes |
|----------|-------|
| HP EliteDesk 800 G2 Mini (×6) | i5/16GB and i3/8GB variants, ~$100-150 each refurbished |
| Minisforum MS-A2 | 32GB RAM, more powerful but noisy |
| Lenovo ThinkPad T480 | Also added as a K8s node |
| Lenovo ThinkCentres | Another good refurbished option |
| Raspberry Pis | Learning only, not for heavy hosting |

---

## TOOLS & PLATFORMS MENTIONED

| Tool/Platform | Purpose |
|---------------|---------|
| Talos Linux | Immutable Kubernetes OS |
| K3S | Lightweight Kubernetes (beginner recommendation) |
| CloudNative-PG | PostgreSQL operator for Kubernetes |
| Flux CD | GitOps continuous delivery |
| Cilium | eBPF-based CNI, load balancer, ingress, Gateway API |
| Grafana + Prometheus | Monitoring and dashboards (kube-prometheus-stack) |
| Grafana Alertmanager | Alerting (preferred over Prometheus Alertmanager) |
| Uptime Kuma | Application uptime monitoring |
| Forgejo | Self-hosted Git server |
| N8N | Self-hosted automation workflows |
| Miniflux | RSS feed reader (multiple instances, AI-scored) |
| Audiobookshelf | Audiobook management + podcast archiving |
| Homepage | Self-hosted YAML-configured dashboard |
| Linkding | Self-hosted bookmark manager |
| Paperless-ngx | OCR document management |
| Wallabag | Self-hosted "read later" app |
| K9s | Terminal-based Kubernetes UI |
| Whoop / Oura Ring / Strava | Quantified self data sources |
| Dev Containers | Working exclusively inside containers |

---

## ACTIONABLE TAKEAWAYS

1. **Start with K3S** for beginners, migrate to Talos Linux once foundational skills are solid
2. **Use refurbished enterprise mini-PCs** ($100-150) — HP EliteDesk, Lenovo ThinkCentre are more than adequate
3. **Run databases on Kubernetes** with CloudNative-PG — production-grade, free, auto-backups to S3
4. **Separate stateful and stateless clusters** — use the stateless cluster as canary for upgrades
5. **Use GitOps (Flux CD)** so your entire homelab is a public portfolio for job applications
6. **Choose Cilium** for enterprise-relevant eBPF networking skills (single component for LB, ingress, Gateway API)
7. **Use Grafana Alertmanager** over Prometheus Alertmanager — "the industry has decided"
8. **Build a quantified-self pipeline** — practical project exercising CronJobs, API integration, SQL, dashboarding
9. **Automate infrastructure maintenance** with N8N + AI for PR classification and auto-merging
10. **Work inside dev containers** rather than installing tools on host
11. **Self-host your Git** (Forgejo) for data sovereignty
12. **Treat your homelab as a career asset**, not just a hobby

---

*Analysis derived from: This Kubernetes Homelab is a DevOps Job Magnet (2026).txt*
