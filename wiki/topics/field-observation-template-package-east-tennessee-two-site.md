---
title: Field observation template package — two-site
page_type: topic
status: active
created: 2026-04-17
updated: 2026-04-25
tags:
  - two-site
  - field-work
  - templates
  - execution
review_status: unreviewed
confidence: high
---

# Field observation template package — two-site

**Purpose**: **Repeatable** forms for **walk-the-fence**, **utility recon**, and **load spot-checks** at **`SITE_HOME`** (Claxton) and **`SITE_FARM`** (Demory). Copy a block into `raw/inbox/` (dated filename) or a field notebook; after review, **promote** facts via [`Parcel evidence intake and validation workflow`](../analyses/parcel-evidence-intake-and-validation-workflow-east-tennessee-two-site.md).

**Package**: [`Local evidence package — East Tennessee two-site`](local-evidence-package-east-tennessee-two-site.md).

**Targets**: [`Site inventory — Claxton`](../analyses/site-inventory-baseline-claxton-home-base-east-tennessee.md) · [`Site inventory — Demory`](../analyses/site-inventory-baseline-demory-farm-site-east-tennessee.md) · [`Infrastructure baseline`](../analyses/infrastructure-inventory-baseline-two-sites-east-tennessee.md) · [`Utility baseline`](../analyses/utility-and-service-baseline-two-sites-east-tennessee.md) · [`Loads register`](../analyses/loads-register-known-estimated-unknown-two-sites-east-tennessee.md).

**Before digging or trenching**: review TN **811** process captures in [`Inbox batch — Frigate, SOPS, Prometheus, TN811, NRCS/UT (2026-04-18)`](../source-notes/inbox-batch-2026-04-18-frigate-sops-prometheus-alertmanager-tenn811-nrcs-ut-extension.md) — **ticket** + **Positive Response** are **project** artifacts, not wiki text.

---

## A. Visit header (every trip)

```markdown
## Field visit — [SITE_HOME | SITE_FARM] — YYYY-MM-DD

**Observers**:
**Weather / ground conditions**:
**Route / access notes**:
**Safety** (PPE, animals, equipment):
**Photos** (roll ID / folder):
```

---

## B. Fence and boundary walk

| Segment | Start/end landmark | Length est. | Post spacing | Wire condition | Gate ID | Fact class (measured / observed / reported) | Photo ref |
|---------|-------------------|-------------|--------------|----------------|---------|-----------------------------------------------|-----------|
| | | | | | | | |

**Unknowns to flag**: missing stakes, ambiguous corners, water along fence.

---

## C. Water points

| Point ID | GPS or landmark | Type | Flow (bucket test / gpm) | Freeze protection | Leaks | Blocks |
|----------|-----------------|------|----------------------------|-------------------|-------|--------|
| | | | | | | |

---

## D. Electrical quick audit (non-contact until qualified)

| Panel location | Main breaker A | Visible labels OK? | Obvious hazards | Generator / transfer | Notes |
|----------------|----------------|-------------------|-----------------|----------------------|-------|
| | | | | | |

**Safety**: **Do not** open energized panels without qualification; **Unknown** is acceptable.

---

## E. Load spot-check (clamp meter session)

| Load ID (link loads register) | Circuit | V | A steady | A start | Time | Fact class |
|-------------------------------|---------|---|----------|---------|------|------------|
| | | | | | | |

---

## F. Utility desk follow-up (same week)

| Provider | Account verified? | Rate tariff noted? | Bill period | kWh | Demand kW | Anomalies |
|----------|-------------------|--------------------|-------------|-----|-----------|-----------|
| | | | | | | |

---

## After the visit

1. File **raw** note with **date** and **site** in path per [`ingest workflow`](../../docs/workflows/ingest.md) (if used).
2. Add or update **source-note** under `wiki/source-notes/` pointing at stable `raw/` path.
3. **Patch** the relevant **baseline** table row—**measured** vs **reported** with **date**.
4. Append **`wiki/log.md`** with short **ingest** line.

---

## Related

- [`Claxton and Demory — missing data register`](../analyses/claxton-and-demory-missing-data-register.md) · [`Execution dossier hub`](../analyses/execution-dossier-hub-phase-0-1-east-tennessee.md)
