---
title: East Tennessee two-site farm business plan — integration revision audit (2026-04)
page_type: analysis
page_subtype: meta_audit
status: active
created: 2026-04-27
updated: 2026-04-28
review_status: unreviewed
confidence: high
tags:
  - business-plan
  - east-tennessee
  - two-site
  - integration
---

# East Tennessee two-site farm business plan — integration revision audit (2026-04)

**Scope**: One **hardening-and-integration** pass over the **existing** canonical package ([`East Tennessee two-site farm business plan (package)`](../business-plan/east-tennessee-two-site-farm-business-plan.md)) and its chapter pages—**no** parallel business plan, **no** TOC replacement.

**Ledger role**: Summarize **what doctrine and evidence packages now change in the plan**, **which pages were touched**, **what strengthened vs what stayed weak or blocked**, and **new sequencing / risk implications**.

---

## What materially changed in the plan

| Theme | Effect on the business plan |
|-------|------------------------------|
| **Local evidence & parcel intelligence** | County/desktop anchors (**NASS rent bands**, **WSS-derived terrain bias** for Campbell AOI, Claxton OSSS/utility posture) are treated as **directional** inputs to enterprise fit, capital sequencing, and labor surge honesty—not as **parcel deed facts**. **G1-class** decisions still require **field verification**, worksheets, and the **missing-data register**; the plan explicitly routes Phase 0–1 execution through [`Field verification program — Phase 0–1 (Claxton and Demory)`](field-verification-program-phase-0-1-claxton-demory.md). |
| **Off-grid & connectivity doctrine** | `SITE_FARM` planning default (**solar + battery**, **mesh / LPWAN before WAN convenience**, **WAN-optional local survivability**) is **bound** into capital sequencing, smart-tech Starlink framing, and risk: Starlink remains **backhaul**, not a substitute for **local gateway + power domain** truth or **DR-1**-style load metering ([`Off-grid systems doctrine package — Demory`](../topics/off-grid-systems-doctrine-package-demory-farm-site.md), [`Local-first / WAN-optional — Demory`](local-first-wan-optional-operating-model-demory-farm.md), [`Connectivity strategy — Claxton & Demory`](connectivity-strategy-for-claxton-and-demory.md)). |
| **Sensor & field telemetry doctrine** | Phase 0–1 **observe-first** scope is tied to **farm sensor architecture**, **field-node roles**, **gateway/controller patterns**, **duty-cycle / power assumptions**, **sensor degraded modes**, and the **sensor checklist matrix**—so pilot design, labor triage, and observability load are not “sensor count” optimism ([`Farm sensor architecture — Demory farm site`](farm-sensor-architecture-demory-farm-site.md), [`Sensor checklist matrix — Demory farm`](sensor-checklist-matrix-for-demory-farm.md)). |
| **Platform, backup/DR, observability** | Where the control-center stack follows **Pi + k3s** patterns, the plan now **routes** explicit **backup/restore obligations**, **DR drill posture**, and **remote trust bar** (secrets, alerting philosophy, minimum conditions before privileged remote work) instead of implying “homelab = free HA” ([`Platform doctrine package`](../topics/platform-doctrine-package-homelab-farm-edge.md), [`Kubernetes platform backup/DR — Pi k3s Longhorn`](kubernetes-platform-backup-dr-pi-k3s-longhorn.md), [`Backup / DR doctrine hub`](../topics/backup-disaster-recovery-doctrine-hub.md), [`Observability, secrets, and trust bar — homelab / farm edge`](observability-secrets-and-trust-bar-homelab-farm-edge.md)). |
| **Source authority & navigation** | Chapters cross-check against **evidence grade** and **evidence-hardening** work so exploratory prose does not masquerade as parcel truth; authoritative clusters remain **operator indexes**, not substitutes for local measurement ([`Evidence grade and canonical authority`](../concepts/evidence-grade-and-canonical-authority.md), [`Evidence hardening audit — East Tennessee (2026-04)`](evidence-hardening-audit-east-tennessee-two-site-2026-04.md)). |

---

## Pages updated (this pass)

