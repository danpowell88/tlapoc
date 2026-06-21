# Cloud environments & infrastructure-as-code (AU East)

> **Epic:** [SPRINT-0 — Engineering foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/IAC`  ·  **Type:** Chore  ·  **Stage:** M0  ·  **Priority:** P0  ·  **Estimate:** 3 pts  ·  **Area:** infra

## Background

As a platform engineer, I want dev, staging and prod environments provisioned via IaC, all pinned to Australia East, so that data residency is guaranteed and environments are reproducible.
All PII/PHI must resolve to Australia East (C21/ADR-0016). Defining dev/staging/prod as code makes residency, isolation and reproducibility provable.

## How it works

dev/staging/prod provisioned as code, all pinned to Australia East so data residency (C21/ADR-0016) is provable and reproducible. A non-AU region for any PII/PHI resource fails the IaC policy check; environments are isolated and a non-prod env can be torn down/recreated with one command.

## Requirements

- Dev, staging and prod environments provisioned via IaC, all pinned to Australia East.
- Compliance: [C21](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] IaC provisions compute, Postgres, blob storage and networking in Australia East for each environment.
- [ ] A non-AU region for any PII/PHI resource fails the IaC policy check.
- [ ] Environments are isolated (separate data stores, secrets, identities).
- [ ] Tear-down/re-create of a non-prod environment is a single command.

## Suggested data model

- **(infra) Environment** — region=AustraliaEast, isolated data store/secrets/identity per env
  - _Residency policy enforced in IaC._

## Technical notes (high level)

- Stack: Azure / CI-CD / IaC
- Architecture decisions: [ADR-0001](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md), [ADR-0016](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Implement: Cloud environments & infrastructure-as-code (AU East)**
- [ ] **Wire into CI/CD + per-environment config**
- [ ] **Document setup & usage**
- [ ] **Validate in dev + add a smoke test**
