# Standardised before/after photos + compare

> **Epic:** [PRD-05 — Clinical charting: injection mapping & before/after](../epics/PRD-05.md)  ·  **Key:** `PRD-05/PHOTOS`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** provider-app
>
> **Depends on:** `PRD-03/IMAGE-CONSENT`

## Background

As a injector, I want to capture standardised before/after photos and compare them against prior visits, so that I can track outcomes consistently.
Capture standardised before/after photos room-side (framing/ghosting guide), compare side-by-side across visits; media stored centrally via signed URLs, never on personal devices, gated by image-use consent (REQ-CLIN-3, C14/ADR-0009).

## Requirements

- To capture standardised before/after photos and compare them against prior visits.
- Compliance: [C14](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Camera/upload with standardised framing/ghosting guide; side-by-side compare across visits.
- [ ] Capture requires current image-use consent (PRD-03).
- [ ] Photos stored centrally via signed URLs; never persisted on device beyond a transient sync cache.
- [ ] Annotation supported.

## UI designs / screenshots

prototype.html — Charting + Clinical (Skin analysis, Body contouring, Complication protocols, Photography & outcomes); treatment-room.html.

## Technical notes (high level)

- Stack: Flutter provider app
- Architecture decisions: [ADR-0009](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-05-clinical-charting.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-05-clinical-charting.md)

## Tasks (dev pickup)

- [ ] **Enforce compliance gate + audit events** — Server-side (C14); blocked path explains why.
- [ ] **Provider app UI (Flutter)**
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
