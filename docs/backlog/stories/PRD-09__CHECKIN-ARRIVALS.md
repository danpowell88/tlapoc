# Kiosk: reception arrivals board feed

> **Epic:** [PRD-09 — Apps (Flutter): client & provider](../epics/PRD-09.md)  ·  **Key:** `PRD-09/CHECKIN-ARRIVALS`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-09/CHECKIN-KIOSK`, `PRD-02/LIFECYCLE`

## Background

As a reception / treatment-room staff, I want an arrivals board that updates instantly when a client checks in, so that I can see who's here, where, and how long they've waited.
Plainly: the staff-facing arrivals board the kiosk feeds — who's here, where, and how long they've waited — updated the instant a client checks in. Where it fits: a follow-up to the kiosk basic (PRD-09/CHECKIN-KIOSK) that adds the staff companion board; the checked_in transition drives the PRD-02 visit lifecycle, updating the board and the provider's day list. Reception and the treatment room are notified instantly.

## How it works

Completing check-in shows the client 'You're checked in' + what happens next; the staff-facing 'Reception arrivals board' shows who's here, where, and how long they've waited. The checked_in transition drives the PRD-02 visit lifecycle, updating the arrivals board and the provider's day list instantly.
Reception and the treatment room are notified; the board is the staff companion the kiosk feeds. It reflects every check-in regardless of which kiosk step the client finished on.

## Requirements

- An arrivals board that updates instantly when a client checks in.

## Acceptance Criteria

- [ ] Completing check-in shows the client 'You're checked in' + what happens next.
- [ ] The staff-facing 'Reception arrivals board' shows who's here, where, and how long they've waited.
- [ ] The checked_in transition drives the PRD-02 visit lifecycle, updating the arrivals board and the provider's day list instantly.
- [ ] Reception and the treatment room are notified.

## UI designs / screenshots

- Prototype: checkin — 'You're checked in' + 'Reception arrivals board' (who's here, where, wait time).
- Updates instantly on checked_in; provider day list updates too; staff notified.

![client-app — prototype screen](../screens/client-app.png)

## Suggested data model

- **(reuses) Appointment.status → checked_in** — PRD-02 — drives the arrivals board / Today read-model
  - _Extends CHECKIN-KIOSK; the board is a read of the lifecycle, no parallel store._

## Other

- Source PRD: [PRD-09-apps-client-provider.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-09-apps-client-provider.md)

## Tasks (dev pickup)

- [ ] **Advance to checked_in + reception arrivals board feed**
  Behaviour: completing check-in advances the Appointment to checked_in and shows 'You're checked in' + what happens next; the staff-facing 'Reception arrivals board' shows who's here, where, and how long they've waited. Requirements: the transition drives the PRD-02 visit lifecycle, updating the arrivals board and the provider's day list instantly; reception and the treatment room are notified; the board is the staff companion the kiosk feeds.
