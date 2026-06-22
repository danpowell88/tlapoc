# Active-role context, scope display & multi-role switching

> **Epic:** [PLATFORM — Platform shell, navigation & cross-cutting UX](../epics/PLATFORM.md)  ·  **Key:** `PLATFORM/ROLE-CONTEXT`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** web
>
> **Depends on:** `PRD-01/RBAC`, `PRD-01/MULTI-ROLE`

## Background

As a staff member with more than one role, I want to see my current role and scope and switch active role where I hold several, so that the app applies the right permissions and shows why an action is blocked.
Plainly: the header chip that makes 'who am I acting as, and what can I do' explicit, with a scope summary and — for people who hold several roles — a way to switch. It is built on the permission layer and the multi-role story. It is the human-facing window onto the permission system: the scope it shows and the rules the server enforces come from the same source, so they always agree. The prototype shows the current persona, role + a scope-of-practice tooltip, and a 'switch user' control. Real users may hold multiple roles (e.g. NP who is also owner) and need to act under a chosen role with the correct scope.

## How it works

The header makes 'who am I acting as, and what can I do' explicit. It shows the signed-in user, the active role, and a scope-of-practice summary — the prototype renders this as the header user chip with a hover scope tooltip (scopeNote, e.g. for the NP: 'Full clinical scope · prescribes & holds S4 (Schedule 4 prescription-only medicine) stock · no business financials') and a 'Switch user' control.
For users who hold more than one role (MULTI-ROLE — an NP who is also owner, a Lead covering reception), a switch-active-role control lets them choose which role they're acting under; capabilities (and therefore visible nav, available actions and the scope summary) update accordingly. Scope is sourced from PRD-01 RBAC (role-based access control) — the role's capabilities/concerns — not hard-coded per screen, so the tooltip and the enforcement always agree.
The active role is recorded on actions and in the audit trail (MULTI-ROLE stamps active_role_id; the role_switch event is audited). When an action is blocked, the scope context is what explains why — the blocked-action banner references the active role and the rule that fired.
Edge cases: a single-role user sees the role/scope but no switch control; switching role re-derives nav + scope immediately (APP-NAV/TODAY re-tailor); financials stay hidden after switching into a clinical role unless the user also holds the finance capability (FIN-GATING invariant from MULTI-ROLE).

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

- Prototype: header user chip + scope tooltip + 'Switch user' (dashboard.png) — shows the signed-in user, active role and a scope-of-practice summary (the persona note); a switch-active-role control for multi-role users.
- Switching role updates capabilities, visible nav and the scope summary immediately; scope sourced from RBAC, not per-screen.

![dashboard — prototype screen](../screens/dashboard.png)

## Suggested data model

- **(session) ActiveRole** — session.active_role_id (from StaffRole) -> scope summary from Role.capabilities/concerns
  - _Stamped on actions + audit (MULTI-ROLE); the scope tooltip + enforcement read the same RBAC source so they always agree._

## Technical notes (high level)

- Architecture decisions: [ADR-0017](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [README.md](https://github.com/danpowell88/tlapoc/blob/main/docs/ux/README.md)

## Tasks (dev pickup)

- [ ] **Active-role + scope context surface (header chip, tooltip, switcher)**
  Build the header user chip showing signed-in user + active role + a scope-of-practice summary sourced from the RBAC (role-based access control) session context (the role's capabilities/concerns — not hard-coded), with the hover scope tooltip. For multi-role users (MULTI-ROLE) add a switch-active-role control; single-role users see no switcher. Render from the same source the server enforces so the tooltip and gates always agree.
- [ ] **Apply active-role switch across the app + audit**
  On switching active role, re-fetch the session context and re-derive visible nav (APP-NAV), Today tailoring (TODAY) and available actions immediately; capabilities update accordingly. The switch is an audited role_switch event and subsequent actions are stamped with the active role (MULTI-ROLE). Keep financials hidden after switching into a clinical role unless the user also holds finance capability (FIN-GATING).
