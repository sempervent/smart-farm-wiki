---
title: Smart technology architecture audit (strategic audit)
page_type: analysis
status: active
created: 2026-04-21
updated: 2026-04-21
review_status: unreviewed
tags:
  - architecture
  - telemetry
  - security
  - observability
confidence: medium
---

# Smart technology architecture audit (strategic audit)

**Purpose**: Dedicated **architecture audit** for the **smart-technology** slice of a future **two-site** operation (~homestead + ~120-acre farm), derived from [`Strategic audit — decision-safe operations for a two-site smart farm`](strategic-audit-decision-safe-operations.md) and [`Implementation backlog — strategic audit (P0–P3)`](implementation-backlog-strategic-audit.md). This page names **what exists in the wiki**, **what is missing**, **where the architecture is fragmented**, and what **reference pages, SOPs, and diagrams** are still required.

**Out of scope here**: Pure **business / revenue** economics (see [`Business viability and farm economics — gap analysis`](business-viability-and-farm-economics-gap-analysis.md)); **biological** stocking conclusions.

---

## 1. What the wiki already covers (by focus area)

| Focus area | What exists (representative pages) | Maturity note |
|------------|-------------------------------------|---------------|
| **Field telemetry** | [`Field telemetry reference architecture — homestead + 120-acre farm`](field-telemetry-reference-architecture-homestead-120ac.md) (draft); [`Tracking chickens — motion sensors over LoRa and MQTT`](tracking-chickens-motion-lora-mqtt.md) | Draft **logical** stack only; no deployed topology |
| **Radios & backhaul** | [`Smart agriculture, Meshtastic, and LoRaWAN`](../topics/smart-agriculture-meshtastic-and-lorawan.md), [`Field network IoT comparisons (HaLow, LoRa, NB-IoT)`](../topics/field-network-iot-comparisons.md), [`LoRa, MQTT, and gateway bridges`](../topics/lora-mqtt-and-gateway-bridges.md); concepts [`LoRa (radio)`](../concepts/lora-radio.md), [`LoRaWAN`](../concepts/lorawan.md), [`Meshtastic`](../concepts/meshtastic.md), [`Wi-Fi HaLow`](../concepts/wi-fi-halow.md) | **Literacy** and source clusters; **not** a chosen **backhaul design** |
| **Edge compute** | [`ESP32, ESPHome, and smart-farming builds`](../topics/esp32-iot-smart-farming-and-tooling.md), [`Homelab, self-hosting, and edge narratives`](../topics/homelab-self-hosting-and-edge-narratives.md), [`Docker, Kubernetes, Compose, and Bake (edge and homelab)`](../topics/docker-kubernetes-compose-and-bake.md) | **Patterns**; no **farm edge** boundary (what runs **in field** vs **barn server** vs **home**) |
| **Home Assistant / farmOS / MQTT / TSDB roles** | [`Farm data, farmOS, and agriculture lab builds`](../topics/farm-data-farmos-and-ag-lab-builds.md) (farmOS + lab); [`Smart home — Matter, Thread, and Home Assistant AI`](../topics/smart-home-matter-thread-and-home-assistant-ai.md); [`Data storage (farm and edge stacks)`](../concepts/data-storage.md) (MQTT + PostgreSQL/PostGIS **documentation links**); PostgreSQL/PostGIS **source-notes** | **Roles not adjudicated**: no **system-of-record** decision; TSDB **named as placeholder** in telemetry draft only |
| **Time sync** | [`Time synchronization — NTP and PTP sources`](../topics/time-synchronization-ntp-and-ptp.md); concepts [`NTP`](../concepts/network-time-protocol.md), [`PTP`](../concepts/precision-time-protocol.md); [`Timing on the farm — synthesis`](timing-on-the-farm-synthesis.md) | Good **primer** layer; **not** tied to **sensor timestamp requirements** per subsystem |
| **Device identity** | Implied in [`Spatial data and farm asset registry standard`](farm-spatial-model-and-asset-registry-standard.md) (telemetry `device_id`); MQTT topic patterns in **LoRa/MQTT** source-notes | **No** global **naming authority** document; **no** MQTT topic tree **owned** by you |
| **Asset registry** | [`Spatial data and farm asset registry standard`](farm-spatial-model-and-asset-registry-standard.md) (draft); PostGIS / enterprise PostGIS **source-notes** under [`Farm data…`](../topics/farm-data-farmos-and-ag-lab-builds.md) | Draft **standard**; **not** populated with real IDs |
| **Alerting** | [`Automation degraded modes and manual fallback SOP`](automation-degraded-modes-manual-fallback-sop.md) (failure classes); HA/MQTT threads in topics | **No** alert **routing** design (who gets paged, escalation); **no** “alert pipeline” SOP |
| **Observability** | Backlog P2 **#19** (*Observability and alerts — broker down…*) — **not** a standalone page | **Gap** |
| **Firmware lifecycle** | Backlog P2 **#20**; ESP32/Meshtastic **culture** in topics | **No** policy for **update cadence**, **staging**, **rollback** |
| **Degraded modes** | [`Automation degraded modes and manual fallback SOP`](automation-degraded-modes-manual-fallback-sop.md) (first draft) | Needs **system-specific** fill-ins and **tabletop** validation |
| **Cybersecurity** | Backlog P2 **#15–16** (OT security concept + **farm cybersecurity hub**) — **hubs not created** | **Gap**; scattered **homelab** only |
| **Remote access** | Homelab topic; **no** **bastion/VPN** architecture for **field admin** | **Gap** |

