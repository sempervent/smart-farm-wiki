---
title: Agentic wiki improvement prompts (staged, strategic audit)
page_type: analysis
status: active
created: 2026-04-21
updated: 2026-04-21
review_status: unreviewed
tags:
  - meta
  - agents
  - prompts
  - roadmap
confidence: high
---

# Agentic wiki improvement prompts (staged, strategic audit)

**Purpose**: **Copy-paste prompts** for improving this repository in **stages**, grounded in [`Strategic audit — decision-safe operations for a two-site smart farm`](strategic-audit-decision-safe-operations.md) and [`Implementation backlog — strategic audit (P0–P3)`](implementation-backlog-strategic-audit.md). Run **pre-prompt** once, then **Phase 1 → 4** in order.

**Repository model assumed**: Git-tracked markdown; `wiki/` holds topics, analyses, comparisons, templates (repo `templates/`), entity pages, and architecture narratives; `docs/` holds operator handbook; [`AGENTS.md`](../../AGENTS.md) is the behavioral contract.

---

## Pre-prompt — quality bar, non-goals, and writing standards

**Copy everything in the block below into a new agent session (or prepend to every phase).**

```text
You are improving a Git-based markdown wiki (this repository). Obey AGENTS.md at the repo root first, then README.md.

QUALITY BAR
- Every new intentional wiki page appears in wiki/index.md under the correct section.
- Pages that change navigation or taxonomy append an entry to wiki/log.md (ingest | refactor | policy as appropriate).
- Run: uv run python scripts/validate_wiki.py --strict before finishing; fix all errors.
- Use kebab-case.md filenames; YAML frontmatter on wiki pages includes at least title and page_type per AGENTS.md.
- Links are relative Markdown only (e.g. ../topics/foo.md), working from Obsidian and MkDocs.
- Do not rewrite or delete historical headings in wiki/log.md; append new entries below prior content.

NON-GOALS (unless the user explicitly expands scope in this session)
- Do not invent site-specific facts (real acreage, addresses, animal counts, budgets, vendor choices). Use placeholders like SITE_HOMESTEAD, COMMUTE_MINUTES, BROKER_TBD.
- Do not alter the meaning of archived material under the **`raw/`** corpus; immutability rules in AGENTS.md apply.
- Do not replace attorneys, accountants, engineers, or veterinarians; frame legal/financial content as questions-for-professionals where needed.
- Avoid drive-by refactors of unrelated pages; keep diffs scoped to the deliverables listed.

REPOSITORY WRITING STANDARDS
- Topic hubs: wiki/topics/<name>.md — narrative + bulleted source-notes and Related links.
- Analyses: wiki/analyses/<name>.md — argument, tables, links to sources and related pages.
- Comparisons: wiki/comparisons/<name>.md — structured tradeoffs.
- Entity pages: wiki/entities/<name>.md — named subject; link to registry/naming docs when relevant.
- Architecture: prefer wiki/analyses/architecture-*.md or dedicated analysis titles; diagrams may be Mermaid in-page or described for later export.
- Templates / SOPs: may live as wiki/analyses/* with tags (template, sop) or future repo templates/* scaffolds; cite AGENTS taxonomy.
- After substantive edits: update wiki/index.md if new pages were added or titles changed.

OUTPUT
- Summarize files created/updated as a checklist.
- If validation fails, fix and re-run until clean.
```

---

## Phase 1 — Foundational architecture (identity, telemetry, system of record)

**Goal**: Establish **naming**, **registry**, **integrative hubs**, and a **credible reference architecture** so later phases attach to stable IDs—not ad-hoc prose. Maps to backlog **P0** (items 1–7) and audit **critical** telemetry/spatial gaps.

### Prompt (copy below)

