# Client app: book → intake → consent journey

> **Epic:** [PRD-09 — Apps (Flutter): client & provider](../epics/PRD-09.md)  ·  **Key:** `PRD-09/CLIENT-JOURNEY`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** client-app
>
> **Depends on:** `PRD-02/ONLINE-BOOK`, `PRD-03/CONSENT`

## Background

As a client, I want to book, complete intake and e-sign consent entirely in the app, so that I'm ready for my visit without paperwork.
A client can complete the full pre-visit journey entirely in-app (REQ-APP-1).

## How it works

The client completes the full pre-visit journey entirely in-app: sign in (social/email/OTP, tenant-scoped via Entra External ID) → book over PRD-02 → complete PRD-03 intake (medical history/BDD) → e-sign per-treatment consent incl. separate image-use consent, ending on 'All set'. The app is a surface over those modules; the treatment gate is enforced server-side.
Home surfaces the next appointment and an amber 'Finish your pre-visit forms' nudge; reminders/recall (PRD-07) arrive as push + in-app notifications. Removes paperwork and gets clients ready before they arrive.

## Requirements

- To book, complete intake and e-sign consent entirely in the app.

## Acceptance Criteria

- [ ] A client completes book → intake → consent (incl. image-use) fully in-app.
- [ ] Surfaces PRD-02 booking and PRD-03 intake/consent.
- [ ] Sign-in via social/email/OTP, tenant-scoped.
- [ ] Reminders/recall (PRD-07) are received in-app.

## UI designs / screenshots

_Prototype screen: client-app.html, treatment-room.html, checkin.html, backroom.html._

- Prototype: client-app — Home/'For you' (greeting, NEXT APPOINTMENT card with treatment/time/injector/room, 'View details', amber 'Finish your pre-visit forms' prompt).
- Quick actions: Book · Messages · Photos · Rewards. Bottom tabs: Home · Book · My care · Rewards · Account.
- Booking ends 'You're booked!'; intake + consent end 'All set — thank you'.

![client-app — prototype screen](../screens/client-app.png)

## Suggested data model

- **(reuses) Appointment** — PRD-02 via the API (book/reschedule endpoints)
  - _Client app is a surface; no app-local appointment store._
- **(reuses) IntakeResponse/ConsentSignature** — PRD-03 — medical history, per-treatment + image-use consent, e-signed
  - _Server holds records; signatures posted from device._
- **(reuses) Notification** — PRD-07 push token + in-app inbox
  - _Drives the pre-visit nudge._

## Technical notes (high level)

- Architecture decisions: [ADR-0004](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-09-apps-client-provider.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-09-apps-client-provider.md)

## Tasks (dev pickup)

- [ ] **Client app: sign-in + book→intake→consent journey**
  Client Flutter flavour: Entra External ID sign-in (social/email/OTP) writing a tenant-pinned session into secure storage. Home screen with the NEXT APPOINTMENT card and the 'Finish your pre-visit forms' nudge. Wire Book to the PRD-02 booking endpoints and the intake/consent screens to PRD-03 (medical history/BDD, per-treatment consent + separate image-use consent, on-device e-signature posted to the API). End-states 'You're booked!' / 'All set'. Register a push token and render reminders/recall (PRD-07) in an in-app inbox. No app-local clinical store; the treatment gate stays server-side.
