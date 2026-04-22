---
title: Smart technology and telemetry strategy — control center on 5 acres
page_type: analysis
status: active
created: 2026-04-17
updated: 2026-04-27
review_status: unreviewed
tags:
  - business-plan
  - automation
  - telemetry
  - two-site
confidence: medium
aliases:
  - East Tennessee two-site farm business plan — smart technology, telemetry, and automation
---

# Smart technology and telemetry strategy — control center on 5 acres

## Purpose

Define how **telemetry and automation** support a **two-site** operation where the **~5-acre homestead** is the long-run **control center** (stable power, daily access, primary **broker**, backups, development) and the **~120-acre farm** holds **production risk** and **field edge**.

**Philosophy**: **Aggressive automation is allowed**—but only as **capital + OPEX + maintenance + triage labor + false-positive drag + cyber exposure** that **passes explicit gates**. Instrumentation **does not** automatically reduce labor; it **may** reduce **trips**, **speed detection**, or **document state**—each claim needs **evidence** ([`Instrumentation ROI model`](instrumentation-roi-model-two-site-smart-farm.md), [`Automation stop rules`](automation-stop-rules-two-site-smart-farm.md)).

**Architecture reference**: [`Field telemetry reference architecture — homestead + 120-acre farm`](field-telemetry-reference-architecture-homestead-120ac.md).  
**Registry / naming**: [`Farm spatial model and asset registry standard`](farm-spatial-model-and-asset-registry-standard.md).  
**Hub**: [`East Tennessee two-site farm business plan — planning framework`](east-tennessee-two-site-farm-business-plan-framework.md).  
**Homelab / edge Kubernetes (when the control-center stack is Pi + k3s)**: [`How to provision k3s, Longhorn, and Rancher on a Raspberry Pi fleet`](how-to-provision-k3s-longhorn-and-rancher-on-a-raspberry-pi-fleet.md) (operational runbook; phases P0/P1 vs later).

**Local evidence (Demory / Campbell)**: **Steep** haul routes and **stock water** risk **favor** **tank/pump/gate** **observability** **before** **broad** sensor sprawl—[`Demory site intelligence`](demory-farm-site-intelligence.md). **Claxton** / **Anderson**: **broker** and **backups** stay **home-base**-biased **after** **power/ISP** verified ([`Claxton site intelligence`](claxton-home-base-site-intelligence.md)).

### Doctrine binding (2026-04 integration)

- **Sensors**: [`Farm sensor architecture — Demory farm site`](farm-sensor-architecture-demory-farm-site.md), [`Field-node classes and communication roles — Demory`](field-node-classes-and-communication-roles-demory-farm.md), [`Sensor checklist matrix — Demory farm`](sensor-checklist-matrix-for-demory-farm.md) — **Phase 0–1** = **one** green path + **observe-first**; defer sprawl per [`Automation stop rules`](automation-stop-rules-two-site-smart-farm.md).
- **Degraded modes**: [`Off-grid degraded modes — power and connectivity`](off-grid-degraded-modes-power-and-connectivity-demory-farm.md) + manual SoT—**WAN down** must not imply **safe remote actuation**.
- **Platform / backup / observability**: [`Platform doctrine package`](../topics/platform-doctrine-package-homelab-farm-edge.md), [`Kubernetes platform backup/DR — Pi k3s Longhorn`](kubernetes-platform-backup-dr-pi-k3s-longhorn.md), [`Observability, secrets, and trust bar — homelab / farm edge`](observability-secrets-and-trust-bar-homelab-farm-edge.md) — **pilot-ready** vs **overbuilt**; privileged **remote** ops only after **trust bar** items are true.
- **Ledger**: [`Business plan integration revision audit (2026-04)`](east-tennessee-two-site-farm-business-plan-integration-revision-audit-2026-04.md).

## Starlink / WAN role (canonical integration)

**Standalone diagrams and sources** live in [`Two-site smart farm — network topology and WAN/edge reference (Mermaid)`](two-site-smart-farm-network-topology-and-wan-edge-reference.md) and [`Electrical, networking, and Starlink — inbox batch`](../source-notes/electrical-networking-starlink-inbox-batch-2026-04-23.md)—this section only **binds** Starlink to **telemetry strategy**.

