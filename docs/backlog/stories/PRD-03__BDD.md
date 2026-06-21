# BDD / psychological screening instrument

> **Epic:** [PRD-03 — Intake, consent & compliance gating](../epics/PRD-03.md)  ·  **Key:** `PRD-03/BDD`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-03/INTAKE`

## Background

Intake, consent & compliance gating — Turns AHPRA's patient-safety rules into enforced workflow: pre-visit intake (medical history, contraindications, BDD/psychological screen), versioned e-signed consent with mandated content, separate withdrawable image-use consent, and cooling-off + payment blocks for under-18s.

As a RN/NP, I want a BDD/psychological screen completed and surfaced before I proceed, so that I can avoid harm for at-risk patients per the guidelines.

Cosmetic guidelines require BDD screening; a positive result must be surfaced to the prescriber before treatment (C3).

## Requirements

- A BDD/psychological screen completed and surfaced before I proceed.
- Traces to requirement(s): REQ-CONS-2.
- Must satisfy compliance obligation(s): C3.

## Acceptance Criteria

- [ ] A validated BDD/psychological screening instrument is embedded in intake.
- [ ] A completed screen authored/reviewed by an RN/NP is present before treatment.
- [ ] A positive flag is surfaced to the prescriber and recorded.
- [ ] Which instrument is used is configurable (open question to confirm).

## UI designs / screenshots

prototype.html — Forms & consent; client-app.html intake/consent; checkin.html.

## Technical notes (high level)

Stack: .NET API (domain/services).
Depends on: PRD-03/INTAKE.

## Other

Epic: PRD-03 — Intake, consent & compliance gating.
Source PRD: docs/prds/PRD-03-intake-consent-gating.md.
Backlog key: PRD-03/BDD.
Phase: 1 · Priority: P0 · Estimate: 5 pts.
Compliance criteria: C3.

## Tasks (dev pickup)

- [ ] **Domain logic & business rules** — Core behaviour + invariants.
- [ ] **API endpoint(s) + OpenAPI contract** — Wire request/response; regenerate clients.
- [ ] **Enforce compliance gate + audit events** — Server-side (C3); blocked path explains why.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
