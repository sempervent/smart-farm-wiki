---
title: Execution gates — Phase 0–1 (East Tennessee two-site)
page_type: analysis
page_subtype: operational_guide
status: active
created: 2026-04-28
updated: 2026-04-29
review_status: unreviewed
operational_maturity: pilot_ready
confidence: medium
tags:
  - business-plan
  - execution
  - gates
  - east-tennessee
  - two-site
  - phase-0-1
---

# Execution gates — Phase 0–1 (East Tennessee two-site)

## Purpose

Turn the **narrowed** Phase 0–1 plan into an **execution-gate system**: what may **start**, what stays **pilot-only**, and what **must not proceed** to **production** posture (irreversible CAPEX, herd scale, privileged remote control, financed infrastructure).

**Relationship to existing IDs**

- **G1–G3** and **V1–V12** remain on [`Validation backlog and decision gates`](east-tennessee-two-site-farm-business-plan-validation-backlog.md). This page adds **EG-** prefixed gates that **decompose** Phase 0–1 readiness by **domain** so a team can see **why** G1 is or is not honest.
- **Fin-G\*** family thresholds live on [`Execution gates — financial thresholds`](execution-gates-financial-thresholds.md)—this page **does not** invent dollar **values** or percentage **constants**; it requires **documented** family/chosen thresholds where those pages use placeholders.

**Pilots vs production (definitions)**

| Stance | Meaning |
|--------|---------|
| **Pilot allowed** | Bounded time/$/scope; **kill criteria** written **before** start; **observe-first** where actuation exists; **no** implied scale. |
| **Production allowed** | Sustained operating posture: **repeatable** visits, **named** coverage, **finance-grade** evidence where money moves, **no** open **fail** rows for the decision class. |

**Evidence routing**: [`Local evidence package — East Tennessee two-site`](../topics/local-evidence-package-east-tennessee-two-site.md), [`Field verification program — Phase 0–1 (Claxton and Demory)`](field-verification-program-phase-0-1-claxton-demory.md), [`Claxton and Demory — missing data register`](claxton-and-demory-missing-data-register.md).

---

## 1. Local evidence readiness

| ID | Gate | Why it matters | Pass criteria | Fail criteria | Unlocks | Blocked if fail |
|----|------|----------------|---------------|---------------|---------|-----------------|
| **EG-LEV-1** | **Register hygiene** | Without an honest gap list, desk maps become fake certainty | **Pilot:** Every **Phase 0–1** row in [`missing data register`](claxton-and-demory-missing-data-register.md) has **status** (open / measured / deferred-with-next-step) + **owner**. **Production:** No **G1-class** item (legal use, access, water, stocking driver) remains **“assumed”** without **dated** field plan or **written waive** | Any G1-class row **blank** or **orphan** (no owner, no next step) | Desktop research, county pulls, **scheduled** field visits | **Production** fence/water/herd decisions that depend on a hidden gap |
| **EG-LEV-2** | **Field verification cadence** | Phase 0–1 is **narrowed** toward **measured** truth | **Pilot:** [`Field verification program`](field-verification-program-phase-0-1-claxton-demory.md) **kickoff** recorded (T0-relative) with **which sections** run first. **Production:** **Dated** logs exist for **both** sites for the **minimum** sections named in dossier “Ready for execution” §C | Program **not started** after calendar slip **without** explicit reschedule | Promotion of measurements into [`local evidence package`](../topics/local-evidence-package-east-tennessee-two-site.md) tables | Treating **county/WSS** summaries as **parcel-complete** for CAPEX |

**Pilot vs production**: **Pilot** allows **scheduled** work and **partial** logs; **production** requires **dated** evidence or **explicit waive** for the specific claim.

---

## 2. Site / infrastructure readiness

