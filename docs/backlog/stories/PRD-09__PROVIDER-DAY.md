# Provider app: day schedule & open patient

> **Epic:** [PRD-09 — Apps (Flutter): client & provider](../epics/PRD-09.md)  ·  **Key:** `PRD-09/PROVIDER-DAY`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** provider-app
>
> **Depends on:** `PRD-05/NOTE-TEMPLATE`

## Background

As a injector/prescriber, I want to see my day and open a patient with consult/consent status shown before I chart, so that I work room-side with the right context and gates.
Plainly: the practitioner's app showing their day's patients, with each patient's consult and consent status checked before charting starts. Where it fits: a late, room-side surface on the shared Flutter codebase that reuses the charting (PRD-05) and gating (PRD-03/04) modules built earlier; the apps come last because they face outward. The provider sees their day and opens a patient with consult+consent status verified before charting (REQ-APP-2).

## How it works

The provider app shows the practitioner's day ('Today · Room 2') and opens a patient with consult+consent status shown before charting. Provider signs in via Entra ID SSO (single sign-on), tenant-scoped; a self-checked-in client is highlighted as ready ('Start visit'). The consult+consent gate (PRD-03/04) is enforced server-side before charting opens — if unmet, the app shows what's outstanding and blocks charting.
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

- [ ] **Provider Flutter flavour: shell + Entra workforce SSO**
  Behaviour: stand up the provider flavour of the shared Flutter codebase with bottom tabs Schedule / Patient / Medicines / Tasks, sharing auth, the API client and the design system. Sign-in via Entra ID workforce SSO (single sign-on), tenant-scoped. Requirements: the session is pinned to the tenant and carried on every call; thumb-first, gloves-on usability (UX §1); this is the same flavour the room-side charting (PROVIDER-ROOMSIDE) and offline (PROVIDER-OFFLINE) stories extend.
- [ ] **'Today · Room X' day schedule with ready-to-start highlight**
  Behaviour: build the practitioner's day list from PRD-02 (arrival times), highlighting a self-checked-in client as ready with 'Start visit' and others as 'Open'. Requirements: reflects the live visit lifecycle (checked_in drives the highlight); reads the practitioner's own day; opening a row goes to the patient with the gate evaluated.
- [ ] **Open-patient consult/consent gate (server-enforced before charting)**
  Behaviour: on opening a patient, render the 'Consent & prescriber authorisation' status block and evaluate the PRD-03/04 gate. Requirements: the gate is evaluated server-side — the charting entry points stay disabled and outstanding items are shown until consult + consent pass; once cleared, expose quick links to injection map / photos / finalise (handing off to PROVIDER-ROOMSIDE); the app never bypasses the gate locally.
