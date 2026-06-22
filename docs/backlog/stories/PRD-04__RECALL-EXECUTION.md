# Recall execution & acknowledgement tracking

> **Epic:** [PRD-04 — Consult, prescribing & S4 medicines governance (the moat)](../epics/PRD-04.md)  ·  **Key:** `PRD-04/RECALL-EXECUTION`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-04/RECALL-LOOKUP`

## Background

As a prescriber/owner, I want to start a recall from a lot and track each client's acknowledgement, so that I can prove every affected client was contacted and who has responded.
Plainly: once a lot is implicated in a safety notice, this is the workflow that actually contacts every affected client and tracks who has acknowledged — turning the lookup into a managed recall. Where it fits: a follow-up to PRD-04/RECALL-LOOKUP that adds the recall workflow on top of the instant lot->clients lookup. Starting a recall resolves the lot to its clients, sends a safety comm (even to marketing-opt-out clients, because it is safety not promotion) and tracks the X-of-N acknowledged trail an inspector asks for; the full hub lives in governance (PRD-08/PRD-11).

## How it works

This follow-up adds the recall workflow on top of the basic's lookup. When a sponsor or the TGA (Therapeutic Goods Administration) issues a field-safety notice for a lot, starting a recall creates a Recall record (lot, reason, started_at), resolves the lot to its affected clients/administrations via the PRD-04/RECALL-LOOKUP query, and seeds acknowledgement tracking.
Per-client acknowledgement is recorded (via SMS / call / app) and surfaced as an X-of-N acknowledged progress bar — exactly the trail an inspector asks for. Safety messages go out even to clients who opted out of marketing, because a recall is a safety comm, not a promotional one.
Recall start and each acknowledgement are audited. The full recall execution surface + DAEN routing detail live in the Governance hub (PRD-08/11); this story owns the recall record and the acknowledgement trail.

## Requirements

- To start a recall from a lot and track each client's acknowledgement.

## Acceptance Criteria

- [ ] Starting a recall creates a Recall record (lot, reason, started_at) and resolves the lot to its affected clients/administrations via the lookup.
- [ ] Per-client acknowledgement is tracked (via SMS / call / app) and shown as an X-of-N acknowledged progress trail.
- [ ] Recall safety messages reach clients even if they opted out of marketing (a safety comm, not a promotional one).
- [ ] Recall start, each acknowledgement and the progress trail are audited; full recall execution + DAEN routing detail hand off to the Governance hub (PRD-08/11).

## UI designs / screenshots

- Prototype screen: Governance - Recalls (gov-recalls.png).
- Governance > Recalls explains the play: 'turn the lot number into the exact client list instantly, send an SMS + call, and track who has acknowledged.'
- An active recall card: 'RC-12 - Lot B2188 (Botulinum toxin) - Sponsor field-safety notice' with a progress bar '9 of 14 acknowledged - 64%' and a 'Run recall' action.
- Run recall resolves the lot to its affected clients/administrations and starts acknowledgement tracking; safety messages reach clients even if they opted out of marketing.

![stock — prototype screen](../screens/stock.png)

## Suggested data model

- **Recall** — id, tenant_id, lot, reason, started_at, status, acknowledgements[]{client_id, at, via}
  - _New entity (extends the basic's lookup). Tracks per-client acknowledgement; safety comms bypass marketing opt-out. The ack trail is the inspector-facing evidence._

## Other

- Source PRD: [PRD-04-consult-prescribing-s4.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-04-consult-prescribing-s4.md)

## Tasks (dev pickup)

- [ ] **Recall entity + start-recall from a lot**
  Behaviour: POST /recall starts a Recall (lot, reason) and seeds acknowledgement tracking, resolving the lot to its clients via the PRD-04/RECALL-LOOKUP query. Requirements: add Recall: id, tenant_id, lot, reason, started_at, status, acknowledgements[]{client_id, at, via}; RLS by tenant; recall safety comms are sent even to marketing-opt-out clients (safety, not promotion).
- [ ] **Acknowledgement tracking + trail audit**
  Behaviour: PATCH /recall/{id}/ack records a client acknowledgement (via sms|call|app); the X-of-N acknowledged trail is shown and audited. Requirements: audit recall start and each acknowledgement (C8); full recall execution + DAEN routing detail hand off to the Governance hub (PRD-08/11).