```text
PHASE 1 — FOUNDATIONAL ARCHITECTURE

Read first: AGENTS.md; wiki/analyses/strategic-audit-decision-safe-operations.md; wiki/analyses/implementation-backlog-strategic-audit.md (P0 section); wiki/analyses/information-architecture-decision-safe-operations.md; wiki/analyses/smart-technology-architecture-audit.md; wiki/concepts/data-storage.md; wiki/topics/farm-data-farmos-and-ag-lab-builds.md; wiki/topics/lora-mqtt-and-gateway-bridges.md; wiki/analyses/field-telemetry-reference-architecture-homestead-120ac.md; wiki/analyses/farm-spatial-model-and-asset-registry-standard.md.

DELIVERABLES
1) wiki/analyses/parcel-paddock-asset-naming-conventions.md — template-style analysis: ID patterns for SITE_A/SITE_B, paddocks, structures, devices; placeholders only.
2) wiki/analyses/farm-asset-registry-minimum-fields.md — table of minimum registry columns; links to naming doc.
3) wiki/topics/two-site-smart-farm-operations.md — hub: 5 ac / 120 ac / ~35 min narrative, links to dual-site non-agritourism analysis, weekly coverage matrix, agritourism contrast, farm stocking prompt.
4) wiki/topics/field-telemetry-and-backhaul.md — hub: links to field telemetry reference architecture, LoRa/MQTT topic, field IoT comparisons, data storage concept, smart-technology audit.
5) wiki/topics/spatial-data-and-farm-map-hygiene.md — hub: links PostGIS source-notes, spatial registry standard, naming conventions, farm data topic.
6) wiki/analyses/telemetry-system-of-record-options-and-boundaries.md — analysis: roles of farmOS vs Home Assistant vs TSDB/DB; conflict rules; placeholders.
7) Update wiki/analyses/field-telemetry-reference-architecture-homestead-120ac.md — add "Related hubs" linking to new topic pages; bump updated date if substantive.
8) Update wiki/index.md (Topics + Analyses as appropriate).
9) Append wiki/log.md: ## [DATE] refactor | Phase 1 foundational architecture hubs and templates

ACCEPTANCE CRITERIA
- validate_wiki.py --strict passes.
- Every new page listed in wiki/index.md with one-line description.
- No invented property facts; placeholders explicit.
- Cross-links exist between hubs and existing analyses (dual-site non-agritourism, weekly coverage matrix, strategic audit).

CONSTRAINTS
- Do not duplicate full bodies of existing analyses; hubs are navigation + short narrative.
- Do not add raw/ files in this phase unless ingesting new material (prefer synthesis only).

FILES TO CREATE (minimum)
- wiki/analyses/parcel-paddock-asset-naming-conventions.md
- wiki/analyses/farm-asset-registry-minimum-fields.md
- wiki/topics/two-site-smart-farm-operations.md
- wiki/topics/field-telemetry-and-backhaul.md
- wiki/topics/spatial-data-and-farm-map-hygiene.md
- wiki/analyses/telemetry-system-of-record-options-and-boundaries.md

FILES TO UPDATE (minimum)
- wiki/index.md
- wiki/log.md
- wiki/analyses/field-telemetry-reference-architecture-homestead-120ac.md
- wiki/topics/knowledge-synthesis.md (add links to new hubs under Domain entry points, if not already crowded)
```

---

## Phase 2 — Operational workflows (SOPs, coverage, risk containment)

**Goal**: **Runnable** operations—incidents, degraded automation, insurance questions, civil systems, logistics framing—so automation failures do not become welfare or safety failures. Maps to **P1** (8–14) and operational items in [`Business viability…`](business-viability-and-farm-economics-gap-analysis.md).

### Prompt (copy below)

```text
PHASE 2 — OPERATIONAL WORKFLOWS

Read first: wiki/analyses/implementation-backlog-strategic-audit.md (P1); wiki/analyses/weekly-coverage-matrix-two-site-farm-operations.md; wiki/analyses/automation-degraded-modes-manual-fallback-sop.md; wiki/topics/two-site-smart-farm-operations.md (from Phase 1); wiki/analyses/dual-site-operations-model-non-agritourism.md; wiki/topics/off-grid-solar-power-and-storage.md; wiki/topics/smart-home-matter-thread-and-home-assistant-ai.md.

DELIVERABLES
1) wiki/analyses/incident-response-livestock-emergency-owner-remote-sop.md — SOP: call order, on-site contact placeholders, vet, water shutoffs; tags: sop; link weekly coverage matrix.
2) Expand wiki/analyses/automation-degraded-modes-manual-fallback-sop.md OR add wiki/analyses/automation-degraded-modes-per-system-appendix.md — structured placeholders per SYSTEM_* without real breaker IDs unless user later fills.
3) wiki/analyses/insurance-liability-two-parcels-question-checklist.md — questions for counsel; not legal advice; link two-site hub.
4) wiki/topics/homestead-civil-systems-water-waste-power-network.md — hub linking solar, smart home, degraded SOPs; "ops base" framing.
5) wiki/concepts/two-site-logistics.md — concept: feed, fuel, harvest, tools, people between parcels; link dual-site model + future economics pages.
6) wiki/analyses/stocking-and-forage-methods-extension-synthesis.md — stub or light synthesis: methods only; cite existing forage source-notes; no carrying capacity numbers without sources.
7) wiki/analyses/capex-opex-enterprise-sequencing-two-site-constraint.md — first draft with placeholder phasing table; link east TN profitable crops matrix + TN hobby farm topic.
8) Update wiki/topics/two-site-smart-farm-operations.md to link new SOPs and checklists.
9) Update wiki/index.md; append wiki/log.md (refactor | Phase 2 operational workflows).

ACCEPTANCE CRITERIA
- validate_wiki.py --strict passes.
- At least one clear cross-link path: two-site hub → incident SOP → weekly coverage matrix.
- Insurance checklist explicitly disclaims legal advice.
- No numeric enterprise promises without labeled assumptions.

CONSTRAINTS
- Do not ingest large new raw corpora unless necessary; prefer linking existing source-notes for forage.

FILES TO CREATE (minimum)
- wiki/analyses/incident-response-livestock-emergency-owner-remote-sop.md
- wiki/analyses/insurance-liability-two-parcels-question-checklist.md
- wiki/topics/homestead-civil-systems-water-waste-power-network.md
- wiki/concepts/two-site-logistics.md
- wiki/analyses/stocking-and-forage-methods-extension-synthesis.md (may be stub with "open items")
- wiki/analyses/capex-opex-enterprise-sequencing-two-site-constraint.md
- Optional: wiki/analyses/automation-degraded-modes-per-system-appendix.md

FILES TO UPDATE (minimum)
- wiki/analyses/automation-degraded-modes-manual-fallback-sop.md (if expanding)
- wiki/topics/two-site-smart-farm-operations.md
- wiki/index.md; wiki/log.md; wiki/analyses/domain-content-overview.md (Gaps bullet if needed)
```

