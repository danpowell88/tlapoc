# Custom-role builder (placeholder)

> **Epic:** [PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model)](../epics/PRD-01.md)  ·  **Key:** `PRD-01/ROLE-BUILDER`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P2  ·  **Estimate:** 1 pts  ·  **Area:** backend

## Background

As a owner, I want to define custom roles from capabilities, so that I can model staff arrangements that don't fit the presets.
Beyond the preset personas, a future custom-role builder lets owners define bespoke capability sets. Deferred — placeholder.

## How it works

Beyond the preset personas (RBAC), a future custom-role builder lets owners compose bespoke capability sets — ticking capabilities + concern tiles to model unusual staffing that doesn't fit a preset (ADR-0017, REQ-TEN-5). Deferred (Phase 2+): the capability/concern model is already builder-ready (roles are lists of capability/concern keys), so this is design-only for v1 — the presets are sufficient for launch.

## Requirements

- To define custom roles from capabilities.
- Deferred (Phase 2+): placeholder, design-only for now.

## Acceptance Criteria

- [ ] Placeholder — design only in v1; presets are sufficient for launch.
- [ ] Captured so the capability model stays builder-ready.

## UI designs / screenshots

- Deferred — no v1 UI. Future: a role editor (name + capability checkboxes + concern tiles) reusing the existing Role/Capability/Concern model; enforcement stays server-side (capabilities gate, concerns present).

## Suggested data model

- **Role (custom)** — reuses Role + RoleCapability/RoleConcern joins + an editor UI
  - _Placeholder; presets suffice for launch. No schema change needed — the builder edits the existing join rows._

## Technical notes (high level)

- Architecture decisions: [ADR-0017](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Scope & design when pulled into a sprint**
  Deferred placeholder — no build in v1. When pulled in: confirm presets still cover real tenant staffing and that the regulatory scope-of-practice constraints (a custom role still can't grant prescribe/S4 custody to an ineligible person) are enforced; then design the role editor over the existing Role/Capability/Concern model (capability checkboxes + concern tiles) with server-side enforcement unchanged, and break it into build tasks.
