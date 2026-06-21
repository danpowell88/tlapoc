# Administration gating & immutable record

> **Epic:** [PRD-04 — Consult, prescribing & S4 medicines governance (the moat)](../epics/PRD-04.md)  ·  **Key:** `PRD-04/ADMIN-GATE`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-04/PRESCRIPTION`, `PRD-04/STOCK-RECEIVE`

## Background

Consult, prescribing & S4 medicines governance (the moat) — The defensible core.

As a RN, I want to administer S4 only against a valid unconsumed script for this client, recording product, units, depth, site and batch-lot/expiry, so that every dose is lawful, traceable and tamper-proof.

An RN can only administer S4 against a valid, unconsumed prescription for that same client, with current consent and a selected in-date lot; the record is immutable once saved (C8).

## Requirements

- To administer S4 only against a valid unconsumed script for this client, recording product, units, depth, site and batch-lot/expiry.
- Traces to requirement(s): REQ-RX-3, REQ-MED-4.
- Must satisfy compliance obligation(s): C8.

## Acceptance Criteria

- [ ] An Administration cannot persist without a valid script (same client), current consent and a selected in-date lot.
- [ ] It records product, units, depth, site and batch-lot/expiry; it is immutable once saved.
- [ ] A blocked attempt shows the reason and writes an audit event.
- [ ] The administration appears in the medicine register.

## UI designs / screenshots

prototype.html — Stock & medicines, Charting (lot select), Governance → Recalls.

## Technical notes (high level)

Stack: .NET API (domain/services).
Architecture decisions: ADR-0010 (see docs/adr/decision-log.md).
Depends on: PRD-04/PRESCRIPTION, PRD-04/STOCK-RECEIVE.

## Other

Epic: PRD-04 — Consult, prescribing & S4 medicines governance (the moat).
Source PRD: docs/prds/PRD-04-consult-prescribing-s4.md.
Backlog key: PRD-04/ADMIN-GATE.
Phase: 1 · Priority: P0 · Estimate: 5 pts.
Compliance criteria: C8.

## Tasks (dev pickup)

- [ ] **Domain logic & business rules** — Core behaviour + invariants.
- [ ] **API endpoint(s) + OpenAPI contract** — Wire request/response; regenerate clients.
- [ ] **Enforce compliance gate + audit events** — Server-side (C8); blocked path explains why.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
