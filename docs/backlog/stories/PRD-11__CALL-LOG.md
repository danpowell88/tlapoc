# Call / phone log

> **Epic:** [PRD-11 — Facility, infection-control, emergency & complaints](../epics/PRD-11.md)  ·  **Key:** `PRD-11/CALL-LOG`  ·  **Type:** Story  ·  **Stage:** M6  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web
>
> **Depends on:** `PRD-07/FOLLOWUPS`

## Background

As a front desk, I want to log phone calls against a client and raise a follow-up if needed, so that phone interactions aren't lost and callbacks happen.
Plainly: log inbound/outbound phone calls against a client and raise a callback when needed, so phone interactions are not lost. Where it fits: part of the operational backbone (Facility/Ops) around the clinical core; calls route into the shared follow-up queue (PRD-07). The prototype's Operations → Call log records inbound/outbound phone interactions against clients and raises follow-ups (the phone is still a primary clinic channel).

## How it works

Log inbound/outbound phone calls against a client (direction, number, summary, outcome) and raise a follow-up job if needed; calls appear in the client's comms history and a missed-call/callback can be tracked to resolution ('Log callback'). Missed calls auto-text-back and become callback jobs; walk-ins and waitlist offers route through the same follow-up queue. Tenant-scoped and audited.
Captures phone interactions so nothing is lost (the phone is still a primary clinic channel).

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

- Prototype: Operations → Call log (ops-phone) — Time · Number · Who · Note (missed → text-back sent; 'Asked to move Fri appt'); 'Log callback'; Walk-in / Offer from waitlist route through the same queue.
- Log a call against a client; raise a follow-up; appears in comms history.

![ops-phone — prototype screen](../screens/ops-phone.png)

## Suggested data model

- **CallLog** — id, tenant_id, client_id?, direction(in|out), number, summary, outcome, at, actor_id
  - _Can raise a Job (PRD-07); appears in comms history; audited._

## Other

- Source PRD: [PRD-11-facility-complaints.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-11-facility-complaints.md)

## Tasks (dev pickup)

- [ ] **CallLog entity + log a call**
  Model CallLog (tenant_id, client_id?, direction[in|out], number, summary, outcome, at, actor_id) under RLS (row-level security, the database-level tenant isolation), audited. Call log UI (Time · Number · Who · Note) to log inbound/outbound calls against a client.
- [ ] **Call → follow-up job + comms history**
  A call can raise a follow-up Job (PRD-07); a linked call appears in the client's comms history. Missed calls auto-text-back and become callback jobs; track a missed-call/callback to resolution ('Log callback').
- [ ] **Shared follow-up queue (walk-ins / waitlist offers)**
  Route walk-ins and waitlist offers through the same follow-up queue as call callbacks, so the front desk works one queue.
