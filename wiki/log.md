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

