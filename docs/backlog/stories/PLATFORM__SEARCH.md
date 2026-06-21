# Global search (clients, appointments, invoices)

> **Epic:** [PLATFORM — Platform shell, navigation & cross-cutting UX](../epics/PLATFORM.md)  ·  **Key:** `PLATFORM/SEARCH`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web
>
> **Depends on:** `PLATFORM/APP-NAV`

## Background

Platform shell, navigation & cross-cutting UX — The cross-cutting product surfaces the prototype exercises that don't belong to a single feature PRD: the app shell + collapsible workspace navigation, the role-tailored Today dashboard, global search, the in-app notification centre, the clinic switcher, the persona/active-role + scope-of-practice display, and the owner-only financial (.fin) gating that hides money figures from non-owner roles.

As a front desk, I want one search box that finds clients, appointments and invoices, so that I can jump to anything in a couple of keystrokes.

The prototype header has a global search across clients, appointments and invoices — a core front-desk speed feature absent from the backlog.

## Requirements

- One search box that finds clients, appointments and invoices.
- Traces to requirement(s): REQ-CLI-1.

## Acceptance Criteria

- [ ] Search returns matching clients, appointments and invoices, grouped by type.
- [ ] Results are tenant-scoped and respect role/financial gating (no money to non-owner).
- [ ] Selecting a result deep-links to the relevant screen.
- [ ] Search is keyboard-accessible and fast on clinic data volumes.

## UI designs / screenshots

prototype.html — header search box.

## Technical notes (high level)

Stack: Angular web (admin/front-desk/public).
Depends on: PLATFORM/APP-NAV.

## Other

Epic: PLATFORM — Platform shell, navigation & cross-cutting UX.
Source PRD: docs/ux/README.md.
Backlog key: PLATFORM/SEARCH.
Phase: 1 · Priority: P2 · Estimate: 2 pts.
Compliance criteria: C10.

## Tasks (dev pickup)

- [ ] **Web UI** — prototype.html — header search box.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
