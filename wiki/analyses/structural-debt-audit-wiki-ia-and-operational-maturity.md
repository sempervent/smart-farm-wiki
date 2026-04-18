---
title: Structural debt audit — wiki IA and operational maturity
page_type: analysis
status: active
created: 2026-04-17
updated: 2026-04-17
review_status: unreviewed
tags:
  - meta
  - information-architecture
  - operational-maturity
page_subtype: meta_audit
operational_maturity: draft
confidence: high
---

# Structural debt audit — wiki IA and operational maturity

**Purpose**: Name **structural tech debt** as the wiki grows (hundreds of pages, **120+** analyses): **analysis sprawl**, **weak canonical ownership**, **guide-shaped pages** without a clear **type**, **maturity** signals that don’t distinguish “essay” from “field procedure,” and **navigation** pain from **flat** `index.md` lists. Complements [`Structural audit — repository shape and canonical routing`](structural-audit-repository-and-canonical-routing.md), [`Structural audit — page ownership, entity gaps, and hub routing`](structural-audit-page-ownership-entity-gaps-and-hub-routing.md), and [`Domain content overview`](domain-content-overview.md).

**Epistemic**: Counts are **approximate** (repository snapshot); re-count with `find wiki/analyses -name '*.md' | wc -l`.

---

## 1. Findings

### 1.1 Analysis sprawl

| Signal | Evidence | Risk |
|--------|----------|------|
| **Large `analyses/` cardinality** | **~123** markdown files under `wiki/analyses/` vs **~430** total wiki pages | Readers land on **query syntheses**, **one-off summaries**, and **canonical** chapters **without** a **sort key** in the filename alone. |
| **Parallel “overview” voices** | Domain overview, strategic audit, execution readiness audit, repository analysis | Three competing “north stars” if not labeled—mitigated by role labels in [`Domain content overview`](domain-content-overview.md) and this audit’s routing table. |
| **Meta-audit proliferation** | Multiple structural / strategic / IA / gap audits | Backlog drift if tables are copied instead of linked—follow `AGENTS.md` canonicalization. |

**Mitigation (governance)**: **`AGENTS.md`** — **Canonicalization before proliferation**, **hub maintenance**, **page ownership** map ([`structural-audit-page-ownership-entity-gaps-and-hub-routing`](structural-audit-page-ownership-entity-gaps-and-hub-routing.md)).

---

### 1.2 Weak canonical ownership

| Signal | Evidence | Risk |
|--------|----------|------|
| **Clusters without a named owner** | Described in ownership audit table | Duplicate chapters and inconsistent gates. |
| **Guide packages only under `analyses/`** | e.g. Pi k3s / Longhorn runbook hub | Discoverability depends on index lines and topic hubs—not a separate directory (by design today). |

**Mitigation**: **Topic** **hubs** (**[`Two-site smart farm operations`](../topics/two-site-smart-farm-operations.md)**, **[`Wiki navigation and structural hubs`](../topics/wiki-navigation-and-structural-hubs.md)**), **business-plan** **package** **hub**, **reference** **architecture** **hub**.

---

### 1.3 Missing guide / standard taxonomy (before this pass)

| Gap | What was wrong | Target state |
|-----|----------------|--------------|
| **No first-class `guide` directory** | Runbooks and how-to packages use `page_type: analysis` only | Keep paths flexible; document `page_subtype` `operational_guide` or `standard` in `AGENTS.md`. |
| **`status` vs “how tested”** | `draft` / `active` / `deprecated` lifecycle ≠ pilot vs field | Add optional `operational_maturity` orthogonal to `status` (see `AGENTS.md`). |

---

### 1.4 Unclear maturity for operational pages

| Signal | Problem |
|--------|---------|
| **`review_status`** | Editorial quality (`unreviewed` / `reviewed` / `stale`), not deployment provenance. |
| **`confidence`** | Epistemic source strength, not “we ran this drill twice.” |

**Target**: Optional `operational_maturity`: `draft` → `pilot_ready` → `field_tested`; use `superseded` together with `superseded_by`.

---

### 1.5 Navigation pain (flat lists)

| Pain | Mitigation implemented |
|------|-------------------------|
| **Single long “Analyses” list in `index.md`** | [`Wiki navigation and structural hubs`](../topics/wiki-navigation-and-structural-hubs.md) — themed tables to canonical entries (not a full mirror). |
| **Agents start from `index` only** | `index.md` Overview links this audit and the navigation topic. |

---

## 2. Implemented fixes (this refactor)

| Fix | Where |
|-----|--------|
| **`page_subtype`** **and** **`operational_maturity`** **documented** | [`AGENTS.md`](../../AGENTS.md) — **Page** **taxonomy** **+** **Frontmatter** **schema** |
| **Navigation** **hub** **(grouped** **routing** **)** | [`Wiki navigation and structural hubs`](../topics/wiki-navigation-and-structural-hubs.md) |
| **Debt** **audit** **(this** **page** **)** | Canonical **meta** **record** **for** **2026-04** **IA** **/ **ops** **maturity** **policy** |
| **Exemplar** **frontmatter** **on** **Pi** **runbook** **hub** | [`How to provision k3s, Longhorn, and Rancher on a Raspberry Pi fleet`](how-to-provision-k3s-longhorn-and-rancher-on-a-raspberry-pi-fleet.md) — **`page_subtype: operational_guide`**, **`operational_maturity: pilot_ready`** |
| **Index** **+** **domain** **overview** **+** **ownership** **audit** **cross-links** | [`index.md`](../index.md), [`domain-content-overview.md`](domain-content-overview.md), [`structural-audit-page-ownership-entity-gaps-and-hub-routing.md`](structural-audit-page-ownership-entity-gaps-and-hub-routing.md) |

---

## 3. Recommended next steps (not all done here)

1. **Incrementally** **tag** **runbooks** **and** **standards** **with** **`page_subtype`** **+** **`operational_maturity`** **when** **touched**.
2. **Prefer** **extending** **canonical** **hubs** **over** **new** **parallel** **“overview”** **analyses** **—** **log** **exceptions** **in** **`wiki/log.md`**.
3. **Optional** **validator** **warning**: **unknown** **`operational_maturity`** **values** **(future** **)**.

---

## Related

- [`Wiki navigation and structural hubs`](../topics/wiki-navigation-and-structural-hubs.md)
- [`Structural audit — page ownership, entity gaps, and hub routing`](structural-audit-page-ownership-entity-gaps-and-hub-routing.md)
- [`Evidence grade and canonical authority`](../concepts/evidence-grade-and-canonical-authority.md)
