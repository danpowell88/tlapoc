# Individual prescription (no batch / no async)

> **Epic:** [PRD-04 — Consult, prescribing & S4 medicines governance (the moat)](../epics/PRD-04.md)  ·  **Key:** `PRD-04/PRESCRIPTION`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-04/CONSULT`, `PRD-01/CREDENTIALS`

## Background

As a prescriber, I want to write an individual prescription for this patient tied to their consult, so that prescribing is lawful and patient-specific.
An individual prescription per client per consult — never batch/standing-order, never async (text/email/online-only) (C2). Supports the designated RN prescriber identity.

## How it works

An individual prescription is written per client per consult — never a batch/standing-order, never async (text/email/online-only) (C2). The prescriber may be an NP, a remote prescriber, or a designated RN prescriber (QLD endorsement, recorded with a partnered prescriber).
Off-label is flagged on the script and requires consent that covers off-label use. The script is the authority an RN administers against.

## Requirements

- To write an individual prescription for this patient tied to their consult.
- Compliance: [C2](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria), [C5](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] One prescription per client per consult; applying one script to multiple clients is rejected.
- [ ] Standing-order/batch scripts and async-only prescribing are impossible to create.
- [ ] Prescriber may be NP, remote prescriber, or designated RN prescriber (with recorded partnered prescriber).
- [ ] Off-label is flagged on the script and requires consent covering off-label use.

## UI designs / screenshots

- Prototype: Charting -> 'Write prescription' (charting.png) — product, dose/units, off-label flag; tied to the just-recorded consult and this single client.
- Attempting a batch/standing-order or applying one script to multiple clients is rejected with a reason.

![charting — prototype screen](../screens/charting.png)

## Suggested data model

- **Prescription** — id, tenant_id, client_id, consult_id, prescriber_id, product_id, dose_units, off_label(bool), status(active|consumed|expired), created_at
  - _One per client per consult; no batch/async (C2). Designated RN prescriber records partnered_prescriber_id._

## Other

- Source PRD: [PRD-04-consult-prescribing-s4.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-04-consult-prescribing-s4.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations**
  Model + migrate (EF Core; every table carries tenant_id with an RLS policy):
  - Prescription — id, tenant_id, client_id, consult_id, prescriber_id, product_id, dose_units, off_label(bool), status(active|consumed|expired), created_at (One per client per consult; no batch/async (C2). Designated RN prescriber records partnered_prescriber_id.)
  - Add the FKs/relationships above; index the columns this story filters or looks up on; make records append-only/immutable where the story requires it.
- [ ] **Backend: domain logic, rules & API endpoint(s)**
  Domain logic + the API the web/Flutter clients call; enforce every rule server-side (never trust the UI):
  - Endpoints: the commands + queries for the entities above and each action in the acceptance criteria.
  - Rule: One prescription per client per consult; applying one script to multiple clients is rejected.
  - Rule: Standing-order/batch scripts and async-only prescribing are impossible to create.
  - Rule: Prescriber may be NP, remote prescriber, or designated RN prescriber (with recorded partnered prescriber).
  - Emit domain events for read-models / notifications / follow-up jobs where relevant.
  - Publish the OpenAPI contract so the generated clients update.
  - Depends on: PRD-04/CONSULT, PRD-01/CREDENTIALS.
- [ ] **Enforce compliance gate + audit events**
  Enforce C2, C5 as a server-side invariant that cannot be bypassed via the API:
  - Block the action when prerequisites are missing; return a clear reason for the blocked-action banner (what's blocked / which rule / how to resolve / who can resolve).
  - Write an immutable AuditEvent for the attempt and its outcome.
  - One prescription per client per consult; applying one script to multiple clients is rejected.
  - Standing-order/batch scripts and async-only prescribing are impossible to create.
  - Off-label is flagged on the script and requires consent covering off-label use.
