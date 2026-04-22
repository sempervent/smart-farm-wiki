---
title: Execution dossier — Phase 0–1 (East Tennessee two-site)
page_type: analysis
status: active
created: 2026-04-21
updated: 2026-04-30
review_status: unreviewed
tags:
  - business-plan
  - execution
  - two-site
  - east-tennessee
confidence: medium
---

# Execution dossier — Phase 0–1 (East Tennessee two-site)

## Purpose

**Single entry** for the **pilot-grounded** operating package through **Phase 0–1** (roughly **months 0–24** on the roadmap, with most families still **before** or **at** **G1** by month **24**). Use this page **first**, then open **only** the slice you need.

**Stance**: **Execution** = **cheap proofs**, **small pilots**, **kill criteria**—not **premature scale**.

**Sources**: [`Validation backlog and decision gates`](east-tennessee-two-site-farm-business-plan-validation-backlog.md) (**V1–V12**, **G1–G3**), [`Execution gates — Phase 0–1 (East Tennessee two-site)`](execution-gates-phase-0-1-east-tennessee-two-site.md) (EG domain pass/fail, **pilot vs production**), [`Validation and pilot plan — first 24 months`](validation-and-pilot-plan-first-24-months-east-tennessee-two-site.md), [`Pilot and recon checklists`](pilot-and-recon-checklists-first-24-months-two-site-smart-farm.md), [`Validation — before major spend`](validation-backlog-before-major-spend-two-site-smart-farm.md).

**Package integration (2026-04)**: [`Business plan integration revision audit`](east-tennessee-two-site-farm-business-plan-integration-revision-audit-2026-04.md) — ledger of **doctrine/evidence → canonical business-plan chapters** (same package spine).

---

## Read order (minimal hopping)

| Order | Page | Use when |
|------:|------|----------|
| 1 | [`Decision memo — Phase 0–1`](execution-dossier-decision-memo-phase-0-1-east-tennessee.md) | **Today**—what is **allowed**, **pilot-only**, **forbidden** |
| 1b | [`Execution gates — Phase 0–1 (East Tennessee two-site)`](execution-gates-phase-0-1-east-tennessee-two-site.md) | **Pass/fail** by domain (EG tables); **pilot** vs **production** stance before expanding spend |
| 2 | [`First 90 days`](execution-first-90-days-phase-0-1-east-tennessee.md) | **Narrative** arc (days 1–90 bands + connectivity) |
| 2a | [`First 90 days — operator packet (East Tennessee two-site)`](first-90-days-operator-packet-east-tennessee-two-site.md) | **Canonical** **weeks 1–12** runbook: priorities, field bundles, stops, checkpoints |
| 3 | [`Master checklist`](execution-dossier-master-checklist-phase-0-1-east-tennessee.md) | **One** ordered list—**land**, **infra**, **business**, **telemetry**, **labor** |
| 4 | [`First 12 months`](execution-first-12-months-phase-0-1-east-tennessee.md) | After day **90**—quarterly rhythm |
| 5 | [`First 24 months`](execution-first-24-months-phase-0-1-east-tennessee.md) | Full arc + **G1** prep window |
| 6 | [`Validation and pilot plan`](validation-and-pilot-plan-first-24-months-east-tennessee-two-site.md) | **Full** validation matrix + **cheap proofs** table (detail) |
| 7 | [`Pilot and recon checklists`](pilot-and-recon-checklists-first-24-months-two-site-smart-farm.md) | **Copy-paste** rows into your tracker |
| 8 | [`Field verification program — Phase 0–1 (Claxton and Demory)`](field-verification-program-phase-0-1-claxton-demory.md) | **Site work tied to validation tasks and gates**: walks, roads, drainage, utilities, power, sensors, gateways, permits |

**Demory `SITE_FARM` field sensors** (long-range RF, gateways, Starlink = WAN only—not field radio): [`Farm sensor architecture — Demory farm site`](farm-sensor-architecture-demory-farm-site.md) · [`Sensor checklist matrix — Demory farm`](sensor-checklist-matrix-for-demory-farm.md).

---

## Calendar anchor (fill once)

| Symbol | Meaning |
|--------|---------|
| **T0** | **Execution start date** (family-declared)—all windows below are relative to **T0** |

---

## Homelab / edge stack (optional)

When execution includes a **Pi + k3s** homelab or farm-edge gateway aligned with the smart-farm platform story: [`How to provision k3s, Longhorn, and Rancher on a Raspberry Pi fleet`](how-to-provision-k3s-longhorn-and-rancher-on-a-raspberry-pi-fleet.md) (stay in **P0/P1** scope unless gates justify HA).

---

## Ready for execution: the plan is operational

