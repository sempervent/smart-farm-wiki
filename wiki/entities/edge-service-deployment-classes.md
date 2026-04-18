---
title: Edge service deployment classes — pilot vs production
page_type: entity
status: active
created: 2026-04-23
updated: 2026-04-23
tags:
  - platform
  - pilot
  - automation
  - k3s
aliases:
  - Observe-only phase automation
confidence: medium
review_status: unreviewed
---

# Edge service deployment classes — pilot vs production

## Purpose

Vocabulary for **how hard** a service is committed: **recon / pilot** (minimal blast radius, may be torn down), **production** (coverage/backup expectations apply), and **deferred** (explicitly not running yet)—aligned with **automation stop rules** and **platform** phase memos.

## Scope

- **In scope**: Definitions and routing to doctrine; **not** a substitute for the **stop-rules** tables.
- **Out of scope**: Service catalog hostnames or versions.

## Knowns

- Phase **0–1** defaults include **observational-only** automation postures in the two-site **stop rules** analysis.
- **HA** “meaning” for the homelab/farm platform is constrained—see HA analysis.

## Assumptions

- Promoting a workload from **pilot** to **production** triggers **backup**, **access**, and **runbook** requirements—see DR package.

## Related analyses

- [`Platform decision memo — phase, HA scope, deferrals`](../analyses/platform-decision-memo-phase-homelab-k3s-pi-fleet-2026-04-18.md)
- [`Automation stop rules — two-site smart farm`](../analyses/automation-stop-rules-two-site-smart-farm.md)
- [`HA meaning and constraints — homelab / farm platform`](../analyses/ha-meaning-and-constraints-homelab-farm-platform.md)
- [`How to provision k3s, Longhorn, and Rancher on a Raspberry Pi fleet`](../analyses/how-to-provision-k3s-longhorn-and-rancher-on-a-raspberry-pi-fleet.md)

## Related source notes

- [`k3s-longhorn-rancher-pi-platform-official-captures`](../source-notes/k3s-longhorn-rancher-pi-platform-official-captures-inbox-2026-04-18.md)

## Outstanding unknowns

- **Explicit** service list with **pilot vs prod** flag per workload (operator registry—not in wiki by default).
