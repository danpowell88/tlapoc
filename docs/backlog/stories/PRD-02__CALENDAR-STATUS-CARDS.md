# Calendar: appointment cards, status colours & summary strip

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/CALENDAR-STATUS-CARDS`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-02/CALENDAR`

## Background

As a front desk, I want appointment cards colour-coded by status and treatment, with a summary strip of counts and utilisation, so that I can read the day's state at a glance and act on each appointment from the grid.
Plainly: the visual treatment of each appointment block (colour by treatment type, status icons, quick actions) plus the summary strip of counts and utilisation above the grid. Where it fits: a follow-up to the multi-resource calendar basic grid (PRD-02/CALENDAR), which renders plain blocks; this adds the operational signal the front desk runs on. Status feeds the visit lifecycle (PRD-02/LIFECYCLE) and a no-show raises a follow-up job (PRD-07). It sits in Reception (PRD-02).

## How it works

The basic grid renders plain blocks; this follow-up makes each appointment card carry its operational meaning — client name, treatment and status — colour-coded by treatment type with a legend (anti-wrinkle / filler / skin / consult) and by status, with quick actions. Clicking a card opens the appointment detail / move-cancel modal.
Above the grid a summary strip surfaces the signal the desk runs on: total appointments, per-treatment-type counts as chips, chairs-booked utilisation %, and idle chair-hours, derived from the day's appointments and resources.
Status drives behaviour beyond colour: a no-show raises a follow-up job in the PRD-07 queue, and arrived/in-progress states feed the check-in and treatment-room surfaces. The status set ties to the visit lifecycle (PRD-02/LIFECYCLE).

## Requirements

- Appointment cards colour-coded by status and treatment, with a summary strip of counts and utilisation.

## Acceptance Criteria

- [ ] Each appointment card shows client, treatment and status with a colour legend (anti-wrinkle / filler / skin / consult).
- [ ] Status (booked / confirmed / arrived / in-progress / complete / cancelled / no-show) drives the card colour and quick actions; clicking opens the appointment detail.
- [ ] A summary strip surfaces total appointments, per-treatment-type counts, chairs-booked utilisation % and idle chair-hours.
- [ ] A no-show raises a follow-up job (PRD-07); arrived/in-progress feed the check-in and treatment-room surfaces.

## UI designs / screenshots

- Prototype: Schedule (schedule.png) — appointment blocks colour-coded by treatment type with a legend, carrying client name, type and status icons.
- Summary strip above the grid: total appointments (14), chairs booked (68%), idle chair time (~12h), and per-type counts as chips.
- Tap a card to open the move/cancel modal; status colours distinguish booked / confirmed / arrived / in-progress / complete / cancelled / no-show.

![schedule — prototype screen](../screens/schedule.png)

## Suggested data model

- **(extends CALENDAR)** — no new entities; derives card colour from service.treatment_type and Appointment.status; computes a (derived) DaySummary (counts, utilisation %, idle chair-hours)
  - _Reads the basic's Appointment + Resource data; status transitions are owned by LIFECYCLE; a no-show raises a Job (PRD-07)._

## Other

- Source PRD: [PRD-02-booking-scheduling.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-02-booking-scheduling.md)

## Tasks (dev pickup)

- [ ] **Status/treatment-coloured appointment cards + quick actions**
  Behaviour: each appointment card shows client, treatment and status, colour-coded by treatment type (legend: anti-wrinkle / filler / skin / consult) and by status, with quick actions. Requirements: status drives the colour; clicking opens the appointment detail/modal; a no-show raises a follow-up job (PRD-07) and arrived/in-progress feed check-in and treatment-room surfaces.
- [ ] **Summary strip (counts, utilisation, idle chair-hours)**
  Behaviour: a strip above the grid with total appointments, per-treatment-type counts, chairs-booked utilisation % and idle chair-hours. Requirements: figures derive from the day's appointments and resources; per-type counts render as chips; utilisation and idle hours surface the operational signal the desk runs on.
