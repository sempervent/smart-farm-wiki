---
title: Enterprise options analysis — 120-acre East Tennessee two-site smart farm
page_type: analysis
status: active
created: 2026-04-17
updated: 2026-04-17
review_status: unreviewed
tags:
  - business-plan
  - enterprise-selection
  - east-tennessee
  - two-site
  - grazing
  - automation
confidence: medium
aliases:
  - East Tennessee two-site farm business plan — enterprise options analysis
---

# Enterprise options analysis — 120-acre East Tennessee two-site smart farm

**Hub**: [`East Tennessee two-site farm business plan — planning framework`](east-tennessee-two-site-farm-business-plan-framework.md)  
**Chosen strategy family (operating plan)**: [`Recommended enterprise strategy`](east-tennessee-two-site-farm-business-plan-recommended-enterprise-strategy.md)

## Scope and non-claims

This page **compares plausible enterprise paths** for the **~120-acre** production parcel under a **two-site** constraint: **~5-acre homestead** = family home + future **operational / telemetry brain** (not primary commercial production); **~35 minutes** one-way between sites. Optimization priority: **profit** > **low labor** > **resilience/sustainability**.

**Not asserted**: Soil maps, fence/water condition, debt capacity, or market access—those remain **validation** items ([`validation backlog`](east-tennessee-two-site-farm-business-plan-validation-backlog.md)). Numbers below are **pattern-level** (typical tradeoffs), not farm-specific pro formas.

**Distance rule of thumb**: A 35-minute one-way leg consumes **~1.2 hours** round-trip plus task time. Models that need **daily eyes** without resident labor score worse unless **batchable**, **deferrable**, or **telemetrable** with honest alert burden.

---

## How automation is scored (honest)

| Helps materially | Often adds burden |
|------------------|-------------------|
| Water tank level / pump fault; remote gate position; temperature / heat index alerts; perimeter breach (where legal & reliable) | Sensor sprawl without naming/registry; cameras without triage; “smart” gear with no spares; MQTT/cloud complexity without runbooks |
| Reducing **unnecessary trips** (“tank OK”) | Replacing **skilled judgment** (body condition, calving assist, crop scouting) |
| Logging events for **asset + liability** traceability | False positives → alert fatigue → ignored real failures |

---

## Candidate path A — Cattle: cow-calf or grazing-focused beef

### What the model is

Commercial **beef** enterprise centered on **grazing** (cow-calf retains breeding stock; **stocker/backgrounder** buys/sells feeder cattle on grass). Revenue from **live animal sales** (auction, direct, video) with optional **value-add** later.

### Likely operational pattern

Seasonal **calving** or arrival windows; **rotation** across paddocks; hay feeding in deficit periods; vet/AI as scheduled; marketing in **discrete sales events**.

### Labor profile

- **Baseline**: Moderate **annual** hours, **spiky** at calving, weaning, working pens, hauling.
- **Two-site**: Works if visits are **batched** (3–4×/week + surge weeks) **or** someone is **often** near the remote parcel (not assumed).

### Capital profile

- **High** if starting from raw land: **fence**, **water**, **handling facilities**, **trailer/truck** class, cattle purchase.
- **Selective financing** often targets **depreciable** livestock or **durable** fence/water.

### Automation / telemetry fit

**Strong** for: water, pump runtime, tank level, gate state, optional LoRaWAN/Meshtastic for remote tanks; **moderate** for herd location (GPS collars = OPEX + vendor lock).

### Time to revenue

**~12–24+ months** from a standing start (herd build, forage establishment). Faster if buying **operating units** or **stockers** on existing grass.

### Key risks

Price cycles; drought; predator/disease; handling injuries; **thin markets** if direct marketing is weak.

### Infrastructure demands

Perimeter fence, **lanes**, **corrals**, reliable **water in every paddock**, loading area, **electric** or solar where needed.

### Skills demands

Stockmanship, low-stress handling, basic nutrition, truck/trailer competence, auction/direct sales literacy.

