# Treatment plans & protocol templates

> **Epic:** [PRD-05 — Clinical charting: injection mapping & before/after](../epics/PRD-05.md)  ·  **Key:** `PRD-05/TREATMENT-PLANS`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** provider-app
>
> **Depends on:** `PRD-05/NOTE-TEMPLATE`

## Background

As a injector, I want to build multi-session treatment plans from protocol templates, so that ongoing care is structured and drives recall.
Multi-session treatment plans + applyable protocol templates feed recall and structure ongoing care (REQ-CLIN-7).

## Requirements

- To build multi-session treatment plans from protocol templates.

## Acceptance Criteria

- [ ] Protocol templates can be applied to create a multi-session plan.
- [ ] Plans feed the recall worklist (PRD-07).
- [ ] Plan progress is visible on the client 360.
- [ ] A charting overview / 'in-room now' entry point lists active plans.

## UI designs / screenshots

prototype.html — Charting + Clinical (Skin analysis, Body contouring, Complication protocols, Photography & outcomes); treatment-room.html.

## Technical notes (high level)

- Stack: Flutter provider app
- Architecture decisions: [ADR-0024](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-05-clinical-charting.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-05-clinical-charting.md)

## Tasks (dev pickup)

- [ ] **Provider app UI (Flutter)**
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
