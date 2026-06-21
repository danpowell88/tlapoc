# Synchronous consult record

> **Epic:** [PRD-04 — Consult, prescribing & S4 medicines governance (the moat)](../epics/PRD-04.md)  ·  **Key:** `PRD-04/CONSULT`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-02/CONSULT-GATE`, `PRD-03/GATING`

## Background

As a prescriber, I want to record a synchronous consult (in person or from our external telehealth app) before writing any script, so that every prescription is backed by a real assessment.
A Consult (in-person or external-telehealth) records modality, prescriber, timestamp, external reference and notes — required before any script (C1).

## Requirements

- To record a synchronous consult (in person or from our external telehealth app) before writing any script.
- Compliance: [C1](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Consult records modality (in-person/telehealth-external), prescriber, timestamp, external reference, notes.
- [ ] A prescription cannot be saved without a linked synchronous consult at/just-before script time.
- [ ] The remote-prescriber path links the externally-conducted consult to the resulting script.
- [ ] Consult creation is audited.

## Technical notes (high level)

- Stack: .NET API (domain/services)
- Architecture decisions: [ADR-0011](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-04-consult-prescribing-s4.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-04-consult-prescribing-s4.md)

## Tasks (dev pickup)

- [ ] **Domain logic & business rules** — Core behaviour + invariants.
- [ ] **API endpoint(s) + OpenAPI contract** — Wire request/response; regenerate clients.
- [ ] **Enforce compliance gate + audit events** — Server-side (C1); blocked path explains why.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
