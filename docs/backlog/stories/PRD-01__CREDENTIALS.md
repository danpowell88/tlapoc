# Staff credentials + canInject compliance gate

> **Epic:** [PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model)](../epics/PRD-01.md)  ·  **Key:** `PRD-01/CREDENTIALS`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-01/RBAC`

## Background

As a owner, I want structured credential + CPD + cosmetic-cover-insurance records that derive whether each practitioner is cleared to treat/inject, so that only registered, insured, in-scope staff can be booked and can treat.
Staff profiles hold AHPRA reg #, type, status/expiry, conditions, ≥1yr-experience flag, CPD and cosmetic-cover PII; these derive a single canInject gate. Must accept the new designated RN prescriber role.

## How it works

Each clinician profile holds the regulatory facts that decide whether they may lawfully treat (ADR-0028, C4/C19, s129 National Law + NMBA cosmetic guidelines): AHPRA registration number/type/status/expiry and any conditions, the >=1-year-cosmetic-experience flag, CPD hours done vs required (RN/EN 20h, NP 30h), and professional-indemnity insurance whose cover must explicitly include cosmetic procedures (standard nursing PII frequently excludes it).
These derive a single boolean canInject, computed exactly as the prototype does: scope is inject AND registration is current (not lapsed) AND insurance covers cosmetic AND insurance is in date. The prototype's staffStatus() shows the human-readable states this drives: 'Current' (emerald), 'Renews in Nd' (amber early warning), 'CPD behind X/Yh' (amber), 'PII excludes cosmetic — blocked' (rose), and 'Not compliant' (rose). Chloe Adams in the seed data is the worked example — registered, but insurance EXCLUDES cosmetic, so canInject is false and she is not bookable for S4.
canInject is the contract other modules consume: booking availability (PRD-02) removes a not-cleared practitioner from offered slots, the charting/administration gate blocks an S4 administration by an uncleared clinician (PRD-04/05), and the owner exceptions digest + Follow-ups queue raise expiry tasks. The signal is necessary on top of the RBAC inject capability — holding the capability is not enough without current credentials.
The designated RN prescriber arrangement (rev-2/rev-4 PRD note) is supported: an RN may administer under a recorded partnered/remote prescriber rather than holding the prescribe capability themselves; the profile records the endorsement and the partnered prescriber. AHPRA register auto-verification via the Practitioner Information Exchange (PIE) is supported where approved, degrading to a first-class manual-verify action that stores a 'verified-on' date (PIE is approval-gated SOAP — treat as best-effort with manual fallback always present).

## Requirements

- Structured credential + CPD + cosmetic-cover-insurance records that derive whether each practitioner is cleared to treat/inject.
- Compliance: [C4](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria), [C19](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Profiles capture AHPRA reg/type/status/expiry/conditions, ≥1yr-experience flag, CPD and cosmetic-cover PII.
- [ ] A practitioner whose PII excludes cosmetic, or whose registration has lapsed, is flagged not-cleared.
- [ ] The designated RN prescriber role is supported (endorsement + recorded partnered prescriber).
- [ ] canInject is a single derived signal consumed by booking (PRD-02) and treatment gates.

## UI designs / screenshots

- Prototype: Team -> People & credentials (team-people.png) — one card per staff member with avatar, name, role, engagement type (Contractor/Employee) and a derived status chip ('Current', 'Renews in 25d', 'PII excludes cosmetic — blocked').
- A credential detail/edit view (per person) captures AHPRA reg #/type/status/expiry/conditions, the >=1yr-experience flag, CPD done/required, and PII insurer/expiry/cosmetic-cover boolean, with a verify action (PIE auto-verify or manual-verify with verified-on date).
- The derived canInject ('cleared to treat' / 'Blocked') is shown read-only — it is computed, never set by hand.

![team-people — prototype screen](../screens/team-people.png)

## Suggested data model

- **StaffProfile (extends TENANT)** — + ahpra_no, ahpra_type(RN|EN|NP|non-AHPRA), ahpra_status, ahpra_expiry, conditions, experience_1yr(bool), engagement_type(employee|contractor), scope(inject|nonS4|none), prescriber_mode(self|partnered), partnered_prescriber_id
  - _Holds the regulatory facts; scope mirrors the prototype (inject/nonS4/none)._
- **Credential** — id, tenant_id, staff_id, kind(registration|insurance|cpd|training), reference, status, expiry, evidence_ref, cosmetic_cover(bool), verified_method(pie|manual), verified_on
  - _Insurance must flag cosmetic_cover for canInject; CPD tracks done vs required; evidence_ref points at signed-URL document storage (AU-resident)._
- **(derived) canInject** — = scope==inject AND registration current AND cosmetic_cover AND insurance in date
  - _Single signal consumed by booking (PRD-02), administration gates (PRD-04/05), the exceptions digest and Follow-ups. Computed server-side; never stored as editable._

## Technical notes (high level)

- Architecture decisions: [ADR-0028](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md), [ADR-0029](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Credential data model & canInject derivation**
  Extend StaffProfile with the AHPRA/experience/engagement/scope fields and model Credential (registration|insurance|cpd|training) with expiry, cosmetic_cover and verified-on. Compute canInject server-side exactly per the prototype rule (scope==inject AND registration current AND cosmetic_cover AND insurance in date) and expose it as a read-only derived signal; recompute on any credential change. Support the designated/partnered prescriber arrangement (prescriber_mode + partnered_prescriber_id). Store credential evidence behind signed URLs in AU-resident storage.
- [ ] **Credential management API + AHPRA PIE / manual verification**
  CRUD for credentials gated to owner/lead (team:manage). Provide a verify action that attempts AHPRA PIE auto-verification where approved and always falls back to a first-class manual-verify that records verified_method + verified_on. Publish the derived canInject and the human-readable status (Current / Renews in Nd / CPD behind / PII excludes cosmetic / Not compliant) so booking, charting gates, the exceptions digest and Follow-ups consume one source of truth. Block S4-relevant booking/administration when canInject is false.
- [ ] **People & credentials UI (Team workspace)**
  Build the Team -> People & credentials cards (team-people.png): staff card with avatar/name/role/engagement and the derived status chip, plus a per-person credential editor for AHPRA reg/type/status/expiry/conditions, experience flag, CPD done/required and PII insurer/expiry/cosmetic-cover, with the verify control. Show canInject read-only. Capability-gate the whole surface to team:manage; non-managers don't see it.
