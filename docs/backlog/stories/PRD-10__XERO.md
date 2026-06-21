# Xero invoice/payment sync

> **Epic:** [PRD-10 — Integrations: Xero & calendar](../epics/PRD-10.md)  ·  **Key:** `PRD-10/XERO`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** integration
>
> **Depends on:** `PRD-06/POS`

## Background

Integrations: Xero & calendar — Outbound integrations that remove double-entry: push sales/payments to Xero, and keep appointments in sync with staff calendars (M365 / Google)

As a owner, I want completed sales/payments to post to Xero with the right account and GST, so that my books reconcile without re-keying.

On checkout, create/sync invoice + payment (and payouts) in Xero with account/GST mapping, retries and reconciliation status, behind IAccountingExport (REQ-INT-1).

## Requirements

- Completed sales/payments to post to Xero with the right account and GST.
- Traces to requirement(s): REQ-INT-1.

## Acceptance Criteria

- [ ] A completed sale creates the corresponding Xero invoice + payment with correct account + GST.
- [ ] Failures retry and show a reconciliation status.
- [ ] Services vs retail vs memberships map to the right accounts (defaults are an open question).
- [ ] Implemented behind IAccountingExport (swappable).

## UI designs / screenshots

prototype.html — Settings → Integrations.

## Technical notes (high level)

Stack: Ports-and-adapters integration.
Architecture decisions: ADR-0012 (see docs/adr/decision-log.md).
Depends on: PRD-06/POS.

## Other

Epic: PRD-10 — Integrations: Xero & calendar.
Source PRD: docs/prds/PRD-10-integrations.md.
Backlog key: PRD-10/XERO.
Phase: 1 · Priority: P1 · Estimate: 3 pts.

## Tasks (dev pickup)

- [ ] **Integration adapter + config** — Behind the port; AU / APP-8 posture.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
