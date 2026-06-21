# Call / phone log

> **Epic:** [PRD-11 — Facility, infection-control, emergency & complaints](../epics/PRD-11.md)  ·  **Key:** `PRD-11/CALL-LOG`  ·  **Type:** Story  ·  **Stage:** M6  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web
>
> **Depends on:** `PRD-07/FOLLOWUPS`

## Background

As a front desk, I want to log phone calls against a client and raise a follow-up if needed, so that phone interactions aren't lost and callbacks happen.
The prototype's Operations → Call log records inbound/outbound phone interactions against clients and raises follow-ups (the phone is still a primary clinic channel).

## How it works

Log inbound/outbound phone calls against a client (direction, summary, outcome) and raise a follow-up job if needed; calls appear in the client's comms history and a missed-call/callback can be tracked to resolution. The phone is still a primary clinic channel.
Captures phone interactions so nothing is lost.

## Requirements

- To log phone calls against a client and raise a follow-up if needed.
- Compliance: [C10](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Calls can be logged (direction, client link, summary, outcome).
- [ ] A call can raise a follow-up job (PRD-07) and appears in the client's comms history.
- [ ] Logs are tenant-scoped and audited.
- [ ] A missed-call/callback can be tracked to resolution.

## UI designs / screenshots

_Prototype screen: prototype.html — Front desk/Operations (Open/close & fridge log, Temperature monitors, Rooms & devices, Equipment, Call log); backroom.html._

- Prototype: Operations -> Call log (ops-phone.png) — log a call against a client; raise a follow-up; appears in comms history.

![ops-phone — prototype screen](../screens/ops-phone.png)

## Suggested data model

- **CallLog** — id, tenant_id, client_id, direction(in|out), summary, outcome, at, actor_id
  - _Can raise a Job (PRD-07); in comms history._

## Technical notes (high level)

- Stack: Angular web (admin/front-desk/public)

## Other

- Source PRD: [PRD-11-facility-complaints.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-11-facility-complaints.md)

## Tasks (dev pickup)

- [ ] **Web UI** — prototype.html — Front desk/Operations (Open/close & fridge log, Temperature monitors, Rooms & devices, Equipment, Call log); backroom.html.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
