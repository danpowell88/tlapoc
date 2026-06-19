# PRD-10 — Integrations: Xero & Calendar

> **Phase:** 1 · **Status:** Draft
> **Requirements:** REQ-INT-1…3 · **Compliance:** C10/C21 (cross-border sub-processors)
> **ADRs:** 0012 (ports-and-adapters), 0016 (residency) · **Depends on:** PRD-01; consumes PRD-06 (payments), PRD-02 (appointments)

## 1. Summary
Outbound integrations that remove double-entry: push sales/payments to **Xero**, and keep
appointments in sync with staff **calendars (M365 / Google)** — each behind a swappable adapter.

## 2. Goals & non-goals
**Goals:** Xero invoice/payment (and payout) sync with account/GST mapping; two-way calendar sync;
adapter pattern so providers are swappable; AU/APP-8 sub-processor posture.
**Non-goals (v1):** inbound webhooks / public API (deferred); marketing/CRM integrations; PMS-to-PMS
migration; health-fund/Medicare claiming.

## 3. Users
Owner/bookkeeper (Xero), practitioners (calendar), system (sync jobs).

## 4. User stories
- As an **owner**, completed sales/payments **post to Xero** with the right account and GST so my books reconcile without re-keying.
- As a **practitioner**, my appointments appear in my **Outlook/Google** calendar and external busy-time blocks my availability.
- As an **owner**, I trust that any data leaving the platform goes to **AU-resident or APP-8-assessed** sub-processors.

## 5. Key flow
```mermaid
flowchart LR
  PAY[Checkout completed PRD-06] --> XQ[Xero adapter\n(IAccountingExport)]
  XQ --> XERO[(Xero)]
  BOOK[Appointment PRD-02] <--> CAL[Calendar adapter\n(ICalendarProvider)]
  CAL <--> M365[(MS Graph)]
  CAL <--> GCAL[(Google Calendar)]
```

## 6. Functional scope
- **Xero** (REQ-INT-1): on checkout, create/sync invoice + payment (and payouts) in Xero; map services/products → accounts; handle **GST**; retries + reconciliation status. Behind `IAccountingExport`.
- **Calendar** (REQ-INT-2): two-way sync of appointments ↔ M365 (Graph) + Google Calendar; external busy events block availability; behind `ICalendarProvider`.
- **Adapters/residency** (REQ-INT-3 deferred for webhooks; ADR-0012/0016): all integrations outbound, swappable; sub-processor data flows AU-resident or APP-8-assessed + consented.

## 7. Data & entities
`IntegrationConnection` (tenant, provider, tokens), `SyncJob`/`SyncLog`, `AccountMapping` (Xero), `CalendarLink` (per staff).

## 8. Acceptance criteria
- **AC1:** A completed sale creates the corresponding Xero invoice + payment with correct account + GST; failures retry and show a reconciliation status.
- **AC2:** Creating/moving/cancelling an appointment reflects in the linked Outlook/Google calendar and vice-versa (busy blocks availability).
- **AC3 (C21):** No integration sends PII to a non-AU sub-processor unless an APP-8 assessment + consent record exists.
- **AC4:** Each integration can be swapped (new adapter) without changes to core modules.

## 9. Dependencies & sequencing
After PRD-01; consumes PRD-06 (payments) and PRD-02 (appointments). Can land late in Phase 1.

## 10. Out of scope
Inbound webhooks/public API (Phase 3), Medicare/health-fund claiming, marketing integrations.

## 11. Open questions
- Xero GST/account mapping defaults for services vs retail vs memberships.
- Calendar: per-staff opt-in and conflict-resolution rules.
