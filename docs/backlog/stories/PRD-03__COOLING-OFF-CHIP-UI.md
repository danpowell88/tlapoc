# Cooling-off: header chip & done-screen note

> **Epic:** [PRD-03 — Intake, consent & compliance gating](../epics/PRD-03.md)  ·  **Key:** `PRD-03/COOLING-OFF-CHIP-UI`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-03/COOLING-OFF`

## Background

As a staff member, I want the under-18 cooling-off state shown on the header and a client done-screen note, so that everyone sees when a minor's treatment is gated and why.
Plainly: surfacing the cooling-off state — an 'under-18 cooling-off' chip with the elapse date on the patient/charting header, a checkout-blocked indicator, the second-consult offer on the timeline, and a client done-screen note. Where it fits: a follow-up to the cooling-off basic under-18 7-day enforcement (PRD-03/COOLING-OFF) that adds the surfacing UI on top of the timer. It sits in Intake & Consent (PRD-03).

## How it works

The basic story enforces the timer; this follow-up surfaces its state to staff and clients. An 'under-18 cooling-off (the mandatory wait before a cosmetic procedure can proceed)' chip with the elapse date renders on the patient/charting header.
A checkout-blocked indicator (except the consult) is shown, and the recorded second-consultation offer appears on the client timeline.
The client done-screen note states 'If under 18, a mandatory 7-day cooling-off applies before any treatment', so a minor and their guardian understand the wait before they leave.

## Requirements

- The under-18 cooling-off state shown on the header and a client done-screen note.

## Acceptance Criteria

- [ ] An 'under-18 cooling-off' chip with the elapse date renders on the patient/charting header.
- [ ] A checkout-blocked indicator (except the consult) is shown.
- [ ] The second-consult offer appears on the client timeline.
- [ ] The client done-screen note states 'If under 18, a mandatory 7-day cooling-off applies before any treatment'.

## UI designs / screenshots

- Patient header shows an 'under-18 cooling-off' chip with the elapse date; a checkout-blocked indicator (except consult) (forms-consent.png).
- A recorded second-consultation offer on the client timeline.
- The client done-screen note: 'If under 18, a mandatory 7-day cooling-off applies before any treatment' (client-app.png).

![forms-consent — prototype screen](../screens/forms-consent.png)

## Suggested data model

- **(reads COOLING-OFF)** — no new entities; renders CoolingOffTimer.eligible_at + payment_blocked as a chip/indicator
  - _Presentation of the cooling-off state; the second-consult offer shows on the timeline._

## Other

- Source PRD: [PRD-03-intake-consent-gating.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-03-intake-consent-gating.md)

## Tasks (dev pickup)

- [ ] **Cooling-off header chip + done-screen note UI**
  Behaviour: surface the cooling-off state. Requirements: an 'under-18 cooling-off (the mandatory wait before a cosmetic procedure can proceed)' chip with the elapse date on the patient/charting header; a checkout-blocked indicator (except the consult); the second-consult offer on the client timeline; the client done-screen note 'If under 18, a mandatory 7-day cooling-off applies before any treatment'.