### Two-site fit (35 min)

**Good** if **batching** + telemetry reduce panic trips; **poor** if the plan assumes **daily** physical checks without resident labor.

### Five-acre home-base fit

**Excellent**: cattle live on **120**; homestead holds **comms, NVR, broker, spare parts**, not animals (unless quarantine policy says otherwise).

### Salary-replacement scalability

**Moderate–high** at 120 acres **if** stocking/forage are right and markets are disciplined—**not** automatic; margin per acre is **thin** without scale efficiencies or premium channels.

---

## Candidate path B — Rotational grazing + small ruminants (sheep / goats)

### What the model is

**Sheep or goats** on **intensive rotation**, often with **higher** stocking than beef per acre (species-dependent). Revenue: lambs/kids, breeding stock, **fiber** niche, or **targeted grazing** contracts.

### Likely operational pattern

Frequent **moves**; predator management; **parasite** management central; seasonal marketing windows.

### Labor profile

**Higher touch per dollar** than beef for many operators: handling, predation, health (parasites), **sorting**.

### Capital profile

**Moderate–high** fence (often **netting**), **handling** system, predator controls; smaller animals can reduce **per-unit** land need but increase **labor intensity**.

### Automation / telemetry fit

**Moderate**: same water/gate stack as cattle; **guard animals / LGD** are not “telemetry.” **Electric net** faults are a real maintenance tax.

### Time to revenue

Can be **faster** than cow-calf if buying **feeder lambs**; breeding herds take **12+ months** to rhythm.

### Key risks

Predators (coyotes, dogs); **parasite resistance**; **thin** local slaughter/processing; price volatility for lambs.

### Infrastructure demands

**Predator-proof** perimeter; **lambing/kidding** shelter strategy; working pens sized to species.

### Skills demands

Species-specific health; marketing **niche** channels often required for margin.

### Two-site fit

**Weaker than beef** for the same family labor budget: **more trips** or **more risk** between trips. Improves if **resident** labor exists on site (not assumed).

### Five-acre fit

**Good** for brain-at-home; **avoid** hobby flock at homestead that **complicates** biosecurity vs production herd.

### Salary scalability

**Possible** but often **harder** than beef at this scale unless **strong** niche + processing—**labor** usually binds before automation saves it.

---

## Candidate path C — Hay / forage production (mechanical)

### What the model is

**Mechanized** hay: cut, rake, bale; sell **square or round** into local equine, cattle, or export **lane**. Optionally **wrap** / **baleage**.

### Likely operational pattern

**Weather windows** drive 80% of the stress; **equipment chains** (mower-conditioner, tedder, rake, baler); **storage** and **loading**.

### Labor profile

**Compressed spikes** (long days in season); **low** weekly hours off-season **if** not chasing custom work.

### Capital profile

**Very high** if owning full line **new**; **moderate** if **used**, **custom hire** for some passes, or **partnership**. **Trap**: hay tools that sit 11 months.

### Automation / telemetry fit

**Weak–moderate**: moisture meters, weather stations, **bale tags**; does not remove **operator in cab**. **Telemtry** helps **logistics** (which field done), not the cut itself.

### Time to revenue

**Fast** once fields are productive: **same season** first sales if quality clears.

### Key risks

**Weather** (rain on windrows); **equipment downtime** at peak; **commodity** pricing for hay; **storage** losses.

### Infrastructure demands

**Equipment shed**, **fuel**, **transport** (truck + loader), **barn or stack** space; **field access** for wagons.

### Skills demands

Heavy equipment maintenance; **forage quality** literacy; CDL may enter depending on haul.

### Two-site fit

**Mixed**: production is **on 120**; but **peak season** may need **sleep-near-field** or **crew**—35 min is **painful** in **narrow weather**.

### Five-acre fit

**Brain** can schedule/log; **equipment** usually lives at **120** or leased yard—duplicate tools at homestead rarely pay.

