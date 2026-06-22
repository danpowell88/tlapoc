# Monorepo & solution scaffolding

> **Epic:** [SPRINT-0 — Engineering foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/REPO`  ·  **Type:** Chore  ·  **Stage:** M0  ·  **Priority:** P0  ·  **Estimate:** 3 pts  ·  **Area:** infra

## Background

As a developer, I want a scaffolded repo with the API, web, app and shared-package folders, a clean .NET solution, an Angular workspace and a Flutter workspace wired together, so that everyone builds against one consistent structure and shared code has an obvious home.
A single, well-structured repo (or workspace) for the .NET API, Angular web, two Flutter apps and shared packages keeps versioning, CI and code-sharing sane from day one.

## How it works

A single workspace holds all four deployables plus the shared packages, with formatter, linter and editorconfig enforced locally from the first commit. The agreed top-level layout is api/ (the .NET solution and its bounded modules), web/ (the Angular workspace), apps/ (the Flutter workspace with client and provider flavours), packages/ (the shared design-system and generated API-client libraries), infra/ (IaC, owned by IAC) and scripts/ (dev/seed tooling).
The .NET solution is organised as the modular monolith from ADR-0005: a host/API project plus bounded-module class libraries (Tenancy, Clients, Booking, Clinical, Consent, Rx, Medicines, Payments, Memberships, Notifications, Reporting, Integrations, Facility) and shared kernel projects, so module seams exist before any feature is written. The Angular workspace is set up to consume a library project; the Flutter workspace uses one package with two app entrypoints (flavours) and shared packages for auth, the API client and the design system.
Shared packages start as empty-but-buildable libraries so dependents can reference them immediately — DESIGN fills the design-system package and OPENAPI fills the API-client package later. Consistent editorconfig + formatter + analyzer/lint rules are committed and run on save / pre-commit, so style is settled before the team scales and before CICD makes the same checks blocking.

## Requirements

- A scaffolded repo with the API, web, app and shared-package folders, a clean .NET solution, an Angular workspace and a Flutter workspace wired together.

## Acceptance Criteria

- [ ] Repo layout documented in a top-level README (api/, web/, apps/, packages/, infra/, scripts/).
- [ ] .NET solution builds; Angular workspace serves; both Flutter app shells run on a simulator.
- [ ] Shared design-system and API-client packages exist as empty-but-buildable libraries.
- [ ] Editorconfig, formatter and linter configs committed and enforced locally.

## Technical notes (high level)

- Architecture decisions: [ADR-0005](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md), [ADR-0006](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Scaffold the workspace, solution & shared-package skeleton**
  Create the top-level layout (api/, web/, apps/, packages/, infra/, scripts/) and a root README documenting it.
  - .NET solution: an API host project plus class-library projects for each bounded module of the modular monolith (Tenancy, Clients, Booking, Clinical, Consent, Rx, Medicines, Payments, Memberships, Notifications, Reporting, Integrations, Facility) and a shared-kernel/common project; solution builds clean.
  - Angular workspace under web/ that serves, plus a buildable library project ready to be the home of the design system.
  - Flutter workspace under apps/ with two flavours (client, provider) launching empty shells on a simulator, and placeholder shared packages (auth, api-client, design-system).
  - packages/ holds the design-system and API-client libraries as empty-but-buildable stubs that web and Flutter already reference, so DESIGN and OPENAPI just fill them in.
- [ ] **Commit editorconfig, formatter & analyzer/lint configs and enforce locally**
  Establish one code-style baseline across all three languages, run on save and pre-commit, so style never becomes a review argument and CICD can later make the same checks blocking.
  - Root .editorconfig covering C#, TypeScript and Dart (indentation, line endings, trailing whitespace, final newline).
  - .NET analyzers + format settings; Angular ESLint + Prettier; Dart analyzer/format — each wired to a single 'format + lint' entrypoint per surface.
  - A lightweight pre-commit hook (documented, opt-in) that runs format-check and lint; the same commands are the ones CICD will gate on, so local and CI behaviour match.
- [ ] **Document repo layout, build commands & contribution conventions**
  Author the top-level README and a short CONTRIBUTING note so a new dev can build every surface and knows where new code goes.
  - One-line-per-surface build/serve/run instructions (API, web, both Flutter flavours), and how to build the shared packages.
  - Folder-ownership map: which module/folder a given feature's API code, web screen, app screen and shared component belong in.
  - Branch-naming and commit conventions (the detail of protection rules is GOV's job; this is the human-facing summary).
