# Custom-role builder (placeholder)

> **Epic:** [PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model)](../epics/PRD-01.md)  ·  **Key:** `PRD-01/ROLE-BUILDER`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P2  ·  **Estimate:** 1 pts  ·  **Area:** backend

## Background

Foundations & tenancy (auth, RBAC, audit, data model) — The domain backbone on top of the Sprint 0 plumbing: tenant provisioning, RBAC + scope-of-practice enforcement, the credential/PII compliance gate that decides who can inject, the exportable audit trail, retention & destruction, the data-breach workflow, and client privacy rights.

As a owner, I want to define custom roles from capabilities, so that I can model staff arrangements that don't fit the presets.

Beyond the preset personas, a future custom-role builder lets owners define bespoke capability sets. Deferred — placeholder.

## Requirements

- To define custom roles from capabilities.
- Traces to requirement(s): REQ-TEN-5.
- Deferred (Phase 2+): placeholder — design-only for now.

## Acceptance Criteria

- [ ] Placeholder — design only in v1; presets are sufficient for launch.
- [ ] Captured so the capability model stays builder-ready.

## UI designs / screenshots

prototype.html — header 'Switch user' (sign-in/persona), Team → People & credentials / Compliance board, Settings.

## Technical notes (high level)

Stack: .NET API (domain/services).
Architecture decisions: ADR-0017 (see docs/adr/decision-log.md).

## Other

Epic: PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model).
Source PRD: docs/prds/PRD-01-foundations-tenancy.md.
Backlog key: PRD-01/ROLE-BUILDER.
Phase: 2+ · Priority: P2 · Estimate: 1 pts.

## Tasks (dev pickup)

- [ ] **Scope & design when pulled into a sprint** — Deferred placeholder — no build yet.
- [ ] **Confirm it still fits scope / regulatory stance**
