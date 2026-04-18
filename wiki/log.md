# Wiki log

Append-only chronological record. New entries go at the **bottom**. Heading format is validated by `scripts/validate_wiki.py`.

---

## [2026-04-17] policy | Initialize template wiki

- Seeded `wiki/` with example pages demonstrating taxonomy and linking.
- Established `raw/processed/2026/example-llm-wiki-note.md` as immutable demo source.
- Documented conventions in `AGENTS.md` and `docs/`.

---

## [2026-04-17] ingest | Example LLM Wiki note

- Filed demo raw source at `raw/processed/2026/example-llm-wiki-note.md`.
- Added source-note [`source-notes/example-llm-wiki-note.md`](source-notes/example-llm-wiki-note.md) and linked from [`concepts/llm-wiki-pattern.md`](concepts/llm-wiki-pattern.md).

---

## [2026-04-17] query | What is the LLM Wiki pattern?

- Answer captured in [`analyses/why-synthesis-layer.md`](analyses/why-synthesis-layer.md) with pointers to concepts and comparisons.

---

## [2026-04-17] lint | Template validation pass

- Ran `validate_wiki.py` with `--strict`; fixed index and link set for demo pages.
---

## [2026-04-17] ingest | LoRa/Meshtastic and smart agriculture inbox batch

- Moved six imports from `raw/inbox/` to stable paths under `raw/processed/2026/` (kebab-case filenames).
- Added six source-notes under `wiki/source-notes/` with `source_ids` pointing at the processed raw files.
- Added concepts [`concepts/meshtastic.md`](concepts/meshtastic.md) and [`concepts/lorawan.md`](concepts/lorawan.md) and topic hub [`topics/smart-agriculture-meshtastic-and-lorawan.md`](topics/smart-agriculture-meshtastic-and-lorawan.md); updated [`index.md`](index.md).
---

## [2026-04-17] ingest | Wi‑Fi HaLow, LoRa, PA, DePIN, and homestead inbox batch

- Moved twelve imports from `raw/inbox/` to `raw/processed/2026/` (kebab-case filenames), including a large full-text book capture and Wikipedia/article imports.
- Added twelve `source-notes/` entries with `source_ids`, plus concepts [`concepts/wi-fi-halow.md`](concepts/wi-fi-halow.md), [`concepts/lora-radio.md`](concepts/lora-radio.md), [`concepts/depin.md`](concepts/depin.md), [`concepts/precision-agriculture.md`](concepts/precision-agriculture.md); topic hubs [`topics/field-network-iot-comparisons.md`](topics/field-network-iot-comparisons.md) and [`topics/homestead-and-regional-gardening-sources.md`](topics/homestead-and-regional-gardening-sources.md).
- Updated [`concepts/lorawan.md`](concepts/lorawan.md), [`topics/smart-agriculture-meshtastic-and-lorawan.md`](topics/smart-agriculture-meshtastic-and-lorawan.md), and [`index.md`](index.md).
---

## [2026-04-17] ingest | ESP32, NTP/PTP, livestock PDFs, and homestead articles

- Moved eighteen imports from `raw/inbox/` to `raw/processed/2026/` (Markdown and two PDFs).
- Added concepts [`concepts/esp32.md`](concepts/esp32.md), [`concepts/network-time-protocol.md`](concepts/network-time-protocol.md), [`concepts/precision-time-protocol.md`](concepts/precision-time-protocol.md); topics [`topics/esp32-iot-smart-farming-and-tooling.md`](topics/esp32-iot-smart-farming-and-tooling.md), [`topics/time-synchronization-ntp-and-ptp.md`](topics/time-synchronization-ntp-and-ptp.md), [`topics/backyard-livestock-and-homestead-animals.md`](topics/backyard-livestock-and-homestead-animals.md); updated [`topics/homestead-and-regional-gardening-sources.md`](topics/homestead-and-regional-gardening-sources.md) and [`index.md`](index.md); eighteen new `source-notes/`.
---

