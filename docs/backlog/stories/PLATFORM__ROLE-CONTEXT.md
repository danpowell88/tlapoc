# Active-role context, scope display & multi-role switching

> **Epic:** [PLATFORM — Platform shell, navigation & cross-cutting UX](../epics/PLATFORM.md)  ·  **Key:** `PLATFORM/ROLE-CONTEXT`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** web
>
> **Depends on:** `PRD-01/RBAC`, `PRD-01/MULTI-ROLE`

## Background

As a staff member with more than one role, I want to see my current role and scope and switch active role where I hold several, so that the app applies the right permissions and shows why an action is blocked.
The prototype shows the current persona, role + a scope-of-practice tooltip, and a 'switch user' control. Real users may hold multiple roles (e.g. NP who is also owner) and need to act under a chosen role with the correct scope.

## Requirements

- To see my current role and scope and switch active role where I hold several.
- Compliance: [C4](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Header shows the signed-in user, active role and a scope-of-practice summary.
- [ ] A user holding multiple roles can switch active role; capabilities update accordingly.
- [ ] The active role is recorded on actions and in the audit trail.
- [ ] Scope is sourced from PRD-01 RBAC, not hard-coded per screen.

## UI designs / screenshots

prototype.html — sidebar/app shell, Today dashboard, header (global search, clinic switcher, switch-user, scope tooltip).

## Technical notes (high level)

- Stack: Angular web (admin/front-desk/public)
- Architecture decisions: [ADR-0017](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [README.md](https://github.com/danpowell88/tlapoc/blob/main/docs/ux/README.md)

## Tasks (dev pickup)

- [ ] **Enforce compliance gate + audit events** — Server-side (C4); blocked path explains why.
- [ ] **Web UI** — prototype.html — sidebar/app shell, Today dashboard, header (global search, clinic switcher, switch-user, scope tooltip).
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
