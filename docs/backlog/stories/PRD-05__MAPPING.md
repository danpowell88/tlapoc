# Injection-mapping canvas (per-point lot)

> **Epic:** [PRD-05 — Clinical charting: injection mapping & before/after](../epics/PRD-05.md)  ·  **Key:** `PRD-05/MAPPING`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** provider-app
>
> **Depends on:** `SPRINT-0/SPIKE-CANVAS`, `PRD-04/RECALL-LOOKUP`

## Background

Clinical charting: injection mapping & before/after — The clinical record that matches the Aesthetic Record / Pabau bar: a guided charting flow opening with product & lot selection, on-image/diagram injection mapping (product · units · depth · site · batch-lot), standardised before/after photos with comparison, immutable finalised notes with audited amendments, and adverse-event logging that feeds the TGA/DAEN pathway

As a injector, I want to drop and drag injection points on a facial diagram or photo, each recording product, units, depth, technique and lot, so that the treatment is precisely charted and traceable to a batch.

On a facial diagram and/or patient photo, tap-to-add and drag injection points, each capturing product, units, depth, technique and batch-lot/expiry; charted units deduct from the selected lot on finalise (REQ-CLIN-2, C8).

## Requirements

- To drop and drag injection points on a facial diagram or photo, each recording product, units, depth, technique and lot.
- Traces to requirement(s): REQ-CLIN-2, REQ-MED-4.
- Must satisfy compliance obligation(s): C8.

## Acceptance Criteria

- [ ] Charting opens with product & batch (lot) selection, restricted to in-date/ARTG/in-custody stock.
- [ ] Each point records product, units, depth, technique and batch-lot/expiry.
- [ ] On finalise, charted units deduct from the selected lot and link to the medicine register + recall (PRD-04).
- [ ] Built on the SPIKE-CANVAS approach; performs smoothly with many points.

## UI designs / screenshots

prototype.html — Charting + Clinical (Skin analysis, Body contouring, Complication protocols, Photography & outcomes); treatment-room.html.

## Technical notes (high level)

Stack: Flutter provider app.
Depends on: SPRINT-0/SPIKE-CANVAS, PRD-04/RECALL-LOOKUP.

## Other

Epic: PRD-05 — Clinical charting: injection mapping & before/after.
Source PRD: docs/prds/PRD-05-clinical-charting.md.
Backlog key: PRD-05/MAPPING.
Phase: 1 · Priority: P0 · Estimate: 5 pts.
Compliance criteria: C8.

## Tasks (dev pickup)

- [ ] **Enforce compliance gate + audit events** — Server-side (C8); blocked path explains why.
- [ ] **Provider app UI (Flutter)**
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