### Salary scalability

**Tough at 120 acres alone** as **primary** income unless **high** yields, **premium** markets, or **custom** income stacks—equipment **CAPEX** competes with salary draw.

---

## Candidate path D — Mixed livestock + forage (e.g., cattle + sheep; or cattle + hay surplus)

### What the model is

**Diversified** animal/forage revenue to **smooth** price/weather shocks; often **one anchor** + **satellite**.

### Likely operational pattern

More **moving parts**: rotations must respect **species** separation; possibly **multiple** marketing channels.

### Labor profile

**Higher complexity**, not always higher **hours** if systems are tight—but **mistakes** cost more.

### Capital profile

**Layered**: fence/water must serve **worst-case** species; **handling** may need **two** systems.

### Automation / telemetry fit

**Same as dominant species**; **more** alert rules to tune; **integration** burden rises.

### Time to revenue

**Staggered**—some streams earlier, some later.

### Key risks

**Diluted focus**; **operational complexity** without extra labor; **cross-subsidy** fantasy.

### Infrastructure demands

Union of species needs—often **higher** than single-species.

### Skills demands

**Multiple** species or **honest** hiring for gaps.

### Two-site fit

**OK** if **one** enterprise is clearly **primary** (80% margin focus) and the other is **small** experiment.

### Five-acre fit

**Good** if homestead stays **command** not **production**.

### Salary scalability

**Higher resilience**, **moderate** execution risk—wins when **management** is strong.

---

## Candidate path E — Specialty crops (vegetables, hemp, etc.)

### What the model is

**High-value** crops with **direct** or **wholesale** channels; **intensive** land use.

### Likely operational pattern

**Weekly** or **daily** season; **plant/harvest** spikes; **cooler** and **food safety** surface.

### Labor profile

**High** vs grazing at same revenue—**hand** work, **sorting**, **market prep**.

### Capital profile

**Irrigation**, **tunnel**, **cooler**, **wash pack**, **possibly GAP**—**lumpy** CAPEX.

### Automation / telemetry fit

**Soil moisture**, **irrigation valves** help **labor** and **yield**—but **scouting**, **harvest**, **pack** remain human-heavy unless **large** scale + equipment.

### Time to revenue

**Months** from plant to first sales; **learning curve** tax in years 1–2.

### Key risks

**Market** access; **labor** burnout; **food safety**; **weather** on perishable product.

### Infrastructure demands

**Water** rights and distribution; **post-harvest** chain.

### Skills demands

Production + **sales** + often **regulatory** literacy.

### Two-site fit

**Poor** for **low-labor** goal: **distance** hurts **daily** ops unless **someone lives there** or **crew** is hired (not in baseline).

### Five-acre fit

**Risk of confusion**: do not **scale specialty** on 5 ac while claiming 120 ac plan—**keep roles explicit**.

### Salary scalability

**Possible** with **strong** channels; **not** the default **low-labor** path.

---

## Candidate path F — Orchard / perennial crops

### What the model is

**Tree fruit, nuts, berries**, or **hops**-class perennials—**long** establishment.

### Likely operational pattern

**Years** of negative cash; **seasonal** harvest **labor** spikes; **pest** complexity.

### Labor profile

**Front-loaded** establishment; **peak** harvest weeks; **pruning** windows.

### Capital profile

**Trees/plants**, **irrigation**, **frost** mitigation, **deer** control—**sunk** for decades.

### Automation / telemetry fit

**Soil moisture**, **frost fans** (capital-heavy), **weather**; **machine harvest** only at **scale** and species fit.

### Time to revenue

**Years** (often **3–7+** depending on crop and variety).

### Key risks

**Biology** (disease, frost); **long** payback; **market** timing when bearing hits.

### Infrastructure demands

**Deer fence**; **irrigation**; possibly **cold storage**.

### Skills demands

**Horticulture** + pest ID; **marketing** for perishables.

### Two-site fit

