# Wiki index

First-stop navigation for humans and agents. Every **intentional** wiki page should appear here unless it is intentionally transient (rare); orphans are reported by `scripts/validate_wiki.py`.

## Overview

- [Wiki overview](overview.md) — North-star summary of this vault’s purpose and rules.
- [Repository analysis](analyses/repository-analysis.md) — This repo’s layout, tooling, CI, corpus scale, and design tradeoffs (meta; complements `docs/`).
- [Domain content overview](analyses/domain-content-overview.md) — What this wiki is *about*: land, connectivity, power, data, business, and time/PNT strands.

## Entities

- [Example Organization](entities/example-org.md) — Fictional org used to demonstrate entity pages.

## Concepts

- [Smart Farm Wiki — mission, audience, and voice](concepts/smart-farm-wiki-mission-and-values.md) — Mission statement, vision, values, and prose style; domain “why” (complements `AGENTS.md`).
- [LLM Wiki pattern](concepts/llm-wiki-pattern.md) — Core ideas: raw vs wiki, synthesis, maintenance.
- [Decentralized physical infrastructure networks (DePIN)](concepts/depin.md) — Token-incentivized physical/digital infrastructure framing (see sources).
- [ESP32](concepts/esp32.md) — Espressif SoC family common in IoT, sensors, and displays.
- [LoRa (radio)](concepts/lora-radio.md) — LoRa PHY vs LoRaWAN and mesh stacks.
- [LoRaWAN](concepts/lorawan.md) — LPWAN stack for long-range sensors; common in farm IoT backhaul framing.
- [Meshtastic](concepts/meshtastic.md) — LoRa mesh firmware for off-grid comms and field nodes.
- [Network Time Protocol (NTP)](concepts/network-time-protocol.md) — Clock sync over IP; typical ms-scale for general hosts.
- [Precision agriculture](concepts/precision-agriculture.md) — Data-driven field management concept (Wikipedia-sourced note).
- [Precision Time Protocol (PTP)](concepts/precision-time-protocol.md) — IEEE 1588 clock sync; hardware timestamping for tight discipline.
- [Wi-Fi HaLow](concepts/wi-fi-halow.md) — IEEE 802.11ah sub-GHz Wi‑Fi for IoT range/power tradeoffs.

## Topics

