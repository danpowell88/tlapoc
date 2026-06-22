# Client app: in-app booking over PRD-02

> **Epic:** [PRD-09 — Apps (Flutter): client & provider](../epics/PRD-09.md)  ·  **Key:** `PRD-09/CLIENT-BOOK`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-09/CLIENT-JOURNEY`, `PRD-02/ONLINE-BOOK`

## Background

As a client, I want to book a visit myself in the app, so that I can get a slot without phoning the clinic.
Plainly: the Book tab of the client app where someone books a visit themselves — service, practitioner, day/time, confirm — getting the same availability the front desk sees. Where it fits: a follow-up to the client-app basic (PRD-09/CLIENT-JOURNEY) that adds in-app booking; it is a thin surface over the online-booking module (PRD-02/ONLINE-BOOK), so a self-booked appointment is identical to a desk booking. Injectable (S4 — Schedule 4 prescription-only medicine) services stay generic-named and unpriced online per the AU advertising rules.

## How it works

The Book tab walks the client through service → practitioner → day/time → review → 'You're booked!', surfacing the SAME scope-aware availability as the front desk so the app never offers a slot the desk wouldn't. Slots and the create call go through the PRD-02/ONLINE-BOOK endpoints; the resulting Appointment is identical to a desk booking (source=online).
Injectable (S4 — Schedule 4 prescription-only medicine) services are shown with generic names, no price and a 'pricing confirmed privately' note, and only offer cleared RN/NP practitioners (the canInject gate), honouring the AU advertising rules. Confirming the booking triggers the intake/consent send (PRD-03), which the client completes via CLIENT-INTAKE.

## Requirements

- To book a visit myself in the app.

## Acceptance Criteria

- [ ] The Book tab walks service → practitioner → day/time → review → 'You're booked!' and surfaces the same scope-aware availability as the desk.
- [ ] Injectable (S4) services show generic names, no price and 'pricing confirmed privately', and only offer cleared RN/NP practitioners.
- [ ] The created Appointment is identical to a desk booking (source=online) and triggers the intake/consent send.
- [ ] Slots and the create call go through the PRD-02/ONLINE-BOOK endpoints — no app-local booking logic.

## UI designs / screenshots

- Prototype: client-app — Book tab (service → practitioner → day/time → review), ending 'You're booked!'.
- Injectable services: generic name, no price, 'pricing confirmed privately', cleared RN/NP only.
- Booking confirmation triggers the intake/consent send.

![client-app — prototype screen](../screens/client-app.png)

## Suggested data model

- **(reuses) Appointment** — PRD-02 via the API (ONLINE-BOOK book/reschedule endpoints); source=online
  - _Extends CLIENT-JOURNEY; no app-local appointment store — identical to a desk booking._

## Other

- Source PRD: [PRD-09-apps-client-provider.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-09-apps-client-provider.md)

## Tasks (dev pickup)

- [ ] **In-app booking flow over PRD-02 (service → practitioner → slot → confirm)**
  Behaviour: the Book tab walks service → practitioner → day/time → review → 'You're booked!', surfacing the SAME scope-aware availability as the desk. Requirements: injectable (S4 — Schedule 4 prescription-only medicine) services show generic names, no price and 'pricing confirmed privately' and only offer cleared RN/NP; slots and the create call go through the PRD-02/ONLINE-BOOK endpoints; the resulting Appointment is identical to a desk booking (source=online) and triggers the intake/consent send.
