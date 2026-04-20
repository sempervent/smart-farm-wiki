---
title: SX1302 gateway — Waveshare HAT captures and Lora-net sx1302_hal (inbox batch 2026-04-20)
page_type: source_note
status: active
created: 2026-04-20
updated: 2026-04-20
source_ids:
  - raw/processed/2026/lora-net-sx1302-hal-readme-packet-forwarder-tools.md
  - raw/processed/2026/waveshare-sx1302-lorawan-gateway-hat-wiki.md
  - raw/processed/2026/waveshare-sx1302-lorawan-gateway-hat-product-page-eu868-gnss.md
source_count: 3
tags:
  - ingest-batch
  - lorawan
  - sx1302
  - waveshare
  - semtech
review_status: unreviewed
confidence: high
---

# SX1302 gateway — Waveshare HAT captures and Lora-net sx1302_hal (inbox batch 2026-04-20)

**Purpose**: Provenance for **Semtech SX1302/SX1303** gateway **software** (upstream HAL / packet forwarder) plus **Waveshare** **Pi HAT** vendor captures (EU868 module + GNSS). **Not** RF regulatory or site-survey advice—follow local band rules and licensed professionals where applicable.

**Downstream hubs**: [`Smart agriculture, Meshtastic, and LoRaWAN`](../topics/smart-agriculture-meshtastic-and-lorawan.md) · [`LoRa, MQTT, and gateway bridges`](../topics/lora-mqtt-and-gateway-bridges.md) · [`Demory farm sensor layer — official and operator-grade source cluster`](demory-farm-sensor-layer-official-and-operator-source-cluster.md)

## Evidence summary

| Field | Content |
|-------|---------|
| **Abstract** | Three **markdown captures**: (1) **Lora-net** `sx1302_hal` **project readme**—libloragw, packet forwarder, USB vs SPI, build/changelog; (2) **Waveshare wiki**—HAT setup with **The Things Stack**, Pi 4/5 demos, FAQs; (3) **Waveshare product page**—discontinued-SKU notice, kit list, L76x GNSS. Together they support **gateway bring-up literacy** next to LoRaWAN stack docs already in the vault. |
| **Authority mix** | **Upstream open-source** (Semtech/Lora-net) + **vendor** (Waveshare wiki/product)—**hardware facts** and **procedure** color; corroborate **regulatory** band use with primary radio rules. |
| **Decision relevance** | Choosing **SX1302-class** Pi **gateways**, **`sx1302_hal`** / **packet forwarder** paths, **TTS** registration, **GNSS-assisted** gateway time; **EU868** vs other regional products. |
| **Canonical wiki links** | [`LoRaWAN`](../concepts/lorawan.md) · [`Inbox batch — Tennessee farm policy, LoRaWAN field stack, ChirpStack, Meshtastic, Decentlab, HaLow (2026-04-18)`](inbox-batch-2026-04-18-tennessee-farm-lorawan-chirpstack-meshtastic-decentlab-halow.md) |

**Key claims** (public-safe; cite raw for version-specific detail):

- **`sx1302_hal`** documents **SPI and USB** Corecell paths, **`packet_forwarder`** uplink/downlink over UDP, **`reset_lgw.sh`** co-location with binaries, and **cross-compile** / **`target.cfg`** install flows.
- **Waveshare HAT** docs describe **EU868** focus, **L76K/L76B** GNSS for PPS/time, **Mini-PCIe** SX1302 module, and **TTS**-oriented **EUI** / **`test_conf.json`** steps.

**Open questions / follow-ups**

- If a **live** two-site deployment standardizes this HAT, fold hardware-specific **runbook** rows into an operational guide and **standards** page—this note stays **vendor + upstream** provenance.

---

## Raw sources and ingest descriptions

| Ingest description | Raw |
|-------|-----|
| **Lora-net `sx1302_hal` readme (tools, packet forwarder, changelog).** Semtech/Lora-net documentation for the **SX1302/SX1303** gateway **HAL**: **`libloragw`** builds to a static library; **packet forwarder** bridges concentrator RF to UDP for a network server; helpers include **util_chip_id** (gateway EUI), **util_net_downlink**, **util_boot** (USB DFU for STM32 bridge), **util_spectral_scan** (sx1261 on Corecell v3). Covers **SPI vs USB** (USB uses STM32 USB↔SPI bridge; MCU firmware in `mcu_bin`), **`tools/reset_lgw.sh`** GPIO init, **make** / **`target.cfg`** install and **ARM cross-compile**, third-party libs (parson, tinymt32), and a long **changelog** (fine timestamping, spectral scan, LBT AS923, SX1303, PROTOCOL updates, CN490 full-duplex merges, etc.). Ends with Semtech legal disclaimer. | [`lora-net-sx1302-hal-readme-packet-forwarder-tools.md`](../../raw/processed/2026/lora-net-sx1302-hal-readme-packet-forwarder-tools.md) |
| **Waveshare SX1302 LoRaWAN Gateway HAT — wiki.** Full vendor wiki: **SX1302/SX1303 + SX1250**, PA/LNA, **EU868**-oriented specs, **Mini-PCIe** module on HAT, **L76K** GNSS (GPS/BD), 40-pin Pi header. **LoRa vs LoRaWAN** primer, architecture diagram (nodes → gateway → server/cloud), **OTAA** join narrative, **The Things Stack** gateway registration, **`chip_id`** for EUI, Pi **4B** (`ws-dev` fork clone) vs **5** (zip demo) build paths, **`global_conf.json.sx1250.EU868`** → **`test_conf.json`**, merge with server-downloaded **`radio_*` / `gateway_conf`**, run **`lora_pkt_fwd`**. Links to **`sx1302_hal`**, datasheets, schematic, 3D, GNSS docs. **FAQ**: enable I2C/SPI/UART, reseat modules on SX1250 errors, **China** band caveat (EU868 vs 470 MHz), **SX1302 vs SX1303** (fine timestamps / TDOA on SX1303), Pi 5 GPIO caveat. | [`waveshare-sx1302-lorawan-gateway-hat-wiki.md`](../../raw/processed/2026/waveshare-sx1302-lorawan-gateway-hat-wiki.md) |
| **Waveshare product page — EU868 HAT (discontinued banner).** Short product-page copy: **discontinued** SKU with pointer to replacement **SX1302 868M LoRaWAN Gateway HAT**; **L76B** GNSS (GPS/BD), **SX1302 + SX1250** EU868, Mini-PCIe, power figures, marketing feature bullets, **on-board** component map (including **ML1220** battery for GNSS ephemeris), pinout/size images, **kit contents** (HAT, module, antennas, headers, IPEX, screws). | [`waveshare-sx1302-lorawan-gateway-hat-product-page-eu868-gnss.md`](../../raw/processed/2026/waveshare-sx1302-lorawan-gateway-hat-product-page-eu868-gnss.md) |

---

## See also

- [`Semtech LoRa smart agriculture applications`](semtech-lora-smart-agriculture-applications.md)
- [`MQTT Manager — “poor man’s gateway” (Instructables)`](mqtt-manager-lora-poor-man-gateway-instructables.md)
