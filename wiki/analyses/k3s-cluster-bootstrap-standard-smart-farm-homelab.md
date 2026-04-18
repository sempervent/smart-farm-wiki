---
title: k3s cluster bootstrap standard — smart farm / homelab
page_type: analysis
page_subtype: standard
operational_maturity: pilot_ready
status: active
created: 2026-04-24
updated: 2026-04-24
tags:
  - k3s
  - bootstrap
  - standards
review_status: reviewed
confidence: high
---

# k3s cluster bootstrap standard — smart farm / homelab

## Purpose

**Canonical expectations** for **ordering** and **gates** when bringing up a **k3s** cluster that may host **farmOS**, **Longhorn**, and **edge** workloads—**not** a duplicate of the full runbook.

**Runbook (procedure)**: [`How to provision k3s, Longhorn, and Rancher on a Raspberry Pi fleet`](how-to-provision-k3s-longhorn-and-rancher-on-a-raspberry-pi-fleet.md). **Node checklist**: [`Raspberry Pi fleet provisioning standard — smart farm / homelab`](raspberry-pi-fleet-provisioning-standard-smart-farm-homelab.md).

---

## Standard (must hold)

| # | Requirement | Rationale |
|---|-------------|-----------|
| 1 | **One** documented **bootstrap** sequence per environment (lab vs prod)—no ad-hoc re-installs without updating docs | Reproducible recovery |
| 2 | **Server** before **agents**; **kubeconfig** and **join token** handled as **secrets** ([`Secrets and certificates — edge cluster standard`](secrets-and-certificates-edge-cluster-standard.md)) | k3s join contract |
| 3 | **Longhorn** only after **nodes** meet **iSCSI** + **disk** prerequisites per Pi standard | CSI prerequisites |
| 4 | **StorageClass** and **default** policy agreed before **stateful** workloads ([`Kubernetes edge — scheduling, storage…`](kubernetes-edge-scheduling-storage-longhorn-standard.md)) | Avoid PVC churn |
| 5 | **Backup** tracks (logical DB + etcd path) **named** before declaring “production” ([`Backup validation cadence`](backup-validation-cadence-standard-farm-stack.md)) | Empty clusters are not success |

**Phase alignment**: Phase 0/1 stays **single-server** k3s unless [`Platform decision memo`](platform-decision-memo-phase-homelab-k3s-pi-fleet-2026-04-18.md) justifies HA.

---

## Related

- [`Platform doctrine package — homelab / farm edge`](../topics/platform-doctrine-package-homelab-farm-edge.md)
- [`Operational standards — farm and homelab platform`](../topics/operational-standards-farm-homelab-platform.md)
