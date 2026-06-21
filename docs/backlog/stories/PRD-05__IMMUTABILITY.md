# Immutable finalisation & audited amendments

> **Epic:** [PRD-05 — Clinical charting: injection mapping & before/after](../epics/PRD-05.md)  ·  **Key:** `PRD-05/IMMUTABILITY`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-05/MAPPING`

## Background

As a injector, I want my finalised note to be locked, with later changes added as visible audited amendments, so that the clinical record is trustworthy and tamper-evident.
A finalised note is locked; any later change is an appended, audited amendment preserving the original (REQ-CLIN-4, ADR-0010).

## How it works

A finalised note is locked; any later change is an appended, audited amendment that preserves the original (ADR-0010). Finalisation happens server-side, and the finalise close-out captures aftercare, recall, the 2-day wellbeing call and any adverse event.
This tamper-evidence is what makes the clinical record trustworthy in an inspection.

## Requirements

- My finalised note to be locked, with later changes added as visible audited amendments.

## Acceptance Criteria

- [ ] A finalised note cannot be edited.
- [ ] An amendment creates a new linked, audited entry preserving the original.
- [ ] Finalisation happens server-side.
- [ ] The finalise close-out captures aftercare, recall, the 2-day wellbeing call and any adverse event.

## UI designs / screenshots

- Prototype: Charting 'Finalise & checkout' (charting.png) — 'Finalising locks the note and deducts the units used from the selected lot'; finalised notes render read-only with an amendment trail.
- Read-only oversight view for non-editors (e.g. owner).

![charting — prototype screen](../screens/charting.png)

## Suggested data model

- **ChartEntry.locked** — + finalised_at
  - _No edit after final._
- **Amendment** — id, chart_entry_id, author_id, created_at, reason, payload
  - _Append-only; original preserved._

## Technical notes (high level)

- Architecture decisions: [ADR-0010](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-05-clinical-charting.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-05-clinical-charting.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations** — Entities/columns + relationships; tenant_id + RLS.
- [ ] **Backend: domain logic, rules & API endpoint(s)** — Behaviour + invariants + the OpenAPI contract the UI/clients consume.
- [ ] **Enforce compliance gate + audit events** — Server-side (see Other); blocked path explains why.
