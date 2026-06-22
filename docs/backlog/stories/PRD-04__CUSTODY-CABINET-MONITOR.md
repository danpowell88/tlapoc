# Custody & storage: access-logged cabinet monitor (CM-01)

> **Epic:** [PRD-04 — Consult, prescribing & S4 medicines governance (the moat)](../epics/PRD-04.md)  ·  **Key:** `PRD-04/CUSTODY-CABINET-MONITOR`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-04/CUSTODY-STORAGE`

## Background

As a owner, I want the locked S4 cabinet to log every access event and raise a job on any anomaly, so that secure storage is evidenced by a logged, alarmed audit trail rather than trust.
Plainly: this turns the paper 'who had the keys' trust model for the locked S4 (Schedule 4 prescription-only medicine) cabinet into a logged, alarmed audit trail — a sensor on the cabinet reports every open, close and tamper, and the system raises a job when something looks wrong. Where it fits: a follow-up to PRD-04/CUSTODY-STORAGE that adds the access-logging half of secure storage (C15) on top of the custody binding. The optional ESP32 cabinet monitor (CM-01) POSTs door + tamper events; the server attributes opens to staff badge taps and raises facility jobs on anomalies, on the same job pathway the fridge monitor uses.

## How it works

Secure storage (C15) requires a locked cabinet/room with access restricted to authorised personnel and access events logged. This follow-up adds the logging half on top of the custody binding the basic provides: the optional ESP32 cabinet monitor (CM-01) turns the paper 'who had the keys' trust model into a logged, alarmed audit trail.
Access is logged: the AccessLog records open/close/tamper events per location with a monotonic sequence. The CM-01 cabinet monitor POSTs signed door + tamper events to a per-clinic+cabinet endpoint; the server attributes an open to a staff badge tap and raises a facility job on an unattributed open, after-hours open, door-left-ajar, tamper, seq-gap or missed heartbeat (the same job pathway the fridge monitor uses). Silence is itself an alarm.
The server decides policy from raw signals — the device reports raw door/tamper events, the server owns the rules — so the same logic applies whether the signal comes from the DIY ESP32 or a future commercial cabinet sensor.

## Requirements

- The locked S4 cabinet to log every access event and raise a job on any anomaly.

## Acceptance Criteria

- [ ] An AccessLog records open/close/tamper events per secure location, with a monotonic sequence so gaps/resets are detectable.
- [ ] The CM-01 cabinet monitor POSTs signed door + tamper events to a per-clinic+cabinet endpoint (bearer token + HMAC signature, idempotency-keyed).
- [ ] The server attributes an open to a staff badge tap and raises a facility job on an unattributed open, after-hours open, door-left-ajar, tamper, sequence gap or missed heartbeat.
- [ ] Every access event is written to the AccessLog and audited (C15).

## UI designs / screenshots

- Prototype screen: the CM-01 cabinet monitor + Stock & medicines header (stock.png).
- Cabinet access (CM-01): an access log of who/when/duration per cabinet, with facility jobs for unattributed/after-hours/ajar/tamper opens — the 'restrict + log access' half of C15/REQ-MED-8.
- An unattributed or after-hours open surfaces a 'Raise job' action on the facility worklist.

![stock — prototype screen](../screens/stock.png)

## Suggested data model

- **AccessLog** — id, tenant_id, location_id, actor_id?, badge_id?, at, event(open|close|tamper_motion|tamper_mask|tamper_lid|sensor_disagreement|heartbeat), attributed(bool), seq
  - _New append-only entity (extends the basic's StockLocation, which already carries cabinet_monitor_id). Feeds the CM-01 cabinet sensor + audit (C15). Server decides policy (unattributed/after-hours/ajar/tamper -> facility job); monotonic seq detects gaps/resets._

## Other

- Source PRD: [PRD-04-consult-prescribing-s4.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-04-consult-prescribing-s4.md)

## Tasks (dev pickup)

- [ ] **AccessLog model (append-only, monotonic seq)**
  Add AccessLog: id, tenant_id, location_id, actor_id/badge_id (nullable), at, event(open|close|tamper_*|sensor_disagreement|heartbeat), attributed(bool), seq(monotonic); RLS by tenant; append-only. Binds to the StockLocation.cabinet_monitor_id the basic reserves.
- [ ] **Cabinet-monitor ingest + access-log policy + audit**
  Endpoint POST /clinics/{slug}/cabinets/{id}/events: verify the per-cabinet bearer token + HMAC X-Signature, dedupe on Idempotency-Key, check monotonic seq (gap/reset = tamper). Server decides policy from raw signals: raise a facility job on unattributed open (no recent badge tap), after-hours, door-left-ajar (no close), any tamper_*/sensor_disagreement, missed heartbeat (>2 intervals) or seq gap. Write every access event to AccessLog + audit (C15).