---

## Phase 3 — Resilience, security, observability, and decision-grade comparisons

**Goal**: **Defensible** stack—cybersecurity, remote access story, observability when alerts fail, firmware policy, gateway and record-stack comparisons, start **resilience graph** narrative. Maps to **P2** (15–21) and parts of **P3 #25**.

### Prompt (copy below)

```text
PHASE 3 — RESILIENCE, SECURITY, OBSERVABILITY, COMPARISONS

Read first: wiki/analyses/smart-technology-architecture-audit.md; wiki/analyses/implementation-backlog-strategic-audit.md (P2–P3 partial); wiki/topics/homelab-self-hosting-and-edge-narratives.md; wiki/topics/field-telemetry-and-backhaul.md; wiki/analyses/telemetry-system-of-record-options-and-boundaries.md.

DELIVERABLES
1) wiki/concepts/operational-technology-ot-security-farms.md — concept: VPN, segmentation, MQTT auth, camera exposure at high level.
2) wiki/topics/farm-cybersecurity-and-remote-access.md — hub linking OT concept, homelab topic, field telemetry hub, data storage concept.
3) wiki/analyses/observability-and-alerts-broker-down-false-positives-oncall.md — analysis/SOP hybrid: failure of alert pipeline; link degraded modes SOP.
4) wiki/analyses/firmware-and-device-lifecycle-field-nodes.md — policy placeholders: cadence, test device, rollback.
5) wiki/comparisons/gateway-architecture-fixed-tower-vs-vehicle-vs-mesh.md — comparison table + when to choose; link field IoT comparisons.
6) wiki/comparisons/farmos-vs-lightweight-record-stack.md — comparison: ops weight, team size, integration; link farm data topic.
7) wiki/analyses/resilience-graph-roads-water-power-comms.md — first draft: cascading dependencies; link road/irrigation/pond topics and steep road analysis.
8) Update wiki/analyses/strategic-audit-decision-safe-operations.md Related section only if a new meta link is needed (minimal).
9) Update wiki/index.md (Concepts, Topics, Comparisons, Analyses); append wiki/log.md.

ACCEPTANCE CRITERIA
- validate_wiki.py --strict passes.
- Farm cybersecurity hub links to both **homelab** and **field** paths.
- Comparisons use structured headings (criteria table), not marketing language.
- Resilience graph explicitly ties at least three strands (e.g. road, water, comms) with placeholders for site specifics.

CONSTRAINTS
- Do not assert specific CVEs or vendor zero-days; stay policy- and architecture-level.
- No real passwords, hostnames, or public IPs in wiki text.

FILES TO CREATE (minimum)
- wiki/concepts/operational-technology-ot-security-farms.md
- wiki/topics/farm-cybersecurity-and-remote-access.md
- wiki/analyses/observability-and-alerts-broker-down-false-positives-oncall.md
- wiki/analyses/firmware-and-device-lifecycle-field-nodes.md
- wiki/comparisons/gateway-architecture-fixed-tower-vs-vehicle-vs-mesh.md
- wiki/comparisons/farmos-vs-lightweight-record-stack.md
- wiki/analyses/resilience-graph-roads-water-power-comms.md

FILES TO UPDATE (minimum)
- wiki/topics/knowledge-synthesis.md
- wiki/index.md; wiki/log.md
- wiki/analyses/information-architecture-decision-safe-operations.md (optional: note Phase 3 shipped)
```

