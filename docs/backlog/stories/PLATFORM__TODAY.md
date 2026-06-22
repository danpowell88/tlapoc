# Role-tailored Today dashboard

> **Epic:** [PLATFORM — Platform shell, navigation & cross-cutting UX](../epics/PLATFORM.md)  ·  **Key:** `PLATFORM/TODAY`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** web
>
> **Depends on:** `PLATFORM/APP-NAV`

## Background

As a staff member, I want a Today landing page showing the live state of the clinic and what needs my attention, tailored to my role, so that I start the day knowing exactly what to do.
Plainly: the landing page staff open onto — the live state of the clinic today and what needs their attention, tailored to their role. It is built on the app shell. Reception sees front-desk tasks, a clinician sees clinical ones, the owner sees the business digest — one screen, role-aware, with one click through to the next action. The prototype opens on a Today board: waiting / in-room / checked-out columns, the day's appointments, the jobs/needs-attention digest and alerts — tailored to the signed-in role's 'concerns' (ADR-0017).

## How it works

Today is the landing page — the live state of the clinic at a glance, tailored to the signed-in role's concerns (ADR-0017). The prototype shows it as a greeting ('Good morning, Lena'), a date/at-a-glance line ('14 appointments · 3 checked in'), a row of stat cards (Appointments 14 / Checked in 3 · 1 waiting / Awaiting consent 2 'treatment gated until done' / Stock on hand), Today's schedule (each appointment with its lifecycle state pills — Late, Start, No-show, Confirmed, In treatment, Resume — per ADR-0024 visit lifecycle), and a Follow-ups panel previewing the queue.
Role-tailoring is by concern, not by separate dashboards: each widget is tagged with a concern (the prototype's data-concern) and shown only if the active role carries it. Reception sees front-desk widgets (waiting/checked-in, recall), an NP (nurse practitioner) sees clinical (awaiting-consent, in-room, stock alerts), the owner sees the business digest. Money cards are additionally .fin-gated (FIN-GATING) so non-owner roles never see revenue on Today.
The 'waiting / in-room / checked-out' live state and the day's schedule come from the appointment/visit state machine (ADR-0024); the needs-attention digest aggregates exceptions (overdue recalls, unbilled visits, expiries from REG-WATCH, failed payments) and the Follow-ups preview reads the Jobs queue (ADR-0023). Quick links jump straight into the in-flight visit: Open chart, Profile, Resume, Checkout.
It's a read aggregation (no new write model) — so each role starts the day knowing exactly what to do, with one click to the next action.

## Requirements

- A Today landing page showing the live state of the clinic and what needs my attention, tailored to my role.

## Acceptance Criteria

- [ ] Today shows waiting / in-room / checked-out and the day's schedule at a glance.
- [ ] The content is role-tailored by concern (e.g. reception sees front-desk tasks, NP sees clinical).
- [ ] Surfaces the follow-up/needs-attention digest and key alerts (expiries, failed payments).
- [ ] Quick links jump to chart/profile/checkout for in-flight visits.

## UI designs / screenshots

_Prototype screen: prototype.html — Today (waiting / in-room / checked-out)._

- Prototype: Today (dashboard.png) — greeting + at-a-glance line, stat cards (Appointments / Checked in · waiting / Awaiting consent / Stock on hand), Today's schedule with per-appointment lifecycle pills (Late / Start / No-show / Confirmed / In treatment / Resume) and Open-chart/Profile quick links, and a Follow-ups preview panel.
- Widgets are concern-tagged (data-concern) and shown per active role; money cards are .fin-gated (owner only).
- Reception sees front-desk tasks; NP sees clinical; owner sees the business digest.

![dashboard — prototype screen](../screens/dashboard.png)

## Suggested data model

- **(read) TodayBoard** — from Appointment/Visit.status (waiting|in-room|checked-out) + Job queue + AttentionDigest, filtered by the active role's concerns and .fin (the owner-only financial gate — money figures are stripped for non-owner roles) gating
  - _Role-tailored read aggregation; no separate persistence. Money figures stripped server-side for non-owner roles._

## Technical notes (high level)

- Architecture decisions: [ADR-0017](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [README.md](https://github.com/danpowell88/tlapoc/blob/main/docs/ux/README.md)

## Tasks (dev pickup)

- [ ] **Greeting + at-a-glance stat cards (Appointments / Checked in / Awaiting consent / Stock)**
  Behaviour: the Today header — a personalised greeting ('Good morning, Lena'), a date/at-a-glance line ('14 appointments · 3 checked in') and the row of stat cards (Appointments, Checked in · waiting, Awaiting consent 'treatment gated until done', Stock on hand). Requirements: each card derives from today's appointments + gate state and live-updates from lifecycle/transition events; the 'Awaiting consent' card reflects the consult/consent gate; cards are concern-tagged (data-concern) and shown per active role; any money card is .fin-gated (owner-only).
- [ ] **Today's schedule with lifecycle pills + 'WITH YOU NOW' in-room strip**
  Behaviour: the Today's schedule list — each appointment with its current status and the next-action pill for whoever owns it now (Late / Start / No-show / Confirmed / In treatment / Resume) — plus a 'WITH YOU NOW' in-room strip showing who is being treated with Open-chart / Profile quick links. Requirements: the live waiting / in-room / checked-out state comes from the appointment/visit state machine (ADR-0024); each pill calls the lifecycle transition and is shown only when legal for the row's state and the user's role; rows deep-link into the in-flight visit (Open chart / Profile / Resume / Checkout); live-updates from transition events.
- [ ] **Follow-ups preview panel + needs-attention digest**
  Behaviour: a Follow-ups preview previewing the Jobs queue and (for the owner) the needs-attention exceptions strip (overdue recalls, unbilled visits, credential expiries from REG-WATCH, failed payments). Requirements: the preview reads the Jobs queue (ADR-0023) with an 'Open queue →' link; the needs-attention items mirror ATTENTION-DIGEST (PRD-08) and deep-link to source; money-bearing items (failed payments) are .fin-gated/genericised for non-owner roles; concern-tailored so reception sees front-desk items, the owner the business digest.
- [ ] **Today read aggregation (role + .fin filtered)**
  Behaviour: the read aggregation powering Today — live visit state (waiting / in-room / checked-out) and the day's schedule from the appointment/visit state machine (ADR-0024), the needs-attention digest and the Follow-ups preview from the Jobs queue (ADR-0023). Requirements: filter widget data by the active role's concerns; strip money figures server-side for non-owner roles (FIN-GATING) so the payload is already safe before the UI hides anything; no separate write model (it's a read aggregation); loading/empty/error states.
