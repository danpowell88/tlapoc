# Two-way calendar sync (M365 / Google)

> **Epic:** [PRD-10 — Integrations: Xero & calendar](../epics/PRD-10.md)  ·  **Key:** `PRD-10/CALENDAR-SYNC`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** integration
>
> **Depends on:** `PRD-02/CALENDAR`

## Background

As a practitioner, I want my appointments to appear in Outlook/Google and external busy-time to block my availability, so that I have one source of truth for my time.
This story keeps each practitioner's appointments in sync with their own Outlook or Google calendar both ways: clinic bookings appear in their personal calendar, and personal busy-time blocks their clinic availability, so they have one source of truth for their time. It sits in the Integrations layer (step 10 of the clinic-first build), built after the booking calendar it syncs with (PRD-02 CALENDAR). Sync is per-staff opt-in; calendar providers are sub-processors governed by the residency posture (SUBPROCESSOR-POSTURE). Appointments sync both ways with Outlook/Google; external busy events block availability, behind ICalendarProvider (REQ-INT-2).

## How it works

Two-way sync of appointments with staff calendars — Microsoft 365 (MS Graph) and Google Calendar — behind an ICalendarProvider port (ADR-0012, promoted to bidirectional under ADR-0036). Creating, moving or cancelling a clinic appointment reflects in the practitioner's linked calendar; and external busy events created in their personal calendar flow back and block their availability in booking (PRD-02 CALENDAR), so a practitioner has one source of truth for their time and the clinic never double-books over a dentist appointment.
Sync is per-staff opt-in: each practitioner connects their own M365/Google account (OAuth), choosing the calendar and a two-way mode; nothing syncs for staff who haven't connected. Outbound pushes are driven by appointment lifecycle events; inbound busy-time is pulled (polling or change-notifications) and projected as availability blocks. Conflict-resolution rules — what wins when an external event and a clinic booking overlap — are an open question; the safe default treats external busy-time as blocking-only (it never deletes or moves a clinic appointment).
Each sync action is logged (direction, appointment, result) for troubleshooting. Because it sits behind ICalendarProvider, M365 and Google are interchangeable adapters and a new provider needs no core change. No clinical detail leaks into the external calendar beyond what the clinic configures (privacy-safe event titles); calendar providers are sub-processors subject to the AU/APP-8 (Australian Privacy Principle 8, cross-border disclosure) posture (SUBPROCESSOR-POSTURE).

## Requirements

- My appointments to appear in Outlook/Google and external busy-time to block my availability.

## Acceptance Criteria

- [ ] Creating/moving/cancelling a clinic appointment reflects in the linked Outlook/Google calendar, and external busy events block availability in booking (PRD-02).
- [ ] Sync is per-staff opt-in (each practitioner connects their own M365/Google account; nothing syncs until connected).
- [ ] Conflict-resolution rules are supported (open question); the default treats external busy-time as blocking-only — it never mutates a clinic appointment.
- [ ] Implemented behind ICalendarProvider (M365/Google swappable); each sync action is logged.
- [ ] External event titles are privacy-safe per clinic config; calendar providers honour the AU/APP-8 posture.

## UI designs / screenshots

- Prototype: Settings → Integrations (settings-integrations.png) — 'Calendar sync (M365 / Google)' card, 'Two-way — external events block availability.', currently 'Outbound only', Connect →.
- Per-staff connect (M365/Google OAuth) + two-way sync toggle + calendar picker.
- Schedule (schedule.png, PRD-02): external busy time shows as unavailable; clinic appointments appear in the staff's external calendar.
- Sync log / status per staff link (last sync, errors).

![settings-integrations — prototype screen](../screens/settings-integrations.png)

## Suggested data model

- **CalendarLink** — id, staff_id, provider(m365|google), oauth_tokens, calendar_id, sync_mode(two_way|outbound), status, region
  - _Per-staff opt-in; AU/APP-8 posture (SUBPROCESSOR-POSTURE)._
- **SyncLog** — id, calendar_link_id, appointment_id?, external_event_id?, direction(out|in), at, result(ok|error), detail?
  - _Inbound busy events project as availability blocks; outbound on appointment lifecycle._

## Technical notes (high level)

- Architecture decisions: [ADR-0012](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-10-integrations.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-10-integrations.md)

## Tasks (dev pickup)

- [ ] **Outbound push behind ICalendarProvider (appointment → external event)**
  Behaviour: a clinic appointment appears in the practitioner's linked Outlook/Google calendar. Requirements: implement M365 (MS Graph) and Google adapters behind ICalendarProvider (ADR-0012/0036) so the providers are interchangeable; on appointment create/move/cancel lifecycle events, upsert/delete the external event with a privacy-safe title (no clinical detail beyond what the clinic configures) and store the external id; log each sync (SyncLog).
- [ ] **Inbound busy-time → availability blocks (blocking-only default)**
  Behaviour: external busy events in a practitioner's personal calendar block their clinic availability. Requirements: pull external busy events (polling or change-notifications) and project them as availability blocks consumed by PRD-02 booking; the default conflict rule is blocking-only — external busy-time never deletes or moves a clinic appointment (conflict resolution beyond that is the open question); so the clinic never double-books over a personal appointment.
- [ ] **Per-staff connect UI + two-way toggle**
  Behaviour: the Settings → Integrations calendar card and the per-staff connect flow. Requirements: each practitioner connects their OWN M365/Google account (OAuth + token refresh), picks the calendar, sets a two-way/outbound mode, and sees status + last-sync/error; nothing syncs until a staff member opts in; external busy-time shows as unavailable in the Schedule (PRD-02); show the AU/APP-8 (Australian Privacy Principle 8, cross-border disclosure) posture (SUBPROCESSOR-POSTURE).
