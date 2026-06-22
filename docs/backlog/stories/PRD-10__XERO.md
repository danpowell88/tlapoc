# Xero invoice/payment sync

> **Epic:** [PRD-10 — Integrations: Xero & calendar](../epics/PRD-10.md)  ·  **Key:** `PRD-10/XERO`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** integration
>
> **Depends on:** `PRD-06/POS`

## Background

As a owner, I want completed sales/payments to post to Xero with the right account and GST, so that my books reconcile without re-keying.
This story removes double-entry into the accounting system: when a sale is taken, the platform automatically posts the matching invoice and payment into Xero with the right account and tax code, so the books reconcile without re-keying. It sits in the Integrations layer (step 10 of the clinic-first build), deliberately late — external systems are wired up once the internal data is solid. It is driven by checkout completion (PRD-06 POS), so it depends on that, and its data residency is governed by the sub-processor posture (SUBPROCESSOR-POSTURE). Money handling here is owner/bookkeeper-only. On checkout, create/sync invoice + payment (and payouts) in Xero with account/GST (Goods and Services Tax, Australia's 10%) mapping, retries and reconciliation status, behind IAccountingExport (REQ-INT-1).

## How it works

On checkout completion (PRD-06 POS), the platform posts the sale to Xero with no re-keying: it creates/syncs the corresponding invoice + payment (and, where applicable, the processor payout) behind an IAccountingExport port (ADR-0012). The app is not the ledger — pricing, reporting and the clinical/commercial decisions stay in the app; the books live in Xero (ADR-0027). This removes the double-entry that the clinic does today between the PMS and the accountant.
Posting is driven by an AccountMapping: each line is coded by item type — services vs retail vs memberships map to the right Xero account — and GST is computed per line from the catalogue tax code (not the prototype's flat total/11), producing a correct invoice and BAS (Business Activity Statement, the GST return)-relevant figures. The default account/GST mapping for services vs retail vs memberships is an open question to settle with the bookkeeper.
Sync is asynchronous and resilient: each post is a SyncJob that retries on transient failure (with backoff, honouring Xero rate limits and idempotency so a retry never double-posts) and carries a reconciliation status (pending / synced / failed) surfaced on the Integrations Xero card. Because it sits behind IAccountingExport, the accounting provider is swappable without touching checkout. All money handling here is owner/bookkeeper-gated.

## Requirements

- Completed sales/payments to post to Xero with the right account and GST.

## Acceptance Criteria

- [ ] A completed sale creates the corresponding Xero invoice + payment (and payout where applicable) with the correct account + GST.
- [ ] GST is computed per line from the catalogue tax code (not a flat total/11); services vs retail vs memberships map to the right accounts.
- [ ] Each post is a SyncJob that retries on transient failure (backoff, rate-limit-aware, idempotent — no double-post) and shows a reconciliation status (pending/synced/failed).
- [ ] Implemented behind IAccountingExport (provider swappable without touching checkout); the AccountMapping is tenant-configurable.
- [ ] AU/APP-8 sub-processor posture applies to the Xero connection (ties to SUBPROCESSOR-POSTURE).

## UI designs / screenshots

- Prototype: Settings → Integrations (settings-integrations.png) — Xero card 'Connected', 'Push invoices & payments on checkout.', Configure → (account/GST mapping + sync/reconciliation status).
- Finance (finance.png): 'Xero connected. Invoices, payments, bills & BAS sync automatically. Manage integrations.' banner — per-sale posting is automatic from Checkout (no manual step).
- Configure: OAuth connect, AccountMapping editor (service/retail/membership → Xero account + GST code), reconciliation status list (pending/synced/failed with retry).

![settings-integrations — prototype screen](../screens/settings-integrations.png)

## Suggested data model

- **IntegrationConnection** — id, tenant_id, provider(xero), oauth_tokens, status, region
  - _OAuth connection; AU/APP-8 posture (SUBPROCESSOR-POSTURE)._
- **AccountMapping** — tenant_id, item_type(service|retail|membership), xero_account_code, gst_code
  - _Drives per-line account coding + GST; tenant-configurable; defaults open question._
- **SyncJob** — id, tenant_id, provider, ref(invoice|payment|payout), external_id?, status(pending|synced|failed), retries, last_error?, reconciled(bool), idempotency_key
  - _Retry + reconciliation status; idempotent so a retry never double-posts._

## Technical notes (high level)

- Architecture decisions: [ADR-0012](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-10-integrations.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-10-integrations.md)

## Tasks (dev pickup)

- [ ] **Xero adapter behind IAccountingExport: invoice/payment build on checkout**
  Behaviour: on the checkout-completed domain event (a fact emitted when something happens in the system), post the sale to Xero — build the invoice from the sale lines and create the invoice + payment (+ processor payout where applicable), storing the external id. Requirements: implement behind the IAccountingExport port (ADR-0012) so the provider is swappable without touching checkout; the app is not the ledger (ADR-0027); checkout stays decoupled (async).
- [ ] **Account mapping + per-line GST coding**
  Behaviour: code each line to the right Xero account and tax. Requirements: drive coding from a tenant-configurable AccountMapping (item_type service/retail/membership → xero_account_code + gst_code); compute GST (Goods and Services Tax, Australia's 10%) per line from the catalogue tax code (NOT a flat total/11) so the invoice and BAS (Business Activity Statement) figures are correct; the default service/retail/membership mapping is an open question to settle with the bookkeeper.
- [ ] **Resilient SyncJob: idempotent retries + reconciliation status + OAuth lifecycle**
  Behaviour: make posting resilient and reconcilable. Requirements: each post is a SyncJob with backoff retry that is rate-limit aware and idempotent (an operation safe to repeat — a retry never double-posts), carrying a reconciliation status (pending/synced/failed); handle the OAuth token lifecycle/refresh; surface the status for reconciliation.
- [ ] **Web UI: Xero card (connect, mapping editor, reconciliation list)**
  Behaviour: the Settings → Integrations Xero card. Requirements: OAuth connect/disconnect + status, the AccountMapping editor (service/retail/membership → Xero account + GST code), and the reconciliation status list (pending/synced/failed) with a manual retry; mirror the 'Xero connected' assurance on Finance; owner/bookkeeper-gated; show the AU/APP-8 (Australian Privacy Principle 8, cross-border disclosure) posture on the card (SUBPROCESSOR-POSTURE).