## [2026-04-17] ingest | PNT alternatives, MagicMirror/e-ink, and GNSS time-server notes

- Moved thirteen Markdown imports from `raw/inbox/` to `raw/processed/2026/` (kebab-case filenames).
- Added thirteen `source-notes/` entries; new topics [`topics/position-navigation-and-timing-alternatives.md`](topics/position-navigation-and-timing-alternatives.md) and [`topics/smart-mirror-and-e-paper-displays.md`](topics/smart-mirror-and-e-paper-displays.md); expanded [`topics/time-synchronization-ntp-and-ptp.md`](topics/time-synchronization-ntp-and-ptp.md); updated [`index.md`](index.md).
---

## [2026-04-17] refactor | Cross-link pass for topic hubs and concepts

- Linked [`topics/field-network-iot-comparisons.md`](topics/field-network-iot-comparisons.md) and [`topics/smart-mirror-and-e-paper-displays.md`](topics/smart-mirror-and-e-paper-displays.md) to adjacent domain topics; expanded [`topics/knowledge-synthesis.md`](topics/knowledge-synthesis.md) with domain entry points.
- Connected [`topics/smart-agriculture-meshtastic-and-lorawan.md`](topics/smart-agriculture-meshtastic-and-lorawan.md) ↔ field network + ESP32 hubs; [`topics/esp32-iot-smart-farming-and-tooling.md`](topics/esp32-iot-smart-farming-and-tooling.md) → field network; clarified [`topics/time-synchronization-ntp-and-ptp.md`](topics/time-synchronization-ntp-and-ptp.md) vs PNT topic.
- Updated [`concepts/meshtastic.md`](concepts/meshtastic.md), [`concepts/lora-radio.md`](concepts/lora-radio.md), [`concepts/esp32.md`](concepts/esp32.md) Related sections and Meshtastic body cross-links.
---

## [2026-04-17] refactor | Concept summary objects and related_concepts frontmatter

- Added [`analyses/concept-relationships-overview.md`](analyses/concept-relationships-overview.md) with narrative clusters, summary table, and YAML `concept_summaries` for machine use.
- Added optional `related_concepts` lists to concept frontmatter (paths under `wiki/`) for domain concepts plus empty list for [`concepts/llm-wiki-pattern.md`](concepts/llm-wiki-pattern.md).
- Linked from [`topics/knowledge-synthesis.md`](topics/knowledge-synthesis.md) and [`index.md`](index.md).
---

## [2026-04-17] ingest | Agritourism, tiny housing, NIST ITS, and 360 PDF

- Moved six imports from `raw/inbox/` to `raw/processed/2026/` (five Markdown, one PDF `360.pdf`).
- Added topic [`topics/agritourism-tiny-housing-and-natural-building.md`](topics/agritourism-tiny-housing-and-natural-building.md) and six source-notes; linked NIST ITS note from [`concepts/network-time-protocol.md`](concepts/network-time-protocol.md) and [`topics/time-synchronization-ntp-and-ptp.md`](topics/time-synchronization-ntp-and-ptp.md); updated [`topics/homestead-and-regional-gardening-sources.md`](topics/homestead-and-regional-gardening-sources.md), [`topics/knowledge-synthesis.md`](topics/knowledge-synthesis.md), [`index.md`](index.md).

---

## [2026-04-17] ingest | Off-grid solar / storage and smart home (Matter, HA AI) batch

- Filed ten Markdown sources under `raw/processed/2026/` (solar sizing, homestead DIY, EcoFlow kits, field-study power, Matter/Thread, Home Assistant AI).
- Added ten `source-notes/` with `source_ids`; topic hubs [`topics/off-grid-solar-power-and-storage.md`](topics/off-grid-solar-power-and-storage.md) and [`topics/smart-home-matter-thread-and-home-assistant-ai.md`](topics/smart-home-matter-thread-and-home-assistant-ai.md).
- Cross-linked [`topics/esp32-iot-smart-farming-and-tooling.md`](topics/esp32-iot-smart-farming-and-tooling.md), [`topics/homestead-and-regional-gardening-sources.md`](topics/homestead-and-regional-gardening-sources.md), [`topics/smart-agriculture-meshtastic-and-lorawan.md`](topics/smart-agriculture-meshtastic-and-lorawan.md), [`topics/smart-mirror-and-e-paper-displays.md`](topics/smart-mirror-and-e-paper-displays.md), [`topics/knowledge-synthesis.md`](topics/knowledge-synthesis.md); updated [`index.md`](index.md).

