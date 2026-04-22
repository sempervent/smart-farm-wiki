# Wiki log

Append-only chronological record. New entries go at the **bottom**. Heading format is validated by `scripts/validate_wiki.py`.

---

## [2026-04-19] policy | Raw validation + MkDocs: public CI without local corpus

- `scripts/validate_raw_pdf_links.py`: **default** treats missing local PDF/extract pairs and missing wiki `raw/` link targets as **warnings**; **`--strict`** fails when the full corpus is expected. `validate_wiki.py --raw-pdf-links` passes `strict` through the same way.
- `tests/test_validate_raw_pdf_links.py`: repo-wide check runs **without** `--strict`.
- `scripts/mkdocs_neutralize_raw_links.py` + `mkdocs.yml` **hooks**: rewrite `raw/` markdown links to non-navigable spans in the public HTML build; Obsidian sources unchanged. `wiki/stylesheets/raw-source-refs.css`.
- Docs: [`docs/operations/raw-corpus-and-publishing.md`](../docs/operations/raw-corpus-and-publishing.md), updates to [`validation.md`](../docs/operations/validation.md), [`publishing.md`](../docs/operations/publishing.md), [`ingest.md`](../docs/workflows/ingest.md), [`AGENTS.md`](../AGENTS.md), [`README.md`](../README.md).

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
- Updated [`docs/operations/publishing.md`](../../docs/operations/publishing.md) and [`README.md`](../../README.md) to describe the split: published wiki vs in-repo `docs/` handbook.

---

## [2026-04-17] query | Stocking and enterprise mix for 120 acres vs 5 acres (automation on larger farm)

- Research brief and copy-paste prompt in [`analyses/farm-stocking-120-acres-vs-5-acres-research-prompt.md`](analyses/farm-stocking-120-acres-vs-5-acres-research-prompt.md); links to livestock, cropping, precision ag, and farm-data topic hubs for follow-up ingests.

---

## [2026-04-17] lint | Wiki link targets from `log.md`

- Adjusted paths to [`docs/operations/publishing.md`](../../docs/operations/publishing.md) and [`README.md`](../../README.md) in [`log.md`](log.md) so `validate_wiki.py` resolves repo-root files from `wiki/`.

---

## [2026-04-18] refactor | Repository analysis wiki page

- Added [`analyses/repository-analysis.md`](analyses/repository-analysis.md) (layout, tooling, CI, corpus counts, risks); linked from [`index.md`](index.md) **Overview** and **Analyses** and from [`overview.md`](overview.md) step 4.

---

## [2026-04-18] query | Domain content strands (synthesis)

- Added [`analyses/domain-content-overview.md`](analyses/domain-content-overview.md) mapping land/water, regional business, LPWAN/mesh, edge compute, solar, home automation overlap, and time/PNT to topic hubs; linked from [`index.md`](index.md) **Overview** and **Analyses** and [`topics/knowledge-synthesis.md`](topics/knowledge-synthesis.md); [`overview.md`](overview.md) step 5. Adjusted counts in [`analyses/repository-analysis.md`](analyses/repository-analysis.md).

---

## [2026-04-18] query | Agritourism business plan — dual-site 5 ac and 120 ac (35 min apart)

- Business plan analysis in [`analyses/agritourism-dual-site-business-plan-five-and-120-acres.md`](analyses/agritourism-dual-site-business-plan-five-and-120-acres.md): site roles, realistic animal placement (small stock at hub; ruminants/batch poultry at large parcel), drive-time operations, revenue mix, risks; linked from [`index.md`](index.md). Updated corpus counts in [`analyses/repository-analysis.md`](analyses/repository-analysis.md).

---

## [2026-04-18] refactor | Agritourism plan — guest hub on farm, owners off-site

- Revised [`analyses/agritourism-dual-site-business-plan-five-and-120-acres.md`](analyses/agritourism-dual-site-business-plan-five-and-120-acres.md): **120 ac** = working farm + **guest lodging**; **5 ac** = **family residence** **35 min** away; all **business** animals and guest experiences on **120**; emphasis on **overnight coverage**, **caretaker/rotation**, **biosecurity** vs hobby animals at home; updated [`index.md`](index.md) blurb.

---

## [2026-04-18] policy | Mission and values in wiki; AGENTS pointer

- Added [`concepts/smart-farm-wiki-mission-and-values.md`](concepts/smart-farm-wiki-mission-and-values.md) (mission statement, vision, audience, authoring values, voice). Updated [`AGENTS.md`](../../AGENTS.md) **Mission** section: domain prose lives in wiki; reasoning; canonical link; handbook/MkDocs clarification; agent checklist points to mission page. Updated [`overview.md`](overview.md) and [`index.md`](index.md).

---

## [2026-04-18] query | Timing on the farm (synthesis)

- Added [`analyses/timing-on-the-farm-synthesis.md`](analyses/timing-on-the-farm-synthesis.md) (seasonal/rotation, labor, water & solar rhythms, NTP/PTP/PNT); linked from [`index.md`](index.md), [`analyses/domain-content-overview.md`](analyses/domain-content-overview.md), [`topics/time-synchronization-ntp-and-ptp.md`](topics/time-synchronization-ntp-and-ptp.md), [`topics/knowledge-synthesis.md`](topics/knowledge-synthesis.md). Set [`.gitignore`](../../.gitignore) to ignore **`.obsidian/`** entirely (replaces workspace-only rules). Updated [`analyses/repository-analysis.md`](analyses/repository-analysis.md) counts.

---

## [2026-04-18] policy | Validator: optional `raw/` citation targets; `raw/` dir only

- `scripts/validate_wiki.py` no longer requires `raw/README.md` or on-disk files for links under `raw/` (corpus may be absent in CI). Requires `raw/` directory. Helper `is_under_raw_dir` in `scripts/wiki_common.py`. Tests and [`docs/operations/validation.md`](../../docs/operations/validation.md) updated; [`analyses/repository-analysis.md`](analyses/repository-analysis.md) wording.

---

## [2026-04-18] query | Smart mirror with ESP32 and Raspberry Pi (build analysis)

- Added [`analyses/smart-mirror-esp32-and-raspberry-pi-build.md`](analyses/smart-mirror-esp32-and-raspberry-pi-build.md) (architecture, parts sourcing table, MagicMirror² docs + web references); linked from [`index.md`](index.md) and [`topics/smart-mirror-and-e-paper-displays.md`](topics/smart-mirror-and-e-paper-displays.md). Updated [`analyses/repository-analysis.md`](analyses/repository-analysis.md) counts.

---

## [2026-04-18] ingest | PDF → Markdown extraction script

- Added [`scripts/pdf_to_markdown.py`](../../scripts/pdf_to_markdown.py) (PyMuPDF): writes `*-extracted.md` next to each PDF under `raw/`; `--all-raw --force`. Dependency `pymupdf` in [`pyproject.toml`](../../pyproject.toml). Documented in [`docs/workflows/ingest.md`](../../docs/workflows/ingest.md), [`README.md`](../../README.md), [`AGENTS.md`](../../AGENTS.md). Ran conversion for local PDFs in `raw/processed/2026/` (extracts gitignored with `raw/**`). Tests in [`tests/test_pdf_to_markdown.py`](../../tests/test_pdf_to_markdown.py).

---

## [2026-04-18] query | Long 360 tractor no-start (web synthesis)

- Added [`analyses/long-360-tractor-no-start-synthesis.md`](analyses/long-360-tractor-no-start-synthesis.md): diesel troubleshooting (crank vs no-crank, battery/load, Thermostart, fuel bleed, forums); web reference list; linked from [`index.md`](index.md); updated [`analyses/repository-analysis.md`](analyses/repository-analysis.md) counts.

---

## [2026-04-18] ingest | Duck and chicken meat imports; comparison page

- Moved seven imports from `raw/inbox/` to `raw/processed/2026/` (ducks-for-meat Reddit, Bramblewood duck meat, chicken butchering ×2, Permies mental hurdle, chicken tractor forum, deep litter/tractor/pasture). Seven new `source-notes/`; comparison [`comparisons/ducks-vs-chickens-meat-raising.md`](comparisons/ducks-vs-chickens-meat-raising.md). Updated [`topics/backyard-livestock-and-homestead-animals.md`](topics/backyard-livestock-and-homestead-animals.md), [`index.md`](index.md), [`analyses/domain-content-overview.md`](analyses/domain-content-overview.md), [`analyses/repository-analysis.md`](analyses/repository-analysis.md).

---

## [2026-04-18] query | East Tennessee profitable crops matrix

- Added [`analyses/east-tennessee-profitable-crops-matrix.md`](analyses/east-tennessee-profitable-crops-matrix.md): enterprise-cluster matrix (row crops, forage, tobacco, vegetables, berries, cut flowers, CPA six-crop landscape, hemp caveat); cites UT AREC budgets, Vegetable Production hub, CPA/Farm Bureau article, USDA NASS TN overview; links vault pages on stocking research and TN/sustainable topics. Updated [`index.md`](index.md).

---

## [2026-04-18] query | Multi-field crop rotation plan

- Added [`analyses/multi-field-crop-rotation-plan.md`](analyses/multi-field-crop-rotation-plan.md): field roles (intensive veg, mechanized annuals, soil-building, perennials), crop-family spacing table, coordinated four-year tables for Fields A–C, perennial/alley management notes, annual checklist; links SARE-style source-notes and sustainable cropping topic. Updated [`index.md`](index.md).

---

## [2026-04-18] ingest | Irrigation and water-wise farming inbox batch

- Moved eight imports from `raw/inbox/` to `raw/processed/2026/` (solar irrigation, WPTO webinars, smart offline irrigation thread, DIY garden irrigation ×2, sustainable farming water-wise blog, sustainable irrigation methods, sustainable irrigation definition/methods systems). Eight new `source-notes/`; topic hub [`topics/irrigation-and-water-wise-farming-sources.md`](topics/irrigation-and-water-wise-farming-sources.md). Expanded [`analyses/multi-field-crop-rotation-plan.md`](analyses/multi-field-crop-rotation-plan.md) with **§1a acreage scenarios** (20 / 40 / 120 ac) and **§4 water-by-field** table tied to ingested sources; linked [`topics/ponds-water-features-and-homestead-hydrology.md`](topics/ponds-water-features-and-homestead-hydrology.md) and [`topics/sustainable-cropping-soil-and-farm-entry-sources.md`](topics/sustainable-cropping-soil-and-farm-entry-sources.md). Updated [`index.md`](index.md).

---

## [2026-04-18] ingest | Rural road erosion inbox batch; dirt road synthesis

- Moved three imports from `raw/inbox/` to `raw/processed/2026/` (steep road Reddit thread, SubStrata six tips, Corrosion Technologies soil stabilization). Three new `source-notes/`; topic [`topics/rural-road-and-driveway-erosion-sources.md`](topics/rural-road-and-driveway-erosion-sources.md); analysis [`analyses/dirt-road-erosion-shade-hill-curve.md`](analyses/dirt-road-erosion-shade-hill-curve.md) (shade + hill + curve scenario). Linked [`topics/ponds-water-features-and-homestead-hydrology.md`](topics/ponds-water-features-and-homestead-hydrology.md). Updated [`index.md`](index.md).

---

## [2026-04-19] ingest | Road erosion inbox batch five; 120-acre prevention summary

- Moved five imports from `raw/inbox/` to `raw/processed/2026/` (Lowe’s yard erosion, OffGridCabins steep road, Las Pilitas hillside, Desert Mtn dirt road stabilization, Backwoods Home maintain dirt road). Five new `source-notes/`; expanded [`topics/rural-road-and-driveway-erosion-sources.md`](topics/rural-road-and-driveway-erosion-sources.md). Added [`analyses/steep-curved-hill-dirt-road-erosion-prevention-120-acres.md`](analyses/steep-curved-hill-dirt-road-erosion-prevention-120-acres.md); cross-linked [`analyses/dirt-road-erosion-shade-hill-curve.md`](analyses/dirt-road-erosion-shade-hill-curve.md). Updated [`index.md`](index.md).

---

## [2026-04-19] ingest | Road engineering PDFs + extracts

- Moved six PDFs from `raw/inbox/` to `raw/processed/2026/` (management practices dirt roads, layman’s Appalachian guide, Penn State crown/cross-slope TB, USFS traveled way surface shape, low-volume roads BMP ch7, Kentucky EPSC protect slopes). Ran `pdf_to_markdown.py` → six `*-extracted.md` sidecars. Six new `source-notes/`; expanded [`analyses/steep-curved-hill-dirt-road-erosion-prevention-120-acres.md`](analyses/steep-curved-hill-dirt-road-erosion-prevention-120-acres.md) with **Agency and extension PDFs** table; updated [`analyses/dirt-road-erosion-shade-hill-curve.md`](analyses/dirt-road-erosion-shade-hill-curve.md) and [`topics/rural-road-and-driveway-erosion-sources.md`](topics/rural-road-and-driveway-erosion-sources.md). Updated [`index.md`](index.md). Force-added `raw/processed/2026/*.pdf` and `*-extracted.md` under `raw/` ignore so corpus is tracked in git for this commit.

---

## [2026-04-19] ingest | Workshop, 3D printing, basement, off-grid smart home batch

- Moved **21** imports from `raw/inbox/` to `raw/processed/2026/` (3D printing primers, shop/garage culture, basement workshop, off-grid + smart-home articles/forums). **21** new `source-notes/`; topic [`topics/home-workshop-3d-printing-basement-offgrid-smart-home-sources.md`](topics/home-workshop-3d-printing-basement-offgrid-smart-home-sources.md); analyses [`analyses/3d-printing-in-a-workshop-summary.md`](analyses/3d-printing-in-a-workshop-summary.md), [`analyses/basement-workshop-design-summary.md`](analyses/basement-workshop-design-summary.md), [`analyses/off-grid-smart-home-setups-summary.md`](analyses/off-grid-smart-home-setups-summary.md). Cross-linked [`topics/homelab-self-hosting-and-edge-narratives.md`](topics/homelab-self-hosting-and-edge-narratives.md), [`topics/off-grid-solar-power-and-storage.md`](topics/off-grid-solar-power-and-storage.md), [`topics/smart-home-matter-thread-and-home-assistant-ai.md`](topics/smart-home-matter-thread-and-home-assistant-ai.md), [`topics/knowledge-synthesis.md`](topics/knowledge-synthesis.md). Updated [`index.md`](index.md).

---

## [2026-04-19] lint | PDF ↔ extract and raw-link validation

- Added [`scripts/validate_raw_pdf_links.py`](../../scripts/validate_raw_pdf_links.py); wired optional [`--raw-pdf-links`](../../scripts/validate_wiki.py) into `validate_wiki.py` (missing raw targets follow `--strict`).
- Linked **Machine extract** lines on PDF source-notes that previously cited PDF only: [`source-notes/cover-crops-sustainable-crop-rotations-pdf.md`](source-notes/cover-crops-sustainable-crop-rotations-pdf.md), [`source-notes/tn-smart-startup-guide-pdf.md`](source-notes/tn-smart-startup-guide-pdf.md), [`source-notes/newbusiness-checklist-pdf.md`](source-notes/newbusiness-checklist-pdf.md), [`source-notes/360-publication-pdf.md`](source-notes/360-publication-pdf.md), [`source-notes/animals-journal-14-01645-pdf.md`](source-notes/animals-journal-14-01645-pdf.md), [`source-notes/ijraw-journal-pdf-4-5-50-1.md`](source-notes/ijraw-journal-pdf-4-5-50-1.md).
- Documented local/CI split in [`docs/workflows/ingest.md`](../../docs/workflows/ingest.md) and [`AGENTS.md`](../../AGENTS.md) scripts table.

---

## [2026-04-20] ingest | Composting for homesteading (six guides)

- Moved six imports from `raw/inbox/` to `raw/processed/2026/` (NRDC Composting 101, Wikipedia compost article, EPA composting at home, extension home/backyard intro, Earth Easy complete guide, ultimate food-waste reduction guide).
- Six new `source-notes/`; concept [`concepts/composting.md`](concepts/composting.md); topic [`topics/homestead-composting-and-soil-sources.md`](topics/homestead-composting-and-soil-sources.md); analysis [`analyses/homestead-composting-guide.md`](analyses/homestead-composting-guide.md). Cross-linked [`topics/homestead-and-regional-gardening-sources.md`](topics/homestead-and-regional-gardening-sources.md), [`topics/sustainable-cropping-soil-and-farm-entry-sources.md`](topics/sustainable-cropping-soil-and-farm-entry-sources.md); updated [`analyses/domain-content-overview.md`](analyses/domain-content-overview.md). Updated [`index.md`](index.md).

---

## [2026-04-20] query | Strategic audit — decision-safe two-site operations

- Captured ruthless **gap analysis** and prioritized **artifact backlog** (data, synthesis, SOPs, architecture) for making the vault **decision-safe** for **~5 ac homestead + ~120 ac farm + smart stack** in [`analyses/strategic-audit-decision-safe-operations.md`](analyses/strategic-audit-decision-safe-operations.md). Linked from [`analyses/domain-content-overview.md`](analyses/domain-content-overview.md), [`topics/knowledge-synthesis.md`](topics/knowledge-synthesis.md), [`index.md`](index.md).

---

## [2026-04-20] query | Implementation backlog (P0–P3) from strategic audit

- Added [`analyses/implementation-backlog-strategic-audit.md`](analyses/implementation-backlog-strategic-audit.md): **P0–P3** items with artifact type, rationale, **dependencies**, **S/M/L effort**, **foundational / integrative / optimization** orientation; split **missing knowledge vs synthesis vs operational structure**; **top 10** highest-leverage pages first. Linked from [`analyses/strategic-audit-decision-safe-operations.md`](analyses/strategic-audit-decision-safe-operations.md), [`topics/knowledge-synthesis.md`](topics/knowledge-synthesis.md), [`index.md`](index.md).

---

## [2026-04-20] ingest | Forage, precision soil/sensing, PostGIS, remote sensing review, org-design captures

