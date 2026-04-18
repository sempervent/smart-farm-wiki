---
title: Wiki overview
page_type: overview
status: active
created: 2026-04-17
updated: 2026-04-18
tags:
  - meta
  - llm-wiki
review_status: reviewed
---

# Overview

This vault is a **structured synthesis layer** on top of immutable **raw** sources. The agent’s job is to compound knowledge: entities, concepts, timelines, and analyses linked with stable paths and explicit provenance. **Purpose and voice** for *Smart Farm Wiki* are stated in [`concepts/smart-farm-wiki-mission-and-values.md`](concepts/smart-farm-wiki-mission-and-values.md).

**Start here (pick one lane)**

| Lane | First pages |
|------|-------------|
| **East Tennessee two-site** (business plan, execution, parcels) | [`Start here`](topics/start-here-smart-farm-wiki.md) → [`East Tennessee two-site farm business plan (package)`](business-plan/east-tennessee-two-site-farm-business-plan.md) → [`Two-site smart farm operations`](topics/two-site-smart-farm-operations.md) |
| **Platform / backup / homelab edge** | [`Platform doctrine package — homelab / farm edge`](topics/platform-doctrine-package-homelab-farm-edge.md) · [`Backup and disaster recovery — doctrine hub`](topics/backup-disaster-recovery-doctrine-hub.md) · [`Operational standards — farm and homelab platform`](topics/operational-standards-farm-homelab-platform.md) |
| **Meta (how to read, evidence, navigation health)** | [`How to read this wiki`](topics/how-to-read-this-wiki.md) · [`Evidence grade and canonical authority`](concepts/evidence-grade-and-canonical-authority.md) · [`Wiki navigation and structural hubs`](topics/wiki-navigation-and-structural-hubs.md) · [`Usability and navigation audit — 2026-04-18`](analyses/usability-and-navigation-audit-2026-04-18.md) |

The full flat catalog is [`index.md`](index.md). **Do not** treat the **Business plan** or **Analyses** sections of `index.md` as a linear reading list—use **package hubs** and **canonical** pages first.

**Onboarding (read first)**

- **[`Start here — Smart Farm Wiki`](topics/start-here-smart-farm-wiki.md)** — fast paths: business plan, two-site ops, local evidence, off-grid doctrine, homelab platform.
- **[`How to read this wiki`](topics/how-to-read-this-wiki.md)** — layers (`raw` vs wiki), page types, vocabulary shortcuts, where the catalog lives.
- **[`Smart Farm Wiki glossary (hub)`](glossary/smart-farm-wiki-glossary.md)** — definition-first entries (gates, SoR, two-site, off-grid, platform terms).
- **[`Source-note abstract and evidence pattern`](concepts/source-note-abstract-and-evidence-pattern.md)** — optional **Evidence summary** block for cluster source-notes (provenance + canonical links).

**Deeper orientation (optional)**

1. [`index.md`](index.md) — full catalog; [`log.md`](log.md) — chronological work; **source-notes** ground claims in `raw/processed/`.
2. **Repo / publishing**: [`analyses/repository-analysis.md`](analyses/repository-analysis.md); operator handbook: `docs/` at repo root.
3. **Domain strands**: [`analyses/domain-content-overview.md`](analyses/domain-content-overview.md).
4. **IA / audits**: [`analyses/information-architecture-decision-safe-operations.md`](analyses/information-architecture-decision-safe-operations.md), [`analyses/strategic-audit-decision-safe-operations.md`](analyses/strategic-audit-decision-safe-operations.md), [`analyses/implementation-backlog-strategic-audit.md`](analyses/implementation-backlog-strategic-audit.md).
5. **East Tennessee two-site package**: [`business-plan/east-tennessee-two-site-farm-business-plan.md`](business-plan/east-tennessee-two-site-farm-business-plan.md); [`topics/local-site-and-county-intelligence.md`](topics/local-site-and-county-intelligence.md); [`topics/two-site-smart-farm-operations.md`](topics/two-site-smart-farm-operations.md); repo wiring: [`analyses/smart-farm-wiki-repository-implementation-plan.md`](analyses/smart-farm-wiki-repository-implementation-plan.md).
6. **Structure / ownership**: [`analyses/structural-audit-repository-and-canonical-routing.md`](analyses/structural-audit-repository-and-canonical-routing.md), [`AGENTS.md`](../AGENTS.md), [`analyses/structural-audit-page-ownership-entity-gaps-and-hub-routing.md`](analyses/structural-audit-page-ownership-entity-gaps-and-hub-routing.md); **operating-object entities**: [`analyses/entity-layer-operating-objects-gap-audit.md`](analyses/entity-layer-operating-objects-gap-audit.md); **source authority**: [`analyses/source-authority-hardening-audit.md`](analyses/source-authority-hardening-audit.md).
7. **Execution readiness** (no invented parcel facts): [`analyses/execution-readiness-gap-audit-east-tennessee-operational-knowledge.md`](analyses/execution-readiness-gap-audit-east-tennessee-operational-knowledge.md); agency ingests: [`source-notes/authoritative-execution-evidence-cluster-east-tennessee.md`](source-notes/authoritative-execution-evidence-cluster-east-tennessee.md); ingest visibility: [`analyses/ingest-visibility-gap-authoritative-evidence-east-tennessee.md`](analyses/ingest-visibility-gap-authoritative-evidence-east-tennessee.md).
8. **Package hubs** (avoid flat analysis lists): [`topics/wiki-navigation-and-structural-hubs.md`](topics/wiki-navigation-and-structural-hubs.md#five-package-hubs-start-here-for-whole-topics) — platform, backup/DR, off-grid + field RF, local site intelligence, execution & pilots.
9. **Operational standards** (repeatable norms): [`topics/operational-standards-farm-homelab-platform.md`](topics/operational-standards-farm-homelab-platform.md) — Pi, k3s, storage/secrets, observability, backup cadence, field/WAN naming, site-to-site boundaries.
10. **Procedural guides** (how-tos and runbooks): [`topics/procedural-guides-package-strategy-smart-farm-wiki.md`](topics/procedural-guides-package-strategy-smart-farm-wiki.md) — where they live, **vs** standards, **`operational_maturity`**, links to doctrine and entities.

**Principles**

- Raw sources are evidence; the wiki is the maintained model.
- Prefer incremental edits and explicit deprecation over silent rewrites.
- Relative links keep Obsidian and validation tooling aligned.
