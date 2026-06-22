# Today: at-a-glance stat cards

> **Epic:** [PLATFORM — Platform shell, navigation & cross-cutting UX](../epics/PLATFORM.md)  ·  **Key:** `PLATFORM/TODAY-STATCARDS`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PLATFORM/TODAY`

## Background

As a staff member, I want a row of at-a-glance stat cards on Today, so that I can read the shape of the day in one glance.
Plainly: the row of headline number cards at the top of Today — Appointments, Checked in / waiting, Awaiting consent (treatment gated until done) and Stock on hand — so a glance tells you the shape of the day. Where it fits: a follow-up to the role-tailored Today dashboard (PLATFORM/TODAY) that adds the stat-card band above the schedule list. Cards are concern-tagged so each role sees the cards relevant to them, and any money card is gated behind the owner-only financial (.fin) capability.

## How it works

The Today header gains the row of stat cards the prototype shows: Appointments (the day's total), Checked in · waiting (the live front-desk count), Awaiting consent with the 'treatment gated until done' caption (how many visits are still blocked on the consult/consent gate), and Stock on hand. Each card is a derived number over today's appointments and the gate state — not a stored figure — and live-updates as visits move through the lifecycle.
Cards are concern-tagged (the prototype's data-concern) and shown only if the active role carries the concern, so reception sees front-desk counts and a clinician sees the clinical gate counts. Any money-bearing card is additionally gated behind the owner-only financial (.fin) capability so non-owner roles never see revenue on Today.

## Requirements

- A row of at-a-glance stat cards on Today.

## Acceptance Criteria

- [ ] Today renders a row of stat cards: Appointments, Checked in · waiting, Awaiting consent ('treatment gated until done'), Stock on hand.
- [ ] Each card derives from today's appointments + gate state and live-updates from lifecycle/transition events.
- [ ] The 'Awaiting consent' card reflects the consult/consent gate.
- [ ] Cards are concern-tagged (data-concern) and shown per active role; any money card is .fin-gated (owner-only).

## UI designs / screenshots

- Prototype: Today (dashboard.png) — the stat-card row above the schedule (Appointments / Checked in · waiting / Awaiting consent 'treatment gated until done' / Stock on hand).
- Cards concern-tagged (data-concern) and shown per active role; money cards .fin-gated (owner-only).

![dashboard — prototype screen](../screens/dashboard.png)

## Suggested data model

- **(read) TodayBoard (extends PLATFORM/TODAY)** — + stat-card counts: appointments_today, checked_in, waiting, awaiting_consent, stock_on_hand
  - _Derived counts over today's appointments + gate/stock state; concern-tagged + .fin-gated. Extends the TODAY read aggregation; no new write model._

## Other

- Source PRD: [README.md](https://github.com/danpowell88/tlapoc/blob/main/docs/ux/README.md)

## Tasks (dev pickup)

- [ ] **Stat-card counts in the Today read aggregation**
  Behaviour: extend the TODAY read aggregation with the derived counts each card needs — appointments today, checked-in, waiting, awaiting-consent (the consult/consent gate count) and stock on hand. Requirements: derived from today's appointments + gate/stock state, never stored; live-updates from lifecycle/transition events; concern-tag each count so it is only computed/returned for roles that carry the concern; any money figure is stripped server-side for non-owner roles (.fin).
- [ ] **Stat-card row UI on Today**
  Behaviour: render the stat-card row above the schedule (Appointments / Checked in · waiting / Awaiting consent 'treatment gated until done' / Stock on hand). Requirements: cards shown per the active role's concerns; money cards hidden for non-owner roles (.fin); each card live-updates from the read aggregation.
