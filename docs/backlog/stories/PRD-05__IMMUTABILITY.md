# Immutable finalisation & audited amendments

> **Epic:** [PRD-05 — Clinical charting: injection mapping & before/after](../epics/PRD-05.md)  ·  **Key:** `PRD-05/IMMUTABILITY`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-05/MAPPING`

## Background

As a injector, I want my finalised note to be locked, with later changes added as visible audited amendments, so that the clinical record is trustworthy and tamper-evident.
A finalised note is locked; any later change is an appended, audited amendment preserving the original (REQ-CLIN-4, ADR-0010).

## Requirements

- My finalised note to be locked, with later changes added as visible audited amendments.

## Acceptance Criteria

- [ ] A finalised note cannot be edited.
- [ ] An amendment creates a new linked, audited entry preserving the original.
- [ ] Finalisation happens server-side.
- [ ] The finalise close-out captures aftercare, recall, the 2-day wellbeing call and any adverse event.

## Technical notes (high level)

- Stack: .NET API (domain/services)
- Architecture decisions: [ADR-0010](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-05-clinical-charting.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-05-clinical-charting.md)

## Tasks (dev pickup)

- [ ] **Domain logic & business rules** — Core behaviour + invariants.
- [ ] **API endpoint(s) + OpenAPI contract** — Wire request/response; regenerate clients.
- [ ] **Enforce compliance gate + audit events** — Server-side (see Other); blocked path explains why.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
