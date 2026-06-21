# Provider app: day schedule & open patient

> **Epic:** [PRD-09 — Apps (Flutter): client & provider](../epics/PRD-09.md)  ·  **Key:** `PRD-09/PROVIDER-DAY`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** provider-app
>
> **Depends on:** `PRD-05/NOTE-TEMPLATE`

## Background

As a injector/prescriber, I want to see my day and open a patient with consult/consent status shown before I chart, so that I work room-side with the right context and gates.
The provider sees their day and opens a patient with consult+consent status verified before charting (REQ-APP-2).

## How it works

The provider app shows the practitioner's day and opens a patient with consult+consent status shown before charting — the consult+consent gate (PRD-03/04) is enforced before charting opens. Provider signs in via Entra SSO, tenant-scoped.
Room-side starting point with the right context and gates.

## Requirements

- To see my day and open a patient with consult/consent status shown before I chart.

## Acceptance Criteria

- [ ] Schedule shows the practitioner's day; opening a patient shows consult+consent status.
- [ ] Provider signs in via Entra SSO, tenant-scoped.
- [ ] The consult+consent gate (PRD-03/04) is enforced before charting opens.
- [ ] Quick links to map/photos/finalise.

## UI designs / screenshots

_Prototype screen: client-app.html, treatment-room.html, checkin.html, backroom.html._

- Prototype: provider app (treatment-room.png) — 'Today · Room 2' schedule; open a patient -> 'Consent & prescriber authorisation' status; quick links to map/photos/finalise.
- Bottom tabs: Schedule / Patient / Medicines / Tasks.

![treatment-room — prototype screen](../screens/treatment-room.png)

## Suggested data model

- **(reuses)** — Appointment (PRD-02) + gate (PRD-03/04)
  - _Provider app surface; Entra SSO._

## Technical notes (high level)

- Stack: Flutter provider app
- Architecture decisions: [ADR-0004](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-09-apps-client-provider.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-09-apps-client-provider.md)

## Tasks (dev pickup)

- [ ] **Provider app UI (Flutter)**
