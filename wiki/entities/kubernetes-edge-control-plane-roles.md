---
title: Kubernetes edge control-plane roles — k3s / etcd / management
page_type: entity
status: active
created: 2026-04-23
updated: 2026-04-23
tags:
  - k3s
  - kubernetes
  - etcd
  - rancher
  - edge
aliases:
  - k3s control plane farm edge
confidence: medium
review_status: unreviewed
---

# Kubernetes edge control-plane roles — k3s / etcd / management

## Purpose

Stable names for **cluster control** on the **farm edge** stack: **k3s** server (API + **embedded etcd** in typical single-server patterns), **agents**, **Longhorn** control/data plane components as **storage** roles, and **Rancher** (if deployed) as **multi-cluster management**—distinct from **application** workloads (farmOS, brokers).

## Scope

- **In scope**: Role boundaries and **backup** implications at a high level (etcd vs app data).
- **Out of scope**: Cluster endpoint URLs, certificate SANs, or node hostnames.

## Knowns

- k3s and Longhorn **roles** are documented in dedicated analyses; **DR** package maps **three tracks** (app / Longhorn / etcd).
- Rancher’s **timing** and **scope** are explicitly debated (see Rancher role analysis).

## Assumptions

- **etcd** recovery without **logical** app backups does not restore farm records—see restore tiers.

## Related analyses

- [`k3s role in the homelab / farm platform`](../analyses/k3s-role-in-homelab-farm-platform.md)
- [`Longhorn role in the homelab / farm platform`](../analyses/longhorn-role-in-homelab-farm-platform.md)
- [`Rancher role and timing — k3s homelab / farm platform`](../analyses/rancher-role-and-timing-k3s-homelab-farm-platform.md)
- [`Kubernetes platform backup / DR — Pi fleet, k3s, Longhorn`](../analyses/kubernetes-platform-backup-dr-pi-k3s-longhorn.md)
- [`How to provision k3s, Longhorn, and Rancher on a Raspberry Pi fleet`](../analyses/how-to-provision-k3s-longhorn-and-rancher-on-a-raspberry-pi-fleet.md)

## Related source notes

- [`k3s-longhorn-rancher-pi-platform-official-captures`](../source-notes/k3s-longhorn-rancher-pi-platform-official-captures-inbox-2026-04-18.md)
- [`Backup / DR — official documentation cluster`](../source-notes/backup-dr-official-documentation-cluster.md)

## Outstanding unknowns

- **Multi-server** k3s topology vs **single-server** pilot default for your fleet (decision memo captures tradeoffs—not a single answer here).
