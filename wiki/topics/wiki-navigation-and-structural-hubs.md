---
title: Wiki navigation and structural hubs
page_type: topic
status: active
created: 2026-04-17
updated: 2026-04-24
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

## Operational standards (farm & homelab)

| Page | Use when |
|------|----------|
| [`Operational standards — farm and homelab platform`](operational-standards-farm-homelab-platform.md) | **Catalog** of Pi, k3s, storage, secrets, backup cadence, field naming, gateways, site boundaries |
| [`Raspberry Pi fleet provisioning standard — smart farm / homelab`](../analyses/raspberry-pi-fleet-provisioning-standard-smart-farm-homelab.md) | **Every node** checklist |
| [`Kubernetes edge — scheduling, storage class, and Longhorn roles standard`](../analyses/kubernetes-edge-scheduling-storage-longhorn-standard.md) | Labels, defaults, taints |
| [`Site-to-site network role boundaries standard`](../analyses/site-to-site-network-role-boundaries-standard.md) | Zones, **SITE_*** roles, WAN vs local |

---

## Procedural guides (how-tos and runbooks)

| Page | Use when |
|------|----------|
| [`Procedural guides package strategy — Smart Farm Wiki`](procedural-guides-package-strategy-smart-farm-wiki.md) | **Contract**: where guides live (`analyses/`), **vs** standards/essays, **`operational_maturity`**, required **links** (architecture, standards, entities) |
| [`How to provision k3s, Longhorn, and Rancher on a Raspberry Pi fleet`](../analyses/how-to-provision-k3s-longhorn-and-rancher-on-a-raspberry-pi-fleet.md) | **Guide hub** — Pi edge stack bootstrap sequence (`page_subtype: operational_guide`) |
| [`Backup and disaster recovery package — smart farm stack`](../analyses/backup-and-disaster-recovery-package-smart-farm-stack.md) | **DR doctrine spine** — operator routing across backup tracks |
| [`Runbook — backup validation and recovery drill`](../analyses/runbook-backup-validation-and-recovery-drill.md) | Example **incident/drill** runbook (`runbook-*.md`) |

**Incident runbooks** (degraded mode): [`Runbook — broker or backhaul down`](../analyses/runbook-broker-or-backhaul-down.md), [`Runbook — power loss at remote site`](../analyses/runbook-power-loss-remote-site.md), [`Runbook — sensor false-positive alert triage`](../analyses/runbook-sensor-false-positive-alert-triage.md), [`Runbook — manual fallback irrigation, gates, pumps`](../analyses/runbook-manual-fallback-irrigation-gates-pumps.md).

---

## Five package hubs (start here for “whole topics”)

| Hub | Use when |
|-----|----------|
| [`Platform doctrine package — homelab / farm edge`](platform-doctrine-package-homelab-farm-edge.md) | k3s / Longhorn / Rancher / Pi **doctrine** and provisioning pointers |
| [`Backup and disaster recovery — doctrine hub`](backup-disaster-recovery-doctrine-hub.md) | farmOS / Postgres / etcd / Longhorn **backup and restore** navigation |
| [`Off-grid power and field networking hub`](off-grid-power-and-field-networking-hub.md) | **Demory** off-grid doctrine + two-site WAN + field RF **routing** |
| [`Local site and county intelligence`](local-site-and-county-intelligence.md) | Claxton / Demory / Anderson / Campbell **evidence** and parcel gaps |
| [`Business plan execution and pilot operations hub`](business-plan-execution-and-pilot-operations-hub.md) | Phase 0–1 **execution dossier**, pilots, **V\*/G\***—not the full strategy TOC |

---

## Onboarding and terminology

| Page | Use when |
|------|----------|
| [`Start here — Smart Farm Wiki`](start-here-smart-farm-wiki.md) | **First visit**—fast paths without reading analyses |
| [`How to read this wiki`](how-to-read-this-wiki.md) | **Layers**, page types, how to use the catalog |
| [`Smart Farm Wiki glossary (hub)`](../glossary/smart-farm-wiki-glossary.md) | **Vocabulary** (gates, SoR, two-site, off-grid, platform) |
| [`Wiki overview`](../overview.md) | North-star + optional deep orientation list |

---

## Entity layer — operating objects