| ID | Gate | Why it matters | Pass criteria | Fail criteria | Unlocks | Blocked if fail |
|----|------|----------------|---------------|---------------|---------|-----------------|
| **EG-SITE-1** | **Legal use + access** | Bad title/use/access **voids** economics | **Pilot:** **V8** started (zoning/ag-structure path **documented** as letter, ticket, or defensible memo). **V2** started (water rights **question list** to attorney or agency). **Production:** **No** open **legal** contradiction on **intended** Phase 2 enterprise on **~120 ac** operating area; **year-round** access **plan** exists (maintain, agreement, or honest **seasonal limit**) | **Silent** assumption that “ag use” equals **your** intended ops | **Pilot** equipment leases, **small** fence patches, **market** probes | **G1** and **EG-LEV** production bars; **financed** perimeter/water |
| **EG-SITE-2** | **Field-safe infrastructure** | Injury, stuck trucks, and **false** capacity drive margin lies | **Pilot:** **V3** walk started (photo + map pins). **Production:** **V3** album + map tied to **rotation/handling** plan; **worst-case** access route logged **once** in bad weather **or** **documented** inability | **No** photos / **no** map authority label | **Pilot** soil/water sampling visits | **Owned herd scale**; **heavy** earthwork without **lane/drainage** peer review |

**Pilot vs production**: **Pilot** allows **recon** and **small** fixes; **production** requires **closed** legal/access story **and** **field** infrastructure truth for the **bet size**.

---

## 3. Off-grid power readiness (`SITE_FARM` default)

| ID | Gate | Why it matters | Pass criteria | Fail criteria | Unlocks | Blocked if fail |
|----|------|----------------|---------------|---------------|---------|-----------------|
| **EG-PWR-1** | **Power domain truth** | Telemetry and gateways **compete** with welfare loads on battery | **Pilot:** [`Off-grid operational decision rules`](off-grid-operational-decision-rules-power-and-networking-demory-farm.md) read; **DR-1** class question (“metered or **bracketed** network + always-on electronics load vs autonomy”) has **named owner** + **due**. **Production:** **Bracket or measure** exists **or** **explicit deferral** caps **new** always-on RF/WAN loads | **New** always-on IP radios / **second** farm WAN while DR-1-class question **open** | **Pilot** single-gateway + **one** RF class pilot | **Production** multi-node RF mesh, **second** Starlink/CPE farm install, **HaLow** scale |
| **EG-PWR-2** | **Degraded posture** | Off-grid **is** time in **brownout** behavior | **Pilot:** [`Off-grid degraded modes`](off-grid-degraded-modes-power-and-connectivity-demory-farm.md) **skimmed**; **manual** welfare check path stated in one paragraph. **Production:** **Ops** agrees **which** pumps/gates are **manual-first** when SoC low / WAN down | **Remote dashboard** treated as welfare proof | **Pilot** observe-only sensors on **Pcrit** loads | **Remote actuation** on water/gate class; **production** “NOC from phone” story |

**Pilot vs production**: **Pilot** = **one** bounded power story + **observe-first**; **production** = **measured or bracketed** headroom for **chosen** always-on stack.

---

## 4. Connectivity and trust-bar readiness

| ID | Gate | Why it matters | Pass criteria | Fail criteria | Unlocks | Blocked if fail |
|----|------|----------------|---------------|---------------|---------|-----------------|
| **EG-NET-1** | **WAN role explicit** | Starlink/LTE must not hide **primary** dependency | **Pilot:** [`Connectivity strategy — Claxton & Demory`](connectivity-strategy-for-claxton-and-demory.md) **read**; per-site **WAN** role captured in **one** sentence each (**primary / backup / deferred**). **Production:** **Local-first** paths exist for **P1** telemetry class when WAN absent ([`Local-first / WAN-optional — Demory`](local-first-wan-optional-operating-model-demory-farm.md)) | Farm **requires** constant WAN for **basic** stock/water safety checks | **Pilot** LTE/Starlink **trial** installs per capital sequencing | **Production** “cloud is SoR” for **welfare** decisions |
| **EG-NET-2** | **Trust bar for remote privilege** | VPN **≠** safety | **Pilot:** [`Observability, secrets, and trust bar`](observability-secrets-and-trust-bar-homelab-farm-edge.md) **minimum trust bar** checklist exists in family runbook (copy OK). **Production:** **All** trust-bar items **true** for the **specific** remote actions contemplated (patch, break-glass, actuator API) | **Privileged** remote path enabled **before** bar items true | **Read-only** dashboards; **pilot** push metrics | **Production** remote **actuation**; **break-glass** admin **from internet** |

**Pilot vs production**: **Pilot** allows **read-only** remote visibility **if** manual welfare path holds; **production** remote **control** requires **EG-NET-2** production pass **plus** [`Automation stop rules`](automation-stop-rules-two-site-smart-farm.md).

