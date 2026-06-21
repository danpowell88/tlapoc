# Individual prescription (no batch / no async)

> **Epic:** [PRD-04 — Consult, prescribing & S4 medicines governance (the moat)](../epics/PRD-04.md)  ·  **Key:** `PRD-04/PRESCRIPTION`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-04/CONSULT`, `PRD-01/CREDENTIALS`

## Background

As a prescriber, I want to write an individual prescription for this patient tied to their consult, so that prescribing is lawful and patient-specific.
An individual prescription per client per consult — never batch/standing-order, never async (text/email/online-only) (C2). Supports the designated RN prescriber identity.

## Requirements

- To write an individual prescription for this patient tied to their consult.
- Compliance: [C2](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria), [C5](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] One prescription per client per consult; applying one script to multiple clients is rejected.
- [ ] Standing-order/batch scripts and async-only prescribing are impossible to create.
- [ ] Prescriber may be NP, remote prescriber, or designated RN prescriber (with recorded partnered prescriber).
- [ ] Off-label is flagged on the script and requires consent covering off-label use.

## Technical notes (high level)

- Stack: .NET API (domain/services)

## Other

- Source PRD: [PRD-04-consult-prescribing-s4.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-04-consult-prescribing-s4.md)

## Tasks (dev pickup)

- [ ] **Domain logic & business rules** — Core behaviour + invariants.
- [ ] **API endpoint(s) + OpenAPI contract** — Wire request/response; regenerate clients.
- [ ] **Enforce compliance gate + audit events** — Server-side (C2, C5); blocked path explains why.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
