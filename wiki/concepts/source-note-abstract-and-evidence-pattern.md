---
title: Source-note abstract and evidence pattern
page_type: concept
status: active
created: 2026-04-18
updated: 2026-04-25
tags:
  - meta
  - source-notes
  - provenance
  - authoring
review_status: unreviewed
confidence: high
---

# Source-note abstract and evidence pattern

**Purpose**: A **lightweight**, **repeatable** block for `wiki/source-notes/` so **cluster** and **batch** notes are scannable in **Obsidian** and **MkDocs**, and **claims** remain intelligible when public builds **neutralize** navigable `raw/` links (see [`docs/operations/raw-corpus-and-publishing.md`](../../docs/operations/raw-corpus-and-publishing.md)).

**When to use**: **Hub / index** source-notes (multiple `raw/` paths), **official** documentation clusters, and **high-friction** batches—not necessarily every **single-file** note.

---

## Optional frontmatter hints

Authors may add tags such as `source_cluster: authoritative` or keep existing `confidence` / `review_status`. No new **required** fields for validation.

---

## Evidence summary block (template)

Place **after** the H1 title and **before** long tables, or **immediately after** a short **Purpose** paragraph.

```markdown
## Evidence summary

| Field | Content |
|-------|---------|
| **Abstract** | 2–4 sentences: what this cluster covers and why it exists. |
| **Authority mix** | One line: e.g. `agency + extension + vendor docs (captured)` or `official docs + community (supporting only)`. |
| **Decision relevance** | Bullet list: which **decisions** or **gates** this evidence supports (or does *not* support). |
| **Canonical wiki links** | Bullet list: **synthesis** pages readers should read first. |

**Key claims** (public-safe; cite *authority*, not only paths):

- Claim one (e.g. “NASS publishes county-level cash rent tables for TN—survey year stated in source-note body”).
- Claim two.

**Open questions / follow-ups**

- What remains unknown, unverified, or pending ingest.
```

**Shorter variant** (single cluster row in a parent index): use only **Abstract**, **Authority mix**, and **Canonical wiki links** in a **mini table** under the cluster heading.

---

## Authority vocabulary (align with evidence grade)

Use the same **plain-language** bands as [`Evidence grade and canonical authority`](evidence-grade-and-canonical-authority.md):

- **Official / agency / extension**: USDA, NRCS, land-grant Extension, primary statutes as cited.
- **Vendor primary**: upstream project docs, datasheets—**good for product facts**, not **regulatory** conclusions alone.
- **Community / anecdotal**: forums, blogs—**ideas and failure-mode color** only unless corroborated.

---

## Examples in this vault

Notes **updated** to demonstrate the pattern (non-exhaustive):

- [`Authoritative execution evidence cluster — East Tennessee`](../source-notes/authoritative-execution-evidence-cluster-east-tennessee.md)
- [`Backup / DR — official documentation cluster`](../source-notes/backup-dr-official-documentation-cluster.md)
- [`Off-grid power, field RF, and optional WAN — source index (Demory planning)`](../source-notes/off-grid-power-rf-wan-source-index-demory-planning-2026-04.md)
- [`Authoritative roads and driveways — source cluster`](../source-notes/authoritative-roads-and-driveways-source-cluster.md)
- [`Inbox batch — Frigate, SOPS, Prometheus, TN811, NRCS/UT (2026-04-18)`](../source-notes/inbox-batch-2026-04-18-frigate-sops-prometheus-alertmanager-tenn811-nrcs-ut-extension.md)
- [`Demory farm sensor layer — official and operator-grade source cluster`](../source-notes/demory-farm-sensor-layer-official-and-operator-source-cluster.md)
- [`Tennessee two-site — official parcel, GIS, flood, and climate portals`](../source-notes/tennessee-two-site-official-parcel-gis-flood-climate-portals.md)
- [`Electrical, networking, and Starlink — inbox batch (2026-04-23)`](../source-notes/electrical-networking-starlink-inbox-batch-2026-04-23.md)
- [`Inbox batch — Tennessee farm policy, LoRaWAN… (2026-04-18)`](../source-notes/inbox-batch-2026-04-18-tennessee-farm-lorawan-chirpstack-meshtastic-decentlab-halow.md)
- [`K3s, Longhorn, Rancher, Raspberry Pi — platform captures`](../source-notes/k3s-longhorn-rancher-pi-platform-official-captures-inbox-2026-04-18.md)
- [`Grafana Alloy — official documentation (primary reference)`](../source-notes/grafana-alloy-official-documentation-primary-reference.md)

---

## See also

- [`Usability and navigation audit — 2026-04-18`](../analyses/usability-and-navigation-audit-2026-04-18.md)
- [`Source authority hardening audit`](../analyses/source-authority-hardening-audit.md)
- [`Glossary — Evidence grade`](../glossary/evidence-grade.md)