---

## 5. Sensor readiness

| ID | Gate | Why it matters | Pass criteria | Fail criteria | Unlocks | Blocked if fail |
|----|------|----------------|---------------|---------------|---------|-----------------|
| **EG-SNS-1** | **Manual baseline (G8 family)** | Automation without baseline is **theater** | **Pilot:** **G8** path chosen (which asset); **paper or spreadsheet** baseline started. **Production:** **G8**-equivalent **complete** per [`validation — before major spend`](validation-backlog-before-major-spend-two-site-smart-farm.md) **G8** row (**log without remote control** language) | Baseline **skipped** “because sensors shipping” | **Pilot** **one** sensor class install | **Second** sensor class; **alerts-as-SoR**; **production** actuation |
| **EG-SNS-2** | **Single pilot scope** | Sprawl **burns** labor on triage | **Pilot:** **Exactly one** pilot cluster documented (device class + uplink + owner + **kill** threshold triage h/wk). **Production:** Pilot **reviewed** against [`Instrumentation ROI`](instrumentation-roi-model-two-site-smart-farm.md) **or** **killed** with reason | **Parallel** pilots **without** written exception | **Pilot** expansion **within** cluster | **Fleet** rollout; **production** “instrument everything” |

**Pilot vs production**: Aligns with [`Farm sensor architecture — Demory`](farm-sensor-architecture-demory-farm-site.md) and [`Sensor checklist matrix — Demory`](sensor-checklist-matrix-for-demory-farm.md)—**one** green path first.

---

## 6. Platform / backup / observability readiness

| ID | Gate | Why it matters | Pass criteria | Fail criteria | Unlocks | Blocked if fail |
|----|------|----------------|---------------|---------------|---------|-----------------|
| **EG-PLT-0** | **Stack scope declared** | Gates **do not apply** to stacks you are **not** running | **Declared:** **No** homelab/k3s in Phase 0–1 **or** **Pi/k3s pilot** scope doc (nodes, services, **non-goals**) | **Implicit** “we’ll fix in prod” k3s | If **no** stack: backup/observability rows **N/A** (other evidence still applies). If **pilot** stack: **EG-PLT-1** applies | Confusion about which **EG-PLT** rows apply |
| **EG-PLT-1** | **Backup + restore + observe** (when stack exists) | k3s without restore is **single incident** from total loss | **Pilot:** **One** restore drill **or** **documented** failure to schedule with **date**. **Production:** **RPO/RTO** stated in **family** terms (hours/days—not dollar amounts); [`Kubernetes platform backup/DR — Pi k3s Longhorn`](kubernetes-platform-backup-dr-pi-k3s-longhorn.md) **P0/P1** checklist **green** for **in-scope** nodes | **No** restore test **and** **no** dated plan | **Pilot** extra workloads on cluster | **Production** Longhorn/HA expansion; **treating** cluster as **SoR** without restore proof |

**Pilot vs production**: [`Platform doctrine package`](../topics/platform-doctrine-package-homelab-farm-edge.md); **production** implies **repeatable** drills and **named** on-call for **patch/secret** hygiene.

---

## 7. Labor readiness

| ID | Gate | Why it matters | Pass criteria | Fail criteria | Unlocks | Blocked if fail |
|----|------|----------------|---------------|---------------|---------|-----------------|
| **EG-LAB-1** | **Hour budget evidence** | Plans collapse in **surge** | **Pilot:** **V11** started (any **multi-week** slice). **Production:** **V11** **8+** weeks including **one** stress/surge window per dossier **Ready** §B | **Weekly grid** treated as fact **before** log | **Pilot** extra **recon** trips | **Production** surge enterprises; **G1** production claim |
| **EG-LAB-2** | **Overload coverage** | Two-site **tax** becomes emergency-only | **Pilot:** [`Coverage matrix`](family-labor-model-and-coverage-matrix-two-site-smart-farm.md) **shows** holes **named**. **Production:** **Each** critical hole has **neighbor / hire / defer** row **non-empty** **or** enterprise scope **cut** | **“We’ll figure it out”** for calving/hay/escape class | **Pilot** market/auction attendance | **Production** commitments needing **daily** presence at **120** |

**Pilot vs production**: **Pilot** accepts **documented** holes; **production** requires **closed** coverage **or** **reduced** scope.

