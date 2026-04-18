---
title: Edge homelab platform terms (k3s, Longhorn, backup)
page_type: glossary
status: active
created: 2026-04-17
updated: 2026-04-17
tags:
  - glossary
  - k3s
  - homelab
review_status: unreviewed
confidence: high
---

# Edge homelab platform terms (k3s, Longhorn, backup)

Short labels used in the **homelab / farm edge** stack pages:

| Term | One-line meaning |
|------|------------------|
| **k3s** | Lightweight **Kubernetes** on small fleets—**API** for workloads at the edge. |
| **Longhorn** | **Distributed block storage** (CSI) for **PVCs**—**not** a substitute for **PostgreSQL** logical backup. |
| **Central storage** | **NAS / object** **outside** the cluster for bulk files, **restic** targets, archives—often **hybrid** with Longhorn. |
| **etcd / volume / app backup** | **Three** different **DR** tracks—see [`Kubernetes platform backup / DR`](../analyses/kubernetes-platform-backup-dr-pi-k3s-longhorn.md). |

**See:** [`Platform doctrine package — homelab / farm edge`](../topics/platform-doctrine-package-homelab-farm-edge.md).
