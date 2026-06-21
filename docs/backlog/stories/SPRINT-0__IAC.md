# Cloud environments & infrastructure-as-code (AU East)

> **Epic:** [SPRINT-0 — Sprint 0 — Foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/IAC`  ·  **Type:** Chore  ·  **Stage:** M0  ·  **Priority:** P0  ·  **Estimate:** 3 pts  ·  **Area:** infra

## Background

Sprint 0 — Foundations & setup — Everything the team needs in place before feature work begins: repositories and solution structure, CI/CD, cloud environments in Australia East, identity wiring for staff and clients, the Postgres + RLS data baseline, the API/web/app shells, a shared design system, observability, a security baseline, and the four de-risk spikes called out in the docs index.

As a platform engineer, I want dev, staging and prod environments provisioned via IaC, all pinned to Australia East, so that data residency is guaranteed and environments are reproducible.

All PII/PHI must resolve to Australia East (C21/ADR-0016). Defining dev/staging/prod as code makes residency, isolation and reproducibility provable.

## Requirements

- Dev, staging and prod environments provisioned via IaC, all pinned to Australia East.
- Must satisfy compliance obligation(s): C21.

## Acceptance Criteria

- [ ] IaC provisions compute, Postgres, blob storage and networking in Australia East for each environment.
- [ ] A non-AU region for any PII/PHI resource fails the IaC policy check.
- [ ] Environments are isolated (separate data stores, secrets, identities).
- [ ] Tear-down/re-create of a non-prod environment is a single command.

## UI designs / screenshots

Non-UI / platform scaffolding — no prototype screen.

## Technical notes (high level)

Stack: Azure / CI-CD / IaC.
Architecture decisions: ADR-0001, ADR-0016 (see docs/adr/decision-log.md).

## Other

Epic: SPRINT-0 — Sprint 0 — Foundations & setup.
Source PRD: docs/prds/PRD-01-foundations-tenancy.md.
Backlog key: SPRINT-0/IAC.
Phase: 0 · Priority: P0 · Estimate: 3 pts.
Compliance criteria: C21.

## Tasks (dev pickup)

- [ ] **Implement: Cloud environments & infrastructure-as-code (AU East)**
- [ ] **Wire into CI/CD + per-environment config**
- [ ] **Document setup & usage**
- [ ] **Validate in dev + add a smoke test**
