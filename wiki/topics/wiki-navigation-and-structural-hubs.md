---
title: Wiki navigation and structural hubs
page_type: topic
status: active
created: 2026-04-17
updated: 2026-04-17
review_status: unreviewed
tags:
  - meta
  - navigation
  - information-architecture
---

# Wiki navigation and structural hubs

**Purpose**: Reduce **flat-list** fatigue in [`index.md`](../index.md) by naming **where to start** for **meta/IA**, **two-site operations**, **homelab edge**, and **audits**. This page is a **router**, not a duplicate of every analysis.

**IA policy & debt**: [`Structural debt audit — wiki IA and operational maturity`](../analyses/structural-debt-audit-wiki-ia-and-operational-maturity.md) · [`AGENTS.md`](../../AGENTS.md) (canonicalization, `page_subtype`, `operational_maturity`).

---

## Backup / disaster recovery

| Page | Use when |
|------|----------|
| [`Backup and disaster recovery package — smart farm stack`](../analyses/backup-and-disaster-recovery-package-smart-farm-stack.md) | **DR spine**: farmOS, PostgreSQL, k3s, Longhorn, Rancher, secrets, edge scope |
| [`Runbook — backup validation and recovery drill`](../analyses/runbook-backup-validation-and-recovery-drill.md) | Restore-tested drills |

---

## Meta, audits, and steering

| Page | Use when |
|------|----------|
| [`Domain content overview`](../analyses/domain-content-overview.md) | Strand map, maturity matrix, backlog |
| [`Repository analysis`](../analyses/repository-analysis.md) | Repo layout, CI, MkDocs, validation |
| [`Structural audit — repository shape and canonical routing`](../analyses/structural-audit-repository-and-canonical-routing.md) | Merge policy, index IA |
| [`Structural audit — page ownership, entity gaps, and hub routing`](../analyses/structural-audit-page-ownership-entity-gaps-and-hub-routing.md) | **Anti–analysis-swarm** ownership map |
| [`Structural debt audit — wiki IA and operational maturity`](../analyses/structural-debt-audit-wiki-ia-and-operational-maturity.md) | Sprawl diagnosis, ops maturity taxonomy |
| [`Execution readiness gap audit — East Tennessee`](../analyses/execution-readiness-gap-audit-east-tennessee-operational-knowledge.md) | ET execution evidence gaps |

---

## Two-site smart farm (East Tennessee package)

| Page | Role |
|------|------|
| [`Two-site smart farm operations`](two-site-smart-farm-operations.md) | **Main hub**: business plan links, telemetry, runbooks, ownership table |
| [`East Tennessee two-site farm business plan (package)`](../business-plan/east-tennessee-two-site-farm-business-plan.md) | Reading order spine |
| [`Reference architecture — 5 ac + 120 ac`](../analyses/reference-architecture-5ac-homebase-120ac-smart-farm.md) | Architecture package map |
| [`Execution dossier — Phase 0–1 (hub)`](../analyses/execution-dossier-hub-phase-0-1-east-tennessee.md) | Pilot execution entry |

---

## Homelab / edge Kubernetes (Pi, k3s, Longhorn)

| Page | Role |
|------|------|
| [`Homelab / edge Kubernetes platform strategy`](../analyses/homelab-edge-kubernetes-platform-strategy-pi-k3s-longhorn-rancher.md) | Canonical stack narrative |
| [`How to provision k3s, Longhorn, and Rancher on a Raspberry Pi fleet`](../analyses/how-to-provision-k3s-longhorn-and-rancher-on-a-raspberry-pi-fleet.md) | **Operational guide hub** (`page_subtype: operational_guide`) |
| [`Docker, Kubernetes, Compose, and Bake`](docker-kubernetes-compose-and-bake.md) | Distro / compose context |

---

## Runbooks and degraded modes (two-site)

| Page | Role |
|------|------|
| [`Automation degraded modes and manual fallback SOP`](../analyses/automation-degraded-modes-manual-fallback-sop.md) | Parent SOP |
| [`Manual fallback and degraded modes — critical operations`](../analyses/manual-fallback-degraded-modes-critical-operations.md) | Scenario matrix |
| [`Runbook — broker or backhaul down`](../analyses/runbook-broker-or-backhaul-down.md) | MQTT / uplink |
| [`Runbook — power loss at remote site`](../analyses/runbook-power-loss-remote-site.md) | Field hub power |

---

## Full catalog

The authoritative **flat** list remains [`index.md`](../index.md) (required for validation and discoverability). Use this hub to **choose a lane** first.
