---
title: Operational standards — farm and homelab platform
page_type: topic
status: active
created: 2026-04-24
updated: 2026-04-25
tags:
  - standards
  - operations
  - k3s
  - homelab
  - two-site
review_status: unreviewed
confidence: high
---

# Operational standards — farm and homelab platform

**Purpose**: **One catalog** for **repeatable** **operator** **norms** on the **farm edge / homelab** stack (Pi, k3s, Longhorn, telemetry) and **two-site** **network** **roles**—**without** replacing procedural runbooks. **Rule**: standards state **what must be true**; **guides** state **how to do it step-by-step**. **Guide policy** (location, maturity, linking): [`Procedural guides package strategy — Smart Farm Wiki`](procedural-guides-package-strategy-smart-farm-wiki.md).

**Doctrine**: [`Platform doctrine package — homelab / farm edge`](platform-doctrine-package-homelab-farm-edge.md) · [`Backup and disaster recovery — doctrine hub`](backup-disaster-recovery-doctrine-hub.md) · [`Off-grid power and field networking hub`](off-grid-power-and-field-networking-hub.md).

---

## Homelab / Kubernetes edge

| Standard | Covers |
|----------|--------|
| [`Raspberry Pi fleet provisioning standard — smart farm / homelab`](../analyses/raspberry-pi-fleet-provisioning-standard-smart-farm-homelab.md) | OS, disk, iSCSI, hostname, join hygiene |
| [`k3s cluster bootstrap standard — smart farm / homelab`](../analyses/k3s-cluster-bootstrap-standard-smart-farm-homelab.md) | Bootstrap order, prerequisites pointer, phase gates |
| [`Kubernetes edge — scheduling, storage class, and Longhorn roles standard`](../analyses/kubernetes-edge-scheduling-storage-longhorn-standard.md) | Labels, taints, **StorageClass** defaults, Longhorn placement |
| [`Secrets and certificates — edge cluster standard`](../analyses/secrets-and-certificates-edge-cluster-standard.md) | No plain secrets in Git, rotation, break-glass |
| [`Observability, secrets, and trust bar — homelab / farm edge`](../analyses/observability-secrets-and-trust-bar-homelab-farm-edge.md) | Alert **philosophy**, **SOPS/Flux** context, **remote** **trust** bar (pairs with secrets + monitoring standards) |
| [`Monitoring and logging expectations — edge cluster standard`](../analyses/monitoring-and-logging-expectations-edge-cluster-standard.md) | Minimum observability bar (metrics/logs) |
| [`Backup validation cadence — farm stack standard`](../analyses/backup-validation-cadence-standard-farm-stack.md) | How often to **prove** restores |

---

## Field telemetry and WAN

| Standard | Covers |
|----------|--------|
| [`Field node identity and naming standard`](../analyses/field-node-identity-and-naming-standard.md) | Stable IDs, **G/R/S/H/W** alignment |
| [`Gateway naming and role assignment standard`](../analyses/gateway-naming-and-role-assignment-standard.md) | RF telemetry vs WAN edge naming |
| [`Site-to-site network role boundaries standard`](../analyses/site-to-site-network-role-boundaries-standard.md) | **SITE_HOME** / **SITE_FARM**, zones, trust |

---

## Related

- [`Wiki navigation and structural hubs`](wiki-navigation-and-structural-hubs.md)
- [`Two-site smart farm operations`](two-site-smart-farm-operations.md)
- [`How to provision k3s, Longhorn, and Rancher on a Raspberry Pi fleet`](../analyses/how-to-provision-k3s-longhorn-and-rancher-on-a-raspberry-pi-fleet.md) — **runbook** (not a standard)
