---
title: First 90 days — operator packet (East Tennessee two-site)
page_type: analysis
page_subtype: operational_guide
status: active
operational_maturity: pilot_ready
created: 2026-04-30
updated: 2026-04-30
review_status: unreviewed
confidence: medium
tags:
  - business-plan
  - execution
  - phase-0-1
  - two-site
  - east-tennessee
  - operator
---

# First 90 days — operator packet (East Tennessee two-site)

## What this is

A **bounded**, **field-facing** runbook for the **first 12 weeks after T0**—**pilot execution only**. It does **not** replace the narrative arc on [`First 90 days — Phase 0–1`](execution-first-90-days-phase-0-1-east-tennessee.md); it **packages** what the operator actually does each week, what **evidence** must exist, and when to **stop**.

**Pilot justification (explicit)**: **Pilot** work is justified when **T0** is set on the [`Decision memo`](execution-dossier-decision-memo-phase-0-1-east-tennessee.md), the family stays inside **Approved now** + **Approved only for pilot**, and **EG** rows are pursued at **pilot** bar—not **production** / **G1** posture ([`Execution gates — Phase 0–1`](execution-gates-phase-0-1-east-tennessee-two-site.md)). **Do not** treat this packet as permission for **Forbidden** rows on the memo.

**Aligns with**: narrowed Phase 0–1 scope · EG gates · [`Field verification program — Phase 0–1`](field-verification-program-phase-0-1-claxton-demory.md) · [`Operator burden review (hostile)`](phase-0-1-operator-burden-review-east-tennessee-two-site.md) · decision memo.

**Out of scope here**: months 4–24 detail, Phase 2 CAPEX, herd scale, salary narrative—use [`First 12 months`](execution-first-12-months-phase-0-1-east-tennessee.md) after day 90.

---

## Weekly priorities (weeks 1–12)

**Rule**: Each week, pick **at most one** “hard” slice (long drive + heavy field) unless surge—[`Operator burden review`](phase-0-1-operator-burden-review-east-tennessee-two-site.md).

