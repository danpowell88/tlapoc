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

- [ ] **Data model & migrations** — Entities/columns + relationships; tenant_id + RLS.
- [ ] **Backend: domain logic, rules & API endpoint(s)** — Behaviour + invariants + the OpenAPI contract the UI/clients consume.
- [ ] **Enforce compliance gate + audit events** — Server-side (C3); blocked path explains why.
