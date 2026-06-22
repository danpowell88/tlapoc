# Xero invoice/payment sync

> **Epic:** [PRD-10 — Integrations: Xero & calendar](../epics/PRD-10.md)  ·  **Key:** `PRD-10/XERO`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** integration
>
> **Depends on:** `PRD-06/POS`

## Background

As a owner, I want completed sales/payments to post to Xero with the right account and GST, so that my books reconcile without re-keying.
On checkout, create/sync invoice + payment (and payouts) in Xero with account/GST mapping, retries and reconciliation status, behind IAccountingExport (REQ-INT-1).

## How it works

On checkout completion (PRD-06 POS), the platform posts the sale to Xero with no re-keying: it creates/syncs the corresponding invoice + payment (and, where applicable, the processor payout) behind an IAccountingExport port (ADR-0012). The app is not the ledger — pricing, reporting and the clinical/commercial decisions stay in the app; the books live in Xero (ADR-0027). This removes the double-entry that the clinic does today between the PMS and the accountant.
Posting is driven by an AccountMapping: each line is coded by item type — services vs retail vs memberships map to the right Xero account — and GST is computed per line from the catalogue tax code (not the prototype's flat total/11), producing a correct invoice and BAS-relevant figures. The default account/GST mapping for services vs retail vs memberships is an open question to settle with the bookkeeper.
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

- [ ] **Xero adapter: invoice/payment sync, mapping, retries & reconciliation (IAccountingExport)**
  Implement the Xero adapter behind IAccountingExport (ADR-0012): on the checkout-completed domain event, build the invoice from the sale lines, coding each line via AccountMapping (service/retail/membership → account) with per-line GST from the catalogue tax code, create invoice + payment (+payout) in Xero, store the external id. Drive it as an idempotent SyncJob with backoff retry (rate-limit aware) and a reconciliation status (pending/synced/failed). OAuth token lifecycle/refresh. Keep checkout decoupled — provider swappable via the port.
- [ ] **Web UI: Xero connection card + account/GST mapping + reconciliation status**
  Build the Settings → Integrations Xero card: OAuth connect/disconnect + status, the AccountMapping editor (service/retail/membership → Xero account + GST code), and the reconciliation status list (pending/synced/failed) with a manual retry. Mirror the 'Xero connected' assurance on Finance. Owner/bookkeeper-gated; surface the AU/APP-8 posture on the card (SUBPROCESSOR-POSTURE).