| Week | Priority theme | Ship this week (max 3 outcomes) |
|------|----------------|----------------------------------|
| **1** | **T0 + books + stop rules** | T0 date on memo; hour log week 1 started; vision stop-rule **template** copied locally |
| **2** | **Legal surface + map authority** | V8 **started** (ticket/letter path); one **canonical** map layer name; trip purpose codes started |
| **3** | **Labor truth** | V11 week 3 logged; coverage matrix **holes named** (no heroics) |
| **4** | **Checkpoint A** | [Decision checkpoints](#decision-review-checkpoints); adjust week 5–8 if overload |
| **5** | **Land intel (cheap)** | V1 **desktop** + first **Demory** walk tied to field program **§1**; V3 photos **started** |
| **6** | **Water + access** | V2 question list moving; water points on map (**I1**); bad-weather **access** log **once** |
| **7** | **Markets paper** | V5 **first** sale bills; V6 **first** processor call log row |
| **8** | **Checkpoint B** | **EG-LEV** pilot pass honest? **NS-2** triage budget real? Trim pilots if not |
| **9** | **Insurance + haul** | V9 quotes collected; B3 haul bracket **documented** as range, not fantasy |
| **10** | **Connectivity (pilot)** | V10 **pin** screenshots **started**; WAN placement/obstruction log per first-90-days connectivity table |
| **11** | **G8 + comms stability** | Manual water (or chosen G8 asset) log **in progress** or **complete**; **no** second sensor class |
| **12** | **Checkpoint C + handoff** | Day-90 “done enough” items from [`First 90 days` § End of day 90](execution-first-90-days-phase-0-1-east-tennessee.md) checklist; schedule **first 12 months** review |

---

## Field verification tasks (mapped)

Execute rows from [`Field verification program`](field-verification-program-phase-0-1-claxton-demory.md) **in this order of emphasis**—**not** all sections every trip.

| Week band | **Demory** (`SITE_FARM`) emphasis | **Claxton** (`SITE_HOME`) emphasis |
|-----------|-------------------------------------|--------------------------------------|
| **1–4** | **§1** orienting + boundary/fence walk starter; **§2** access lane **photo** | **§4–5** utility / ISP / OSSS **truth** path **started** (desktop + any field) |
| **5–8** | **§3** drainage / sediment **eyes** after rain if possible; **§1** fence segments deepen | Same + **§6** gateway **location** **paper** only unless pilot already approved |
| **9–12** | **§4–5** power / pump **spot** checks **without** new always-on RF; **§7** sensor **mount** sites **scout** only | **§6** homelab / WAN **power** intent for CPE |

**Cadence**: Follow field program **§ “Bundling”**—every Demory trip bundles access + one infra slice.

---

## Infrastructure setup tasks (90-day cap)

| Task | Site | Done when | Gate / stop |
|------|------|-----------|-------------|
| **Primary route bad-weather log** | Demory | **One** logged attempt or **documented** deferral with date | Supports **EG-SITE-2** pilot |
| **Water points on map** | Demory | All known points pinned + **Unknown** list | **V2** / **I1** |
| **CPE / WAN power intent** | Claxton | Ticket or **two-person** shutdown story on paper | Connectivity table **Days 31–60** row |
| **Spot fence / escape fix** | Demory | **Only** safety per memo **pilot** infra row—**not** perimeter MVP | Memo **Forbidden** guard |

---

## Sensor / network / platform tasks (90-day cap)

| Task | Done when | Stop |
|------|-----------|------|
| **Declare stack scope** | **EG-PLT-0**: written “no k3s” **or** “k3s pilot = {nodes}” | If undeclared, **freeze** cluster feature creep |
| **G8 manual baseline** | Asset chosen; paper/spreadsheet log **started** week **≤8**; complete **by T0+120d** if not by day 90 | **No** sensor install without baseline path |
| **One RF / one gateway pilot** | Matches **DR-5** class scope; **no** second farm WAN / HaLow while **DR-1** open | **CS-5** |
| **V10 cell at pins** | Notebook/screenshots **started** week **≤10** | **No** “telemetry drives trips” claim without V10 track |
| **Triage time budget** | **H_TRIAGE_BUDGET_WK** set in ROI worksheet or family equivalent | **NS-2** |

---

## Documentation updates required

| Artifact | Owner | By |
|----------|-------|-----|
| [`Missing data register`](claxton-and-demory-missing-data-register.md) rows | Ops lead | **Weekly** status + owner (**EG-LEV-1**) |
| [`Local evidence package`](../topics/local-evidence-package-east-tennessee-two-site.md) tables | Ops lead | After **each** field visit bundle |
| Hour log (**V11**) | Named family | **Weekly** through week **≥8** inside 90d window |
| WAN / reliability notebook | Tech lead | First entry by **day 30**; weekly by **day 90** |
| Pilot **one-pager** (one sensor class, kill threshold) | Tech lead | **Before** any install (**EG-SNS-2**) |

---

## Stop conditions (non-exhaustive)

**Freeze or cut** the week’s plan if **any** apply—then **document** and **reschedule**:

- [`Decision memo`](execution-dossier-decision-memo-phase-0-1-east-tennessee.md) **Forbidden** row would be violated by the next action.
- **EG** **pilot** fail in a domain you are about to spend in (e.g. register orphan rows before claiming “ready for contractor talk”).
- [`Automation stop rules`](automation-stop-rules-two-site-smart-farm.md) **NS-1–NS-3**, **CS-1**, **CS-4**, **CS-5** after one remediation attempt.
- [`Operator burden review`](phase-0-1-operator-burden-review-east-tennessee-two-site.md) **collision** week: **Tech lead** and **Field lead** same person and **both** had surge—**drop** one pilot thread.
- **R17** signal: triage + field + off-grid **same** week with **no** coverage—invoke coverage matrix **or** cancel non-welfare work.

---

## Evidence collection requirements

| By | Minimum evidence | Feeds |
|------|------------------|--------|
| **Day 30** | V8 path **started**; V11 **≥4** weeks; map authority; **one** Demory field visit log (**field program**); WAN obstruction/placement log **started** | **EG-SITE-1** pilot, **EG-LEV-2** pilot |
| **Day 60** | V1 + V3 **usable** for conversation (not perfect); V5/V6 **first rows**; V10 notebook **started** | **V** tasks; first-90-days days **31–60** |
| **Day 90** | First-90-days **end checklist** satisfied **or** **dated** slip with **which** item carries to **T0+120d** | Handoff to **First 12 months** |

---

## Decision review checkpoints

| When | Review questions (family) | Outcome |
|------|----------------------------|---------|
| **End week 4** | Still inside memo **Approved** / **pilot** only? Any **Forbidden** pressure? **EG-LEV** pilot rows **owned**? | **Adjust** weeks 5–8 scope |
| **End week 8** | **V11** on track for **8** weeks total? **NS-2** triage budget real? **Exactly one** telemetry pilot thread? | **Kill** or **defer** sensor/WAN extras |
| **End week 12** | First-90-days end checklist met **or** slips **dated**? **G8** done **or** scheduled by **T0+120d**? **No** **G1** / production composite claimed without evidence? | **Written** plan for days **91–180**; handoff to [`First 12 months`](execution-first-12-months-phase-0-1-east-tennessee.md) |

---

## Related

- [`Phase 0–1 operator burden review — East Tennessee two-site (hostile)`](phase-0-1-operator-burden-review-east-tennessee-two-site.md)
- [`First 90 days — Phase 0–1 execution`](execution-first-90-days-phase-0-1-east-tennessee.md)
- [`Decision memo — Phase 0–1`](execution-dossier-decision-memo-phase-0-1-east-tennessee.md)
- [`Execution gates — Phase 0–1 (East Tennessee two-site)`](execution-gates-phase-0-1-east-tennessee-two-site.md)
- [`Execution dossier — Phase 0–1 (hub)`](execution-dossier-hub-phase-0-1-east-tennessee.md)
- [`Master checklist — Phase 0–1`](execution-dossier-master-checklist-phase-0-1-east-tennessee.md)
