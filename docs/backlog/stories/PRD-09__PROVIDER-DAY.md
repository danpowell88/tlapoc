# Provider app: day schedule & open patient

> **Epic:** [PRD-09 — Apps (Flutter): client & provider](../epics/PRD-09.md)  ·  **Key:** `PRD-09/PROVIDER-DAY`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** provider-app
>
> **Depends on:** `PRD-05/NOTE-TEMPLATE`

## Background

As a injector/prescriber, I want to see my day and open a patient with consult/consent status shown before I chart, so that I work room-side with the right context and gates.
The provider sees their day and opens a patient with consult+consent status verified before charting (REQ-APP-2).

## How it works

The provider app shows the practitioner's day ('Today · Room 2') and opens a patient with consult+consent status shown before charting. Provider signs in via Entra ID SSO, tenant-scoped; a self-checked-in client is highlighted as ready ('Start visit'). The consult+consent gate (PRD-03/04) is enforced server-side before charting opens — if unmet, the app shows what's outstanding and blocks charting.
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

- Prototype: treatment-room — 'Today · Room 2' day list (arrival times; self-checked-in client highlighted with 'Start visit', others 'Open').
- Open a patient → 'Consent & prescriber authorisation' status; quick links to map/photos/finalise. Bottom tabs: Schedule / Patient / Medicines / Tasks.

![treatment-room — prototype screen](../screens/treatment-room.png)

## Suggested data model

- **(reuses) Appointment** — PRD-02 — practitioner's day; checked-in status drives the highlight
  - _Provider app surface; Entra ID SSO._
- **(reuses) Consent/PrescriberAuthorisation gate** — PRD-03/04 — verified before charting opens
  - _Block + show outstanding if unmet._

## Technical notes (high level)

- Architecture decisions: [ADR-0004](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-09-apps-client-provider.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-09-apps-client-provider.md)

## Tasks (dev pickup)

- [ ] **Provider app: day schedule + open-patient consult/consent gate**
  Provider Flutter flavour with Entra ID workforce SSO (tenant-scoped). Build the 'Today · Room X' schedule from PRD-02 (arrival times, highlight a self-checked-in client with 'Start visit', others 'Open'). On opening a patient, render the 'Consent & prescriber authorisation' status block and evaluate the PRD-03/04 gate server-side: disable the charting entry points and show outstanding items until it passes; then expose quick links to injection map / photos / finalise. Bottom tabs Schedule / Patient / Medicines / Tasks.
