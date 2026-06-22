# PRD-10 — Integrations: Xero & calendar

> **Stage / Milestone:** M4 · Commerce, comms & integrations (PRD-06, PRD-07, PRD-10)  ·  **Phase:** 1  ·  **Stories:** 7

Outbound integrations that remove double-entry: push sales/payments to Xero, and keep appointments in sync with staff calendars (M365 / Google) — each behind a swappable adapter, with an AU/APP-8 sub-processor posture.

**Source PRD:** `docs/prds/PRD-10-integrations.md`

## Stories

| Key | Story | Type | Priority | Est | Tasks |
|---|---|---|---|---|---|
| `XERO` | [Xero invoice/payment sync (basic)](../stories/PRD-10__XERO.md) | Story | P1 | 3 | 2 |
| `XERO-SYNCJOB` | [Xero: resilient idempotent SyncJob + OAuth lifecycle](../stories/PRD-10__XERO-SYNCJOB.md) | Story | P1 | 3 | 1 |
| `XERO-RECON-UI` | [Xero: Settings card + mapping editor + reconciliation list](../stories/PRD-10__XERO-RECON-UI.md) | Story | P2 | 2 | 1 |
| `CALENDAR-SYNC` | [Calendar sync: outbound push (basic)](../stories/PRD-10__CALENDAR-SYNC.md) | Story | P2 | 2 | 2 |
| `CALENDAR-INBOUND` | [Calendar sync: inbound busy-time → availability blocks](../stories/PRD-10__CALENDAR-INBOUND.md) | Story | P2 | 2 | 1 |
| `SUBPROCESSOR-POSTURE` | [Sub-processor residency posture (APP-8)](../stories/PRD-10__SUBPROCESSOR-POSTURE.md) | Story | P2 | 2 | 3 |
| `INTEGRATIONS-LATER` | [Online checkout, e-prescribing, webhooks/API (placeholder)](../stories/PRD-10__INTEGRATIONS-LATER.md) | Story | P2 | 1 | 1 |

_Totals: 7 stories · 11 tasks._
