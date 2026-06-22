# Calendar: day / week view toggle & time-axis layout

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/CALENDAR-DAYWEEK`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-02/CALENDAR`

## Background

As a front desk, I want to switch the calendar between a single-day and a Mon–Fri week layout with a sensible time axis, so that I can see one day in detail or the whole week at a glance.
Plainly: the toggle that flips the schedule between a detailed single-day view and a week overview, and the time axis both share. Where it fits: a follow-up to the multi-resource calendar basic grid (PRD-02/CALENDAR), which ships day-view only; this adds the week layout and the configurable time axis. It reads the active range from the header navigation (PRD-02/CALENDAR-HEADER-NAV) and sits in Reception (PRD-02).

## How it works

The basic grid shows a single day; this follow-up adds a day/week toggle and the time-axis layout both views share. Week view recasts the grid into Mon–Fri day columns for a whole-week overview; day view keeps the detailed practitioner × room columns.
The time axis spans the clinic's configured opening hours, with off-hours muted, and the slot interval (e.g. 15 minutes) is selectable so the grid granularity matches how the clinic books. Closed days and public holidays render non-bookable in both layouts.
The chosen view persists per user (alongside the last-viewed date from CALENDAR-HEADER-NAV) so the schedule reopens the way each user prefers.

## Requirements

- To switch the calendar between a single-day and a Mon–Fri week layout with a sensible time axis.

## Acceptance Criteria

- [ ] A toggle switches between a single-day and a Mon–Fri week layout.
- [ ] The time axis spans configured opening hours with off-hours visually muted; the slot interval is selectable (e.g. 15 min).
- [ ] Week view collapses resource columns into day columns.
- [ ] Closed days and public holidays render non-bookable; the choice persists per user.

## UI designs / screenshots

- Prototype: Schedule (schedule.png) — the Day/Week toggle in the header.
- Day view: practitioner × room columns with hourly rows; week view: Mon–Fri day columns.
- Time axis spans opening hours with off-hours muted; closed days/holidays render non-bookable; selectable slot interval.

![schedule — prototype screen](../screens/schedule.png)

## Suggested data model

- **(extends CALENDAR)** — no new entities; adds a per-user view (day|week) + slot-interval preference; reads opening-hours / closed-days config
  - _Re-lays-out the same Appointment + Availability data; opening hours and public holidays come from clinic config._

## Other

- Source PRD: [PRD-02-booking-scheduling.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-02-booking-scheduling.md)

## Tasks (dev pickup)

- [ ] **Day / week toggle + week-column layout**
  Behaviour: a toggle that switches between a single-day grid and a Mon–Fri week layout. Requirements: week view collapses the practitioner × room columns into day columns; day view keeps the detailed resource columns; the choice persists per user; both read the active range from the header.
- [ ] **Time-axis layout (opening hours, slot interval, closed days)**
  Behaviour: a time axis spanning the configured opening hours with off-hours muted and a selectable slot interval (e.g. 15 min). Requirements: closed days and public holidays render non-bookable; the slot interval governs how appointments snap; opening hours and holidays come from clinic config.
