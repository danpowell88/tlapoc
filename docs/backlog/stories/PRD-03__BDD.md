# BDD / psychological screening instrument

> **Epic:** [PRD-03 — Intake, consent & compliance gating](../epics/PRD-03.md)  ·  **Key:** `PRD-03/BDD`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-03/INTAKE`

## Background

As a RN/NP, I want a BDD/psychological screen completed and surfaced before I proceed, so that I can avoid harm for at-risk patients per the guidelines.
Cosmetic guidelines require BDD screening; a positive result must be surfaced to the prescriber before treatment (C3).

## Requirements

- A BDD/psychological screen completed and surfaced before I proceed.
- Compliance: [C3](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] A validated BDD/psychological screening instrument is embedded in intake.
- [ ] A completed screen authored/reviewed by an RN/NP is present before treatment.
- [ ] A positive flag is surfaced to the prescriber and recorded.
- [ ] Which instrument is used is configurable (open question to confirm).

## Technical notes (high level)

- Stack: .NET API (domain/services)

## Other

- Source PRD: [PRD-03-intake-consent-gating.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-03-intake-consent-gating.md)

## Tasks (dev pickup)

- [ ] **Domain logic & business rules** — Core behaviour + invariants.
- [ ] **API endpoint(s) + OpenAPI contract** — Wire request/response; regenerate clients.
- [ ] **Enforce compliance gate + audit events** — Server-side (C3); blocked path explains why.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