---

## [2026-04-17] ingest | farmOS, ag lab, homelab, Docker/Kubernetes, Home Assistant installation

- Moved twenty-one Markdown imports from `raw/inbox/` to `raw/processed/2026/` (kebab-case filenames): farmOS + agriculture lab thread; homelab narratives (guides, wiki, AI architecture, Reddit threads, Alaska culvert, partial solar / EcoFlow); Docker Compose ×3, Docker Bake ×2, Kubernetes (overview, RKE2 vs K3s, when-to-use, short compare); Home Assistant “20 things” installation listicle.
- Added twenty-one `source-notes/` with `source_ids`; new topic hubs [`topics/farm-data-farmos-and-ag-lab-builds.md`](topics/farm-data-farmos-and-ag-lab-builds.md), [`topics/homelab-self-hosting-and-edge-narratives.md`](topics/homelab-self-hosting-and-edge-narratives.md), [`topics/docker-kubernetes-compose-and-bake.md`](topics/docker-kubernetes-compose-and-bake.md).
- Extended [`topics/smart-home-matter-thread-and-home-assistant-ai.md`](topics/smart-home-matter-thread-and-home-assistant-ai.md) with the HA installation source-note; cross-linked [`topics/off-grid-solar-power-and-storage.md`](topics/off-grid-solar-power-and-storage.md), [`topics/smart-agriculture-meshtastic-and-lorawan.md`](topics/smart-agriculture-meshtastic-and-lorawan.md), [`topics/esp32-iot-smart-farming-and-tooling.md`](topics/esp32-iot-smart-farming-and-tooling.md), [`topics/knowledge-synthesis.md`](topics/knowledge-synthesis.md); updated [`index.md`](index.md).

---

## [2026-04-17] ingest | LoRa, MQTT, and gateway bridges (MultiTech, OpenMQTTGateway, HiveMQ, HA, Instructables)

- Moved seven Markdown imports from `raw/inbox/` to `raw/processed/2026/` (MQTT/LoRa/LoRaWAN gateway and integration captures; note: former filename `Understanding MQTT.md` is **Meshtastic LoRa↔MQTT** Reddit content, stored as `meshtastic-lora-mqtt-bridge-reddit-thread.md`).
- Added seven `source-notes/` and topic hub [`topics/lora-mqtt-and-gateway-bridges.md`](topics/lora-mqtt-and-gateway-bridges.md); linked [`topics/backyard-livestock-and-homestead-animals.md`](topics/backyard-livestock-and-homestead-animals.md), [`topics/smart-agriculture-meshtastic-and-lorawan.md`](topics/smart-agriculture-meshtastic-and-lorawan.md), [`topics/knowledge-synthesis.md`](topics/knowledge-synthesis.md); updated [`index.md`](index.md).

---

## [2026-04-17] query | Track chickens with motion sensors over LoRa using MQTT

- Answer captured in [`analyses/tracking-chickens-motion-lora-mqtt.md`](analyses/tracking-chickens-motion-lora-mqtt.md) with pointers to [`topics/lora-mqtt-and-gateway-bridges.md`](topics/lora-mqtt-and-gateway-bridges.md) and raw sources under `raw/processed/2026/`.

---

## [2026-04-18] ingest | Tennessee business, hobby farm guides, USDA BFR, startup PDFs

