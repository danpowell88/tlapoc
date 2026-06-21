# Xero invoice/payment sync

> **Epic:** [PRD-10 — Integrations: Xero & calendar](../epics/PRD-10.md)  ·  **Key:** `PRD-10/XERO`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** integration
>
> **Depends on:** `PRD-06/POS`

## Background

As a owner, I want completed sales/payments to post to Xero with the right account and GST, so that my books reconcile without re-keying.
On checkout, create/sync invoice + payment (and payouts) in Xero with account/GST mapping, retries and reconciliation status, behind IAccountingExport (REQ-INT-1).

## How it works

On checkout, create/sync the invoice + payment (and payouts) in Xero with correct account + GST mapping, retries and a reconciliation status — behind an IAccountingExport port. Services vs retail vs memberships map to the right accounts (defaults an open question).
Removes double-entry so the books reconcile without re-keying; the app keeps pricing/reporting while the ledger lives in Xero (ADR-0027).

## Requirements

- Completed sales/payments to post to Xero with the right account and GST.

## Acceptance Criteria

- [ ] A completed sale creates the corresponding Xero invoice + payment with correct account + GST.
- [ ] Failures retry and show a reconciliation status.
- [ ] Services vs retail vs memberships map to the right accounts (defaults are an open question).
- [ ] Implemented behind IAccountingExport (swappable).

## UI designs / screenshots

- Prototype: Settings -> Integrations (settings-integrations.png) — Xero connection card + account/GST mapping + sync/reconciliation status; per-sale posting is automatic from Checkout.

![settings-integrations — prototype screen](../screens/settings-integrations.png)

## Suggested data model

- **IntegrationConnection** — id, tenant_id, provider(xero), tokens, status
  - _OAuth connection; AU/APP-8 posture._
- **AccountMapping** — tenant_id, item_type(service|retail|membership), xero_account, gst_code
  - _Drives the posting._
- **SyncJob** — id, provider, ref(invoice/payment), status, retries, reconciled(bool)
  - _Retry + reconciliation status._

## Technical notes (high level)

- Stack: Ports-and-adapters integration
- Architecture decisions: [ADR-0012](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-10-integrations.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-10-integrations.md)

## Tasks (dev pickup)

- [ ] **Integration adapter + config** — Behind the port; AU / APP-8 posture.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
