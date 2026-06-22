# Complaint → indefinite retention flag

> **Epic:** [PRD-11 — Facility, infection-control, emergency & complaints](../epics/PRD-11.md)  ·  **Key:** `PRD-11/COMPLAINT-RETENTION`  ·  **Type:** Story  ·  **Stage:** M6  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** —
>
> **Depends on:** `PRD-11/COMPLAINTS`, `PRD-01/PRIVACY-RIGHTS`

## Background

As a manager, I want a logged complaint to keep the related record from being destroyed, so that we retain everything tied to a complaint for as long as it exists.
Plainly: logging a complaint must keep the related record from being destroyed for as long as the complaint exists. Where it fits: a follow-up to the complaints register (PRD-11/COMPLAINTS) that wires the indefinite-retention flag into the foundations retention engine (PRD-01); the engine reads the flag and exempts the record from the normal destruction schedule. A compliance control (C18).

## How it works

A complaint must keep the related record from being destroyed: logging a complaint (PRD-11/COMPLAINTS) sets an indefinite-retention flag on the related record. The PRD-01 retention engine reads it and exempts that record from the normal destruction schedule for as long as the complaint exists (C18).
This is the retention arm of the complaints workflow, separate from the reporting hooks (COMPLAINT-REPORTING). Setting and clearing the flag is audited.

## Requirements

- A logged complaint to keep the related record from being destroyed.

## Acceptance Criteria

- [ ] Logging a complaint sets an indefinite-retention flag on the related record.
- [ ] The PRD-01 retention engine reads the flag and exempts that record from the normal destruction schedule.
- [ ] The exemption holds for as long as the complaint exists (C18).
- [ ] Setting/clearing the flag is audited.

## UI designs / screenshots

- Prototype: Governance — a logged complaint marks the related record as indefinitely retained.
- PRD-01 retention engine exempts the flagged record from destruction; flag changes audited.

![ops-openclose — prototype screen](../screens/ops-openclose.png)

## Suggested data model

- **(reuses) Complaint + RetentionRule** — PRD-11/COMPLAINTS complaint sets an indefinite-retention flag read by the PRD-01 retention engine
  - _Extends COMPLAINTS; exempts the related record from destruction for the complaint's life (C18)._

## Other

- Source PRD: [PRD-11-facility-complaints.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-11-facility-complaints.md)

## Tasks (dev pickup)

- [ ] **Complaint → indefinite retention flag**
  Behaviour: a complaint must keep the related record from being destroyed. Requirements: logging a complaint sets an indefinite-retention flag on the related record; the PRD-01 retention engine reads it and exempts that record from the normal destruction schedule for as long as the complaint exists (C18).
