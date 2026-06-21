# Global search (clients, appointments, invoices)

> **Epic:** [PLATFORM — Platform shell, navigation & cross-cutting UX](../epics/PLATFORM.md)  ·  **Key:** `PLATFORM/SEARCH`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web
>
> **Depends on:** `PLATFORM/APP-NAV`

## Background

As a front desk, I want one search box that finds clients, appointments and invoices, so that I can jump to anything in a couple of keystrokes.
The prototype header has a global search across clients, appointments and invoices — a core front-desk speed feature absent from the backlog.

## Requirements

- One search box that finds clients, appointments and invoices.
- Compliance: [C10](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Search returns matching clients, appointments and invoices, grouped by type.
- [ ] Results are tenant-scoped and respect role/financial gating (no money to non-owner).
- [ ] Selecting a result deep-links to the relevant screen.
- [ ] Search is keyboard-accessible and fast on clinic data volumes.

## UI designs / screenshots

prototype.html — header search box.

## Technical notes (high level)

- Stack: Angular web (admin/front-desk/public)

## Other

- Source PRD: [README.md](https://github.com/danpowell88/tlapoc/blob/main/docs/ux/README.md)

## Tasks (dev pickup)

- [ ] **Web UI** — prototype.html — header search box.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
