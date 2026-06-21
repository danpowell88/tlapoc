# Consult gate on injectable appointments

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/CONSULT-GATE`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-02/ONLINE-BOOK`

## Background

Booking & scheduling (+ client/CRM basics) — The calendar that runs the front desk and the 360° client record everything hangs off.

As a system, I want to block a checked-in injectable appointment from opening charting unless a consult is linked, so that no S4 treatment can proceed without the required consult.

An injectable appointment cannot move to charting without a linked Consult — the booking-side half of the moat (REQ-BOOK-5).

## Requirements

- To block a checked-in injectable appointment from opening charting unless a consult is linked.
- Traces to requirement(s): REQ-BOOK-5.
- Must satisfy compliance obligation(s): C1.

## Acceptance Criteria

- [ ] A checked-in injectable appointment with no linked consult cannot open the charting screen.
- [ ] The blocked-action banner explains what's missing and who can resolve it.
- [ ] Once a consult is recorded the gate clears (handoff to PRD-04).
- [ ] The block is server-enforced, not just UI.

## UI designs / screenshots

prototype.html — Schedule, 'New booking' wizard, Clients directory & 360.

## Technical notes (high level)

Stack: .NET API (domain/services).
Depends on: PRD-02/ONLINE-BOOK.

## Other

Epic: PRD-02 — Booking & scheduling (+ client/CRM basics).
Source PRD: docs/prds/PRD-02-booking-scheduling.md.
Backlog key: PRD-02/CONSULT-GATE.
Phase: 1 · Priority: P0 · Estimate: 5 pts.
Compliance criteria: C1.

## Tasks (dev pickup)

- [ ] **Domain logic & business rules** — Core behaviour + invariants.
- [ ] **API endpoint(s) + OpenAPI contract** — Wire request/response; regenerate clients.
- [ ] **Enforce compliance gate + audit events** — Server-side (C1); blocked path explains why.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