| Location | Role | Telemetry implication |
|----------|------|-------------------------|
| **`SITE_HOME`** | **Primary or backup LEO WAN** (relative to any future wireline)—**document** which | **Broker**, backups, patch cadence, and **admin VPN** **prefer** stable uplink here; **do not** move “brain” CAPEX ahead of **power + ISP truth** ([`Claxton site intelligence`](claxton-home-base-site-intelligence.md)). |
| **`SITE_FARM`** | **Conditional** when field gateways need **Internet**; **deferred** until **Phase 1** pilot scope is clear | **Observe-first** sensors and **MQTT egress** **depend** on **honest** backhaul planning—**LTE vs Starlink** is an **either/or** design choice, not both by default. |

**Enables**: fewer **blind** nights when **batching** trips; **TLS** to cloud broker; **remote triage** of alerts **if** **safe-default** actuation rules hold.

**Must not silently become**: **permission** to **remote-actuate** gates/pumps without [`Automation stop rules`](automation-stop-rules-two-site-smart-farm.md); **reason** to skip **G8**-style **manual baselines**; **default** that **MQTT** **equals** **system of record**—see [`Telemetry system of record — boundaries and authority`](telemetry-system-of-record-boundaries-and-authority.md).

**What changed because of Starlink analysis**: Spec **PDFs** and **captures** give **hardware-class** language (**Mini** vs **Standard / kit**) for **uplink planning**—strategy pages still **avoid** duplicating that prose; they **assign** Starlink to **WAN layer** above **MQTT/field RF**.

### `SITE_FARM` off-grid-first — business and labor consequences

**Demory / `SITE_FARM`** is modeled **off-grid-first** (solar + battery default; WAN secondary). For telemetry strategy, that implies:

| Consequence | Execution rule |
|-------------|----------------|
| Always-on networking is an energy load | Gateways, 24/7 Wi‑Fi, HaLow APs, and optional Starlink CPE compete with pumps and inverter headroom—budget Pcrit vs Popt per [`Off-grid power strategy — Demory farm site`](off-grid-power-strategy-demory-farm-site.md). Do not expand fleet RF while [`Off-grid operational decision rules`](off-grid-operational-decision-rules-power-and-networking-demory-farm.md) **DR-1** (metered network load vs battery autonomy) is still open. |
| Mesh / LPWAN before WAN convenience | Meshtastic-class links for sparse telemetry first; HaLow only where throughput or IP semantics win per [`Meshtastic vs HaLow vs Wi‑Fi`](../comparisons/meshtastic-wi-fi-halow-conventional-wi-fi-off-grid-farm-operations.md). Pilot scope: one gateway + one RF class ([`Decision rules`](off-grid-operational-decision-rules-power-and-networking-demory-farm.md) **DR-5**). |
| Maintenance burden rises | Add battery/BMS awareness, DC wiring discipline, and enclosure corrosion to **H_PATCH** / **H_FIELD** (maintenance burden § below). Keep broker/patch cadence at **`SITE_HOME`**; avoid duplicating a full “brain” stack at the farm. |
| Remote trust | Starlink/LTE dashboards are optional; welfare checks and safe defaults must hold with WAN down and with field power stressed—same bar as [`Automation stop rules`](automation-stop-rules-two-site-smart-farm.md) **CS-4**, **MV-7**, **MV-8**. |

---

## Decisions supported by this page

| Decision | This page provides |
|----------|-------------------|
| **What** to deploy **before** Phase 2 production | **Allowed / forbidden early** tables |
| **Where** the **broker** and **secrets** live | Homestead vs field split |
| **When** remote control is allowed | **Proof gates** before actuation |
| **OPEX + labor cap** for subscriptions and on-call time | **Maintenance burden** + **stop rules** link |
| **Security minimum** before exposure grows | **Security obligations** |

---

## Why the control center is on the 5-acre parcel

