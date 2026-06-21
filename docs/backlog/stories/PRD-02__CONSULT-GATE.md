# Consult gate on injectable appointments

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/CONSULT-GATE`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-02/ONLINE-BOOK`

## Background

As a system, I want to block a checked-in injectable appointment from opening charting unless a consult is linked, so that no S4 treatment can proceed without the required consult.
An injectable appointment cannot move to charting without a linked Consult — the booking-side half of the moat (REQ-BOOK-5).

## Requirements

- To block a checked-in injectable appointment from opening charting unless a consult is linked.
- Compliance: [C1](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] A checked-in injectable appointment with no linked consult cannot open the charting screen.
- [ ] The blocked-action banner explains what's missing and who can resolve it.
- [ ] Once a consult is recorded the gate clears (handoff to PRD-04).
- [ ] The block is server-enforced, not just UI.

## Technical notes (high level)

- Stack: .NET API (domain/services)

## Other

- Source PRD: [PRD-02-booking-scheduling.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-02-booking-scheduling.md)

## Tasks (dev pickup)

- [ ] **Domain logic & business rules** — Core behaviour + invariants.
- [ ] **API endpoint(s) + OpenAPI contract** — Wire request/response; regenerate clients.
- [ ] **Enforce compliance gate + audit events** — Server-side (C1); blocked path explains why.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
