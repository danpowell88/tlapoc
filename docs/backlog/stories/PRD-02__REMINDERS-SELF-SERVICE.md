# Reminders: self-service reschedule / cancel within policy

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/REMINDERS-SELF-SERVICE`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-02/REMINDERS`

## Background

As a client, I want to reschedule or cancel my appointment myself within the clinic's policy, so that I don't need to call and the diary stays accurate.
Plainly: letting a client move or cancel their own appointment within the clinic's cancellation window, freeing the slot when they do. Where it fits: a follow-up to the reminders basic scheduling & dispatch (PRD-02/REMINDERS) that adds client self-service on top of the reminder. It reuses the availability engine to move and emits the slot-freed event the waitlist (PRD-02/WAITLIST) backfills from. There is no deposit and no auto-charge in v1. It sits in Reception (PRD-02).

## How it works

The basic story sends reminders; this follow-up lets the client act on their booking without calling. Within the configurable cancellation window the client can self-reschedule (reusing the same availability engine to find a new slot) or cancel.
A cancel or successful reschedule frees the original slot and emits the slot-freed event the waitlist (PRD-02/WAITLIST) backfills from, keeping the diary accurate.
Outside the cancellation window the configured rule applies (block/flag/message) — there is NO deposit and NO auto-charge in v1 (REQ-BOOK-3). All self-service actions are audited. The window itself comes from the cancellation policy (PRD-02/REMINDERS-POLICY).

## Requirements

- To reschedule or cancel my appointment myself within the clinic's policy.

## Acceptance Criteria

- [ ] A client can self-reschedule or cancel within the cancellation window.
- [ ] Inside the window: reuse the availability engine to move, or cancel and free the slot (emitting the slot-freed event).
- [ ] Outside the window: apply the configured rule (block/flag/message) with NO charge or deposit in v1.
- [ ] All self-service actions are audited.

## UI designs / screenshots

- Client app / SMS / email: reschedule/cancel links (self-service within policy).
- Inside the window the client picks a new slot via the availability engine or cancels; outside it the configured rule shows.
- v1 explicitly states 'no auto-charge'.

![schedule — prototype screen](../screens/schedule.png)

## Suggested data model

- **(extends REMINDERS)** — no new entities; reuses the availability engine to move and the CancellationPolicy to enforce the window
  - _Inside-window move/cancel frees the slot (emits slot-freed for WAITLIST); no charge/deposit in v1; audited._

## Other

- Source PRD: [PRD-02-booking-scheduling.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-02-booking-scheduling.md)

## Tasks (dev pickup)

- [ ] **Self-service reschedule / cancel within policy**
  Behaviour: the client can self-reschedule or cancel within the cancellation window. Requirements: enforce CancellationPolicy.window_hours server-side — inside the window reuse the availability engine to move, or cancel and free the slot (emits the slot-freed event for WAITLIST); outside the window apply the configured rule (block/flag/message) with NO charge or deposit in v1; all actions audited.
