# Xero: Settings card + mapping editor + reconciliation list

> **Epic:** [PRD-10 — Integrations: Xero & calendar](../epics/PRD-10.md)  ·  **Key:** `PRD-10/XERO-RECON-UI`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-10/XERO`, `PRD-10/XERO-SYNCJOB`

## Background

As a owner, I want a Settings card to connect Xero, edit the mapping and watch reconciliation, so that I can configure the integration and see that every sale posted.
This story gives the owner/bookkeeper the operator surface for the Xero integration: connect, edit the account/GST mapping, and watch the reconciliation status with a manual retry. It sits in the Integrations layer (step 10 of the clinic-first build) as a follow-up to the Xero basic (PRD-10/XERO) and the SyncJob (PRD-10/XERO-SYNCJOB), surfacing what they produce; it shows the AU/APP-8 posture on the card (SUBPROCESSOR-POSTURE). Owner/bookkeeper-gated.

## How it works

The Settings → Integrations Xero card: OAuth connect/disconnect + status, the AccountMapping editor (service/retail/membership → Xero account + GST code), and the reconciliation status list (pending/synced/failed) with a manual retry — surfacing the SyncJob status (PRD-10/XERO-SYNCJOB) for reconciliation.
Mirror the 'Xero connected' assurance on Finance; show the AU/APP-8 (Australian Privacy Principle 8, cross-border disclosure) posture on the card (SUBPROCESSOR-POSTURE). Owner/bookkeeper-gated; no money figures leak to non-owner roles. This is the operator-facing complement to the headless basic + SyncJob.

## Requirements

- A Settings card to connect Xero, edit the mapping and watch reconciliation.

## Acceptance Criteria

- [ ] The Settings → Integrations Xero card provides OAuth connect/disconnect + status.
- [ ] An AccountMapping editor (service/retail/membership → Xero account + GST code) is provided.
- [ ] A reconciliation status list (pending/synced/failed) with a manual retry is shown.
- [ ] The 'Xero connected' assurance is mirrored on Finance; the card shows the AU/APP-8 posture; owner/bookkeeper-gated.

## UI designs / screenshots

- Prototype: Settings → Integrations (settings-integrations.png) — Xero card Configure → OAuth connect, AccountMapping editor (service/retail/membership → Xero account + GST code), reconciliation status list (pending/synced/failed with retry).
- Finance (finance.png): 'Xero connected … Manage integrations.' banner; card shows the AU/APP-8 posture (SUBPROCESSOR-POSTURE).

![settings-integrations — prototype screen](../screens/settings-integrations.png)

## Suggested data model

- **(reuses) AccountMapping/SyncJob/IntegrationConnection** — PRD-10/XERO + XERO-SYNCJOB — mapping edited, SyncJob status listed, OAuth connect/disconnect
  - _Extends XERO; operator surface only; owner/bookkeeper-gated._

## Other

- Source PRD: [PRD-10-integrations.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-10-integrations.md)

## Tasks (dev pickup)

- [ ] **Web UI: Xero card (connect, mapping editor, reconciliation list)**
  Behaviour: the Settings → Integrations Xero card. Requirements: OAuth connect/disconnect + status, the AccountMapping editor (service/retail/membership → Xero account + GST code), and the reconciliation status list (pending/synced/failed) with a manual retry; mirror the 'Xero connected' assurance on Finance; owner/bookkeeper-gated; show the AU/APP-8 (Australian Privacy Principle 8, cross-border disclosure) posture on the card (SUBPROCESSOR-POSTURE).
