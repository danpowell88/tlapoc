# Client app: shell, sign-in & home (basic)

> **Epic:** [PRD-09 — Apps (Flutter): client & provider](../epics/PRD-09.md)  ·  **Key:** `PRD-09/CLIENT-JOURNEY`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** client-app
>
> **Depends on:** `PRD-02/ONLINE-BOOK`, `PRD-03/CONSENT`

## Background

As a client, I want to sign in to the app and see my next appointment on a home screen, so that I have a working app that knows who I am and when I'm next in.
Plainly: this is the client's phone app at its most basic — sign in and land on a home screen that shows your next appointment. Where it fits: the client-facing Flutter apps come last in the build, after the staff web app and clinical core; this basic slice stands up the client flavour of the shared codebase and the home landing, and is the foundation the booking, intake/consent and push follow-ups build on. A client can sign in and see their next appointment in-app (REQ-APP-1).

## How it works

The client completes the full pre-visit journey entirely in-app: sign in (social/email/OTP (one-time passcode), tenant-scoped via Entra External ID) → book over PRD-02 → complete PRD-03 intake (medical history/BDD (body dysmorphic disorder screen)) → e-sign per-treatment consent incl. separate image-use consent, ending on 'All set'. The app is a surface over those modules; the treatment gate is enforced server-side.
Home surfaces the next appointment and an amber 'Finish your pre-visit forms' nudge; reminders/recall (PRD-07) arrive as push + in-app notifications. Removes paperwork and gets clients ready before they arrive.

## Requirements

- To sign in to the app and see my next appointment on a home screen.

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

- [ ] **Client Flutter flavour: shell, sign-in & tenant-pinned session**
  Behaviour: stand up the client flavour of the shared Flutter codebase — bottom tabs (Home / Book / My care / Rewards / Account), the design system and the API client. Sign-in via Entra External ID (social / email / OTP one-time passcode). Requirements: the chosen tenant is pinned into a session held in platform secure storage (Keychain / Keystore); every API call carries the tenant + token; sign-out clears it; no clinical data is stored app-local. This shell is shared with CLIENT-CARE / CLIENT-PRIVACY (same flavour, other tabs).
- [ ] **Home / 'For you' landing (next appointment)**
  Behaviour: the Home tab greets the client and shows a NEXT APPOINTMENT card (treatment, time, injector, room, 'View details'). Requirements: reads the client's next booking over PRD-02 via the API; nothing here is the source of truth — it reflects the booking read; the pre-visit nudge, quick-action routing and push inbox are added by the follow-ups (CLIENT-INTAKE, CLIENT-PUSH).
