# Multi-role staff & active-role context

> **Epic:** [PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model)](../epics/PRD-01.md)  ·  **Key:** `PRD-01/MULTI-ROLE`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-01/RBAC`

## Background

As a staff member with multiple roles, I want to be assigned more than one role and act under a chosen active role, so that my permissions reflect what I'm doing without separate logins.
Some users legitimately hold several roles (e.g. an NP who is also the business owner, or a lead nurse covering reception). The model must allow multiple role assignments and an active-role context that the authorisation pipeline honours.

## How it works

Some staff legitimately hold several roles — an NP who is also the business owner, or a Lead Nurse covering reception. The prototype models exactly these combinations (the Solo-NP and Nurse-led presets union multiple concern/capability sets). This story makes multiple role assignments first-class and defines an active-role context the authorisation pipeline honours.
The model: a StaffProfile has many roles (StaffRole join, one default); a session carries an active_role_id. The RBAC pipeline evaluates capabilities for the active role (not the union) so a clinician acting 'as reception' doesn't accidentally exercise clinical capability — and the active role is stamped on every action and audit event (consumed by PLATFORM/ROLE-CONTEXT). Switching active role is itself a recorded (role_switch) event.
A deliberate invariant: owner-only financial capability (finance.read / .fin) is independent of clinical roles — being an NP never automatically makes you the owner, and switching into a clinical role never reveals financials unless the person also holds the owner/finance capability. This keeps FIN-GATING structurally sound for multi-role people.
Edge cases: a person whose only roles lack a capability simply can't do that action under any active role; the default role is what they land in at sign-in; deactivating one role doesn't sign them out if another remains.

## Requirements

- To be assigned more than one role and act under a chosen active role.
- Compliance: [C4](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] A staff profile can hold multiple roles; the union/active-role model is well-defined.
- [ ] The authorisation pipeline evaluates capabilities for the active role (consumed by PLATFORM/ROLE-CONTEXT).
- [ ] Switching active role is recorded; actions capture the role used.
- [ ] Owner-only financial capability is independent of clinical roles (an NP isn't automatically owner).

## UI designs / screenshots

- Header shows the active role + scope tooltip (extends the prototype persona display); a switch-active-role control appears for users holding more than one role (PLATFORM/ROLE-CONTEXT renders it).
- Switching role updates the visible nav + scope immediately (capabilities re-evaluated for the new active role).

## Suggested data model

- **StaffRole** — staff_id, role_id, is_default
  - _Many-to-many; active role chosen per session and stamped on actions. Default role is the sign-in landing role._
- **(session) active_role_id** — session.active_role_id (from StaffRole)
  - _Pipeline evaluates capabilities for the active role (not the union); role_switch is an audited event; finance capability independent of clinical roles._

## Technical notes (high level)

- Architecture decisions: [ADR-0017](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Multi-role assignment model + default role**
  Model StaffRole as a many-to-many (staff_id, role_id, is_default) so a profile can hold several roles, with one default that is the sign-in landing role. Deactivating one role leaves the others (and the session) intact. Keep owner/finance capability independent of clinical roles — holding a clinical role never implies owner.
- [ ] **Active-role context in the authorisation pipeline**
  Carry active_role_id on the session and make the RBAC pipeline evaluate capabilities for the ACTIVE role (not the union of all roles), so acting 'as reception' can't exercise clinical capability. Resolve the active role at sign-in to the default and on each switch. Expose active role + its capabilities/scope via the session context endpoint (consumed by ROLE-CONTEXT, APP-NAV).
- [ ] **Switch-active-role action + audit stamping**
  Implement switch-active-role (only among roles the user holds), writing a role_switch auth event. Stamp the active role on every action and AuditEvent so the trail shows which role a person acted under. Ensure financials stay invisible after switching into a clinical role unless the user also holds the finance capability.
