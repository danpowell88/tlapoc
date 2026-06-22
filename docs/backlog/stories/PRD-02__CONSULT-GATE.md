# Consult gate on injectable appointments

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/CONSULT-GATE`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-02/ONLINE-BOOK`

## Background

As a system, I want to block a checked-in injectable appointment from opening charting unless a consult is linked, so that no S4 treatment can proceed without the required consult.
The consult gate is the booking-side half of the clinic's compliance moat. It sits in Reception (PRD-02) right after a client is booked and checked in, and it stands between the visit and the clinical record: a checked-in injectable visit cannot open charting (PRD-05) until a consult has been linked. It pairs with the consent gate from Intake/Consent (PRD-03/GATING) and is cleared downstream when the prescriber records the consult in Injectables (PRD-04/CONSULT) — together these enforce the consult → prescription → administration chain before any prescription-only treatment can proceed. As the system, I want to block a checked-in injectable appointment from opening charting unless a consult is linked, so that no S4 treatment can proceed without the required consult.  An injectable appointment cannot move to charting without a linked Consult — the booking-side half of the moat (REQ-BOOK-5).

## How it works

The booking-side half of the compliance moat: a checked-in injectable (S4) appointment cannot progress to charting until a synchronous Consult is linked (REQ-BOOK-5, C1). The gate is server-enforced — the open-charting action checks Appointment.consult_id (for S4 services) before returning the charting context, so it cannot be bypassed by hitting the API directly.
On the schedule/Today board the injectable visit shows its gate status; on the Charting screen the pre-treatment review shows the gate chips (Consult / Consent / screening) and a calm blocked-action banner stating what is missing and who can resolve it (per ADR-0008 — never a dead-end). Once the prescriber records the consult (handoff to PRD-04 CONSULT), consult_id is set and the gate clears.
This complements, and is distinct from, the consent gate (PRD-03 GATING) and the Rx gate (PRD-04): consult-linked is necessary but not alone sufficient for an S4 treatment. Non-S4 (skin) services have no consult requirement and are unaffected.

## Requirements

- To block a checked-in injectable appointment from opening charting unless a consult is linked.
- Compliance: [C1](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] A checked-in injectable appointment with no linked consult cannot open the charting screen.
- [ ] The blocked-action banner explains what's missing and who can resolve it.
- [ ] Once a consult is recorded the gate clears (handoff to PRD-04).
- [ ] The block is server-enforced, not just UI.

## UI designs / screenshots

- Prototype: Charting (charting.png) — the patient header shows 'Consult ✓ · Consent ✓ · screening clear'; the Pre-treatment review card surfaces the same chips and the Consult & prescription card. A checked-in injectable with no consult cannot open charting and shows why.
- On the schedule/Today board the injectable visit shows its gate status (e.g. 'Awaiting consent/consult' style chip).
- Blocked-action banner explains what's missing, links to the fix (record consult), and names who can resolve it (NP/prescriber).

![charting — prototype screen](../screens/charting.png)

## Suggested data model

- **Appointment.consult_id** — FK Consult (PRD-04), nullable until consult recorded
  - _Charting open is blocked while null for S4 services; non-S4 ignores it._
- **(derived) ConsultGate** — = service.schedule==S4 ⇒ require Appointment.consult_id present
  - _Evaluated server-side before charting context is returned (ADR-0008); audited._

## Other

- Source PRD: [PRD-02-booking-scheduling.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-02-booking-scheduling.md)

## Tasks (dev pickup)

- [ ] **Server-side consult gate on charting-open (S4 only)**
  When the charting context for an Appointment is requested, evaluate the gate: if service.schedule==S4 (Schedule 4 prescription-only medicine) and Appointment.consult_id is null, refuse to return the editable charting context and return a structured 'missing: consult' reason instead. Enforce in the domain/API layer (ADR-0008), independent of the UI. Add Appointment.consult_id (FK Consult, nullable). Clearing happens when PRD-04 records the consult and sets consult_id.
- [ ] **Gate status on Today/Schedule board + blocked-action banner**
  Surface the per-visit gate state on the Today board and Schedule (chip: consult/consent/screening status). On the Charting screen render the calm blocked-action banner from the structured reason: what's missing, the fix link (record consult), and who can resolve it (NP/prescriber). Reuse the same banner component PRD-03 GATING uses.
- [ ] **Gate-decision audit events**
  Every gate evaluation that BLOCKS (and the later clear) writes an AuditEvent (actor, appointment, reason, timestamp) to the append-only stream (ADR-0010) so the moat is demonstrable to a regulator. Emit a domain event when consult_id is set so the board/banner update live.
