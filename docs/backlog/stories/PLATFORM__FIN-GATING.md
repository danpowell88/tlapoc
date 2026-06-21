# Owner-only financial (.fin) capability gating

> **Epic:** [PLATFORM — Platform shell, navigation & cross-cutting UX](../epics/PLATFORM.md)  ·  **Key:** `PLATFORM/FIN-GATING`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-01/RBAC`

## Background

Platform shell, navigation & cross-cutting UX — The cross-cutting product surfaces the prototype exercises that don't belong to a single feature PRD: the app shell + collapsible workspace navigation, the role-tailored Today dashboard, global search, the in-app notification centre, the clinic switcher, the persona/active-role + scope-of-practice display, and the owner-only financial (.fin) gating that hides money figures from non-owner roles.

As a owner, I want all revenue/MRR/pricing figures hidden from non-owner roles across the app and API, so that financials stay owner-only.

Project rule + prototype: revenue, MRR and pricing figures must stay gated behind the owner financial capability; non-owner roles (e.g. reception) see memberships but no money figures. The prototype tags these with a .fin class toggled by capability.

## Requirements

- All revenue/MRR/pricing figures hidden from non-owner roles across the app and API.
- Traces to requirement(s): REQ-TEN-3.
- Must satisfy compliance obligation(s): C4, C10.

## Acceptance Criteria

- [ ] A financial capability gates money figures in dashboards, checkout, finance, memberships and reports.
- [ ] Non-owner roles see operational data (e.g. membership status) but no revenue/MRR/pricing.
- [ ] Gating is enforced server-side (API never returns gated figures to unauthorised roles), not just hidden in UI.
- [ ] Attempted access is denied and audited.

## UI designs / screenshots

prototype.html — sidebar/app shell, Today dashboard, header (global search, clinic switcher, switch-user, scope tooltip).

## Technical notes (high level)

Stack: .NET API (domain/services).
Architecture decisions: ADR-0017 (see docs/adr/decision-log.md).
Depends on: PRD-01/RBAC.

## Other

Epic: PLATFORM — Platform shell, navigation & cross-cutting UX.
Source PRD: docs/ux/README.md.
Backlog key: PLATFORM/FIN-GATING.
Phase: 1 · Priority: P0 · Estimate: 5 pts.
Compliance criteria: C4, C10.

## Tasks (dev pickup)

- [ ] **Domain logic & business rules** — Core behaviour + invariants.
- [ ] **API endpoint(s) + OpenAPI contract** — Wire request/response; regenerate clients.
- [ ] **Enforce compliance gate + audit events** — Server-side (C4, C10); blocked path explains why.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
