---
title: Dual-site operations model — non-agritourism farm business
page_type: analysis
status: active
created: 2026-04-21
updated: 2026-04-21
aliases:
  - Dual-site operations model (non-agritourism)
tags:
  - two-site
  - operations
  - logistics
review_status: unreviewed
confidence: low
---

# Dual-site operations model — non-agritourism farm business

## Purpose

Give a **first-draft operational model** for running a farm business split across **two sites**—a smaller **homestead** (`SITE_A_LABEL`) and a larger **production holding** (`SITE_B_LABEL`) separated by **`COMMUTE_TIME_ONE_WAY`**—when **revenue is not primarily lodging or guest stays**. The goal is to make **batch work, equipment placement, fuel, cold chain, and coverage** explicit so decisions are not unconsciously copied from a **guest-led** dual-site scenario.

## Scope

- **In scope**: Production logistics, commute batching, where **fixed assets** might live, **coverage** when the owner is at the other site, and **questions** to resolve before capital spend.
- **Out of scope**: Specific enterprises (row crops, livestock species, etc.) except as **placeholders**; legal/tax structure (link to checklist only); precision marketing.

## Assumptions (edit for your situation)

| Placeholder | Meaning |
|-------------|---------|
| `SITE_A_LABEL` | Homestead / family base (e.g. ~5 acres)—**placeholder size**. |
| `SITE_B_LABEL` | Farm business parcel (e.g. ~120 acres)—**placeholder size**. |
| `COMMUTE_TIME_ONE_WAY` | Typical one-way drive time (e.g. **35 minutes**)—adjust. |
| `PRIMARY_ENTERPRISE` | Main income activity **other than** lodging—**TBD**. |
| `CRITICAL_ANIMALS_OR_NONE` | Whether **livestock** require **daily eyes-on** at `SITE_B_LABEL`—**TBD**. |

## Key questions

1. **Where does the work happen?** Which tasks **must** be on `SITE_B_LABEL` vs can be done from `SITE_A_LABEL` (planning, phone, parts ordering)?
2. **Batch vs daily**: Which operations tolerate **2–3×/week** visits vs require **daily** presence? If daily, what is the **minimum on-site minutes**?
3. **Equipment home base**: Where do **tractor, truck, trailer, fuel, tools** sleep? Moving them has a **time tax** every move.
4. **Cold chain and wash/pack**: If you harvest or process perishables, where is **cooling** authoritative? Splitting cold storage without a plan creates **spoilage and food-safety** risk.
5. **Emergency response**: If an animal is down, a water line fails, or a gate is wrong, who is **physically available** within **`EMERGENCY_RESPONSE_MINUTES`** of `SITE_B_LABEL` when you are not there?
6. **Vendor and service routes**: Will **vet, feed delivery, equipment dealer** visit `SITE_B_LABEL` reliably, or do you become the **logistics layer** for every input?

## Decision criteria (practical)

| Decision | Prefer this when… | Red flag |
|----------|-------------------|----------|
| **Heavy fixed infrastructure on `SITE_B_LABEL`** | Enterprise revenue **requires** field presence; commute would burn **unacceptable** hours | Capital sits **idle** because visits are too infrequent |
| **Consolidate fuel/tools on one site** | Same crew moves between sites; **theft** or **weather** exposure is a concern | Duplicate expensive inventory **without** a written **custody** rule |
| **Hire/part-time coverage at `SITE_B_LABEL`** | Daily animal or irrigation checks are non-negotiable | No **SOP** or contact list—coverage is “hope” |

## First-draft operating picture (placeholders)

**Weekly rhythm (example skeleton—not your calendar):**

- **Fixed batch days**: `BATCH_DAY_1`, `BATCH_DAY_2` = long work sessions at `SITE_B_LABEL` (field, livestock moves, repairs).
- **Light touch days**: quick checks (water, fences, gates)—target **max minutes** on site if possible.
- **No-go**: assuming **automation replaces** daily welfare checks without a **coverage matrix**—see [`Weekly coverage matrix — two-site farm operations`](weekly-coverage-matrix-two-site-farm-operations.md).

**Contrast (explicit):** [`Agritourism business plan — guest hub on 120 acres, family home 35 min away`](agritourism-dual-site-business-plan-five-and-120-acres.md) optimizes **guests + animals + coverage** for a **lodging-led** model. This page assumes **production-led** economics; **do not** copy guest/caretaker logic without validating **animal and asset** needs.

## Connects the strands

| Strand | How this page connects |
|--------|-------------------------|
| **A (land/livestock)** | **Batch** vs **daily** presence drives **pasture** and **animal** placement; links [`Farm stocking…`](farm-stocking-120-acres-vs-5-acres-research-prompt.md). |
| **B (business)** | **Cold chain**, **fuel**, **vendor routes**—inputs to [`CAPEX, OPEX, and enterprise sequencing — two-site constraint`](capex-opex-enterprise-sequencing-two-site-constraint.md). |
| **C–D (telemetry/records)** | **Where** tools and **telemetry** live—feeds [`Field telemetry reference architecture — homestead + 120-acre farm`](field-telemetry-reference-architecture-homestead-120ac.md) and [`Farm spatial model and asset registry standard`](farm-spatial-model-and-asset-registry-standard.md). |
| **E (power)** | **Generator** / **grid** at which site for **batch** work vs **remote** monitoring. |

**Ingest (economics / planning)**: UT budget PDFs—[`source-notes/ut-extension-fm-boot-2017-budgets-velandia-pdf.md`](../source-notes/ut-extension-fm-boot-2017-budgets-velandia-pdf.md), [`ut-publication-w1348-pdf.md`](../source-notes/ut-publication-w1348-pdf.md)—support **sequencing** decisions, not **your** numbers until filled.

## Links to related future or existing pages

- [`Strategic audit — decision-safe operations for a two-site smart farm`](strategic-audit-decision-safe-operations.md) — gap framing.
- [`Farm stocking — 120 acres vs 5 acres (research prompt)`](farm-stocking-120-acres-vs-5-acres-research-prompt.md) — scale questions; **not** prescriptions.
- [`Weekly coverage matrix — two-site farm operations`](weekly-coverage-matrix-two-site-farm-operations.md) — scheduling layer.
- [`Field telemetry reference architecture — homestead + 120-acre farm`](field-telemetry-reference-architecture-homestead-120ac.md) — what remote visibility **can** change about visit frequency (**cannot** replace welfare SOPs).
- [`Spatial data and farm asset registry standard`](farm-spatial-model-and-asset-registry-standard.md) — where **equipment and gates** are known entities.
- [`Automation degraded modes and manual fallback SOP`](automation-degraded-modes-manual-fallback-sop.md) — when **automation is wrong or offline**.
- Future: **CAPEX/OPEX and enterprise sequencing — two-site constraint** (see [`Implementation backlog — strategic audit (P0–P3)`](implementation-backlog-strategic-audit.md)).

## Open items

- [ ] Fill placeholders (`SITE_*`, commute, enterprise).
- [ ] List **non-negotiable daily** tasks at `SITE_B_LABEL`.
- [ ] Decide **equipment home** and document in asset registry standard.

---

*First draft: placeholders only; revise with real constraints and professional advice where safety, animal welfare, or food safety apply.*
