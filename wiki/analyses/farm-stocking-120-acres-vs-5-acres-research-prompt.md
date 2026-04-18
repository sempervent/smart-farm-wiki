---
title: Farm stocking — 120 acres vs 5 acres (research prompt)
page_type: analysis
status: active
created: 2026-04-17
updated: 2026-04-20
review_status: unreviewed
tags:
  - farm-planning
  - poultry
  - stocking-rate
  - automation
confidence: low
---

# Farm stocking — 120 acres vs 5 acres (research prompt)

**Question**: What **sources and methods** support calculating **how many chickens** and **which crops and animals** to raise on a **120-acre** farm versus a **5-acre** farm, with the **larger farm** run **more hands-off** via **automation**?

**Epistemic note**: This page is a **structured research brief** for gathering **extension, academic, and government** references—not a stocking prescription. Carrying capacity depends on **climate, soil, water, forage quality, markets, labor, regulations**, and **animal welfare** standards; numbers without that context are not actionable.

## Existing wiki anchors (starting points)

- **Forage primers (ingested)**: [`source-notes/ut-forage-menu-beef-forage-center.md`](../source-notes/ut-forage-menu-beef-forage-center.md) (UT extension), [`source-notes/guide-livestock-forage-feeding-grit.md`](../source-notes/guide-livestock-forage-feeding-grit.md) (popular press)—not carrying-capacity math; still need **AU**/pasture **methods** synthesis per [`Implementation backlog`](../analyses/implementation-backlog-strategic-audit.md) P1 #12.
- Poultry and small livestock primers: [`Backyard livestock and homestead animal sources`](../topics/backyard-livestock-and-homestead-animals.md) (egg/meat flock, cattle intro, cited source-notes).
- Cropping and soil entry: [`Sustainable cropping, soil, and farm entry sources`](../topics/sustainable-cropping-soil-and-farm-entry-sources.md) (rotations, cover crops, SARE-style planning).
- Small-farm scale narrative: [`Five Acres and Independence full text`](../source-notes/five-acres-and-independence-full-text.md) — historical **small-farm** guide (verify modern practices against current extension).
- Precision / data-heavy management framing: [`Precision agriculture`](../concepts/precision-agriculture.md); operations stack ideas: [`Farm data, farmOS, and agriculture lab builds`](../topics/farm-data-farmos-and-ag-lab-builds.md); field connectivity: [`Field network IoT comparisons (HaLow, LoRa, NB-IoT)`](../topics/field-network-iot-comparisons.md), [`Smart agriculture, Meshtastic, and LoRaWAN`](../topics/smart-agriculture-meshtastic-and-lorawan.md).

## Copy-paste research prompt (for LLM or literature search)

Use the block below as a **single prompt**; replace bracketed items with your **region, climate zone, and goals** (subsistence vs market, organic vs conventional).

```text
You are helping locate authoritative sources (not opinions) for farm enterprise planning.

Context:
- Farm A: ~5 acres — higher labor per acre acceptable; mixed garden, small flock, possibly a few larger animals if zoning/forage allow.
- Farm B: ~120 acres — prioritize lower daily labor per acre; willing to invest in fencing, water systems, monitoring, and mechanization where ROI is clear.

Tasks:
1) List source types to trust for stocking and mix decisions: land-grant extension bulletins, NRCS/soil & water, state ag departments, peer-reviewed grazing/poultry science, and published enterprise budgets (university or USDA). Exclude generic blog advice unless it cites primary sources.

2) For CHICKENS on each scale, what variables determine flock size? (coop/run space, pasture rotation if used, predator pressure, manure loading, feed logistics, processing regulations). Cite extension publications that give space-per-bird or pasture rotation guidelines.

3) For OTHER ANIMALS (e.g. cattle, sheep, goats, pigs), explain animal unit (AU) or standard stocking concepts and how carrying capacity is calculated from forage/pasture — and what changes when the operation is 5 acres vs 120 acres.

4) For CROPS, contrast intensive raised beds / market garden on 5 acres vs row-crop or hay/forage allocation on 120 acres. Point to rotation planning tools and soil-test-driven planning.

5) For “hands-off at 120 acres,” list automation categories: perimeter and interior fencing + waterers; remote monitoring (weather, tank levels, gate status); pasture subdivision (paddock shifts); feed handling; record-keeping (e.g. farm management software). Map each to realistic labor savings and capital cost bands at a high level, with citations where possible.

6) Output a numbered bibliography-style list of documents to obtain (title + organization + URL pattern if known), prioritized for [REGION/STATE] and [USDA plant hardiness zone or equivalent].

Constraints:
- Flag regulatory triggers (processing, water use, waste, zoning) as “consult local extension / ag attorney” rather than giving legal conclusions.
- If sources conflict, summarize the disagreement and what data would resolve it.
```

## Search terms to combine

- “**stocking rate**” + species + “**animal unit month**” / “**AUM**”
- “**carrying capacity**” + “**pasture**” + region
- “**poultry**” + “**space requirements**” + “extension”
- “**enterprise budget**” + state + (chickens | beef | vegetables)
- “**whole farm plan**” OR “**beginning farmer**” + extension
- “**rotational grazing**” + “**paddock**” + design

## Comparison framing (design intent)

| Dimension | ~5 acres (labor-feasible) | ~120 acres (automation-biased) |
|-----------|---------------------------|--------------------------------|
| Typical enterprise mix | Intensive veg/fruit, small flock, high attention per unit land | Forage-led livestock, hay/row crops, equipment amortized over acres |
| Chickens | Small flock; daily checks plausible; compost/manure on garden scale | Larger flock only if feed, water, predator control, and processing scale; mobility (tractors/egg mobiles) matters |
| Cropping | Bed ft, succession planting, hand harvest | Mechanized field ops, possibly sensor-guided irrigation |
| “Hands-off” enablers | Smaller geography, simpler systems | Remote monitors, reliable water, fence that holds, fewer failure points per acre of attention |

## Next steps for this wiki

When **raw sources** are ingested (extension PDFs, enterprise budgets, grazing manuals), add **`source-notes/`** entries and either update this page with **cited ranges** or spawn a **`comparisons/`** page with explicit assumptions.
