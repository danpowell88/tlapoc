# Server-enforced treatment gating

> **Epic:** [PRD-03 — Intake, consent & compliance gating](../epics/PRD-03.md)  ·  **Key:** `PRD-03/GATING`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-03/CONSENT`, `PRD-03/BDD`

## Background

As a RN/NP, I want the system to block treatment until required intake and consent are complete and current, telling me exactly what's missing, so that the compliant path is the only path.
Server-enforced treatment gating is the keystone of Intake & Consent (PRD-03): the single, shared mechanism that blocks treatment until the required intake and consent are complete and current. It sits at the end of PRD-03, consuming intake (PRD-03/INTAKE), the BDD screen (PRD-03/BDD) and consent (PRD-03/CONSENT). It is the one gate that the consult/prescription (PRD-04) and charting (PRD-05) downstream all reuse rather than re-implementing — making the compliant path the only path between booking (PRD-02) and the clinical record, and feeding its audited decisions to compliance reporting (PRD-08). As an RN/NP, I want the system to block treatment until required intake and consent are complete and current, telling me exactly what's missing, so that the compliant path is the only path.  Treatment cannot start unless required intake + consent are complete and current — enforced server-side, surfaced via the blocked-action banner (ADR-0008).

## How it works

The shared treatment gate: charting/treatment cannot start unless the required items are complete and current — required IntakeResponse present, an RN/NP-reviewed ScreeningResult (BDD), and a current, version-matched ConsentSignature; for an S4 service it additionally requires the consult (PRD-02 CONSULT-GATE) and Rx (PRD-04). It is enforced server-side as a domain invariant + the charting-open check (ADR-0008), so the compliant path is the only path — it cannot be bypassed via the API.
When blocked it is never a dead-end: a calm blocked-action banner states WHAT is missing, HOW to fix it, and WHO can resolve it (e.g. 'consent v3.2 not signed → send link → client/reception'), and links straight to the fix. The same gate decision is what the Charting pre-treatment review chips reflect.
This is the single mechanism PRD-04 (consult/Rx) and PRD-05 (charting) consume rather than each re-implementing checks; every gate decision (block and clear) is audited so coverage is demonstrable to a regulator. The same gate is reused on the provider app (treatment-room).

## Requirements

- The system to block treatment until required intake and consent are complete and current, telling me exactly what's missing.
- Compliance: [C5](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Treatment is blocked server-side unless required intake + current consent exist.
- [ ] The block states what's missing and how to resolve it (never a dead-end).
- [ ] The gate is the shared mechanism consumed by PRD-04/05.
- [ ] Gate decisions are audited.

## UI designs / screenshots

- Prototype: the Charting pre-treatment review (charting.png) shows the gate chips (Allergies/Contraindications, BDD screen clear, Consent ✓, Consult ✓) and blocks opening the map until satisfied; the banner explains and links the fix.
- Same gate reused on the provider app (treatment-room) and surfaced as the Today 'Awaiting consent — treatment gated until done' tile (dashboard).
- The block states exactly what is missing and is never a dead-end (ADR-0008).

![charting — prototype screen](../screens/charting.png)

## Suggested data model

- **(derived) TreatmentGate** — = required IntakeResponse present AND RN/NP-reviewed ScreeningResult AND current version-matched ConsentSignature (AND Consult/Rx for S4 AND under-18 cooling-off elapsed)
  - _Server-enforced; evaluated before charting opens (ADR-0008); each decision audited._
- **GateDecision (audit)** — id, tenant_id, appointment_id, allowed(bool), missing[], actor_id, at
  - _Append-only record of every block/clear (ADR-0010) for compliance reporting (PRD-08)._

## Technical notes (high level)

- Architecture decisions: [ADR-0008](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-03-intake-consent-gating.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-03-intake-consent-gating.md)

## Tasks (dev pickup)

- [ ] **Shared server-side TreatmentGate evaluation (ADR-0008)**
  A single, reusable gate evaluator invoked before charting/treatment opens: checks required IntakeResponse present, RN/NP-reviewed ScreeningResult, current version-matched ConsentSignature, and (for S4 (Schedule 4 prescription-only medicine)) consult_id + valid Rx + elapsed under-18 cooling-off. Returns allowed + a structured missing[] (item, fix, who-resolves). Enforced as a domain invariant so a direct API call is blocked too. This is the one mechanism PRD-04/05 consume. Every decision writes a GateDecision to the append-only audit stream (ADR-0010) for PRD-08 consent-coverage reporting.
- [ ] **Blocked-action banner (what/how/who) + chips, reused on web + provider app**
  Render the calm blocked-action banner from the gate's missing[]: what is missing, how to fix, who can resolve, with a deep link to the fix (send consent/intake link, record consult). Render the pre-treatment review chips from the same evaluation; reuse the identical component/contract on the Angular charting screen and the Flutter provider app (treatment-room) and the Today 'treatment gated' tile — never a dead-end.
