# Calendar: drag-to-book, move & resize

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/CALENDAR-DRAG`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-02/CALENDAR`

## Background

As a front desk, I want to click an empty slot to start a booking and drag or resize an appointment to reschedule it, so that I can rearrange the diary directly on the grid without re-keying a booking.
Plainly: the direct-manipulation interactions on the calendar grid — click-to-book an empty slot, drag an appointment to move it, resize to change its duration. Where it fits: a follow-up to the multi-resource calendar basic grid (PRD-02/CALENDAR), which renders appointments but doesn't yet let you move them on the grid. It re-uses the basic's server-side availability engine on every drop, and sits in Reception (PRD-02).

## How it works

The basic grid renders appointments statically; this follow-up adds direct manipulation. Clicking an empty slot starts a booking at that time/resource; dragging an appointment moves it to a new slot/resource; resizing the block changes its duration. Everything snaps to the configured slot interval.
Every drop re-runs the SAME server-side availability check the basic engine owns — practitioner scope (canInject for S4), a free room/chair/device for the whole block incl. buffers, and the roster — and an invalid move is rejected with a structured reason rather than silently committing a clash.
The interaction updates optimistically so the grid feels immediate, then confirms against the server or rolls back if the move is rejected, keeping the displayed diary always consistent with what is actually bookable.

## Requirements

- To click an empty slot to start a booking and drag or resize an appointment to reschedule it.

## Acceptance Criteria

- [ ] Clicking an empty slot starts a booking; dragging an appointment moves it; resizing changes its duration.
- [ ] All interactions snap to the configured slot interval.
- [ ] Availability (practitioner scope + room free + roster) is re-checked server-side on drop and an invalid move is rejected with a reason.
- [ ] The UI updates optimistically then confirms or rolls back.

## UI designs / screenshots

- Prototype: Schedule (schedule.png) — in move mode, valid drop targets show a dashed add-location affordance and conflicting room/chair/device usage is flagged inline.
- Click an empty cell to begin a booking; drag a block to move; resize the block edge to change duration; everything snaps to the slot interval.
- An invalid drop is rejected with a reason; the optimistic block reverts on rollback.

![schedule — prototype screen](../screens/schedule.png)

## Suggested data model

- **(extends CALENDAR)** — no new entities; mutates Appointment.start/end/practitioner_id/room_id on move/resize
  - _Re-validates against the same (derived) Availability function on every drop; no new schema._

## Other

- Source PRD: [PRD-02-booking-scheduling.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-02-booking-scheduling.md)

## Tasks (dev pickup)

- [ ] **Drag-to-book / move / resize with slot snapping**
  Behaviour: click an empty slot to start a booking, drag an appointment to move it, and resize to change duration, all snapping to the slot interval. Requirements: the gesture maps to a move/resize of the same Appointment; the surface stays usable on a busy grid; conflicting drop targets are flagged inline.
- [ ] **Server-side re-validation on drop (optimistic + rollback)**
  Behaviour: re-check availability when an appointment is dropped or resized. Requirements: the move re-runs the SAME server-side availability check (practitioner scope + free room/chair/device incl. buffers + roster) and is rejected with a structured reason if invalid; the UI updates optimistically then confirms or rolls back.