- [Knowledge synthesis](topics/knowledge-synthesis.md) — Cross-cutting theme for how conclusions are built here.
- [Agritourism, tiny housing, and natural building sources](topics/agritourism-tiny-housing-and-natural-building.md) — Farm stays, natural building, agritourism listicles, news excerpts.
- [Tennessee hobby farm and small-farm business sources](topics/tennessee-hobby-farm-and-small-farm-business-sources.md) — Hobby-farm primers, TN business guides, USDA BFR, revenue/licensing excerpts, startup PDFs.
- [Backyard livestock and homestead animal sources](topics/backyard-livestock-and-homestead-animals.md) — Poultry/cattle guides, AI husbandry marketing, PDF papers.
- [ESP32, ESPHome, and smart-farming builds](topics/esp32-iot-smart-farming-and-tooling.md) — MCU guides, smart-farming firmware README, ESPHome CYD.
- [Docker, Kubernetes, Compose, and Bake (edge and homelab)](topics/docker-kubernetes-compose-and-bake.md) — Compose, Bake, k3s/RKE2, distro comparisons for self-hosted stacks.
- [Farm data, farmOS, and agriculture lab builds](topics/farm-data-farmos-and-ag-lab-builds.md) — farmOS (Drupal), ag-lab automation thread, sensor integration hints.
- [Field network IoT comparisons (HaLow, LoRa, NB-IoT)](topics/field-network-iot-comparisons.md) — Comparative articles on LPWAN / HaLow / cellular IoT.
- [LoRa, MQTT, and gateway bridges](topics/lora-mqtt-and-gateway-bridges.md) — LoRaWAN app MQTT, OpenMQTTGateway, DIY gateways, Meshtastic MQTT thread, HA LoRa exploration.
- [Homestead and regional gardening sources](topics/homestead-and-regional-gardening-sources.md) — Small-farm book import and Tennessee gardening guide.
- [Homelab, self-hosting, and edge narratives](topics/homelab-self-hosting-and-edge-narratives.md) — Homelab guides, Reddit threads, AI architecture, partial solar rack.
- [Off-grid solar power and storage (special topic)](topics/off-grid-solar-power-and-storage.md) — PV, charge control, battery sizing: homestead, off-grid homes, field power.
- [Ponds, water features, and homestead hydrology](topics/ponds-water-features-and-homestead-hydrology.md) — DIY ponds, biofilters, farm ponds, fountains, pumping.
- [Position, navigation, and timing alternatives](topics/position-navigation-and-timing-alternatives.md) — BPS, LORAN, resilient trackers beyond GPS.
- [Smart agriculture, Meshtastic, and LoRaWAN](topics/smart-agriculture-meshtastic-and-lorawan.md) — Field networks: precision-ag LoRaWAN vs Meshtastic mesh deployments.
- [Sustainable cropping, soil, and farm entry sources](topics/sustainable-cropping-soil-and-farm-entry-sources.md) — Rotations, cover crops, SARE, TN beginning-farmer links.
- [Smart home — Matter, Thread, and Home Assistant AI (special topic)](topics/smart-home-matter-thread-and-home-assistant-ai.md) — Matter/Thread interoperability and HA AI tooling.
- [Smart mirror and e-paper display builds](topics/smart-mirror-and-e-paper-displays.md) — MagicMirror² ecosystem + E Ink survey.
- [Time synchronization — NTP and PTP sources](topics/time-synchronization-ntp-and-ptp.md) — NTP/PTP references, GNSS-disciplined Pi clocks, Time Pi Ansible, forums.

## Source notes

