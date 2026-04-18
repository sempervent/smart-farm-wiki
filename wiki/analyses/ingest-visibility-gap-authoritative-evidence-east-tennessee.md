---
title: Ingest visibility gap — authoritative evidence vs published wiki (East Tennessee)
page_type: analysis
status: active
created: 2026-04-23
updated: 2026-04-23
tags:
  - meta
  - ingest
  - east-tennessee
  - information-architecture
review_status: unreviewed
confidence: high
---

# Ingest visibility gap — authoritative evidence vs published wiki (East Tennessee)

**Summary**: Recent **authoritative** material was **filed correctly** under `raw/processed/` and **grounded** in `wiki/source-notes/`, but readers still had to **hunt** for **what changed** and **where numbers live** in the **synthesis** layer. The gap is mostly **routing and signal**, not missing files: **too many valid pages**, **split entry points** (agency cluster vs local site intelligence), **epistemic hedging** repeated in multiple analyses, and the **MkDocs** build **neutralizing** `raw/` links so the public HTML site does not behave like Obsidian for corpus navigation.

**Related workflow**: [`docs/workflows/ingest.md`](../../docs/workflows/ingest.md); publishing: [`docs/operations/publishing.md`](../../docs/operations/publishing.md).

---

## What we checked

| Question | Finding |
|----------|---------|
| Did new material stay only in `raw/processed/`? | **No** for the **TN / UT / NASS / NRCS / FSA** batch: companion **source-notes** exist and point at stable `raw/` paths. The **risk** is **orphan raw** in other drops—always verify each processed file has a **source-note** + **log** entry. |
| Were source-notes created but not linked? | **Partially**. Notes are listed in [`index.md`](../index.md), but the **source-notes** section is **long**; without a **cluster** or **package** pointer, new rows **do not stand out**. The [`Authoritative execution evidence cluster — East Tennessee`](../source-notes/authoritative-execution-evidence-cluster-east-tennessee.md) mitigates this **if** readers know to open it. |
| Were canonical pages not updated? | **Synthesis lag** was real for **local** evidence: **county NASS** and **Campbell WSS** landed in **raw** first; **high-traffic** visibility required **follow-on** analyses, entities, and hubs (site intelligence, comparison, local router). That is **expected** for ingest (raw → note → synthesis), but **navigation** did not advertise the **two-step** path clearly enough. |
| Do relevant pages exist but stay hard to find? | **Yes**. The **evidence cluster** and **business plan package** both link authority material, but **MkDocs** generates navigation from the **tree**—readers who start at [`Planning framework`](east-tennessee-two-site-farm-business-plan-framework.md) may **never** see the **source index** unless they read the **package** or **overview** carefully. |
| Was county/site data treated too cautiously? | **Correctly cautious** on **parcel** claims (no invented deed facts). The **side effect** is **muted headlines**: repeated “estimate / not your lease / confirm AOI” language is **right** but **dilutes scan-ability** unless a **single** page states the **takeaway table** (NASS rows, WSS session scope) **once**, with caveats **below** the fold. |
| Does hub/index structure hide value? | **Index** lists everything; **signal** is the issue. **Two** parallel “homes” for evidence (**agency cluster** vs **local site router**) split **mental model**—readers need an explicit **split**: **regulatory / county statistics** vs **named-place intelligence**. |

---

## Root causes (information architecture)

1. **Ingest completes in layers** (`AGENTS.md`): raw → source-note → synthesis → index → log. **Visibility** spikes only when **step 3** touches **high-traffic** hubs; otherwise value sits in **correct but quiet** notes.
2. **Catalog scale**: Hundreds of `source-notes/` entries make **“what’s new”** invisible without **`log.md`** discipline or a **cluster** page.
3. **Publishing vs vault**: Public MkDocs **rewrites** `raw/` links ([`publishing.md`](../../docs/operations/publishing.md)); **primary PDFs** are not first-class navigation targets in HTML. **Synthesis must surface numbers** in wiki pages.
4. **Dual entry points** without a one-line **decision rule**: **Authoritative execution evidence cluster** (agency/extension catalog) vs **Local site and county intelligence** (Claxton/Demory/Anderson/Campbell routing).

---

## Remediation plan (durable)

| Priority | Action | Owner |
|---------|--------|--------|
| P0 | Keep **one** authoritative **index** ([`Authoritative execution evidence cluster`](../source-notes/authoritative-execution-evidence-cluster-east-tennessee.md)) as the **agency/extension** front door; **link it from** the **business plan package** and **overview** (already started—keep as mandatory stop). | Canonical hubs |
| P0 | Keep **one** **local router** ([`Local site and county intelligence`](../topics/local-site-and-county-intelligence.md)) for **named places + counties + validation**; **do not** duplicate long tables—link **out**. | Canonical hubs |
| P1 | Every **ingest batch**: append **`log.md`** with **file list** + **source-note paths** + **synthesis pages touched** (template already implied by `ingest` workflow). | Agents |
| P1 | On **large** PDF drops: ensure **`*-extracted.md`** exists and source-notes link **Machine extract** lines ([`ingest.md`](../../docs/workflows/ingest.md)). | Agents |
| P2 | Optional **“What changed”** line in **domain overview** or **package** when a batch lands—**one sentence**, not a new essay. | Canonical |

---

## Smallest page updates (this remediation)

Concrete, low-churn wiring applied alongside this analysis:

- **Package hub** [`east-tennessee-two-site-farm-business-plan.md`](../business-plan/east-tennessee-two-site-farm-business-plan.md): explicit **local router** next to **site intelligence** so **county vs site vs agency catalog** is one click from the spine.
- **Evidence cluster** [`authoritative-execution-evidence-cluster-east-tennessee.md`](../source-notes/authoritative-execution-evidence-cluster-east-tennessee.md): **“After ingest / how to read”** callout: package → cluster → local router → site intelligence.
- **[`index.md`](../index.md)**: **Business plan** subsection line tying **agency cluster** + **local router** (repeat for scan-ability).
- **[`overview.md`](../overview.md)**: clarify **item 10** — **agency catalog** vs **named-place** routing.

---

## Related

- [`Execution readiness gap audit — East Tennessee operational knowledge`](execution-readiness-gap-audit-east-tennessee-operational-knowledge.md)
- [`Domain content overview`](domain-content-overview.md) — Strand B / local layer
- [`Business plan source-ingest campaign — East Tennessee two-site`](business-plan-source-ingest-campaign-east-tennessee-two-site.md) — backlog-oriented companion (if present)
