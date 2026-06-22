# Secrets & configuration management

> **Epic:** [SPRINT-0 — Engineering foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/SECRETS`  ·  **Type:** Chore  ·  **Stage:** M0  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** infra
>
> **Depends on:** `SPRINT-0/IAC`

## Background

As a platform engineer, I want a managed secret store (Key Vault) wired into each environment and a typed config story for the API and apps, so that no secret is ever committed and rotation is possible.
Sprint 0 (setup), security baseline: this gives every environment a managed vault for its secrets — database passwords, payment/SMS/accounting keys, signing keys — so nothing sensitive is ever stored in the code, and a key can be rotated without a code change. It builds on the cloud environments (which provision the vault) and feeds the database, sign-in, the deploy pipeline and every external integration; a commit-time scan enforces the no-secrets-in-code rule. Connection strings, provider keys (Square, SMS, Xero) and signing secrets must live in a managed vault, never in code or config files.

## How it works

Each environment has its own Azure Key Vault (provisioned by IAC). The API and pipelines read secrets from the vault at runtime/deploy via managed identity — no secret is in source control, ever. A secret-scanning check in CI (continuous integration) fails the build if a secret is committed, so the rule is enforced, not trusted.
Configuration is environment-specific and strongly typed: the API binds config to typed options and validates required values at startup, so a missing or malformed required setting fails fast (the app refuses to start) rather than failing mysteriously at first use. Non-secret config lives in environment settings; secrets are referenced by vault key.
Rotation requires no code change: rotating a secret in the vault is picked up by the running services (cached with a bounded refresh), so a leaked or expiring key is swapped operationally. The split — typed config for shape, vault for secret values, scanning to keep them out of git — is documented so module authors add new secrets the same way.

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

- [ ] **Wire per-environment Key Vault into the API and provide typed, fail-fast config**
  Make the vault the only home for secrets and make config validate at startup.
  - API + pipelines read secrets from the per-environment Key Vault (IAC) via managed identity; nothing secret in source control.
  - Config bound to typed options with required-value validation at startup — a missing/invalid required setting fails fast (app won't start).
  - Non-secret config in environment settings; secret values referenced by vault key; rotation in the vault needs no code change (bounded cache refresh).
- [ ] **Add the secret-scanning gate and per-environment config to CI/CD**
  Enforce 'no committed secrets' and select the right config/secrets per deploy (add the secret-scanning gate to CI/CD — continuous integration / continuous delivery).
  - A secret-scanning check in CI (continuous integration) that fails the build on a committed secret (coordinated with SEC-BASE's scan suite).
  - Deploy jobs select per-environment config and vault references so a deploy never crosses environments (ties to CICD/IAC).
  - Vault access via least-privilege managed identities (no shared admin credentials).
- [ ] **Document the secrets & configuration model and how to add a new secret**
  Write the config/secrets guide so the pattern is followed consistently.
  - The split: typed config for shape, vault for secret values, scanning to keep them out of git.
  - How to add a new secret (vault key naming, typed-option binding, required-value validation) and how rotation works without code change.
  - The list of secret categories (DB connection, Entra/External ID provider creds, Square (the payment provider)/SMS (short message service)/Xero (the accounting system) keys, signing secrets) and where each lives.
