# Standardised before/after photos + compare

> **Epic:** [PRD-05 — Clinical charting: injection mapping & before/after](../epics/PRD-05.md)  ·  **Key:** `PRD-05/PHOTOS`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** provider-app
>
> **Depends on:** `PRD-03/IMAGE-CONSENT`

## Background

Clinical charting: injection mapping & before/after — The clinical record that matches the Aesthetic Record / Pabau bar: a guided charting flow opening with product & lot selection, on-image/diagram injection mapping (product · units · depth · site · batch-lot), standardised before/after photos with comparison, immutable finalised notes with audited amendments, and adverse-event logging that feeds the TGA/DAEN pathway

As a injector, I want to capture standardised before/after photos and compare them against prior visits, so that I can track outcomes consistently.

Capture standardised before/after photos room-side (framing/ghosting guide), compare side-by-side across visits; media stored centrally via signed URLs, never on personal devices, gated by image-use consent (REQ-CLIN-3, C14/ADR-0009).

## Requirements

- To capture standardised before/after photos and compare them against prior visits.
- Traces to requirement(s): REQ-CLIN-3.
- Must satisfy compliance obligation(s): C14.

## Acceptance Criteria

- [ ] Camera/upload with standardised framing/ghosting guide; side-by-side compare across visits.
- [ ] Capture requires current image-use consent (PRD-03).
- [ ] Photos stored centrally via signed URLs; never persisted on device beyond a transient sync cache.
- [ ] Annotation supported.

## UI designs / screenshots

prototype.html — Charting + Clinical (Skin analysis, Body contouring, Complication protocols, Photography & outcomes); treatment-room.html.

## Technical notes (high level)

Stack: Flutter provider app.
Architecture decisions: ADR-0009 (see docs/adr/decision-log.md).
Depends on: PRD-03/IMAGE-CONSENT.

## Other

Epic: PRD-05 — Clinical charting: injection mapping & before/after.
Source PRD: docs/prds/PRD-05-clinical-charting.md.
Backlog key: PRD-05/PHOTOS.
Phase: 1 · Priority: P1 · Estimate: 3 pts.
Compliance criteria: C14.

## Tasks (dev pickup)

- [ ] **Enforce compliance gate + audit events** — Server-side (C14); blocked path explains why.
- [ ] **Provider app UI (Flutter)**
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
