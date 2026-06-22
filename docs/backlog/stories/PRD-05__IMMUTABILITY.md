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

- [ ] **Data model & migrations**
  Model + migrate (EF Core; every table carries tenant_id with an RLS policy):
  - ChartEntry.locked — + finalised_at (No edit after final.)
  - Amendment — id, chart_entry_id, author_id, created_at, reason, payload (Append-only; original preserved.)
  - Add the FKs/relationships above; index the columns this story filters or looks up on; make records append-only/immutable where the story requires it.
- [ ] **Backend: domain logic, rules & API endpoint(s)**
  Domain logic + the API the web/Flutter clients call; enforce every rule server-side (never trust the UI):
  - Endpoints: the commands + queries for the entities above and each action in the acceptance criteria.
  - Rule: A finalised note cannot be edited.
  - Rule: An amendment creates a new linked, audited entry preserving the original.
  - Rule: Finalisation happens server-side.
  - Emit domain events for read-models / notifications / follow-up jobs where relevant.
  - Publish the OpenAPI contract so the generated clients update.
  - Depends on: PRD-05/MAPPING.
- [ ] **Enforce compliance gate + audit events**
  Enforce the relevant criteria as a server-side invariant that cannot be bypassed via the API:
  - Block the action when prerequisites are missing; return a clear reason for the blocked-action banner (what's blocked / which rule / how to resolve / who can resolve).
  - Write an immutable AuditEvent for the attempt and its outcome.
  - A finalised note cannot be edited.
