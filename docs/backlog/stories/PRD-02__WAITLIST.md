# Waitlist & cancellation backfill

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/WAITLIST`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** web
>
> **Depends on:** `PRD-02/REMINDERS`

## Background

As a front desk, I want a waitlist that auto-offers a freed slot when an appointment cancels or no-shows, so that we keep the diary full.
Clients can join a waitlist; cancellations/no-shows auto-offer the freed slot to fill quiet windows.

## How it works

A waitlist captures clients who want an earlier slot; when an appointment cancels or no-shows, the freed slot is auto-offered to the waitlist to keep the diary full and fill quiet windows.
Offered/accepted/expired states are tracked.

## Requirements

- A waitlist that auto-offers a freed slot when an appointment cancels or no-shows.

## Acceptance Criteria

- [ ] Clients can be added to a waitlist for a service/window.
- [ ] Cancelling/no-showing a slot offers it to the waitlist.
- [ ] Quiet-window fill suggestions surface from utilisation data.
- [ ] Offered/accepted/expired waitlist states are tracked.

## UI designs / screenshots

_Prototype screen: prototype.html — Schedule, 'New booking' wizard, Clients directory & 360._

- Prototype: Schedule (schedule.png) — waitlist management + a backfill prompt on cancellation; quiet-window fill suggestions from utilisation.

![schedule — prototype screen](../screens/schedule.png)

## Suggested data model

- **WaitlistEntry** — id, tenant_id, client_id, service_id, window, status(waiting|offered|accepted|expired), offered_at
  - _Backfills on cancel/no-show._

## Technical notes (high level)

- Architecture decisions: [ADR-0026](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-02-booking-scheduling.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-02-booking-scheduling.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations**
  Model + migrate (EF Core; every table carries tenant_id with an RLS policy):
  - WaitlistEntry — id, tenant_id, client_id, service_id, window, status(waiting|offered|accepted|expired), offered_at (Backfills on cancel/no-show.)
  - Add the FKs/relationships above; index the columns this story filters or looks up on; make records append-only/immutable where the story requires it.
- [ ] **Backend: domain logic, rules & API endpoint(s)**
  Domain logic + the API the web/Flutter clients call; enforce every rule server-side (never trust the UI):
  - Endpoints: the commands + queries for the entities above and each action in the acceptance criteria.
  - Rule: Clients can be added to a waitlist for a service/window.
  - Rule: Cancelling/no-showing a slot offers it to the waitlist.
  - Rule: Quiet-window fill suggestions surface from utilisation data.
  - Emit domain events for read-models / notifications / follow-up jobs where relevant.
  - Publish the OpenAPI contract so the generated clients update.
  - Depends on: PRD-02/REMINDERS.
- [ ] **Web UI**
  Build on the Angular web app: the schedule per the UI spec. Wire to the API with loading/empty/error states; capability-gate controls; responsive; show the blocked-action banner / gate chips where gated; respect owner-only .fin gating for money figures.
  Key elements (from the prototype):
  - Prototype: Schedule (schedule.png) — waitlist management + a backfill prompt on cancellation; quiet-window fill suggestions from utilisation.
