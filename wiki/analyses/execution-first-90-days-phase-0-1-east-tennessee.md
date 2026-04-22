---
title: First 90 days — Phase 0–1 execution (East Tennessee two-site)
page_type: analysis
status: active
created: 2026-04-21
updated: 2026-04-30
review_status: unreviewed
tags:
  - business-plan
  - execution
  - two-site
confidence: medium
---

# First 90 days — Phase 0–1 execution (East Tennessee two-site)

## Purpose

**Actionable** first **90 days** after **T0** (execution start—[`dossier hub`](execution-dossier-hub-phase-0-1-east-tennessee.md)). **Pilot-grounded** tasks only; **no** **scale** bets.

**Boundaries**: [`Decision memo — Phase 0–1`](execution-dossier-decision-memo-phase-0-1-east-tennessee.md). **Ordered tasks**: [`Master checklist`](execution-dossier-master-checklist-phase-0-1-east-tennessee.md).

**Operator packet (canonical runbook)**: [`First 90 days — operator packet (East Tennessee two-site)`](first-90-days-operator-packet-east-tennessee-two-site.md) — **weeks 1–12** priorities, field verification bundling, infra/sensor caps, documentation, **stop** conditions, evidence by day **30/60/90**, decision checkpoints—**pilot** stance aligned with **EG** gates and [`Operator burden review (hostile)`](phase-0-1-operator-burden-review-east-tennessee-two-site.md).

