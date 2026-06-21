# Individual prescription (no batch / no async)

> **Epic:** [PRD-04 — Consult, prescribing & S4 medicines governance (the moat)](../epics/PRD-04.md)  ·  **Key:** `PRD-04/PRESCRIPTION`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-04/CONSULT`, `PRD-01/CREDENTIALS`

## Background

Consult, prescribing & S4 medicines governance (the moat) — The defensible core.

As a prescriber, I want to write an individual prescription for this patient tied to their consult, so that prescribing is lawful and patient-specific.

An individual prescription per client per consult — never batch/standing-order, never async (text/email/online-only) (C2). Supports the designated RN prescriber identity.

## Requirements

- To write an individual prescription for this patient tied to their consult.
- Traces to requirement(s): REQ-RX-2, REQ-RX-5.
- Must satisfy compliance obligation(s): C2, C5.

## Acceptance Criteria

- [ ] One prescription per client per consult; applying one script to multiple clients is rejected.
- [ ] Standing-order/batch scripts and async-only prescribing are impossible to create.
- [ ] Prescriber may be NP, remote prescriber, or designated RN prescriber (with recorded partnered prescriber).
- [ ] Off-label is flagged on the script and requires consent covering off-label use.

## UI designs / screenshots

prototype.html — Stock & medicines, Charting (lot select), Governance → Recalls.

## Technical notes (high level)

Stack: .NET API (domain/services).
Depends on: PRD-04/CONSULT, PRD-01/CREDENTIALS.

## Other

Epic: PRD-04 — Consult, prescribing & S4 medicines governance (the moat).
Source PRD: docs/prds/PRD-04-consult-prescribing-s4.md.
Backlog key: PRD-04/PRESCRIPTION.
Phase: 1 · Priority: P0 · Estimate: 5 pts.
Compliance criteria: C2, C5.

## Tasks (dev pickup)

- [ ] **Domain logic & business rules** — Core behaviour + invariants.
- [ ] **API endpoint(s) + OpenAPI contract** — Wire request/response; regenerate clients.
- [ ] **Enforce compliance gate + audit events** — Server-side (C2, C5); blocked path explains why.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
