# Visit lifecycle: Today KPI tiles & in-room strip

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/LIFECYCLE-TODAY-BOARD`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-02/LIFECYCLE`

## Background

As a front desk, I want Today header tiles and a 'WITH YOU NOW' in-room strip, so that I can see the day's state and who's in treatment at a glance.
Plainly: the Today dashboard's summary — KPI tiles (appointments, checked in, awaiting consent, stock, follow-ups) and a 'WITH YOU NOW' strip showing who is currently in-room. Where it fits: a follow-up to the visit lifecycle basic state-machine (PRD-02/LIFECYCLE) that adds the at-a-glance Today board on top of the status data. The 'awaiting consent' tile ties to the consult/consent gates (PRD-02/CONSULT-GATE, PRD-03/GATING). It sits in Reception (PRD-02).

## How it works

The basic list shows rows; this follow-up adds the Today board's summary view. Header KPI tiles surface appointments, checked in, awaiting consent, stock and follow-ups, derived from today's appointments and the gate state.
A 'WITH YOU NOW' in-room strip lists every appointment currently in the in_room state, each with Open chart and Profile quick links so a clinician can jump straight to the right record.
Everything live-updates from the transition events the basic state-machine emits; the 'awaiting consent' tile reflects the consult/consent gate, tying the lifecycle to the compliance gates.

## Requirements

- Today header tiles and a 'WITH YOU NOW' in-room strip.

## Acceptance Criteria

- [ ] Today header tiles show appointments, checked in, awaiting consent, stock and follow-ups.
- [ ] A 'WITH YOU NOW' strip lists every appointment in the in_room state with Open chart / Profile quick links.
- [ ] Tiles derive from today's appointments + gate state and live-update from transition events.
- [ ] The 'awaiting consent' tile reflects the consult/consent gate.

## UI designs / screenshots

- Prototype: Today (dashboard.png) — KPI tiles (appointments, checked in, awaiting consent, stock, follow-ups) and a 'WITH YOU NOW' in-room strip (client + Open chart/Profile).
- Tiles live-update from transition events; the in-room strip lists in_room appointments.
- 'Awaiting consent — treatment gated until done' tile ties the lifecycle to the gates.

![schedule — prototype screen](../screens/schedule.png)

## Suggested data model

- **(derived) TodaySummary (extends LIFECYCLE)** — = today's appointments + gate state → tile counts; in_room appointments → in-room strip
  - _Read-model fed by transition events; the gate state comes from the consult/consent gates._

## Other

- Source PRD: [PRD-02-booking-scheduling.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-02-booking-scheduling.md)

## Tasks (dev pickup)

- [ ] **Today KPI tiles + 'WITH YOU NOW' in-room strip**
  Behaviour: the Today header tiles (appointments, checked in, awaiting consent, stock, follow-ups) and a 'WITH YOU NOW' strip showing who is in-room with Open chart / Profile quick links. Requirements: tiles derive from today's appointments + gate state and live-update from transition events; the in-room strip lists every appointment in the in_room state; the 'awaiting consent' tile reflects the gate (ties to the consult/consent gates).
