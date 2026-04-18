---
title: Start here — Smart Farm Wiki
page_type: topic
status: active
created: 2026-04-17
updated: 2026-04-24
tags:
  - meta
  - onboarding
review_status: unreviewed
confidence: high
---

# Start here — Smart Farm Wiki

**What this is**: A **markdown-first** knowledge base: **`raw/`** holds **immutable** sources; **`wiki/`** holds **syntheses** (entities, concepts, analyses, glossary). **`docs/`** (repo root) is the **operator handbook** for *how the repo works*, not farm domain knowledge.

**Fast path** (pick one):

| If you want to… | Open |
|-----------------|------|
| **Understand vocabulary** (gates, SoR, two-site, degraded modes) | [`Smart Farm Wiki glossary (hub)`](../glossary/smart-farm-wiki-glossary.md) |
| **Read the East Tennessee two-site business plan** (~5 ac + ~120 ac + phased strategy) | [`East Tennessee two-site farm business plan (package)`](../business-plan/east-tennessee-two-site-farm-business-plan.md) |
| **Run operations / telemetry / runbooks** for that scenario | [`Two-site smart farm operations`](../topics/two-site-smart-farm-operations.md) |
| **See Claxton vs Demory / county vs parcel routing** | [`Local site and county intelligence`](../topics/local-site-and-county-intelligence.md) |
| **Demory off-grid-first** (solar + battery, mesh, WAN optional) | [`Off-grid systems doctrine package — Demory`](../topics/off-grid-systems-doctrine-package-demory-farm-site.md) |
| **Homelab / farm edge compute** (Pi, k3s, Longhorn, backup) | [`Platform doctrine package — homelab / farm edge`](../topics/platform-doctrine-package-homelab-farm-edge.md) |
| **How pages are structured** (canonical vs analysis sprawl) | [`How to read this wiki`](how-to-read-this-wiki.md) · [`Evidence grade and canonical authority`](../concepts/evidence-grade-and-canonical-authority.md) |
| **Repeated operating roles** (gateways, WAN, node classes, DR tiers—link instead of re-explaining) | [`Entity layer — operating objects gap audit`](../analyses/entity-layer-operating-objects-gap-audit.md) · [`index.md` Entities](../index.md#entities) |
| **Whole-topic packages** (platform, backup, off-grid, sites, execution) without scanning analyses | [`Wiki navigation and structural hubs`](../topics/wiki-navigation-and-structural-hubs.md#five-package-hubs-start-here-for-whole-topics) |
| **Procedural guides and runbooks** (where how-tos live, vs standards, maturity labels) | [`Procedural guides package strategy — Smart Farm Wiki`](procedural-guides-package-strategy-smart-farm-wiki.md) |

**North-star narrative**: [`Wiki overview`](../overview.md) (short; links here and to domain strands).

---

## For agents

Follow [`AGENTS.md`](../../AGENTS.md): **`wiki/log.md`** is append-only; run `uv run python scripts/validate_wiki.py` before commit.

---

## See also

- [`Wiki navigation and structural hubs`](wiki-navigation-and-structural-hubs.md) — themed routers (meta, two-site, off-grid, homelab, runbooks)
- [`Domain content overview`](../analyses/domain-content-overview.md) — what strands the wiki covers