---

## 2. What is missing (architecture-critical)

Aligned to audit **§3–5** and backlog **P0–P2** for technology.

| Layer | Missing artifact | Why it matters |
|-------|------------------|----------------|
| **End-to-end reference** | **One** maintained **reference architecture** (diagram + dataflow + SPOF) **approved for your sites** | Without it, every purchase is ad hoc |
| **System of record** | **Analysis**: *Telemetry system of record — options and boundaries* (farmOS vs HA state vs TSDB/DB) — backlog **P0 #6** | Conflicting **truth** breaks automation and records |
| **Integration pattern** | Canonical **event → device → asset → map geometry** path | Audit: farmOS and telemetry are **adjacent**, not integrated |
| **Topic hubs** | **`Field telemetry and backhaul`**, **`Farm cybersecurity and remote access`** (backlog **#5 topic + #16 hub**) | Stops knowledge living only in long analyses |
| **Security** | **OT/security** concept + **remote access** story (VPN, segmentation, MQTT TLS/auth, camera exposure) | Remote farm is a **high-value** target for misconfiguration |
| **Operations** | **Observability** page; **firmware lifecycle** page; **broker-down / false-positive** runbook | **MTTR** and **trust** in alerts |
| **Time** | **Per-subsystem** clock requirements (e.g. sub-second unnecessary for soil moisture; **correlation** for triangulation)—not written | NTP/PTP **exist** but not **bound** to architecture |
| **Comparisons** | **Gateway architecture — fixed tower vs vehicle vs mesh**; **farmOS vs lightweight** (partially economic, partially ops) | **Decision-grade** tradeoffs |

---

## 3. Where the architecture is currently fragmented

Cross-cutting breaks (from audit **§4 Missing integration layers**, narrowed to **technology**):

1. **Radios ↔ land**: LPWAN/mesh topics **do not** consistently reference **paddock IDs**, **gates**, or **terrain**—[`Domain content overview`](domain-content-overview.md) states this gap.
2. **Records ↔ telemetry**: [`Farm data, farmOS…`](../topics/farm-data-farmos-and-ag-lab-builds.md) and MQTT/LoRa topics **do not** define a **single** ingest or **ID scheme** linking **observations** to **farmOS assets**.
3. **Homelab ↔ field**: [`Homelab…`](../topics/homelab-self-hosting-and-edge-narratives.md) and [`Smart home…`](../topics/smart-home-matter-thread-and-home-assistant-ai.md) are **not** tied to **farm alerting**, **on-call**, or **degraded modes** at the **120-acre** site.
4. **Power ↔ compute ↔ radio**: [`Off-grid solar power and storage`](../topics/off-grid-solar-power-and-storage.md) exists; **field gateway uptime** vs **battery days** is **not** one diagram with **telemetry**.
5. **Time ↔ events**: **NTP/PTP** strand does not state **which logs** must be **traceable** for **debugging** vs **legal** vs **nice-to-have**.
6. **Security ↔ remote access ↔ actuators**: **Irrigation/gates** appear in degraded-mode SOP **placeholders**; **no** **threat model** (who can open what remotely).

**Symptom**: Strong **horizontal** coverage (many topics); weak **vertical** slice from **sensor** → **identity** → **storage** → **alert** → **human** → **fallback**.

---

## 4. Reference architecture page outline (target: one canonical page)

**Suggested path**: `wiki/analyses/architecture-reference-smart-farm-homestead-and-120ac.md` (or evolve [`Field telemetry reference architecture…`](field-telemetry-reference-architecture-homestead-120ac.md) into this **v1.0**).

| Section | Contents |
|---------|----------|
| **1. Document control** | Version, owner, **last site walk date**, **next review** (quarterly recommended) |
| **2. Sites & trust boundaries** | `SITE_HOMESTEAD` vs `SITE_FARM`; **LAN**, **VPN**, **cellular**, **internet**; **what must never cross** (e.g. cameras to public MQTT) |
| **3. Logical diagram** | Field devices → edge/gateway → backhaul → **broker** → consumers (HA, farmOS ingest, TSDB, alerts) |
| **4. Dataflow & system of record** | **Authoritative** store per data type (telemetry history, agronomic record, alert state); **conflict resolution** |
| **5. Identity** | **Device ID**, **MQTT topic root**, **TLS/client ID** policy; link [`Spatial data and farm asset registry standard`](farm-spatial-model-and-asset-registry-standard.md) |
| **6. Time** | **Stratum** for servers; **NTP** sources; **PTP** if used; **sensor timestamp** rules |
| **7. Radios & backhaul** | Chosen stacks (placeholders until decided): LoRaWAN vs Meshtastic vs HaLow vs Wi‑Fi; **failover** |
| **8. Edge compute** | What runs **on** gateways vs **barn NUC** vs **home**; **container** runtime if any |
| **9. Alerting & observability** | Path from **metric/event** → **notification**; **on-call**; **dead-man** checks for broker |
| **10. Degraded modes** | Link [`Automation degraded modes…`](automation-degraded-modes-manual-fallback-sop.md); **per-system** safe states |
| **11. Security & remote access** | VPN, **MQTT auth**, **segmentation**, **camera policy**, **patch cadence** |
| **12. Firmware & lifecycle** | **Update** policy, **test** device, **rollback** |
| **13. SPOF & test plan** | Table: component, failure mode, **detection**, **mitigation**, **last drill** |
| **14. Related diagrams** | List of **required figures** (below) |

---

## 5. Required SOPs (prioritized)

| SOP | Intent | Backlog / status |
|-----|--------|------------------|
| **Degraded modes — automation off** | Manual safe state when logic or comms fails | Draft: [`Automation degraded modes…`](automation-degraded-modes-manual-fallback-sop.md) |
| **Observability — broker down, false positives, on-call** | What to do when **alerts lie** or **stop** | P2 #19 — **to write** |
| **Incident — telemetry integrity suspected** (sensor lying, stale data) | Disable **closed-loop** control | **New** |
| **Firmware / certificate update — field gateway** | Ordered steps; **rollback** | Derive from P2 #20 |
| **Remote access session — admin to field network** | VPN/bastion steps; **no** permanent port forwards without review | Part of cybersecurity hub |
| **Time sync failure — skew beyond threshold** | Which subsystems **halt** vs **degrade** | **New** |
| **New device onboarding** | ID assignment, topic provisioning, **registry** row, **test** plan | **New** |

---

## 6. Required diagrams (checklist)

| Diagram | Shows |
|---------|--------|
| **D1 — Physical topology** | Homestead vs farm buildings, **towers**, **gateways**, **solar**, **fiber/radio** paths (even **notional**) |
| **D2 — Network & trust zones** | VLANs or **zones**: **cameras**, **PLC/irrigation**, **guest Wi‑Fi**, **management** |
| **D3 — MQTT / dataflow** | Topics (high level), **broker**, **bridges**, **HA**, **farmOS**, **TSDB** |
| **D4 — Alert path** | Trigger → **rule engine** → channel (SMS/push/voice) → **escalation** |
| **D5 — Power & uptime** | Field gateway: **solar/battery/grid**, **autonomy days**, **low-voltage cutoff** |
| **D6 — Time** | Which hosts use **which** NTP/PTP; **GNSS** if any |
| **D7 — Degraded mode decision tree** | Internet down / broker down / **sensor fault** / **actuator fault** → **safe state** |
| **D8 — Remote admin** | VPN to **where**; **jump host**; **no** direct SSH to cameras from internet |

**Format**: Mermaid in wiki, **or** exported PNG/SVG in `raw/assets/` with source-note—**your** choice; keep **one** canonical diagram set per [`AGENTS.md`](../../AGENTS.md) citation rules.

---

## 7. Related pages

- [`Implementation backlog — strategic audit (P0–P3)`](implementation-backlog-strategic-audit.md)
- [`Information architecture — decision-safe operational brain (target design)`](information-architecture-decision-safe-operations.md)
- [`Business viability and farm economics — gap analysis`](business-viability-and-farm-economics-gap-analysis.md) — economics only

---

*Update when P0 telemetry architecture is promoted from **draft** to **v1.0**, or when cybersecurity / observability hubs ship.*
