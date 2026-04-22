---
title: Field verification program — Phase 0–1 (Claxton and Demory)
page_type: analysis
page_subtype: operational_guide
status: active
operational_maturity: draft
created: 2026-04-26
updated: 2026-04-30
review_status: unreviewed
confidence: high
tags:
  - two-site
  - field-work
  - validation
  - claxton
  - demory
---

# Field verification program — Phase 0–1 (Claxton and Demory)

**Purpose**: Tie **Phase 0–1 execution** to **repeatable site work** at **`SITE_HOME`** (**Claxton**, Anderson) and **`SITE_FARM`** (**Demory**, Campbell)—**methods and evidence contracts only**. **Do not** pre-fill results; each visit **updates** baselines, worksheets, and [`missing data register`](claxton-and-demory-missing-data-register.md) rows via [`parcel evidence intake workflow`](parcel-evidence-intake-and-validation-workflow-east-tennessee-two-site.md).

**Legend — Site**: **C** = Claxton / `SITE_HOME` · **D** = Demory / `SITE_FARM` · **Both** = both.  
**Legend — Desktop vs field**: **Desktop** = GIS, portals, calls, quotes without standing on dirt · **Field** = boots on ground · **Both** = desk prep + mandatory field confirmation.

**Templates**: [`Field observation template package — two-site`](../topics/field-observation-template-package-east-tennessee-two-site.md).  
**Gates / tasks**: **V1–V12**, **G1–G3** on [`Validation backlog and decision gates`](east-tennessee-two-site-farm-business-plan-validation-backlog.md); **G1–G8** “major spend” alignment on [`Validation — before major spend`](validation-backlog-before-major-spend-two-site-smart-farm.md).  
**Sensor / RF doctrine**: [`Farm sensor architecture — Demory farm site`](farm-sensor-architecture-demory-farm-site.md) · [`Sensor checklist matrix — Demory farm`](sensor-checklist-matrix-for-demory-farm.md).

**90-day bundling**: [`First 90 days — operator packet (East Tennessee two-site)`](first-90-days-operator-packet-east-tennessee-two-site.md) maps **weeks 1–12** to this program’s sections for **pilot** execution.

---

## 1. Site walks and boundaries

| Verification item | Site | Why it matters | Method | Evidence to record | Gates / decisions affected | Desktop vs field |
|-------------------|------|----------------|--------|-------------------|---------------------------|------------------|
| **Orienting walk** (buildings, fields, hazards, stock routes) | Both | Every other row assumes you know **where** things are | Walk with printed map / tablet; use visit header template | Dated log, photo roll IDs, **fact class** per fact | All **V** tasks; **R14** context | Field |
| **Fence + boundary walk** (segments, gates, corners) | **D** primary; **C** if livestock boundary | **V3**; legal/settlement risk if fence ≠ line | Template §B; flag **Unknown** corners | Segment table → [`Infrastructure baseline`](infrastructure-inventory-baseline-two-sites-east-tennessee.md) | **V3**; **G1** fence CAPEX; deed/title (**V8** surface) | Field |
| **Stake / corner ambiguity list** | Both | Blocks confident fence/water CAD | GPS optional; **do not** claim survey accuracy | List of IDs needing **surveyor** | **G1**; missing register §1 | Field |
| **Handling / load-out / corral as-built** | **D** | **V6** timing; welfare | Sketch + photos + dimensions where safe | Row in site inventory | **V6**; Phase 2 ops | Field |

---

## 2. Access and road checks

| Verification item | Site | Why it matters | Method | Evidence to record | Gates / decisions affected | Desktop vs field |
|-------------------|------|----------------|--------|-------------------|---------------------------|------------------|
| **Primary ingress route** (pavement → driveway → lane) | Both | **Trip batching** + emergency response | Template §C; wet/dry passes | Segment photos, **mud/ice** notes | [`Trip policy`](trip-batching-and-site-visit-policy-two-site-smart-farm.md); **R14** | Field |
| **Haul / equipment path** (turn radii, soft spots) | **D** | Hay, stock trailer, drill timing | Drive + walk with load surrogate if legal/safe | Pin map + **season** note | **G1** earthwork; **capital plan** | Field |
| **Easement / shared lane facts** | Both | **R13**; who maintains | Desk: title index → Field: match posts/signs | Redacted letter or map in `raw/` + source-note | **V8** (legal); **R13** | Both |
| **911 / official address sanity** | Both | Permits, utilities, **WAN** billing | Desk: county GIS/911; Field: mailbox/sign match | Capture path + photo | Workflow “Official farm address” row | Both |

