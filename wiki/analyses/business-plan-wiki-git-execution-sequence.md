---
title: Business plan wiki — Git-friendly execution sequence
page_type: analysis
status: active
created: 2026-04-18
updated: 2026-04-18
review_status: unreviewed
tags:
  - meta
  - business-plan
  - git
  - workflow
confidence: medium
aliases:
  - ET two-site business plan PR sequence
---

# Business plan wiki — Git-friendly execution sequence

## Purpose

Describe a **coherent merge order** for landing the East Tennessee **two-site business-plan** work: **pull requests** (or change batches), **per-PR scope**, **commits within each PR**, **landing order** to avoid orphans and misleading context, and a **minimum usable state** milestone. Aligns with [`Smart Farm Wiki — repository implementation plan (business plan integration)`](smart-farm-wiki-repository-implementation-plan.md).

**Audience**: Humans merging markdown; CI expects `uv run python scripts/validate_wiki.py --strict`.

---

## 1. Proposed sequence of pull requests (batches)

Each block is a **logical PR**. Squash-merge or keep commits per team policy. If work **already exists on `main`**, use each block as a **retroactive chunk** or **future refactor** scope.

---

### PR 1 — Navigation shell (topic hub + catalog)

| Field | Content |
|-------|---------|
| **Title** | `wiki: two-site business plan topic hub + index/overview links` |
| **Purpose** | Make the business-plan cluster discoverable before specialized satellites. Matches implementation plan **Phase A — Navigation**. |
| **Files** | `wiki/topics/two-site-smart-farm-operations.md` (create), `wiki/index.md`, `wiki/overview.md`, `wiki/topics/knowledge-synthesis.md`, `wiki/analyses/east-tennessee-two-site-farm-business-plan-framework.md` (topic hub link), `wiki/log.md` |
| **Why together** | A hub without inbound links is orphaned; the framework should point to the hub for round-trip navigation. |
| **Acceptance criteria** | `validate_wiki.py --strict` passes; every new file listed in `index.md`; topic hub links only to paths that exist at merge time. |

---

### PR 2 — Planning framework hub

| Field | Content |
|-------|---------|
| **Title** | `wiki: ET two-site business plan — planning framework + package tree` |
| **Purpose** | Establish the single canonical hub with a child table before long children land. |
| **Files** | `wiki/analyses/east-tennessee-two-site-farm-business-plan-framework.md`, `wiki/index.md` if new entry needed |
| **Why together** | Greenfield rule: add framework + executive summary + vision in one PR **or** link only to files that exist—avoid stub titles without files. |
| **Acceptance criteria** | Package table rows resolve to real paths; no broken links in the framework tree. |

---

### PR 3 — Business plan narrative pages

| Field | Content |
|-------|---------|
| **Title** | `wiki: ET two-site business plan — vision through validation package` |
| **Purpose** | Land decision-grade narrative as one coherent story (or split 3a / 3b if diff is huge). |
| **Files** | `east-tennessee-two-site-farm-business-plan-vision-and-constraints.md`, `…-two-site-operating-context.md`, `…-enterprise-options-analysis.md`, `…-recommended-enterprise-strategy.md`, `…-labor-and-family-model.md`, `…-smart-tech-strategy.md`, `…-capital-and-financing.md`, `…-revenue-and-phased-income.md`, `…-risk-register.md`, `…-10-year-roadmap.md`, `…-validation-backlog.md`, `…-executive-summary.md`, `wiki/index.md`, `wiki/topics/two-site-smart-farm-operations.md`, `wiki/log.md` |
| **Why together** | Cross-links between chapters break if half the package is missing on `main`. **Split option**: 3a vision → enterprise → strategy; 3b labor → tech → capital → revenue → risk → roadmap → validation → **executive summary last** (summary maps children). |
| **Acceptance criteria** | Relative links between package pages resolve; executive summary lists actual filenames; `validate_wiki.py --strict`. |

---

### PR 4 — Operational artifacts and comparisons

