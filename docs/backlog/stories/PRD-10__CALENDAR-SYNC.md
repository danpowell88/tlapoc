# Calendar sync: outbound push (basic)

> **Epic:** [PRD-10 — Integrations: Xero & calendar](../epics/PRD-10.md)  ·  **Key:** `PRD-10/CALENDAR-SYNC`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** integration
>
> **Depends on:** `PRD-02/CALENDAR`

## Background

As a practitioner, I want my clinic appointments to appear in my Outlook/Google calendar, so that my clinic bookings sit alongside my personal time.
This story pushes each practitioner's clinic appointments into their own Outlook or Google calendar, so their clinic bookings appear alongside their personal time. It sits in the Integrations layer (step 10 of the clinic-first build), built after the booking calendar it syncs with (PRD-02 CALENDAR). Sync is per-staff opt-in; calendar providers are sub-processors governed by the residency posture (SUBPROCESSOR-POSTURE). This basic slice is the outbound push behind ICalendarProvider plus the per-staff connect; the inbound busy-time → availability blocking is the follow-up (CALENDAR-INBOUND) (REQ-INT-2).

## How it works

Outbound sync of appointments to staff calendars — Microsoft 365 (MS Graph) and Google Calendar — behind an ICalendarProvider port (ADR-0012, bidirectional under ADR-0036). Creating, moving or cancelling a clinic appointment reflects in the practitioner's linked calendar, so their clinic bookings appear in their personal calendar.
Sync is per-staff opt-in: each practitioner connects their own M365/Google account (OAuth), choosing the calendar and the sync mode; nothing syncs for staff who haven't connected. Outbound pushes are driven by appointment lifecycle events; each sync action is logged (direction, appointment, result) for troubleshooting. No clinical detail leaks into the external calendar beyond what the clinic configures (privacy-safe event titles); calendar providers are sub-processors subject to the AU/APP-8 (Australian Privacy Principle 8, cross-border disclosure) posture (SUBPROCESSOR-POSTURE).
Because it sits behind ICalendarProvider, M365 and Google are interchangeable adapters and a new provider needs no core change. The inbound busy-time pulled back to block clinic availability — so the clinic never double-books over a personal appointment — is the follow-up (CALENDAR-INBOUND).

## Requirements

- My clinic appointments to appear in my Outlook/Google calendar.

## Acceptance Criteria

- [ ] Creating/moving/cancelling a clinic appointment reflects in the linked Outlook/Google calendar.
- [ ] Sync is per-staff opt-in (each practitioner connects their own M365/Google account; nothing syncs until connected).
- [ ] Implemented behind ICalendarProvider (M365/Google swappable); each sync action is logged; external event titles are privacy-safe per clinic config.
- [ ] The inbound busy-time → availability blocking is added by the follow-up (CALENDAR-INBOUND).

## UI designs / screenshots

- Prototype: Settings → Integrations (settings-integrations.png) — 'Calendar sync (M365 / Google)' card, currently 'Outbound only', Connect →.
- Per-staff connect (M365/Google OAuth) + sync-mode + calendar picker; per-staff status (last sync, errors).
- Schedule (schedule.png, PRD-02): clinic appointments appear in the staff's external calendar. Inbound busy-time blocking is the follow-up (CALENDAR-INBOUND).

![settings-integrations — prototype screen](../screens/settings-integrations.png)

## Suggested data model

- **CalendarLink** — id, staff_id, provider(m365|google), oauth_tokens, calendar_id, sync_mode(two_way|outbound), status, region
  - _Per-staff opt-in; outbound here, two_way enabled by CALENDAR-INBOUND; AU/APP-8 posture (SUBPROCESSOR-POSTURE)._
- **SyncLog** — id, calendar_link_id, appointment_id?, external_event_id?, direction(out|in), at, result(ok|error), detail?
  - _Outbound on appointment lifecycle here; inbound direction added by CALENDAR-INBOUND._

## Technical notes (high level)

- Architecture decisions: [ADR-0012](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-10-integrations.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-10-integrations.md)

## Tasks (dev pickup)

- [ ] **Outbound push behind ICalendarProvider (appointment → external event)**
  Behaviour: a clinic appointment appears in the practitioner's linked Outlook/Google calendar. Requirements: implement M365 (MS Graph) and Google adapters behind ICalendarProvider (ADR-0012/0036) so the providers are interchangeable; on appointment create/move/cancel lifecycle events, upsert/delete the external event with a privacy-safe title (no clinical detail beyond what the clinic configures) and store the external id; log each sync (SyncLog).
- [ ] **Per-staff connect UI + sync-mode toggle**
  Behaviour: the Settings → Integrations calendar card and the per-staff connect flow. Requirements: each practitioner connects their OWN M365/Google account (OAuth + token refresh), picks the calendar, sets the sync mode, and sees status + last-sync/error; nothing syncs until a staff member opts in; clinic appointments appear in the staff's external calendar; show the AU/APP-8 (Australian Privacy Principle 8, cross-border disclosure) posture (SUBPROCESSOR-POSTURE). The two-way 'external events block availability' mode is enabled by CALENDAR-INBOUND.
