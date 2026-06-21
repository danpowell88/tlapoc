# Global search (clients, appointments, invoices)

> **Epic:** [PLATFORM — Platform shell, navigation & cross-cutting UX](../epics/PLATFORM.md)  ·  **Key:** `PLATFORM/SEARCH`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web
>
> **Depends on:** `PLATFORM/APP-NAV`

## Background

As a front desk, I want one search box that finds clients, appointments and invoices, so that I can jump to anything in a couple of keystrokes.
The prototype header has a global search across clients, appointments and invoices — a core front-desk speed feature absent from the backlog.

## How it works

One global search across clients, appointments and invoices, grouped by type, returning tenant-scoped results that respect role/financial gating (no money to non-owner). Selecting a result deep-links to the relevant screen; keyboard-accessible and fast.
The front-desk speed feature — jump to anything in a couple of keystrokes.

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

- Prototype: the header search box (dashboard.png, 'Search clients, appointments, invoices…') — grouped results; select -> deep link.

![dashboard — prototype screen](../screens/dashboard.png)

## Suggested data model

- **(index) SearchIndex** — client/appointment/invoice projections, tenant-scoped
  - _Role/financial-filtered results._

## Technical notes (high level)

- Stack: Angular web (admin/front-desk/public)

## Other

- Source PRD: [README.md](https://github.com/danpowell88/tlapoc/blob/main/docs/ux/README.md)

## Tasks (dev pickup)

- [ ] **Web UI** — prototype.html — header search box.
