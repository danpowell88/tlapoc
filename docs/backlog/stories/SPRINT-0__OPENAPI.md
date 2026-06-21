# OpenAPI contract + typed client generation

> **Epic:** [SPRINT-0 — Engineering foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/OPENAPI`  ·  **Type:** Chore  ·  **Stage:** M0  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** backend
>
> **Depends on:** `SPRINT-0/API`

## Background

As a developer, I want the API to publish an OpenAPI document and CI to generate typed clients for web and Flutter, so that front-ends always match the API contract.
Generating typed clients for Angular and Flutter from the API's OpenAPI spec keeps the three surfaces in lock-step and removes hand-written DTO drift (ADR-0006).

## How it works

The API publishes a versioned OpenAPI document and CI generates typed clients for Angular + Flutter into the shared packages, failing on a breaking contract change without a version bump (ADR-0006). Keeps the three surfaces in lock-step and removes hand-written DTO drift.

## Requirements

- The API to publish an OpenAPI document and CI to generate typed clients for web and Flutter.

## Acceptance Criteria

- [ ] API serves a versioned OpenAPI document.
- [ ] Typed clients are generated for Angular and Flutter and published to the shared packages.
- [ ] Client generation runs in CI and fails on a breaking contract change without a version bump.
- [ ] The sample endpoint is consumed via the generated client in both web and app.

## Technical notes (high level)

- Architecture decisions: [ADR-0006](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Implement: OpenAPI contract + typed client generation**
- [ ] **Document setup & usage**
