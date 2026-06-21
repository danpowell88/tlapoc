# Two-way calendar sync (M365 / Google)

> **Epic:** [PRD-10 — Integrations: Xero & calendar](../epics/PRD-10.md)  ·  **Key:** `PRD-10/CALENDAR-SYNC`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** integration
>
> **Depends on:** `PRD-02/CALENDAR`

## Background

As a practitioner, I want my appointments to appear in Outlook/Google and external busy-time to block my availability, so that I have one source of truth for my time.
Appointments sync both ways with Outlook/Google; external busy events block availability, behind ICalendarProvider (REQ-INT-2).

## How it works

Two-way sync of appointments with Outlook (MS Graph) and Google Calendar behind an ICalendarProvider port: creating/moving/cancelling reflects both ways, and external busy events block availability in booking (PRD-02). Per-staff opt-in and conflict-resolution rules (open question).
Gives practitioners one source of truth for their time.

## Requirements

- My appointments to appear in Outlook/Google and external busy-time to block my availability.

## Acceptance Criteria

- [ ] Creating/moving/cancelling an appointment reflects in the linked Outlook/Google calendar and vice-versa.
- [ ] External busy events block availability in booking (PRD-02).
- [ ] Per-staff opt-in and conflict-resolution rules (open question) supported.
- [ ] Implemented behind ICalendarProvider (swappable).

## UI designs / screenshots

- Prototype: Settings -> Integrations (settings-integrations.png) — per-staff calendar connect (M365/Google) + two-way sync toggle; external busy time shows as unavailable in Schedule.

![settings-integrations — prototype screen](../screens/settings-integrations.png)

## Suggested data model

- **CalendarLink** — id, staff_id, provider(m365|google), tokens, sync_mode(two_way), status
  - _Per-staff opt-in._
- **SyncLog** — id, calendar_link_id, appointment_id, direction, at, result
  - _Busy events block availability._

## Technical notes (high level)

- Architecture decisions: [ADR-0012](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-10-integrations.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-10-integrations.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations** — Entities/columns + relationships; tenant_id + RLS.
- [ ] **Integration adapter, sync & config** — Behind the port; trigger + retries/reconciliation; AU/APP-8 posture.
