# Client app: book → intake → consent journey

> **Epic:** [PRD-09 — Apps (Flutter): client & provider](../epics/PRD-09.md)  ·  **Key:** `PRD-09/CLIENT-JOURNEY`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** client-app
>
> **Depends on:** `PRD-02/ONLINE-BOOK`, `PRD-03/CONSENT`

## Background

As a client, I want to book, complete intake and e-sign consent entirely in the app, so that I'm ready for my visit without paperwork.
A client can complete the full pre-visit journey entirely in-app (REQ-APP-1).

## How it works

The client completes the full pre-visit journey entirely in-app: book -> intake -> e-sign consent (incl. image-use), then receives reminders/recall. Surfaces PRD-02 booking and PRD-03 intake/consent through the Flutter client app; sign-in via social/email/OTP, tenant-scoped.
Removes paperwork and gets clients ready before they arrive.

## Requirements

- To book, complete intake and e-sign consent entirely in the app.

## Acceptance Criteria

- [ ] A client completes book → intake → consent (incl. image-use) fully in-app.
- [ ] Surfaces PRD-02 booking and PRD-03 intake/consent.
- [ ] Sign-in via social/email/OTP, tenant-scoped.
- [ ] Reminders/recall (PRD-07) are received in-app.

## UI designs / screenshots

_Prototype screen: client-app.html, treatment-room.html, checkin.html, backroom.html._

- Prototype: client app (client-app.png) bottom-tabs — Home/For you, Book, then the intake + consent flow ('You're booked!', 'All set — thank you').
- Reminders/recall received in-app.

![client-app — prototype screen](../screens/client-app.png)

## Suggested data model

- **(reuses)** — Appointment (PRD-02) + IntakeResponse/ConsentSignature (PRD-03) via the API
  - _Client app is a surface over those modules._

## Technical notes (high level)

- Stack: Flutter client app
- Architecture decisions: [ADR-0004](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-09-apps-client-provider.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-09-apps-client-provider.md)

## Tasks (dev pickup)

- [ ] **Client app UI (Flutter)**
