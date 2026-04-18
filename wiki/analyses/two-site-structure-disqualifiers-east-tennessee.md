---
title: Two-site structure disqualifiers — East Tennessee smart farm package
page_type: analysis
status: active
created: 2026-04-21
updated: 2026-04-21
review_status: unreviewed
tags:
  - two-site
  - business-plan
  - east-tennessee
  - enterprise-selection
confidence: medium
---

# Two-site structure disqualifiers — East Tennessee smart farm package

## Purpose

List **enterprise and operating patterns** that are **structurally poor fits** for **`SITE_HOME` (~5 ac) + `SITE_FARM` (~120 ac)** with **`COMMUTE_ONE_WAY` ≈ 35 min**—**without** softening that split. Use this as a **hard filter** before debate, CAPEX, or “we’ll figure it out in the truck.”

**Consumes**: [`Two-site operating model — 5 ac / 120 ac`](two-site-operations-model-5ac-homebase-120ac-production.md), [`Trip batching and site visit policy`](trip-batching-and-site-visit-policy-two-site-smart-farm.md), [`Enterprise unit economics`](enterprise-unit-economics-worksheet-methodology-two-site-smart-farm.md).

**Feeds**: [`Enterprise options analysis`](east-tennessee-two-site-farm-business-plan-enterprise-options-analysis.md), [`Recommended enterprise strategy`](east-tennessee-two-site-farm-business-plan-recommended-enterprise-strategy.md), [`Execution gates — financial thresholds`](execution-gates-financial-thresholds.md).

---

## Definitions

| Term | Meaning |
|------|---------|
| **Baseline labor** | Family + agreed **hired** pattern in the **business plan**—**not** “hero mode” |
| **Resident** | A person **living** at or adjacent to `SITE_FARM` **as part of the plan**—**not assumed** unless documented |
| **Junk trip** | Visit **without** prior **work order** **and** **without** open **Tier-1** condition ([`trip policy`](trip-batching-and-site-visit-policy-two-site-smart-farm.md)) |

---

## Category A — Enterprise patterns (structural misfits)

**Unless** **remediated** by **resident labor**, **full-time crew**, or a **fundamentally different** commute geometry, treat as **disqualified** for **primary** reliance.

| ID | Pattern | Why it breaks |
|----|---------|----------------|
| **DQ-E1** | **Daily** harvest / **daily** pack-and-ship **vegetables or perishables** at `SITE_FARM` | **T3** touch class—**35 min** makes **daily** presence **default**; **R_SPLIT** explodes |
| **DQ-E2** | **Dairy-style** or **frequent milking / collection** rhythm **without** parlor at `SITE_HOME` | Same—**time-locked** visits |
| **DQ-E3** | **Intensive** small ruminants **as primary** with **high** handling + predation pressure **and** **no** resident coverage | **More trips** than beef baseline; see enterprise options **Path B** drag |
| **DQ-E4** | **Mechanical hay as primary income** on **this** acreage **without** **sleep-near-field** or **crew** in **weather windows** | **Peak** weeks **collide** with commute—**structural** |
| **DQ-E5** | **Agritourism / events primary** with **guest** expectations **across** both sites **without** staff | **Presence** + **logistics** tax; see [`Agritourism dual-site`](agritourism-dual-site-business-plan-five-and-120-acres.md) **only** as alternate **explicit** scenario |
| **DQ-E6** | **Orchard / perennial primary** when **near-term** salary replacement is **required** | **Years** to revenue—**bridge** must be explicit, not hope |
| **DQ-E7** | **“We’ll do a bit of everything”** with **no** **80%** primary enterprise | **Complexity** + **trips**—[`Vision` scope creep](east-tennessee-two-site-farm-business-plan-vision-and-constraints.md) |

**Remediation (only if honest)**

| ID | Remediation | Still subject to |
|----|-------------|-------------------|
| **R-E1** | **Resident** manager or **full-time** employee at `SITE_FARM` | Labor economics + **MVCM** |
| **R-E2** | **Lease/custom** **or** **tenant** operation on acres that **cannot** be served by batching | **Contract** quality + **field checks** still bounded |
| **R-E3** | **Change geometry** (move home, buy adjacent, shorten commute)—**rare** | Full **capital** + life decision |

---

## Category B — Operating patterns (self-disqualifying behaviors)

| ID | Pattern | Why it breaks |
|----|---------|----------------|
| **DQ-O1** | **Ad-hoc** trips “**to check**” when **telemetry** could answer | **Junk trips** → margin + **morale** |
| **DQ-O2** | **No** **work-order** discipline (nothing written before wheels roll) | **Cannot** measure **`H_VISIT`**, **`R_SPLIT`**, or improvement |
| **DQ-O3** | **Alert-driven** lifestyle (**constant** pings) **without** **triage** SOP and **H_TRIAGE** cap | [`Enterprise unit economics`](enterprise-unit-economics-worksheet-methodology-two-site-smart-farm.md)—**telemetry becomes second job** |
| **DQ-O4** | **Splitting** “**brain**” across **two** competing **systems of record** | **Duplication** trips + **errors** |
| **DQ-O5** | **Equipment** that **forces** **solo** **field** work **during** **off-farm** job hours **every** week | **Unsustainable**—either **batch**, **hire**, or **defer** |

---

## Category C — Telemetry / “smart” traps

| ID | Pattern | Why it breaks |
|----|---------|----------------|
| **DQ-T1** | **Cameras** / **maps** **without** **named** assets + **runbooks** | **Triage** hell—[`Instrumentation ROI`](instrumentation-roi-model-two-site-smart-farm.md) |
| **DQ-T2** | **Sensors** on **non-critical** loads **before** **water / power / gate** truth | **OPEX** + **attention** for **no** trip reduction |
| **DQ-T3** | **Homelab** complexity **that** **increases** **H_TRIAGE** above policy cap | **Fails** financial + labor gates |

---

## How to use this page (decision drill)

1. **Name** candidate enterprise → assign **touch tier** (T0–T3) per [`two-site operating model`](two-site-operations-model-5ac-homebase-120ac-production.md).
2. **Check** **Category A** — if **hit**, **stop** or **remediate** with **written** structural change.
3. **Compute** **`Δ_OPEX_SPLIT`** + **`R_SPLIT`** when numbers exist—**SPLIT-1** fail → **no scale** debt ([`CAPEX/OPEX sequencing`](capex-opex-enterprise-sequencing-two-site-constraint.md)).
4. **Review** **Category B** quarterly—**behaviors** are **early warning** before **P&L** shows damage.

---

## Related

- [`Own equipment vs custom hire`](../comparisons/own-equipment-vs-custom-hire-two-site-logistics.md)
- [`Validation backlog — before major spend`](validation-backlog-before-major-spend-two-site-smart-farm.md)
- [`Family labor model and coverage matrix`](family-labor-model-and-coverage-matrix-two-site-smart-farm.md)