| Page | Use when |
|------|----------|
| [`Entity layer — operating objects gap audit`](../analyses/entity-layer-operating-objects-gap-audit.md) | **Audit**: what entities were for; what this pass added |
| [`Field node classes (G/R/S/H/W)`](../entities/field-node-classes-off-grid-farm-roles.md) | Off-grid **roles** (not SKUs) |
| [`RF and telemetry gateway roles`](../entities/rf-telemetry-gateway-roles-field-network.md) vs [`WAN edge and backhaul roles`](../entities/wan-edge-and-backhaul-roles.md) | Disambiguate **field** vs **internet** gateways |
| [`Backup and restore tier labels`](../entities/backup-restore-tier-labels-farm-stack.md) | Tier 0–3 **DR vocabulary** |
| [`Kubernetes edge control-plane roles`](../entities/kubernetes-edge-control-plane-roles.md) | k3s / etcd / Rancher **boundaries** |
| [`index.md`](../index.md#entities) | Full **Entities** list including labor, markets, infrastructure categories |

---

## Backup / disaster recovery

| Page | Use when |
|------|----------|
| [`Backup and disaster recovery — doctrine hub`](backup-disaster-recovery-doctrine-hub.md) | **Router**—start here for DR navigation |
| [`Backup and disaster recovery package — smart farm stack`](../analyses/backup-and-disaster-recovery-package-smart-farm-stack.md) | **Canonical spine** (same story as hub; full prose) |
| [`Disaster recovery decision rules — farm edge stack`](../analyses/disaster-recovery-decision-rules-farm-edge-stack.md) | **Incidents**: what failed, what to restore first, execution alignment |
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
| [`Source authority hardening audit`](../analyses/source-authority-hardening-audit.md) | **Provenance**: forums/blogs vs **official** clusters; backlog |

---

## Two-site smart farm (East Tennessee package)

| Page | Role |
|------|------|
| [`Two-site smart farm operations`](two-site-smart-farm-operations.md) | **Main hub**: business plan links, telemetry, runbooks, ownership table |
| [`East Tennessee two-site farm business plan (package)`](../business-plan/east-tennessee-two-site-farm-business-plan.md) | Reading order spine |
| [`Business plan execution and pilot operations hub`](business-plan-execution-and-pilot-operations-hub.md) | **Execution / pilots** router (memo, 90d, validation) |
| [`Reference architecture — 5 ac + 120 ac`](../analyses/reference-architecture-5ac-homebase-120ac-smart-farm.md) | Architecture package map |
| [`Execution dossier — Phase 0–1 (hub)`](../analyses/execution-dossier-hub-phase-0-1-east-tennessee.md) | Pilot execution entry (canonical analysis) |

---

## Off-grid systems — Demory farm (`SITE_FARM`)

| Page | Role |
|------|------|
| [`Off-grid power and field networking hub`](off-grid-power-and-field-networking-hub.md) | **Umbrella router** (Demory doctrine + two-site WAN + field links) |
| [`Off-grid systems doctrine package — Demory`](off-grid-systems-doctrine-package-demory-farm-site.md) | **First-class** hub: power domains, field-node classes, WAN deps, degraded modes, stop rules |
| [`Off-grid power doctrine — Demory`](../analyses/off-grid-power-strategy-demory-farm-site.md) | Solar+battery default; always-on vs duty-cycled; networking as load |
| [`Power domains and battery-backed infrastructure tiers — Demory`](../analyses/off-grid-power-domains-and-battery-tiers-demory-farm.md) | Pcrit / Popt; T0–T3 tiers |
| [`Field-node classes and communication roles — Demory`](../analyses/field-node-classes-and-communication-roles-demory-farm.md) | G/R/S/H/W roles (architecture, not SKUs) |
| [`Connectivity dependency map — farm systems (Demory)`](../analyses/connectivity-dependency-map-farm-systems-demory-farm.md) | What must work without WAN |
| [`Local-first / WAN-optional operating model — Demory`](../analyses/local-first-wan-optional-operating-model-demory-farm.md) | Operating posture; pilot vs scale |
| [`Off-grid degraded modes — power and connectivity (Demory)`](../analyses/off-grid-degraded-modes-power-and-connectivity-demory-farm.md) | P1/P2/N1/N2 failure classes |
| [`Off-grid infrastructure stop rules — Demory`](../analyses/off-grid-operational-decision-rules-power-and-networking-demory-farm.md) | DR-* rules; simplification triggers |
| [`Mesh and field networking — off-grid Demory`](../analyses/mesh-and-field-networking-strategy-off-grid-demory-farm.md) | Layering; Meshtastic vs HaLow vs Wi‑Fi |
| [`Off-grid farm execution topology (Mermaid)`](../analyses/off-grid-farm-execution-topology-demory-mermaid.md) | Reference / pilot / degraded diagrams |

---

## Homelab / edge Kubernetes (Pi, k3s, Longhorn)

| Page | Role |
|------|------|
| [`Platform doctrine package — homelab / farm edge`](platform-doctrine-package-homelab-farm-edge.md) | **First-class** hub: strategy, HA semantics, k3s/Longhorn/Rancher **roles**, storage comparison, **approved vs deferred** |
| [`Platform strategy for farm and homestead services`](../analyses/homelab-edge-kubernetes-platform-strategy-pi-k3s-longhorn-rancher.md) | Canonical stack narrative (same file; **alias** old long title) |
| [`Platform decision memo — phase, HA scope, deferrals`](../analyses/platform-decision-memo-phase-homelab-k3s-pi-fleet-2026-04-18.md) | Governance: Phase 0/1 vs deferred |
| [`HA meaning and constraints — homelab / farm platform`](../analyses/ha-meaning-and-constraints-homelab-farm-platform.md) | What **HA** does / does not mean here |
| [`k3s role in the homelab / farm platform`](../analyses/k3s-role-in-homelab-farm-platform.md), [`Longhorn role in the homelab / farm platform`](../analyses/longhorn-role-in-homelab-farm-platform.md) | Component boundaries |
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