**Moderate**: less **daily** need than vegetables once established, but **harvest** still **compressed**; **theft/vandalism** risk when absent.

### Five-acre fit

**Brain** at home OK; **crop** on 120.

### Salary scalability

**High ceiling** **if** bearing years align with markets—**poor fit** for **near-term** salary replacement **unless** other income bridges the gap.

---

## Candidate path G — Agritourism / event-based revenue

### What the model is

**Day visitors**, **events**, **classes**, **U-pick**, **farm stays** (strong regulatory/insurance surface).

### Likely operational pattern

**Weekend** and **evening** presence; **marketing** continuous; **guest** workflows.

### Labor profile

**People hours** per dollar can be **high**; **hard** to automate **hospitality**.

### Capital profile

**Parking**, **bathrooms**, **structures**, **signage**, **ADA** considerations—**lumpy**.

### Automation / telemetry fit

**Booking**, **access control**, **cameras**—helps **ops**, not core **experience** labor.

### Time to revenue

**Months** if audience exists; **years** to **stable** calendar.

### Key risks

**Zoning**; **liability**; **weather** on event day; **reputation** risk.

### Infrastructure demands

**Road**, **power**, **water**, **egress**, **capacity**.

### Skills demands

**Sales**, **event ops**, **food** rules if serving.

### Two-site fit

**Often poor** for **low-labor**: **presence** expectation conflicts with **35 min** unless **staff** or **sparse** events only.

### Five-acre fit

**Dangerous to conflate**: if **lodging** is on 5 ac and **experience** on 120, **logistics** split must be **designed**—see [`Agritourism business plan — guest hub on 120 acres…`](agritourism-dual-site-business-plan-five-and-120-acres.md) for a **different** explicit scenario.

### Salary scalability

**Can** work as **minority** revenue stream; **rarely** the **low-labor** backbone at modest scale.

---

## Candidate path H — Mixed strategy with phased progression

### What the model is

**Explicit sequencing**: e.g. **forage + fence + water** → **grazing enterprise** → **add** hay sales or **lease** crop acres → **later** niche crop or **direct** beef.

### Likely operational pattern

**Only one major new system per phase**; **gates** on cash and labor.

### Labor profile

**Ramps** with complexity—**disciplined** operators only.

### Capital profile

**Spreads** lumpy spend; uses **cash from Phase 1** to fund Phase 2 where possible.

### Automation / telemetry fit

**Layered**: **water first**, then **inventory** records, then **optional** collars.

### Time to revenue

**Depends on first phase**—often **grazing or hay** fastest.

### Key risks

**Scope creep**; **shiny** diversification before **core** margin.

### Infrastructure demands

**Whatever Phase 1 picks**—should be **multi-use** (fence/water serves many futures).

### Skills demands

**Project management** + primary enterprise skills.

### Two-site fit

**Strong**: **batch** work aligns with **phased** intensity.

### Five-acre fit

**Strong**: homestead remains **C2** / **NOC** for telemetry as phases roll.

### Salary scalability

**High** among options because it **refuses** to bet the farm on one **slow** crop.

---

## Candidate path I — Land-improvement-first, monetization second

### What the model is

**Years 0–2**: **soil**, **fence**, **water**, **access**, **erosion**, **invasive** control—**possibly** paid **NRCS-style** practices + **EQIP**-class programs (eligibility **not assumed**). **Minimal** livestock/crop exposure until **carrying capacity** is known.

### Likely operational pattern

**Contractors** + **family** project windows; **monitoring** plots; **grazing** trials last.

### Labor profile

**Project spikes**; **lower** daily livestock labor early.

### Capital profile

**High** “dirt” spend **before** revenue—**risk** if not **grant/contract** assisted.

### Automation / telemetry fit

**Monitoring**: **rain gauges**, **soil moisture** probes, **trail** cameras for **access** control—**good** for **proving** progress, weak for **direct** income.

### Time to revenue

**Delayed**—this is **deliberate**.

