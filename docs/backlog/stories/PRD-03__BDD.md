# BDD / psychological screening instrument

> **Epic:** [PRD-03 — Intake, consent & compliance gating](../epics/PRD-03.md)  ·  **Key:** `PRD-03/BDD`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-03/INTAKE`

## Background

As a RN/NP, I want a BDD/psychological screen completed and surfaced before I proceed, so that I can avoid harm for at-risk patients per the guidelines.
Cosmetic guidelines require BDD screening; a positive result must be surfaced to the prescriber before treatment (C3).

## How it works

Cosmetic guidelines require screening for Body Dysmorphic Disorder. A validated BDD/psychological instrument is embedded in intake; a completed screen authored/reviewed by an RN/NP must be present before treatment, and a positive flag is surfaced to the prescriber.
Which validated instrument to embed is an open question to confirm clinically.

## Requirements

- A BDD/psychological screen completed and surfaced before I proceed.
- Compliance: [C3](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] A validated BDD/psychological screening instrument is embedded in intake.
- [ ] A completed screen authored/reviewed by an RN/NP is present before treatment.
- [ ] A positive flag is surfaced to the prescriber and recorded.
- [ ] Which instrument is used is configurable (open question to confirm).

## UI designs / screenshots

- Client app: the BDD/wellbeing screen within the intake wizard (client-app.png).
- Charting pre-treatment review (charting.png) shows a 'BDD screen: clear' / flagged chip to the prescriber.

![forms-consent — prototype screen](../screens/forms-consent.png)

## Suggested data model

- **ScreeningResult** — id, tenant_id, client_id, instrument, answers(json), score, flag(bool), reviewed_by, reviewed_at
  - _Positive flag surfaced to prescriber; required before treatment (C3)._

## Other

- Source PRD: [PRD-03-intake-consent-gating.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-03-intake-consent-gating.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations**
  Model + migrate (EF Core; every table carries tenant_id with an RLS policy):
  - ScreeningResult — id, tenant_id, client_id, instrument, answers(json), score, flag(bool), reviewed_by, reviewed_at (Positive flag surfaced to prescriber; required before treatment (C3).)
  - Add the FKs/relationships above; index the columns this story filters or looks up on; make records append-only/immutable where the story requires it.
- [ ] **Backend: domain logic, rules & API endpoint(s)**
  Domain logic + the API the web/Flutter clients call; enforce every rule server-side (never trust the UI):
  - Endpoints: the commands + queries for the entities above and each action in the acceptance criteria.
  - Rule: A validated BDD/psychological screening instrument is embedded in intake.
  - Rule: A completed screen authored/reviewed by an RN/NP is present before treatment.
  - Rule: A positive flag is surfaced to the prescriber and recorded.
  - Emit domain events for read-models / notifications / follow-up jobs where relevant.
  - Publish the OpenAPI contract so the generated clients update.
  - Depends on: PRD-03/INTAKE.
- [ ] **Enforce compliance gate + audit events**
  Enforce C3 as a server-side invariant that cannot be bypassed via the API:
  - Block the action when prerequisites are missing; return a clear reason for the blocked-action banner (what's blocked / which rule / how to resolve / who can resolve).
  - Write an immutable AuditEvent for the attempt and its outcome.
  - A validated BDD/psychological screening instrument is embedded in intake.
