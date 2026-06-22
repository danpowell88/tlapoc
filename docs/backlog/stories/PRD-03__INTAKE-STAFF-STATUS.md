# Pre-visit intake: staff status + send/chase

> **Epic:** [PRD-03 — Intake, consent & compliance gating](../epics/PRD-03.md)  ·  **Key:** `PRD-03/INTAKE-STAFF-STATUS`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-03/INTAKE`

## Background

As a front desk, I want to see each client's intake status and send or chase the intake link, so that intake is complete before the visit and nothing is missed.
Plainly: the staff Forms & consent surface that shows per-client intake status and lets the desk send or chase an intake link. Where it fits: a follow-up to the pre-visit intake basic capture (PRD-03/INTAKE) that adds the staff-facing status/chase surface on top of the basic submission. Send/chase goes via Comms (PRD-07); status reflects whether a required, current IntakeResponse exists. It sits in Intake & Consent (PRD-03).

## How it works

The basic story lets a client submit intake; this follow-up gives the desk visibility and control. The staff Forms & consent screen shows recent submissions with per-client intake status (complete / pending — link sent).
The desk can send or chase an intake link, with the send going via Comms (PRD-07). The status reflects whether a required, current IntakeResponse exists for the client/appointment.
Rows deep-link to the client so the desk can act in one step, keeping intake complete before the visit.

## Requirements

- To see each client's intake status and send or chase the intake link.

## Acceptance Criteria

- [ ] The staff Forms & consent screen shows recent submissions with per-client intake status (complete / pending — link sent).
- [ ] Actions to send or chase an intake link, going via PRD-07.
- [ ] Status reflects whether a required, current IntakeResponse exists.
- [ ] Rows deep-link to the client.

## UI designs / screenshots

- Prototype: Forms & consent (forms-consent.png) — recent submissions with per-client intake status (e.g. 'Jess Tan · Medical history · pending — link sent') and a send/chase action.
- Status reflects whether a required, current IntakeResponse exists; send/chase via PRD-07.
- Rows deep-link to the client.

![forms-consent — prototype screen](../screens/forms-consent.png)

## Suggested data model

- **(reads INTAKE)** — no new entities; reads IntakeResponse presence/status per client/appointment
  - _Status = whether a required, current IntakeResponse exists; send/chase via PRD-07._

## Other

- Source PRD: [PRD-03-intake-consent-gating.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-03-intake-consent-gating.md)

## Tasks (dev pickup)

- [ ] **Staff Forms & consent: intake status + send/chase**
  Behaviour: the staff Forms & consent screen showing recent submissions with per-client intake status (complete / pending — link sent) and actions to send or chase an intake link. Requirements: send/chase goes via PRD-07; status reflects whether a required, current IntakeResponse exists; rows deep-link to the client.