### Key risks

**Sunk cost** with no **enterprise**; **analysis paralysis**.

### Infrastructure demands

**Roads**, **water development**, **fence**—often **enables** all later paths.

### Skills demands

**Earthwork**, **grant writing**, **planning**—or **hire**.

### Two-site fit

**Good**: **improvement** visits can be **batched**; **telemetry** proves **remote** progress.

### Five-acre fit

**Planning office** at homestead.

### Salary scalability

**Indirect**: raises **ceiling** on **all** later paths; **must** transition to **revenue** before year ~3–5 or **opportunity cost** wins.

---

## Candidate path J — Leasing / contract components

### What the model is

**Cash rent** to crop tenant; **custom grazing** contract; **hunting lease**; **solar** lease (site-dependent); **targeted grazing** contract. Often **combined** with owned enterprise.

### Likely operational pattern

**Low** touch if tenant is **solid**; **high** touch if tenant is **not**.

### Labor profile

**Low–moderate**: **lease admin**, **field checks**, **dispute** handling.

### Capital profile

**Low** additional if land is **already** attractive; **opportunity cost** of **not** farming yourself.

### Automation / telemetry fit

**Boundary** monitoring, **access** logging; **not** core to tenant farming.

### Time to revenue

**Fast** once leased—**annual** checks.

### Key risks

**Soil compaction**; **herbicide** drift; **hunting** liability; **below-market** rent if desperate.

### Infrastructure demands

**Legal** clarity; **access** roads; **clear** boundaries.

### Skills demands

**Contract** literacy; **landlord** patience.

### Two-site fit

**Excellent**: **mailbox money** reduces **trip pressure** for **other** enterprises.

### Five-acre fit

**N/A** production—**cash** supports **homelab** amortization.

### Salary scalability

**Usually partial** at 120 acres—**supplements** salary replacement **unless** rent is **strong** and **expenses** low.

---

## Comparison table

Scores are **relative** for this **family**, **two-site**, **profit/low-labor/automation** brief—**not** universal truths. Scale **1–5** (5 = best fit).

| Path | Profit potential | Labor intensity (5=low) | Cap intensity (5=low) | Automation leverage | Time to revenue (5=fast) | Two-site fit | Resilience | Notes |
|------|------------------|-------------------------|------------------------|---------------------|--------------------------|--------------|------------|-------|
| A Beef grazing / cow-calf | 3–4 | 3 | 2 | 4 | 2 | 4 | 4 | Thin margins unless premium/direct |
| B Small ruminants | 2–3 | 2 | 2 | 3 | 3 | 2 | 3 | Predator/labor/markets |
| C Hay mechanical | 2–3 | 2 | 1 | 2 | 5 | 2 | 3 | Equipment trap |
| D Mixed livestock | 3 | 2 | 2 | 3 | 3 | 3 | 4 | Complexity tax |
| E Specialty crops | 3–5 | 1 | 2 | 3 | 4 | 1 | 3 | Channel-dependent |
| F Orchard / perennial | 3–5* | 2 | 2 | 3 | 1 | 3 | 3 | *Years to bearing |
| G Agritourism | 2–4 | 1 | 2 | 2 | 4 | 2 | 3 | Presence + regs |
| H Phased mixed | 4 | 3 | 3 | 4 | 3 | 4 | 4 | **Meta-strategy** |
| I Land-first | 2† | 3 | 2 | 3 | 1 | 4 | 4 | †Raises **future** profit |
| J Lease / contract | 2–3 | 4 | 5 | 2 | 5 | 5 | 3 | Usually **partial** income |

---

## Top 3 paths (conditional, not dogmatic)

**1 — Path H (phased mixed strategy)**  
**Why**: Matches **minimal early spend**, **optionality**, and **family** capacity to absorb **one** major system at a time. **Does not** require committing to orchard or agritourism before **fence/water/forage** reality is known.

