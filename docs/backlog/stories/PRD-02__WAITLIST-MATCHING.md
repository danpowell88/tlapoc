# Waitlist: matching / backfill engine on slot-freed

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/WAITLIST-MATCHING`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-02/WAITLIST`

## Background

As a front desk, I want a freed slot to be auto-offered to the best matching waiting client, so that cancellations and no-shows are filled without manual chasing.
Plainly: the engine that, when an appointment cancels or no-shows, automatically offers the freed slot to the best-matching waiting client. Where it fits: a follow-up to the waitlist basic entries & management (PRD-02/WAITLIST) that adds the demand-side matching on top of the entry list. It subscribes to the slot-freed event from reminders/lifecycle (PRD-02/REMINDERS, PRD-02/LIFECYCLE) and re-uses the same scope-aware availability engine so a backfilled booking still honours the rules. It sits in Reception (PRD-02).

## How it works

The basic story captures waiting clients; this follow-up adds the engine that matches them to freed slots. When a booking cancels or no-shows, the freed slot is automatically offered to the best matching waiting entry (priority + FIFO).
Matching subscribes to the slot-freed event (from PRD-02/REMINDERS and PRD-02/LIFECYCLE) and matches on service + desired window + scope/resource feasibility via the SAME availability engine the desk and online booking use — so a backfilled booking still honours scope and resource rules.
It creates an offer with an expires_at and dispatches it (PRD-07). The matching is idempotent and tenant-scoped so a single slot-freed event never produces duplicate offers.

## Requirements

- A freed slot to be auto-offered to the best matching waiting client.

## Acceptance Criteria

- [ ] When a booking cancels or no-shows, the freed slot is auto-offered to the best matching waiting entry.
- [ ] Matching subscribes to the slot-freed event and matches by service + window + scope/resource feasibility via the same availability engine.
- [ ] An offer is created with an expiry and dispatched (PRD-07).
- [ ] Matching is idempotent and tenant-scoped.

## UI designs / screenshots

- No new primary screen — the engine reacts to slot-freed events behind the scenes.
- A dispatched offer is delivered via PRD-07; the offer state appears on the waitlist management list.
- Matching respects the same scope/resource feasibility as the booking engine.

![schedule — prototype screen](../screens/schedule.png)

## Suggested data model

- **(extends WAITLIST)** — WaitlistEntry.status → offered; offered_at, expires_at set on match
  - _Subscribes to the slot-freed event (REMINDERS/LIFECYCLE); matches via the shared availability engine; idempotent._

## Other

- Source PRD: [PRD-02-booking-scheduling.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-02-booking-scheduling.md)

## Tasks (dev pickup)

- [ ] **Matching / backfill engine on slot-freed**
  Behaviour: when a booking cancels or no-shows the freed slot is auto-offered to the best matching waiting entry. Requirements: subscribe to the slot-freed event (from REMINDERS/LIFECYCLE); match by service + window + scope/resource feasibility via the SAME availability engine; create an offer with expires_at and dispatch it (PRD-07); idempotent and tenant-scoped.