| Reason | Implication |
|--------|-------------|
| **Uptime and access** | Grid power and daily presence beat remote rack in a barn for **patching**, **backups**, **credential** hygiene |
| **Security** | VPN and credentials terminate where **physical** access is **routine** |
| **Amortization** | One **homelab** stack serves the whole operation—**avoid** duplicating “brains” at `SITE_FARM` |
| **Separation of concerns** | **Mess, theft exposure, and weather** concentrate at **120**; **stable compute** stays **home** |

**Constraint**: If the **only** copy of **critical** logic lives at home, **design degraded behavior** at **120** when **backhaul fails** ([`Runbook — broker or backhaul down`](runbook-broker-or-backhaul-down.md)).

---

## Principles (execution-safe)

1. **Telemetry must prove trip reduction, risk reduction, or authoritative state**—otherwise it is **cost**, not ROI (**instrumentation does not default to labor savings**).
2. **Manual process and naming before scale**: defined assets, good/bad thresholds, **one season** of logs before **fleet** or **tight** alerts.
3. **Degraded modes first**: broker down, power down, alert flood—[`Automation degraded modes and manual fallback SOP`](automation-degraded-modes-manual-fallback-sop.md), runbooks below.
4. **One system of record** for operational events (e.g. farmOS-class)—MQTT is **transport** unless you **explicitly** choose otherwise.
5. **Triage and upkeep are budget lines**—same stature as **capex** ([`Instrumentation ROI`](instrumentation-roi-model-two-site-smart-farm.md)).

---

## Automation **allowed** early (Phase 0–1)

These are **permitted** **before** broad production scaling because they **increase safety**, **reduce blind spots**, or **bind sensors to land**—with **bounded** remote **risk** (mostly **observe**, not **act**).

| ID | Allowed | Why | Still required |
|----|---------|-----|----------------|
| **AA-1** | **Maps**, parcel/paddock IDs, asset registry hooks | Every later sensor **binds** to **land** | Geometry + naming in [`Farm spatial model`](farm-spatial-model-and-asset-registry-standard.md) |
| **AA-2** | **One** **water level** or **pump run/fault** signal on **highest-risk** tank/line | Highest **trip-avoidance** leverage per dollar at distance | Calibration; **freeze** / **fouling** plan; **observational** first |
| **AA-3** | **Power** awareness at **pump** or **field gateway** (uptime, voltage bucket) | Explains **silent** failures | Not a substitute for **genset** / **transfer** plan |
| **AA-4** | **Backup + tested restore** of **records** and **broker config** at **home** | Brain survives disk | **Scheduled** restore **test**; **offline** export |
| **AA-5** | **Documented** MQTT topics / **one** field node → **home** broker **pilot** | Proves **path** before **fleet** | **No** duplicate consumers without **written** reason |
| **AA-6** | **Read-only** dashboards for **gate** state **if** **physical** safe-default is **already** true | Visibility **without** **remote actuation** | See **proof gates** below |

**Rule**: **AA-2–AA-3** default to **observational** (**sense + alert**). **Remote actuation** requires **proof gates** (next section).

---

## Automation **forbidden** early (Phase 0–1)

Deploying these **before** **manual** competence, **registry**, and **ROI/triage** discipline is **forbidden**—they **inflate** **OPEX**, **triage**, **attack surface**, or **liability** without **offsetting** **documented** value.

| ID | Forbidden early | Why |
|----|-----------------|-----|
| **AF-1** | **Camera mesh** “everywhere” | Bandwidth, storage, privacy, **triage** load—[`ROI false-positive fields`](instrumentation-roi-model-two-site-smart-farm.md) |
| **AF-2** | **Herd-wide GPS collars** (fleet) | OPEX, vendor lock; weak ROI at **small** herd **unless** **proven** **must-have** |
| **AF-3** | **Full irrigation automation** (valves, schedules) | Skill + crop commitment—**off** default **grazing** path until **Phase 3+** **and** **gates** |
| **AF-4** | **Remote gate / pump actuation** **without** **proof gates** met | **Safety + liability** |
| **AF-5** | **“AI”** on edge for **decisions** | After **SOPs**, **labels**, and **human** **baseline** |
| **AF-6** | **Second** parallel **system of record** **or** **shadow** MQTT consumers | Integration **debt** + **alert** duplication |
| **AF-7** | **Fleet** expansion while **pilot** **triage** **hours** **exceed** **budget** | [`Automation stop rules`](automation-stop-rules-two-site-smart-farm.md) |

