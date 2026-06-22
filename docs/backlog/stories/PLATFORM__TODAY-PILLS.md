# Today: lifecycle next-action pills + 'WITH YOU NOW' strip

> **Epic:** [PLATFORM — Platform shell, navigation & cross-cutting UX](../epics/PLATFORM.md)  ·  **Key:** `PLATFORM/TODAY-PILLS`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PLATFORM/TODAY`

## Background

As a staff member, I want next-action pills on each appointment and a 'with you now' in-room strip, so that I can move a visit forward and jump straight into the person in front of me.
Plainly: the Today schedule rows gain a next-action button (Late / Start / No-show / Confirmed / In treatment / Resume) for whoever owns the visit right now, plus a 'WITH YOU NOW' strip of who is in-room being treated with one-click Open-chart / Profile links. Where it fits: a follow-up to the role-tailored Today dashboard (PLATFORM/TODAY) that turns the read-only schedule list into an actionable board. The pills drive the appointment/visit state machine (ADR-0024) and deep-link into the in-flight visit, so a row is never a dead end.

## How it works

The Today schedule list (PLATFORM/TODAY) becomes actionable: each appointment shows the single next-action pill for whoever owns it now — Late, Start, No-show, Confirmed, In treatment or Resume — and pressing it calls the matching appointment/visit lifecycle transition (ADR-0024). A pill is shown only when it is a legal transition for the row's current state and the acting user's role, so the board can't offer an action the visit or person can't take.
Above the list, a 'WITH YOU NOW' strip surfaces the in-room visits — who is being treated right now — with Open-chart and Profile quick links so a clinician jumps straight to the person in front of them. Every row deep-links into the in-flight visit (Open chart / Profile / Resume / Checkout), and the board live-updates from transition events so two staff watching Today see the same state.

## Requirements

- Next-action pills on each appointment and a 'with you now' in-room strip.

## Acceptance Criteria

- [ ] Each schedule row shows the next-action pill legal for its state and the user's role (Late / Start / No-show / Confirmed / In treatment / Resume).
- [ ] Pressing a pill calls the appointment/visit lifecycle transition (ADR-0024) and the row updates live.
- [ ] A 'WITH YOU NOW' strip shows who is in-room being treated, with Open-chart / Profile quick links.
- [ ] Rows deep-link into the in-flight visit (Open chart / Profile / Resume / Checkout).

## UI designs / screenshots

- Prototype: Today (dashboard.png) — per-appointment lifecycle pills (Late / Start / No-show / Confirmed / In treatment / Resume) and the 'WITH YOU NOW' in-room strip with Open-chart / Profile quick links.
- Each pill is shown only when legal for the row's state + the user's role and calls the lifecycle transition; rows deep-link into the in-flight visit; live-updates from transition events.

![dashboard — prototype screen](../screens/dashboard.png)

## Suggested data model

- **(read) TodayBoard (extends PLATFORM/TODAY)** — + per-row legal next-actions (from the appointment/visit state machine), + in-room set for the WITH-YOU-NOW strip
  - _Reads the appointment/visit state machine (ADR-0024); no new write model — the pills call existing lifecycle transitions._

## Other

- Source PRD: [README.md](https://github.com/danpowell88/tlapoc/blob/main/docs/ux/README.md)

## Tasks (dev pickup)

- [ ] **Per-row next-action pills wired to the lifecycle transitions**
  Behaviour: render the next-action pill on each schedule row (Late / Start / No-show / Confirmed / In treatment / Resume) and wire it to the appointment/visit lifecycle transition (ADR-0024). Requirements: show a pill only when its transition is legal for the row's current state and the acting user's role; the row updates live on transition; the board reflects transitions made elsewhere.
- [ ] **'WITH YOU NOW' in-room strip + deep links**
  Behaviour: render the 'WITH YOU NOW' strip of in-room visits with Open-chart / Profile quick links, and make every schedule row deep-link into the in-flight visit (Open chart / Profile / Resume / Checkout). Requirements: the in-room set comes from the appointment/visit state machine; quick links respect the user's role; live-updates from transition events.