**2 — Path A (commercial grazing: cow-calf or stocker)**  
**Why**: At **120 acres** in **ET**, **grass-based** revenue is **plausible** with **batchable** labor; **telemetry** (water, gates, power) has **clear ROI** against **35-minute** trips. **Caveat**: **must** validate **stocking**, **markets**, and **infrastructure** state—otherwise **path I** first.

**3 — Path J + A or J + H (lease income as stabilizer + owned grazing or phased stack)**  
**Why**: **Cash rent** or **hunting/custom** lease can **buy time** and **reduce** forced trips while **improving land** or **building herd**. **Does not** usually **replace** salary alone at **one** tract—treat as **component**.

### Why other paths rank lower (for this brief)

| Path | Primary drag |
|------|----------------|
| **B** Small ruminants | **Labor + predators + markets** vs same automation budget |
| **C** Hay primary | **Equipment CAPEX** and **weather peaks** vs 120-ac **scale** |
| **E** Specialty | **Daily/weekly** labor and **marketing** vs **35 min** |
| **F** Orchard primary | **Years** to material revenue—**salary replacement** needs **bridge** income |
| **G** Agritourism primary | **Presence**, **regs**, **liability**—conflicts with **low-labor** unless **niche** scale |

**Not disqualified**: Paths **E, F, G** can be **phase-3** **slices** if **Phase 1–2** create **margin + audience**.

---

## Recommended phased strategy (strategy, not a single enterprise)

**Phase 0 — Validate gates (parallel, cheap)**  
Soil, water, fence, legal **use** rights, **processing** access, **market** probes. **Telemetry**: minimal **monitoring** to **log** baseline (rain, soil moisture points, tank levels if any).

**Phase 1 — Land + liquidity that does not assume heroic labor**  
- **Path I** elements **as needed** (water/fence/access).  
- **Path J** where acceptable (**partial lease**, **hunting**, **custom graze**) to **fund** improvements and **reduce** cash panic.  
- **Avoid** buying **orphan equipment** for hay or **planting** **slow** perennials **before** **cash** plan exists.

**Phase 2 — Core grazing enterprise (Path A or conservative D)**  
Start **one** **grazing** engine: **stockers** (faster cash cycle) **or** **small cow-calf** (if family wants breeding). **Automation**: **water + power + gate** truth; **records** in **farmOS-class** system ([`Farm spatial model and asset registry standard`](farm-spatial-model-and-asset-registry-standard.md)).

**Phase 3 — Add only if Phase 2 clears margin tests**  
- **Hay** only if **equipment** is **solved** (hire/custom/partner), not **default** ownership.  
- **Specialty / U-pick / events** only with **proven** labor and **channel**—otherwise **stay** grazing-led.

**Kill / pivot triggers (examples—quantify in revenue page)**  
- **Two consecutive years** **negative** operating cash after **excluding** family labor at **replacement wage**.  
- **Automation** OPEX > **documented** trip/labor savings + **risk reduction**.  
- **Market** channel fails **minimum** price **floor** test.

---

## Assumptions vs validation

| Item | Status |
|------|--------|
| 35 min is representative for planning | **Assumption** — log seasonally |
| **120 ac** can support **commercial** grazing **after** water/fence | **Unknown** — carrying capacity study |
| **Direct** beef **premium** exists locally | **Unknown** — test lots |
| **Lease** rates in county | **Unknown** — comps |

---

## Links

- [`Planning framework — rubric`](east-tennessee-two-site-farm-business-plan-framework.md#weighted-evaluation-rubric)
- [`Two-site operating context`](east-tennessee-two-site-farm-business-plan-two-site-operating-context.md)
- [`East Tennessee — profitable crops matrix`](east-tennessee-profitable-crops-matrix.md)
- [`Dual-site operations model — non-agritourism`](dual-site-operations-model-non-agritourism.md)
- [`Field telemetry reference architecture — homestead + 120-acre farm`](field-telemetry-reference-architecture-homestead-120ac.md)
