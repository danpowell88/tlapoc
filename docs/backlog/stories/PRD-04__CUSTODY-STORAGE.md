# Custody & secure storage

> **Epic:** [PRD-04 — Consult, prescribing & S4 medicines governance (the moat)](../epics/PRD-04.md)  ·  **Key:** `PRD-04/CUSTODY-STORAGE`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-04/STOCK-RECEIVE`

## Background

As a owner, I want stock custody limited to an on-site prescriber and bound to a secure, access-logged location, so that S4 custody meets the exclusive-custody rule.
Only NP/prescriber roles may take custody; stock is bound to a secure, access-logged location. Mode-A custodian must physically work at the clinic with exclusive custody (C7/C15).

## How it works

QLD's exclusive-custody rule (GAP-3, C7) is sharp: a Mode-A custodian must be a prescriber who physically works at the clinic and holds EXCLUSIVE custody and control of the S4 stock. A remote prescriber consigning stock to a nurse-held clinic is non-compliant - this breaks the legacy 'remote telehealth doctor + nurse-held stock' model. RNs may only POSSESS S4 to administer it.
Secure storage (C15) requires a locked cabinet/room with access restricted to authorised personnel and access events logged. The optional ESP32 cabinet monitor (CM-01) turns the paper 'who had the keys' trust model into a logged, alarmed audit trail.
Stock is bound to a StockLocation (e.g. 'locked fridge') with a named custodian. Only NP/prescriber roles can take custody; a custody change is capability-gated and audited. The location carries an exclusive-custody attestation and a designated medicine-store/management contact (GAP-3).
A remote prescriber recorded as consigning stock to a clinic where they lack exclusive custody is flagged non-compliant - the system surfaces it rather than silently allowing it.
Access is logged: the AccessLog records open/close/tamper events per location. The CM-01 cabinet monitor POSTs signed door + tamper events to a per-clinic+cabinet endpoint; the server attributes an open to a staff badge tap and raises a facility job on an unattributed open, after-hours open, door-left-ajar, tamper, seq-gap or missed heartbeat (the same job pathway the fridge monitor uses). Silence is itself an alarm.
The header surface ('custody Dr Lee NP - locked fridge') and the per-lot custody field make the custodian + secure-location binding visible everywhere stock is shown.

## Requirements

- Stock custody limited to an on-site prescriber and bound to a secure, access-logged location.
- Compliance: [C7](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria), [C15](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Only NP/prescriber roles can take custody of stock.
- [ ] Stock is bound to a secure location; access is logged.
- [ ] A custodian + exclusive-custody attestation + designated medicine-store contact are recorded.
- [ ] A remote prescriber consigning stock is flagged non-compliant.

## UI designs / screenshots

- Prototype screens: Stock & medicines header (stock.png) + the CM-01 cabinet monitor.
- The Medicines & stock header reads 'On-site stock - custody Dr Lee NP - locked fridge' - the custodian + secure-location binding is visible at a glance.
- Lot detail shows 'Custody: Dr Lee NP' and 'Storage: Fridge 1 - 4.2C' per lot.
- Cabinet access (CM-01): an access log of who/when/duration per cabinet, with facility jobs for unattributed/after-hours/ajar/tamper opens - the 'restrict + log access' half of C15/REQ-MED-8.
- Custody change is capability-gated to prescriber/owner and audited.

![stock — prototype screen](../screens/stock.png)

## Suggested data model

- **StockLocation** — id, tenant_id, name(locked cabinet/fridge), custodian_id, exclusive_custody_attested(bool), store_contact, cabinet_monitor_id?
  - _Custody limited to on-site prescriber (C7); exclusive-custody attestation + designated store contact recorded (GAP-3). Optional CM-01 binding for logged access._
- **AccessLog** — id, tenant_id, location_id, actor_id?, badge_id?, at, event(open|close|tamper_motion|tamper_mask|tamper_lid|sensor_disagreement|heartbeat), attributed(bool), seq
  - _Feeds the CM-01 cabinet sensor + audit (C15). Server decides policy (unattributed/after-hours/ajar/tamper -> facility job); monotonic seq detects gaps/resets._

## Other

- Source PRD: [PRD-04-consult-prescribing-s4.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-04-consult-prescribing-s4.md)

## Tasks (dev pickup)

- [ ] **StockLocation + AccessLog model (exclusive custody, attestation) (model & migration)**
  Add StockLocation: id, tenant_id, name, custodian_id, exclusive_custody_attested(bool), store_contact, cabinet_monitor_id (nullable); RLS by tenant. Add AccessLog: id, tenant_id, location_id, actor_id/badge_id (nullable), at, event(open|close|tamper_*|sensor_disagreement|heartbeat), attributed(bool), seq(monotonic). StockItem.location_id + custodian_id FK to the location. AccessLog is append-only.
- [ ] **Custody/storage API + exclusive-custody rule**
  Endpoints: POST/PATCH /locations (custodian, attestation, store_contact), POST /locations/{id}/custody (take/transfer custody - capability-gated to NP/prescriber). Enforce: only a prescribe-S4 staffer can be custodian (C7); record exclusive_custody_attested + store_contact (GAP-3). Flag a remote prescriber consigning stock to a clinic without their exclusive on-site custody as non-compliant (surface it, don't silently allow). RNs may possess-to-administer only.
- [ ] **Cabinet-monitor ingest + access-log policy + audit**
  Endpoint POST /clinics/{slug}/cabinets/{id}/events: verify the per-cabinet bearer token + HMAC X-Signature, dedupe on Idempotency-Key, check monotonic seq (gap/reset = tamper). Server decides policy from raw signals: raise a facility job on unattributed open (no recent badge tap), after-hours, door-left-ajar (no close), any tamper_*/sensor_disagreement, missed heartbeat (>2 intervals) or seq gap. Write every access event to AccessLog + audit (C15).