**Connectivity validation (WAN / Starlink track)** — survey, power, reliability log, remote-access readiness, cost lines: [`Validation and pilot plan` § Connectivity validation](validation-and-pilot-plan-first-24-months-east-tennessee-two-site.md#connectivity-validation) · [`Connectivity strategy — Claxton & Demory`](connectivity-strategy-for-claxton-and-demory.md). **Parallel** tasks below **overlap** **V10** **and** **G8**.

**Local evidence**: **Days 15–30** **V1** on **Demory** / **Campbell** must **reconcile** processed WSS AOI (large, **sloped**) with **~120 ac** **operating** map—[`Demory site intelligence`](demory-farm-site-intelligence.md). **Claxton** / **Anderson**: **open** **WSS** on **homestead** AOI; **no** vault substitute.

---

## Days 1–14 — Baseline, books, legal surface

| Focus | Do | Closes / unlocks |
|-------|-----|------------------|
| **Stop rules** | Copy numeric **triggers** from [`Vision`](east-tennessee-two-site-farm-business-plan-vision-and-constraints.md) into **one** family-visible doc | Shared **abort** rules |
| **Books** | Start **chart of accounts** skeleton per [`Farm accounting baseline`](farm-accounting-baseline-chart-of-accounts-enterprise-pl-two-site-smart-farm.md) | **Receipt** discipline |
| **Land use / zoning** | **V8** started: county / use call or letter path | **Structures** and **on-farm** sales **risk** surfaced |
| **Labor truth** | **V11** started: **week 1** of **8-week** hour log (see **W1** on [`checklists`](pilot-and-recon-checklists-first-24-months-two-site-smart-farm.md)) | **Real** **hour** **budget** |
| **Map authority** | **L1**: one **canonical** map file/layer name | **No** **orphan** **photos** |

**Do not**: Sign **major** lease for **equipment**; **commit** **herd** **scale**; **deploy** **telemetry** **beyond** **manual** **log** (**G8**).

---

## Days 15–30 — Land intelligence (cheap)

| Focus | Do | Task IDs |
|-------|-----|----------|
| **Soils / limitations** | **V1**: NRCS + walk; name **no-go** areas | V1 |
| **Fence recon** | **V3** started: **L5** segment photos + rough lengths | V3, L5 |
| **Water** | **V2** started: locate **all** points on map (**I1**); schedule **well** **report** or **pump** **test** if needed | V2, I1 |
| **Access** | Bad-weather **drive** of **primary** route; **photo** **log** | — |

---

## Days 31–60 — Markets + processing (paper)

| Focus | Do | Task IDs |
|-------|-----|----------|
| **Sale bills** | **V5** started: collect **auction** bills toward **12-week** set | V5, B1 |
| **Processing** | **V6** started: **B2** processor **call** **log** | V6, B2 |
| **Haul** | **B3** range **per** **head** (quote or **DIY**) | B3 |
| **Insurance** | **V9** quotes started | V9 |

**Kill / pivot**: Write **B5** rule if **prices** or **processing** **fail** **threshold**—[`pilot checklists`](pilot-and-recon-checklists-first-24-months-two-site-smart-farm.md#first-business-experiments).

---

## Days 61–90 — Telemetry pilot prep + labor proof

| Focus | Do | Task IDs |
|-------|-----|----------|
| **Manual water log** | **T1** **30-day** **manual** **water** **check** **completed** **or** **in** **final** **weeks** (**G8** path) | G8, T1 |
| **Comms** | **V10**: **T2** **cell** **screenshots** at **tank** / **gate** **pins** | V10, T2 |
| **One pilot sensor** | Only if **comms** **stable**: **T3** **one** **ID**, **one** **mount**—[`Instrumentation priority matrix`](instrumentation-priority-matrix-two-site-smart-farm.md) | T3 |
| **Trip log** | **W4** **two-site** **purpose** **codes** **4+** **weeks** | W4 |
| **Surge** | Schedule **or** **capture** **one** **stress** **window** toward **W2** | W2 |

---

## Days 1–90 — Connectivity validation (parallel)

| Window | Focus | Pass (minimum) |
|--------|--------|----------------|
| **Days 1–30** | **Obstruction / placement**: **photo + map** **candidates** **for** **`SITE_HOME`** **WAN** **mount** **(Starlink** **/** **CPE** **)**; **note** **trees** **/** **roof** **line** | Log **exists** **before** **hardware** **commit** **(see** [`Validation plan` § Connectivity](validation-and-pilot-plan-first-24-months-east-tennessee-two-site.md#connectivity-validation) **)** |
| **Days 31–60** | **Power / grounding**: **intent** **for** **dedicated** **branch** **/** **UPS** **for** **CPE** **+** **edge**; **surge** **at** **demarc** **on** **checklist** **or** **sparky** **visit** **scheduled** | **Two** **people** **know** **shutdown** **order** **for** **WAN** **gear** |
| **Days 61–90** | **WAN reliability testing**: **start** **weekly** **honest** **up/down** **+** **weather** **notes** **(not** **only** **bar** **icons** **)** **toward** **V10** | **Notebook** **or** **sheet** **started** **;** **one** **bad-weather** **event** **captured** **if** **possible** |
| **Before** **treating** **telemetry** **as** **trip** **input** | **Remote access hardening**: **inventory** **admin** **path** **per** [`Remote access and operational security model`](remote-access-operational-security-model-two-site-smart-farm.md) **(VPN** **/** **outbound** **tunnel** **)** | **No** **“** **inbound** **to** **field** **”** **shortcuts** **documented** **as** **production** |

**Dependency rules (90-day horizon)** — **May** **depend** **on** **Starlink** **/** **WAN** **for**: **convenience** **dashboards**, **remote** **peek**, **non-welfare** **alerts**. **Must not** **depend** **on** **WAN** **for**: **welfare** **verification**, **books** **authority** **without** **offline** **export**, **safe** **defaults** **at** **edge** **—** **full** **tables**: [`Validation plan` § Connectivity](validation-and-pilot-plan-first-24-months-east-tennessee-two-site.md#connectivity-validation).

**`SITE_FARM` / Demory (off-grid-first)** — **parallel** discipline (does not replace fence/water/G8): (1) **Capital**: no second farm WAN, HaLow segment, or always-on RF fleet until [`Capital plan` off-grid sequencing](east-tennessee-two-site-farm-business-plan-capital-and-financing.md#off-grid-demory-capital-sequencing) A–D and **DR-1** are addressed. (2) **Pilot**: one gateway + one RF class ([`Off-grid decision rules`](off-grid-operational-decision-rules-power-and-networking-demory-farm.md) **DR-5**). (3) **Stop rules**: **CS-5** freezes scope while networking load is unbudgeted vs battery. (4) **Before** remote ops are trusted at Demory: **MV-8** local-only / SOC-stressed drill ([`Automation stop rules`](automation-stop-rules-two-site-smart-farm.md)). Canonical detail: [`Off-grid power`](off-grid-power-strategy-demory-farm-site.md), [`Mesh/field networking`](mesh-and-field-networking-strategy-off-grid-demory-farm.md), [`Validation plan` off-grid gates](validation-and-pilot-plan-first-24-months-east-tennessee-two-site.md#off-grid-demory-validation-gates).

**Cost**: **Tag** **ISP** **+** **LEO** **+** **cell** **(pilot)** **in** **books** **as** **separate** **lines** **;** **first** **quarterly** **WAN** **vs** **value** **review** **no** **later** **than** **T0+90d** **(see** **CS-*** **on** [`Automation stop rules`](automation-stop-rules-two-site-smart-farm.md) **)**.

---

## End of day 90 — “Done enough” checklist

- [ ] **V8** **no** **fatal** **surprise** **or** **written** **path**
- [ ] **V1** **+** **V3** **maps** **usable** **for** **conversation** **with** **contractor** **(not** **necessarily** **built** **)**
- [ ] **V5** **+** **V6** **have** **first** **evidence** **rows** **(not** **necessarily** **complete** **)**
- [ ] **V11** **8-week** **log** **complete** **or** **in** **final** **week**
- [ ] **G8** **manual** **baseline** **complete** **or** **scheduled** **to** **complete** **≤** **T0+120d**
- [ ] **Connectivity**: **`SITE_HOME`** **placement** **/** **obstruction** **log** **started** **;** **WAN** **reliability** **notebook** **started** **(V10** **track** **)** **;** **CPE** **power** **/** **grounding** **plan** **or** **ticket** **open** **;** **remote** **access** **inventory** **started** **per** [`Validation plan` § Connectivity](validation-and-pilot-plan-first-24-months-east-tennessee-two-site.md#connectivity-validation)

---

## Next

- [`First 12 months`](execution-first-12-months-phase-0-1-east-tennessee.md)
- [`Validation and pilot plan`](validation-and-pilot-plan-first-24-months-east-tennessee-two-site.md) (full matrix)
