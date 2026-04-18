---
title: Gateway naming and role assignment standard
page_type: analysis
page_subtype: standard
operational_maturity: pilot_ready
status: active
created: 2026-04-24
updated: 2026-04-24
tags:
  - gateway
  - wan
  - telemetry
  - standards
review_status: reviewed
confidence: high
---

# Gateway naming and role assignment standard

## Purpose

Disambiguate **RF / telemetry gateways** (field → **MQTT** / **broker**) from **WAN edge** (Starlink / LTE **CPE**) in **names**, **diagrams**, and **runbooks**—matches [`RF and telemetry gateway roles`](../entities/rf-telemetry-gateway-roles-field-network.md) and [`WAN edge and backhaul roles`](../entities/wan-edge-and-backhaul-roles.md).

---

## Standard

| Role | Name pattern (example) | Must not be called |
|------|------------------------|----------------------|
| **Telemetry / RF gateway** (mesh/LPWAN → IP) | `{SITE}-GW-RF-{n}` or embed **G** class | **“router”** **alone** |
| **WAN CPE** (internet **egress**) | `{SITE}-WAN-{tech}-{n}` | **“gateway”** **without** **WAN** **context** |
| **Home** / **barn** **LAN** **router** | `{SITE}-LAN-CORE` (optional) | Same as **RF** **gateway** **name** |

**Documentation**: **Every** **diagram** **legend** **defines** **G** **vs** **W** **(or** **RF** **vs** **WAN** **)** **once**.

---

## Related

- [`Field telemetry network — two-site`](../entities/field-telemetry-network-two-site.md)
- [`Connectivity strategy — Claxton home base and Demory farm site`](connectivity-strategy-for-claxton-and-demory.md)
- [`Operational standards — farm and homelab platform`](../topics/operational-standards-farm-homelab-platform.md)