**Defer** does **not** mean “never”—it means **not until** **stop rules** and **ROI** **PASS**.

---

## Proof requirements **before** remote actuation

**Actuation** = **any** remote command that **moves** water, **starts/stops** a pump **beyond** local **hardware** safeties, **opens/closes** a gate, or **changes** **setpoints** that can **harm** stock, **flood**, or **strand** vehicles.

| Proof ID | Requirement | Before enabling… |
|----------|-------------|------------------|
| **PA-1** | **Manual** knowledge: **normal** vs **failure** **behavior** (stick, timer, visual, **flow**) **documented** | **Remote** pump logic / **setpoints** |
| **PA-2** | **Written** **safe default** (**fail-safe** direction) for **gate** and **pump** | **Remote** gate or **pump** **control** |
| **PA-3** | **Physical** **visit** rhythm **proven** **sustainable** (weekly animal/asset check **or** **batch** policy) **without** **alert addiction** | **Escalation** rules that **trigger** **more** **trips** |
| **PA-4** | **Pilot** period: **instrument** ran **observe-only** **≥** **`T_OBSERVE_MIN`** (placeholder **weeks**) with **logged** **true/false** **alert** **rates** | **Closing** the loop to **actuate** |
| **PA-5** | **Spares** path for **actuator** / **relay** / **radio** **documented** | **Production** reliance on **remote** **fix** |
| **PA-6** | **Cyber**: **inventory**, **remote access** **posture**, **patch** **owner** ([`Security obligations`](#security-obligations-non-negotiable)) | **Any** **inbound** **from** **internet** |

**Phase 1 default**: **Meet PA-1–PA-3** for **operations**; **PA-4–PA-6** **before** **turning on** **remote** **actuation**. **Phase 1 observational-only** list: [`Automation stop rules`](automation-stop-rules-two-site-smart-farm.md#phase-1-observational-only-by-default).

---

## Maintenance burden assumptions (book explicitly)

Automation **creates** **recurring** **owner** work. **Assume** these **unless** **measured** otherwise and **revised** in [`Instrumentation ROI`](instrumentation-roi-model-two-site-smart-farm.md):

| Burden class | Assumption (placeholder) | Where to log |
|--------------|--------------------------|--------------|
| **Patch / upgrade** | **`H_PATCH_MO`** hours/month on **broker**, **OS**, **containers** | ROI **upkeep** fields |
| **Physical** **field** **maintenance** | **`H_FIELD_MO`**—battery, **antenna**, **corrosion**, **critters** | Same |
| **Alert** **triage** | **`H_TRIAGE_MO`**—see ROI; **ceiling** **`H_TRIAGE_MAX`** per [`Enterprise unit economics`](enterprise-unit-economics-worksheet-methodology-two-site-smart-farm.md) | Stop rules |
| **Subscription** **admin** | **`H_ADMIN_MO`**—SIMs, **billing**, **vendor** **portals** | ROI |
| **Incident** **response** | **`N_INC_MO`**, **`H_INC_MO`**—not “saved labor” until **SOP** **proves** **reduction** | ROI **false-positive** **cost** |

**Rule**: If **sum** of **burden** **hours** **≥** **documented** **trip/time** **saved**, the **instrument** **fails** **net** **labor** **test**—**even** **if** **capex** **sunk**.

---

## Security obligations (non-negotiable)

Remote access and **cloud** **hooks** **expand** **blast radius**. Minimum **before** **scaling** **exposed** **surfaces**:

| ID | Obligation |
|----|------------|
| **SO-1** | **Asset inventory** of **remote** **access** **paths** (who, what, **MFA**)—CISA-style **mindset**; see planning framework **source** links |
| **SO-2** | **Segmentation** intent: **home** **LAN** vs **IoT** vs **field** **VPN**—**documented**, even if **imperfect** **at** **first** |
| **SO-3** | **Patch** **cadence** **owner** (name **or** **role**) and **rollback** **path** for **broker** |
| **SO-4** | **Secrets** **not** **only** on **field** **edge**; **rotation** **plan** for **VPN** **and** **MQTT** **creds** |
| **SO-5** | **No** **anonymous** **inbound** to **actuators**—**break-glass** **only** **with** **logging** |

**Financing tie-in**: Do **not** **finance** **gadget** **stacks** **on** **consumer** **credit**—[`Validation backlog`](validation-backlog-before-major-spend-two-site-smart-farm.md), [`CAPEX/OPEX sequencing`](capex-opex-enterprise-sequencing-two-site-constraint.md).

---

## Stack posture by phase

| Phase | Posture |
|-------|---------|
| **0** | Spreadsheets + photos; avoid **cloud-only** for compliance-critical records |
| **1** | **Pilot**: MQTT → broker at **home**; **1–2** field nodes; **document** topics; **observe-first**—[`stop rules`](automation-stop-rules-two-site-smart-farm.md) |
| **2** | System of record live; **actuation** **only** **where** **PA-*** **met** |
| **3** | Observability: uptime, **alert** **budget**, **spares** list; **fleet** **only** **if** **ROI** **curve** **healthy** |
| **4** | Hardening: segmentation, patch cadence, key rotation |

---

## Failure modes (expect them)

| Mode | Expectation |
|------|-------------|
| Backhaul down | Field edge **fails safe**; **increase** physical check frequency per runbook—**automation** **did** **not** **remove** **need** **for** **batch** **visits** |
| Power loss at 120 | Tanks drain; pumps don’t self-fix—[`Runbook — power loss at remote site`](runbook-power-loss-remote-site.md) |
| Alert flood | Corroborate before mute—[`Runbook — sensor false positive and alert triage`](runbook-sensor-false-positive-alert-triage.md) |
| Cyber | Remote access = exposure—**SO-*** |

---

## Known facts

| ID | Statement |
|----|-----------|
| K1 | The plan designates the **5-acre parcel** as the long-run **operations / telemetry control center**, not primary production. |
| K2 | The vault already contains **reference architecture** and **runbooks** for degraded modes. |

## Assumptions

| ID | Statement |
|----|-----------|
| A1 | Someone in the family can **maintain** one Linux/Docker-class stack **or** budget **paid** support. |
| A2 | Home internet is **good enough** for VPN + monitoring, with a **documented** fallback (LTE/Starlink-class) if required. |

## Open questions

| ID | Question |
|----|----------|
| Q1 | **farmOS vs lighter stack**? [`Comparison`](../comparisons/farmos-vs-lightweight-stack-two-site-farm.md) |
| Q2 | **LoRaWAN vs Meshtastic** for fixed telemetry? [`Comparison`](../comparisons/lorawan-vs-meshtastic-fixed-farm-telemetry.md) |
| Q3 | **Who is on-call** for alerts after normal hours? |
| Q4 | **Maximum** acceptable **alert hours per week** before you **de-scope** sensors? — **See** [`Automation stop rules`](automation-stop-rules-two-site-smart-farm.md) |

---

## Iterative updates

- Fill **Instrumentation priority matrix** [`instrumentation-priority-matrix-two-site-smart-farm.md`](instrumentation-priority-matrix-two-site-smart-farm.md) after pilot **ROI** numbers exist.
- Add **topic naming convention** table when MQTT topics are frozen.
- Date any **stack version** pin and **review quarterly**.

---

## Related pages

- [`Automation stop rules — two-site smart farm`](automation-stop-rules-two-site-smart-farm.md)
- [`Instrumentation ROI model`](instrumentation-roi-model-two-site-smart-farm.md)
- [`East Tennessee two-site farm business plan — labor model and weekly operating rhythm`](east-tennessee-two-site-farm-business-plan-labor-and-family-model.md)
- [`East Tennessee two-site farm business plan — capital plan and phased infrastructure roadmap`](east-tennessee-two-site-farm-business-plan-capital-and-financing.md)
- [`Two-site smart farm operations`](../topics/two-site-smart-farm-operations.md)
