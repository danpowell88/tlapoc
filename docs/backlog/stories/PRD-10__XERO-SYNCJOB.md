# Xero: resilient idempotent SyncJob + OAuth lifecycle

> **Epic:** [PRD-10 — Integrations: Xero & calendar](../epics/PRD-10.md)  ·  **Key:** `PRD-10/XERO-SYNCJOB`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** —
>
> **Depends on:** `PRD-10/XERO`

## Background

As a owner, I want Xero posting to retry safely on failure and keep its connection alive, so that a transient failure or token expiry never loses or duplicates a posted sale.
This story makes the Xero posting resilient and reconcilable: each post becomes a retrying, idempotent SyncJob and the OAuth token lifecycle is handled so the connection stays live. It sits in the Integrations layer (step 10 of the clinic-first build) as a follow-up to the Xero basic (PRD-10/XERO) that adds resilience around the post-on-checkout already built; the data residency posture is governed by SUBPROCESSOR-POSTURE. A retry never double-posts.

## How it works

Make posting resilient and reconcilable: each post (built by the Xero basic, PRD-10/XERO) becomes a SyncJob with backoff retry that is rate-limit aware and idempotent (an operation safe to repeat — a retry never double-posts, keyed by an idempotency_key), carrying a reconciliation status (pending/synced/failed).
Handle the OAuth token lifecycle/refresh so the connection stays live, and surface the status for reconciliation (the operator-facing reconciliation card is XERO-RECON-UI). Because it sits behind IAccountingExport, the accounting provider is swappable without touching checkout. Money handling here is owner/bookkeeper-gated.

## Requirements

- Xero posting to retry safely on failure and keep its connection alive.

## Acceptance Criteria

- [ ] Each post is a SyncJob that retries on transient failure (backoff, rate-limit-aware).
- [ ] Posting is idempotent — a retry never double-posts.
- [ ] The SyncJob carries a reconciliation status (pending/synced/failed).
- [ ] The OAuth token lifecycle/refresh is handled so the connection stays live.

## UI designs / screenshots

- No new screen of its own — the SyncJob status it produces is surfaced by the reconciliation card (XERO-RECON-UI).
- OAuth connect/refresh keeps the IntegrationConnection live; idempotency_key guards against double-posting on retry.

![settings-integrations — prototype screen](../screens/settings-integrations.png)

## Suggested data model

- **SyncJob** — id, tenant_id, provider, ref(invoice|payment|payout), external_id?, status(pending|synced|failed), retries, last_error?, reconciled(bool), idempotency_key
  - _New entity extending XERO; retry + reconciliation status; idempotent so a retry never double-posts._
- **(reuses) IntegrationConnection** — PRD-10/XERO — OAuth token lifecycle/refresh handled here
  - _Keeps the Xero connection live; AU/APP-8 posture (SUBPROCESSOR-POSTURE)._

## Other

- Source PRD: [PRD-10-integrations.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-10-integrations.md)

## Tasks (dev pickup)

- [ ] **Resilient SyncJob: idempotent retries + reconciliation status + OAuth lifecycle**
  Behaviour: make posting resilient and reconcilable. Requirements: each post is a SyncJob with backoff retry that is rate-limit aware and idempotent (an operation safe to repeat — a retry never double-posts), carrying a reconciliation status (pending/synced/failed); handle the OAuth token lifecycle/refresh; surface the status for reconciliation.
