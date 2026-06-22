# Client app: book → intake → consent journey

> **Epic:** [PRD-09 — Apps (Flutter): client & provider](../epics/PRD-09.md)  ·  **Key:** `PRD-09/CLIENT-JOURNEY`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** client-app
>
> **Depends on:** `PRD-02/ONLINE-BOOK`, `PRD-03/CONSENT`

## Background

As a client, I want to book, complete intake and e-sign consent entirely in the app, so that I'm ready for my visit without paperwork.
Plainly: this is the client's phone app for getting ready before a visit — sign in, book, fill in the medical-history form and sign consent, all in one place. Where it fits: the client-facing Flutter apps come last in the build, after the staff web app and clinical core, reusing the booking (PRD-02) and intake/consent (PRD-03) modules already built. A client can complete the full pre-visit journey entirely in-app (REQ-APP-1).

## How it works

The client completes the full pre-visit journey entirely in-app: sign in (social/email/OTP (one-time passcode), tenant-scoped via Entra External ID) → book over PRD-02 → complete PRD-03 intake (medical history/BDD (body dysmorphic disorder screen)) → e-sign per-treatment consent incl. separate image-use consent, ending on 'All set'. The app is a surface over those modules; the treatment gate is enforced server-side.
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

- [ ] **Client Flutter flavour: shell, sign-in & tenant-pinned session**
  Behaviour: stand up the client flavour of the shared Flutter codebase — bottom tabs (Home / Book / My care / Rewards / Account), the design system and the API client. Sign-in via Entra External ID (social / email / OTP one-time passcode). Requirements: the chosen tenant is pinned into a session held in platform secure storage (Keychain / Keystore); every API call carries the tenant + token; sign-out clears it; no clinical data is stored app-local. This shell is shared with CLIENT-CARE / CLIENT-PRIVACY (same flavour, other tabs).
- [ ] **Home / 'For you' landing (next appointment + pre-visit nudge)**
  Behaviour: the Home tab greets the client and shows a NEXT APPOINTMENT card (treatment, time, injector, room, 'View details') plus an amber 'Finish your pre-visit forms' nudge when intake/consent is outstanding. Requirements: the nudge is driven by the server-side gate state (PRD-03) and deep-links into the forms; quick actions (Book / Messages / Photos / Rewards) route to the relevant screens; nothing here is the source of truth — it reflects the booking + gate read.
- [ ] **In-app booking flow over PRD-02 (service → practitioner → slot → confirm)**
  Behaviour: the Book tab walks service → practitioner → day/time → review → 'You're booked!', surfacing the SAME scope-aware availability as the desk. Requirements: injectable (S4 — Schedule 4 prescription-only medicine) services show generic names, no price and 'pricing confirmed privately' and only offer cleared RN/NP; slots and the create call go through the PRD-02/ONLINE-BOOK endpoints; the resulting Appointment is identical to a desk booking (source=online) and triggers the intake/consent send.
- [ ] **Intake + per-treatment consent + image-use consent (PRD-03), e-signed on device**
  Behaviour: the pre-visit forms screen completes the PRD-03 medical-history / BDD (body dysmorphic disorder) intake and e-signs per-treatment consent plus a SEPARATE, withdrawable image-use consent, ending on 'All set'. Requirements: the on-device signature is captured and posted to the API (records live server-side, no parallel app store); the treatment gate stays server-enforced — the app only reflects outstanding items; image-use consent is its own toggle the client can later withdraw.
- [ ] **Push token registration + in-app notification inbox (PRD-07)**
  Behaviour: register a push token at sign-in and render reminders / recall as push plus an in-app inbox. Requirements: notifications are delivered by PRD-07 (this surface only receives and displays them); transactional care/appointment messages are always shown; the inbox drives the Home pre-visit nudge; tapping a notification deep-links to the relevant screen.
