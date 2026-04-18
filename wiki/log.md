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

