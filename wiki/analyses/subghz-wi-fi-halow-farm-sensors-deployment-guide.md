---
title: Sub-GHz Wi‑Fi (802.11ah / HaLow) — farm sensors and IP backhaul (how-to outline)
page_type: analysis
status: active
created: 2026-04-18
updated: 2026-04-18
tags:
  - wi-fi-halow
  - 802-11ah
  - farm
  - sensors
review_status: unreviewed
confidence: medium
---

# Sub-GHz Wi‑Fi (802.11ah / HaLow) — farm sensors and IP backhaul (how-to outline)

## Purpose

Structured **how-to outline** for using **802.11ah (Wi‑Fi HaLow)** across a farm for **sensor-grade IP** links and **local backhaul**—with **explicit assumptions** and **links to vault sources**. This is **not** a substitute for **site survey**, **regulatory**, and **vendor** manuals.

**Concept primer**: [`Wi‑Fi HaLow`](../concepts/wi-fi-halow.md).

---

## 1. Clarify the job

| Need | HaLow often fits when… | Often wrong tool when… |
|------|------------------------|-------------------------|
| **Sparse telemetry** (kB/day) | You still want **IP** on device or **MQTT** without building many 2.4 GHz hops | Power budget is **tiny** and range is **extreme**—consider **LoRa/Meshtastic** ([`comparison`](../comparisons/wi-fi-halow-lorawan-meshtastic-conventional-wi-fi-farm-field-networking.md)) |
| **IP cameras / moderate throughput** | You can place **AP + antennas** with **line of sight** or good sub-GHz behavior | You need **multi-acre mesh** without careful RF design—validate with **field test** |
| **Backhaul to barn** | You have **Ethernet** at one end and **HaLow bridge** at the other | **Starlink** alone is easier but **different** failure mode ([`connectivity strategy`](connectivity-strategy-for-claxton-and-demory.md)) |

---

## 2. Architecture pattern (generic)

1. **Edge router / firewall** remains the **trust anchor**—HaLow is **LAN extension**, not a bypass of segmentation ([`network segmentation`](network-segmentation-site-to-site-and-internet-exposure-two-site-smart-farm.md)).
2. **HaLow AP** uplinks via **Ethernet** to PoE switch or **gateway** (capture shows **AP + bridge** pattern).
3. **Sensors / bridges** attach as **802.11ah STAs** or via **Wi‑Fi → HaLow bridge** for legacy 2.4 GHz devices (vendor PoC narrative).

**Source (PoC narrative, not universal)**: [`how-to 10x reach HaLow` Silex-style capture](../../raw/processed/2026/how-to-10x-the-reach-of-wi-fi-devices-with-wi-fi-halow-802-11ah-inbox-2026-04-23.md) — **SSID/PSK**, **Ethernet** to network, **WPA3** mentioned for HaLow link.

---

## 3. Field steps (operator checklist)

| Step | Action | Citation / note |
|------|--------|-----------------|
| **A** | **Map** power at AP and bridge sites (solar/battery headroom) | [`Off-grid power — Demory`](off-grid-power-strategy-demory-farm-site.md) |
| **B** | **Choose** band / channel plan for **your** regulatory domain | **Not** in vault as legal advice—verify locally |
| **C** | **Cable** Ethernet with **surge** discipline at building entry | [`Wiring` / electrical cluster](../source-notes/electrical-networking-starlink-inbox-batch-2026-04-23.md) |
| **D** | **Configure** SSIDs; **isolate** IoT **VLAN** if available on upstream router | [`Segmentation` page](network-segmentation-site-to-site-and-internet-exposure-two-site-smart-farm.md) |
| **E** | **Measure** RSSI/throughput **seasonally** (leaf-on, rain) | Same expectation as **V10** WAN logging ([`validation plan`](validation-and-pilot-plan-first-24-months-east-tennessee-two-site.md)) |

---

## 4. Sensor traffic profile

- **Observation-only** (temp, tank level via IP MCU): usually **fits** HaLow if **duty cycle** and **firmware** are sane.
- **Safety interlocks**: prefer **wired** or **proven** local link; do not rely on **best-effort** IP alone ([`automation stop rules`](automation-stop-rules-two-site-smart-farm.md)).

---

## 5. Related comparisons

- [`Wi‑Fi HaLow vs LoRaWAN vs Meshtastic vs conventional Wi‑Fi — farm field networking`](../comparisons/wi-fi-halow-lorawan-meshtastic-conventional-wi-fi-farm-field-networking.md)
- [`Meshtastic vs HaLow vs conventional Wi‑Fi — off-grid operations`](../comparisons/meshtastic-wi-fi-halow-conventional-wi-fi-off-grid-farm-operations.md)
