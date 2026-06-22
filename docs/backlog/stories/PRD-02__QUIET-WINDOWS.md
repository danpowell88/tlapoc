# Quiet windows to fill (idle-slot recovery)

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/QUIET-WINDOWS`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** —
>
> **Depends on:** `PRD-02/CALENDAR`

## Background

As a front-of-house lead, I want to see upcoming quiet windows and fill them in one click, so that idle chairs are recovered before they cost us and before stock expires.
Plainly: a panel on the schedule that spots upcoming low-occupancy windows and helps fill them - by recall, a waitlist offer or a targeted campaign - before the chair sits idle. Where it fits: part of the Reception schedule and a sibling of the multi-resource calendar (PRD-02/CALENDAR); it reads occupancy from the calendar and stock expiry from injectables inventory (PRD-04), and the fill actions create follow-up jobs handled by Comms (PRD-07). A quiet window is an upcoming slot a resource has free during opening hours.

## How it works

The schedule already knows occupancy; this feature projects upcoming slots where a resource is free during opening hours and ranks them by how quiet (and how soon) they are. The threshold and the rolling horizon (e.g. the next 14 days) are configurable.
Each window is framed with a why: an idle chair spreads fixed staff cost across fewer treatments, so cost-per-treatment rises. The dollar framing is owner-only and stripped for non-owner roles (the .fin capability).
Inventory is cross-referenced: lots nearing expiry (FEFO - first-expiry-first-out) are matched to nearby quiet windows so the clinic can book treatments that consume that stock before it must be written off.
Filling a window hands off to existing channels: a recall worklist entry, a waitlist offer to a waiting client, or a small targeted campaign - each becomes a follow-up job (PRD-07) and honours the client's marketing-consent state.

## Requirements

- To see upcoming quiet windows and fill them in one click.

## Acceptance Criteria

- [ ] Upcoming quiet windows are detected per resource/day across a rolling horizon and listed with how idle each is.
- [ ] Each window shows the business reason to fill it (an idle chair raises staff cost-per-treatment), with figures gated to owner-only (.fin).
- [ ] Stock nearing expiry (first-expiry-first-out, FEFO) is surfaced against windows that could absorb it to avoid a write-off.
- [ ] A one-click fill action offers recall, a waitlist offer or a targeted campaign and creates the matching follow-up jobs, respecting marketing consent.

## UI designs / screenshots

- 'Quiet windows to fill' panel header with a savings icon and the one-line rationale (filling idle chairs cuts staff cost-per-treatment).
- A responsive grid of window cards (resource, day, idle duration) with a Fill affordance per card.
- An inline stock-expiry hint on cards where an expiring lot could be absorbed (e.g. 'Lot expiring ~6 wks - 3 quiet windows could absorb it').
- Owner-only savings/cost figures rendered only when the .fin capability is present.

![schedule — prototype screen](../screens/schedule.png)

## Suggested data model

- **QuietWindow (read-model)** — resource_id, date, start, end, idle_minutes, score; projected from appointments + roster + opening hours
  - _Derived/projected, not hand-edited; refreshed as bookings change._
- **FillAction** — id, quiet_window_ref, kind(recall|waitlist|campaign), created_job_id, actor_id, at
  - _Audit of what was done to fill a window._

## Other

- Source PRD: [PRD-02-booking-scheduling.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-02-booking-scheduling.md)

## Tasks (dev pickup)

- [ ] **Idle-slot detection (quiet-window projection)**
  Behaviour: project upcoming slots where a resource is free during opening hours, ranked by idle duration and proximity. Requirements: configurable quietness threshold and rolling horizon; excludes closed days, time-off and blocked time; refreshes as bookings change. Reads occupancy from the calendar (PRD-02/CALENDAR).
- [ ] **Cost-per-treatment / savings framing**
  Behaviour: show why a window matters - an idle chair raises staff cost-per-treatment - with an estimated figure. Requirements: all dollar/cost figures are owner-only and stripped for non-owner roles (the .fin capability); non-owners see the window and the prompt to fill it, but no money.
- [ ] **Stock-expiry / FEFO tie-in**
  Behaviour: surface lots nearing expiry and match them to quiet windows that could absorb the stock. Requirements: pulls expiring lots from injectables inventory (PRD-04) ordered first-expiry-first-out (FEFO); flags the write-off avoided; links through to the stock item.
- [ ] **Fill action: recall / waitlist offer / campaign**
  Behaviour: a one-click action to fill a window via the recall worklist, a waitlist offer, or a small targeted campaign. Requirements: creates the matching follow-up jobs (PRD-07); honours each client's marketing-consent state; records a FillAction for audit.
