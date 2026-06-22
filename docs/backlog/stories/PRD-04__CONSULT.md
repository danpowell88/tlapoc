# Synchronous consult record

> **Epic:** [PRD-04 — Consult, prescribing & S4 medicines governance (the moat)](../epics/PRD-04.md)  ·  **Key:** `PRD-04/CONSULT`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-02/CONSULT-GATE`, `PRD-03/GATING`

## Background

As a prescriber, I want to record a synchronous consult (in person or from our external telehealth app) before writing any script, so that every prescription is backed by a real assessment.
A Consult (in-person or external-telehealth) records modality, prescriber, timestamp, external reference and notes — required before any script (C1).

## How it works

A synchronous Consult is the legal precondition for any S4 prescription. It records modality (in-person or external-telehealth), prescriber, timestamp, an external reference (for telehealth) and notes, and must exist before a script can be written (C1).
The remote-prescriber path links an externally-conducted consult to the resulting script — the consult happens in the clinic's existing telehealth tool; this system records its details (ADR-0011).

## Requirements

- To record a synchronous consult (in person or from our external telehealth app) before writing any script.
- Compliance: [C1](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Consult records modality (in-person/telehealth-external), prescriber, timestamp, external reference, notes.
- [ ] A prescription cannot be saved without a linked synchronous consult at/just-before script time.
- [ ] The remote-prescriber path links the externally-conducted consult to the resulting script.
- [ ] Consult creation is audited.

## UI designs / screenshots

- Prototype: Charting pre-treatment review (charting.png) — the 'Consult & prescription' card with a 'Record consult' action and status tick; consult must be ticked before 'Write prescription' is usable.
- Modality toggle (in-person / telehealth-external) with an external-reference field for telehealth.

![charting — prototype screen](../screens/charting.png)

## Suggested data model

- **Consult** — id, tenant_id, client_id, appointment_id, prescriber_id, modality(in_person|telehealth_ext), at, external_ref, notes
  - _Required before any Prescription (C1); audited._

## Technical notes (high level)

- Architecture decisions: [ADR-0011](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-04-consult-prescribing-s4.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-04-consult-prescribing-s4.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations**
  Model + migrate (EF Core; every table carries tenant_id with an RLS policy):
  - Consult — id, tenant_id, client_id, appointment_id, prescriber_id, modality(in_person|telehealth_ext), at, external_ref, notes (Required before any Prescription (C1); audited.)
  - Add the FKs/relationships above; index the columns this story filters or looks up on; make records append-only/immutable where the story requires it.
- [ ] **Backend: domain logic, rules & API endpoint(s)**
  Domain logic + the API the web/Flutter clients call; enforce every rule server-side (never trust the UI):
  - Endpoints: the commands + queries for the entities above and each action in the acceptance criteria.
  - Rule: Consult records modality (in-person/telehealth-external), prescriber, timestamp, external reference, notes.
  - Rule: A prescription cannot be saved without a linked synchronous consult at/just-before script time.
  - Rule: The remote-prescriber path links the externally-conducted consult to the resulting script.
  - Emit domain events for read-models / notifications / follow-up jobs where relevant.
  - Publish the OpenAPI contract so the generated clients update.
  - Depends on: PRD-02/CONSULT-GATE, PRD-03/GATING.
- [ ] **Enforce compliance gate + audit events**
  Enforce C1 as a server-side invariant that cannot be bypassed via the API:
  - Block the action when prerequisites are missing; return a clear reason for the blocked-action banner (what's blocked / which rule / how to resolve / who can resolve).
  - Write an immutable AuditEvent for the attempt and its outcome.
  - A prescription cannot be saved without a linked synchronous consult at/just-before script time.
