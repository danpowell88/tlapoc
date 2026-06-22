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

- [ ] **Today read aggregation (live clinic state + digest), role + .fin filtered**
  Build the read aggregation that powers Today: the live visit state (waiting / in-room / checked-out) and the day's schedule from the appointment/visit state machine (ADR-0024), the needs-attention digest (overdue recalls, unbilled visits, credential expiries from REG-WATCH, failed payments) and a Follow-ups preview from the Jobs queue (ADR-0023). Filter widget data by the active role's concerns and strip money figures server-side for non-owner roles (FIN-GATING).
- [ ] **Today dashboard UI (concern-tailored widgets + quick links)**
  Build Today (dashboard.png): greeting + at-a-glance line, the stat cards, Today's schedule with per-appointment lifecycle pills (Late/Start/No-show/Confirmed/In treatment/Resume) and Open-chart/Profile/Resume/Checkout quick links into the in-flight visit, and the Follow-ups preview. Show/hide each widget by the active role's concern (data-concern) and .fin-gate the money cards so only the owner sees revenue. Loading/empty/error states.
