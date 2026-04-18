---
title: Mesh and field networking strategy — off-grid Demory farm
page_type: analysis
status: active
created: 2026-04-24
updated: 2026-04-25
review_status: unreviewed
tags:
  - mesh
  - meshtastic
  - halow
  - off-grid
  - demory
confidence: medium
---

# Mesh and field networking strategy — off-grid Demory farm

## Purpose

Define **how** **`SITE_FARM`** **(Demory)** **should** **use** **local** **RF** **and** **LAN** **when** **off-grid-first** **:** **resilient** **mesh** **behavior** **,** **offline** **survivability** **,** **and** **WAN** **/** **Starlink** **only** **as** **secondary** **convenience** **—** **aligned** **with** [`Connectivity strategy — Claxton & Demory`](connectivity-strategy-for-claxton-and-demory.md) **(**farm** **WAN** **conditional** **/** **deferred** **)** **.**

**Doctrine package**: [`Off-grid systems doctrine package — Demory`](../topics/off-grid-systems-doctrine-package-demory-farm-site.md) · [`Field-node classes and communication roles — Demory`](field-node-classes-and-communication-roles-demory-farm.md).

**Sources**: [`Off-grid power, field RF, and optional WAN — source index`](../source-notes/off-grid-power-rf-wan-source-index-demory-planning-2026-04.md).

**Comparison** (Meshtastic vs HaLow vs Wi‑Fi): [`Meshtastic vs Wi‑Fi HaLow vs conventional Wi‑Fi — off-grid farm operations`](../comparisons/meshtastic-wi-fi-halow-conventional-wi-fi-off-grid-farm-operations.md).

---

## Layering (policy)

| Layer | Role at Demory | WAN required? |
|-------|----------------|---------------|
| **Sensor** **/** **LPWAN** **/** **mesh** **(e.g.** **Meshtastic** **,** **LoRa** **)** | **Sparse** **telemetry** **,** **text** **/** **position** **class** **traffic** **;** **multi-hop** **where** **terrain** **breaks** **LOS** | **No** **for** **local** **delivery** **to** **gateway** **.** |
| **Sub-GHz** **Wi‑Fi** **/** **HaLow** **(802.11ah)** | **Higher** **throughput** **than** **LoRa** **for** **IP** **devices** **where** **HaLow** **hardware** **exists** **and** **ROI** **clears** | **No** **for** **LAN** **segment** **;** **egress** **optional** **.** |
| **Conventional** **Wi‑Fi** **/** **Ethernet** | **Barn** **office** **,** **NVR** **on** **LAN** **,** **gateway** **uplink** **to** **fiber** **/** **LTE** **/** **Starlink** **CPE** | **LAN** **survives** **WAN** **loss** **;** **cloud** **features** **don’t** **.** |
| **WAN** **(** **Starlink** **,** **LTE** **)** | **Egress** **,** **optional** **admin** **,** **maps** | **Secondary** **—** **see** **“** **must** **not** **depend** **”** **below** **.** |

---

## Where Meshtastic is a good fit

- **Ultra-low** **average** **power** **nodes** **with** **solar** **+** **small** **pack** **at** **distant** **fence** **/** **tank** **corners** **.**
- **Messaging** **/** **presence** **/** **simple** **telemetry** **when** **LoRa** **ISM** **rules** **and** **firmware** **ops** **are** **acceptable** **.**
- **Mesh** **resilience** **where** **no** **single** **tower** **gateway** **sees** **all** **paddocks** **—** [`LoRaWAN vs Meshtastic`](../comparisons/lorawan-vs-meshtastic-fixed-farm-telemetry.md) **.**

---

## Where Wi‑Fi HaLow is a better fit

- **IP** **throughput** **needed** **beyond** **LoRa** **rates** **but** **still** **want** **sub-GHz** **penetration** **—** **Morse** **Micro** **datasheets** **in** [`source index`](../source-notes/off-grid-power-rf-wan-source-index-demory-planning-2026-04.md) **.**
- **Bridging** **a** **few** **IP** **sensors** **or** **cameras** **across** **hundreds** **of** **meters** **where** **2.4** **/** **5** **GHz** **is** **weak** **(**homelab** **802.11ah** **mesh** **capture** **in** **source** **index** **)** **.**
- **Still** **requires** **clear** **ops** **:** **router** **/** **OpenWrt** **class** **support** **,** **antenna** **plan** **,** **security** **patching** **.**

---

## Where conventional Wi‑Fi or Ethernet still belongs

- **Short** **range** **high** **throughput** **inside** **barn** **/** **equipment** **shed** **(NVR** **,** **laptop** **config** **)** **.**
- **Backhaul** **from** **field** **gateway** **to** **Starlink** **/** **LTE** **CPE** **over** **Ethernet** **(preferred** **)** **.**
- **Do** **not** **stretch** **one** **fat** **Wi‑Fi** **SSID** **across** **120** **ac** **—** **use** **mesh** **/** **HaLow** **/** **fiber** **where** **needed** **.**

---

## What must work with no WAN

- **Local** **sensor** **→** **gateway** **→** **actuator** **interlocks** **(**water** **,** **gate** **safe** **states** **)** **.**
- **Meshtastic** **/** **LoRa** **mesh** **delivery** **to** **a** **field** **gateway** **that** **buffers** **or** **displays** **locally** **.**
- **Operator** **physical** **rounds** **and** **paper** **fallback** **(**[`Manual fallback`](manual-fallback-degraded-modes-critical-operations.md)**)** **.**

---

## What may rely on WAN / Starlink

- **Cloud** **dashboards** **,** **OTA** **firmware** **(if** **chosen** **)** **,** **optional** **egress** **of** **MQTT** **.**
- **Maps** **,** **weather** **radar** **,** **voice** **when** **mobile** **.**

**Starlink** **must** **not** **become** **a** **hidden** **dependency** **for** **:** **welfare** **verification** **,** **sole** **path** **for** **books** **,** **assumed** **camera** **coverage** **everywhere** **,** **or** **“** **we** **know** **the** **tanks** **are** **full** **because** **the** **app** **says** **so** **”** **without** **G8** **/** **manual** **baseline** **(**[`Connectivity strategy`](connectivity-strategy-for-claxton-and-demory.md)**)** **.**

---

## Security (brief)

- **Z2** **field** **OT** **—** **same** **as** [`Remote access model`](remote-access-operational-security-model-two-site-smart-farm.md) **and** [`Segmentation policy`](network-segmentation-site-to-site-and-internet-exposure-two-site-smart-farm.md) **:** **no** **flat** **admin** **from** **WAN** **to** **cameras** **.**

---

## Related

- [`Farm sensor architecture — Demory farm site`](farm-sensor-architecture-demory-farm-site.md) — reference / pilot / degraded diagrams; Starlink as WAN only
- [`Off-grid power doctrine — Demory farm site`](off-grid-power-strategy-demory-farm-site.md)
- [`Field telemetry reference architecture — homestead + 120-acre farm`](field-telemetry-reference-architecture-homestead-120ac.md)
- [`Execution topology package — two-site smart farm (Mermaid)`](execution-topology-package-two-site-smart-farm.md)
