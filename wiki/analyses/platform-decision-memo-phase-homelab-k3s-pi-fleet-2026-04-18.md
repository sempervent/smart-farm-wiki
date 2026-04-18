---
title: Platform decision memo — phase, HA scope, deferrals (Pi / k3s / Longhorn / Rancher)
page_type: analysis
status: active
created: 2026-04-18
updated: 2026-04-17
tags:
  - k3s
  - longhorn
  - rancher
  - raspberry-pi
  - governance
review_status: unreviewed
confidence: medium
aliases:
  - Homelab k3s platform phase memo 2026
---

# Platform decision memo — phase, HA scope, deferrals (Pi / k3s / Longhorn / Rancher)

## Purpose

Decision memo for the smart-farm-wiki homelab/edge Kubernetes platform: what belongs in Phase 0/1, what is deferred, what “HA” means in this repo, and what must not be overbuilt before workload truth (farmOS, telemetry) exists.

**Doctrine package** (first-class hub): [`Platform doctrine package — homelab / farm edge`](../topics/platform-doctrine-package-homelab-farm-edge.md).

**Canonical stack doc**: [`Platform strategy for farm and homestead services`](homelab-edge-kubernetes-platform-strategy-pi-k3s-longhorn-rancher.md).

**HA semantics** (expanded): [`HA meaning and constraints — homelab / farm platform`](ha-meaning-and-constraints-homelab-farm-platform.md). **Component roles**: [`k3s role`](k3s-role-in-homelab-farm-platform.md), [`Longhorn role`](longhorn-role-in-homelab-farm-platform.md).

---

## Phase 0/1 (pilot-ready)

**In scope**

- **1–3** Pi-class nodes: **one** k3s server + agents per [`k3s quick-start`](../../raw/processed/2026/k3s-quick-start-guide-docs-capture-inbox-2026-04-18.md)—embedded datastore acceptable for non-life-safety lab use.
- **Longhorn** trial only if iSCSI + disk plan are ready ([`Longhorn CSI on K3s`](../../raw/processed/2026/longhorn-csi-on-k3s-docs-capture-inbox-2026-04-18.md)); otherwise local-path or hostPath spikes (throwaway).
- **One** stateful pilot: farmOS or broker + DB—with logical backup proven ([`Backup strategy comparison`](backup-strategy-comparison-farmos-homelab-postgresql-containers.md)).
- **Documentation**: tokens, kubeconfig hygiene, hostname uniqueness ([`Pi fleet provisioning standard`](raspberry-pi-fleet-provisioning-standard-smart-farm-homelab.md)).

**Out of scope for 0/1**

- **Rancher** by default ([`Rancher role and timing`](rancher-role-and-timing-k3s-homelab-farm-platform.md)).
- Multi-server etcd HA without a written restore drill.
- GitOps multi-cluster unless you already have more than one cluster to operate.

---

## Deferred (until justified)

| Item | Defer until |
|------|-------------|
| k3s HA control plane (3+ servers) | Uptime need exceeds maintenance windows you can tolerate; read [HA embedded etcd](https://docs.k3s.io/datastore/ha-embedded) and test failover |
| Rancher | More than one cluster to operate, or explicit need for catalog / CD ([`Rancher role and timing`](rancher-role-and-timing-k3s-homelab-farm-platform.md)) |
| Longhorn as default for every workload | I/O and CPU cost understood on Pi; central NAS may win for bulk ([`Longhorn vs central storage`](longhorn-vs-central-storage-architecture-homelab-farm-platform.md)) |
| Service mesh, complex ingress tiers | Ten microservices you do not have yet |

---

## What “HA” means in this repository

| Term | Meaning | Not implied |
|------|---------|-------------|
| **k3s HA** | Multiple server nodes + quorum datastore per k3s docs ([`architecture`](../../raw/processed/2026/k3s-architecture-docs-capture-inbox-2026-04-18.md)) | Multi-region; zero RPO for farm records without app-level backup |
| **Longhorn replication** | Survive node/disk loss on the same farm LAN | Geographic DR; ransomware immutability (needs object-lock / air-gap policy) |
| **Central NAS “HA”** | Vendor appliance feature set | Kubernetes SLO unless integrated as PV backend |

**Full doctrine**: [`HA meaning and constraints — homelab / farm platform`](ha-meaning-and-constraints-homelab-farm-platform.md).

---

## Anti-patterns (do not overbuild)

1. **Kubernetes** for a single static container on one Pi—use **Docker Compose** first when appropriate ([`farmOS Docker capture`](../../raw/processed/2026/farmos-docker-developing-hosting-capture-inbox-2026-04-17.md) is a lighter-weight pattern for dev).
2. **Longhorn** before stable k3s + disk + iSCSI—debug the base cluster first ([`CSI on K3s`](../../raw/processed/2026/longhorn-csi-on-k3s-docs-capture-inbox-2026-04-18.md)).
3. **Rancher** before you can restore etcd / PVC—the dashboard is not a backup.

---

## Related

- [`Platform doctrine package — homelab / farm edge`](../topics/platform-doctrine-package-homelab-farm-edge.md)
- [`Two-site smart farm operations`](../topics/two-site-smart-farm-operations.md)
- [`Kubernetes platform backup / DR`](kubernetes-platform-backup-dr-pi-k3s-longhorn.md)
