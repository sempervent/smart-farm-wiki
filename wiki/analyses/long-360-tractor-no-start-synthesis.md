---
title: Long 360 tractor — no-start troubleshooting (synthesis)
page_type: analysis
status: active
created: 2026-04-18
updated: 2026-04-18
review_status: unreviewed
tags:
  - tractors
  - diesel
  - equipment
confidence: medium
---

# Long 360 tractor — no-start troubleshooting (synthesis)

**Context**: The **Long 360** is a compact utility diesel (often cited **1977–1991**, **2WD/4WD**) sold in North America; many units trace to **UTB/Universal** (Romania) branding. Engine references in open specs usually describe a **3-cylinder diesel** (commonly listed as **Uzina D-115** class in English-language spec databases—not Perkins); always match **your dataplate** before ordering parts ([TractorData engine notes](https://www.tractordata.com/farm-tractors/005/8/1/5813-long-360-engine.html), [Agro-Specs overview](https://agro-specs.com/tractors/14491-long-360.html)).

**Disclaimer**: This is **synthesis from public forums and general diesel practice**, not a substitute for the **factory service manual**, **lockout/tagout**, or a qualified diesel technician. Torque, bleeding order, and wiring differ by serial year.

---

## 1. Separate “won’t crank” from “cranks, won’t fire”

| Symptom | Typical buckets |
|--------|------------------|
| **No starter rotation** (or weak/brief) | Battery, cables/grounds, starter/solenoid, key circuit, seized engine |
| **Cranks normally, won’t run** | Air in fuel, filters, lift pump, injection timing, poor compression, cold-start/preheat |

Forum threads titled “Long 360 starting problem” and “Long 360 no start” repeatedly mix both—**observe which case you have** before swapping parts ([Tractor Forum — Long 360 starting problem](https://www.tractorforum.com/threads/long-360-starting-problem.50021/), [Long 360 no start](https://www.tractorforum.com/threads/long-360-no-start.59008/page-2)).

---

## 2. Electrical: solenoid click, poor cranking, “good” resting voltage

A **documented pattern** on a **1984 Long 360**: **new starter**, **~13.4 V at the starter**, hot-wiring the **S** terminal, yet **only brief cranking** then **rapid solenoid chatter** ([iFixit thread](https://www.ifixit.com/Answers/View/407296/Tractor+(1984+long+360)+is+not+starting.)).

Plausible interpretations from that thread and general practice:

- **Battery under load**: Lead-acid can show **healthy open-circuit voltage** but **collapse under cranking current**. Responses suggest watching **voltage at the battery posts while cranking**; large sag points to a **bad cell** or **tiny surface charge**—load-testing or substitution is the next step ([same iFixit answers](https://www.ifixit.com/Answers/View/407296/Tractor+(1984+long+360)+is+not+starting.)).
- **Boost test**: Jump from a **known-good** battery or vehicle to **isolate** supply vs. starter ([iFixit](https://www.ifixit.com/Answers/View/407296/Tractor+(1984+long+360)+is+not+starting.)).
- **Control-side current**: Another owner with **solenoid click / lazy engagement** on an older diesel improved reliability by adding a **relay** in the starter control circuit so the **keyswitch** does not carry the full solenoid hold-in current ([iFixit answer describing relay wiring](https://www.ifixit.com/Answers/View/407296/Tractor+(1984+long+360)+is+not+starting.))—treat as a **known pattern on vintage tractors**, not a guaranteed Long 360 factory diagram match.

Also verify **chassis ground** straps, **terminal torque**, and any **fusible links** or **fuses** in the battery feed if glow/PTO/dash lose power together (seen on related models in forum posts—**verify on your schematic**).

---

## 3. Cold start / Thermostart (glow-type preheat)

Community guidance for the Long 360 describes a **Thermostart**-style **intake preheater**: turn the **ignition/key** to a **preheat** position (often described as **partial counter-clockwise**), wait on the order of **~30 seconds**, then crank ([Tractor Forum — Long 360 starting problem](https://www.tractorforum.com/threads/long-360-starting-problem.50021/)). Aftermarket listings describe **12 V** Thermostart-type parts for Long 360-series tractors ([parts vendor listing example](https://tractoramerica.com/products/glow-plug-thermostart-for-long-tractor-360-460-510-550-560-610-2310-2360-2460)).

**If the engine cranks but won’t catch when cold**, confirm **voltage at the heater circuit** when commanded and that **ground paths** are sound.

---

## 4. Fuel path (air, filters, lift, injection)

Typical **diesel no-start** checks repeated for Long 360 discussions:

- **Water/contamination** and **filter replacement**; **bleed** per manual from **filter**, **pump**, and **injector lines** as required ([Tractor Forum threads](https://www.tractorforum.com/threads/long-360-fuel-problem.38067/), [starting problem thread](https://www.tractorforum.com/threads/long-360-starting-problem.50021/)).
- **Fuel delivery to injectors**—crack lines carefully observing safety; **re-torque** to spec.
- **Tank vent** plugged (can mimic fuel starvation) ([Long 360 fuel problem thread](https://www.tractorforum.com/threads/long-360-fuel-problem.38067/)).
- **Banjo fittings / washers** leaking air ([same fuel problem thread](https://www.tractorforum.com/threads/long-360-fuel-problem.38067/)).
- **Injection hardware**: Forum posts mention **CAV-family pumps** and **injector testing** when delivery is suspected ([Long 360 no start](https://www.tractorforum.com/threads/long-360-no-start.59008/page-2))—use a **shop** for pop-test and pump work unless you are equipped.

Generic diesel no-start framing (non-model-specific) also lists **clogged filter**, **line leaks**, and **pressure** checks ([illustrative guide](https://diesel-tractor-won-t-start-troubleshooting.pages.dev/posts/diesel-tractor-won-t-start-troubleshooting/))—useful as a checklist, not a Long manual.

---

## 5. Compression and internals

If **cranking speed is good** and **fuel is known good**, **low compression** (worn rings/cylinders, valves, head gasket) can prevent starting. That requires **gauge work** and interpretation against **spec**—beyond forum guesswork.

---

## 6. Parts sourcing hints (not endorsements)

Starters and electricals appear in **aftermarket** catalogs (e.g. [DB Electrical starter listing mentioning Long 360](https://www.dbelectrical.com/products/new-starter-for-long-tractor-2360-2460-260-2630-310-340-360-445-460.html)); **Thermostart**-type parts appear at specialty vendors ([example](https://tractoramerica.com/products/glow-plug-thermostart-for-long-tractor-360-460-510-550-560-610-2310-2360-2460)). Always **cross-reference OEM/part numbers** from your tractor.

---

## 7. Gaps and epistemic limits

- **Serial-year wiring** (relay vs. direct solenoid, fuse locations) varies; **this page is not a wiring diagram**.
- **Forum anecdotes** can be wrong; prefer **manual + measurement**.
- **No raw import** for this note—**web-only** references below. Ingest a **service manual PDF** later into `raw/processed/` and add a **`source-note`** if you want provenance-grounded steps.

---

## 8. Web references (consulted for this synthesis)

- [Tractor Forum — Long 360 starting problem](https://www.tractorforum.com/threads/long-360-starting-problem.50021/)
- [Tractor Forum — Long 360 no start (p. 2)](https://www.tractorforum.com/threads/long-360-no-start.59008/page-2)
- [Tractor Forum — Long 360 fuel problem](https://www.tractorforum.com/threads/long-360-fuel-problem.38067/)
- [iFixit — 1984 Long 360 not starting (solenoid click / cranking)](https://www.ifixit.com/Answers/View/407296/Tractor+(1984+long+360)+is+not+starting.)
- [TractorData — Long 360 engine](https://www.tractordata.com/farm-tractors/005/8/1/5813-long-360-engine.html)
- [Agro-Specs — Long 360](https://agro-specs.com/tractors/14491-long-360.html)
- [General diesel tractor no-start checklist (non-model-specific)](https://diesel-tractor-won-t-start-troubleshooting.pages.dev/posts/diesel-tractor-won-t-start-troubleshooting/)

---

*When you obtain a **Long 360 service manual** or **dealer bulletin**, file it under `raw/processed/` and link a `source-note` so this page can cite stable paths.*