Treat the wiki package as **operational** (not merely “written”) only when **all** are true. This is stricter than having pages filled—it is **behavioral** and **evidence**-based. Cross-check: [`Hostile internal review` §7](east-tennessee-two-site-farm-business-plan-hostile-internal-review.md#7-second-pass-execution-illusions-stricter-than-2), [`Remediation` §4 P0/P1](east-tennessee-two-site-farm-business-plan-remediation-backlog.md#4-must-validate-in-the-real-world-first-checklist).

### A. Governance and honesty

- [ ] Numeric **stop rules** from [`Vision`](east-tennessee-two-site-farm-business-plan-vision-and-constraints.md) are **posted** where decisions happen—not only in the wiki.
- [ ] Family agrees **checklists ≠ validation** ([`Pilot checklists` warning](pilot-and-recon-checklists-first-24-months-two-site-smart-farm.md)).
- [ ] **T0** execution start date recorded on [`Decision memo`](execution-dossier-decision-memo-phase-0-1-east-tennessee.md).

### B. Labor and surge (labor optimism killed)

- [ ] **V11**: **8+** week hour log **complete** including **one** stress/surge window.
- [ ] **Weekly DOW template** explicitly treated as **hypothesis** until surge measured ([`Labor model`](east-tennessee-two-site-farm-business-plan-labor-and-family-model.md)).
- [ ] [`Coverage matrix`](family-labor-model-and-coverage-matrix-two-site-smart-farm.md) shows **who** covers overload—or **hired/neighbor** row **non-empty**.

### C. Truth before scale (narrative optimism killed)

- [ ] **P0** items in [`Remediation` §4](east-tennessee-two-site-farm-business-plan-remediation-backlog.md) **pass** or **written waive** with date.
- [ ] **G1** is **not** assumed from **calendar**—evidence dated ([`First 24 months`](execution-first-24-months-phase-0-1-east-tennessee.md)).
- [ ] **Field verification program** underway: at least one **dated** visit log covering **§1–§3** at **Demory** and **§4–§5** at **Claxton** per [`Field verification program — Phase 0–1`](field-verification-program-phase-0-1-claxton-demory.md) cadence (**evidence** promoted via [`local evidence package`](../topics/local-evidence-package-east-tennessee-two-site.md), not free-text only).

### D. Technology optimism killed

- [ ] **G8** path: manual water (or critical) **baseline** log complete **before** actuation talk.
- [ ] **One** telemetry pilot only; **triage hours** tracked vs trip savings ([`ROI`](instrumentation-roi-model-two-site-smart-farm.md), [`Stop rules`](automation-stop-rules-two-site-smart-farm.md)).

### E. Financial and insurance illusions killed

- [ ] **Working capital** policy exists (even placeholder)—[`Capital plan`](east-tennessee-two-site-farm-business-plan-capital-and-financing.md).
- [ ] **V9**: binder **reviewed** with agent (exclusions/limits)—not quote-only ([`Decision memo` insurance note](execution-dossier-decision-memo-phase-0-1-east-tennessee.md)).

**If any box is unchecked**, the plan is **documentation**, not **operational control**.

**Domain gates (EG)**: Cross-check **A–E** above with the **composite** stance table in [`Execution gates — Phase 0–1`](execution-gates-phase-0-1-east-tennessee-two-site.md#composite-what-each-stance-allows)—especially before claiming **G1** in **production** posture.

---

## Related

- [`East Tennessee two-site farm business plan (package)`](../business-plan/east-tennessee-two-site-farm-business-plan.md)
- [`Local evidence package — East Tennessee two-site`](../topics/local-evidence-package-east-tennessee-two-site.md) — **site / infra / utility / loads** baselines + field templates; where **measured** facts land without scattering across analyses
- [`Field verification program — Phase 0–1 (Claxton and Demory)`](field-verification-program-phase-0-1-claxton-demory.md) — **structured** Claxton/Demory verification tied to **V\*/G\*** and baselines
- [`First 90 days — operator packet (East Tennessee two-site)`](first-90-days-operator-packet-east-tennessee-two-site.md) — **Field-facing** weekly operator bundle (pilot only)
- [`Execution gates — Phase 0–1 (East Tennessee two-site)`](execution-gates-phase-0-1-east-tennessee-two-site.md) — EG tables: what may **begin**, **pilot**, or **not** proceed to **production**
- [`Recommended enterprise strategy`](east-tennessee-two-site-farm-business-plan-recommended-enterprise-strategy.md)
- [`Two-site smart farm operations`](../topics/two-site-smart-farm-operations.md)
- [`Execution readiness gap audit — East Tennessee operational knowledge`](execution-readiness-gap-audit-east-tennessee-operational-knowledge.md) — **missing execution-grade data**, authority clusters, canonical update list
- [`Authoritative execution evidence cluster — East Tennessee`](../source-notes/authoritative-execution-evidence-cluster-east-tennessee.md) — **indexed** agency/extension ingests
- [`Claxton home base — site intelligence`](claxton-home-base-site-intelligence.md), [`Demory farm — site intelligence`](demory-farm-site-intelligence.md) — **county** evidence now **folded** into operating model, capital, validation, and execution slices above
- [`Off-grid systems doctrine package — Demory`](../topics/off-grid-systems-doctrine-package-demory-farm-site.md) — **`SITE_FARM`** **off-grid-first** **:** power, local RF, WAN-optional, degraded modes, **DR-*** stop rules
