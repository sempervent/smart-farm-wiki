---
title: Procedural guides package strategy — Smart Farm Wiki
page_type: topic
status: active
created: 2026-04-24
updated: 2026-04-24
tags:
  - meta
  - procedures
  - guides
  - operations
review_status: unreviewed
confidence: high
---

# Procedural guides package strategy — Smart Farm Wiki

**Purpose**: Treat **stepwise operator procedures** as **first-class** pages: one **place** they live, shared **metadata**, clear separation from **essays** and **standards**, and explicit **links** to **architecture**, **entities**, and **norms**.

**Policy**: [`AGENTS.md`](../../AGENTS.md) — `page_subtype`, `operational_maturity`, **Guides vs runbooks vs standards** (below in this file mirrors the contract).

---

## Where guides live

- **Path**: `wiki/analyses/` only (same validation rules and MkDocs publishing as other syntheses; no parallel `wiki/guides/` tree).
- **Page type**: `page_type: analysis` with **`page_subtype: operational_guide`** for any **procedure-shaped** page: a single how-to, a **hub** that sequences child steps, an **incident runbook**, or a long **doctrine spine** that still cues operators (tables, phases, drill steps).
- **Filenames**: `kebab-case.md`; prefer **`runbook-*.md`** for **incident / degraded-mode** procedures so they are obvious in search and indexes.

---

## How guides differ from analyses, standards, and runbooks

| Kind | `page_subtype` | Reader question |
|------|----------------|-----------------|
| **Essay / audit / synthesis** | *(omit)*, or `meta_audit` / `query_synthesis` | Why? What should we believe? What did we decide? |
| **Standard** | `standard` | What **must** be true? (short **norm**; bar, not a full install) |
| **Guide (procedural)** | `operational_guide` | What **steps**, in what **order**? (bootstrap, migration, validation drill) |
| **Runbook** | `operational_guide` + **`runbook-*.md`** (or **Runbook —** title) | What do we do when something **breaks**, **degrades**, or **alarms**? |

**Doctrine / package spines** (e.g. backup DR **package**) often use `operational_guide` because they **route** operators; they are still **guides** in the sense of this strategy—they are not optional “essays.”

**Standards vs guides**: standards state **bars**; guides implement **sequences**. Do not duplicate full command-level procedure in a standard when a guide exists—**link** the standard to the guide hub.

---

## Guide maturity

Use **`operational_maturity`** for procedure pages (orthogonal to **`status`**: `draft` / `active` / `deprecated`).

| YAML value | Plain language |
|------------|----------------|
| `draft` | Structure exists; not yet walked on live systems |
| `pilot_ready` | Lab or constrained pilot; limitations documented |
| `field_tested` | Used on real farm/homelab edge under stated constraints; drills or incidents inform updates |
| `superseded` | Routing only; pair with **`superseded_by`** (and a short pointer in the body) |

Labels like **pilot-ready** or **field-tested** in prose map to **`pilot_ready`** and **`field_tested`** in frontmatter.

---

## Links guides should carry

Each procedural page should make **routing** easy without copying canonical architecture:

1. **Doctrine or reference architecture** — why this procedure exists (if not obvious from the title).
2. **Standards** — norms that must hold before/after the steps ([`Operational standards — farm and homelab platform`](operational-standards-farm-homelab-platform.md) catalog).
3. **Entities** — stable roles ([`Field node classes (G/R/S/H/W)`](../entities/field-node-classes-off-grid-farm-roles.md), [`WAN edge and backhaul roles`](../entities/wan-edge-and-backhaul-roles.md), [`Backup and restore tier labels`](../entities/backup-restore-tier-labels-farm-stack.md), …) instead of redefining glossaries.
4. **Parent hub** — package hub ([`Platform doctrine package — homelab / farm edge`](platform-doctrine-package-homelab-farm-edge.md), [`Backup and disaster recovery — doctrine hub`](backup-disaster-recovery-doctrine-hub.md), …) or [`Wiki navigation and structural hubs`](wiki-navigation-and-structural-hubs.md).

**Secrets**: follow [`AGENTS.md`](../../AGENTS.md) — placeholders in published pages; no live credentials in `wiki/`.

---

## Canonical guide hubs (entry points)

| Domain | Hub |
|--------|-----|
| Homelab edge — Pi, k3s, Longhorn, Rancher | [`How to provision k3s, Longhorn, and Rancher on a Raspberry Pi fleet`](../analyses/how-to-provision-k3s-longhorn-and-rancher-on-a-raspberry-pi-fleet.md) |
| Backup / DR — stack-wide story | [`Backup and disaster recovery package — smart farm stack`](../analyses/backup-and-disaster-recovery-package-smart-farm-stack.md) |
| DR — incident framing | [`Disaster recovery decision rules — farm edge stack`](../analyses/disaster-recovery-decision-rules-farm-edge-stack.md) |
| Kubernetes platform backup / DR (integration) | [`Kubernetes platform backup / DR — Pi, k3s, Longhorn`](../analyses/kubernetes-platform-backup-dr-pi-k3s-longhorn.md) |

**Example runbooks** (incident-shaped): [`Runbook — backup validation and recovery drill`](../analyses/runbook-backup-validation-and-recovery-drill.md), [`Runbook — broker or backhaul down`](../analyses/runbook-broker-or-backhaul-down.md), [`Runbook — power loss at remote site`](../analyses/runbook-power-loss-remote-site.md).

---

## See also

- [`Wiki navigation and structural hubs`](wiki-navigation-and-structural-hubs.md) — routers + this topic linked from the **Procedural guides** section
- [`Operational standards — farm and homelab platform`](operational-standards-farm-homelab-platform.md) — norms catalog (pair with guides, do not merge blindly)
- [`Structural debt audit — wiki IA and operational maturity`](../analyses/structural-debt-audit-wiki-ia-and-operational-maturity.md) — history of `page_subtype` / `operational_maturity`
