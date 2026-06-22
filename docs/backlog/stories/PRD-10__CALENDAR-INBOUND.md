# Calendar sync: inbound busy-time → availability blocks

> **Epic:** [PRD-10 — Integrations: Xero & calendar](../epics/PRD-10.md)  ·  **Key:** `PRD-10/CALENDAR-INBOUND`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-10/CALENDAR-SYNC`, `PRD-02/CALENDAR`

## Background

As a practitioner, I want my external busy-time to block my clinic availability, so that the clinic never books me over a personal appointment.
This story pulls each practitioner's personal busy-time back into the clinic so it blocks their clinic availability — the clinic never double-books over a dentist appointment. It sits in the Integrations layer (step 10 of the clinic-first build) as a follow-up to the outbound-push basic (PRD-10/CALENDAR-SYNC), promoting the link to two-way under ADR-0036; the default treats external busy-time as blocking-only — it never mutates a clinic appointment. Calendar providers honour the AU/APP-8 posture (SUBPROCESSOR-POSTURE).

## How it works

External busy events created in a practitioner's personal calendar flow back and block their availability in booking (PRD-02 CALENDAR), so a practitioner has one source of truth for their time and the clinic never double-books over a dentist appointment. This promotes the per-staff CalendarLink (PRD-10/CALENDAR-SYNC) to two-way (ADR-0036).
Inbound busy-time is pulled (polling or change-notifications) and projected as availability blocks consumed by PRD-02 booking. The default conflict rule is blocking-only — external busy-time never deletes or moves a clinic appointment (conflict resolution beyond that is the open question). Each inbound sync action is logged (SyncLog, direction=in); external busy-time shows as unavailable in the Schedule. Calendar providers honour the AU/APP-8 (Australian Privacy Principle 8, cross-border disclosure) posture (SUBPROCESSOR-POSTURE).

## Requirements

- My external busy-time to block my clinic availability.

## Acceptance Criteria

- [ ] External busy events created in a practitioner's personal calendar block their availability in booking (PRD-02).
- [ ] Inbound busy-time is pulled (polling or change-notifications) and projected as availability blocks.
- [ ] The default conflict rule is blocking-only — external busy-time never deletes or moves a clinic appointment (further conflict resolution is the open question).
- [ ] The two-way mode toggles on; each inbound sync action is logged; external busy-time shows as unavailable in the Schedule.

## UI designs / screenshots

- Prototype: Settings → Integrations (settings-integrations.png) — 'Calendar sync' card flips to 'Two-way — external events block availability.' once inbound is on.
- Schedule (schedule.png, PRD-02): external busy time shows as unavailable.
- Inbound sync log / status per staff link (last sync, errors).

![settings-integrations — prototype screen](../screens/settings-integrations.png)

## Suggested data model

- **(reuses) CalendarLink** — PRD-10/CALENDAR-SYNC — sync_mode promoted to two_way
  - _Extends CALENDAR-SYNC; inbound busy events project as availability blocks (blocking-only default)._
- **(reuses) SyncLog** — direction(in) — inbound busy events pulled + projected
  - _Inbound busy-time blocks PRD-02 availability; never mutates a clinic appointment._

## Other

- Source PRD: [PRD-10-integrations.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-10-integrations.md)

## Tasks (dev pickup)

- [ ] **Inbound busy-time → availability blocks (blocking-only default)**
  Behaviour: external busy events in a practitioner's personal calendar block their clinic availability. Requirements: pull external busy events (polling or change-notifications) and project them as availability blocks consumed by PRD-02 booking; the default conflict rule is blocking-only — external busy-time never deletes or moves a clinic appointment (conflict resolution beyond that is the open question); so the clinic never double-books over a personal appointment.