| Path | Change summary |
|------|----------------|
| [`../business-plan/east-tennessee-two-site-farm-business-plan.md`](../business-plan/east-tennessee-two-site-farm-business-plan.md) | **“What changed”** block + `updated` date; points here. |
| [`east-tennessee-two-site-farm-business-plan-framework.md`](east-tennessee-two-site-farm-business-plan-framework.md) | Known fact **K10**, unknown **U10**, assumption **A5**, vault spine links (platform DR, observability trust bar, field verification, this audit). |
| [`east-tennessee-two-site-farm-business-plan-vision-and-constraints.md`](east-tennessee-two-site-farm-business-plan-vision-and-constraints.md) | **Evidence / doctrine alignment** note for Phase 1 gates vs desk evidence. |
| [`east-tennessee-two-site-farm-business-plan-two-site-operating-context.md`](east-tennessee-two-site-farm-business-plan-two-site-operating-context.md) | **WAN-optional / connectivity** routing on the 35-minute model. |
| [`east-tennessee-two-site-farm-business-plan-enterprise-options-analysis.md`](east-tennessee-two-site-farm-business-plan-enterprise-options-analysis.md) | **Automation-fit** scoring tied to sensor doctrine artifacts. |
| [`east-tennessee-two-site-farm-business-plan-recommended-enterprise-strategy.md`](east-tennessee-two-site-farm-business-plan-recommended-enterprise-strategy.md) | Pointer to this audit as integration spine. |
| [`east-tennessee-two-site-farm-business-plan-labor-and-family-model.md`](east-tennessee-two-site-farm-business-plan-labor-and-family-model.md) | **Field verification** as labor/time evidence path. |
| [`east-tennessee-two-site-farm-business-plan-smart-tech-strategy.md`](east-tennessee-two-site-farm-business-plan-smart-tech-strategy.md) | **Doctrine binding** bullets (sensors, degraded modes, platform, backup/DR, trust bar). |
| [`east-tennessee-two-site-farm-business-plan-capital-and-financing.md`](east-tennessee-two-site-farm-business-plan-capital-and-financing.md) | **Platform/backup/observability** obligations when edge/k3s scope is real. |
| [`east-tennessee-two-site-farm-business-plan-revenue-and-phased-income.md`](east-tennessee-two-site-farm-business-plan-revenue-and-phased-income.md) | **Haul / processing / parcel** evidence caveat. |
| [`east-tennessee-two-site-farm-business-plan-risk-register.md`](east-tennessee-two-site-farm-business-plan-risk-register.md) | **R16** — WAN + off-grid stress converging on telemetry trust. |
| [`east-tennessee-two-site-farm-business-plan-10-year-roadmap.md`](east-tennessee-two-site-farm-business-plan-10-year-roadmap.md) | Phase **0–1** rows reference **field verification program**. |
| [`east-tennessee-two-site-farm-business-plan-validation-backlog.md`](east-tennessee-two-site-farm-business-plan-validation-backlog.md) | Integration audit + structured field program routing. |
| [`east-tennessee-two-site-farm-business-plan-remediation-backlog.md`](east-tennessee-two-site-farm-business-plan-remediation-backlog.md) | Top pointer: hostile review **plus** integration ledger. |
| [`east-tennessee-two-site-farm-business-plan-executive-summary.md`](east-tennessee-two-site-farm-business-plan-executive-summary.md) | One-paragraph **integration** pointer. |
| [`execution-dossier-hub-phase-0-1-east-tennessee.md`](execution-dossier-hub-phase-0-1-east-tennessee.md) | Purpose block: **integration audit** link. |
| [`execution-dossier-decision-memo-phase-0-1-east-tennessee.md`](execution-dossier-decision-memo-phase-0-1-east-tennessee.md) | Governance cross-link to audit + trust bar. |
| [`../topics/business-plan-execution-and-pilot-operations-hub.md`](../topics/business-plan-execution-and-pilot-operations-hub.md) | Canonical table row for this audit. |
| [`../topics/two-site-smart-farm-operations.md`](../topics/two-site-smart-farm-operations.md) | Business-plan table row for audit. |
| [`../index.md`](../index.md) | Index line for discoverability. |
| [`../log.md`](../log.md) | **`refactor`** entry for this pass. |

---

## Assumptions strengthened

- **Two-site + batching thesis** for grazing-led work on a **rough Campbell-class** production context (WSS AOI summary in site intelligence)—still **not** a substitute for **field** fence/water/stock movement proof.
- **Homestead-as-control-center** for broker, backups, and patch cadence—**conditional** on verified **power + ISP** truth at `SITE_HOME` (Claxton intelligence + capital page sequencing).
- **Starlink / LTE as WAN**, not field RF—consistent across connectivity dependency maps and smart-tech strategy.
- **Telemetry ROI skepticism** reinforced with **explicit** sensor power/degraded-mode and triage routing (checklist matrix + stop rules).

---

## Assumptions still weak, blocked, or parcel-gapped

- **Exact ~120 ac operating boundary**, internal lanes, septic/soil per field, live pump/well tests, and **haul/processor math** remain **open** until field worksheets + register rows close ([`Claxton and Demory — missing data register`](claxton-and-demory-missing-data-register.md), [`Parcel evidence intake workflow`](parcel-evidence-intake-and-validation-workflow-east-tennessee-two-site.md)).
- **Debt capacity, household cash need (`HH_NEED`), and effective family FTE** remain **family evidence**, not wiki-filled numbers.
- **Longhorn / central storage HA** choices stay **scope-gated** by platform decision memo and pilot maturity—business plan states **pilot-ready vs overbuilt** without prescribing SKUs.

---

## New or elevated risks / sequencing implications

- **R16 (new)**: Concurrent **WAN brownout** + **battery/autonomy stress** can invalidate “remote triage saves trips” unless **local-first** state, **manual SoT**, and **trust-bar** remote rules hold.
- **Earlier explicit earthwork / lane / drainage peers** with fence/water on `SITE_FARM` when terrain evidence is adverse (already partially in capital/risk—now echoed in framework unknowns).
- **Field verification** is a **first-class** Phase 0–1 deliverable channel—not optional “nice photos.”

---

## Related canonical artifacts (unchanged scope; routing targets)

- [`Local evidence package — East Tennessee two-site`](../topics/local-evidence-package-east-tennessee-two-site.md)
- [`Procedural guides package strategy`](../topics/procedural-guides-package-strategy-smart-farm-wiki.md)
- [`Operational standards — farm and homelab platform`](../topics/operational-standards-farm-homelab-platform.md)

---

## Status

**Closed** for 2026-04 integration pass: ledger captured; further doctrine changes should **edit chapters + append a dated subsection here** or spawn a **new dated audit** only if the delta is large enough to warrant a second ledger (avoid parallel strategy essays per [`AGENTS.md`](../../AGENTS.md) canonicalization rule).

**Follow-on**: [`Execution gates — Phase 0–1 (East Tennessee two-site)`](execution-gates-phase-0-1-east-tennessee-two-site.md) (EG gate tables) — operational **pilot vs production** pass/fail system derived from this narrowing (2026-04-28).
