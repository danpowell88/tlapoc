# Active-role context, scope display & multi-role switching

> **Epic:** [PLATFORM — Platform shell, navigation & cross-cutting UX](../epics/PLATFORM.md)  ·  **Key:** `PLATFORM/ROLE-CONTEXT`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** web
>
> **Depends on:** `PRD-01/RBAC`, `PRD-01/MULTI-ROLE`

## Background

As a staff member with more than one role, I want to see my current role and scope and switch active role where I hold several, so that the app applies the right permissions and shows why an action is blocked.
The prototype shows the current persona, role + a scope-of-practice tooltip, and a 'switch user' control. Real users may hold multiple roles (e.g. NP who is also owner) and need to act under a chosen role with the correct scope.

## How it works

The header shows the signed-in user, active role and a scope-of-practice summary; a user holding multiple roles can switch active role and capabilities update accordingly (consumes PRD-01 RBAC + MULTI-ROLE). The active role is recorded on actions and in the audit trail; scope is sourced from RBAC, not hard-coded per screen.
Makes 'who am I acting as and what can I do' explicit, and explains blocks.

## Requirements

- To see my current role and scope and switch active role where I hold several.
- Compliance: [C4](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Header shows the signed-in user, active role and a scope-of-practice summary.
- [ ] A user holding multiple roles can switch active role; capabilities update accordingly.
- [ ] The active role is recorded on actions and in the audit trail.
- [ ] Scope is sourced from PRD-01 RBAC, not hard-coded per screen.

## UI designs / screenshots

_Prototype screen: prototype.html — sidebar/app shell, Today dashboard, header (global search, clinic switcher, switch-user, scope tooltip)._

- Prototype: header user chip + scope tooltip + 'Switch user' (dashboard.png) — active role + scope summary; switch-active-role for multi-role users.

![dashboard — prototype screen](../screens/dashboard.png)

## Suggested data model

- **(session) ActiveRole** — session.active_role_id (from StaffRole)
  - _Stamped on actions + audit; scope from Role.capabilities._

## Technical notes (high level)

- Architecture decisions: [ADR-0017](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [README.md](https://github.com/danpowell88/tlapoc/blob/main/docs/ux/README.md)

## Tasks (dev pickup)

- [ ] **Enforce compliance gate + audit events**
  Enforce C4 as a server-side invariant that cannot be bypassed via the API:
  - Block the action when prerequisites are missing; return a clear reason for the blocked-action banner (what's blocked / which rule / how to resolve / who can resolve).
  - Write an immutable AuditEvent for the attempt and its outcome.
- [ ] **Web UI**
  Build on the Angular web app: the dashboard per the UI spec. Wire to the API with loading/empty/error states; capability-gate controls; responsive; show the blocked-action banner / gate chips where gated; respect owner-only .fin gating for money figures.
  Key elements (from the prototype):
  - Prototype: header user chip + scope tooltip + 'Switch user' (dashboard.png) — active role + scope summary; switch-active-role for multi-role users.
