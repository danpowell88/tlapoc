# Automations: live stats (sent / booked / returned)

> **Epic:** [PRD-07 — Communications, reminders & recall](../epics/PRD-07.md)  ·  **Key:** `PRD-07/AUTOMATIONS-STATS`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-07/AUTOMATIONS`

## Background

As a owner, I want each automation to show how many messages it sent and how many converted, so that I can see which flows are working.
Plainly: show each automation's real performance — how many sent, and how many led to a booking or return — so the owner can see what's working. Where it fits: a follow-up to the automations core (PRD-07/AUTOMATIONS), which renders the cards/toggles; this adds the live stat line on each card. Stats read from NotificationLog (PRD-07/CHANNELS) joined to outcomes (bookings/returns) over a rolling window, computed server-side.

## How it works

Each automation card shows live stats — e.g. 'Recall 42 sent · 18 booked', 'Aftercare 96 sent (30d)', 'Win-back 128 sent · 11 returned', 'No-show 9 sent · 5 rebooked'. This extends the automations core (PRD-07/AUTOMATIONS) card UI.
Stats read from NotificationLog (PRD-07/CHANNELS) sends joined to outcomes (bookings/returns) over a rolling window; computed server-side, not hand-entered.

## Requirements

- Each automation to show how many messages it sent and how many converted.

## Acceptance Criteria

- [ ] Each automation card shows live stats — e.g. 'Recall 42 sent · 18 booked', 'Aftercare 96 sent (30d)', 'Win-back 128 sent · 11 returned', 'No-show 9 sent · 5 rebooked'.
- [ ] Stats read from NotificationLog (PRD-07/CHANNELS) joined to outcomes (bookings/returns) over a rolling window.
- [ ] Stats are computed server-side, not hand-entered.
- [ ] Loading/empty states are handled per card.

## UI designs / screenshots

- Prototype: Comms -> Automations — live stats on each card ('42 sent · 18 booked', etc.).

![marketing-inbox — prototype screen](../screens/marketing-inbox.png)

## Suggested data model

- **(read-model over NotificationLog + outcomes)** — per-automation sends joined to bookings/returns over a rolling window
  - _No new entity; computed server-side; reads PRD-07/CHANNELS NotificationLog._

## Other

- Source PRD: [PRD-07-comms-reminders-recall.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-07-comms-reminders-recall.md)

## Tasks (dev pickup)

- [ ] **Automation live stats (sent / booked / returned)**
  Behaviour: each automation card shows live stats (sent · booked/returned/rebooked over a rolling window). Requirements: read from NotificationLog (PRD-07/CHANNELS) joined to outcomes; computed server-side, not hand-entered; per-card loading/empty states.