---

## 3. Drainage and erosion observations

| Verification item | Site | Why it matters | Method | Evidence to record | Gates / decisions affected | Desktop vs field |
|-------------------|------|----------------|--------|-------------------|---------------------------|------------------|
| **Crown / ditch / culvert / rolling dip** inventory | **D**; **C** driveway | **R14**; winter access | Walk in **rain** or soon after; measure only if trained | Labeled photo series + segment IDs | **V2** routing; **R14** | Field |
| **Active rills / gullies / sediment at gates** | **D** | Sediment traps gates; **V3** | Flag + GPS optional | Before/after photos when fixed | **R14**; **G1** civil line | Field |
| **Ponding / seasonally wet panels** | **D** | **V1** wet limitation; fence post rot | Walk with WSS map on tablet | Polygon sketch on worksheet | **V1**; **V4** | Both |
| **Stream / buffer observation** (no work in buffer) | **D** | **TDEC** / liability | Visual only from legal access | Photo + “no disturbance” note | **V2**; **R10** | Field |

---

## 4. Utility and service verification

| Verification item | Site | Why it matters | Method | Evidence to record | Gates / decisions affected | Desktop vs field |
|-------------------|------|----------------|--------|-------------------|---------------------------|------------------|
| **Electric account structure** (meter IDs, rate class) | Both | Loads + **broker** UPS story | Call/portal; **redact** in wiki | Provider + **unknowns** only on [`Utility baseline`](utility-and-service-baseline-two-sites-east-tennessee.md) | **Capital**; smart-tech | Desktop |
| **Will-serve / transformer / single vs three-phase** | Both | Pumps, cold, shop | Utility engineer visit or letter | PDF in `raw/` + source-note | **V2** pump ceiling; **G1** | Both |
| **Domestic vs ag water meters** | Both | Books + drought planning | Field locate meters; photo labels | Table update | **Revenue** / COA alignment | Field |
| **Well / pump / pressure tank walkdown** | **D** (primary) | **V2** | Visual + **safe** sound check; hire for drawdown test | Log + contractor report if done | **V2**, **V4** | Field |
| **Septic / OSSS locate + setback sketch** | **C**; **D** if structures | **V8** buildability | County env. health + field locate lids | Sketch + permit # if issued | **V8**; homestead CAPEX | Both |
| **ISP / LTE / Starlink obstruction sketch** | **C** office; **D** pilot pins | **V10** | Desk: coverage maps → Field: obstruction photos | Pin list + signal meter screenshots | **V10**; **G8** | Both |
| **811 process readiness** (before any dig) | Both | Legal + safety | Read TN811 captures; file ticket when digging | Ticket # in **private** runbook | **All** trenching | Desktop |

---

## 5. Power and load observation

| Verification item | Site | Why it matters | Method | Evidence to record | Gates / decisions affected | Desktop vs field |
|-------------------|------|----------------|--------|-------------------|---------------------------|------------------|
| **Main panel photo + breaker map** (de-identified) | Both | **Loads register** truth | Safe photo; turn off before opening if not qualified | Annotated diagram in `raw/` | [`Loads register`](loads-register-known-estimated-unknown-two-sites-east-tennessee.md) | Field (hire electrician if needed) |
| **Duty-cycled loads spot-check** (well, heat tape, cooler) | Both | Off-grid / **CS-5** story at **D** | Clamp meter window if competent; else log **run hours** | Time-series CSV or notebook | **G8**; Demory power doctrine | Field |
| **Generator / transfer switch test** | Either | Degraded mode | Exercise per manual; log | Test log | **MV-8** drills | Field |
| **Homelab / edge rack measured draw** | **C** | **Pcrit** / **Popt** coupling | PDU or UPS readout | kWh sample | [`Power domains — Demory`](off-grid-power-domains-and-battery-tiers-demory-farm.md) cross-site budget | Field |