| Field | Content |
|-------|---------|
| **Title** | `wiki: two-site operational artifacts + equipment/telemetry comparisons` |
| **Purpose** | Matrices and comparisons the plan references for execution. |
| **Files** | `two-site-operations-model-5ac-homebase-120ac-production.md`, `family-labor-model-and-coverage-matrix-two-site-smart-farm.md`, `instrumentation-priority-matrix-two-site-smart-farm.md`, `capital-phasing-table-years-0-10-two-site-smart-farm.md`, `revenue-milestone-model-supplemental-to-salary-replacement.md`, `business-risk-register-two-site-smart-farm.md`, `manual-fallback-degraded-modes-critical-operations.md`, `validation-backlog-before-major-spend-two-site-smart-farm.md`, `comparisons/lorawan-vs-meshtastic-fixed-farm-telemetry.md`, `comparisons/farmos-vs-lightweight-stack-two-site-farm.md`, `comparisons/own-equipment-vs-custom-hire-two-site-logistics.md`, `comparisons/fixed-gateway-tower-vs-mobile-vehicle-gateway.md`, `wiki/index.md`, `wiki/topics/two-site-smart-farm-operations.md`, `east-tennessee-two-site-farm-business-plan-framework.md` (artifact table), `wiki/log.md` |
| **Why together** | Artifacts are cross-linked from strategy and hub; comparisons support smart-tech without bloating narrative pages. |
| **Acceptance criteria** | No orphan artifacts (each in `index.md` or hub table); comparisons linked from instrumentation matrix or smart-tech strategy. |

---

### PR 5 — Meta: critique, remediation, implementation plan

| Field | Content |
|-------|---------|
| **Title** | `wiki: business plan hostile review + remediation + repo implementation plan` |
| **Purpose** | Second-order docs that assume the core plan exists. |
| **Files** | `east-tennessee-two-site-farm-business-plan-hostile-internal-review.md`, `east-tennessee-two-site-farm-business-plan-remediation-backlog.md`, `smart-farm-wiki-repository-implementation-plan.md`, `wiki/index.md`, `east-tennessee-two-site-farm-business-plan-framework.md`, `wiki/topics/knowledge-synthesis.md`, `wiki/log.md` |
| **Why together** | Single meta merge keeps `main` truthful: no remediation without a review target. |
| **Acceptance criteria** | Remediation links hostile review; implementation plan checkboxes match shipped navigation. |

---

### PR 6 — Financial planning layer

| Field | Content |
|-------|---------|
| **Title** | `wiki: two-site financial planning layer (worksheets + milestones + ROI)` |
| **Purpose** | Economics scaffolding with placeholders only. |
| **Files** | `enterprise-unit-economics-worksheet-methodology-two-site-smart-farm.md`, `capex-opex-enterprise-sequencing-two-site-constraint.md`, `farm-accounting-baseline-chart-of-accounts-enterprise-pl-two-site-smart-farm.md`, `revenue-milestone-model-supplemental-to-salary-replacement.md` (major edit), `instrumentation-roi-model-two-site-smart-farm.md`, `wiki/index.md` (financial subsection), `east-tennessee-two-site-farm-business-plan-framework.md` (financial table), `wiki/topics/two-site-smart-farm-operations.md`, `wiki/log.md` |
| **Why together** | Cross-dependencies (unit economics → accounting → milestones); one navigation block avoids half-visible economics. |
| **Acceptance criteria** | No fabricated budget numbers; `validate_wiki.py --strict`. |

---

### PR 7 — Smart-farm architecture package

| Field | Content |
|-------|---------|
| **Title** | `wiki: two-site smart-farm architecture package (reference arch, SoR, security)` |
| **Purpose** | Technical architecture aligned to business-plan telemetry assumptions. |
| **Files** | `reference-architecture-5ac-homebase-120ac-smart-farm.md`, `telemetry-system-of-record-boundaries-and-authority.md`, `automation-principles-two-site-smart-farm.md`, `remote-access-operational-security-model-two-site-smart-farm.md`, edits to `field-telemetry-reference-architecture-homestead-120ac.md`, `farm-spatial-model-and-asset-registry-standard.md`, `instrumentation-priority-matrix-two-site-smart-farm.md`, `manual-fallback-degraded-modes-critical-operations.md`, `wiki/index.md`, `east-tennessee-two-site-farm-business-plan-framework.md`, `wiki/topics/two-site-smart-farm-operations.md`, `wiki/log.md` |
| **Why together** | Reference hub links SoR and field telemetry; splitting leaves broken package-map rows. |
| **Acceptance criteria** | Package table in reference architecture resolves; SoR linked from field telemetry reference architecture. |

---

### PR 8 — Validation and pilot (24 months)

