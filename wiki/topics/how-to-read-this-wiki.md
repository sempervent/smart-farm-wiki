---
title: How to read this wiki
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

# How to read this wiki

**Goal**: Get value **without** reading every long analysis. Use **hubs**, **glossary**, and **page types** as signals.

---

## Layers

| Layer | Location | Role |
|-------|----------|------|
| **Raw sources** | `raw/` (see repo layout) | **Evidence**; not rewritten for convenience |
| **Source-notes** | `wiki/source-notes/` | Stable pointers into `raw/` + short notes |
| **Synthesis** | `wiki/` (entities, concepts, analyses, topics, glossary) | **Maintained** model—**this** is the “wiki” for most readers |

**Comparison**: [`Raw vs wiki`](../comparisons/raw-vs-wiki.md). **Repo pattern name**: [`Synthesis layer`](../glossary/synthesis-layer.md).

---

## Page types (signals)

| Kind | Typical path | Trust it for… |
|------|--------------|----------------|
| **Overview / topic hub** | `overview.md`, `topics/*` | **Routing**—where to go next |
| **Business plan package** | `business-plan/*`, linked chapters | **Decision narrative** and **gates** |
| **Entity** | `entities/*` | **Named** subject (place, product, system) with stable anchor |
| **Glossary** | `glossary/*` | **Definitions**—short; not full strategy |
| **Analysis** | `analyses/*` | **Depth**—may be long; check **Related** and **hubs** first |

**Analysis flavors** (same folder; use frontmatter and filenames—see [`Procedural guides package strategy`](procedural-guides-package-strategy-smart-farm-wiki.md)):

| Flavor | Signals |
|--------|---------|
| **Essay / audit** | Default; or `page_subtype: meta_audit` |
| **Standard** | `page_subtype: standard` — short **norms** |
| **Guide or runbook** | `page_subtype: operational_guide`; runbooks often **`runbook-*.md`** |

**Anti-swamp**: Prefer **canonical hubs** listed in [`Structural audit — page ownership`](../analyses/structural-audit-page-ownership-entity-gaps-and-hub-routing.md) over random deep analyses.

---

## Vocabulary shortcuts

- **Two-site model**: [`Two-site sites (SITE_HOME / SITE_FARM)`](../glossary/two-site-sites.md) · [`Distance tax (two-site)`](../glossary/distance-tax-two-site.md)
- **Gates**: [`Validation gate`](../glossary/validation-gate.md) · [`Execution gate`](../glossary/execution-gate.md)
- **Operations**: [`Degraded mode`](../glossary/degraded-mode.md) · [`System of record`](../glossary/system-of-record-farm-data.md) · [`Automation stop rules (terms)`](../glossary/automation-stop-rules-terms.md)
- **Places vs roles**: [`Entity vs site role`](../glossary/entity-vs-site-role.md)

Full table: [`Smart Farm Wiki glossary (hub)`](../glossary/smart-farm-wiki-glossary.md).

---

## Where the catalog lives

The **flat index** [`index.md`](../index.md) lists **intentional** pages for MkDocs and validation. **Themed entry**: [`Wiki navigation and structural hubs`](wiki-navigation-and-structural-hubs.md). **Chronological work**: [`log.md`](../log.md).

---

## See also

- [`Start here — Smart Farm Wiki`](start-here-smart-farm-wiki.md)
