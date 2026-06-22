# Kiosk: details review + today's health check

> **Epic:** [PRD-09 — Apps (Flutter): client & provider](../epics/PRD-09.md)  ·  **Key:** `PRD-09/CHECKIN-DETAILS`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-09/CHECKIN-KIOSK`, `PRD-03/GATING`

## Background

As a client arriving for a visit, I want to review my details and answer a quick health check at the kiosk, so that my records are current and the clinician knows what's changed.
Plainly: the step after confirming at the kiosk where the client does a quick contact-details review and answers a safety 'anything changed?' health check before the chair. Where it fits: a follow-up to the kiosk basic (PRD-09/CHECKIN-KIOSK) that adds the details/health-check step; it writes back to the client record (PRD-02) and intake (PRD-03), feeding the clinician a per-visit re-screen. No clinical record is exposed at the kiosk.

## How it works

After confirming, 'Check your details' is a 10-second contact-details review to keep records current, then 'Today's health check' asks the safety 'anything changed?' question captured before the chair. Both write back to the PRD-02 client record / PRD-03 intake.
The health-check response is the per-visit re-screen feeding the clinician; no clinical record is exposed at the kiosk. This step slots between confirm-it's-me and the outstanding-forms step (CHECKIN-FORMS).

## Requirements

- To review my details and answer a quick health check at the kiosk.

## Acceptance Criteria

- [ ] 'Check your details' is a 10-second contact-details review that keeps records current (writes back to the PRD-02 client record).
- [ ] 'Today's health check' asks the safety 'anything changed?' question and the response is captured as the per-visit re-screen (PRD-03 intake).
- [ ] The health-check response feeds the clinician before the chair.
- [ ] No clinical record is exposed at the kiosk.

## UI designs / screenshots

- Prototype: checkin — steps Check details · Health check (between Confirm appointment and Checked in).
- 10-second details review; 'anything changed?' safety re-screen; no clinical record shown.

![client-app — prototype screen](../screens/client-app.png)

## Suggested data model

- **(reuses) Client/IntakeResponse** — PRD-02 contact details + PRD-03 per-visit health-check re-screen
  - _Extends CHECKIN-KIOSK; writes back to the owning modules, no parallel store._

## Other

- Source PRD: [PRD-09-apps-client-provider.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-09-apps-client-provider.md)

## Tasks (dev pickup)

- [ ] **Details review + today's health check ('anything changed?')**
  Behaviour: 'Check your details' is a 10-second contact-details review to keep records current, then 'Today's health check' asks the safety 'anything changed?' question captured before the chair. Requirements: writes back to the PRD-02 client record / PRD-03 intake; the health-check response is the per-visit re-screen feeding the clinician; no clinical record is exposed at the kiosk.