---

## 6. Sensor pilot placement

| Verification item | Site | Why it matters | Method | Evidence to record | Gates / decisions affected | Desktop vs field |
|-------------------|------|----------------|--------|-------------------|---------------------------|------------------|
| **Candidate mount points** (height, sun, theft, stock rub) | **D** | One-pilot discipline | Tag photos + pole/tree ID | Matrix row → [`Sensor checklist matrix`](sensor-checklist-matrix-for-demory-farm.md) | **Stop rules** telemetry scope | Field |
| **Gateway / concentrator elevation + backhaul** | **D** | RF vs **WAN** separation | Map LOS to home vs LTE; **no** trench without 811 | Sketch + pin | [`Farm sensor architecture`](farm-sensor-architecture-demory-farm-site.md) | Both |
| **Soil probe / tank level pilot “pencil install”** | **D** | Prove **SoR** path | Single device; document **asset ID** | farmOS/log stub or spreadsheet | [`Telemetry system of record — boundaries and authority`](telemetry-system-of-record-boundaries-and-authority.md) | Field |
| **Spurious RF noise scan** (microwave, motors) | **D** | Avoid false **automation** | Short spectrum notes or “motor on/off” test | Log | [`Automation stop rules — two-site smart farm`](automation-stop-rules-two-site-smart-farm.md) | Field |

---

## 7. Controller and gateway location validation

| Verification item | Site | Why it matters | Method | Evidence to record | Gates / decisions affected | Desktop vs field |
|-------------------|------|----------------|--------|-------------------|---------------------------|------------------|
| **Barn / shed environment** (dust, temp, Ethernet pull) | **D** | k3s / Pi survival | Thermometer + dust visual; cable path | Photo + max/min temp guess | Platform doctrine | Field |
| **Enclosure + grounding + surge path** | **D** | Lightning / **Pcrit** | Visual inspection; **electrician** for bonding | Photo + **defer** note if not qualified | **DR** / safety | Field |
| **Homelab as control plane** reachability | **C** | When **WAN** down | VPN/overlay test from **D** phone hotspot | Latency log | [`Remote access model`](remote-access-operational-security-model-two-site-smart-farm.md) | Both |
| **UPS / battery maintenance access** | **C** | Graceful shutdown | Physical clearance check | Photo | **MV** drills | Field |

---

## 8. Buildability, septic, and permit follow-ups

| Verification item | Site | Why it matters | Method | Evidence to record | Gates / decisions affected | Desktop vs field |
|-------------------|------|----------------|--------|-------------------|---------------------------|------------------|
| **Zoning district + permitted ag structures** letter | Both | **V8** | Planning desk request | PDF in `raw/` + source-note | **V8**; **G1** | Desktop |
| **Setback field verify** (tape from foundation corners) | Both | Maps lie | Measure only where safe/legal | Sketch | **V8** | Field |
| **Flood zone field check** (signs of ponding vs map) | Both | Insurance + build | FEMA layer on tablet + walk | Photo + zone print | **V9**; build siting | Both |
| **Perc / morph if required** | **C** | ADU / shop expansion | County-scheduled test | Report in `raw/` | **Capital** sequencing | Field |

---

## Program cadence (suggested)

| Cadence | Bundle |
|---------|--------|
| **Every Demory trip** | Access (§2) + one infrastructure slice (§1 or §3) + one utility/power spot (§4–5) |
| **Quarterly** | Full fence segment progress (**§1**), drainage after heavy rain (**§3**), insurance/agent delta (**V9**) |
| **Before any dig** | §4 **811** + §8 permits |

---

## Related

- [`Local evidence package — East Tennessee two-site`](../topics/local-evidence-package-east-tennessee-two-site.md)
- [`Execution dossier — Phase 0–1 (hub)`](execution-dossier-hub-phase-0-1-east-tennessee.md)
- [`Pilot and recon checklists — first 24 months`](pilot-and-recon-checklists-first-24-months-two-site-smart-farm.md)
- [`First 90 days — operator packet (East Tennessee two-site)`](first-90-days-operator-packet-east-tennessee-two-site.md)
