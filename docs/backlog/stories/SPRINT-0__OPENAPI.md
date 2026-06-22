# OpenAPI contract + typed client generation

> **Epic:** [SPRINT-0 — Engineering foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/OPENAPI`  ·  **Type:** Chore  ·  **Stage:** M0  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** backend
>
> **Depends on:** `SPRINT-0/API`

## Background

As a developer, I want the API to publish an OpenAPI document and CI to generate typed clients for web and Flutter, so that front-ends always match the API contract.
Generating typed clients for Angular and Flutter from the API's OpenAPI spec keeps the three surfaces in lock-step and removes hand-written DTO drift (ADR-0006).

## How it works

The API publishes a versioned OpenAPI document generated from its endpoints and models, with the version bumped deliberately on contract changes. CI runs the client generators (one for Angular/TypeScript, one for Flutter/Dart) and publishes the results into the shared packages from REPO, so front-ends import a typed client rather than writing DTOs.
Client generation runs in the pipeline (CICD) and is a gate: a breaking contract change without a version bump fails the build, which is what keeps web and Flutter from silently diverging from the API. The generated artefacts are reproducible from the spec, so a regenerate is deterministic.
The vertical-slice sample endpoint from API is consumed via the generated client in both web and Flutter, proving the round-trip (spec -> generated client -> real call) before feature work depends on it. Versioning strategy and the breaking-change definition are documented so module authors know when a bump is required.

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

- [ ] **Publish a versioned OpenAPI doc and generate typed clients into the shared packages**
  Make the API contract the single source and generate clients from it for both front-ends.
  - API serves a versioned OpenAPI document generated from its endpoints/models.
  - Generators produce an Angular/TypeScript client and a Flutter/Dart client, published into the shared API-client package(s) from REPO.
  - Generation runs in CI and fails the build on a breaking contract change without a version bump (the lock-step guarantee).
  - The API sample endpoint is consumed via the generated client in both web and Flutter to prove the round-trip.
- [ ] **Document the contract/versioning workflow**
  Write the contract guide so module authors keep the surfaces in sync.
  - How to regenerate clients locally and how CI enforces it.
  - The versioning scheme and the definition of a breaking change that requires a bump.
  - Where generated clients live and how web/Flutter import them.
