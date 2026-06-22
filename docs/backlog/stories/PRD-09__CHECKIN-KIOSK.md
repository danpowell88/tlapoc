# Reception self-check-in surface (tablet)

> **Epic:** [PRD-09 — Apps (Flutter): client & provider](../epics/PRD-09.md)  ·  **Key:** `PRD-09/CHECKIN-KIOSK`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web
>
> **Depends on:** `PRD-02/LIFECYCLE`, `PRD-03/GATING`

## Background

As a client arriving for a visit, I want to check myself in on the reception tablet, so that the team knows I've arrived and I complete anything outstanding.
Plainly: the locked-down reception tablet where an arriving client checks themselves in, confirms details and finishes outstanding forms or consent. Where it fits: a late, client-facing surface that reuses the booking-lifecycle (PRD-02) and gating (PRD-03) modules; one of the kiosk (the in-clinic self-service check-in surface)/back-office surfaces that come last. The prototype's checkin surface is a reception-desk tablet where clients check themselves in (confirm details, complete any outstanding intake/consent), updating the Today board.

## How it works

A locked-down reception-tablet surface where clients self-check-in: from an idle 'Welcome in' attract screen, find their booking, confirm details, and complete any outstanding intake (medical history/health check) or consent (PRD-03). Check-in moves the appointment to checked_in (PRD-02 lifecycle), updating the reception arrivals board and the provider's day list. Steps: Find booking · Confirm appointment · Check details · Health check · Sign consent · Checked in.
Single-client session with no access to other clients' data, auto-timing-out to the attract screen between clients (C10). Re-uses the same modules as the client app. Speeds arrivals and captures missing pre-visit items.

## Requirements

- To check myself in on the reception tablet.
- Compliance: [C10](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] A client can self-check-in (verify identity/appointment) on a shared tablet surface.
- [ ] Outstanding intake/consent is prompted and completable at check-in.
- [ ] Check-in updates the visit lifecycle/Today board (PRD-02).
- [ ] The surface is locked-down (no access to other clients' data) and times out between clients.

## UI designs / screenshots

_Prototype screen: checkin.html._

- Prototype: checkin — idle 'Welcome in' attract screen ('Tap to check in'); steps Find booking · Confirm appointment · Check details · Health check · Sign consent · Checked in; 'Reception arrivals board'.
- Returns to a neutral state between clients (auto-timeout).

![checkin — prototype screen](../screens/checkin.png)

## Suggested data model

- **(reuses) Appointment.status → checked_in** — PRD-02 — advances lifecycle, updates arrivals board / Today
  - _Kiosk session is single-client + auto-timeout._
- **(reuses) IntakeResponse/ConsentSignature** — PRD-03 — outstanding intake/consent completed at the desk
  - _Same modules as the client app; no parallel store._

## Other

- Source PRD: [PRD-09-apps-client-provider.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-09-apps-client-provider.md)

## Tasks (dev pickup)

- [ ] **Reception self-check-in tablet surface**
  Locked-down web/PWA (progressive web app) kiosk surface re-using the PRD-02/03 modules. Idle 'Welcome in' attract screen → 'Tap to check in' → booking lookup + light detail confirmation (not a staff login) → prompt/complete outstanding intake (medical history/health check) and consent (PRD-03) → advance Appointment to checked_in (PRD-02), updating the arrivals board and the provider day list. Single-client session with no cross-client data access; auto-timeout back to the attract screen between clients (C10).
