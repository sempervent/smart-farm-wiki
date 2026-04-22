---
title: Phase 0–1 operator burden review — East Tennessee two-site (hostile)
page_type: analysis
page_subtype: query_synthesis
status: active
created: 2026-04-29
updated: 2026-04-29
review_status: unreviewed
confidence: medium
tags:
  - business-plan
  - labor
  - operations
  - two-site
  - east-tennessee
  - phase-0-1
  - operator-burden
---

# Phase 0–1 operator burden review — East Tennessee two-site (hostile)

## Stance

**Default failure mode**: the plan is **under-budgeted** on **operator hours**, not **under-documented**. Hidden burden is **normal**: travel, corrosion, battery anxiety, alert triage, restore drills, and “quick checks” from the phone **compound** while the family still has **jobs**, **school**, and **weather**.

This page **does not** add new gates (see [`Execution gates — Phase 0–1`](execution-gates-phase-0-1-east-tennessee-two-site.md)); it **names load** so EG passes are not confused with **free time**.

---

## Burden lenses (what to evaluate)

### Travel time

**Recurring**: **~70 min** round-trip **cab time** per **batch** visit before productive work at **`SITE_FARM`** ([`Two-site operations model`](two-site-operations-model-5ac-homebase-120ac-production.md)). **Surge**: bad weather, detours, trailer, stuck gate = **P90** blows the spreadsheet.

**Doctrine that helps**: distance-tax rules, trip batching policy, **P1** instrumentation ordering (water/gate class first).

**Still thin**: “two visits/week” as **calendar** truth without **logged** **τ_ctx** (gear, fuel, boots) and **night** emergencies **outside** batch windows.

### Field maintenance

**Recurring**: fence, vegetation, culverts, **lane** surface on **sloped** ground ([`Demory site intelligence`](demory-farm-site-intelligence.md)). **Surge**: storm washouts, escape repair.

**Doctrine**: site intelligence + capital sequencing peers earthwork with fence/water.

**Thin**: **O&M $/hr** for **internal roads** as a **first-class** line next to fence O&M (often **lumped** or ignored).

### Off-grid power upkeep

**Recurring**: terminals, corrosion, **BMS** quirks, inverter warnings, **genset** policy if any, **SOC** discipline. **Surge**: prolonged cloud, heat, **cold** derates, **equipment** failure stacking with **livestock** stress.

**Doctrine**: [`Off-grid operational decision rules`](off-grid-operational-decision-rules-power-and-networking-demory-farm.md), [`Power domains and battery-backed tiers`](off-grid-power-domains-and-battery-tiers-demory-farm.md), degraded modes.

**Thin**: **night** response when **telemetry says fine** but **physics** disagrees—trust in dashboards vs **mandatory** physical rounds under stress is **under-modeled emotionally**.

### Sensor upkeep and failure handling

**Recurring**: battery swaps, antenna aim, critter damage, firmware drift, **false negatives** (worst case). **Surge**: **every** sensor looks guilty during a welfare event.

**Doctrine**: observe-first Phase 1, stop rules **NS** family, single-pilot scope ([`Execution gates`](execution-gates-phase-0-1-east-tennessee-two-site.md) **EG-SNS**), sensor checklist matrix.

**Thin**: **spares** policy **time** (who drives which spare to which pole at 21:00) is rarely written until after first failure.

### Gateway / controller upkeep

**Recurring**: power cycling stuck radios, **SD** corruption class failures, **config** drift, **TLS** expiry on edge. **Surge**: “gateway down” = **blind** **until** someone is on-site.

**Doctrine**: field-node classes, one RF class pilot, local-first / WAN-optional model.

**Thin**: **two-site** means **two** places things break—**homelab** patch night **same week** as **120** gateway swap is **optimistic** without naming **who** loses sleep.

### Backup and restore obligations

**Recurring**: backup job monitoring, **restore** tests, credential rotation, **ticket** hygiene. **Surge**: **actual** restore during calving week.

**Doctrine**: [`Kubernetes platform backup/DR — Pi k3s Longhorn`](kubernetes-platform-backup-dr-pi-k3s-longhorn.md), backup cadence standards, **EG-PLT** gates.

**Thin**: “**P0/P1** checklist green” is still **hours** and **stress**; families **overweight** “automated backup = safe” and **underweight** **restore rehearsal** **labor**.

### Observability and alert triage

**Recurring**: Alertmanager routing changes, silences discipline, **dashboard** hygiene, **log** volume growth. **Surge**: alert storms during WAN/power transitions.

**Doctrine**: [`Observability, secrets, and trust bar`](observability-secrets-and-trust-bar-homelab-farm-edge.md), inhibition / welfare vs convenience split, **CS-4**.

**Thin**: **On-call** is often **implicitly** the same person who already drives **120** twice this week—**no** modeled **collision** between **NOC hat** and **field hat**.

### Family labor reliability