- [Example LLM Wiki note (raw)](source-notes/example-llm-wiki-note.md) — Grounding note for `raw/processed/2026/example-llm-wiki-note.md`.
- [Backyard ponds — farm waterfall forum (short)](source-notes/backyard-ponds-farm-waterfall-forum-short.md) — Liner/stone/waterfall tips fragment.
- [Beginning farmer resources (TN + USDA)](source-notes/beginning-farmer-resources-list.md) — Link hub for programs and manuals.
- [Cover crops — sustainable rotations (article)](source-notes/cover-crops-sustainable-crop-rotations.md) — SARE-style cover crop piece.
- [Cover crops — sustainable rotations (PDF)](source-notes/cover-crops-sustainable-crop-rotations-pdf.md) — Large PDF companion; confirm metadata inside.
- [Crop rotations overview](source-notes/crop-rotations-overview.md) — Rodale-style soil health explainer.
- [Cultivating the Future — sustainable farming](source-notes/cultivating-the-future-sustainable-farming-deep-dive.md) — Essay capture.
- [13 tips — starting a hobby farm (AgAmerica)](source-notes/agamerica-13-tips-starting-hobby-farm.md) — Zoning, plan, fencing, mindset checklist.
- [Beginning farmers and ranchers (USDA farmers.gov)](source-notes/beginning-farmers-and-ranchers-usda-farmers-gov.md) — BFR coordinators, programs entry.
- [How to start a hobby farm — beginner's guide (KW Land)](source-notes/kw-land-how-to-start-hobby-farm-beginners-guide.md) — Hobby vs commercial framing, pros/cons.
- [What's a hobby farm? (Land.com)](source-notes/land-com-whats-a-hobby-farm-guide.md) — Definition, USDA small-farm stats, time/cost reality.
- [newbusiness-checklist (PDF)](source-notes/newbusiness-checklist-pdf.md) — Checklist PDF import; confirm inside PDF.
- [Shopify — start a business in TN (10 steps, 2025)](source-notes/shopify-how-to-start-business-tennessee-10-steps-2025.md) — TN startup outline; not legal advice.
- [TN business tax / TNTAP licensing excerpt](source-notes/tennessee-business-tax-registration-licensing-tntap.md) — Gross receipts, county license fee notes.
- [TN Smart Startup Guide (PDF)](source-notes/tn-smart-startup-guide-pdf.md) — Large TN startup PDF; confirm edition inside file.
- [Zarla — how to start a business in Tennessee](source-notes/zarla-how-to-start-business-in-tennessee.md) — Stepwise TN formation article.
- [ezcGman LoRa-to-MQTT gateway (ESP32, EByte)](source-notes/ezcgman-lora-to-mqtt-gateway-esp32-ebyte.md) — DIY gateway PCB + broker integration.
- [Home Assistant — LoRa long-range sensors / MQTT exploration](source-notes/home-assistant-lora-long-range-sensors-mqtt-exploration.md) — ESP32 SX1276 P2P LoRa to extend HA reach.
- [How to make water go uphill without electricity](source-notes/how-to-make-water-go-uphill-without-electricity.md) — Ram pumps, siphons, low-input lifts.
- [How to start farming with no money](source-notes/how-to-start-farming-with-no-money.md) — Bootstrap listicle capture.
- [Keeping your horse at home](source-notes/keeping-your-horse-at-home.md) — Small-farm horse basics.
- [Plant a fountain, dig a pond (Acreage Life)](source-notes/plant-a-fountain-dig-a-pond-acreage-life.md) — Farm pond sizing, liners, stocking, fountains.
- [Pump pond water uphill — hose bib irrigation (Reddit)](source-notes/pond-pump-uphill-hose-bib-irrigation-reddit.md) — Forum advice thread.
- [Pump water uphill](source-notes/pump-water-uphill.md) — Head/flow/pump primer.
- [Start farming — planning crop rotation (SARE)](source-notes/start-farming-planning-crop-rotation.md) — Rotation planning for new producers.
- [Sustainable food & agriculture investment (short)](source-notes/sustainable-food-agriculture-investment-deep-dive.md) — High-level investment excerpt.
- [Tyrant Farms — DIY pond + self-cleaning biofilter](source-notes/tyrant-farms-diy-backyard-pond-self-cleaning-biofilter.md) — Long build log, ecosystem + filtration.
- [Water features — origins and design (deep dive)](source-notes/water-features-origins-history-design.md) — History/design essay.
- [LoRaWAN + MQTT integration (HiveMQ article)](source-notes/lorawan-mqtt-integration-iot-application-design-hivemq.md) — App-server MQTT patterns, LPWAN constraints.
- [Meshtastic — LoRa ↔ MQTT (Reddit)](source-notes/meshtastic-lora-mqtt-bridge-reddit-thread.md) — Mesh/MQTT policy and 0-hop discussion.
- [MultiTech — MQTT messages / LoRa topics](source-notes/multitech-developer-resources-mqtt-messages-lora-topics.md) — `lora/<DEV-EUI>/...` broker topic reference.
- [MQTT Manager + LoRa poor-man gateway (Instructables)](source-notes/mqtt-manager-lora-poor-man-gateway-instructables.md) — Two ESP32 LoRa modules + MQTT Manager apps.
- [OpenMQTTGateway — Theengs LoRa gateway (v1.8.1)](source-notes/openmqttgateway-theengs-lora-gateway-v1-8-1.md) — Raw LoRa ↔ MQTT pub/sub, config via MQTT/WebUI.
- [7 homelab ideas — why you should have a homelab](source-notes/7-homelab-ideas-why-you-should-have-homelab.md) — Motivation and project ideas for a home lab.
- [Agriculture lab build (2023, r/homelab)](source-notes/agriculture-lab-build-2023-homelab-reddit.md) — Large automated ag lab; farmOS suggested in comments.
- [Build homelab if major is computing — Reddit](source-notes/build-homelab-if-major-computing-reddit.md) — Student-oriented motivation thread.
- [Building Compose projects with Bake](source-notes/building-compose-projects-with-bake.md) — Bake + Compose project wiring.
- [Deep dive — Docker Compose](source-notes/deep-dive-docker-compose.md) — Long single-topic Compose reference.
- [Deep dive — my home lab](source-notes/deep-dive-my-home-lab.md) — Personal inventory-style homelab tour.
- [Docker Bake — comprehensive guide](source-notes/docker-bake-comprehensive-guide.md) — buildx bake at scale.
- [Docker Compose in depth](source-notes/docker-compose-in-depth.md) — Mid-length Compose explainer.
- [farmOS overview (farmOS.org)](source-notes/farmos-overview-farmos-org.md) — Drupal-based farm management platform snapshot.
- [Home Assistant — 20 things wished I knew (installation)](source-notes/home-assistant-20-things-installation.md) — Installation pitfalls and tips listicle.
- [Homelab — AI life architecture deep dive](source-notes/homelab-runs-my-ai-life-architecture.md) — AI-centric homelab architecture article.
- [Homelab server — getting started (2026)](source-notes/homelab-server-getting-started-2026.md) — 2026-era homelab server guide.
- [Homelab underground culvert — Alaska off-grid](source-notes/homelab-underground-culvert-alaska-off-grid.md) — Extreme environment forum capture.
- [K3s or RKE2?](source-notes/k3s-or-rke2.md) — Short distro comparison.
- [Kubernetes distributions overview](source-notes/kubernetes-distributions-overview-kubeadm-k3s-microk8s-minikube-talos-rke2.md) — kubeadm, k3s, MicroK8s, Minikube, Talos, RKE2.
- [Mastering Docker Compose — multi-container apps](source-notes/mastering-docker-compose-multi-container-applications.md) — Practical multi-service Compose guide.
- [Partial solar homelab — EcoFlow](source-notes/partial-solar-homelab-ecoflow.md) — Rack load, stringing, UPS, Home Assistant energy UI.
- [r/homelab wiki — building a homelab](source-notes/rhomelab-wiki-guide-building-homelab.md) — Subreddit wiki capture.
- [RKE2 vs K3s — choosing a distribution](source-notes/rke2-vs-k3s-choosing-right-distribution.md) — Selection criteria and positioning.
- [What led you to homelab — Reddit](source-notes/what-led-you-to-homelab-reddit.md) — Origin-story community thread.
- [When to use K3s and RKE2](source-notes/when-to-use-k3s-and-rke2.md) — Scenario-oriented guidance.
- [5 steps — calculate ideal solar battery storage](source-notes/5-steps-calculate-ideal-solar-battery-storage.md) — Load inventory, daily Wh, autonomy, panel + battery sizing.
- [5 steps — design off-grid solar energy storage](source-notes/5-steps-design-off-grid-solar-energy-storage.md) — Off-grid solar + storage design workflow.
- [Complete off-grid solar system guide (2025)](source-notes/complete-off-grid-solar-system-guide-2025.md) — End-to-end off-grid solar overview.
- [Deep dive — home solar systems](source-notes/deep-dive-home-solar-systems.md) — Residential solar components and framing.
- [DIY off-grid solar — homestead wiring](source-notes/diy-off-grid-solar-homestead-wiring.md) — Practical install and balance-of-system emphasis.
- [EcoFlow power kits — off-grid deep dive](source-notes/ecoflow-power-kits-off-grid-deep-dive.md) — Integrated portable power-station ecosystem.
- [Home Assistant AI deep dive (HASS Podcast)](source-notes/home-assistant-ai-deep-dive-hasspodcast.md) — LLM vision, HACS, Ollama/LiteLLM, MCP-style tooling.
- [Sizing solar — off-grid field studies (Eosense-style)](source-notes/sizing-solar-off-grid-field-studies-eosense.md) — Remote field station loads, autonomy, SLA/AGM constraints.
- [Smart home — Matter and Thread deep dive (Part 1)](source-notes/smart-home-matter-thread-deep-dive-part-1.md) — Matter interoperability and Thread mesh roles.
- [Solar battery bank sizing calculator — off-grid](source-notes/solar-battery-bank-sizing-calculator-off-grid.md) — Ah/Wh, DoD, bank voltage calculator framing.
- [Building solar-powered Meshtastic community network](source-notes/building-solar-powered-meshtastic-community-network.md) — Solar sizing, Heltec/ESP32 power notes, repeater + sensor pairing.
- [How to build a solar Meshtastic node the easy way](source-notes/how-to-build-solar-meshtastic-node-easy-way.md) — Integrated solar node (ThinkNode M6) deployment guide.
- [Meshtastic nodes basics and deployment (Seeed)](source-notes/meshtastic-nodes-basics-deployment-seeed.md) — Roles, maps, range, solar kits vs DIY.
- [LoRaWAN farmers money and yields (TEKTELIC)](source-notes/lorawan-farmers-money-yields-tektelic.md) — Vendor overview of LoRaWAN in agriculture and case studies.
- [Semtech LoRa smart agriculture applications](source-notes/semtech-lora-smart-agriculture-applications.md) — Semtech marketing summary of LoRa/LoRaWAN ag use cases.
- [Solar Meshtastic GPS ESP32 outdoor](source-notes/solar-meshtastic-gps-esp32-outdoor.md) — Power envelopes and informal multi-node GPS query behavior.
- [Deep look Wi‑Fi HaLow vs LoRaWAN (Newracom)](source-notes/deep-look-wi-fi-halow-lorawan-newracom.md) — Vendor LPWAN comparison and claims.
- [Experimental HaLow vs LoRa smart grid (Sensors 2023)](source-notes/experimental-halow-lora-smart-grid-sensors.md) — Peer-reviewed field performance study.
- [Compare Wi‑Fi HaLow and LoRa (Morse Micro)](source-notes/compare-wi-fi-halow-lora-morse-micro.md) — Short vendor positioning piece.
- [DePIN Wikipedia excerpt](source-notes/depin-wikipedia.md) — Decentralized physical infrastructure snapshot.
- [Five Acres and Independence full text](source-notes/five-acres-and-independence-full-text.md) — Large historical small-farm guide import.
- [IEEE 802.11ah Wikipedia excerpt](source-notes/ieee-802-11ah-wikipedia.md) — Wi‑Fi HaLow standard overview tables.
- [Long-range internet over LoRa (Pi forums)](source-notes/long-range-internet-lora-raspberry-pi-forums.md) — Forum realism on LoRa throughput for “web” use.
- [LoRa Wikipedia excerpt](source-notes/lora-wikipedia.md) — LoRa PHY and LoRaWAN ecosystem overview.
- [Precision agriculture Wikipedia excerpt](source-notes/precision-agriculture-wikipedia.md) — PA definition and methods overview.
- [Wi‑Fi HaLow vs LoRaWAN (RAD)](source-notes/wifi-halow-vs-lorawan-rad.md) — Vendor comparison blog.
- [Wi‑Fi HaLow, LoRa, or NB‑IoT (WizzDev)](source-notes/wi-fi-halow-lora-nb-iot-wizzdev.md) — Three-way technology comparison.
- [Tennessee garden beginners (Willow Ridge)](source-notes/tennessee-garden-beginners-willow-ridge.md) — East TN seasonal planting guide.
- [AI animal husbandry (Ambiq)](source-notes/ai-animal-husbandry-ambiq.md) — Marketing survey of AI in livestock sectors.
- [Animals journal PDF (animals-14-01645)](source-notes/animals-journal-14-01645-pdf.md) — Peer-reviewed PDF import; confirm metadata in file.
- [Cheap Yellow Display ESPHome beginners](source-notes/esphome-yellow-display-beginners.md) — ESP32-2432S028 + Home Assistant YAML.
- [DIY PTP grandmaster Pi (Geerling)](source-notes/diy-ptp-grandmaster-pi-geerling.md) — Time Pi / TimeHAT stratum-1 NTP+PTP build.
- [ESP32 deep dive Medium](source-notes/esp32-series-deep-dive-medium.md) — ESP8266/32 family overview (may be paywalled).
- [ESP32 for IoT Nabto guide](source-notes/esp32-for-iot-nabto-guide.md) — Long vendor feature overview.
- [IJRAW journal PDF (ijraw-4-5-50.1)](source-notes/ijraw-journal-pdf-4-5-50-1.md) — Large PDF import; confirm title inside document.
- [Lily OSP smart farming ESP32 README](source-notes/lily-osp-smart-farming-esp32-readme.md) — Irrigation automation project documentation.
- [NTP Wikipedia excerpt](source-notes/network-time-protocol-wikipedia.md) — Network Time Protocol baseline article.
- [PTP explained NetworkLessons](source-notes/precision-time-protocol-explained-networklessons.md) — IEEE 1588 tutorial and profiles.
- [PTP Wikipedia excerpt](source-notes/precision-time-protocol-wikipedia.md) — Precision Time Protocol baseline article.
- [Pi 5 Ethernet PTP timestamping forums](source-notes/raspberry-pi-5-ptp-timestamping-forums.md) — Community discussion of HW PTP support.
- [Raising backyard chickens (Wine & Country Life)](source-notes/raising-backyard-chickens.md) — Starting an egg flock (regional article).
- [Raising cattle beginning farmers (Hobby Farms)](source-notes/raising-cattle-beginning-farmers-guide.md) — Fencing and small-scale beef framing.
- [Raising chickens for meat](source-notes/raising-chickens-for-meat.md) — Broiler quick-facts and grow-out basics.
- [Sustainable egg & meat flock (forum)](source-notes/sustainable-egg-meat-flock.md) — Dual-purpose flock planning thread.
- [ESP32 deep dive request (ESP32.com)](source-notes/tutorial-deep-dive-esp32-forum.md) — Forum ask for advanced Espressif training.
- [Homestead chickens eggs or meat](source-notes/what-to-know-raising-homestead-chickens.md) — Layers vs broilers vs dual-purpose.
- [BPS GPS alternative (Geerling)](source-notes/bps-gps-alternative-geerling.md) — ATSC 3.0 broadcast timing vs GPS PPS demo notes.
- [E Ink world technology and uses](source-notes/e-ink-world-technology-and-uses.md) — E-paper tech and applications survey.
- [geerlingguy/time-pi Ansible configuration](source-notes/geerlingguy-time-pi-ansible-configuration.md) — Stratum-1 Pi NTP/PTP repo README.
- [GNSS HAT setting time (Pi forums)](source-notes/gnss-hat-setting-time-raspberry-pi-forums.md) — Receiver HAT time discipline thread.
- [GPS clock display Engineering Radio](source-notes/gps-controlled-clock-raspberry-pi-engineering-radio.md) — NTP Pi + HDMI/LAN clock adjunct.
- [How to build a smart Magic Mirror](source-notes/how-to-build-smart-magic-mirror.md) — Hardware build guide.
- [Trackers without GPS](source-notes/how-to-design-trackers-without-gps.md) — Resilient positioning design article.
- [LORAN definition (TME)](source-notes/loran-definition-tme.md) — Long-range navigation / eLORAN overview.
- [Magic Mirror Buddy](source-notes/magic-mirror-buddy.md) — Project article capture.
- [Magic Mirror reTerminal DM gestures](source-notes/magic-mirror-reterminal-dm-gestures.md) — Gesture + embedded display write-up.
- [MagicMirror² platform README](source-notes/magicmirror2-open-source-smart-mirror-platform.md) — Upstream project excerpt.
- [NTP and GPS timing Raspberry Shake](source-notes/ntp-and-gps-timing-raspberry-shake.md) — Seismic logger UTC/NTP operational notes.
- [Timeserver with GNSS (Pi forums)](source-notes/timeserver-with-gnss-receiver-raspberry-pi-forums.md) — Stratum-1 Pi discussion.
- [360 publication PDF](source-notes/360-publication-pdf.md) — Large PDF import; confirm title inside file.
- [Deep dive natural building Natalie Bogwalker](source-notes/deep-dive-natural-building-natalie-bogwalker-podcast.md) — Podcast page on slip straw / hempcrete.
- [Deep dive tiny houses Medium](source-notes/deep-dive-tiny-houses-medium-casimir-curney.md) — Essay excerpt; Medium paywall.
- [Farmers agritourism tiny homes turtle bypass ABC](source-notes/farmers-agritourism-tiny-homes-turtle-bypass-abc.md) — Australia news excerpt.
- [Maximizing farm income agritourism](source-notes/maximizing-farm-income-agritourism.md) — Agritourism revenue ideas list.
- [NIST Internet Time Service servers](source-notes/nist-internet-time-service-servers.md) — ITS hostname/IP snapshot and usage notes.

## Analyses

- [Repository analysis](analyses/repository-analysis.md) — Structure, validation, publishing, and content profile of **smart-farm-wiki**.
- [Domain content overview](analyses/domain-content-overview.md) — Subject-matter strands (land, connectivity, power, data, business, time/PNT) and how topic hubs map to them.
- [Timing on the farm — synthesis](analyses/timing-on-the-farm-synthesis.md) — Seasonal, rotation, labor, water/energy, and clock sync (NTP/PTP) as layers of “time.”
- [Smart mirror with ESP32 and Raspberry Pi — build analysis](analyses/smart-mirror-esp32-and-raspberry-pi-build.md) — Pi runs MagicMirror²; ESP32 for sensors/side HMI; parts sourcing and web references.
- [Why a synthesis layer](analyses/why-synthesis-layer.md) — Short analysis tying concepts to practice.
- [Concept relationships — summary objects](analyses/concept-relationships-overview.md) — Related concepts: narrative clusters, table, YAML graph.
- [Tracking chickens — motion sensors over LoRa and MQTT](analyses/tracking-chickens-motion-lora-mqtt.md) — Query synthesis: coop/run architecture, MQTT paths, limits vs per-bird tracking.
- [Agritourism, tiny houses, Tennessee hobby farms](analyses/agritourism-tiny-houses-tennessee-hobby-farm.md) — Query synthesis: diversification, TN business context, zoning caveat.
- [Agritourism smart hobby farm — tiny houses and guest work stays](analyses/agritourism-smart-hobby-farm-tiny-houses-guest-work-stays.md) — Query synthesis: lodging + farm work, smart-farm links, risk framing.
- [Starting and stocking a pond — beautiful water feature](analyses/starting-stocking-pond-beautiful-water-feature.md) — Query synthesis: build, stock legally, aesthetics, irrigation adjacency.
- [Farm stocking — 120 acres vs 5 acres (research prompt)](analyses/farm-stocking-120-acres-vs-5-acres-research-prompt.md) — Query brief: research prompt and methods for chickens, crops, animals; automation bias on larger holding.
- [Agritourism business plan — guest hub on 120 acres, family home 35 min away](analyses/agritourism-dual-site-business-plan-five-and-120-acres.md) — Working farm + lodging on 120 ac; private 5 ac residence; coverage and animal placement.

## Comparisons

- [Raw vs wiki](comparisons/raw-vs-wiki.md) — Side-by-side responsibilities and failure modes.

## Timelines

- [Example domain timeline](timelines/example-domain-timeline.md) — Illustrative chronology for template demos.

## Glossary

- [Synthesis layer](glossary/synthesis-layer.md) — Definition entry used across pages.

## Meta

- [Append-only log](log.md) — Chronological record of ingests, queries, and lint passes.
