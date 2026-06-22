# Global search (clients, appointments, invoices)

> **Epic:** [PLATFORM — Platform shell, navigation & cross-cutting UX](../epics/PLATFORM.md)  ·  **Key:** `PLATFORM/SEARCH`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web
>
> **Depends on:** `PLATFORM/APP-NAV`

## Background

As a front desk, I want one search box that finds clients, appointments and invoices, so that I can jump to anything in a couple of keystrokes.
The prototype header has a global search across clients, appointments and invoices — a core front-desk speed feature absent from the backlog.

## How it works

One global search across clients, appointments and invoices — the front-desk speed feature (the prototype header box reads 'Search clients, appointments, invoices…'). Results are grouped by type, and selecting one deep-links to the relevant screen (client 360, the appointment in Schedule, the invoice in checkout/finance) so staff jump to anything in a couple of keystrokes.
Results are tenant-scoped (RLS) and respect role/financial gating: a non-owner never sees money in results — an invoice result shows the client/date/status but not the amount for a role without finance.read (FIN-GATING), and gating is enforced server-side so the API never returns a figure the role can't see, not merely hidden in the UI. Results also respect capability scope (a role that can't see clinical context doesn't get clinical fields in a client result).
It's keyboard-accessible (focus the box, arrow through grouped results, Enter to open) and fast on real clinic data volumes — backed by a tenant-scoped search projection rather than scanning OLTP tables, kept current from domain events.
Edge cases: an empty query shows recent/contextual suggestions, not everything; a deep-link to a record the role can't fully access opens the parts it can; no result leaks a money figure to a non-owner.

## Requirements

- One search box that finds clients, appointments and invoices.
- Compliance: [C10](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Search returns matching clients, appointments and invoices, grouped by type.
- [ ] Results are tenant-scoped and respect role/financial gating (no money to non-owner).
- [ ] Selecting a result deep-links to the relevant screen.
- [ ] Search is keyboard-accessible and fast on clinic data volumes.

## UI designs / screenshots

_Prototype screen: prototype.html — header search box._

- Prototype: the header search box (dashboard.png, placeholder 'Search clients, appointments, invoices…') — typing returns results grouped by type (Clients / Appointments / Invoices); selecting one deep-links to its screen.
- Keyboard-accessible; tenant-scoped; money figures in invoice results are .fin-gated (owner only).

![dashboard — prototype screen](../screens/dashboard.png)

## Suggested data model

- **(index) SearchIndex** — client / appointment / invoice projections, tenant-scoped, kept current from domain events
  - _Role/financial-filtered at query time — money fields stripped server-side for non-owner roles; capability scope applied to fields._

## Other

- Source PRD: [README.md](https://github.com/danpowell88/tlapoc/blob/main/docs/ux/README.md)

## Tasks (dev pickup)

- [ ] **Tenant-scoped global search (projection, role + .fin filtered, deep-linking)**
  Build a tenant-scoped search projection over clients, appointments and invoices kept current from domain events (not OLTP scans) and the header search UI: grouped results by type, keyboard navigation, and deep-links to client 360 / Schedule / checkout-finance. Enforce role/financial gating server-side so the API never returns a money figure (or a clinical field) the active role can't see — strip, don't hide (FIN-GATING). Empty query shows recent/contextual suggestions.
