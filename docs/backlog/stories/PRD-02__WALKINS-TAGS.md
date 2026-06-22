# Walk-ins: VIP / first-time tags & distinct rendering

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/WALKINS-TAGS`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-02/WALKINS`

## Background

As a front desk, I want VIP and first-time tags on appointments and walk-in blocks rendered distinctly, so that the team spots walk-ins and special clients at a glance.
Plainly: appointment tags (VIP, first-time) set at booking, and rendering walk-in blocks distinctly on the calendar with a quick-add affordance. Where it fits: a follow-up to the walk-ins basic gate-respecting booking (PRD-02/WALKINS) that adds tagging and distinct rendering on top of the walk-in flow. It re-uses the existing move/cancel modal and the calendar block rendering. It sits in Reception (PRD-02).

## How it works

The basic walk-in flow creates the appointment; this follow-up adds the visual signal. Appointments can carry tags[] (vip, first_time) set at booking, and walk-in blocks render distinctly on the calendar (e.g. 'Walk-in NEW') with a quick-add affordance from an open/quiet cell.
Tags render both on the calendar block and on the appointment record so the team spots a VIP or first-time client and any walk-in at a glance.
It reuses the existing move/cancel modal, and the conflict warning (PRD-02/WALKINS-CONFLICT) still shows before confirmation — this story only adds the tagging and distinct rendering.

## Requirements

- VIP and first-time tags on appointments and walk-in blocks rendered distinctly.

## Acceptance Criteria

- [ ] Appointment tags[] (vip, first_time) can be set at booking.
- [ ] Walk-in blocks render distinctly (e.g. 'Walk-in NEW') with a quick-add affordance from an open/quiet cell.
- [ ] Tags render on the calendar block and on the appointment.
- [ ] The existing move/cancel modal is reused and the conflict warning shows before confirmation.

## UI designs / screenshots

- Prototype: Schedule (schedule.png) — a 'Walk-in NEW · Skin' block rendered distinctly; VIP / first-time tags on the appointment.
- A quick-add affordance from an open/quiet cell; tags render on the block and the appointment.
- Reuses the move/cancel modal; the conflict warning shows before confirm.

![schedule — prototype screen](../screens/schedule.png)

## Suggested data model

- **Appointment (extends WALKINS)** — tags[] (vip|first_time)
  - _Tags set at booking; render on the calendar block and the appointment; walk-in blocks render distinctly._

## Other

- Source PRD: [PRD-02-booking-scheduling.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-02-booking-scheduling.md)

## Tasks (dev pickup)

- [ ] **VIP / first-time tags + distinct walk-in rendering**
  Behaviour: support appointment tags[] (vip, first_time) set at booking and render walk-in blocks distinctly (e.g. 'Walk-in NEW') with a quick-add affordance from an open/quiet cell. Requirements: tags render on the calendar block and on the appointment; reuse the existing move/cancel modal; the conflict warning shows before confirmation.
