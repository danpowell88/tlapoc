# Owner-only financial (.fin) capability gating

> **Epic:** [PLATFORM — Platform shell, navigation & cross-cutting UX](../epics/PLATFORM.md)  ·  **Key:** `PLATFORM/FIN-GATING`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-01/RBAC`

## Background

As a owner, I want all revenue/MRR/pricing figures hidden from non-owner roles across the app and API, so that financials stay owner-only.
Project rule + prototype: revenue, MRR and pricing figures must stay gated behind the owner financial capability; non-owner roles (e.g. reception) see memberships but no money figures. The prototype tags these with a .fin class toggled by capability.

## Requirements

- All revenue/MRR/pricing figures hidden from non-owner roles across the app and API.
- Compliance: [C4](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria), [C10](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] A financial capability gates money figures in dashboards, checkout, finance, memberships and reports.
- [ ] Non-owner roles see operational data (e.g. membership status) but no revenue/MRR/pricing.
- [ ] Gating is enforced server-side (API never returns gated figures to unauthorised roles), not just hidden in UI.
- [ ] Attempted access is denied and audited.

## Technical notes (high level)

- Stack: .NET API (domain/services)
- Architecture decisions: [ADR-0017](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [README.md](https://github.com/danpowell88/tlapoc/blob/main/docs/ux/README.md)

## Tasks (dev pickup)

- [ ] **Domain logic & business rules** — Core behaviour + invariants.
- [ ] **API endpoint(s) + OpenAPI contract** — Wire request/response; regenerate clients.
- [ ] **Enforce compliance gate + audit events** — Server-side (C4, C10); blocked path explains why.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
