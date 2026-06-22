# Secrets & configuration management

> **Epic:** [SPRINT-0 — Engineering foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/SECRETS`  ·  **Type:** Chore  ·  **Stage:** M0  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** infra
>
> **Depends on:** `SPRINT-0/IAC`

## Background

As a platform engineer, I want a managed secret store (Key Vault) wired into each environment and a typed config story for the API and apps, so that no secret is ever committed and rotation is possible.
Connection strings, provider keys (Square, SMS, Xero) and signing secrets must live in a managed vault, never in code or config files.

## How it works

A managed secret store (Key Vault) wired into each environment with typed, environment-specific config that fails fast on missing required values; a secret-scanning check fails the build on a committed secret. No secret ever in source control; rotation needs no code change.

## Requirements

- A managed secret store (Key Vault) wired into each environment and a typed config story for the API and apps.

## Acceptance Criteria

- [ ] API and pipelines read secrets from the vault per environment; none in source control.
- [ ] A secret-scanning check fails the build on a committed secret.
- [ ] Config is environment-specific and typed; missing required config fails fast at startup.
- [ ] Rotating a secret requires no code change.

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Implement: Secrets & configuration management**
  Deliver per the acceptance criteria:
  - API and pipelines read secrets from the vault per environment; none in source control.
  - A secret-scanning check fails the build on a committed secret.
  - Config is environment-specific and typed; missing required config fails fast at startup.
  - Rotating a secret requires no code change.
- [ ] **Wire into CI/CD + per-environment config**
  Build/test/deploy steps + env-specific config & secrets; required for merge.
- [ ] **Document setup & usage**
  How to run/operate it; runbook notes for the team.
