# Staff credentials + canInject compliance gate

> **Epic:** [PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model)](../epics/PRD-01.md)  ·  **Key:** `PRD-01/CREDENTIALS`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-01/RBAC`

## Background

As a owner, I want structured credential + CPD + cosmetic-cover-insurance records that derive whether each practitioner is cleared to treat/inject, so that only registered, insured, in-scope staff can be booked and can treat.
Staff profiles hold AHPRA reg #, type, status/expiry, conditions, ≥1yr-experience flag, CPD and cosmetic-cover PII; these derive a single canInject gate. Must accept the new designated RN prescriber role.

## How it works

Each clinician profile holds the regulatory facts that decide whether they may treat: AHPRA registration no/type/status/expiry/conditions, the >=1yr-experience flag, CPD hours, and professional indemnity insurance that must explicitly cover cosmetic procedures.
These derive a single canInject signal: a practitioner whose PII excludes cosmetic, or whose registration has lapsed, is auto-flagged not-cleared and removed from bookable availability (PRD-02) — the 'cleared to treat' guarantee.

## Requirements

- Structured credential + CPD + cosmetic-cover-insurance records that derive whether each practitioner is cleared to treat/inject.
- Compliance: [C4](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria), [C19](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Profiles capture AHPRA reg/type/status/expiry/conditions, ≥1yr-experience flag, CPD and cosmetic-cover PII.
- [ ] A practitioner whose PII excludes cosmetic, or whose registration has lapsed, is flagged not-cleared.
- [ ] The designated RN prescriber role is supported (endorsement + recorded partnered prescriber).
- [ ] canInject is a single derived signal consumed by booking (PRD-02) and treatment gates.

## UI designs / screenshots

- Prototype: Team -> People & credentials (team-people.png) — staff cards with reg #, type, status, expiry, CPD, PII cover, engagement type and a derived 'cleared to treat' badge.
- AHPRA register auto-verification (PIE) shown as a verify action with a first-class manual-verify fallback.

![team-people — prototype screen](../screens/team-people.png)

## Suggested data model

- **StaffProfile** — id, tenant_id, user_id, role_id, ahpra_no, ahpra_type, ahpra_status, ahpra_expiry, conditions, experience_1yr, engagement_type(employee|contractor)
  - _Derives canInject._
- **Credential** — id, staff_id, kind(registration|insurance|cpd|training), reference, status, expiry, evidence_ref, cosmetic_cover(bool)
  - _Insurance must flag cosmetic_cover for canInject._
- **(derived) canInject** — = registration current AND cosmetic PII AND in-scope role
  - _Consumed by booking + treatment gates._

## Technical notes (high level)

- Architecture decisions: [ADR-0028](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md), [ADR-0029](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations** — Entities/columns + relationships; tenant_id + RLS.
- [ ] **Backend: domain logic, rules & API endpoint(s)** — Behaviour + invariants + the OpenAPI contract the UI/clients consume.
- [ ] **Enforce compliance gate + audit events** — Server-side (C4, C19); blocked path explains why.
