# Calendar: resource & practitioner filters

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/CALENDAR-FILTERS`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-02/CALENDAR`

## Background

As a front desk, I want to filter the calendar by practitioner, room and treatment type, with a 'my schedule' quick filter, so that I can focus on just the columns I care about on a busy day.
Plainly: the filter controls that narrow which practitioner/room columns and which treatment types the schedule shows. Where it fits: a follow-up to the multi-resource calendar basic grid (PRD-02/CALENDAR); the basic grid shows every resource, and this adds the ability to pare it down. It reads the rostered practitioners for the active range (the same roster the availability engine uses) and sits in Reception (PRD-02).

## How it works

On a busy day the full practitioner × room grid is noisy; this follow-up lets the desk filter the visible columns by practitioner, room and treatment type (multi-select), plus a 'my schedule' quick filter that isolates the signed-in practitioner's columns.
Filters compose with AND, and only practitioners rostered for the active range are offered as filter options (reads the same roster the availability engine uses), so the filter list never offers someone who isn't working.
The active filter set is encoded in the URL/state so a page refresh keeps it and a shared link reproduces the same filtered view.

## Requirements

- To filter the calendar by practitioner, room and treatment type, with a 'my schedule' quick filter.

## Acceptance Criteria

- [ ] Multi-select filters by practitioner, room and treatment type narrow the visible columns/blocks.
- [ ] A 'my schedule' quick filter shows only the signed-in practitioner's columns.
- [ ] Filters compose (AND); only practitioners rostered for the range are offered.
- [ ] The active filter set persists in the URL/state so a refresh or share keeps it.

## UI designs / screenshots

- Prototype: Schedule (schedule.png) — practitioner/room/treatment-type filter controls and a 'my schedule' quick filter above the grid.
- Multi-select chips; the colour legend (anti-wrinkle / filler / skin / consult) ties treatment-type filtering to the grid blocks.
- The active filter set persists in the URL/state across refresh and share.

![schedule — prototype screen](../screens/schedule.png)

## Suggested data model

- **(extends CALENDAR)** — no new entities; a filter state (practitioner_ids[], room_ids[], treatment_types[], my_schedule) held in URL/state
  - _Filters the existing Appointment + resource set; rostered-practitioner options read from the roster._

## Other

- Source PRD: [PRD-02-booking-scheduling.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-02-booking-scheduling.md)

## Tasks (dev pickup)

- [ ] **Multi-select practitioner / room / treatment-type filters + 'my schedule'**
  Behaviour: multi-select filters for practitioner, room and treatment type plus a 'my schedule' quick filter. Requirements: filters compose (AND); only practitioners rostered for the active range are offered as options (reads the roster); 'my schedule' isolates the signed-in practitioner's columns.
- [ ] **Filter-state persistence in URL/state**
  Behaviour: keep the active filter set across refresh and share. Requirements: encode the filter set in the URL/state so a refresh restores it and a shared link reproduces the same filtered view.
