# Cloud environments & infrastructure-as-code (AU East)

> **Epic:** [SPRINT-0 — Engineering foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/IAC`  ·  **Type:** Chore  ·  **Stage:** M0  ·  **Priority:** P0  ·  **Estimate:** 3 pts  ·  **Area:** infra

## Background

As a platform engineer, I want dev, staging and prod environments provisioned via IaC, all pinned to Australia East, so that data residency is guaranteed and environments are reproducible.
Still in Sprint 0 (setup): this story defines the cloud environments — dev, staging and production — as code, so they are built the same way every time and provably keep all personal and health data inside Australia. It is the ground the platform stands on: the database, the secret vault, media storage and the deploy pipeline are all provisioned into the environments described here, and a later compliance story (RESIDENCY) audits what this pins.  All PII/PHI must resolve to Australia East (C21/ADR-0016). Defining dev/staging/prod as code makes residency, isolation and reproducibility provable.

## How it works

Azure resources (ADR-0001) are declared as code — compute (Container Apps / App Service for the API + web), Azure Database for PostgreSQL Flexible Server (ADR-0002), Blob storage, Key Vault, networking and the observability workspace — parameterised per environment so dev/staging/prod are the same definition with different inputs. Every PII/PHI-bearing resource is pinned to Australia East.
A residency policy check is part of the pipeline: a resource declaring any non-AU region for a data-bearing service fails the IaC plan/validation step before anything is created (Azure Policy / a deny rule plus a plan-time assertion). This is the mechanism that makes ADR-0016 enforceable rather than a comment in a doc.
Environments are fully isolated — separate data stores, separate Key Vault, separate managed identities and separate networking per environment — so a credential or query in one environment can never reach another. Non-prod environments are disposable: a single command tears down and recreates dev or staging from the same definitions, which keeps them cheap and keeps drift out.

## Requirements

- Dev, staging and prod environments provisioned via IaC, all pinned to Australia East.
- Compliance: [C21](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] IaC provisions compute, Postgres, blob storage and networking in Australia East for each environment.
- [ ] A non-AU region for any PII/PHI resource fails the IaC policy check.
- [ ] Environments are isolated (separate data stores, secrets, identities).
- [ ] Tear-down/re-create of a non-prod environment is a single command.

## Suggested data model

- **(infra) Environment** — name(dev|staging|prod), region=AustraliaEast, isolated dataStore/keyVault/identity/network
  - _Same IaC definition per environment, different parameters; residency pinned and policy-enforced._

## Technical notes (high level)

- Architecture decisions: [ADR-0001](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md), [ADR-0016](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Author the IaC modules for the AU-East environment stack**
  Declare the full per-environment Azure stack as parameterised, reusable modules so dev/staging/prod differ only by inputs.
  - Modules: compute (API + web hosting), Postgres Flexible Server, Blob storage, Key Vault, networking, observability workspace.
  - Every data-bearing resource pinned to Australia East; region is a guarded parameter, not a free string.
  - Isolation by construction: each environment gets its own data store, vault, managed identities and network — no shared resources across environments.
  - Outputs (connection endpoints, identity ids, vault uri) are consumed by DB, SECRETS, MEDIA-STORAGE and CICD rather than hand-copied.
- [ ] **Enforce the AU residency policy and make non-prod disposable**
  Make residency a hard gate and make tearing down non-prod a one-liner.
  - A plan/validation-time assertion plus an Azure Policy deny rule: any PII/PHI resource declaring a non-AU region fails before provisioning (the test that proves ADR-0016).
  - A single command provisions, and a single command tears down + recreates, a non-prod environment from the same definitions.
  - State management and naming conventions so environments never collide; document the residency exception process (there is none for v1 — it simply fails).
- [ ] **Wire provisioning into CI/CD and document environment topology**
  Make environment changes go through the pipeline, and document the topology so on-call and PRD-01/RESIDENCY can audit it.
  - Plan-on-PR / apply-on-merge for infra changes, with the residency check as a blocking step (ties into CICD).
  - A diagram of the three environments, their isolated resources and the AU-East pinning.
  - How to read the policy-check output and what 'provable residency' means for the RESIDENCY register later.