---

## 8. Financial readiness

| ID | Gate | Why it matters | Pass criteria | Fail criteria | Unlocks | Blocked if fail |
|----|------|----------------|---------------|---------------|---------|-----------------|
| **EG-FIN-1** | **Insurance reality** | One loss **wipes** years | **Pilot:** **V9** quotes collected. **Production:** **Binder reviewed** with agent; exclusions/limits **understood** (notes OK) | **Quote-only** treated as covered | **Pilot** small sales / lease probes | **Production** visitor-facing ops; **financed** equipment **where** lender requires proof |
| **EG-FIN-2** | **Numeric policy exists** | Stop rules **without numbers** are **decorative** | **Pilot:** [`Vision`](east-tennessee-two-site-farm-business-plan-vision-and-constraints.md) stop-rule **template** copied locally. **Production:** Placeholders **N** (key-person weeks), **D%** (debt vs gross revenue), and **operating reserve months** (per [`Capital plan`](east-tennessee-two-site-farm-business-plan-capital-and-financing.md) / [`Execution gates — financial thresholds`](execution-gates-financial-thresholds.md)) are **filled in the family ledger**—**wiki** holds **structure**, not invented constants | **Blank** thresholds during **Phase 2** CAPEX ask | **Pilot** bookkeeping pattern | **Production** term debt; **salary** narrative |

**Pilot vs production**: **No** invented **financial** constants in-repo—**EG-FIN-2** production pass is **“filled elsewhere, linked or cited privately”**, not numbers invented in markdown.

---

## Composite: what each stance allows

| Decision class | Minimum gate posture |
|----------------|----------------------|
| **Begin** desk / county / calls / templates | **No** EG production requirement; follow [`Decision memo`](execution-dossier-decision-memo-phase-0-1-east-tennessee.md) **Approved now** |
| **Pilot** spend / installs / small CAPEX | Relevant **EG** **pilot** passes for that domain **+** decision memo **pilot** rules |
| **Production** spend (G1-class: fence MVP, water development, herd scale, financed infra, remote actuation) | **G1** on validation backlog **and** **production** bars for **EG-LEV-1**, **EG-SITE-1**, **EG-LAB-1**, **EG-FIN-1**; **plus** domain **production** bars for power/connectivity/sensors/platform **if** that domain is in scope |

---

## Mapping — EG gates to V / G references

| EG gate | Primary V / G / doc hooks |
|---------|---------------------------|
| EG-LEV-1 / EG-LEV-2 | Register + field program; supports **G1** honesty |
| EG-SITE-1 | **V2**, **V8**; **G1** legal/access |
| EG-SITE-2 | **V3**; **G1b**-class physical access |
| EG-PWR-1 / EG-PWR-2 | **DR-\*** / degraded docs; blocks **production** RF/WAN sprawl |
| EG-NET-1 / EG-NET-2 | Connectivity strategy + trust bar; pairs **R16** mitigations |
| EG-SNS-1 / EG-SNS-2 | **G8**, instrumentation matrix, stop rules |
| EG-PLT-0 / EG-PLT-1 | Platform decision memo + backup/DR page |
| EG-LAB-1 / EG-LAB-2 | **V11**, coverage matrix |
| EG-FIN-1 / EG-FIN-2 | **V9**, vision/capital **numeric** policy |

---

## Related

- [`First 90 days — operator packet (East Tennessee two-site)`](first-90-days-operator-packet-east-tennessee-two-site.md) — **Weeks 1–12** pilot runbook aligned to EG **pilot** bars
- [`Phase 0–1 operator burden review — East Tennessee two-site (hostile)`](phase-0-1-operator-burden-review-east-tennessee-two-site.md) — **skeptical** stack view of recurring/surge/invisible load vs EG gates
- [`Execution dossier — Phase 0–1 (hub)`](execution-dossier-hub-phase-0-1-east-tennessee.md)
- [`Validation backlog and decision gates`](east-tennessee-two-site-farm-business-plan-validation-backlog.md)
- [`Business plan integration revision audit (2026-04)`](east-tennessee-two-site-farm-business-plan-integration-revision-audit-2026-04.md)
- [`East Tennessee two-site farm business plan (package)`](../business-plan/east-tennessee-two-site-farm-business-plan.md)