---

## Phase 4 — Optimization, economics depth, instrumentation, and governance

**Goal**: **Prioritize** spend and complexity—unit economics methodology, instrumentation ROI, phased multi-year build, data retention, optional catastrophe and entity placeholders. Maps to **P3** (22–28) and optimization items in business + tech audits.

### Prompt (copy below)

```text
PHASE 4 — OPTIMIZATION AND GOVERNANCE

Read first: wiki/analyses/business-viability-and-farm-economics-gap-analysis.md; wiki/analyses/implementation-backlog-strategic-audit.md (P3); wiki/analyses/capex-opex-enterprise-sequencing-two-site-constraint.md (from Phase 2); wiki/analyses/east-tennessee-profitable-crops-matrix.md; wiki/analyses/smart-technology-architecture-audit.md (diagram checklist).

DELIVERABLES
1) wiki/analyses/enterprise-unit-economics-worksheet-methodology.md — methodology only; link UT budget URLs via east TN matrix; placeholders for yields/prices.
2) wiki/analyses/instrumentation-priority-matrix-acres-risks-roi.md — framework for ranking sensors; no fake ROI numbers.
3) wiki/timelines/phased-build-years-0-5-two-sites.md — timeline template with placeholder years/milestones; link CAPEX/OPEX analysis.
4) wiki/analyses/data-retention-ownership-compliance-telemetry.md — governance questions; link SoR analysis and farm cybersecurity hub.
5) wiki/analyses/drought-flood-wildfire-water-access-contingencies.md — stub or light synthesis; link resilience graph and irrigation/pond topics.
6) wiki/entities/example-farm-sites-placeholder.md — OPTIONAL: replace or supplement entities/example-org.md pattern with **explicitly placeholder** farm sites (or add two short entity stubs: site-homestead-placeholder.md, site-farm-placeholder.md) — if added, document as placeholders in body and index.
7) Add Mermaid or bullet diagrams to wiki/analyses/architecture-reference-smart-farm-homestead-and-120ac.md OR create that file by promoting/expanding field-telemetry-reference-architecture into v1.0 outline per smart-technology-architecture-audit §4.
8) Update wiki/index.md; append wiki/log.md; update wiki/analyses/domain-content-overview.md Gaps if major hubs landed.

ACCEPTANCE CRITERIA
- validate_wiki.py --strict passes.
- Unit economics page does not present fabricated farm profit; methodology only.
- Data retention page flags legal/compliance as professional territory.
- Timeline and instrumentation pages usable as **templates** with empty tables.

CONSTRAINTS
- Do not store secrets or personal data in wiki pages.
- Entity pages: if created, must be clearly labeled placeholder or draft.

FILES TO CREATE (minimum)
- wiki/analyses/enterprise-unit-economics-worksheet-methodology.md
- wiki/analyses/instrumentation-priority-matrix-acres-risks-roi.md
- wiki/timelines/phased-build-years-0-5-two-sites.md
- wiki/analyses/data-retention-ownership-compliance-telemetry.md
- wiki/analyses/drought-flood-wildfire-water-access-contingencies.md
- wiki/analyses/architecture-reference-smart-farm-homestead-and-120ac.md OR major update to field-telemetry-reference-architecture-homestead-120ac.md

FILES TO UPDATE (minimum)
- wiki/index.md; wiki/log.md; wiki/topics/two-site-smart-farm-operations.md; wiki/analyses/implementation-backlog-strategic-audit.md (add "shipped" links to new pages in a maintenance note, without rewriting history)
```

---

## Sequence summary

| Order | Focus | Backlog alignment |
|-------|--------|---------------------|
| Pre-prompt | Standards | AGENTS.md |
| Phase 1 | Foundational architecture | P0 |
| Phase 2 | Operational workflows | P1 |
| Phase 3 | Resilience, security, comparisons | P2 (+ resilience graph) |
| Phase 4 | Optimization & governance | P3 |

---

## Related

- [`Strategic audit — decision-safe operations for a two-site smart farm`](strategic-audit-decision-safe-operations.md)
- [`Implementation backlog — strategic audit (P0–P3)`](implementation-backlog-strategic-audit.md)
- [`Information architecture — decision-safe operational brain (target design)`](information-architecture-decision-safe-operations.md)

---

*When a phase completes, optionally tick items in the implementation backlog body or add a short **policy** log entry documenting prompt-pack version.*