- Moved seven Markdown imports and **two PDFs** from `raw/inbox/` to `raw/processed/2026/` (hobby farm articles, TN business formation guides, USDA beginning farmers page, TN Department of Revenue licensing excerpt; PDFs `newbusiness-checklist.pdf`, `tn-smart-startup-guide.pdf`).
- Added nine `source-notes/` and topic hub [`topics/tennessee-hobby-farm-and-small-farm-business-sources.md`](topics/tennessee-hobby-farm-and-small-farm-business-sources.md); updated [`topics/agritourism-tiny-housing-and-natural-building.md`](topics/agritourism-tiny-housing-and-natural-building.md), [`topics/homestead-and-regional-gardening-sources.md`](topics/homestead-and-regional-gardening-sources.md), [`topics/knowledge-synthesis.md`](topics/knowledge-synthesis.md), [`index.md`](index.md).

---

## [2026-04-18] query | Agritourism with tiny houses on a Tennessee hobby farm

- Answer captured in [`analyses/agritourism-tiny-houses-tennessee-hobby-farm.md`](analyses/agritourism-tiny-houses-tennessee-hobby-farm.md) with pointers to [`topics/tennessee-hobby-farm-and-small-farm-business-sources.md`](topics/tennessee-hobby-farm-and-small-farm-business-sources.md), [`topics/agritourism-tiny-housing-and-natural-building.md`](topics/agritourism-tiny-housing-and-natural-building.md), and cited `raw/processed/2026/` sources.

---

## [2026-04-18] query | Agrotourism smart hobby farm — tiny houses, rentals, guest farm work

- Answer captured in [`analyses/agritourism-smart-hobby-farm-tiny-houses-guest-work-stays.md`](analyses/agritourism-smart-hobby-farm-tiny-houses-guest-work-stays.md) with links to agritourism/hobby-farm sources and smart-farm topic hubs (`farmOS`, ESP32/HA, LoRa/MQTT); emphasizes labor/safety/legal sensitivity beyond raw excerpts.

---

## [2026-04-18] ingest | Ponds, water features, irrigation, crop rotation, farm entry

- Moved fifteen Markdown imports and one **PDF** from `raw/inbox/` to `raw/processed/2026/` (pond DIY + Acreage Life farm pond, waterfall forum fragment, water-feature history, uphill pumping articles, crop rotation + cover crops + SARE planning, sustainable ag essays, TN beginning-farmer link list, horse-at-home article).
- Added sixteen `source-notes/` and topic hubs [`topics/ponds-water-features-and-homestead-hydrology.md`](topics/ponds-water-features-and-homestead-hydrology.md), [`topics/sustainable-cropping-soil-and-farm-entry-sources.md`](topics/sustainable-cropping-soil-and-farm-entry-sources.md); updated [`topics/homestead-and-regional-gardening-sources.md`](topics/homestead-and-regional-gardening-sources.md), [`topics/knowledge-synthesis.md`](topics/knowledge-synthesis.md), [`index.md`](index.md).

---

## [2026-04-18] query | Start and stock a pond as a beautiful water feature

- Answer captured in [`analyses/starting-stocking-pond-beautiful-water-feature.md`](analyses/starting-stocking-pond-beautiful-water-feature.md) with pointers to [`topics/ponds-water-features-and-homestead-hydrology.md`](topics/ponds-water-features-and-homestead-hydrology.md) and cited `raw/processed/2026/` sources (Tyrant Farms biofilter build, Acreage Life stocking/regulatory framing).

---

## [2026-04-18] policy | MkDocs builds `wiki/` only; `raw/` not committed by default

- `mkdocs.yml` sets `docs_dir: wiki` and relaxes MkDocs link validation for `raw/` URLs not present in the site tree; GitHub Pages workflow still runs `mkdocs build --strict`.
- `.gitignore` keeps `raw/**` out of commits except `**/.gitkeep`; removed `raw/README.md` and the demo processed note from version control (files remain locally). Added `raw/processed/2026/.gitkeep` for directory layout.
- Updated [`docs/operations/publishing.md`](docs/operations/publishing.md) and [`README.md`](README.md) to describe the split: published wiki vs in-repo `docs/` handbook.

