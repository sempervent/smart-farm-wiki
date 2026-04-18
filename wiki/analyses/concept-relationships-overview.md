---
title: Concept relationships — summary objects
page_type: analysis
status: active
created: 2026-04-17
updated: 2026-04-17
tags:
  - concepts
  - graph
  - synthesis
confidence: medium
review_status: unreviewed
---

# Concept relationships — summary objects

This page **synthesizes** how domain **concepts** relate: short **summary objects** (one-line roles + explicit `relates_to` edges) for agents and humans. Provenance remains on individual concept pages and source-notes; this is navigational structure only.

**See also:** [`Knowledge synthesis`](../topics/knowledge-synthesis.md), [`LLM Wiki pattern`](../concepts/llm-wiki-pattern.md).

---

## Clusters (narrative)

### LPWAN, Wi‑Fi, and mesh (field RF)

[`LoRa (radio)`](../concepts/lora-radio.md) is the shared **PHY** for both [`LoRaWAN`](../concepts/lorawan.md) (star/gateway uplinks) and [`Meshtastic`](../concepts/meshtastic.md) (mesh firmware). [`Wi-Fi HaLow`](../concepts/wi-fi-halow.md) is an alternative sub-GHz **802.11**-family stack often compared to LoRa-class LPWAN for throughput/range tradeoffs—not the same PHY as LoRa.

### Agriculture and edge compute

[`Precision agriculture`](../concepts/precision-agriculture.md) is the **management science** framing; [`LoRaWAN`](../concepts/lorawan.md) and [`ESP32`](../concepts/esp32.md) appear as common **telemetry / actuator** layers in source material, not equivalents.

### Time and infrastructure

[`Network Time Protocol (NTP)`](../concepts/network-time-protocol.md) and [`Precision Time Protocol (PTP)`](../concepts/precision-time-protocol.md) are **distribution/discipline** protocols over IP/Ethernet; they pair with GNSS in sources but are not GNSS themselves.

### Incentivized infrastructure

[`Decentralized physical infrastructure networks (DePIN)`](../concepts/depin.md) is an **economic/architecture** pattern sometimes listed beside **LPWAN** and **802.11ah** in survey material—treat as orthogonal to PHY choice unless a source ties them for a specific deployment.

### Meta (this vault)

[`LLM Wiki pattern`](../concepts/llm-wiki-pattern.md) describes **raw vs wiki** maintenance; it does not assert domain RF facts.

---

## Summary table

| Concept | One-line summary | Relates to |
|--------|-------------------|------------|
| [`DePIN`](../concepts/depin.md) | Incentivized shared physical/digital networks | LoRa, LoRaWAN, Wi‑Fi HaLow |
| [`ESP32`](../concepts/esp32.md) | Espressif SoC line for Wi‑Fi/BT IoT, sensors, displays | LoRa (radio), Meshtastic, precision agriculture |
| [`LoRa (radio)`](../concepts/lora-radio.md) | Semtech-style chirp PHY for long-range low-rate RF | LoRaWAN, Meshtastic, Wi‑Fi HaLow |
| [`LoRaWAN`](../concepts/lorawan.md) | MAC + network stack on LoRa to gateways/servers | LoRa (radio), Meshtastic, precision agriculture |
| [`Meshtastic`](../concepts/meshtastic.md) | LoRa mesh firmware for local comms/telemetry | LoRa (radio), LoRaWAN |
| [`NTP`](../concepts/network-time-protocol.md) | Internet clock sync, typically ms-scale | PTP |
| [`Precision agriculture`](../concepts/precision-agriculture.md) | Data-driven spatial/temporal farm management | ESP32, LoRaWAN |
| [`PTP`](../concepts/precision-time-protocol.md) | IEEE 1588 clock sync, often ns/sub-µs with HW assist | NTP |
| [`Wi-Fi HaLow`](../concepts/wi-fi-halow.md) | IEEE 802.11ah sub-GHz Wi‑Fi for IoT range/power | LoRa (radio), LoRaWAN |
| [`LLM Wiki pattern`](../concepts/llm-wiki-pattern.md) | Raw evidence vs maintained synthesis in this repo | (meta) |

---

## Machine-readable summary objects (YAML)

Stable ids are **`concepts/<kebab-file>.md`** paths relative to the `wiki/` directory.

```yaml
concept_summaries:
  - id: concepts/depin.md
    summary: "Token-incentivized shared physical/digital infrastructure."
    relates_to:
      - concepts/lora-radio.md
      - concepts/lorawan.md
      - concepts/wi-fi-halow.md
  - id: concepts/esp32.md
    summary: "Espressif SoC family for Wi-Fi/BT IoT, sensors, displays."
    relates_to:
      - concepts/lora-radio.md
      - concepts/meshtastic.md
      - concepts/precision-agriculture.md
  - id: concepts/lora-radio.md
    summary: "Proprietary LoRa PHY; underpins LoRaWAN and Meshtastic radios."
    relates_to:
      - concepts/lorawan.md
      - concepts/meshtastic.md
      - concepts/wi-fi-halow.md
  - id: concepts/lorawan.md
    summary: "LPWAN star topology on LoRa to gateways and network servers."
    relates_to:
      - concepts/lora-radio.md
      - concepts/meshtastic.md
      - concepts/precision-agriculture.md
  - id: concepts/meshtastic.md
    summary: "Open LoRa mesh firmware for off-grid local relay."
    relates_to:
      - concepts/lora-radio.md
      - concepts/lorawan.md
  - id: concepts/network-time-protocol.md
    summary: "NTP — internet time sync, typically millisecond-scale."
    relates_to:
      - concepts/precision-time-protocol.md
  - id: concepts/precision-agriculture.md
    summary: "Spatial/temporal data-driven farm management."
    relates_to:
      - concepts/esp32.md
      - concepts/lorawan.md
  - id: concepts/precision-time-protocol.md
    summary: "IEEE 1588 PTP — tight clock sync over Ethernet/IP."
    relates_to:
      - concepts/network-time-protocol.md
  - id: concepts/wi-fi-halow.md
    summary: "IEEE 802.11ah sub-GHz Wi-Fi for IoT range and power tradeoffs."
    relates_to:
      - concepts/lora-radio.md
      - concepts/lorawan.md
  - id: concepts/llm-wiki-pattern.md
    summary: "Repository pattern — raw evidence vs wiki synthesis."
    relates_to: []
```

---

## Limits

- **Not a formal ontology** — edges are pragmatic reading aids; refine when new sourced analyses appear.
- **LLM Wiki pattern** has empty `relates_to` in YAML to keep domain RF concepts separate from meta.
