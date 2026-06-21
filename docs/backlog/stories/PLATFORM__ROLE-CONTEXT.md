# Active-role context, scope display & multi-role switching

> **Epic:** [PLATFORM — Platform shell, navigation & cross-cutting UX](../epics/PLATFORM.md)  ·  **Key:** `PLATFORM/ROLE-CONTEXT`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** web
>
> **Depends on:** `PRD-01/RBAC`, `PRD-01/MULTI-ROLE`

## Background

Platform shell, navigation & cross-cutting UX — The cross-cutting product surfaces the prototype exercises that don't belong to a single feature PRD: the app shell + collapsible workspace navigation, the role-tailored Today dashboard, global search, the in-app notification centre, the clinic switcher, the persona/active-role + scope-of-practice display, and the owner-only financial (.fin) gating that hides money figures from non-owner roles.

As a staff member with more than one role, I want to see my current role and scope and switch active role where I hold several, so that the app applies the right permissions and shows why an action is blocked.

The prototype shows the current persona, role + a scope-of-practice tooltip, and a 'switch user' control. Real users may hold multiple roles (e.g. NP who is also owner) and need to act under a chosen role with the correct scope.

## Requirements

- To see my current role and scope and switch active role where I hold several.
- Traces to requirement(s): REQ-TEN-3, REQ-TEN-4.
- Must satisfy compliance obligation(s): C4.

## Acceptance Criteria

- [ ] Header shows the signed-in user, active role and a scope-of-practice summary.
- [ ] A user holding multiple roles can switch active role; capabilities update accordingly.
- [ ] The active role is recorded on actions and in the audit trail.
- [ ] Scope is sourced from PRD-01 RBAC, not hard-coded per screen.

## UI designs / screenshots

prototype.html — sidebar/app shell, Today dashboard, header (global search, clinic switcher, switch-user, scope tooltip).

## Technical notes (high level)

Stack: Angular web (admin/front-desk/public).
Architecture decisions: ADR-0017 (see docs/adr/decision-log.md).
Depends on: PRD-01/RBAC, PRD-01/MULTI-ROLE.

## Other

Epic: PLATFORM — Platform shell, navigation & cross-cutting UX.
Source PRD: docs/ux/README.md.
Backlog key: PLATFORM/ROLE-CONTEXT.
Phase: 1 · Priority: P1 · Estimate: 3 pts.
Compliance criteria: C4.

## Tasks (dev pickup)

- [ ] **Enforce compliance gate + audit events** — Server-side (C4); blocked path explains why.
- [ ] **Web UI** — prototype.html — sidebar/app shell, Today dashboard, header (global search, clinic switcher, switch-user, scope tooltip).
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
