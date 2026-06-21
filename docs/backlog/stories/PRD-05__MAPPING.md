# Injection-mapping canvas (per-point lot)

> **Epic:** [PRD-05 — Clinical charting: injection mapping & before/after](../epics/PRD-05.md)  ·  **Key:** `PRD-05/MAPPING`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** provider-app
>
> **Depends on:** `SPRINT-0/SPIKE-CANVAS`, `PRD-04/RECALL-LOOKUP`

## Background

As a injector, I want to drop and drag injection points on a facial diagram or photo, each recording product, units, depth, technique and lot, so that the treatment is precisely charted and traceable to a batch.
On a facial diagram and/or patient photo, tap-to-add and drag injection points, each capturing product, units, depth, technique and batch-lot/expiry; charted units deduct from the selected lot on finalise (REQ-CLIN-2, C8).

## Requirements

- To drop and drag injection points on a facial diagram or photo, each recording product, units, depth, technique and lot.
- Compliance: [C8](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Charting opens with product & batch (lot) selection, restricted to in-date/ARTG/in-custody stock.
- [ ] Each point records product, units, depth, technique and batch-lot/expiry.
- [ ] On finalise, charted units deduct from the selected lot and link to the medicine register + recall (PRD-04).
- [ ] Built on the SPIKE-CANVAS approach; performs smoothly with many points.

## UI designs / screenshots

prototype.html — Charting + Clinical (Skin analysis, Body contouring, Complication protocols, Photography & outcomes); treatment-room.html.

## Technical notes (high level)

- Stack: Flutter provider app

## Other

- Source PRD: [PRD-05-clinical-charting.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-05-clinical-charting.md)

## Tasks (dev pickup)

- [ ] **Enforce compliance gate + audit events** — Server-side (C8); blocked path explains why.
- [ ] **Provider app UI (Flutter)**
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