**Recurring**: weekly rhythm **fiction** until **V11** proves otherwise. **Surge**: illness, job travel, school events.

**Doctrine**: labor model falsifiers, coverage matrix, **EG-LAB** gates.

**Thin**: **three-generation** optimism—**correlation** of absence events is **not** independence; **overlap** weeks happen.

### Weather / outage / degraded-mode workload

**Recurring**: seasonal adjustments. **Surge**: ice, mud, **multi-day** outage stacks **WAN + power + water** simultaneously ([`Risk register`](east-tennessee-two-site-farm-business-plan-risk-register.md) **R16**).

**Doctrine**: manual fallback SOPs, off-grid degraded modes, runbooks.

**Thin**: **Drills** are **work**; if drills are not scheduled, degraded posture is **theoretical** and **burden** shows up as **panic**.

---

## Burden classes (summary)

| Class | Examples |
|-------|----------|
| **Recurring** | Trips, triage, patch windows, fence/road minutes, backup checks |
| **Surge** | Escape, storm, processing squeeze, simultaneous gateway + power fault |
| **Invisible** | Context switching, “quick phone checks,” shame-driven dashboard refreshes, credential hunting, waiting on vendor forums, **coordination tax** between two sites |

---

## Master burden table (Phase 0–1)

**Severity**: **H** = high (can dominate a week), **M** = medium, **L** = low **if** disciplined. **Who**: family role placeholders—**replace with names** locally.

| Burden source | Severity | Who carries it (default) | Mitigation | Recommendation |
|---------------|----------|---------------------------|------------|-----------------|
| **Round-trip travel tax** | H | Field lead + vehicle time | Batch; telemetry on P1 loads; honest P90 logging | **Simplify** enterprise choices; **defer** daily-touch crops; **outsource** custom hire for peak moves where cheaper than marginal trip |
| **Lane / drainage / gravel O&M** | M–H | Field lead | Peer with fence plan; register rows | **Defer** “pretty” projects; **simplify** internal movement plan until measured |
| **Battery / inverter / BMS attention** | M–H | Tech lead + field lead | Bracket loads (**DR-1**); degraded SOPs; training | **Defer** always-on RF/WAN sprawl; **automate** only **non-welfare** annunciators where safe; **outsource** electrical work per code |
| **Sensor false positives / negatives** | M–H | Tech lead (triage), Field lead (ground truth) | NS stops; one pilot; corroboration rules | **Simplify** to fewer signals; **defer** second class; kill pilot per ROI |
| **Gateway / RF maintenance** | M | Tech lead | Spares kit; one-class pilot; documented power cycle | **Defer** mesh fleet; **simplify** topology; **outsource** tower work if any |
| **Backup/restore + DR rehearsal** | M | Tech lead | Calendar drills; narrow RPO claim | **Defer** HA fantasies; **simplify** what is “in cluster”; treat restore as **scheduled labor** |
| **Observability / alert routing** | M | Tech lead | Inhibition; welfare vs convenience routing; mute policy | **Simplify** receivers; **defer** Alloy/log pipeline expansion; **outsource** MSP only if budgeted |
| **Degraded / outage drills** | M | Whole family (rotates) | Written drill card; seasonal window | **Simplify** drill scope; **defer** new systems until one drill passes; do not **automate** away physical welfare checks |
| **Coverage gaps (surge)** | H | Ops lead “absorbs” until burnout | Coverage matrix rows; hire/neighbor | **Simplify** herd/enterprise; **defer** expansion; **outsource** key surge slices |
| **Concurrent WAN + power stress** | H | Tech + field (R16) | Local-first; manual SoT; trust bar | **Defer** remote actuation; **simplify** cloud dependence |

---

## Verdict (skeptical)

The **narrowed** Phase 0–1 scope is **directionally** right—**observe-first**, **WAN-optional**, **single pilots**, **EG** gates—but **still optimistic** if the family does not **book** triage hours, **road** minutes, **power** anxiety checks, and **restore** drills as **first-class calendar items** alongside field work.

**Most under-modeled**: **collision** between **homelab ops nights** and **field surge weeks**, and **invisible** phone triage that **eats** batching gains.

---

## Related

- [`Labor model and weekly operating rhythm`](east-tennessee-two-site-farm-business-plan-labor-and-family-model.md)
- [`Risk register and mitigation strategy`](east-tennessee-two-site-farm-business-plan-risk-register.md)
- [`Observability, secrets, and trust bar — homelab / farm edge`](observability-secrets-and-trust-bar-homelab-farm-edge.md)
- [`Automation stop rules — two-site smart farm`](automation-stop-rules-two-site-smart-farm.md)
- [`Execution gates — Phase 0–1 (East Tennessee two-site)`](execution-gates-phase-0-1-east-tennessee-two-site.md)
- [`Instrumentation ROI model — two-site smart farm`](instrumentation-roi-model-two-site-smart-farm.md)
