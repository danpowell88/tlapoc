# Roster: engagement-type recording for attribution

> **Epic:** [PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model)](../epics/PRD-01.md)  ·  **Key:** `PRD-01/ROSTER-ENGAGEMENT`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-01/ROSTER`

## Background

As a manager, I want each staff member's engagement type (employee / contractor) recorded, so that downstream revenue attribution and the contractor compliance banner can use it.
Plainly: recording whether each staff member is an employee or a contractor, so downstream revenue attribution and the contractor compliance banner can use it — without the app becoming a payroll system. Where it fits: a follow-up to the roster core (PRD-01/ROSTER); the engagement-type field already lives on StaffProfile (from PRD-01/CREDENTIALS), so this story is the deliberate recording of it for downstream use. Explicitly attribution only: the platform attributes revenue by engagement type but is NOT a payroll/super engine (ADR-0027).

## How it works

Each staff member's engagement type (employee / contractor) is recorded for downstream use — it already lives on StaffProfile from PRD-01/CREDENTIALS, so this story is its deliberate capture and exposure rather than a new field. It feeds downstream commission/pay attribution and the contractor compliance banner (ADR-0027).
The boundary is explicit: the platform attributes revenue by engagement type but is NOT a payroll/super engine (ADR-0027) — there is no payroll or commission UI here; the attribution itself happens downstream (Reporting / Xero). This story only makes the engagement type a first-class, recorded input.

## Requirements

- Each staff member's engagement type (employee / contractor) recorded.

## Acceptance Criteria

- [ ] Engagement type (employee / contractor) is recorded per staff member (already on StaffProfile from CREDENTIALS).
- [ ] The engagement type is available to downstream commission/pay attribution and the contractor compliance banner.
- [ ] No payroll / commission UI here — attribution is downstream.
- [ ] The platform attributes revenue by engagement type but is explicitly not a payroll/super engine (ADR-0027).

## UI designs / screenshots

- Prototype: engagement type (Contractor/Employee) shown on the People & credentials card (team-people.png); recorded per staff member.
- No payroll/commission UI here — the engagement type is an input to downstream attribution and the contractor compliance banner (ADR-0027).

## Suggested data model

- **StaffProfile (extends PRD-01/CREDENTIALS)** — uses existing engagement_type(employee|contractor)
  - _No new entity — records/exposes the engagement type already on StaffProfile for downstream attribution; the platform is not a payroll engine (ADR-0027)._

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Engagement-type recording for downstream attribution**
  Behaviour: record each staff member's engagement type (employee/contractor) — it already lives on StaffProfile from CREDENTIALS — for downstream commission/pay attribution and the contractor compliance banner. Requirements: the platform attributes revenue by engagement type but is explicitly NOT a payroll/super engine (ADR-0027); no payroll/commission UI here — attribution is downstream.
