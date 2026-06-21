# Secrets & configuration management

> **Epic:** [SPRINT-0 — Sprint 0 — Foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/SECRETS`  ·  **Type:** Chore  ·  **Stage:** M0  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** infra
>
> **Depends on:** `SPRINT-0/IAC`

## Background

Sprint 0 — Foundations & setup — Everything the team needs in place before feature work begins: repositories and solution structure, CI/CD, cloud environments in Australia East, identity wiring for staff and clients, the Postgres + RLS data baseline, the API/web/app shells, a shared design system, observability, a security baseline, and the four de-risk spikes called out in the docs index.

As a platform engineer, I want a managed secret store (Key Vault) wired into each environment and a typed config story for the API and apps, so that no secret is ever committed and rotation is possible.

Connection strings, provider keys (Square, SMS, Xero) and signing secrets must live in a managed vault, never in code or config files.

## Requirements

- A managed secret store (Key Vault) wired into each environment and a typed config story for the API and apps.

## Acceptance Criteria

- [ ] API and pipelines read secrets from the vault per environment; none in source control.
- [ ] A secret-scanning check fails the build on a committed secret.
- [ ] Config is environment-specific and typed; missing required config fails fast at startup.
- [ ] Rotating a secret requires no code change.

## UI designs / screenshots

Non-UI / platform scaffolding — no prototype screen.

## Technical notes (high level)

Stack: Azure / CI-CD / IaC.
Depends on: SPRINT-0/IAC.

## Other

Epic: SPRINT-0 — Sprint 0 — Foundations & setup.
Source PRD: docs/prds/PRD-01-foundations-tenancy.md.
Backlog key: SPRINT-0/SECRETS.
Phase: 0 · Priority: P1 · Estimate: 3 pts.

## Tasks (dev pickup)

- [ ] **Implement: Secrets & configuration management**
- [ ] **Wire into CI/CD + per-environment config**
- [ ] **Document setup & usage**
- [ ] **Validate in dev + add a smoke test**