| Field | Content |
|-------|---------|
| **Title** | `wiki: 24-month validation and pilot plan + recon checklists` |
| **Purpose** | Operationalize V/G IDs into a time-bounded cadence. |
| **Files** | `validation-and-pilot-plan-first-24-months-east-tennessee-two-site.md`, `pilot-and-recon-checklists-first-24-months-two-site-smart-farm.md`, `east-tennessee-two-site-farm-business-plan-validation-backlog.md` (cross-link), `east-tennessee-two-site-farm-business-plan-framework.md`, `wiki/index.md`, `wiki/topics/two-site-smart-farm-operations.md`, `wiki/log.md` |
| **Why together** | Checklists without the parent plan page are orphan templates. |
| **Acceptance criteria** | Validation backlog links 24-month plan; checklist anchors match parent links. |

---

### PR 9 — Source-ingest campaign and IA alignment (optional)

| Field | Content |
|-------|---------|
| **Title** | `wiki: source-ingest campaign meta + IA/strategic doc alignment` |
| **Purpose** | Campaign doc + implementation plan Phase B (IA alignment). |
| **Files** | `business-plan-source-ingest-campaign-east-tennessee-two-site.md`, `domain-content-overview.md`, `information-architecture-decision-safe-operations.md`, `implementation-backlog-strategic-audit.md` (as needed), `wiki/index.md`, `wiki/log.md` |
| **Why together** | Low-risk batch after core content is stable; avoids editing IA docs while URLs are in flux. |
| **Acceptance criteria** | IA doc does not list “pending” hubs that already shipped. |

---

## 2. Recommended commit sequence within each PR

| Order | Commit focus | Typical message prefix |
|-------|----------------|-------------------------|
| 1 | New or updated analysis/topic **content** | `docs(wiki): add …` |
| 2 | Cross-links from framework, hub, or parents | `docs(wiki): link … from framework and hub` |
| 3 | `wiki/index.md` catalog | `docs(wiki): index two-site business plan …` |
| 4 | `overview.md` / `knowledge-synthesis.md` if touched | `docs(wiki): surface … in overview` |
| 5 | `wiki/log.md` append | `docs(wiki): log …` |

**Rule**: Do not commit `log.md` describing content until that content exists on the branch (earlier commit or same commit).

---

## 3. Landing order — pages and navigation first

| Priority | Rule |
|----------|------|
| P0 | Update `wiki/index.md` and `wiki/overview.md` in the **same batch** as any new analysis that should be discoverable from the catalog. |
| P0 | Land `wiki/topics/two-site-smart-farm-operations.md` **with** inbound links from index, overview, `knowledge-synthesis.md`, and outbound from [`east-tennessee-two-site-farm-business-plan-framework.md`](east-tennessee-two-site-farm-business-plan-framework.md). |
| P1 | Land [`east-tennessee-two-site-farm-business-plan-framework.md`](east-tennessee-two-site-farm-business-plan-framework.md) before or with the first child that only links “up” to the framework; keep the framework package table consistent with files on disk. |
| P2 | Land meta pages (hostile review, remediation, implementation plan) **after** the core plan pages they reference or critique. |
| P2 | Land financial and architecture packages with `index.md` subsections and `framework.md` links in the **same PR** as the new pages. |
| P3 | Append `wiki/log.md` last in the batch (or dedicated commit) so append-only history stays clear in git blame. |

---

## 4. Minimum usable state milestone

**Definition of done** for “business-plan work landed in the wiki”:

| # | Criterion |
|---|-----------|
| 1 | A reader entering via `wiki/overview.md` or `wiki/index.md` can reach [`east-tennessee-two-site-farm-business-plan-framework.md`](east-tennessee-two-site-farm-business-plan-framework.md) in ≤ 2 clicks. |
| 2 | [`wiki/topics/two-site-smart-farm-operations.md`](../topics/two-site-smart-farm-operations.md) exists and is linked from index, overview, knowledge-synthesis, and the framework. |
| 3 | All intentional business-plan and artifact pages appear in `index.md` or are linked from the framework or topic hub (validator orphan policy). |
| 4 | `uv run python scripts/validate_wiki.py --strict` passes on `main`. |
| 5 | Placeholder economics stay explicitly TBD—no invented dollar figures in merged markdown (per [implementation plan §6](smart-farm-wiki-repository-implementation-plan.md)). |

Below this bar, treat the repo as not ready for external stakeholders browsing `main`.

**Note**: PRs 6–9 are **enhancements** to the minimum state; the **structural** minimum is satisfied after **PR 1–3** (navigation + framework + narrative) plus **index** integrity—see PR sequence above.

---

## Related

- [`Smart Farm Wiki — repository implementation plan (business plan integration)`](smart-farm-wiki-repository-implementation-plan.md)
- [`East Tennessee two-site farm business plan — planning framework`](east-tennessee-two-site-farm-business-plan-framework.md)
