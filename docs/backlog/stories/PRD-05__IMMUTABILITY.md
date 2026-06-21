# Immutable finalisation & audited amendments

> **Epic:** [PRD-05 — Clinical charting: injection mapping & before/after](../epics/PRD-05.md)  ·  **Key:** `PRD-05/IMMUTABILITY`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-05/MAPPING`

## Background

Clinical charting: injection mapping & before/after — The clinical record that matches the Aesthetic Record / Pabau bar: a guided charting flow opening with product & lot selection, on-image/diagram injection mapping (product · units · depth · site · batch-lot), standardised before/after photos with comparison, immutable finalised notes with audited amendments, and adverse-event logging that feeds the TGA/DAEN pathway

As a injector, I want my finalised note to be locked, with later changes added as visible audited amendments, so that the clinical record is trustworthy and tamper-evident.

A finalised note is locked; any later change is an appended, audited amendment preserving the original (REQ-CLIN-4, ADR-0010).

## Requirements

- My finalised note to be locked, with later changes added as visible audited amendments.
- Traces to requirement(s): REQ-CLIN-4.
- Must satisfy compliance obligation(s): see Other.

## Acceptance Criteria

- [ ] A finalised note cannot be edited.
- [ ] An amendment creates a new linked, audited entry preserving the original.
- [ ] Finalisation happens server-side.
- [ ] The finalise close-out captures aftercare, recall, the 2-day wellbeing call and any adverse event.

## UI designs / screenshots

prototype.html — Charting + Clinical (Skin analysis, Body contouring, Complication protocols, Photography & outcomes); treatment-room.html.

## Technical notes (high level)

Stack: .NET API (domain/services).
Architecture decisions: ADR-0010 (see docs/adr/decision-log.md).
Depends on: PRD-05/MAPPING.

## Other

Epic: PRD-05 — Clinical charting: injection mapping & before/after.
Source PRD: docs/prds/PRD-05-clinical-charting.md.
Backlog key: PRD-05/IMMUTABILITY.
Phase: 1 · Priority: P0 · Estimate: 5 pts.

## Tasks (dev pickup)

- [ ] **Domain logic & business rules** — Core behaviour + invariants.
- [ ] **API endpoint(s) + OpenAPI contract** — Wire request/response; regenerate clients.
- [ ] **Enforce compliance gate + audit events** — Server-side (see Other); blocked path explains why.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