- Moved **eight** imports from `raw/inbox/` to `raw/processed/2026/` (PostGIS workflow, Futurice AI-native ops, Kotter dual operating excerpt, MSU precision soil mapping, RSE remote sensing crop-mapping review, UNL CropWatch soil sensing, Grit forage feeding guide, **UT Beef & Forage Center** forage menu).
- Eight new `source-notes/`; cross-linked [`topics/sustainable-cropping-soil-and-farm-entry-sources.md`](topics/sustainable-cropping-soil-and-farm-entry-sources.md), [`topics/backyard-livestock-and-homestead-animals.md`](topics/backyard-livestock-and-homestead-animals.md), [`topics/farm-data-farmos-and-ag-lab-builds.md`](topics/farm-data-farmos-and-ag-lab-builds.md), [`topics/smart-agriculture-meshtastic-and-lorawan.md`](topics/smart-agriculture-meshtastic-and-lorawan.md), [`topics/field-network-iot-comparisons.md`](topics/field-network-iot-comparisons.md), [`topics/tennessee-hobby-farm-and-small-farm-business-sources.md`](topics/tennessee-hobby-farm-and-small-farm-business-sources.md), [`concepts/precision-agriculture.md`](concepts/precision-agriculture.md), [`analyses/farm-stocking-120-acres-vs-5-acres-research-prompt.md`](analyses/farm-stocking-120-acres-vs-5-acres-research-prompt.md), [`analyses/implementation-backlog-strategic-audit.md`](analyses/implementation-backlog-strategic-audit.md) (P1 #12 partial ingests). Updated [`analyses/domain-content-overview.md`](analyses/domain-content-overview.md), [`topics/knowledge-synthesis.md`](topics/knowledge-synthesis.md), [`index.md`](index.md).

---

## [2026-04-21] ingest | PostgreSQL / PostGIS captures and data storage concept

- Confirmed **four** processed raw files under `raw/processed/2026/` (PostgreSQL system-design chapter, Medium query-flow deep dive, enterprise PostGIS deep dive, GiST spatial index explainer).
- Added **four** `source-notes/` with `source_ids`; concept [`concepts/data-storage.md`](concepts/data-storage.md) with **official** links to [MQTT specification](https://mqtt.org/mqtt-specification/), [OASIS MQTT 5.0](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html), [PostgreSQL docs](https://www.postgresql.org/docs/current/), and [PostGIS documentation](https://postgis.net/documentation/).
- Cross-linked [`topics/farm-data-farmos-and-ag-lab-builds.md`](topics/farm-data-farmos-and-ag-lab-builds.md), [`topics/lora-mqtt-and-gateway-bridges.md`](topics/lora-mqtt-and-gateway-bridges.md), [`topics/knowledge-synthesis.md`](topics/knowledge-synthesis.md), [`source-notes/postgis-complete-workflow.md`](source-notes/postgis-complete-workflow.md); updated [`analyses/domain-content-overview.md`](analyses/domain-content-overview.md) (Strand D); updated [`index.md`](index.md).

---

## [2026-04-21] ingest | Inbox PDF batch (soil PA, PostGIS slides, forage)

- Moved **six** PDFs from `raw/inbox/` to `raw/processed/2026/` with kebab-case names; mislabeled `noaa_58706_DS1.pdf` renamed to [`raw/processed/2026/mdpi-agriculture-13091777-soil-ml-smart-farming.pdf`](../../raw/processed/2026/mdpi-agriculture-13091777-soil-ml-smart-farming.pdf) (content is MDPI *Agriculture* 2023 soil/ML article).
- Ran `scripts/pdf_to_markdown.py` for each PDF → sibling `*-extracted.md`.
- Six new `wiki/source-notes/*-pdf.md` (PDF + extract links); cross-linked [`topics/sustainable-cropping-soil-and-farm-entry-sources.md`](topics/sustainable-cropping-soil-and-farm-entry-sources.md), [`topics/backyard-livestock-and-homestead-animals.md`](topics/backyard-livestock-and-homestead-animals.md), [`topics/farm-data-farmos-and-ag-lab-builds.md`](topics/farm-data-farmos-and-ag-lab-builds.md), [`concepts/precision-agriculture.md`](concepts/precision-agriculture.md), [`concepts/data-storage.md`](concepts/data-storage.md); updated [`index.md`](index.md).

---

## [2026-04-21] policy | PDFs explicit in ingest contract

- [`AGENTS.md`](../../AGENTS.md): ingest workflow and definition-of-done now require **PDF** inbox drops to follow `docs/workflows/ingest.md` (stable path, **`pdf_to_markdown.py`** extract, source-note cites **PDF + `*-extracted.md`**); `raw/` layer table mentions PDFs.
- [`docs/workflows/ingest.md`](../../docs/workflows/ingest.md): step 1 states **PDFs** are first-class alongside markdown.

---

## [2026-04-21] ingest | Five priority operational drafts from strategic audit

- First-draft **`analyses/`** pages (placeholders, `status: draft`): [`dual-site-operations-model-non-agritourism.md`](analyses/dual-site-operations-model-non-agritourism.md), [`field-telemetry-reference-architecture-homestead-120ac.md`](analyses/field-telemetry-reference-architecture-homestead-120ac.md), [`farm-spatial-model-and-asset-registry-standard.md`](analyses/farm-spatial-model-and-asset-registry-standard.md), [`weekly-coverage-matrix-two-site-farm-operations.md`](analyses/weekly-coverage-matrix-two-site-farm-operations.md), [`automation-degraded-modes-manual-fallback-sop.md`](analyses/automation-degraded-modes-manual-fallback-sop.md). Linked from [`index.md`](index.md) and [`information-architecture-decision-safe-operations.md`](analyses/information-architecture-decision-safe-operations.md).

---

## [2026-04-21] policy | Staged agentic prompts for wiki improvement

- Added [`analyses/agentic-wiki-improvement-prompts-strategic-audit.md`](analyses/agentic-wiki-improvement-prompts-strategic-audit.md): **pre-prompt** (quality bar, non-goals, AGENTS-aligned writing standards) and **Phase 1–4** copy-paste prompts (foundational architecture → operational workflows → resilience/security → optimization/governance) with deliverables, acceptance criteria, constraints, and file lists; aligned to [`implementation-backlog-strategic-audit.md`](analyses/implementation-backlog-strategic-audit.md). Linked from [`index.md`](index.md), [`topics/knowledge-synthesis.md`](topics/knowledge-synthesis.md), [`analyses/strategic-audit-decision-safe-operations.md`](analyses/strategic-audit-decision-safe-operations.md); pointer in [`docs/index.md`](../../docs/index.md).

---

## [2026-04-21] query | Smart technology architecture audit

- Added [`analyses/smart-technology-architecture-audit.md`](analyses/smart-technology-architecture-audit.md): coverage vs gaps by layer (field telemetry through remote access), **fragmentation** analysis, **reference architecture** page outline, prioritized **SOPs** and **diagrams** checklist. Linked from [`index.md`](index.md), [`topics/knowledge-synthesis.md`](topics/knowledge-synthesis.md), [`analyses/strategic-audit-decision-safe-operations.md`](analyses/strategic-audit-decision-safe-operations.md), [`analyses/domain-content-overview.md`](analyses/domain-content-overview.md).

---

## [2026-04-21] query | Business viability and farm economics — gap analysis

- Added [`analyses/business-viability-and-farm-economics-gap-analysis.md`](analyses/business-viability-and-farm-economics-gap-analysis.md): dimension-by-dimension gap table (revenue, enterprise selection, market channels, staffing, insurance, accounting, CAPEX/OPEX, logistics, risk); prioritized **financial/business-planning** wiki pages; list of decisions **not** supportable from the repo alone; templates, calculators, comparisons. Linked from [`index.md`](index.md), [`topics/knowledge-synthesis.md`](topics/knowledge-synthesis.md), [`analyses/strategic-audit-decision-safe-operations.md`](analyses/strategic-audit-decision-safe-operations.md).

---

## [2026-04-21] query | Target information architecture for decision-safe operational brain

- Delivered [`analyses/information-architecture-decision-safe-operations.md`](analyses/information-architecture-decision-safe-operations.md): top-level logical layers, new topic hubs (two-site spine, telemetry, spatial, cybersecurity, civil systems), required analyses/comparisons/templates/SOPs/architecture docs/entities, cross-linking rules, orphan/integration gaps, phased migration plan; grounded in [`analyses/strategic-audit-decision-safe-operations.md`](analyses/strategic-audit-decision-safe-operations.md).
- Linked from [`overview.md`](overview.md), [`topics/knowledge-synthesis.md`](topics/knowledge-synthesis.md), [`analyses/domain-content-overview.md`](analyses/domain-content-overview.md), [`analyses/implementation-backlog-strategic-audit.md`](analyses/implementation-backlog-strategic-audit.md), [`analyses/strategic-audit-decision-safe-operations.md`](analyses/strategic-audit-decision-safe-operations.md), [`index.md`](index.md).

---

## [2026-04-17] ingest | Steering overview, four foundation pages, narrow PDF campaign, comparisons, runbooks

- **Raw**: Inbox PDFs and related captures moved under `raw/processed/2026/` (kebab-case); each PDF run through `scripts/pdf_to_markdown.py` → sibling `*-extracted.md`; **source-notes** with PDF + extract links and **Supports** pointers to the four foundation analyses (UT budgets/enterprise, NRCS conservation scenarios, farmOS model/API, CISA OT/remote access where filed).
- **Steering doc**: Rewrote [`analyses/domain-content-overview.md`](analyses/domain-content-overview.md) — strand map retained; added **future-state**, **maturity by strand**, **gaps**, **supported vs unsupported decisions**, **prioritized backlog**.
- **Foundation spine**: Active analyses for dual-site ops, field telemetry (homestead + 120 ac), farm spatial model + asset registry, **CAPEX/OPEX and enterprise sequencing — two-site constraint**; cross-links between strands.
- **Comparisons** (tradeoffs): [`lorawan-vs-meshtastic-fixed-farm-telemetry.md`](comparisons/lorawan-vs-meshtastic-fixed-farm-telemetry.md), [`farmos-vs-lightweight-stack-two-site-farm.md`](comparisons/farmos-vs-lightweight-stack-two-site-farm.md), [`own-equipment-vs-custom-hire-two-site-logistics.md`](comparisons/own-equipment-vs-custom-hire-two-site-logistics.md), [`fixed-gateway-tower-vs-mobile-vehicle-gateway.md`](comparisons/fixed-gateway-tower-vs-mobile-vehicle-gateway.md).
- **Runbooks** (after architecture): [`runbook-broker-or-backhaul-down.md`](analyses/runbook-broker-or-backhaul-down.md), [`runbook-power-loss-remote-site.md`](analyses/runbook-power-loss-remote-site.md), [`runbook-sensor-false-positive-alert-triage.md`](analyses/runbook-sensor-false-positive-alert-triage.md), [`runbook-manual-fallback-irrigation-gates-pumps.md`](analyses/runbook-manual-fallback-irrigation-gates-pumps.md); linked from [`automation-degraded-modes-manual-fallback-sop.md`](analyses/automation-degraded-modes-manual-fallback-sop.md).
- **Cross-links**: [`topics/knowledge-synthesis.md`](topics/knowledge-synthesis.md), [`analyses/information-architecture-decision-safe-operations.md`](analyses/information-architecture-decision-safe-operations.md), [`analyses/strategic-audit-decision-safe-operations.md`](analyses/strategic-audit-decision-safe-operations.md), [`source-notes/ut-publication-w1268-pdf.md`](source-notes/ut-publication-w1268-pdf.md), [`index.md`](index.md).
- **Validation**: `uv run python scripts/validate_wiki.py --strict` passes.

---

## [2026-04-17] query | East Tennessee two-site farm business plan — planning framework (skeleton)

- Added **hub** [`analyses/east-tennessee-two-site-farm-business-plan-framework.md`](analyses/east-tennessee-two-site-farm-business-plan-framework.md): page package, creation order, enterprise comparison steps (gates A–E), **weighted rubric** (0.45 / 0.35 / 0.20 profit / labor / resilience), knowns, unknowns, assumptions, pre-spend decisions.
- Added **11 skeleton** child analyses (vision, two-site context, enterprise options, labor/family, smart-tech, capital/financing, revenue tranches, risk register, 10-year roadmap, validation backlog, executive summary last); linked to existing dual-site / telemetry / CAPEX / comparisons.
- Updated [`index.md`](index.md), [`topics/knowledge-synthesis.md`](topics/knowledge-synthesis.md).

---

## [2026-04-17] query | Enterprise scenario analysis — 120 ac ET two-site

- Filled [`analyses/east-tennessee-two-site-farm-business-plan-enterprise-options-analysis.md`](analyses/east-tennessee-two-site-farm-business-plan-enterprise-options-analysis.md): per-path ops/labor/capital/automation/time/risk/infrastructure/skills/two-site fit; comparison table; **top 3** (phased mixed, commercial grazing, lease as stabilizer); **why others rank lower**; **phased strategy** Phase 0–3 + pivot triggers; explicit automation **helps vs burden**; canonical title *Enterprise options analysis — 120-acre East Tennessee two-site smart farm*.
- Updated [`index.md`](index.md) entry line.

---

## [2026-04-17] query | Phased ET two-site business plan package (11 pages + hub)

- **Filled** business plan analyses: [`vision`](analyses/east-tennessee-two-site-farm-business-plan-vision-and-constraints.md), [`two-site operating model`](analyses/east-tennessee-two-site-farm-business-plan-two-site-operating-context.md), [`recommended enterprise strategy`](analyses/east-tennessee-two-site-farm-business-plan-recommended-enterprise-strategy.md) (new), [`smart-tech`](analyses/east-tennessee-two-site-farm-business-plan-smart-tech-strategy.md), [`labor + weekly rhythm`](analyses/east-tennessee-two-site-farm-business-plan-labor-and-family-model.md), [`capital + infrastructure sequencing`](analyses/east-tennessee-two-site-farm-business-plan-capital-and-financing.md), [`revenue + milestones`](analyses/east-tennessee-two-site-farm-business-plan-revenue-and-phased-income.md), [`risk + mitigation`](analyses/east-tennessee-two-site-farm-business-plan-risk-register.md), [`10-year roadmap` Phases 0–4](analyses/east-tennessee-two-site-farm-business-plan-10-year-roadmap.md), [`validation backlog`](analyses/east-tennessee-two-site-farm-business-plan-validation-backlog.md), [`executive summary`](analyses/east-tennessee-two-site-farm-business-plan-executive-summary.md). Each page: **Known / Assumed / Open** sections.
- **Phases**: 0 no-regret groundwork → 1 land intelligence + pilot telemetry → 2 first grazing business → 3 scale/optimization → 4 salary-replacement architecture.
- Updated [`planning framework`](analyses/east-tennessee-two-site-farm-business-plan-framework.md) package table + status; [`index.md`](index.md); [`topics/knowledge-synthesis.md`](topics/knowledge-synthesis.md); cross-link from [`enterprise options analysis`](analyses/east-tennessee-two-site-farm-business-plan-enterprise-options-analysis.md) to recommended strategy.

---

## [2026-04-17] query | Operational artifacts for ET two-site business plan

- Added **eight** first-draft **operational** analyses: [`two-site-operations-model-5ac-homebase-120ac-production`](analyses/two-site-operations-model-5ac-homebase-120ac-production.md), [`family-labor-model-and-coverage-matrix-two-site-smart-farm`](analyses/family-labor-model-and-coverage-matrix-two-site-smart-farm.md), [`instrumentation-priority-matrix-two-site-smart-farm`](analyses/instrumentation-priority-matrix-two-site-smart-farm.md), [`capital-phasing-table-years-0-10-two-site-smart-farm`](analyses/capital-phasing-table-years-0-10-two-site-smart-farm.md), [`revenue-milestone-model-supplemental-to-salary-replacement`](analyses/revenue-milestone-model-supplemental-to-salary-replacement.md), [`business-risk-register-two-site-smart-farm`](analyses/business-risk-register-two-site-smart-farm.md), [`manual-fallback-degraded-modes-critical-operations`](analyses/manual-fallback-degraded-modes-critical-operations.md), [`validation-backlog-before-major-spend-two-site-smart-farm`](analyses/validation-backlog-before-major-spend-two-site-smart-farm.md). Each: purpose, **decisions supported**, fillable structure, **Known/assumed/open**, links to business-plan pages and runbooks.
- Updated [`east-tennessee-two-site-farm-business-plan-framework`](analyses/east-tennessee-two-site-farm-business-plan-framework.md), [`executive summary`](analyses/east-tennessee-two-site-farm-business-plan-executive-summary.md), [`index.md`](index.md), [`topics/knowledge-synthesis.md`](topics/knowledge-synthesis.md).

---

## [2026-04-18] query | Business plan wiki — Git-friendly execution sequence

- Added [`analyses/business-plan-wiki-git-execution-sequence.md`](analyses/business-plan-wiki-git-execution-sequence.md): **9** logical **PRs** (navigation → framework → narrative → artifacts → meta → financial layer → architecture → 24-mo validation → source/IA), **commit** order inside PRs, **landing** **order** (hub/index with dependents), **minimum** **usable** **state** milestone; linked from [`smart-farm-wiki-repository-implementation-plan`](analyses/smart-farm-wiki-repository-implementation-plan.md), [`east-tennessee-two-site-farm-business-plan-framework`](analyses/east-tennessee-two-site-farm-business-plan-framework.md), [`index.md`](index.md).

---

## [2026-04-18] query | Validation and pilot plan — first 24 months (two-site business plan)

- Added [`analyses/validation-and-pilot-plan-first-24-months-east-tennessee-two-site.md`](analyses/validation-and-pilot-plan-first-24-months-east-tennessee-two-site.md): **validation matrix** (assumption → test → cost band → time → success → unlock → V ID), **pilot** sections (land mapping, infra recon, business, telemetry, labor), **Phase** **1→2** / **2→3** **gates** **+** **scaling** **blockers**, **cheap** **proofs** list; **minimal** **spend** framing.
- Added [`analyses/pilot-and-recon-checklists-first-24-months-two-site-smart-farm.md`](analyses/pilot-and-recon-checklists-first-24-months-two-site-smart-farm.md) — linked **templates** (owner/date/done/evidence columns).
- Updated [`east-tennessee-two-site-farm-business-plan-validation-backlog.md`](analyses/east-tennessee-two-site-farm-business-plan-validation-backlog.md), [`east-tennessee-two-site-farm-business-plan-framework.md`](analyses/east-tennessee-two-site-farm-business-plan-framework.md), [`index.md`](index.md), [`topics/two-site-smart-farm-operations.md`](topics/two-site-smart-farm-operations.md).

---

## [2026-04-18] refactor | Smart-farm architecture package (two-site business plan)

- Added [`analyses/reference-architecture-5ac-homebase-120ac-smart-farm.md`](analyses/reference-architecture-5ac-homebase-120ac-smart-farm.md) — **package hub** (5 ac control center + 120 ac production, commute, scenarios, links).
- Added [`analyses/telemetry-system-of-record-boundaries-and-authority.md`](analyses/telemetry-system-of-record-boundaries-and-authority.md) — authority matrix: records, telemetry, dashboards, alerts, manual verification.
- Added [`analyses/automation-principles-two-site-smart-farm.md`](analyses/automation-principles-two-site-smart-farm.md) — automate early / late / never; distance and maintenance.
- Added [`analyses/remote-access-operational-security-model-two-site-smart-farm.md`](analyses/remote-access-operational-security-model-two-site-smart-farm.md) — trust zones, remote admin patterns, patching burden, physical risk.
- Expanded [`analyses/instrumentation-priority-matrix-two-site-smart-farm.md`](analyses/instrumentation-priority-matrix-two-site-smart-farm.md) — **first acres / first risks / first systems**; [`analyses/manual-fallback-degraded-modes-critical-operations.md`](analyses/manual-fallback-degraded-modes-critical-operations.md) — **scenario model** (travel, outage, sensor, comms, maintenance); [`analyses/farm-spatial-model-and-asset-registry-standard.md`](analyses/farm-spatial-model-and-asset-registry-standard.md) — architecture **minimum standard** subsection; [`analyses/field-telemetry-reference-architecture-homestead-120ac.md`](analyses/field-telemetry-reference-architecture-homestead-120ac.md) — SoR link + security cross-link.
- Updated [`east-tennessee-two-site-farm-business-plan-framework.md`](analyses/east-tennessee-two-site-farm-business-plan-framework.md), [`index.md`](index.md), [`topics/two-site-smart-farm-operations.md`](topics/two-site-smart-farm-operations.md).

---

## [2026-04-18] refactor | Financial planning layer scaffolding (two-site business plan)

- Added [`analyses/enterprise-unit-economics-worksheet-methodology-two-site-smart-farm.md`](analyses/enterprise-unit-economics-worksheet-methodology-two-site-smart-farm.md), [`analyses/farm-accounting-baseline-chart-of-accounts-enterprise-pl-two-site-smart-farm.md`](analyses/farm-accounting-baseline-chart-of-accounts-enterprise-pl-two-site-smart-farm.md), [`analyses/instrumentation-roi-model-two-site-smart-farm.md`](analyses/instrumentation-roi-model-two-site-smart-farm.md) — purpose/inputs/outputs/assumptions/placeholder tables; **no** fabricated budgets.
- Expanded [`analyses/capex-opex-enterprise-sequencing-two-site-constraint.md`](analyses/capex-opex-enterprise-sequencing-two-site-constraint.md), [`analyses/revenue-milestone-model-supplemental-to-salary-replacement.md`](analyses/revenue-milestone-model-supplemental-to-salary-replacement.md) — same scaffolding pattern; bridge-years table; scenario-aware milestones.
- Updated [`analyses/instrumentation-priority-matrix-two-site-smart-farm.md`](analyses/instrumentation-priority-matrix-two-site-smart-farm.md) — link to ROI model; [`east-tennessee-two-site-farm-business-plan-framework.md`](analyses/east-tennessee-two-site-farm-business-plan-framework.md) — **Financial planning layer** subsection; [`index.md`](index.md) — financial layer block; [`topics/two-site-smart-farm-operations.md`](topics/two-site-smart-farm-operations.md) — finance table rows.

---

## [2026-04-18] ingest | Business plan source-ingest campaign (meta)

- Added [`analyses/business-plan-source-ingest-campaign-east-tennessee-two-site.md`](analyses/business-plan-source-ingest-campaign-east-tennessee-two-site.md): **campaign goals** (G1–G7), **P0–P3** category priority, per-category **questions / wiki targets / prefer vs avoid**, **proposed source-note filenames** backlog, **routing rules** (raw vs `source_note` vs synthesis vs comparison vs defer). Linked from [`planning framework`](analyses/east-tennessee-two-site-farm-business-plan-framework.md), [`index.md`](index.md), [`knowledge-synthesis`](topics/knowledge-synthesis.md), [`two-site-smart-farm-operations`](topics/two-site-smart-farm-operations.md).

---

## [2026-04-17] query | Business plan remediation backlog (from hostile review)

- Added [`analyses/east-tennessee-two-site-farm-business-plan-remediation-backlog.md`](analyses/east-tennessee-two-site-farm-business-plan-remediation-backlog.md): **15-row** weakness→fix matrix (severity, repo fix, fix type), **revised** implementation priority, **do not finance** register, **P0/P1/P2** real-world checklist, **page revision** acceptance table, **decision controls**; linked from [`hostile internal review`](analyses/east-tennessee-two-site-farm-business-plan-hostile-internal-review.md), [`planning framework`](analyses/east-tennessee-two-site-farm-business-plan-framework.md), [`index.md`](index.md), [`knowledge-synthesis`](topics/knowledge-synthesis.md), [`two-site-smart-farm-operations`](topics/two-site-smart-farm-operations.md).

---

## [2026-04-17] query | Repository implementation plan — business plan integration

- Added [`analyses/smart-farm-wiki-repository-implementation-plan.md`](analyses/smart-farm-wiki-repository-implementation-plan.md): proposed **topic hub** (`topics/two-site-smart-farm-operations.md`), file tree (new vs update), page-by-page table, **minimum coherent merge** PR set, phased execution, **placeholders until evidence**; linked from [`index.md`](index.md).

---

## [2026-04-17] refactor | Business plan eight core pages — first-draft operational rewrite

- Rewrote for long-term wiki use (purpose, **decisions supported**, knowns, assumptions, open questions, **iterative updates**, relative links): [`two-site-operations-model-5ac-homebase-120ac-production`](analyses/two-site-operations-model-5ac-homebase-120ac-production.md), [`recommended-enterprise-strategy`](analyses/east-tennessee-two-site-farm-business-plan-recommended-enterprise-strategy.md), [`smart-tech-strategy`](analyses/east-tennessee-two-site-farm-business-plan-smart-tech-strategy.md), [`labor-and-family-model`](analyses/east-tennessee-two-site-farm-business-plan-labor-and-family-model.md), [`capital-and-financing`](analyses/east-tennessee-two-site-farm-business-plan-capital-and-financing.md), [`revenue-and-phased-income`](analyses/east-tennessee-two-site-farm-business-plan-revenue-and-phased-income.md), [`risk-register`](analyses/east-tennessee-two-site-farm-business-plan-risk-register.md), [`validation-backlog`](analyses/east-tennessee-two-site-farm-business-plan-validation-backlog.md). Updated [`index.md`](index.md), [`topics/two-site-smart-farm-operations.md`](topics/two-site-smart-farm-operations.md), [`executive-summary`](analyses/east-tennessee-two-site-farm-business-plan-executive-summary.md) link text; **risk** register adds R12–R13 (two-site delay, remote theft).

---

## [2026-04-17] refactor | Topic hub + overview wiring for two-site business plan

- Added [`topics/two-site-smart-farm-operations.md`](topics/two-site-smart-farm-operations.md) — navigation hub (business plan, artifacts, telemetry, resilience, finance, comparisons).
- Updated [`overview.md`](overview.md) (how-to-read bullet 7), [`index.md`](index.md) (Topics), [`knowledge-synthesis.md`](topics/knowledge-synthesis.md), [`east-tennessee-two-site-farm-business-plan-framework.md`](analyses/east-tennessee-two-site-farm-business-plan-framework.md) (topic hub link); [`smart-farm-wiki-repository-implementation-plan.md`](analyses/smart-farm-wiki-repository-implementation-plan.md) marks minimum-merge steps **done**.

---

## [2026-04-17] query | Hostile internal review — ET two-site business plan

- Added [`analyses/east-tennessee-two-site-farm-business-plan-hostile-internal-review.md`](analyses/east-tennessee-two-site-farm-business-plan-hostile-internal-review.md): executive critique, **15** weaknesses, prioritized **real-world** **validation** list, **pages to revise**, **revised** **implementation** **order**, **do not finance yet** items; linked from [`index.md`](index.md) and [`planning framework`](analyses/east-tennessee-two-site-farm-business-plan-framework.md).

---

## [2026-04-17] query | Time and smart sensors — two-site (120 ac → 5 ac)

- Captured synthesis in [`analyses/time-smart-sensors-120ac-to-5ac-homestead.md`](analyses/time-smart-sensors-120ac-to-5ac-homestead.md): operational time vs E2E latency, clock correlation, staleness/authority, sampling vs control-loop; links to existing two-site and telemetry pages.
- Updated [`index.md`](index.md) (Analyses); [`timing-on-the-farm-synthesis.md`](analyses/timing-on-the-farm-synthesis.md) (related entry).

---

## [2026-04-21] policy | AGENTS governance + structural audit (canonical routing)

- `AGENTS.md`: **public vs private** corpus and secrets, **canonicalization before proliferation**, **entity-first** for named products/orgs, **hub maintenance**, **claim strength and source authority**; session checklist and **lint** definition-of-done updated.
- Added [`analyses/structural-audit-repository-and-canonical-routing.md`](analyses/structural-audit-repository-and-canonical-routing.md) — strengths, structural risks, highest-value canonical extensions, merge vs routing policy.
- Entities: [`entities/farmos.md`](entities/farmos.md), [`entities/home-assistant.md`](entities/home-assistant.md); [`entities/example-org.md`](entities/example-org.md) links to those patterns.
- **Routing** (not merge): [`dual-site-operations-model-non-agritourism.md`](analyses/dual-site-operations-model-non-agritourism.md) ↔ [`two-site-operations-model-5ac-homebase-120ac-production.md`](analyses/two-site-operations-model-5ac-homebase-120ac-production.md).
- Fix: [`comparisons/farmos-vs-lightweight-stack-two-site-farm.md`](comparisons/farmos-vs-lightweight-stack-two-site-farm.md) → [`telemetry-system-of-record-boundaries-and-authority.md`](analyses/telemetry-system-of-record-boundaries-and-authority.md) (replacing mistaken backlog link).
- Hubs / index: [`overview.md`](overview.md), [`index.md`](index.md), [`domain-content-overview.md`](analyses/domain-content-overview.md), [`topics/two-site-smart-farm-operations.md`](topics/two-site-smart-farm-operations.md), [`topics/farm-data-farmos-and-ag-lab-builds.md`](topics/farm-data-farmos-and-ag-lab-builds.md), [`concepts/data-storage.md`](concepts/data-storage.md).

---

## [2026-04-21] refactor | Business plan + glossary + timelines as first-class lanes

- **`wiki/business-plan/`**: [`east-tennessee-two-site-farm-business-plan.md`](business-plan/east-tennessee-two-site-farm-business-plan.md) — package navigation spine (`page_type: topic`); `scripts/wiki_common.py` + `scripts/bootstrap.py` include `business-plan/`; `AGENTS.md` mission + taxonomy + index categories updated.
- **`wiki/index.md`**: new **Business plan** section (moved ET pages out of the **Analyses** block); **Entities** intro; **Timelines** + **Glossary** expanded with real pages; removed template `timelines/example-domain-timeline.md`.
- **Glossary**: [`glossary/smart-farm-wiki-glossary.md`](glossary/smart-farm-wiki-glossary.md) hub + [`two-site-sites`](glossary/two-site-sites.md), [`system-of-record-farm-data`](glossary/system-of-record-farm-data.md), [`validation-gate`](glossary/validation-gate.md), [`degraded-mode`](glossary/degraded-mode.md); [`synthesis-layer.md`](glossary/synthesis-layer.md) links hub.
- **Timeline**: [`timelines/east-tennessee-two-site-farm-business-plan-phase-timeline.md`](timelines/east-tennessee-two-site-farm-business-plan-phase-timeline.md) — Phases 0–4 bands.
- Wiring: [`overview.md`](overview.md), [`east-tennessee-two-site-farm-business-plan-framework.md`](analyses/east-tennessee-two-site-farm-business-plan-framework.md), [`topics/two-site-smart-farm-operations.md`](topics/two-site-smart-farm-operations.md), [`topics/knowledge-synthesis.md`](topics/knowledge-synthesis.md), [`analyses/structural-audit-repository-and-canonical-routing.md`](analyses/structural-audit-repository-and-canonical-routing.md).

---

## [2026-04-21] policy | Page ownership audit + entity layer (anti–analysis sprawl)

- Added [`analyses/structural-audit-page-ownership-entity-gaps-and-hub-routing.md`](analyses/structural-audit-page-ownership-entity-gaps-and-hub-routing.md): canonical **clusters** vs supporting analyses, overlap risks, hub weaknesses, entity backlog, agritourism vs ET routing.
- **`AGENTS.md`**: **Page ownership** section; **entity-first** expanded (sites, infrastructure systems); **agent checklist** points at ownership audit.
- **Entities** (planning roles, no fake deeds): [`five-acre-home-base-site-home-et-two-site.md`](entities/five-acre-home-base-site-home-et-two-site.md), [`120-acre-production-farm-site-farm-et-two-site.md`](entities/120-acre-production-farm-site-farm-et-two-site.md), [`farm-parcels-and-land-units.md`](entities/farm-parcels-and-land-units.md), [`farm-water-infrastructure-system.md`](entities/farm-water-infrastructure-system.md), [`farm-on-site-power-system.md`](entities/farm-on-site-power-system.md), [`field-telemetry-network-two-site.md`](entities/field-telemetry-network-two-site.md); [`example-org.md`](entities/example-org.md) updated.
- **Hubs / routing**: [`overview.md`](overview.md), [`index.md`](index.md), [`domain-content-overview.md`](analyses/domain-content-overview.md), [`topics/two-site-smart-farm-operations.md`](topics/two-site-smart-farm-operations.md) (**Canonical ownership** table), [`analyses/reference-architecture-5ac-homebase-120ac-smart-farm.md`](analyses/reference-architecture-5ac-homebase-120ac-smart-farm.md) (entity anchors), [`analyses/structural-audit-repository-and-canonical-routing.md`](analyses/structural-audit-repository-and-canonical-routing.md) (related link), [`glossary/two-site-sites.md`](glossary/two-site-sites.md), [`glossary/smart-farm-wiki-glossary.md`](glossary/smart-farm-wiki-glossary.md).

---

## [2026-04-21] refactor | Phase 1–2 execution thesis — recommended enterprise strategy

- Rewrote [`analyses/east-tennessee-two-site-farm-business-plan-recommended-enterprise-strategy.md`](analyses/east-tennessee-two-site-farm-business-plan-recommended-enterprise-strategy.md): **default** = **stocker/backgrounder-led beef** on grass; **single fallback** = **lease/custom/rent-heavy** minimal owned inventory; **deferred** theses table (cow-calf primary, small ruminants primary, specialty/orchard/agritourism/row primary); **decision boundaries** table (default alive / fallback / stop both) tied to **V1–V7** and **G1** + [`Vision` stop rules](analyses/east-tennessee-two-site-farm-business-plan-vision-and-constraints.md); **“not now”** section; operational **what Phase 1–2 becomes** language. No invented economics.

---

## [2026-04-21] refactor | Financial layer → execution gates (methodology to pass/fail)

- New [`analyses/execution-gates-financial-thresholds.md`](analyses/execution-gates-financial-thresholds.md): **Fin-G(0→1)** … **Fin-G(3→4)** consolidated criteria; links **M0–M4**, validation **G1–G3**, **FC*** family.
- Revised [`revenue-milestone-model-supplemental-to-salary-replacement.md`](analyses/revenue-milestone-model-supplemental-to-salary-replacement.md): inputs, **M*** formulas, threshold placeholders, **no-salary-claim**, bridge-year rules, gate crosswalk.
- Revised [`enterprise-unit-economics-worksheet-methodology-two-site-smart-farm.md`](analyses/enterprise-unit-economics-worksheet-methodology-two-site-smart-farm.md): **MVCM-1–3**, **SPLIT-1–2**, labor (`L_CHRG`, family shadow, **`H_TRIAGE`** caps).
- Revised [`capex-opex-enterprise-sequencing-two-site-constraint.md`](analyses/capex-opex-enterprise-sequencing-two-site-constraint.md): **FD-1–6** forbidden debt cases, **infrastructure unlock** matrix, **SS-1–5** spend-stops; aligns with [`Vision`](analyses/east-tennessee-two-site-farm-business-plan-vision-and-constraints.md) and [`Remediation` §3](analyses/east-tennessee-two-site-farm-business-plan-remediation-backlog.md).
- Navigation: [`index.md`](index.md) financial layer, [`business-plan/east-tennessee-two-site-farm-business-plan.md`](business-plan/east-tennessee-two-site-farm-business-plan.md), [`topics/two-site-smart-farm-operations.md`](topics/two-site-smart-farm-operations.md).

---

## [2026-04-21] refactor | 35-minute split — tighten operating pages + policy overlays

- [`two-site-operations-model-5ac-homebase-120ac-production.md`](analyses/two-site-operations-model-5ac-homebase-120ac-production.md): **Distance-tax rules** (**DT-0–DT-6**), **T0–T3** touch tiers, **`R_SPLIT`** / worksheet linkage; **no** softening of **`COMMUTE_ONE_WAY`**.
- [`east-tennessee-two-site-farm-business-plan-two-site-operating-context.md`](analyses/east-tennessee-two-site-farm-business-plan-two-site-operating-context.md): **Package** two-site chapter aligned to **distance tax**, **trip policy**, **disqualifiers**; phased behavior **0–4** tightened.
- [`east-tennessee-two-site-farm-business-plan-enterprise-options-analysis.md`](analyses/east-tennessee-two-site-farm-business-plan-enterprise-options-analysis.md): **Split-site penalty model** (**T0–T3**, **`R_SPLIT`**), **Split tax** column on comparison table (**1–5**, **1=highest** penalty).
- New [`trip-batching-and-site-visit-policy-two-site-smart-farm.md`](analyses/trip-batching-and-site-visit-policy-two-site-smart-farm.md): **J1–J4** justification, **batching** rules, **remote** observability priority, **failure** signals.
- New [`two-site-structure-disqualifiers-east-tennessee.md`](analyses/two-site-structure-disqualifiers-east-tennessee.md): **DQ-E**/**DQ-O**/**DQ-T** patterns + **remediation** table.
- Navigation: [`index.md`](index.md), [`business-plan/east-tennessee-two-site-farm-business-plan.md`](business-plan/east-tennessee-two-site-farm-business-plan.md) (reading order **2b–2c**), [`topics/two-site-smart-farm-operations.md`](topics/two-site-smart-farm-operations.md).

---

## [2026-04-21] refactor | Automation / telemetry → execution controls

- Revised [`east-tennessee-two-site-farm-business-plan-smart-tech-strategy.md`](analyses/east-tennessee-two-site-farm-business-plan-smart-tech-strategy.md): **AA-*** allowed early, **AF-*** forbidden early, **PA-*** proof before actuation, **maintenance burden** assumptions, **SO-*** security obligations; aggressive automation allowed only under scrutiny; **no** default labor reduction from instrumentation.
- Revised [`instrumentation-roi-model-two-site-smart-farm.md`](analyses/instrumentation-roi-model-two-site-smart-farm.md): **triage** fields (`H_TRIAGE_*`, `FP_RATE`), **false-positive cost** (`C_FP`, `FP_COST_YR`), **upkeep** (`H_PATCH_MO`, `UPKEEP_YR`, etc.), **DC-*** decommission criteria; net hours can be negative.
- New [`automation-stop-rules-two-site-smart-farm.md`](analyses/automation-stop-rules-two-site-smart-farm.md): **NS-*** no-scale, **MV-*** pre-rollout manual gates, **Phase 1** observational-only table.
- Navigation: [`index.md`](index.md), [`business-plan/east-tennessee-two-site-farm-business-plan.md`](business-plan/east-tennessee-two-site-farm-business-plan.md) (reading order **6b**), [`topics/two-site-smart-farm-operations.md`](topics/two-site-smart-farm-operations.md).

---

## [2026-04-21] refactor | Phase 0–1 execution dossier (first 24 months)

- New [`execution-dossier-hub-phase-0-1-east-tennessee.md`](analyses/execution-dossier-hub-phase-0-1-east-tennessee.md): **spine** — read order memo → 90d → checklist → 12m → 24m → validation plan detail.
- New [`execution-first-90-days-phase-0-1-east-tennessee.md`](analyses/execution-first-90-days-phase-0-1-east-tennessee.md), [`execution-first-12-months-phase-0-1-east-tennessee.md`](analyses/execution-first-12-months-phase-0-1-east-tennessee.md), [`execution-first-24-months-phase-0-1-east-tennessee.md`](analyses/execution-first-24-months-phase-0-1-east-tennessee.md): practical **T0-relative** windows; **pilot-grounded** only.
- New [`execution-dossier-master-checklist-phase-0-1-east-tennessee.md`](analyses/execution-dossier-master-checklist-phase-0-1-east-tennessee.md): consolidated **P0–P3** bands (land, infra, business, telemetry, labor).
- New [`execution-dossier-decision-memo-phase-0-1-east-tennessee.md`](analyses/execution-dossier-decision-memo-phase-0-1-east-tennessee.md): **approved now** / **pilot only** / **forbidden until gates**.
- Revised [`validation-and-pilot-plan-first-24-months-east-tennessee-two-site.md`](analyses/validation-and-pilot-plan-first-24-months-east-tennessee-two-site.md): **T0** anchor, calendar windows, quarter overlay, links to dossier; status **active**.
- Revised [`east-tennessee-two-site-farm-business-plan-validation-backlog.md`](analyses/east-tennessee-two-site-farm-business-plan-validation-backlog.md): **Next 90 days** tied to **T0** + dossier links; [`pilot-and-recon-checklists-first-24-months-two-site-smart-farm.md`](analyses/pilot-and-recon-checklists-first-24-months-two-site-smart-farm.md) banner.
- [`east-tennessee-two-site-farm-business-plan-framework.md`](analyses/east-tennessee-two-site-farm-business-plan-framework.md): execution dossier hub link in document tree.
- Navigation: [`index.md`](index.md), [`business-plan/east-tennessee-two-site-farm-business-plan.md`](business-plan/east-tennessee-two-site-farm-business-plan.md), [`topics/two-site-smart-farm-operations.md`](topics/two-site-smart-farm-operations.md).

---

## [2026-04-21] lint | Execution risk — second-pass illusions + ready-for-execution bar

- [`east-tennessee-two-site-farm-business-plan-hostile-internal-review.md`](analyses/east-tennessee-two-site-farm-business-plan-hostile-internal-review.md): **§7** second-pass **execution illusions** (12); **§8** canonical edit map.
- [`east-tennessee-two-site-farm-business-plan-remediation-backlog.md`](analyses/east-tennessee-two-site-farm-business-plan-remediation-backlog.md): **§2** replaced with **execution hardening** priority order; **§4** links **Ready for execution** checklist.
- [`execution-dossier-hub-phase-0-1-east-tennessee.md`](analyses/execution-dossier-hub-phase-0-1-east-tennessee.md): **Ready for execution** checklist (governance, labor, truth, tech, finance/insurance).
- Direct edits: [`vision`](analyses/east-tennessee-two-site-farm-business-plan-vision-and-constraints.md), [`executive summary`](analyses/east-tennessee-two-site-farm-business-plan-executive-summary.md), [`recommended enterprise strategy`](analyses/east-tennessee-two-site-farm-business-plan-recommended-enterprise-strategy.md), [`labor model`](analyses/east-tennessee-two-site-farm-business-plan-labor-and-family-model.md), [`execution-first-24-months…`](analyses/execution-first-24-months-phase-0-1-east-tennessee.md), [`pilot/recon checklists`](analyses/pilot-and-recon-checklists-first-24-months-two-site-smart-farm.md), [`execution decision memo`](analyses/execution-dossier-decision-memo-phase-0-1-east-tennessee.md); [`business-plan package`](business-plan/east-tennessee-two-site-farm-business-plan.md) **operational bar** line.

---

## [2026-04-17] ingest | raw/inbox batch — TN/UT/NASS/NRCS/FSA/farmOS + PDFs

- **Moved to** `raw/processed/2026/`: **9 new PDFs** (UT D32, NASS corn + all-crops cash rents TN 2024, TN Revenue ag exemption Jan 2023, NRCS E472A/E528R FY2025, UT Beef & Forage PB1663 calendar, TN PC498 agritourism act, Livestock Companion Apr 2025) with **`*-extracted.md`** via `scripts/pdf_to_markdown.py`. **Skipped** duplicate inbox PDFs identical to existing `ut-publication-d31/d252c/d252d.pdf`.
- **Web captures** (markdown) from inbox → `raw/processed/2026/*-inbox-2026-04-18.md` (FSA, farmOS docs, septic/SSDS, Web Soil Survey, 3D Elevation, TN GA bill info, USDA NASS page, Agricultural Exemption page). **`raw/inbox/` cleared** (PDFs + captures) after archival so strict PDF–extract pairing passes.
- **Source-notes** added under `wiki/source-notes/` (UT D32, NASS pair + survey page, TN exemption PDF + page, NRCS CEAP pair, PB1663, PC498, Livestock Companion, FSA batch, farmOS batch, septic batch, WSS/elevation, TN GA bill); [`index.md`](index.md) updated.
- Validator: `validate_wiki.py --strict` and `--raw-pdf-links` (strict).

---

## [2026-04-22] query | Claxton/Demory missing-data register

- New [`claxton-and-demory-missing-data-register.md`](analyses/claxton-and-demory-missing-data-register.md): eight sections (land, buildability/utilities, soils/hydro, access/roads, market/rent, infra recon, desktop vs field); each gap table includes **site** (C/D/Both), **why**, **resolve**, **blocks/informs**; links package, site intelligence, validation plan. [`index.md`](index.md) (business plan + analyses).

---

## [2026-04-22] refactor | Business plan tightened to Claxton/Anderson + Demory/Campbell evidence

- **Package hub** [`east-tennessee-two-site-farm-business-plan.md`](business-plan/east-tennessee-two-site-farm-business-plan.md): one-line pointer to **which** chapters **fold** site intelligence (no new pages).
- **Execution dossier hub** [`execution-dossier-hub-phase-0-1-east-tennessee.md`](analyses/execution-dossier-hub-phase-0-1-east-tennessee.md): Related links to Claxton/Demory intelligence.
- **Two-site operating model** [`two-site-operations-model-5ac-homebase-120ac-production.md`](analyses/two-site-operations-model-5ac-homebase-120ac-production.md): named anchors, NASS rent refs, **Campbell** terrain → batching / CAPEX emphasis; **what changed** note.
- **Recommended enterprise strategy** [`east-tennessee-two-site-farm-business-plan-recommended-enterprise-strategy.md`](analyses/east-tennessee-two-site-farm-business-plan-recommended-enterprise-strategy.md): local evidence paragraph tying default thesis to **WSS** + **NASS**.
- **Capital plan** [`east-tennessee-two-site-farm-business-plan-capital-and-financing.md`](analyses/east-tennessee-two-site-farm-business-plan-capital-and-financing.md): **Campbell** earthwork/lane peer sequencing; **Anderson** homestead verify before broker scale.
- **Revenue model** [`east-tennessee-two-site-farm-business-plan-revenue-and-phased-income.md`](analyses/east-tennessee-two-site-farm-business-plan-revenue-and-phased-income.md): lease row + **2024 NASS** county numbers + caveats.
- **Risk register** [`east-tennessee-two-site-farm-business-plan-risk-register.md`](analyses/east-tennessee-two-site-farm-business-plan-risk-register.md): **R14** terrain/sediment, **R15** AOI mismatch.
- **Validation / pilot plan** [`validation-and-pilot-plan-first-24-months-east-tennessee-two-site.md`](analyses/validation-and-pilot-plan-first-24-months-east-tennessee-two-site.md): **V1**/**V7** county anchors.
- **Execution dossier slices** [`execution-first-90-days-phase-0-1-east-tennessee.md`](analyses/execution-first-90-days-phase-0-1-east-tennessee.md), [`execution-first-12-months-phase-0-1-east-tennessee.md`](analyses/execution-first-12-months-phase-0-1-east-tennessee.md), [`execution-first-24-months-phase-0-1-east-tennessee.md`](analyses/execution-first-24-months-phase-0-1-east-tennessee.md): local evidence bullets.
- **Spatial model** [`farm-spatial-model-and-asset-registry-standard.md`](analyses/farm-spatial-model-and-asset-registry-standard.md): **Campbell** AOI acreage vs **~120 ac** assumption row.
- **Labor** [`east-tennessee-two-site-farm-business-plan-labor-and-family-model.md`](analyses/east-tennessee-two-site-farm-business-plan-labor-and-family-model.md), **Smart tech** [`east-tennessee-two-site-farm-business-plan-smart-tech-strategy.md`](analyses/east-tennessee-two-site-farm-business-plan-smart-tech-strategy.md): surge + telemetry placement vs terrain.

---

## [2026-04-22] ingest | Campbell WSS AOI capture + Claxton/Demory site intelligence

- **Raw**: [`web-soil-survey-campbell-county-aoi-soil-map-tab-capture-2026-04-18.md`](../raw/processed/2026/web-soil-survey-campbell-county-aoi-soil-map-tab-capture-2026-04-18.md) (moved from `raw/inbox/` Web Soil Survey capture); **source-note** [`campbell-county-wss-aoi-soil-map-tab-capture-2026-04-18.md`](source-notes/campbell-county-wss-aoi-soil-map-tab-capture-2026-04-18.md).
- **Analyses**: [`claxton-home-base-site-intelligence.md`](analyses/claxton-home-base-site-intelligence.md) (Anderson / `SITE_HOME`), [`demory-farm-site-intelligence.md`](analyses/demory-farm-site-intelligence.md) (Campbell / `SITE_FARM`); **comparison** [`anderson-county-vs-campbell-county-operating-implications.md`](comparisons/anderson-county-vs-campbell-county-operating-implications.md). NASS 2024 county cash rent figures cited from [`nass-cash-rents-all-crops-tn-2024.pdf`](../raw/processed/2026/nass-cash-rents-all-crops-tn-2024.pdf).
- **Entities** [`five-acre-home-base-site-home-et-two-site.md`](entities/five-acre-home-base-site-home-et-two-site.md), [`120-acre-production-farm-site-farm-et-two-site.md`](entities/120-acre-production-farm-site-farm-et-two-site.md); package hub, [`authoritative-execution-evidence-cluster-east-tennessee.md`](source-notes/authoritative-execution-evidence-cluster-east-tennessee.md), [`index.md`](index.md), [`two-site-smart-farm-operations.md`](topics/two-site-smart-farm-operations.md).

---

## [2026-04-22] refactor | Execution readiness — gap audit, authority vocabulary, hub routing

- New [`execution-readiness-gap-audit-east-tennessee-operational-knowledge.md`](analyses/execution-readiness-gap-audit-east-tennessee-operational-knowledge.md): missing **site-specific** execution data, mixed-authority clusters, thin glossary/timeline/onboarding, **canonical update** list (no invented parcel facts).
- New [`evidence-grade-and-canonical-authority.md`](concepts/evidence-grade-and-canonical-authority.md), [`evidence-grade.md`](glossary/evidence-grade.md); source index [`authoritative-execution-evidence-cluster-east-tennessee.md`](source-notes/authoritative-execution-evidence-cluster-east-tennessee.md) (links existing ingests: soils, NASS, DOR, FSA, septic, farmOS, CISA).
- **Canonical updates**: [`east-tennessee-two-site-farm-business-plan.md`](business-plan/east-tennessee-two-site-farm-business-plan.md) (authority block), [`east-tennessee-two-site-farm-business-plan-framework.md`](analyses/east-tennessee-two-site-farm-business-plan-framework.md), [`east-tennessee-two-site-farm-business-plan-capital-and-financing.md`](analyses/east-tennessee-two-site-farm-business-plan-capital-and-financing.md) (FSA reference table), [`farm-spatial-model-and-asset-registry-standard.md`](analyses/farm-spatial-model-and-asset-registry-standard.md), [`execution-dossier-hub-phase-0-1-east-tennessee.md`](analyses/execution-dossier-hub-phase-0-1-east-tennessee.md), [`domain-content-overview.md`](analyses/domain-content-overview.md); entities [`farm-parcels-and-land-units.md`](entities/farm-parcels-and-land-units.md), [`farmos.md`](entities/farmos.md); topic [`two-site-smart-farm-operations.md`](topics/two-site-smart-farm-operations.md) (**Regulatory & site evidence** row); timeline [`east-tennessee-two-site-farm-business-plan-phase-timeline.md`](timelines/east-tennessee-two-site-farm-business-plan-phase-timeline.md); [`overview.md`](overview.md), [`smart-farm-wiki-glossary.md`](glossary/smart-farm-wiki-glossary.md), [`index.md`](index.md).

---

## [2026-04-23] refactor | Local site and county intelligence hub + navigation

- New topic hub [`local-site-and-county-intelligence.md`](topics/local-site-and-county-intelligence.md): routes business plan readers to **county** context (comparison + evidence cluster), **Claxton** / **Demory** site intelligence, **validation plan**, **missing-data register**, and distinguishes county vs site vs execution analyses vs unresolved gaps.
- [`overview.md`](overview.md) (how to read item 7): pointer to hub for Anderson/Campbell + Claxton/Demory routing alongside two-site operations.
- [`domain-content-overview.md`](analyses/domain-content-overview.md): short **Local site + county layer** pointer after canonical ownership.
- [`index.md`](index.md): Topics catalog entry for local site and county intelligence.
- Validator: `validate_wiki.py --strict`.


---

## [2026-04-23] refactor | Place + county entities (Claxton, Demory, Anderson, Campbell)

- New **place** entities: [`claxton-home-base.md`](entities/claxton-home-base.md), [`demory-farm-site.md`](entities/demory-farm-site.md) — role vs deed, known facts, assumptions, analyses, source-notes, decisions, unknowns; link [`farm water`](entities/farm-water-infrastructure-system.md) / [`on-site power`](entities/farm-on-site-power-system.md) / [`telemetry`](entities/field-telemetry-network-two-site.md) as patterns (no new utility-class pages).
- New **county context** entities: [`anderson-county-tennessee.md`](entities/anderson-county-tennessee.md), [`campbell-county-tennessee.md`](entities/campbell-county-tennessee.md) — NASS rows + qualitative geography; Campbell ties WSS capture discipline to Demory thread.
- **Role entities** [`five-acre-home-base-site-home-et-two-site.md`](entities/five-acre-home-base-site-home-et-two-site.md), [`120-acre-production-farm-site-farm-et-two-site.md`](entities/120-acre-production-farm-site-farm-et-two-site.md): place + county anchors + router hub link; [`farm-parcels-and-land-units.md`](entities/farm-parcels-and-land-units.md) lists named places and counties.
- **Analyses** [`claxton-home-base-site-intelligence.md`](analyses/claxton-home-base-site-intelligence.md), [`demory-farm-site-intelligence.md`](analyses/demory-farm-site-intelligence.md): role / place / county entity lines in header block.
- **Hubs / nav**: [`local-site-and-county-intelligence.md`](topics/local-site-and-county-intelligence.md), [`two-site-smart-farm-operations.md`](topics/two-site-smart-farm-operations.md), [`domain-content-overview.md`](analyses/domain-content-overview.md), [`anderson-county-vs-campbell-county-operating-implications.md`](comparisons/anderson-county-vs-campbell-county-operating-implications.md), [`two-site-sites.md`](glossary/two-site-sites.md), [`index.md`](index.md).
- Validator: `validate_wiki.py --strict`.


---

## [2026-04-23] query | Ingest visibility — IA diagnosis + hub wiring

- New [`ingest-visibility-gap-authoritative-evidence-east-tennessee.md`](analyses/ingest-visibility-gap-authoritative-evidence-east-tennessee.md): **diagnosis** (raw vs source-notes vs synthesis vs MkDocs `raw/` neutralization vs dual entry points); **remediation** table; **smallest fix** list.
- **Canonical wiring**: [`authoritative-execution-evidence-cluster-east-tennessee.md`](source-notes/authoritative-execution-evidence-cluster-east-tennessee.md) (“after ingest” spine), [`east-tennessee-two-site-farm-business-plan.md`](business-plan/east-tennessee-two-site-farm-business-plan.md) (site intelligence + **local router**), [`local-site-and-county-intelligence.md`](topics/local-site-and-county-intelligence.md) (pair with agency cluster), [`overview.md`](overview.md) item 10 split **agency** vs **named-place** routing, [`index.md`](index.md) (business-plan block + analyses line).
- Validator: `validate_wiki.py --strict`.


---

## [2026-04-23] ingest | WSS home capture + parcel intelligence worksheets (Claxton / Demory)

- **Raw** (already under `raw/processed/2026/`): [`web-soil-survey-home-inbox-2026-04-18.md`](../raw/processed/2026/web-soil-survey-home-inbox-2026-04-18.md) — WSS product home / process reference (not parcel soils).
- **Source-note**: [`web-soil-survey-home-page-inbox-2026-04-18.md`](source-notes/web-soil-survey-home-page-inbox-2026-04-18.md); **evidence cluster** [`authoritative-execution-evidence-cluster-east-tennessee.md`](source-notes/authoritative-execution-evidence-cluster-east-tennessee.md) updated (WSS home row + parcel package pointer).
- **Parcel intelligence package**: topic hub [`parcel-intelligence-package-east-tennessee-two-site.md`](topics/parcel-intelligence-package-east-tennessee-two-site.md); blank worksheet [`parcel-intelligence-worksheet-template.md`](topics/parcel-intelligence-worksheet-template.md); repo scaffold [`templates/parcel-intelligence-sheet.md`](../templates/parcel-intelligence-sheet.md).
- **Worksheets**: [`parcel-intelligence-claxton-home-base-east-tennessee-two-site.md`](analyses/parcel-intelligence-claxton-home-base-east-tennessee-two-site.md) (placeholders; no homestead WSS AOI in vault), [`parcel-intelligence-demory-farm-site-east-tennessee-two-site.md`](analyses/parcel-intelligence-demory-farm-site-east-tennessee-two-site.md) (Campbell WSS table from existing capture; AOI vs ~120 ac explicit).
- **Wiring**: [`campbell-county-wss-aoi-soil-map-tab-capture-2026-04-18.md`](source-notes/campbell-county-wss-aoi-soil-map-tab-capture-2026-04-18.md), [`east-tennessee-two-site-farm-business-plan.md`](business-plan/east-tennessee-two-site-farm-business-plan.md), [`local-site-and-county-intelligence.md`](topics/local-site-and-county-intelligence.md), site intelligence analyses, place entities, [`farm-parcels-and-land-units.md`](entities/farm-parcels-and-land-units.md), [`index.md`](index.md).
- Validator: `validate_wiki.py --strict`.


---

## [2026-04-23] ingest | Electrical / networking / Starlink PDFs + captures; Mermaid topology analysis

- **Raw**: moved **10 PDFs** from `raw/inbox/` → `raw/processed/2026/` (Victron *Wiring Unlimited*, NREL off-grid modules 5–6, Morse Micro MM6108/MM8108, UT PB1752 + SP434A, Starlink Mini + Standard 4× kit specs, technical information EN); **`pdf_to_markdown.py`** `*-extracted.md` for each.
- **Web captures**: **33** Markdown files from `raw/inbox/` → `raw/processed/2026/*-inbox-2026-04-23.md` (Victron wiring series, Starlink/Meshtastic/HaLow/OpenWrt articles, etc.); inbox **cleared** for PDFs + MD.
- **Source-note**: [`electrical-networking-starlink-inbox-batch-2026-04-23.md`](source-notes/electrical-networking-starlink-inbox-batch-2026-04-23.md); **evidence cluster** updated (DC/Starlink batch + topology link).
- **Analysis**: [`two-site-smart-farm-network-topology-and-wan-edge-reference.md`](analyses/two-site-smart-farm-network-topology-and-wan-edge-reference.md) — **Mermaid** diagrams (WAN/sites, telemetry data plane, DC bus pattern, HaLow vs mesh overlay).
- **MkDocs**: `mkdocs-mermaid2-plugin` + `mermaid2.version` in [`mkdocs.yml`](../../mkdocs.yml); **docs** [`publishing.md`](../../docs/operations/publishing.md).
- **Navigation**: [`index.md`](index.md), [`reference-architecture-5ac-homebase-120ac-smart-farm.md`](analyses/reference-architecture-5ac-homebase-120ac-smart-farm.md).
- Validator: `validate_wiki.py --strict`; `mkdocs build --strict`.


---

## [2026-04-24] refactor | Starlink / LEO WAN — canonical integration (two-site ops, not standalone topology)

- **Intent**: Fold **Starlink / satellite WAN posture** into the **owning** analyses so it is operationally actionable; keep [`two-site-smart-farm-network-topology-and-wan-edge-reference.md`](analyses/two-site-smart-farm-network-topology-and-wan-edge-reference.md) as **diagram + detail** without duplicating its prose elsewhere.
- **Updated** (per-site **primary / backup / conditional / deferred**, enables vs **must-not** silent dependencies, validation/capital hooks): [`two-site-operations-model-5ac-homebase-120ac-production.md`](analyses/two-site-operations-model-5ac-homebase-120ac-production.md), [`east-tennessee-two-site-farm-business-plan-smart-tech-strategy.md`](analyses/east-tennessee-two-site-farm-business-plan-smart-tech-strategy.md), [`reference-architecture-5ac-homebase-120ac-smart-farm.md`](analyses/reference-architecture-5ac-homebase-120ac-smart-farm.md), [`remote-access-operational-security-model-two-site-smart-farm.md`](analyses/remote-access-operational-security-model-two-site-smart-farm.md), [`manual-fallback-degraded-modes-critical-operations.md`](analyses/manual-fallback-degraded-modes-critical-operations.md), [`automation-degraded-modes-manual-fallback-sop.md`](analyses/automation-degraded-modes-manual-fallback-sop.md), [`validation-and-pilot-plan-first-24-months-east-tennessee-two-site.md`](analyses/validation-and-pilot-plan-first-24-months-east-tennessee-two-site.md), [`east-tennessee-two-site-farm-business-plan-capital-and-financing.md`](analyses/east-tennessee-two-site-farm-business-plan-capital-and-financing.md).
- **Hub / nav**: [`index.md`](index.md) (topology line → **canonical integration** link set), [`two-site-smart-farm-operations.md`](topics/two-site-smart-farm-operations.md) (Telemetry + SoR row: topology + ops/strategy ownership).
- **Sources**: batch hub [`electrical-networking-starlink-inbox-batch-2026-04-23.md`](source-notes/electrical-networking-starlink-inbox-batch-2026-04-23.md).
- Validator: `validate_wiki.py --strict`.


---

## [2026-04-24] query | Canonical connectivity strategy — Claxton & Demory (two-site WAN)

- New [`connectivity-strategy-for-claxton-and-demory.md`](analyses/connectivity-strategy-for-claxton-and-demory.md): **Starlink/LTE/terrestrial** roles per **`SITE_HOME`** / **`SITE_FARM`**, local vs WAN-dependent systems, power/cost/security, WAN-required vs **WAN-loss-tolerant** farm functions, **pilot vs scale** expectations; links **topology** Starlink analysis, **reference architecture**, **degraded-mode** runbooks, **business plan** execution spine.
- [`index.md`](index.md) (business-plan block + analyses), [`east-tennessee-two-site-farm-business-plan.md`](business-plan/east-tennessee-two-site-farm-business-plan.md) (operational artifacts), [`two-site-smart-farm-operations.md`](topics/two-site-smart-farm-operations.md) (Telemetry + SoR row), [`reference-architecture-5ac-homebase-120ac-smart-farm.md`](analyses/reference-architecture-5ac-homebase-120ac-smart-farm.md) (business-plan links line).
- Validator: `validate_wiki.py --strict`.


---

## [2026-04-24] refactor | Execution topology package — reference, pilot, degraded Mermaid

- New [`execution-topology-package-two-site-smart-farm.md`](analyses/execution-topology-package-two-site-smart-farm.md): **three** **execution-safe** diagrams (**full reference**, **Phase 0/1 pilot**, **WAN-out degraded**) with **legend** (Z1/Z2/Z3, WAN-dependent vs **local-only survivable**), interpretation under each, links to [`reference-architecture-5ac-homebase-120ac-smart-farm.md`](analyses/reference-architecture-5ac-homebase-120ac-smart-farm.md), [`connectivity-strategy-for-claxton-and-demory.md`](analyses/connectivity-strategy-for-claxton-and-demory.md), degraded pages, **runbooks** (`runbook-broker-or-backhaul-down`, `runbook-power-loss-remote-site`), [`remote-access-operational-security-model-two-site-smart-farm.md`](analyses/remote-access-operational-security-model-two-site-smart-farm.md). **Mermaid** already enabled in [`mkdocs.yml`](../../mkdocs.yml).
- Wired: [`two-site-smart-farm-network-topology-and-wan-edge-reference.md`](analyses/two-site-smart-farm-network-topology-and-wan-edge-reference.md) (pointer to execution package), [`connectivity-strategy-for-claxton-and-demory.md`](analyses/connectivity-strategy-for-claxton-and-demory.md), [`reference-architecture-5ac-homebase-120ac-smart-farm.md`](analyses/reference-architecture-5ac-homebase-120ac-smart-farm.md) (package map row 1), [`index.md`](index.md), [`two-site-smart-farm-operations.md`](topics/two-site-smart-farm-operations.md), [`east-tennessee-two-site-farm-business-plan.md`](business-plan/east-tennessee-two-site-farm-business-plan.md).
- Validator: `validate_wiki.py --strict`; `mkdocs build --strict`.


---

## [2026-04-24] refactor | Connectivity validation in first-24-months execution plan

- [`validation-and-pilot-plan-first-24-months-east-tennessee-two-site.md`](analyses/validation-and-pilot-plan-first-24-months-east-tennessee-two-site.md): **`#connectivity-validation`** (survey/obstruction, power/grounding, WAN reliability testing, remote access hardening, Starlink **may**/**must-not**, cost + **CS-*** stops); **V10** matrix row; pilot **§2.4** row; Related → **Automation stop rules**.
- Execution dossier: [`execution-first-90-days-phase-0-1-east-tennessee.md`](analyses/execution-first-90-days-phase-0-1-east-tennessee.md), [`execution-first-12-months-phase-0-1-east-tennessee.md`](analyses/execution-first-12-months-phase-0-1-east-tennessee.md), [`execution-first-24-months-phase-0-1-east-tennessee.md`](analyses/execution-first-24-months-phase-0-1-east-tennessee.md).
- [`automation-stop-rules-two-site-smart-farm.md`](analyses/automation-stop-rules-two-site-smart-farm.md): **CS-1–CS-4**, **MV-7**.
- [`index.md`](index.md).
- Validator: `validate_wiki.py --strict`; `mkdocs build --strict`.


---

## [2026-04-24] refactor | Network segmentation + hardened remote-access model (Starlink / WAN layer)

- New [`network-segmentation-site-to-site-and-internet-exposure-two-site-smart-farm.md`](analyses/network-segmentation-site-to-site-and-internet-exposure-two-site-smart-farm.md): **site-to-site** assumptions (no flat L2 across commute, overlay, outbound-first field), **segmentation** by device class (user, admin, edge, gateway, telemetry, cameras), **VPN/overlay** policy, **internet** **reachable** vs **never** **directly** **exposed**, **Starlink** **home** **vs** **farm** security implications; ties to runbooks, degraded modes, [`validation plan` § Connectivity](analyses/validation-and-pilot-plan-first-24-months-east-tennessee-two-site.md#connectivity-validation), **business** **plan** **package**.
- [`remote-access-operational-security-model-two-site-smart-farm.md`](analyses/remote-access-operational-security-model-two-site-smart-farm.md): **active** **canonical** **;** **Starlink** **as** **transport-not-trust** table **;** **Execution** **and** **validation** **hooks** **(MV-6,** **MV-7,** **CS-3,** **connectivity** **validation** **)** **;** **links** **segmentation** **page** **.**
- [`reference-architecture-5ac-homebase-120ac-smart-farm.md`](analyses/reference-architecture-5ac-homebase-120ac-smart-farm.md) package map **row** **8** **;** [`connectivity-strategy-for-claxton-and-demory.md`](analyses/connectivity-strategy-for-claxton-and-demory.md) **;** [`two-site-smart-farm-operations.md`](topics/two-site-smart-farm-operations.md) **;** [`index.md`](index.md).
- Validator: `validate_wiki.py --strict`.


---

## [2026-04-24] ingest | Off-grid Demory — power, mesh, HaLow, Meshtastic, Starlink (canonical synthesis)

- **Sources** (already under `raw/processed/2026/`; indexed, not re-ingested): NREL off-grid solar module 5 (design/modeling) and module 6 (installation, O&M); Victron *Wiring Unlimited* and numbered DC/AC wiring web captures; Morse Micro MM6108/MM8108 datasheets; Meshtastic getting started and power configuration captures; Wi‑Fi HaLow / sub‑GHz / OpenWrt article captures; Starlink spec PDFs and farm-WAN article captures. Full paths: [`off-grid-power-rf-wan-source-index-demory-planning-2026-04.md`](source-notes/off-grid-power-rf-wan-source-index-demory-planning-2026-04.md), [`electrical-networking-starlink-inbox-batch-2026-04-23.md`](source-notes/electrical-networking-starlink-inbox-batch-2026-04-23.md).
- **Source index / cluster**: [`off-grid-power-rf-wan-source-index-demory-planning-2026-04.md`](source-notes/off-grid-power-rf-wan-source-index-demory-planning-2026-04.md); [`electrical-networking-starlink-inbox-batch-2026-04-23.md`](source-notes/electrical-networking-starlink-inbox-batch-2026-04-23.md); [`authoritative-execution-evidence-cluster-east-tennessee.md`](source-notes/authoritative-execution-evidence-cluster-east-tennessee.md).
- **Analyses**: [`off-grid-power-strategy-demory-farm-site.md`](analyses/off-grid-power-strategy-demory-farm-site.md), [`mesh-and-field-networking-strategy-off-grid-demory-farm.md`](analyses/mesh-and-field-networking-strategy-off-grid-demory-farm.md), [`off-grid-degraded-modes-power-and-connectivity-demory-farm.md`](analyses/off-grid-degraded-modes-power-and-connectivity-demory-farm.md), [`off-grid-operational-decision-rules-power-and-networking-demory-farm.md`](analyses/off-grid-operational-decision-rules-power-and-networking-demory-farm.md), [`off-grid-farm-execution-topology-demory-mermaid.md`](analyses/off-grid-farm-execution-topology-demory-mermaid.md) (Mermaid reference / pilot / degraded, Pcrit/Popt).
- **Comparison**: [`meshtastic-wi-fi-halow-conventional-wi-fi-off-grid-farm-operations.md`](comparisons/meshtastic-wi-fi-halow-conventional-wi-fi-off-grid-farm-operations.md); [`lorawan-vs-meshtastic-fixed-farm-telemetry.md`](comparisons/lorawan-vs-meshtastic-fixed-farm-telemetry.md) (cross-link).
- **Hub / integration**: [`demory-farm-site-intelligence.md`](analyses/demory-farm-site-intelligence.md) (Off-grid-first section); [`connectivity-strategy-for-claxton-and-demory.md`](analyses/connectivity-strategy-for-claxton-and-demory.md); [`reference-architecture-5ac-homebase-120ac-smart-farm.md`](analyses/reference-architecture-5ac-homebase-120ac-smart-farm.md) package row 9; [`execution-topology-package-two-site-smart-farm.md`](analyses/execution-topology-package-two-site-smart-farm.md); [`manual-fallback-degraded-modes-critical-operations.md`](analyses/manual-fallback-degraded-modes-critical-operations.md); [`east-tennessee-two-site-farm-business-plan.md`](business-plan/east-tennessee-two-site-farm-business-plan.md); [`two-site-smart-farm-operations.md`](topics/two-site-smart-farm-operations.md); [`index.md`](index.md).
- **Remaining unknowns**: metered Wh/day for field networking; exact PV kW and battery kWh; genset presence and policy; permit/AHJ for fixed towers; field RF map at Demory coordinates (not in vault).
- Validator: `uv run python scripts/validate_wiki.py --strict`; `uv run mkdocs build --strict`.


---

## [2026-04-17] refactor | Off-grid Demory woven into business-plan execution package

- **Capital sequencing**: [`east-tennessee-two-site-farm-business-plan-capital-and-financing.md`](analyses/east-tennessee-two-site-farm-business-plan-capital-and-financing.md) — new subsection with explicit A–D order (water/fence → DC Pcrit domain → one gateway/RF class → metering vs DR-1); stable anchor `#off-grid-demory-capital-sequencing`.
- **Smart tech + labor/OPEX**: [`east-tennessee-two-site-farm-business-plan-smart-tech-strategy.md`](analyses/east-tennessee-two-site-farm-business-plan-smart-tech-strategy.md) — `SITE_FARM` off-grid-first consequences table (energy load, mesh-first, maintenance, remote trust).
- **Stop rules + manual validation**: [`automation-stop-rules-two-site-smart-farm.md`](analyses/automation-stop-rules-two-site-smart-farm.md) — **CS-5** (DR-1 / always-on RF); **MV-8** (local-only + SOC-stressed drill); Phase 1 table notes MV-8 for off-grid farm assets.
- **Validation gates**: [`validation-and-pilot-plan-first-24-months-east-tennessee-two-site.md`](analyses/validation-and-pilot-plan-first-24-months-east-tennessee-two-site.md) — `#off-grid-demory-validation-gates` (Dcrit/Pcrit, DR-1/CS-5, MV-8, pilot scope).
- **Execution dossier**: [`execution-first-90-days-phase-0-1-east-tennessee.md`](analyses/execution-first-90-days-phase-0-1-east-tennessee.md), [`execution-first-12-months-phase-0-1-east-tennessee.md`](analyses/execution-first-12-months-phase-0-1-east-tennessee.md), [`execution-first-24-months-phase-0-1-east-tennessee.md`](analyses/execution-first-24-months-phase-0-1-east-tennessee.md) — Demory parallel rules; year-1 MV-8/CS-5; “do not” list extended.
- **Degraded modes**: [`manual-fallback-degraded-modes-critical-operations.md`](analyses/manual-fallback-degraded-modes-critical-operations.md) (PV/battery stressed row); [`automation-degraded-modes-manual-fallback-sop.md`](analyses/automation-degraded-modes-manual-fallback-sop.md) (**E2**).
- **Package + hub**: [`east-tennessee-two-site-farm-business-plan.md`](business-plan/east-tennessee-two-site-farm-business-plan.md) (reading order **6c**, operational artifacts tightened); [`execution-topology-package-two-site-smart-farm.md`](analyses/execution-topology-package-two-site-smart-farm.md) (pilot interpretation); [`two-site-smart-farm-operations.md`](topics/two-site-smart-farm-operations.md); [`off-grid-operational-decision-rules-power-and-networking-demory-farm.md`](analyses/off-grid-operational-decision-rules-power-and-networking-demory-farm.md) (prose cleanup); [`index.md`](index.md).
- Validator: `uv run python scripts/validate_wiki.py --strict`.


---

## [2026-04-18] ingest | Homelab backup stack (restic, Longhorn, farmOS Docker) + backup/HaLow synthesis

**Raw** (inbox → `raw/processed/2026/`): [`restic-backing-up-documentation-0-18-1-capture-inbox-2026-04-17.md`](../../raw/processed/2026/restic-backing-up-documentation-0-18-1-capture-inbox-2026-04-17.md), [`restic-removing-backup-snapshots-documentation-0-18-1-capture-inbox-2026-04-17.md`](../../raw/processed/2026/restic-removing-backup-snapshots-documentation-0-18-1-capture-inbox-2026-04-17.md), [`longhorn-backup-system-capture-inbox-2026-04-17.md`](../../raw/processed/2026/longhorn-backup-system-capture-inbox-2026-04-17.md), [`longhorn-restore-system-capture-inbox-2026-04-17.md`](../../raw/processed/2026/longhorn-restore-system-capture-inbox-2026-04-17.md), [`longhorn-documentation-hub-capture-inbox-2026-04-17.md`](../../raw/processed/2026/longhorn-documentation-hub-capture-inbox-2026-04-17.md), [`farmos-docker-developing-hosting-capture-inbox-2026-04-17.md`](../../raw/processed/2026/farmos-docker-developing-hosting-capture-inbox-2026-04-17.md) (v1.x/MariaDB dev pattern—verify current hosting for 2.x).

**Source note**: [`homelab-backup-stack-official-captures-inbox-2026-04-18.md`](source-notes/homelab-backup-stack-official-captures-inbox-2026-04-18.md).

**Analyses**: [`source-gap-audit-backup-dr-and-subghz-wifi-2026-04-18.md`](analyses/source-gap-audit-backup-dr-and-subghz-wifi-2026-04-18.md), [`backup-strategy-comparison-farmos-homelab-postgresql-containers.md`](analyses/backup-strategy-comparison-farmos-homelab-postgresql-containers.md), [`restore-recovery-tiers-homelab-farm-systems.md`](analyses/restore-recovery-tiers-homelab-farm-systems.md), [`subghz-wi-fi-halow-farm-sensors-deployment-guide.md`](analyses/subghz-wi-fi-halow-farm-sensors-deployment-guide.md), [`off-grid-implications-backup-and-networking-choices.md`](analyses/off-grid-implications-backup-and-networking-choices.md).

**Comparison**: [`wi-fi-halow-lorawan-meshtastic-conventional-wi-fi-farm-field-networking.md`](comparisons/wi-fi-halow-lorawan-meshtastic-conventional-wi-fi-farm-field-networking.md).

**Hubs / integration**: [`farm-data-farmos-and-ag-lab-builds.md`](topics/farm-data-farmos-and-ag-lab-builds.md), [`field-network-iot-comparisons.md`](topics/field-network-iot-comparisons.md), [`data-storage.md`](concepts/data-storage.md), [`wi-fi-halow.md`](concepts/wi-fi-halow.md), [`farmos.md`](entities/farmos.md), [`reference-architecture-5ac-homebase-120ac-smart-farm.md`](analyses/reference-architecture-5ac-homebase-120ac-smart-farm.md), [`meshtastic-wi-fi-halow-conventional-wi-fi-off-grid-farm-operations.md`](comparisons/meshtastic-wi-fi-halow-conventional-wi-fi-off-grid-farm-operations.md), [`index.md`](index.md).

**PDFs**: none in this inbox wave (markdown captures only).

**Remaining gaps**: official farmOS backup chapter as dedicated capture; PostgreSQL vendor Barman/continuous archiving if cluster-scale; regulatory HaLow channel plan per jurisdiction—see gap audit.

- Validator: `uv run python scripts/validate_wiki.py --strict`.


---

## [2026-04-18] ingest | K3s / Longhorn / Rancher / Pi platform (official docs + homelab narrative)

**Raw** (`raw/processed/2026/`): [`k3s-architecture-docs-capture-inbox-2026-04-18.md`](../../raw/processed/2026/k3s-architecture-docs-capture-inbox-2026-04-18.md), [`k3s-installation-index-docs-capture-inbox-2026-04-18.md`](../../raw/processed/2026/k3s-installation-index-docs-capture-inbox-2026-04-18.md), [`k3s-quick-start-guide-docs-capture-inbox-2026-04-18.md`](../../raw/processed/2026/k3s-quick-start-guide-docs-capture-inbox-2026-04-18.md), [`k3s-configuration-options-docs-capture-inbox-2026-04-18.md`](../../raw/processed/2026/k3s-configuration-options-docs-capture-inbox-2026-04-18.md), [`longhorn-csi-on-k3s-docs-capture-inbox-2026-04-18.md`](../../raw/processed/2026/longhorn-csi-on-k3s-docs-capture-inbox-2026-04-18.md), [`rancher-k3s-product-page-capture-inbox-2026-04-18.md`](../../raw/processed/2026/rancher-k3s-product-page-capture-inbox-2026-04-18.md), [`raspberry-pi-k3s-longhorn-rancher-homelab-capture-inbox-2026-04-18.md`](../../raw/processed/2026/raspberry-pi-k3s-longhorn-rancher-homelab-capture-inbox-2026-04-18.md). **External**: [K3s requirements](https://docs.k3s.io/installation/requirements), [Rancher install on Kubernetes](https://rancher.com/docs/rancher/latest/en/installation/install-rancher-on-k8s/).

**Source note**: [`k3s-longhorn-rancher-pi-platform-official-captures-inbox-2026-04-18.md`](source-notes/k3s-longhorn-rancher-pi-platform-official-captures-inbox-2026-04-18.md).

**Analyses**: [`homelab-edge-kubernetes-platform-strategy-pi-k3s-longhorn-rancher.md`](analyses/homelab-edge-kubernetes-platform-strategy-pi-k3s-longhorn-rancher.md), [`raspberry-pi-fleet-provisioning-standard-smart-farm-homelab.md`](analyses/raspberry-pi-fleet-provisioning-standard-smart-farm-homelab.md), [`longhorn-vs-central-storage-architecture-homelab-farm-platform.md`](analyses/longhorn-vs-central-storage-architecture-homelab-farm-platform.md), [`rancher-role-and-timing-k3s-homelab-farm-platform.md`](analyses/rancher-role-and-timing-k3s-homelab-farm-platform.md), [`kubernetes-platform-backup-dr-pi-k3s-longhorn.md`](analyses/kubernetes-platform-backup-dr-pi-k3s-longhorn.md), [`platform-decision-memo-phase-homelab-k3s-pi-fleet-2026-04-18.md`](analyses/platform-decision-memo-phase-homelab-k3s-pi-fleet-2026-04-18.md).

**Hubs**: [`domain-content-overview.md`](analyses/domain-content-overview.md), [`reference-architecture-5ac-homebase-120ac-smart-farm.md`](analyses/reference-architecture-5ac-homebase-120ac-smart-farm.md), [`homelab-self-hosting-and-edge-narratives.md`](topics/homelab-self-hosting-and-edge-narratives.md), [`docker-kubernetes-compose-and-bake.md`](topics/docker-kubernetes-compose-and-bake.md), [`two-site-smart-farm-operations.md`](topics/two-site-smart-farm-operations.md), [`backup-strategy-comparison-farmos-homelab-postgresql-containers.md`](analyses/backup-strategy-comparison-farmos-homelab-postgresql-containers.md), [`homelab-backup-stack-official-captures-inbox-2026-04-18.md`](source-notes/homelab-backup-stack-official-captures-inbox-2026-04-18.md), [`index.md`](index.md).

**Remaining gaps**: processed capture for full K3s **Requirements** page; full Rancher requirements page capture; RKE2 evaluation if policy shifts ([`k3s or RKE2`](source-notes/k3s-or-rke2.md)).

- Validator: `uv run python scripts/validate_wiki.py --strict`.

## [2026-04-17] policy | Structural IA debt audit + guide metadata (`page_subtype`, `operational_maturity`)

- **Audit page**: [`structural-debt-audit-wiki-ia-and-operational-maturity.md`](analyses/structural-debt-audit-wiki-ia-and-operational-maturity.md) — sprawl, ownership, flat-index pain, implemented mitigations.
- **Router topic**: [`wiki-navigation-and-structural-hubs.md`](topics/wiki-navigation-and-structural-hubs.md) — themed entry points (meta, ET two-site, homelab k3s, runbooks).
- **`AGENTS.md`**: analysis **`page_subtype`** (e.g. `operational_guide`, `standard`, `meta_audit`, `query_synthesis`); optional **`operational_maturity`** (`draft` / `pilot_ready` / `field_tested` / `superseded`); **Operational and guide-shaped content** subsection under canonicalization; index maintenance + session checklist point to navigation hub.
- **Exemplar frontmatter**: [`how-to-provision-k3s-longhorn-and-rancher-on-a-raspberry-pi-fleet.md`](analyses/how-to-provision-k3s-longhorn-and-rancher-on-a-raspberry-pi-fleet.md), [`raspberry-pi-fleet-provisioning-standard-smart-farm-homelab.md`](analyses/raspberry-pi-fleet-provisioning-standard-smart-farm-homelab.md).
- **Hubs updated**: [`domain-content-overview.md`](analyses/domain-content-overview.md), [`structural-audit-page-ownership-entity-gaps-and-hub-routing.md`](analyses/structural-audit-page-ownership-entity-gaps-and-hub-routing.md), [`two-site-smart-farm-operations.md`](topics/two-site-smart-farm-operations.md), [`index.md`](index.md).
- Validator: `uv run python scripts/validate_wiki.py --strict`.

## [2026-04-18] ingest | Homelab / edge / networking inbox → processed (k3s, Longhorn, restic, ESPHome, WireGuard, OpenWrt PDF)

- **Raw**: moved **37** markdown + **`openwrt.pdf`** from `raw/inbox/` → `raw/processed/2026/` (kebab-case basenames); **`pdf_to_markdown.py`** → `raw/processed/2026/openwrt-extracted.md` beside `raw/processed/2026/openwrt.pdf`.
- **Source note**: [`homelab-edge-networking-inbox-batch-2026-04-18.md`](source-notes/homelab-edge-networking-inbox-batch-2026-04-18.md) — table of paths; synthesis links to DR package, k3s captures, homelab topics, MQTT/field network, remote access.
- **`index.md`**: source-notes entry added.
- **Note**: `raw/**` is **gitignored** by default; use **`git add -f`** for corpus files you intend to version (see repository `.gitignore`).

## [2026-04-17] ingest | Backup / DR official link batch + canonical DR package (farmOS, k3s, Longhorn, Rancher)

- **Raw**: [`backup-dr-official-documentation-links-batch-2026-04-17.md`](../../raw/processed/2026/backup-dr-official-documentation-links-batch-2026-04-17.md) — curated pointers (k3s etcd backup/restore, Rancher manager docs, PostgreSQL manual, cross-refs to existing Longhorn/restic captures).
- **Source note**: [`backup-dr-official-documentation-cluster.md`](source-notes/backup-dr-official-documentation-cluster.md).
- **Hub**: [`backup-and-disaster-recovery-package-smart-farm-stack.md`](analyses/backup-and-disaster-recovery-package-smart-farm-stack.md) — package map, backup vs sync, volume vs app-aware, Mermaid scope.
- **New analyses**: [`central-vs-local-backup-scope-farm-edge-stack.md`](analyses/central-vs-local-backup-scope-farm-edge-stack.md), [`runbook-backup-validation-and-recovery-drill.md`](analyses/runbook-backup-validation-and-recovery-drill.md).
- **Updated**: [`backup-strategy-comparison-farmos-homelab-postgresql-containers.md`](analyses/backup-strategy-comparison-farmos-homelab-postgresql-containers.md), [`restore-recovery-tiers-homelab-farm-systems.md`](analyses/restore-recovery-tiers-homelab-farm-systems.md) (RPO/RTO worksheet), [`kubernetes-platform-backup-dr-pi-k3s-longhorn.md`](analyses/kubernetes-platform-backup-dr-pi-k3s-longhorn.md) (Rancher + secrets tracks), Pi provisioning/DR cross-links, [`reference-architecture-5ac-homebase-120ac-smart-farm.md`](analyses/reference-architecture-5ac-homebase-120ac-smart-farm.md), [`domain-content-overview.md`](analyses/domain-content-overview.md), [`wiki-navigation-and-structural-hubs.md`](topics/wiki-navigation-and-structural-hubs.md), [`homelab-backup-stack-official-captures-inbox-2026-04-18.md`](source-notes/homelab-backup-stack-official-captures-inbox-2026-04-18.md); [`index.md`](index.md).
- Validator: `uv run python scripts/validate_wiki.py --strict`.

## [2026-04-17] refactor | Pi k3s + Longhorn + Rancher operational runbook package

- **Canonical hub**: [`how-to-provision-k3s-longhorn-and-rancher-on-a-raspberry-pi-fleet.md`](analyses/how-to-provision-k3s-longhorn-and-rancher-on-a-raspberry-pi-fleet.md) — stepwise sequences (prerequisites → BOM → network/power → storage model → bootstrap → Longhorn → Rancher → backup → validation → troubleshooting); **mandatory** vs **optional HA**, **P0/P1** vs **later**, Pi resource limits.
- **Supporting pages**: `raspberry-pi-k3s-fleet-*.md` (10) under `wiki/analyses/`.
- **Cross-links**: [`homelab-edge-kubernetes-platform-strategy-pi-k3s-longhorn-rancher.md`](analyses/homelab-edge-kubernetes-platform-strategy-pi-k3s-longhorn-rancher.md), [`reference-architecture-5ac-homebase-120ac-smart-farm.md`](analyses/reference-architecture-5ac-homebase-120ac-smart-farm.md), [`backup-strategy-comparison-farmos-homelab-postgresql-containers.md`](analyses/backup-strategy-comparison-farmos-homelab-postgresql-containers.md), [`kubernetes-platform-backup-dr-pi-k3s-longhorn.md`](analyses/kubernetes-platform-backup-dr-pi-k3s-longhorn.md), [`domain-content-overview.md`](analyses/domain-content-overview.md), [`two-site-smart-farm-operations.md`](topics/two-site-smart-farm-operations.md), [`docker-kubernetes-compose-and-bake.md`](topics/docker-kubernetes-compose-and-bake.md), [`homelab-self-hosting-and-edge-narratives.md`](topics/homelab-self-hosting-and-edge-narratives.md), [`east-tennessee-two-site-farm-business-plan-smart-tech-strategy.md`](analyses/east-tennessee-two-site-farm-business-plan-smart-tech-strategy.md), [`execution-dossier-hub-phase-0-1-east-tennessee.md`](analyses/execution-dossier-hub-phase-0-1-east-tennessee.md), [`longhorn-vs-central-storage-architecture-homelab-farm-platform.md`](analyses/longhorn-vs-central-storage-architecture-homelab-farm-platform.md), [`raspberry-pi-fleet-provisioning-standard-smart-farm-homelab.md`](analyses/raspberry-pi-fleet-provisioning-standard-smart-farm-homelab.md); [`index.md`](index.md) updated.
- Validator: `uv run python scripts/validate_wiki.py --strict`.

## [2026-04-17] refactor | Local evidence package — East Tennessee two-site (field baselines + workflow)

- **Topic hub**: [`local-evidence-package-east-tennessee-two-site.md`](topics/local-evidence-package-east-tennessee-two-site.md) — spine for **measured / reported / assumption / unknown** tables and **decision gates** (no invented parcel or utility facts).
- **New analyses**: [`site-inventory-baseline-claxton-home-base-east-tennessee.md`](analyses/site-inventory-baseline-claxton-home-base-east-tennessee.md), [`site-inventory-baseline-demory-farm-site-east-tennessee.md`](analyses/site-inventory-baseline-demory-farm-site-east-tennessee.md), [`infrastructure-inventory-baseline-two-sites-east-tennessee.md`](analyses/infrastructure-inventory-baseline-two-sites-east-tennessee.md), [`utility-and-service-baseline-two-sites-east-tennessee.md`](analyses/utility-and-service-baseline-two-sites-east-tennessee.md), [`loads-register-known-estimated-unknown-two-sites-east-tennessee.md`](analyses/loads-register-known-estimated-unknown-two-sites-east-tennessee.md), [`parcel-evidence-intake-and-validation-workflow-east-tennessee-two-site.md`](analyses/parcel-evidence-intake-and-validation-workflow-east-tennessee-two-site.md).
- **New topic**: [`field-observation-template-package-east-tennessee-two-site.md`](topics/field-observation-template-package-east-tennessee-two-site.md) — copy-paste visit templates.
- **Cross-links**: [`local-site-and-county-intelligence.md`](topics/local-site-and-county-intelligence.md), [`parcel-intelligence-package-east-tennessee-two-site.md`](topics/parcel-intelligence-package-east-tennessee-two-site.md), [`claxton-and-demory-missing-data-register.md`](analyses/claxton-and-demory-missing-data-register.md), [`claxton-home-base-site-intelligence.md`](analyses/claxton-home-base-site-intelligence.md), [`demory-farm-site-intelligence.md`](analyses/demory-farm-site-intelligence.md), entities **Claxton** / **Demory**, [`execution-dossier-hub-phase-0-1-east-tennessee.md`](analyses/execution-dossier-hub-phase-0-1-east-tennessee.md), [`east-tennessee-two-site-farm-business-plan.md`](business-plan/east-tennessee-two-site-farm-business-plan.md), [`two-site-smart-farm-operations.md`](topics/two-site-smart-farm-operations.md); [`index.md`](index.md) updated.
- Validator: `uv run python scripts/validate_wiki.py --strict`.

## [2026-04-17] refactor | Platform doctrine package — homelab / farm edge (Pi, k3s, Longhorn, Rancher)

- **Topic hub**: [`platform-doctrine-package-homelab-farm-edge.md`](topics/platform-doctrine-package-homelab-farm-edge.md) — first-class doctrine: **pilot vs production**, **HA** semantics, Mermaid overview, ties to **farmOS**, **telemetry**, **backup/DR**.
- **Renamed display title** (same path): [`homelab-edge-kubernetes-platform-strategy-pi-k3s-longhorn-rancher.md`](analyses/homelab-edge-kubernetes-platform-strategy-pi-k3s-longhorn-rancher.md) → **Platform strategy for farm and homestead services** (alias preserved).
- **New analyses**: [`k3s-role-in-homelab-farm-platform.md`](analyses/k3s-role-in-homelab-farm-platform.md), [`longhorn-role-in-homelab-farm-platform.md`](analyses/longhorn-role-in-homelab-farm-platform.md), [`ha-meaning-and-constraints-homelab-farm-platform.md`](analyses/ha-meaning-and-constraints-homelab-farm-platform.md).
- **Updated**: [`platform-decision-memo-phase-homelab-k3s-pi-fleet-2026-04-18.md`](analyses/platform-decision-memo-phase-homelab-k3s-pi-fleet-2026-04-18.md), [`raspberry-pi-fleet-provisioning-standard-smart-farm-homelab.md`](analyses/raspberry-pi-fleet-provisioning-standard-smart-farm-homelab.md) (operational boundaries), [`longhorn-vs-central-storage-architecture-homelab-farm-platform.md`](analyses/longhorn-vs-central-storage-architecture-homelab-farm-platform.md) (hybrid Mermaid), [`rancher-role-and-timing-k3s-homelab-farm-platform.md`](analyses/rancher-role-and-timing-k3s-homelab-farm-platform.md), [`how-to-provision-k3s-longhorn-and-rancher-on-a-raspberry-pi-fleet.md`](analyses/how-to-provision-k3s-longhorn-and-rancher-on-a-raspberry-pi-fleet.md); hubs [`wiki-navigation-and-structural-hubs.md`](topics/wiki-navigation-and-structural-hubs.md), [`domain-content-overview.md`](analyses/domain-content-overview.md), [`reference-architecture-5ac-homebase-120ac-smart-farm.md`](analyses/reference-architecture-5ac-homebase-120ac-smart-farm.md), [`two-site-smart-farm-operations.md`](topics/two-site-smart-farm-operations.md), [`homelab-self-hosting-and-edge-narratives.md`](topics/homelab-self-hosting-and-edge-narratives.md), [`docker-kubernetes-compose-and-bake.md`](topics/docker-kubernetes-compose-and-bake.md), DR/backup package cross-links; [`index.md`](index.md).
- Validator: `uv run python scripts/validate_wiki.py --strict`; MkDocs: `uv run mkdocs build --strict`.

## [2026-04-17] refactor | Off-grid systems doctrine package — Demory farm (SITE_FARM)

- **Topic hub**: [`off-grid-systems-doctrine-package-demory-farm-site.md`](topics/off-grid-systems-doctrine-package-demory-farm-site.md) — first-class map: power domains, field-node classes, WAN dependency, local-first ops, degraded modes, **DR-*** stop rules; Mermaid end-to-end diagram.
- **Display title update** (same path): [`off-grid-power-strategy-demory-farm-site.md`](analyses/off-grid-power-strategy-demory-farm-site.md) → **Off-grid power doctrine — Demory farm site** (aliases preserve “power strategy”).
- **New analyses**: [`off-grid-power-domains-and-battery-tiers-demory-farm.md`](analyses/off-grid-power-domains-and-battery-tiers-demory-farm.md), [`field-node-classes-and-communication-roles-demory-farm.md`](analyses/field-node-classes-and-communication-roles-demory-farm.md), [`connectivity-dependency-map-farm-systems-demory-farm.md`](analyses/connectivity-dependency-map-farm-systems-demory-farm.md), [`local-first-wan-optional-operating-model-demory-farm.md`](analyses/local-first-wan-optional-operating-model-demory-farm.md).
- **Updated**: [`off-grid-degraded-modes-power-and-connectivity-demory-farm.md`](analyses/off-grid-degraded-modes-power-and-connectivity-demory-farm.md) (state diagram), [`off-grid-operational-decision-rules-power-and-networking-demory-farm.md`](analyses/off-grid-operational-decision-rules-power-and-networking-demory-farm.md) → **Off-grid infrastructure stop rules** + simplification triggers, [`mesh-and-field-networking-strategy-off-grid-demory-farm.md`](analyses/mesh-and-field-networking-strategy-off-grid-demory-farm.md), [`off-grid-farm-execution-topology-demory-mermaid.md`](analyses/off-grid-farm-execution-topology-demory-mermaid.md); [`wiki-navigation-and-structural-hubs.md`](topics/wiki-navigation-and-structural-hubs.md); [`east-tennessee-two-site-farm-business-plan.md`](business-plan/east-tennessee-two-site-farm-business-plan.md); [`execution-dossier-hub-phase-0-1-east-tennessee.md`](analyses/execution-dossier-hub-phase-0-1-east-tennessee.md); [`demory-farm-site-intelligence.md`](analyses/demory-farm-site-intelligence.md); [`demory-farm-site.md`](entities/demory-farm-site.md); [`reference-architecture-5ac-homebase-120ac-smart-farm.md`](analyses/reference-architecture-5ac-homebase-120ac-smart-farm.md); [`off-grid-power-rf-wan-source-index-demory-planning-2026-04.md`](source-notes/off-grid-power-rf-wan-source-index-demory-planning-2026-04.md); [`index.md`](index.md).
- Validator: `uv run python scripts/validate_wiki.py --strict`; MkDocs: `uv run mkdocs build --strict`.

## [2026-04-17] refactor | Onboarding layer + glossary expansion

- **New topics**: [`start-here-smart-farm-wiki.md`](topics/start-here-smart-farm-wiki.md) (fast paths), [`how-to-read-this-wiki.md`](topics/how-to-read-this-wiki.md) (layers, page types, vocabulary shortcuts).
- **New glossary entries**: [`execution-gate.md`](glossary/execution-gate.md), [`distance-tax-two-site.md`](glossary/distance-tax-two-site.md), [`entity-vs-site-role.md`](glossary/entity-vs-site-role.md), [`off-grid-site-farm-terms.md`](glossary/off-grid-site-farm-terms.md), [`edge-homelab-platform-terms.md`](glossary/edge-homelab-platform-terms.md), [`automation-stop-rules-terms.md`](glossary/automation-stop-rules-terms.md), [`labor-coverage-two-site.md`](glossary/labor-coverage-two-site.md).
- **Updated**: [`smart-farm-wiki-glossary.md`](glossary/smart-farm-wiki-glossary.md) (categorized hub), [`validation-gate.md`](glossary/validation-gate.md) (V vs G), [`degraded-mode.md`](glossary/degraded-mode.md), [`two-site-sites.md`](glossary/two-site-sites.md); [`overview.md`](overview.md) (onboarding-first); [`wiki-navigation-and-structural-hubs.md`](topics/wiki-navigation-and-structural-hubs.md); [`domain-content-overview.md`](analyses/domain-content-overview.md); [`index.md`](index.md) (Overview + Topics + Glossary lists).
- Validator: `uv run python scripts/validate_wiki.py --strict`.

## [2026-04-24] refactor | Operational standards layer (farm & homelab platform)

- **Topic hub**: [`operational-standards-farm-homelab-platform.md`](topics/operational-standards-farm-homelab-platform.md) — catalog linking standards to runbooks/guides.
- **New standards** (`page_subtype: standard`): [`k3s-cluster-bootstrap-standard-smart-farm-homelab.md`](analyses/k3s-cluster-bootstrap-standard-smart-farm-homelab.md), [`kubernetes-edge-scheduling-storage-longhorn-standard.md`](analyses/kubernetes-edge-scheduling-storage-longhorn-standard.md), [`secrets-and-certificates-edge-cluster-standard.md`](analyses/secrets-and-certificates-edge-cluster-standard.md), [`monitoring-and-logging-expectations-edge-cluster-standard.md`](analyses/monitoring-and-logging-expectations-edge-cluster-standard.md), [`backup-validation-cadence-standard-farm-stack.md`](analyses/backup-validation-cadence-standard-farm-stack.md), [`field-node-identity-and-naming-standard.md`](analyses/field-node-identity-and-naming-standard.md), [`gateway-naming-and-role-assignment-standard.md`](analyses/gateway-naming-and-role-assignment-standard.md), [`site-to-site-network-role-boundaries-standard.md`](analyses/site-to-site-network-role-boundaries-standard.md).
- **Updated**: [`raspberry-pi-fleet-provisioning-standard-smart-farm-homelab.md`](analyses/raspberry-pi-fleet-provisioning-standard-smart-farm-homelab.md); [`platform-doctrine-package-homelab-farm-edge.md`](topics/platform-doctrine-package-homelab-farm-edge.md); [`wiki-navigation-and-structural-hubs.md`](topics/wiki-navigation-and-structural-hubs.md); [`two-site-smart-farm-operations.md`](topics/two-site-smart-farm-operations.md); [`overview.md`](overview.md); [`domain-content-overview.md`](analyses/domain-content-overview.md); [`index.md`](index.md).
- Validator: `uv run python scripts/validate_wiki.py --strict`.

## [2026-04-24] refactor | Backup and DR doctrine package (tighten + DR decision rules)

- **New**: [`disaster-recovery-decision-rules-farm-edge-stack.md`](analyses/disaster-recovery-decision-rules-farm-edge-stack.md) — failure classes, restore order, platform + execution alignment.
- **Tightened spine**: [`backup-and-disaster-recovery-package-smart-farm-stack.md`](analyses/backup-and-disaster-recovery-package-smart-farm-stack.md) — scope table, read order, business execution context, package map row, diagram label.
- **Doctrine pages** (`operational_guide` / reviewed where noted): [`backup-strategy-comparison-farmos-homelab-postgresql-containers.md`](analyses/backup-strategy-comparison-farmos-homelab-postgresql-containers.md), [`restore-recovery-tiers-homelab-farm-systems.md`](analyses/restore-recovery-tiers-homelab-farm-systems.md), [`runbook-backup-validation-and-recovery-drill.md`](analyses/runbook-backup-validation-and-recovery-drill.md), [`central-vs-local-backup-scope-farm-edge-stack.md`](analyses/central-vs-local-backup-scope-farm-edge-stack.md), [`kubernetes-platform-backup-dr-pi-k3s-longhorn.md`](analyses/kubernetes-platform-backup-dr-pi-k3s-longhorn.md) (integration role).
- **Cross-links**: [`raspberry-pi-k3s-fleet-backup-and-restore-sequence.md`](analyses/raspberry-pi-k3s-fleet-backup-and-restore-sequence.md), [`off-grid-implications-backup-and-networking-choices.md`](analyses/off-grid-implications-backup-and-networking-choices.md); [`backup-restore-tier-labels-farm-stack.md`](entities/backup-restore-tier-labels-farm-stack.md); [`backup-disaster-recovery-doctrine-hub.md`](topics/backup-disaster-recovery-doctrine-hub.md); [`wiki-navigation-and-structural-hubs.md`](topics/wiki-navigation-and-structural-hubs.md); [`index.md`](index.md); [`domain-content-overview.md`](analyses/domain-content-overview.md).
- Validator: `uv run python scripts/validate_wiki.py --strict`.

## [2026-04-24] refactor | Canonical package hubs (navigation routers)

- **New topics**: [`backup-disaster-recovery-doctrine-hub.md`](topics/backup-disaster-recovery-doctrine-hub.md), [`off-grid-power-and-field-networking-hub.md`](topics/off-grid-power-and-field-networking-hub.md), [`business-plan-execution-and-pilot-operations-hub.md`](topics/business-plan-execution-and-pilot-operations-hub.md).
- **Improved hubs**: [`platform-doctrine-package-homelab-farm-edge.md`](topics/platform-doctrine-package-homelab-farm-edge.md), [`local-site-and-county-intelligence.md`](topics/local-site-and-county-intelligence.md), [`off-grid-systems-doctrine-package-demory-farm-site.md`](topics/off-grid-systems-doctrine-package-demory-farm-site.md) — **what this hub owns**, **start here**, **canonical vs supporting**.
- **Cross-links**: [`backup-and-disaster-recovery-package-smart-farm-stack.md`](analyses/backup-and-disaster-recovery-package-smart-farm-stack.md) → DR topic hub; [`east-tennessee-two-site-farm-business-plan.md`](business-plan/east-tennessee-two-site-farm-business-plan.md) → execution hub; [`wiki-navigation-and-structural-hubs.md`](topics/wiki-navigation-and-structural-hubs.md), [`two-site-smart-farm-operations.md`](topics/two-site-smart-farm-operations.md), [`start-here-smart-farm-wiki.md`](topics/start-here-smart-farm-wiki.md), [`overview.md`](overview.md), [`index.md`](index.md), [`domain-content-overview.md`](analyses/domain-content-overview.md).
- Validator: `uv run python scripts/validate_wiki.py --strict`.

## [2026-04-24] refactor | Source authority hardening (audit + official clusters + classified low-authority notes)

- **Audit**: [`source-authority-hardening-audit.md`](analyses/source-authority-hardening-audit.md) — weak areas by domain, authoritative categories, backlog (FHWA PDF ingest).
- **New source-notes**: [`authoritative-roads-and-driveways-source-cluster.md`](source-notes/authoritative-roads-and-driveways-source-cluster.md), [`fhwa-gravel-roads-maintenance-guide-official-reference.md`](source-notes/fhwa-gravel-roads-maintenance-guide-official-reference.md) (official URL; PDF not in `raw/` yet), [`postgresql-and-postgis-official-documentation-primary-cluster.md`](source-notes/postgresql-and-postgis-official-documentation-primary-cluster.md).
- **Canonical / concept updates**: [`backup-and-disaster-recovery-package-smart-farm-stack.md`](analyses/backup-and-disaster-recovery-package-smart-farm-stack.md) (evidence stance; `confidence: high`), [`evidence-grade-and-canonical-authority.md`](concepts/evidence-grade-and-canonical-authority.md), [`steep-curved-hill-dirt-road-erosion-prevention-120-acres.md`](analyses/steep-curved-hill-dirt-road-erosion-prevention-120-acres.md).
- **Topics / hubs**: [`rural-road-and-driveway-erosion-sources.md`](topics/rural-road-and-driveway-erosion-sources.md), [`lora-mqtt-and-gateway-bridges.md`](topics/lora-mqtt-and-gateway-bridges.md), [`farm-data-farmos-and-ag-lab-builds.md`](topics/farm-data-farmos-and-ag-lab-builds.md), [`homelab-self-hosting-and-edge-narratives.md`](topics/homelab-self-hosting-and-edge-narratives.md), [`wiki-navigation-and-structural-hubs.md`](topics/wiki-navigation-and-structural-hubs.md).
- **Marked exploratory** (`confidence: low` + tags): Reddit/Instructables/Medium threads (Meshtastic MQTT, erosion, basement workshop, ducks, homelab motivation, ag-lab); Medium PostgreSQL/PostGIS primers.
- **Mixed-corpus note**: [`off-grid-power-rf-wan-source-index-demory-planning-2026-04.md`](source-notes/off-grid-power-rf-wan-source-index-demory-planning-2026-04.md).
- **Index / overview**: [`index.md`](index.md), [`overview.md`](overview.md) (source-authority link in orientation list).
- Validator: `uv run python scripts/validate_wiki.py --strict`.

## [2026-04-23] refactor | Entity layer — operating objects (roles and categories)

- **Gap audit (meta)**: [`entity-layer-operating-objects-gap-audit.md`](analyses/entity-layer-operating-objects-gap-audit.md).
- **New entities**: [`field-node-classes-off-grid-farm-roles.md`](entities/field-node-classes-off-grid-farm-roles.md), [`edge-cluster-storage-roles-homelab-farm.md`](entities/edge-cluster-storage-roles-homelab-farm.md), [`backup-restore-tier-labels-farm-stack.md`](entities/backup-restore-tier-labels-farm-stack.md), [`rf-telemetry-gateway-roles-field-network.md`](entities/rf-telemetry-gateway-roles-field-network.md), [`wan-edge-and-backhaul-roles.md`](entities/wan-edge-and-backhaul-roles.md), [`labor-roles-two-site-farm-operations.md`](entities/labor-roles-two-site-farm-operations.md), [`farm-business-legal-entity-model.md`](entities/farm-business-legal-entity-model.md), [`farm-market-channel-categories.md`](entities/farm-market-channel-categories.md), [`farm-infrastructure-system-categories.md`](entities/farm-infrastructure-system-categories.md), [`edge-service-deployment-classes.md`](entities/edge-service-deployment-classes.md), [`field-radio-link-classes.md`](entities/field-radio-link-classes.md), [`kubernetes-edge-control-plane-roles.md`](entities/kubernetes-edge-control-plane-roles.md).
- **Updated**: [`field-telemetry-network-two-site.md`](entities/field-telemetry-network-two-site.md) (operating-object links); [`structural-audit-page-ownership-entity-gaps-and-hub-routing.md`](analyses/structural-audit-page-ownership-entity-gaps-and-hub-routing.md); [`domain-content-overview.md`](analyses/domain-content-overview.md); [`wiki-navigation-and-structural-hubs.md`](topics/wiki-navigation-and-structural-hubs.md); [`two-site-smart-farm-operations.md`](topics/two-site-smart-farm-operations.md); [`platform-doctrine-package-homelab-farm-edge.md`](topics/platform-doctrine-package-homelab-farm-edge.md); [`off-grid-systems-doctrine-package-demory-farm-site.md`](topics/off-grid-systems-doctrine-package-demory-farm-site.md); [`overview.md`](overview.md); [`start-here-smart-farm-wiki.md`](topics/start-here-smart-farm-wiki.md); [`smart-farm-wiki-glossary.md`](glossary/smart-farm-wiki-glossary.md); [`index.md`](index.md).
- Validator: `uv run python scripts/validate_wiki.py --strict`.

## [2026-04-24] policy | Procedural guides package strategy + AGENTS guide/runbook distinctions

- **Evaluation**: Taxonomy was already sufficient for durable how-tos: guides live in `wiki/analyses/` with `page_subtype: operational_guide` and `operational_maturity` (`draft` / `pilot_ready` / `field_tested` / `superseded`); no new directory or validator change required.
- **New topic (canonical strategy)**: [`procedural-guides-package-strategy-smart-farm-wiki.md`](topics/procedural-guides-package-strategy-smart-farm-wiki.md) — where guides live, **vs** essays/standards/runbooks, maturity, links to architecture / standards / entities; **guide hub** table.
- **Updated**: [`AGENTS.md`](../../AGENTS.md) — mission line, **Guides vs runbooks vs standards** table, first-class guides bullet, session checklist link; [`wiki-navigation-and-structural-hubs.md`](topics/wiki-navigation-and-structural-hubs.md) — **Procedural guides** section; [`index.md`](index.md); [`overview.md`](overview.md); [`domain-content-overview.md`](analyses/domain-content-overview.md); [`start-here-smart-farm-wiki.md`](topics/start-here-smart-farm-wiki.md); [`how-to-read-this-wiki.md`](topics/how-to-read-this-wiki.md); [`operational-standards-farm-homelab-platform.md`](topics/operational-standards-farm-homelab-platform.md); [`platform-doctrine-package-homelab-farm-edge.md`](topics/platform-doctrine-package-homelab-farm-edge.md).
- Validator: `uv run python scripts/validate_wiki.py --strict`.

## [2026-04-25] ingest | Inbox batch — TN farm policy, LoRaWAN stack, ChirpStack, Meshtastic, Decentlab, HaLow

- **Moved** (inbox drop filed **2026-04-18**) 42 files from `raw/inbox/` → `raw/processed/2026/` (kebab-case basenames); **PDF extracts**: 7 new `*-extracted.md` via `scripts/pdf_to_markdown.py` (HaLowLink ×2, LSE01 power, TN law PDF, W1266, farmers.gov taxes, LoRaWAN spec).
- **Source-note index**: [`inbox-batch-2026-04-18-tennessee-farm-lorawan-chirpstack-meshtastic-decentlab-halow.md`](source-notes/inbox-batch-2026-04-18-tennessee-farm-lorawan-chirpstack-meshtastic-decentlab-halow.md) — themed tables + `source_ids`.
- **Cross-links**: [`tennessee-hobby-farm-and-small-farm-business-sources.md`](topics/tennessee-hobby-farm-and-small-farm-business-sources.md), [`smart-agriculture-meshtastic-and-lorawan.md`](topics/smart-agriculture-meshtastic-and-lorawan.md), [`lora-mqtt-and-gateway-bridges.md`](topics/lora-mqtt-and-gateway-bridges.md), [`field-network-iot-comparisons.md`](topics/field-network-iot-comparisons.md), [`authoritative-execution-evidence-cluster-east-tennessee.md`](source-notes/authoritative-execution-evidence-cluster-east-tennessee.md); [`index.md`](index.md).
- Validator: `uv run python scripts/validate_wiki.py --strict` (and `--raw-pdf-links --strict` when local corpus complete).

## [2026-04-25] refactor | Demory farm long-range sensor architecture package

- **Source cluster**: [`demory-farm-sensor-layer-official-and-operator-source-cluster.md`](source-notes/demory-farm-sensor-layer-official-and-operator-source-cluster.md) — LoRaWAN spec, ChirpStack, HaLowLink, Meshtastic, vendor pages, Starlink as WAN; **See also** on [`inbox-batch-2026-04-18-...`](source-notes/inbox-batch-2026-04-18-tennessee-farm-lorawan-chirpstack-meshtastic-decentlab-halow.md).
- **Canonical analyses**: [`farm-sensor-architecture-demory-farm-site.md`](analyses/farm-sensor-architecture-demory-farm-site.md) (reference / pilot / degraded Mermaid), [`gateway-controller-patterns-demory-120-acre-farm.md`](analyses/gateway-controller-patterns-demory-120-acre-farm.md), [`sensor-degraded-modes-and-failure-rules-demory-farm.md`](analyses/sensor-degraded-modes-and-failure-rules-demory-farm.md), [`sensor-power-and-duty-cycle-assumptions-demory-farm.md`](analyses/sensor-power-and-duty-cycle-assumptions-demory-farm.md), [`sensor-checklist-matrix-for-demory-farm.md`](analyses/sensor-checklist-matrix-for-demory-farm.md).
- **Comparison**: [`lorawan-wi-fi-halow-meshtastic-demory-farm-sensor-layer.md`](comparisons/lorawan-wi-fi-halow-meshtastic-demory-farm-sensor-layer.md); **updated** [`field-node-classes-and-communication-roles-demory-farm.md`](analyses/field-node-classes-and-communication-roles-demory-farm.md), [`mesh-and-field-networking-strategy-off-grid-demory-farm.md`](analyses/mesh-and-field-networking-strategy-off-grid-demory-farm.md), [`subghz-wi-fi-halow-farm-sensors-deployment-guide.md`](analyses/subghz-wi-fi-halow-farm-sensors-deployment-guide.md), [`field-telemetry-reference-architecture-homestead-120ac.md`](analyses/field-telemetry-reference-architecture-homestead-120ac.md), [`connectivity-strategy-for-claxton-and-demory.md`](analyses/connectivity-strategy-for-claxton-and-demory.md), [`domain-content-overview.md`](analyses/domain-content-overview.md), [`execution-dossier-hub-phase-0-1-east-tennessee.md`](analyses/execution-dossier-hub-phase-0-1-east-tennessee.md).
- **Entities / topics**: [`demory-farm-site.md`](entities/demory-farm-site.md), [`field-telemetry-network-two-site.md`](entities/field-telemetry-network-two-site.md), [`rf-telemetry-gateway-roles-field-network.md`](entities/rf-telemetry-gateway-roles-field-network.md), [`wan-edge-and-backhaul-roles.md`](entities/wan-edge-and-backhaul-roles.md), [`off-grid-systems-doctrine-package-demory-farm-site.md`](topics/off-grid-systems-doctrine-package-demory-farm-site.md), [`off-grid-power-and-field-networking-hub.md`](topics/off-grid-power-and-field-networking-hub.md), [`two-site-smart-farm-operations.md`](topics/two-site-smart-farm-operations.md), [`wiki-navigation-and-structural-hubs.md`](topics/wiki-navigation-and-structural-hubs.md); **business plan**: [`east-tennessee-two-site-farm-business-plan.md`](business-plan/east-tennessee-two-site-farm-business-plan.md).
- **Index**: [`index.md`](index.md).
- Validator: `uv run python scripts/validate_wiki.py --strict`.

## [2026-04-25] lint | Business plan + local-site hub — Demory sensor links

- **Updated**: [`east-tennessee-two-site-farm-business-plan.md`](business-plan/east-tennessee-two-site-farm-business-plan.md) — Demory off-grid-first bullet: [`Farm sensor architecture — Demory farm site`](analyses/farm-sensor-architecture-demory-farm-site.md), [`Sensor checklist matrix — Demory farm`](analyses/sensor-checklist-matrix-for-demory-farm.md).
- **Updated**: [`local-site-and-county-intelligence.md`](topics/local-site-and-county-intelligence.md) — Campbell County + Demory route map: same two pages.
- Validator: `uv run python scripts/validate_wiki.py --strict`.

## [2026-04-18] refactor | Usability / navigation audit + source-note Evidence summary pattern

- **New analysis**: [`usability-and-navigation-audit-2026-04-18.md`](analyses/usability-and-navigation-audit-2026-04-18.md) — navigation noise, hub strength, canonical vs supporting, source-note scanability; complements structural audits.
- **New concept**: [`source-note-abstract-and-evidence-pattern.md`](concepts/source-note-abstract-and-evidence-pattern.md) — optional **Evidence summary** block (abstract, authority mix, canonical links, key claims, open questions).
- **Routing**: [`overview.md`](overview.md) — **three-lane** entry table; [`index.md`](index.md) — **Reader lanes** blurb + audit/pattern links; [`start-here-smart-farm-wiki.md`](topics/start-here-smart-farm-wiki.md); [`wiki-navigation-and-structural-hubs.md`](topics/wiki-navigation-and-structural-hubs.md); [`evidence-grade-and-canonical-authority.md`](concepts/evidence-grade-and-canonical-authority.md) (See also).
- **Source-notes** (Evidence summary added): [`authoritative-execution-evidence-cluster-east-tennessee.md`](source-notes/authoritative-execution-evidence-cluster-east-tennessee.md), [`backup-dr-official-documentation-cluster.md`](source-notes/backup-dr-official-documentation-cluster.md), [`off-grid-power-rf-wan-source-index-demory-planning-2026-04.md`](source-notes/off-grid-power-rf-wan-source-index-demory-planning-2026-04.md), [`authoritative-roads-and-driveways-source-cluster.md`](source-notes/authoritative-roads-and-driveways-source-cluster.md), [`inbox-batch-2026-04-18-frigate-sops-prometheus-alertmanager-tenn811-nrcs-ut-extension.md`](source-notes/inbox-batch-2026-04-18-frigate-sops-prometheus-alertmanager-tenn811-nrcs-ut-extension.md).
- **Index hygiene** (validator): linked [`evidence-hardening-audit-east-tennessee-two-site-2026-04.md`](analyses/evidence-hardening-audit-east-tennessee-two-site-2026-04.md), [`observability-secrets-and-trust-bar-homelab-farm-edge.md`](analyses/observability-secrets-and-trust-bar-homelab-farm-edge.md), [`local-video-nvr-role-and-deferral-boundaries-farm-stack.md`](analyses/local-video-nvr-role-and-deferral-boundaries-farm-stack.md), [`grafana-alloy-official-documentation-primary-reference.md`](source-notes/grafana-alloy-official-documentation-primary-reference.md), [`tennessee-two-site-official-parcel-gis-flood-climate-portals.md`](source-notes/tennessee-two-site-official-parcel-gis-flood-climate-portals.md); restored portal → evidence-hardening link.
- Validator: `uv run python scripts/validate_wiki.py --strict`.

## [2026-04-25] ingest | Inbox — Frigate, SOPS, Prometheus, TN811, NRCS/UT PDFs

- **Moved** `raw/inbox/*.md` → `raw/processed/2026/*-capture-inbox-2026-04-18.md` (Frigate intro/config; Flux+SOPS guide; SOPS readme; Prometheus **Alertmanager** overview + configuration; TN811 home + before-you-dig; NRCS CPS 614 hub page).
- **PDFs**: `7385.pdf` → NRCS NEH Part 652 *Irrigation Guide* (1997); `PB1541.pdf` / `PB1641.pdf` → UT Extension fence + livestock watering; **`scripts/pdf_to_markdown.py`** extracts beside each PDF.
- **Source-note**: [`inbox-batch-2026-04-18-frigate-sops-prometheus-alertmanager-tenn811-nrcs-ut-extension.md`](source-notes/inbox-batch-2026-04-18-frigate-sops-prometheus-alertmanager-tenn811-nrcs-ut-extension.md).
- **Cross-links**: [`authoritative-execution-evidence-cluster-east-tennessee.md`](source-notes/authoritative-execution-evidence-cluster-east-tennessee.md); [`platform-doctrine-package-homelab-farm-edge.md`](topics/platform-doctrine-package-homelab-farm-edge.md); [`secrets-and-certificates-edge-cluster-standard.md`](analyses/secrets-and-certificates-edge-cluster-standard.md); [`monitoring-and-logging-expectations-edge-cluster-standard.md`](analyses/monitoring-and-logging-expectations-edge-cluster-standard.md); [`k3s-longhorn-rancher-pi-platform-official-captures-inbox-2026-04-18.md`](source-notes/k3s-longhorn-rancher-pi-platform-official-captures-inbox-2026-04-18.md); [`local-site-and-county-intelligence.md`](topics/local-site-and-county-intelligence.md); [`index.md`](index.md).
- Validator: `uv run python scripts/validate_wiki.py --strict`.

## [2026-04-25] refactor | Evidence hardening pass — desk portals, observability doctrine, video deferral

- **Audit**: [`evidence-hardening-audit-east-tennessee-two-site-2026-04.md`](analyses/evidence-hardening-audit-east-tennessee-two-site-2026-04.md) — what was added, remaining gaps, canonical changelog.
- **Source-notes**: [`tennessee-two-site-official-parcel-gis-flood-climate-portals.md`](source-notes/tennessee-two-site-official-parcel-gis-flood-climate-portals.md); [`grafana-alloy-official-documentation-primary-reference.md`](source-notes/grafana-alloy-official-documentation-primary-reference.md).
- **Doctrine / policy**: [`observability-secrets-and-trust-bar-homelab-farm-edge.md`](analyses/observability-secrets-and-trust-bar-homelab-farm-edge.md); [`local-video-nvr-role-and-deferral-boundaries-farm-stack.md`](analyses/local-video-nvr-role-and-deferral-boundaries-farm-stack.md).
- **Hubs / packages updated** (routing): [`local-evidence-package-east-tennessee-two-site.md`](topics/local-evidence-package-east-tennessee-two-site.md), [`parcel-intelligence-package-east-tennessee-two-site.md`](topics/parcel-intelligence-package-east-tennessee-two-site.md), [`parcel-evidence-intake-and-validation-workflow-east-tennessee-two-site.md`](analyses/parcel-evidence-intake-and-validation-workflow-east-tennessee-two-site.md), [`infrastructure-inventory-baseline-two-sites-east-tennessee.md`](analyses/infrastructure-inventory-baseline-two-sites-east-tennessee.md), [`claxton-home-base-site-intelligence.md`](analyses/claxton-home-base-site-intelligence.md), [`demory-farm-site-intelligence.md`](analyses/demory-farm-site-intelligence.md), [`field-observation-template-package-east-tennessee-two-site.md`](topics/field-observation-template-package-east-tennessee-two-site.md), [`operational-standards-farm-homelab-platform.md`](topics/operational-standards-farm-homelab-platform.md), [`platform-doctrine-package-homelab-farm-edge.md`](topics/platform-doctrine-package-homelab-farm-edge.md), [`reference-architecture-5ac-homebase-120ac-smart-farm.md`](analyses/reference-architecture-5ac-homebase-120ac-smart-farm.md), [`remote-access-operational-security-model-two-site-smart-farm.md`](analyses/remote-access-operational-security-model-two-site-smart-farm.md), [`domain-content-overview.md`](analyses/domain-content-overview.md), [`wiki-navigation-and-structural-hubs.md`](topics/wiki-navigation-and-structural-hubs.md), [`authoritative-execution-evidence-cluster-east-tennessee.md`](source-notes/authoritative-execution-evidence-cluster-east-tennessee.md), [`index.md`](index.md).
- Validator: `uv run python scripts/validate_wiki.py --strict`; docs: `uv run mkdocs build`.

## [2026-04-25] policy | Source-note Evidence summaries + structural vs integration validation (chronology note)

- **Chronology (no rewrite of prior entries)**: **[2026-04-18]** *Usability / navigation audit* — reader lanes, hub tables, **Evidence summary** pattern introduced on **initial** cluster notes. **[2026-04-25]** *Evidence hardening pass* — desk **portal** URLs, observability **doctrine**, **video** deferral, canonical **site/infra** routing. **This entry** — `AGENTS.md` + `docs/operations/*` now **encode** activation, Evidence summaries, **when** matrices/guides/standards attach, and **structural** (CI) vs **integration** (policy) validation so future work does not **partially adopt** by accident.
- **Updated policy / operator docs**: [`AGENTS.md`](../AGENTS.md); [`agent-maintenance.md`](../docs/operations/agent-maintenance.md); [`validation.md`](../docs/operations/validation.md); [`raw-corpus-and-publishing.md`](../docs/operations/raw-corpus-and-publishing.md); [`publishing.md`](../docs/operations/publishing.md); [`obsidian.md`](../docs/operations/obsidian.md).
- **Evidence summaries added** (high-value clusters): [`demory-farm-sensor-layer-official-and-operator-source-cluster.md`](source-notes/demory-farm-sensor-layer-official-and-operator-source-cluster.md), [`tennessee-two-site-official-parcel-gis-flood-climate-portals.md`](source-notes/tennessee-two-site-official-parcel-gis-flood-climate-portals.md), [`electrical-networking-starlink-inbox-batch-2026-04-23.md`](source-notes/electrical-networking-starlink-inbox-batch-2026-04-23.md), [`inbox-batch-2026-04-18-tennessee-farm-lorawan-chirpstack-meshtastic-decentlab-halow.md`](source-notes/inbox-batch-2026-04-18-tennessee-farm-lorawan-chirpstack-meshtastic-decentlab-halow.md), [`k3s-longhorn-rancher-pi-platform-official-captures-inbox-2026-04-18.md`](source-notes/k3s-longhorn-rancher-pi-platform-official-captures-inbox-2026-04-18.md), [`grafana-alloy-official-documentation-primary-reference.md`](source-notes/grafana-alloy-official-documentation-primary-reference.md); [`source-note-abstract-and-evidence-pattern.md`](concepts/source-note-abstract-and-evidence-pattern.md) examples list extended.
- **Package routing**: [`east-tennessee-two-site-farm-business-plan.md`](business-plan/east-tennessee-two-site-farm-business-plan.md), [`local-evidence-package-east-tennessee-two-site.md`](topics/local-evidence-package-east-tennessee-two-site.md), [`backup-disaster-recovery-doctrine-hub.md`](topics/backup-disaster-recovery-doctrine-hub.md), [`procedural-guides-package-strategy-smart-farm-wiki.md`](topics/procedural-guides-package-strategy-smart-farm-wiki.md), [`two-site-smart-farm-operations.md`](topics/two-site-smart-farm-operations.md); [`index.md`](index.md) reader lane.
- Validator: `uv run python scripts/validate_wiki.py --strict`; MkDocs: `uv run mkdocs build`.

## [2026-04-25] refactor | Package-completion pass — hub integration language + artifact backlog

- **New analysis (durable backlog)**: [`package-artifact-backlog-canonical-packages-east-tennessee.md`](analyses/package-artifact-backlog-canonical-packages-east-tennessee.md) — ranked **matrix / standard / runbook / checklist** gaps; **Evidence summary** queue (homelab backup, farmOS, WSS, CISA, NRCS FY25); **spot-check** table for existing standards/runbooks.
- **Hub integration / boundary** updates: [`off-grid-power-and-field-networking-hub.md`](topics/off-grid-power-and-field-networking-hub.md), [`off-grid-systems-doctrine-package-demory-farm-site.md`](topics/off-grid-systems-doctrine-package-demory-farm-site.md), [`platform-doctrine-package-homelab-farm-edge.md`](topics/platform-doctrine-package-homelab-farm-edge.md), [`parcel-intelligence-package-east-tennessee-two-site.md`](topics/parcel-intelligence-package-east-tennessee-two-site.md), [`local-evidence-package-east-tennessee-two-site.md`](topics/local-evidence-package-east-tennessee-two-site.md); [`field-telemetry-reference-architecture-homestead-120ac.md`](analyses/field-telemetry-reference-architecture-homestead-120ac.md) (sensors / telemetry **router** alignment).
- **Routing**: [`wiki-navigation-and-structural-hubs.md`](topics/wiki-navigation-and-structural-hubs.md); [`index.md`](index.md) (overview + analyses catalog).
- Validator: `uv run python scripts/validate_wiki.py --strict`; `uv run mkdocs build --strict`.

## [2026-04-17] query | Sub-GHz field networking — single-file synthesis

- **New topic**: [`subghz-field-networking-synthesis.md`](topics/subghz-field-networking-synthesis.md) — One-page map: scope (LoRa/LoRaWAN/Meshtastic/HaLow), WAN vs field RF, reader goals, comparisons, analyses, entities, standards, source clusters, runbooks; does not replace canonical doctrine pages.
- **Routing**: [`index.md`](index.md) (Topics); [`off-grid-power-and-field-networking-hub.md`](topics/off-grid-power-and-field-networking-hub.md); [`field-network-iot-comparisons.md`](topics/field-network-iot-comparisons.md) Related; [`wiki-navigation-and-structural-hubs.md`](topics/wiki-navigation-and-structural-hubs.md) (Off-grid systems table).

## [2026-04-17] ingest | Evidence surfacing pass — raw corpus audit + Evidence summaries + AGENTS

- **New analysis**: [`raw-corpus-evidence-surfacing-audit-2026.md`](analyses/raw-corpus-evidence-surfacing-audit-2026.md) — `raw/processed/2026/` (~449 files) vs wiki synthesis by theme; prioritized backlog (no per-file spam).
- **Evidence summaries added/standardized**: [`homelab-backup-stack-official-captures-inbox-2026-04-18.md`](source-notes/homelab-backup-stack-official-captures-inbox-2026-04-18.md), [`farmos-documentation-captures-inbox-2026-04-18.md`](source-notes/farmos-documentation-captures-inbox-2026-04-18.md), [`postgresql-and-postgis-official-documentation-primary-cluster.md`](source-notes/postgresql-and-postgis-official-documentation-primary-cluster.md), [`homelab-edge-networking-inbox-batch-2026-04-18.md`](source-notes/homelab-edge-networking-inbox-batch-2026-04-18.md).
- **Policy**: [`AGENTS.md`](../AGENTS.md) — new **Capture, activation, and summarization** subsection; ingest steps **4–6** reunited under **Ingest** (append log, index, validate).
- **Routing**: [`overview.md`](overview.md), [`index.md`](index.md) (Overview + Analyses), [`wiki-navigation-and-structural-hubs.md`](topics/wiki-navigation-and-structural-hubs.md), [`platform-doctrine-package-homelab-farm-edge.md`](topics/platform-doctrine-package-homelab-farm-edge.md), [`farm-data-farmos-and-ag-lab-builds.md`](topics/farm-data-farmos-and-ag-lab-builds.md), [`domain-content-overview.md`](analyses/domain-content-overview.md) (gaps bullet); [`source-note-abstract-and-evidence-pattern.md`](concepts/source-note-abstract-and-evidence-pattern.md) examples + See also.
- Validator: `uv run python scripts/validate_wiki.py --strict`; `uv run mkdocs build --strict`.

## [2026-04-18] ingest | Inbox — TWRA hunting regulations, licenses, third-party season guide, Remington captures

- **Moved** eight `raw/inbox/*.md` files → `raw/processed/2026/` with **kebab-case** basenames (`twra-*`, `tennessee-hunting-season-guide-third-party-*`, `remington-*`).
- **Source-note**: [`twra-tennessee-hunting-regulations-inbox-batch-2026-04-18.md`](source-notes/twra-tennessee-hunting-regulations-inbox-batch-2026-04-18.md) — Evidence summary + `source_ids` table (TWRA-heavy batch; blog + gun pages labeled **lower authority**).
- **Cross-links**: [`authoritative-execution-evidence-cluster-east-tennessee.md`](source-notes/authoritative-execution-evidence-cluster-east-tennessee.md) (TN tax table row); [`tennessee-hobby-farm-and-small-farm-business-sources.md`](topics/tennessee-hobby-farm-and-small-farm-business-sources.md); [`index.md`](index.md).
- Validator: `uv run python scripts/validate_wiki.py --strict`.

## [2026-04-19] ingest | American ginseng — VCE PDF, web captures, seed-start analysis

- **Moved** five `raw/inbox/*.md` + `2011ginsengforest.pdf` → `raw/processed/2026/` (**kebab-case**); **`scripts/pdf_to_markdown.py`** → `2011-ginseng-forest-farming-guide-usda-fs-ne-region-capture-inbox-2026-04-19-extracted.md` beside canonical PDF.
- **Source-note**: [`american-ginseng-seed-forest-culture-sources-inbox-batch-2026-04-19.md`](source-notes/american-ginseng-seed-forest-culture-sources-inbox-batch-2026-04-19.md) — Evidence summary + provenance tables (**VCE 354-313** + vendor / NGO / popular captures).
- **Analysis** (`page_subtype` **operational_guide**): [`american-ginseng-from-seed-asap-start-plan.md`](analyses/american-ginseng-from-seed-asap-start-plan.md) — **Start-ASAP** phased plan (fall planting window, site screen, establishment); **TN legal** deferral.
- **Cross-links**: [`authoritative-execution-evidence-cluster-east-tennessee.md`](source-notes/authoritative-execution-evidence-cluster-east-tennessee.md); [`sustainable-cropping-soil-and-farm-entry-sources.md`](topics/sustainable-cropping-soil-and-farm-entry-sources.md); [`domain-content-overview.md`](analyses/domain-content-overview.md); [`index.md`](index.md).
- Validator: `uv run python scripts/validate_wiki.py --strict`.

## [2026-04-19] ingest | Tennessee ginseng — TDEC program, MTSU wild-simulated PDF, dealer list, UT notes

- **Moved** nine `raw/inbox` drops → `raw/processed/2026/` (**kebab-case**): **TDEC** program page + **UT Crops** ginseng capture + **Smart Yards** profile + Wilson County MG article + Appalachia article + four **PDFs** (2018 Andrea regulation deck, **2025** certified dealer list, TDEC brochure, **MTSU/TSU/UT** wild-simulated production guide).
- **`scripts/pdf_to_markdown.py`** on each PDF → sibling **`*-extracted.md`** (brochure extract **empty** / image-heavy).
- **Updated cluster**: [`american-ginseng-seed-forest-culture-sources-inbox-batch-2026-04-19.md`](source-notes/american-ginseng-seed-forest-culture-sources-inbox-batch-2026-04-19.md) — TN tables + `source_ids` expansion.
- **Updated analysis**: [`american-ginseng-from-seed-asap-start-plan.md`](analyses/american-ginseng-from-seed-asap-start-plan.md) — **TDEC** harvest/dealer gates, **MTSU-region** seed/soil protocol hooks, **UT** N guidance; **no** dealer-table **PII** in wiki body.
- **Cross-links**: [`authoritative-execution-evidence-cluster-east-tennessee.md`](source-notes/authoritative-execution-evidence-cluster-east-tennessee.md); [`index.md`](index.md).
- Validator: `uv run python scripts/validate_wiki.py --strict`.

## [2026-04-20] ingest | American ginseng — PDF-heavy batch + three operational guides

- **Moved** 19 **PDFs** + 10 **markdown** captures from `raw/inbox/` → `raw/processed/2026/`; **`pdf_to_markdown.py`** on each PDF (planter comparison + some pages **image-only** in extracts).
- **Source-note**: [`american-ginseng-pdf-heavy-inbox-batch-2026-04-20.md`](source-notes/american-ginseng-pdf-heavy-inbox-batch-2026-04-20.md) — themed tables + `source_ids`.
- **New analyses** (`operational_guide`): [`american-ginseng-site-evaluation-and-materials-checklist.md`](analyses/american-ginseng-site-evaluation-and-materials-checklist.md), [`american-ginseng-planting-and-cultivation-guide.md`](analyses/american-ginseng-planting-and-cultivation-guide.md), [`american-ginseng-woodlot-maintenance-remote-security-and-trail-cameras.md`](analyses/american-ginseng-woodlot-maintenance-remote-security-and-trail-cameras.md) (trail-camera **Phase 0** + **Frigate** deferral pointers).
- **Updated**: [`american-ginseng-from-seed-asap-start-plan.md`](analyses/american-ginseng-from-seed-asap-start-plan.md) (**four-part suite** link); [`american-ginseng-seed-forest-culture-sources-inbox-batch-2026-04-19.md`](source-notes/american-ginseng-seed-forest-culture-sources-inbox-batch-2026-04-19.md); [`authoritative-execution-evidence-cluster-east-tennessee.md`](source-notes/authoritative-execution-evidence-cluster-east-tennessee.md); [`sustainable-cropping-soil-and-farm-entry-sources.md`](topics/sustainable-cropping-soil-and-farm-entry-sources.md); [`index.md`](index.md).
- Validator: `uv run python scripts/validate_wiki.py --strict`.

## [2026-04-20] ingest | SX1302 — Waveshare HAT captures, Lora-net sx1302_hal readme

- **Moved** three `raw/inbox/*.md` → `raw/processed/2026/` (**kebab-case**): `lora-net-sx1302-hal-readme-packet-forwarder-tools.md`, `waveshare-sx1302-lorawan-gateway-hat-wiki.md`, `waveshare-sx1302-lorawan-gateway-hat-product-page-eu868-gnss.md`.
- **Source-note**: [`sx1302-waveshare-hat-and-lora-net-sx1302-hal-inbox-2026-04-20.md`](source-notes/sx1302-waveshare-hat-and-lora-net-sx1302-hal-inbox-2026-04-20.md) — **Evidence summary** + **per-source ingest descriptions** (table).
- **Hub**: [`smart-agriculture-meshtastic-and-lorawan.md`](topics/smart-agriculture-meshtastic-and-lorawan.md); [`demory-farm-sensor-layer-official-and-operator-source-cluster.md`](source-notes/demory-farm-sensor-layer-official-and-operator-source-cluster.md) (**ChirpStack** § gateway chip pointer); [`index.md`](index.md).
- **Policy**: [`AGENTS.md`](../AGENTS.md) **Ingest** step 2 — explicit **ingest descriptions** requirement.
- Validator: `uv run python scripts/validate_wiki.py --strict`.

## [2026-04-20] ingest | Raw processed 2026 summary-gap cleanup

- **Audit ledger**: `PROCESSED-CHECKLIST.md` at repository root (optional local scratch; not tracked) — deterministic checklist of `raw/processed/2026/` files that lacked any explicit wiki summary text at review time.
- **Source-note updated**: [`electrical-networking-starlink-inbox-batch-2026-04-23.md`](source-notes/electrical-networking-starlink-inbox-batch-2026-04-23.md) — added **per-source descriptions** for the 14 previously unmentioned 2026-04-23 files (Victron wiring chapters plus Starlink/farm-networking supporting captures).
- **Activation decision**: kept this work as **source-note + deferred follow-up note** rather than spawning new standalone notes because the gap set was a single batch already routed from canonical WAN/off-grid pages.
- Validator: `uv run python scripts/validate_wiki.py`.

## [2026-04-21] ingest | Pig raising — homestead inbox batch (blog, Reddit, permaculture)

- **Moved** three `raw/inbox/*.md` → `raw/processed/2026/`: `how-to-raise-pigs-naturally-timber-creek-farmer-inbox-2026-04-21.md`, `general-pig-raising-advice-reddit-homestead-inbox-2026-04-21.md`, `raising-pigs-for-beginners-abundant-permaculture-inbox-2026-04-21.md`.
- **Source-note** (batch + **Evidence summary**): [`pig-raising-homestead-inbox-batch-2026-04-21.md`](source-notes/pig-raising-homestead-inbox-batch-2026-04-21.md).
- **Synthesis** (`operational_guide`, **draft** maturity): [`raising-pigs-small-scale-homestead-guide.md`](analyses/raising-pigs-small-scale-homestead-guide.md).
- **Routing**: [`backyard-livestock-and-homestead-animals.md`](topics/backyard-livestock-and-homestead-animals.md), [`domain-content-overview.md`](analyses/domain-content-overview.md) (Strand A), [`farm-stocking-120-acres-vs-5-acres-research-prompt.md`](analyses/farm-stocking-120-acres-vs-5-acres-research-prompt.md), [`index.md`](index.md).
- Validator: `uv run python scripts/validate_wiki.py --strict`.

## [2026-04-26] ingest | Field verification program — Phase 0–1 (Claxton and Demory)

- **New** `operational_guide`: [`field-verification-program-phase-0-1-claxton-demory.md`](analyses/field-verification-program-phase-0-1-claxton-demory.md) — checklist tables (site, method, evidence, gates, desktop vs field) for walks, access/roads, drainage, utilities, power/loads, sensor pilots, gateway/controller validation, buildability/septic/permits; **no invented results**.
- **Routing**: [`local-evidence-package-east-tennessee-two-site.md`](topics/local-evidence-package-east-tennessee-two-site.md), [`parcel-evidence-intake-and-validation-workflow-east-tennessee-two-site.md`](analyses/parcel-evidence-intake-and-validation-workflow-east-tennessee-two-site.md), [`claxton-and-demory-missing-data-register.md`](analyses/claxton-and-demory-missing-data-register.md) (§9 map), [`execution-dossier-hub-phase-0-1-east-tennessee.md`](analyses/execution-dossier-hub-phase-0-1-east-tennessee.md), [`field-observation-template-package-east-tennessee-two-site.md`](topics/field-observation-template-package-east-tennessee-two-site.md), [`index.md`](index.md).
- Validator: `uv run python scripts/validate_wiki.py --strict`.

## [2026-04-27] refactor | East Tennessee two-site business plan — doctrine integration pass

- **New** `meta_audit`: [`east-tennessee-two-site-farm-business-plan-integration-revision-audit-2026-04.md`](analyses/east-tennessee-two-site-farm-business-plan-integration-revision-audit-2026-04.md) — material deltas vs local evidence, off-grid/WAN, sensors, platform/backup/DR, observability trust bar, evidence authority; pages touched; strengthened vs blocked assumptions; **R16** risk.
- **Package + chapters**: [`east-tennessee-two-site-farm-business-plan.md`](business-plan/east-tennessee-two-site-farm-business-plan.md) (**What changed** block), planning framework, vision, two-site operating context, enterprise options, recommended strategy, labor, smart-tech, capital, revenue, risk register, roadmap, validation backlog, remediation, executive summary; **execution**: decision memo + dossier hub.
- **Hubs / index**: [`business-plan-execution-and-pilot-operations-hub.md`](topics/business-plan-execution-and-pilot-operations-hub.md), [`two-site-smart-farm-operations.md`](topics/two-site-smart-farm-operations.md), [`index.md`](index.md).
- Validator / docs: `uv run python scripts/validate_wiki.py --strict`; `uv run mkdocs build -q`.

## [2026-04-28] refactor | Execution gates — Phase 0–1 (East Tennessee two-site)

- **New** `operational_guide`: [`execution-gates-phase-0-1-east-tennessee-two-site.md`](analyses/execution-gates-phase-0-1-east-tennessee-two-site.md) — eight domain tables (local evidence, site/infra, off-grid power, connectivity + trust bar, sensors, platform/backup/observability, labor, financial) with pass/fail, pilot vs production, unlocks, blocked-if-fail; composite stance + V/G mapping.
- **Updated**: [`east-tennessee-two-site-farm-business-plan-validation-backlog.md`](analyses/east-tennessee-two-site-farm-business-plan-validation-backlog.md) (G1 production honesty + EG link), [`validation-backlog-before-major-spend-two-site-smart-farm.md`](analyses/validation-backlog-before-major-spend-two-site-smart-farm.md), [`execution-dossier-hub-phase-0-1-east-tennessee.md`](analyses/execution-dossier-hub-phase-0-1-east-tennessee.md), [`execution-dossier-decision-memo-phase-0-1-east-tennessee.md`](analyses/execution-dossier-decision-memo-phase-0-1-east-tennessee.md), [`east-tennessee-two-site-farm-business-plan-remediation-backlog.md`](analyses/east-tennessee-two-site-farm-business-plan-remediation-backlog.md), [`execution-readiness-gap-audit-east-tennessee-operational-knowledge.md`](analyses/execution-readiness-gap-audit-east-tennessee-operational-knowledge.md), [`east-tennessee-two-site-farm-business-plan-executive-summary.md`](analyses/east-tennessee-two-site-farm-business-plan-executive-summary.md), [`east-tennessee-two-site-farm-business-plan-10-year-roadmap.md`](analyses/east-tennessee-two-site-farm-business-plan-10-year-roadmap.md), [`east-tennessee-two-site-farm-business-plan-framework.md`](analyses/east-tennessee-two-site-farm-business-plan-framework.md), [`east-tennessee-two-site-farm-business-plan-integration-revision-audit-2026-04.md`](analyses/east-tennessee-two-site-farm-business-plan-integration-revision-audit-2026-04.md), [`east-tennessee-two-site-farm-business-plan-vision-and-constraints.md`](analyses/east-tennessee-two-site-farm-business-plan-vision-and-constraints.md); package + execution hubs + [`index.md`](index.md).
- Validator: `uv run python scripts/validate_wiki.py --strict`.

## [2026-04-29] query | Phase 0–1 hostile operator-burden review (East Tennessee two-site)

- **New** `query_synthesis`: [`phase-0-1-operator-burden-review-east-tennessee-two-site.md`](analyses/phase-0-1-operator-burden-review-east-tennessee-two-site.md) — burden lenses, recurring/surge/invisible classes, master burden table (severity, who, mitigation, defer/simplify/automate/outsource), skeptical verdict.
- **Updated**: [`east-tennessee-two-site-farm-business-plan-labor-and-family-model.md`](analyses/east-tennessee-two-site-farm-business-plan-labor-and-family-model.md), [`east-tennessee-two-site-farm-business-plan-risk-register.md`](analyses/east-tennessee-two-site-farm-business-plan-risk-register.md) (**R17**), [`observability-secrets-and-trust-bar-homelab-farm-edge.md`](analyses/observability-secrets-and-trust-bar-homelab-farm-edge.md), [`automation-stop-rules-two-site-smart-farm.md`](analyses/automation-stop-rules-two-site-smart-farm.md), [`execution-gates-phase-0-1-east-tennessee-two-site.md`](analyses/execution-gates-phase-0-1-east-tennessee-two-site.md), [`business-plan-execution-and-pilot-operations-hub.md`](topics/business-plan-execution-and-pilot-operations-hub.md), [`index.md`](index.md).
- Validator: `uv run python scripts/validate_wiki.py --strict`.

## [2026-04-30] refactor | First 90 days — operator packet (East Tennessee two-site)

- **New** `operational_guide`: [`first-90-days-operator-packet-east-tennessee-two-site.md`](analyses/first-90-days-operator-packet-east-tennessee-two-site.md) — weeks **1–12** priorities, field verification bundling, infra/sensor/platform caps, documentation updates, stop conditions, evidence **30/60/90**, decision checkpoints (**pilot** stance vs memo **Forbidden**).
- **Updated**: [`execution-first-90-days-phase-0-1-east-tennessee.md`](analyses/execution-first-90-days-phase-0-1-east-tennessee.md), [`execution-dossier-hub-phase-0-1-east-tennessee.md`](analyses/execution-dossier-hub-phase-0-1-east-tennessee.md), [`execution-dossier-decision-memo-phase-0-1-east-tennessee.md`](analyses/execution-dossier-decision-memo-phase-0-1-east-tennessee.md), [`execution-dossier-master-checklist-phase-0-1-east-tennessee.md`](analyses/execution-dossier-master-checklist-phase-0-1-east-tennessee.md), [`field-verification-program-phase-0-1-claxton-demory.md`](analyses/field-verification-program-phase-0-1-claxton-demory.md), [`execution-gates-phase-0-1-east-tennessee-two-site.md`](analyses/execution-gates-phase-0-1-east-tennessee-two-site.md), [`east-tennessee-two-site-farm-business-plan.md`](business-plan/east-tennessee-two-site-farm-business-plan.md), [`business-plan-execution-and-pilot-operations-hub.md`](topics/business-plan-execution-and-pilot-operations-hub.md), [`index.md`](index.md).
- Validator: `uv run python scripts/validate_wiki.py --strict`.
