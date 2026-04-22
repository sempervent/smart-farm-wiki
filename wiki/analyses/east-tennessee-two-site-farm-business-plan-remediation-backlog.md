---
title: Business plan remediation backlog
page_type: analysis
status: active
created: 2026-04-17
updated: 2026-04-28
review_status: unreviewed
tags:
  - business-plan
  - risk
  - meta
  - two-site
confidence: medium
aliases:
  - ET two-site business plan remediation
---

# Business plan remediation backlog

**Source critique**: [`East Tennessee two-site farm business plan — hostile internal review`](east-tennessee-two-site-farm-business-plan-hostile-internal-review.md) — **not** superseded; this page **operationalizes** it into **repository changes** and **decision controls**. **Second-pass execution illusions**: [§7](east-tennessee-two-site-farm-business-plan-hostile-internal-review.md#7-second-pass-execution-illusions-stricter-than-2).

**Doctrine integration ledger (2026-04)**: [`Business plan integration revision audit`](east-tennessee-two-site-farm-business-plan-integration-revision-audit-2026-04.md) — what changed in the **canonical chapters** when local evidence, off-grid/WAN, sensors, platform/backup/observability, and evidence-grade routing were **bound** (not a new plan).

**Authoritative sources** (minimum ingest set, category priorities, proposed source-note titles): [`Business plan source-ingest campaign — East Tennessee two-site`](business-plan-source-ingest-campaign-east-tennessee-two-site.md).

**Hard rules**: **Over-automation**, **labor underestimation**, **revenue optimism**, and **bad sequencing** are **first-class risks**. Remedies are **specific** (tables, gates, new rows)—not “be careful.”

---

## 1. Weakness → remediation matrix

| # | Weakness | Why it matters | Severity | Proposed repository fix | Fix type |
|---|----------|----------------|----------|-------------------------|----------|
| 1 | **Salary replacement** is mostly **narrative** | Decisions (off-farm quit, debt) **without** numbers are **gambling** | **Critical** | Add **required** subsections to [`revenue model and milestones`](east-tennessee-two-site-farm-business-plan-revenue-and-phased-income.md) and [`revenue milestone model`](revenue-milestone-model-supplemental-to-salary-replacement.md): **`HH_NEED`**, **contribution margin line**, **explicit “no salary claim until…”** rule with **milestone IDs**. **Forbidden** to cite salary replacement in [`executive summary`](east-tennessee-two-site-farm-business-plan-executive-summary.md) until **M3/M5** rows filled. | Page edit |
| 2 | **“Low labor”** vs **grazing surge** | First **calving/hay/escape** week **invalidates** a pretty weekly grid | **Critical** | [`Labor model and weekly rhythm`](east-tennessee-two-site-farm-business-plan-labor-and-family-model.md): add **surge week template** with **hour totals** and **what gets dropped** (off-farm, sleep, tech). [`Family labor and coverage matrix`](family-labor-model-and-coverage-matrix-two-site-smart-farm.md): **non-optional** surge rows. | Page edit |
| 3 | **Family labor ≠ FTE** | **Headcount** masks **effective capacity** | **High** | [`Labor model`](east-tennessee-two-site-farm-business-plan-labor-and-family-model.md): table **effective FTE** = f(jobs, school, health); link to **V11** time log in [`validation backlog`](east-tennessee-two-site-farm-business-plan-validation-backlog.md). | Page edit + **real-world validation** (V11) |
| 4 | **Telemetry** without **triage tax** | **False positives** and **dashboard checks** **eat** hours—**net** labor **can rise** | **High** | [`Instrumentation priority matrix`](instrumentation-priority-matrix-two-site-smart-farm.md): add columns **est. triage h/yr**, **subscription $/yr**, **kill threshold**. [`Smart technology and telemetry strategy`](east-tennessee-two-site-farm-business-plan-smart-tech-strategy.md): **hard cap** on alert hours/week and **annual subscription OPEX**. | Page edit |
| 5 | **Homelab-as-prod** fragility | **Rot** when **family** is **busy** **off-farm**; **silent** **security** **debt** | **High** | [`Smart technology strategy`](east-tennessee-two-site-farm-business-plan-smart-tech-strategy.md): subsection **SPOF + burnout**—**minimum** patch/backup cadence **or** **paid** support line item. New optional artifact: **`wiki/analyses/homelab-ops-checklist-two-site-farm.md`** (quarterly checklist). [`Implementation backlog`](implementation-backlog-strategic-audit.md): pointer if file created. | Page edit + **new artifact** (optional) |
| 6 | **Water** CAPEX **under-modeled** | **Wrong** water **kills** **inventory** and **welfare**; **blows** budget | **Critical** | [`Capital plan`](east-tennessee-two-site-farm-business-plan-capital-and-financing.md): **water line-item** **ranges** placeholder + **rule**: no **herd scale** until **V2/V4** green. [`capital phasing table`](capital-phasing-table-years-0-10-two-site-smart-farm.md): separate **water** rows. Ingest **well report** to `raw/` when obtained → **source-note**. | Page edit + **source-ingest** (when docs exist) + **real-world validation** |
| 7 | **Fence** as **one-time** CAPEX | **OPEX** and **labor** **forever**; **underfunded** fence **=** **escape** **risk** | **High** | [`Capital plan`](east-tennessee-two-site-farm-business-plan-capital-and-financing.md): add **annual fence/OPEX row** (maint, vegetation, shorts). [`Risk register`](east-tennessee-two-site-farm-business-plan-risk-register.md): tie **R5** to **$** **maint** **budget**. | Page edit |
| 8 | **Working capital** invisible | **Cash** **peaks** **before** **P&L** **looks** **bad** | **Critical** | [`Capital plan`](east-tennessee-two-site-farm-business-plan-capital-and-financing.md): **WC policy** subsection—**minimum** **months** **operating** **cash**, **line** **of** **credit** **rules**. [`capital phasing table`](capital-phasing-table-years-0-10-two-site-smart-farm.md): **WC** rows. [`revenue model`](east-tennessee-two-site-farm-business-plan-revenue-and-phased-income.md): **inventory** **timing** note (cattle **as** **inventory**). | Page edit |
| 9 | **Equipment trap** (hay, loader, truck) | **Finance** **easy**; **hours**/year **may** **not** **clear** | **High** | [`Enterprise options`](east-tennessee-two-site-farm-business-plan-enterprise-options-analysis.md): already flags—add **cross-link** to **do not finance** register (§3). [`validation before major spend`](validation-backlog-before-major-spend-two-site-smart-farm.md): **gate** **equipment** **to** **hire** **quote** **+** **hours** **proof**. | Page edit + **decision control** |
| 10 | **Processing / haul** under-owned | **Shrink**, **slot** **loss**, **distance** **eat** **margin** | **High** | [`validation backlog`](east-tennessee-two-site-farm-business-plan-validation-backlog.md): **elevate V6** to **G1** **blocker** for **owned** **herd** **scale**. New row in [`revenue model`](east-tennessee-two-site-farm-business-plan-revenue-and-phased-income.md): **all-in** **cost** **per** **head** **sold** placeholder. | Page edit + **real-world validation** |
| 11 | **Regulatory** thin | **Zoning**, **transport**, **health** **can** **stop** **cold** | **High** | [`Risk register`](east-tennessee-two-site-farm-business-plan-risk-register.md) + [`business risk register`](business-risk-register-two-site-smart-farm.md): add **R14** county/neighbor **nuisance**; **owner** column **required**. [`validation backlog`](east-tennessee-two-site-farm-business-plan-validation-backlog.md): **V8** must **pass** before **structure** **CAPEX**. TN **source-notes** already in repo—**link** from risk rows when **citing**. | Page edit + **source-ingest** (optional new TN ordinance capture) |
| 12 | **Insurance** as checkbox | **One** **uncovered** **loss** **wipes** **years** | **High** | [`Risk register`](east-tennessee-two-site-farm-business-plan-risk-register.md): **binder review** **date** field. [`validation backlog`](east-tennessee-two-site-farm-business-plan-validation-backlog.md): **V9** **pass** **required** before **Phase** **2** **financed** **equipment**. | Page edit + **real-world validation** |
| 13 | **Scale before margin** | **Violates** **G2**; **emotional** **scaling** | **Critical** | [`validation backlog`](east-tennessee-two-site-farm-business-plan-validation-backlog.md) + [`before major spend`](validation-backlog-before-major-spend-two-site-smart-farm.md): add **explicit** **“scale** **freeze”** **if** **trailing** **margin** **negative**. [`10-year roadmap`](east-tennessee-two-site-farm-business-plan-10-year-roadmap.md): **one** **paragraph** **kill** **switch**. | Page edit |
| 14 | **Two-site** theft / slow response | **Remote** **120** **=** **target** **+** **delay** | **Medium** | [`two-site ops`](two-site-operations-model-5ac-homebase-120ac-production.md): **physical** **security** **minimums** (locks, **neighbor** **check**, **no** **camera-only** **delusion**). [`manual fallback`](manual-fallback-degraded-modes-critical-operations.md): **road** **blocked** / **theft** **row**. Already **R12–R13** in plan risk page—**verify** **mitigation** **owners** filled. | Page edit |
| 15 | **5 ac brain overload** | **NOC** **+** **books** **+** **shop** **+** **family** **=** **failure** **mode** **is** **attention** **not** **uptime** | **High** | [`two-site ops`](two-site-operations-model-5ac-homebase-120ac-production.md): **scope** **limit** **for** **homelab** **(max** **services**, **or** **outsource)**. [`Smart technology strategy`](east-tennessee-two-site-farm-business-plan-smart-tech-strategy.md): **“boring** **stack** **wins”** **rule**. | Page edit |

**Deferred risk** (track but do not pretend closed): **commodity** **price** **war**, **family** **conflict**, **lender** **covenant** **breach**—keep in [`risk register`](east-tennessee-two-site-farm-business-plan-risk-register.md) **review** **cadence**, **no** **wiki** **text** **alone** **fixes** **them**.

---

## 2. Revised priority order (execution hardening — second pass, 2026)

**Principle**: **Kill narrative optimism before capital optimism**—**labor truth** and **liquidity** before **scale**; **manual** competence before **remote** **control**; **one** financed bet at a time. **Supersedes** ad-hoc ordering if conflict: see [`Hostile internal review` §7](east-tennessee-two-site-farm-business-plan-hostile-internal-review.md#7-second-pass-execution-illusions-stricter-than-2).

**Ready-for-execution gate** (behavioral): [`Execution dossier hub — Ready for execution`](execution-dossier-hub-phase-0-1-east-tennessee.md#ready-for-execution-the-plan-is-operational).

| Rank | Harden first | Do not advance until |
|------|--------------|----------------------|
| 1 | **Stop rules + hour log** posted and used ([`Vision`](east-tennessee-two-site-farm-business-plan-vision-and-constraints.md), **V11**) | **Scale** or **debt** **talk** **without** **labor** **truth** |
| 2 | **Legal / access / zoning** (`V8`, deed) | **G1** **evidence** **on** **paper** |
| 3 | **Water** truth (`V2`, conservative **V4**) | **Fence/water** **CAPEX** **or** **herd** |
| 4 | **Market + processing** (`V5`, `V6`) + **WC** policy ([`Capital plan`](east-tennessee-two-site-farm-business-plan-capital-and-financing.md)) | **Owned** **livestock** **scale** |
| 5 | **Surge** measured; **coverage** **matrix** **non-fantasy** | **Second** **enterprise** **or** **“we’ll** **grind”** **weeks** |
| 6 | **Books** + **numeric** **stop** **rules** **reconciled** **to** **behavior** | **New** **term** **debt** |
| 7 | **Telemetry** pilot: **trip** + **triage** **hours** ([`ROI`](instrumentation-roi-model-two-site-smart-farm.md)) | **Fleet** **/** **cameras** **/** **actuation** |
| 8 | **Margin** **years** **or** **honest** **subsidy** **line** | **Salary** **claim** (**G3**) |
| 9 | **Insurance** **binder** **review** (**V9**) **not** **quote-only** | **Financed** **equipment** **(Phase** **2** **gear** **)** |

**Demoted vs older drafts**: **dashboards** and **strategy** **essays** **after** **labor** **surge** **truth**—**correct** **for** **execution** **risk**.

---

## 3. “Do not finance yet” register (decision control)

**Rule**: If the row is **checked** **without** **Prove first** **evidence** **in** **`validation`** **or** **family** **files**, **the** **answer** **is** **no**.

| Item | Prove first (minimum) | Evidence hook |
|------|------------------------|---------------|
| Perimeter fence **at designed scale** | Carrying capacity + water plan + legal access | **G1**, V1–V4 |
| Well / water **development** **(major)** | Flow, sustainability, rights | V2, well report → **source-note** |
| Herd **expansion** (breeding or stockers) | WC line + market exit + processing slot | V5, V6, WC subsection (when added) |
| Hay **equipment** **line** | Custom hire quote + hours/year in cab | Hire vs own comparison artifact |
| Loader / tractor **upgrade** | 3-year hire vs own math | Same |
| Large **telemetry** **rollout** | Pilot ROI + triage SOP + OPEX cap | Instrumentation matrix columns |
| Cold chain / **direct** **marketing** **assets** | Repeated small sales, positive unit margin | Revenue milestones |
| **Any** term debt with **personal guarantee** | Written worst-case exit + household stress test | Family doc **outside** wiki OK; **wiki** records **gate** **passed** **Y/N** |

---

## 4. “Must validate in the real world first” checklist

**Operational bar**: Also satisfy [`Ready for execution`](execution-dossier-hub-phase-0-1-east-tennessee.md#ready-for-execution-the-plan-is-operational) **before** treating the plan as **operational** (not just documented).

**Phase 0–1 execution gates (EG)**: Domain **pass/fail** tables (**pilot** vs **production**) — [`Execution gates — Phase 0–1 (East Tennessee two-site)`](execution-gates-phase-0-1-east-tennessee-two-site.md). Use **EG** rows when translating P0/P1 checkboxes into **who must pass what** before spend.

**P0** — **no** **Phase** **2** **production** **bet** **without** **these** **as** **pass** **or** **written** **waive** **with** **date**:

- [ ] **Deed/lease** matches **intended** **use** **of** **120** **ac**
- [ ] **Physical** **access** **year-round** (road **maint** **plan** **or** **honest** **“no”**)
- [ ] **Water** **quantity** **+** **rights** **documented**
- [ ] **Conservative** **carrying** **capacity** **band**
- [ ] **Zoning** / **ag** **structure** **path** **for** **planned** **builds**

**P1** — **before** **owned** **herd** **or** **meaningful** **CAPEX**:

- [ ] **Auction** **or** **direct** **price** **reality** (sale bills / trial)
- [ ] **Processing** **or** **haul** **all-in** **cost** **per** **head**
- [ ] **Family** **hour** **log** **8+** **weeks** **including** **one** **stress** **window**
- [ ] **Insurance** **binder** **review** **(farm** **+** **umbrella** **)**

**P2** — **before** **telemetry** **scale** **or** **salary** **narrative**:

- [ ] **Before/after** **trip** **count** **+** **triage** **hours** **from** **pilot**
- [ ] **Two** **years** **operating** **margin** **truth** **(or** **honest** **subsidy** **accounting** **)**

---

## 5. Change plan — business-plan pages requiring revision

| Page | Required change (acceptance criteria) |
|------|---------------------------------------|
| [`revenue model and milestones`](east-tennessee-two-site-farm-business-plan-revenue-and-phased-income.md) | **`HH_NEED`** placeholder; **WC** / inventory timing; **all-in** **per** **head**; **ban** **salary** **language** **until** **milestones** |
| [`revenue milestone model`](revenue-milestone-model-supplemental-to-salary-replacement.md) | **Bridge** **years**; **M2** **failure** **behavior** |
| [`labor model`](east-tennessee-two-site-farm-business-plan-labor-and-family-model.md) | **Surge** **hours** **table**; **effective** **FTE** |
| [`family labor and coverage matrix`](family-labor-model-and-coverage-matrix-two-site-smart-farm.md) | **T1** **from** **trial**; **hired/neighbor** **row** **if** **gap** |
| [`capital plan`](east-tennessee-two-site-farm-business-plan-capital-and-financing.md) | **WC** **policy**; **fence** **OPEX**; **water** **cost** **band** |
| [`capital phasing 0–10`](capital-phasing-table-years-0-10-two-site-smart-farm.md) | **WC** **rows**; **gate** **ID** **per** **financed** **line** |
| [`instrumentation priority matrix`](instrumentation-priority-matrix-two-site-smart-farm.md) | **Triage** **h/yr**; **sub** **cap** |
| [`smart technology strategy`](east-tennessee-two-site-farm-business-plan-smart-tech-strategy.md) | **SPOF/burnout**; **boring** **stack** **rule**; **alert** **hour** **cap** |
| [`two-site ops 5/120`](two-site-operations-model-5ac-homebase-120ac-production.md) | **Homelab** **scope** **limit**; **physical** **security** **minimums** |
| [`business risk register`](business-risk-register-two-site-smart-farm.md) | **Neighbor**, **WC** **crunch**, **processing** **failure** |
| [`plan risk register`](east-tennessee-two-site-farm-business-plan-risk-register.md) | **Mirror** **+** **owners**; **binder** **date** |
| [`validation before major spend`](validation-backlog-before-major-spend-two-site-smart-farm.md) | **$** **thresholds**; **two** **comps** **for** **market**; **equipment**→hire **gate** |
| [`validation backlog`](east-tennessee-two-site-farm-business-plan-validation-backlog.md) | **V6** **elevation**; **scale** **freeze** **rule** |
| [`manual fallback`](manual-fallback-degraded-modes-critical-operations.md) | **Theft/road** **blocked** |
| [`10-year roadmap`](east-tennessee-two-site-farm-business-plan-10-year-roadmap.md) | **Kill** **switch** **paragraph** |
| [`executive summary`](east-tennessee-two-site-farm-business-plan-executive-summary.md) | **No** **salary** **claim** **until** **milestones** **—** **link** **this** **page** |

---

## 6. Decision controls (how to use this backlog)

| Control | Mechanism |
|---------|-----------|
| **PR** **that** **touches** **revenue** **or** **capital** | Must **reference** **row** **in** §1 **or** **§5** **or** **explain** **“N/A”** |
| **New** **debt** | **Check** §3 **register**; **log** **gate** **ID** **in** [`wiki/log.md`](../log.md) **policy** **or** **refactor** **entry** |
| **Telemetry** **purchase** **\> $** **\_** | **Instrumentation** **matrix** **row** **complete** **including** **triage** **budget** |

---

## Links

- [`Hostile internal review`](east-tennessee-two-site-farm-business-plan-hostile-internal-review.md)
- [`Planning framework`](east-tennessee-two-site-farm-business-plan-framework.md)
- [`Executive summary`](east-tennessee-two-site-farm-business-plan-executive-summary.md)
