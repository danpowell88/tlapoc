# OpenAPI contract + typed client generation

> **Epic:** [SPRINT-0 — Sprint 0 — Foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/OPENAPI`  ·  **Type:** Chore  ·  **Stage:** M0  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** backend
>
> **Depends on:** `SPRINT-0/API`

## Background

Sprint 0 — Foundations & setup — Everything the team needs in place before feature work begins: repositories and solution structure, CI/CD, cloud environments in Australia East, identity wiring for staff and clients, the Postgres + RLS data baseline, the API/web/app shells, a shared design system, observability, a security baseline, and the four de-risk spikes called out in the docs index.

As a developer, I want the API to publish an OpenAPI document and CI to generate typed clients for web and Flutter, so that front-ends always match the API contract.

Generating typed clients for Angular and Flutter from the API's OpenAPI spec keeps the three surfaces in lock-step and removes hand-written DTO drift (ADR-0006).

## Requirements

- The API to publish an OpenAPI document and CI to generate typed clients for web and Flutter.

## Acceptance Criteria

- [ ] API serves a versioned OpenAPI document.
- [ ] Typed clients are generated for Angular and Flutter and published to the shared packages.
- [ ] Client generation runs in CI and fails on a breaking contract change without a version bump.
- [ ] The sample endpoint is consumed via the generated client in both web and app.

## UI designs / screenshots

Non-UI / platform scaffolding — no prototype screen.

## Technical notes (high level)

Stack: .NET API (domain/services).
Architecture decisions: ADR-0006 (see docs/adr/decision-log.md).
Depends on: SPRINT-0/API.

## Other

Epic: SPRINT-0 — Sprint 0 — Foundations & setup.
Source PRD: docs/prds/PRD-01-foundations-tenancy.md.
Backlog key: SPRINT-0/OPENAPI.
Phase: 0 · Priority: P1 · Estimate: 3 pts.

## Tasks (dev pickup)

- [ ] **Implement: OpenAPI contract + typed client generation**
- [ ] **Document setup & usage**
- [ ] **Validate in dev + add a smoke test**
