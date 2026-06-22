# Calendar: header & date navigation

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/CALENDAR-HEADER-NAV`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-02/CALENDAR`

## Background

As a front desk, I want a calendar header with Today / previous / next and a date picker that re-queries the diary for any date, so that I can jump around the diary quickly and always know which range I'm looking at.
Plainly: the sticky toolbar at the top of the schedule that controls which date range the calendar shows. Where it fits: a follow-up to the multi-resource calendar basic grid (PRD-02/CALENDAR) that adds date navigation on top of the single-day grid; it is the control every other element on the schedule reacts to (the grid, later the filters and the quiet-windows panel all re-query around the selected range). It sits in Reception (PRD-02), the front-of-house entry point to a visit.

## How it works

The basic calendar renders a single day; this follow-up adds the navigation that lets the desk move through the diary. A sticky header carries Today, previous and next controls, a date picker, and a range label that always states the period currently shown.
Navigating to any date re-queries the availability + appointment data for that range so the grid repaints; Today snaps back to the current day. Keyboard shortcuts (t = today, left/right arrows = step) make moving through a busy week fast.
The last-used date is persisted per user so reopening the schedule lands where they left off. This control becomes the single source of the active range that the grid, and later the filters and quiet-windows panel, all read.

## Requirements

- A calendar header with Today / previous / next and a date picker that re-queries the diary for any date.

## Acceptance Criteria

- [ ] A sticky header shows Today / previous / next, a date picker and a range label reflecting the active view.
- [ ] Jumping to any date re-queries the calendar for that range; Today resets to the current day.
- [ ] Keyboard shortcuts step the range (t = today, arrows = previous/next).
- [ ] The last-used date is remembered per user across sessions.

## UI designs / screenshots

- Prototype: Schedule (schedule.png) — the week-range stepper and date controls in the header above the grid.
- Sticky header: Today button, prev/next chevrons, a date picker, and a human-readable range label (e.g. 'Mon 23 — Fri 27 Jun').
- Changing the date repaints the grid for the new range; keyboard shortcuts (t, arrows) step it.

![schedule — prototype screen](../screens/schedule.png)

## Suggested data model

- **(extends CALENDAR)** — no new entities; adds a per-user last-viewed date/view preference
  - _Re-queries the existing Appointment + Availability data for the selected range; stores a small UI preference per user._

## Other

- Source PRD: [PRD-02-booking-scheduling.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-02-booking-scheduling.md)

## Tasks (dev pickup)

- [ ] **Sticky header with Today / prev / next + date picker**
  Behaviour: a sticky calendar header with Today, previous and next controls, a date picker and a range label reflecting the active view. Requirements: jumping to any date re-queries the appointment/availability data for that range and repaints the grid; Today resets to the current day; keyboard shortcuts (t = today, arrows = step).
- [ ] **Per-user last-viewed-date persistence**
  Behaviour: remember the last-used date per user. Requirements: persist a small per-user preference so reopening the schedule lands on the last viewed date; the header is the single source of the active range every other schedule element reads.
