# Lot → clients recall lookup & medicine register

> **Epic:** [PRD-04 — Consult, prescribing & S4 medicines governance (the moat)](../epics/PRD-04.md)  ·  **Key:** `PRD-04/RECALL-LOOKUP`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-04/ADMIN-GATE`

## Background

As a prescriber/owner, I want to enter a lot number and instantly see every client who received it, plus export the medicine register, so that we can run a recall in minutes and evidence the register.
Given a lot, the system must instantly list every client/administration for that lot, and export an audit-ready medicine register (C8).

## How it works

This is the payoff of recording per-point batch-lot at every administration (C8). When a sponsor or the TGA issues a field-safety notice for a specific lot, the clinic must instantly identify and contact everyone treated from that lot. A recall that takes days on paper takes minutes here.
It is also where the audit-ready medicine register is produced: a complete, immutable record of every administration (batch-lot, qty, prescriber, administrator, client, datetime), queryable and exportable for QLD Health / AHPRA scrutiny. Recall execution + acknowledgement tracking lives in the Governance hub (full hub in PRD-08/11).
The recall query takes a lot number and returns every Administration for that lot - client, datetime, units, administrator - built directly on the immutable Administration + StockItem data (no separate denormalised copy that could drift). An index on Administration(lot_id) makes it instant.
Starting a recall creates a Recall record (lot, reason, started_at) and tracks per-client acknowledgement. Safety messages go out even to clients who opted out of marketing (a safety comm, not a promotional one); the acknowledgement trail (X of N acknowledged) is exactly what an inspector asks for.
The medicine register is the same immutable Administration data, queryable by date, product, prescriber and administrator, and exportable - the audit-ready S4 register (C8).

## Requirements

- To enter a lot number and instantly see every client who received it, plus export the medicine register.
- Compliance: [C8](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] A lot lookup returns all clients/administrations for that lot.
- [ ] The S4 register exports a complete, immutable record of administrations.
- [ ] Recall execution + acknowledgement tracking is available (full hub in PRD-08/11).
- [ ] The register is queryable by date, product, prescriber, administrator.

## UI designs / screenshots

- Prototype screen: Governance - Recalls (gov-recalls.png).
- Governance > Recalls explains the play: 'turn the lot number into the exact client list instantly, send an SMS + call, and track who has acknowledged.'
- An active recall card: 'RC-12 - Lot B2188 (Botulinum toxin) - Sponsor field-safety notice' with a progress bar '9 of 14 acknowledged - 64%' and a 'Run recall' action.
- Run recall resolves the lot to its affected clients/administrations and starts acknowledgement tracking; safety messages reach clients even if they opted out of marketing.
- The medicine register is queryable by date, product, prescriber, administrator and exportable (audit pack).

![gov-recalls — prototype screen](../screens/gov-recalls.png)

## Suggested data model

- **LotRecall (query)** — lot -> [Administration{client, at, units, administrator, prescriber}]
  - _Built on Administration + StockItem; index on Administration(lot_id). Powers recall + register export (C8). Mapping: recallsData[] {id, lot, product, reason, clients, acked, status}._
- **Recall** — id, tenant_id, lot, reason, started_at, status, acknowledgements[]{client_id, at, via}
  - _Tracks per-client acknowledgement; safety comms bypass marketing opt-out. The ack trail is the inspector-facing evidence._
- **MedicineRegister (read model)** — queryable view over immutable Administration: date, product, prescriber, administrator, client, lot, units
  - _Audit-ready export (C8); immutable source (ADR-0010)._

## Other

- Source PRD: [PRD-04-consult-prescribing-s4.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-04-consult-prescribing-s4.md)

## Tasks (dev pickup)

- [ ] **Recall entity + lot index over Administration (model & migration)**
  Add Recall: id, tenant_id, lot, reason, started_at, status, acknowledgements[]{client_id, at, via}; RLS by tenant. Add the index on Administration(lot_id) (and (lot_id, client_id)) that makes the lot->clients lookup instant. Build the MedicineRegister read model as a queryable view over the immutable Administration stream (date, product, prescriber, administrator, client, lot, units) - no denormalised copy that could drift (ADR-0013).
- [ ] **Recall lookup + register query/export API**
  Endpoints: GET /recall/lookup?lot=... returns every Administration for the lot (client, at, units, administrator, prescriber); POST /recall starts a Recall (lot, reason) and seeds acknowledgement tracking; PATCH /recall/{id}/ack records a client acknowledgement (via sms|call|app). GET /register queryable by date/product/prescriber/administrator with an export (audit pack). Recall safety comms are sent even to marketing-opt-out clients (safety, not promotion).
- [ ] **Immutability guarantee + acknowledgement trail audit**
  The register/recall read strictly from the append-only Administration stream (ADR-0010) so the exported register is provably complete and tamper-evident. Audit recall start, each acknowledgement and each register export - the X-of-N acknowledged trail and the export log are the inspector-facing evidence (C8). Full recall execution + DAEN routing detail hand off to the Governance hub (PRD-08/11).
