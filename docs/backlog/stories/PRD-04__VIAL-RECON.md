# Vial / unit reconciliation

> **Epic:** [PRD-04 — Consult, prescribing & S4 medicines governance (the moat)](../epics/PRD-04.md)  ·  **Key:** `PRD-04/VIAL-RECON`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-04/ADMIN-GATE`

## Background

Consult, prescribing & S4 medicines governance (the moat) — The defensible core.

As a owner, I want vial/unit reconciliation across draws and wastage, so that stock, billing and the medicine register always agree.

Units drawn vs vial size + wastage must reconcile so stock, billing and the register agree (C8).

## Requirements

- Vial/unit reconciliation across draws and wastage.
- Traces to requirement(s): REQ-MED-5.
- Must satisfy compliance obligation(s): C8.

## Acceptance Criteria

- [ ] Each administration decrements the selected lot; vial reconciliation tracks units drawn vs vial size + wastage.
- [ ] Discrepancies are surfaced.
- [ ] Reconciliation data feeds reporting (PRD-08).
- [ ] Partial-vial handling is supported.

## UI designs / screenshots

prototype.html — Stock & medicines, Charting (lot select), Governance → Recalls.

## Technical notes (high level)

Stack: .NET API (domain/services).
Depends on: PRD-04/ADMIN-GATE.

## Other

Epic: PRD-04 — Consult, prescribing & S4 medicines governance (the moat).
Source PRD: docs/prds/PRD-04-consult-prescribing-s4.md.
Backlog key: PRD-04/VIAL-RECON.
Phase: 1 · Priority: P1 · Estimate: 3 pts.
Compliance criteria: C8.

## Tasks (dev pickup)

- [ ] **Domain logic & business rules** — Core behaviour + invariants.
- [ ] **API endpoint(s) + OpenAPI contract** — Wire request/response; regenerate clients.
- [ ] **Enforce compliance gate + audit events** — Server-side (C8); blocked path explains why.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
