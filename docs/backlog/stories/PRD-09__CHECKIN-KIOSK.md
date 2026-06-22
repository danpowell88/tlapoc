# Reception self-check-in surface (basic)

> **Epic:** [PRD-09 — Apps (Flutter): client & provider](../epics/PRD-09.md)  ·  **Key:** `PRD-09/CHECKIN-KIOSK`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web
>
> **Depends on:** `PRD-02/LIFECYCLE`

## Background

As a client arriving for a visit, I want to find my booking and confirm it on the reception tablet, so that the team knows I've arrived.
Plainly: the locked-down reception tablet at its core — an arriving client finds their booking and confirms it's them, then is marked arrived. Where it fits: a late, client-facing surface that reuses the booking-lifecycle (PRD-02) module; one of the kiosk (the in-clinic self-service check-in surface)/back-office surfaces that come last. This basic slice is the kiosk shell + lookup/confirm; the details/health-check step, the intake/consent step and the arrivals-board feed are its follow-ups.

## How it works

A locked-down reception-tablet surface where clients self-check-in: from an idle 'Welcome in' attract screen, find their booking (by mobile number, no app or password) and confirm it's them, advancing the appointment to checked_in (PRD-02 lifecycle). Steps in this basic: Find booking · Confirm appointment · Checked in.
Single-client session with no access to other clients' data, auto-timing-out to the attract screen between clients (C10). The details + health-check step, outstanding intake/consent completion, and the staff arrivals-board feed are added by the follow-ups (CHECKIN-DETAILS, CHECKIN-FORMS, CHECKIN-ARRIVALS). Speeds arrivals.

## Requirements

- To find my booking and confirm it on the reception tablet.
- Compliance: [C10](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] A client can self-check-in by finding their booking and confirming it's them on a shared tablet surface.
- [ ] The surface is locked-down (no access to other clients' data) and times out to the attract screen between clients (C10).
- [ ] Confirming advances the Appointment to checked_in (PRD-02 lifecycle).
- [ ] Lookup returns only the matching client's own booking; the public lookup is rate-limited/guarded.

## UI designs / screenshots

_Prototype screen: checkin.html._

- Prototype: checkin — idle 'Welcome in' attract screen ('Tap to check in'); steps Find booking · Confirm appointment · Checked in.
- Returns to a neutral state between clients (auto-timeout); single-client session, no other clients' data.

![checkin — prototype screen](../screens/checkin.png)

## Suggested data model

- **(reuses) Appointment.status → checked_in** — PRD-02 — advances lifecycle
  - _Kiosk session is single-client + auto-timeout; no parallel store._

## Other

- Source PRD: [PRD-09-apps-client-provider.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-09-apps-client-provider.md)

## Tasks (dev pickup)

- [ ] **Locked-down kiosk shell + attract screen + session timeout**
  Behaviour: a locked-down web/PWA (progressive web app) kiosk surface that idles on a 'Welcome in' attract screen ('Tap to check in') and steps through Find booking · Confirm · Checked in. Requirements: a single-client session with NO access to other clients' data and no staff login; auto-timeout back to the attract screen between clients, clearing all state (C10); the device is kiosk-pinned (no browser chrome / navigation away).
- [ ] **Booking lookup + confirm-it's-me (no password) → checked_in**
  Behaviour: 'Find your booking' matches the visit by mobile number (no app or password), then 'Confirm appointment' shows the found booking and the client confirms it's them, advancing the Appointment to checked_in. Requirements: lookup returns only the matching client's own booking; a light verification (not a staff login); reception can also look it up; rate-limit/guard the public lookup.
