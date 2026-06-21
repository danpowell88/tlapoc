# Security baseline: encryption, headers, dependency & secret scanning

> **Epic:** [SPRINT-0 — Sprint 0 — Foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/SEC-BASE`  ·  **Type:** Chore  ·  **Stage:** M0  ·  **Priority:** P0  ·  **Estimate:** 3 pts  ·  **Area:** infra
>
> **Depends on:** `SPRINT-0/CICD`

## Background

Sprint 0 — Foundations & setup — Everything the team needs in place before feature work begins: repositories and solution structure, CI/CD, cloud environments in Australia East, identity wiring for staff and clients, the Postgres + RLS data baseline, the API/web/app shells, a shared design system, observability, a security baseline, and the four de-risk spikes called out in the docs index.

As a security-minded engineer, I want TLS everywhere, encryption at rest, hardened HTTP headers, least-privilege identities and dependency/secret/code scanning in CI, so that the platform meets its baseline security obligations from day one.

Encryption in transit + at rest, least-privilege, secure headers and automated scanning establish the security posture the compliance docs assume (C10/C21).

## Requirements

- TLS everywhere, encryption at rest, hardened HTTP headers, least-privilege identities and dependency/secret/code scanning in CI.
- Must satisfy compliance obligation(s): C10, C21.

## Acceptance Criteria

- [ ] All traffic is TLS; data stores are encrypted at rest.
- [ ] Security headers (CSP, HSTS, etc.) applied to web; CORS locked down.
- [ ] Dependency, secret and SAST scans run in CI and gate merges on high-severity findings.
- [ ] Service identities follow least-privilege; no shared admin credentials.

## UI designs / screenshots

Non-UI / platform scaffolding — no prototype screen.

## Technical notes (high level)

Stack: Azure / CI-CD / IaC.
Architecture decisions: ADR-0016 (see docs/adr/decision-log.md).
Depends on: SPRINT-0/CICD.

## Other

Epic: SPRINT-0 — Sprint 0 — Foundations & setup.
Source PRD: docs/prds/PRD-01-foundations-tenancy.md.
Backlog key: SPRINT-0/SEC-BASE.
Phase: 0 · Priority: P0 · Estimate: 3 pts.
Compliance criteria: C10, C21.

## Tasks (dev pickup)

- [ ] **Implement: Security baseline: encryption, headers, dependency & secret scanning**
- [ ] **Wire into CI/CD + per-environment config**
- [ ] **Document setup & usage**
- [ ] **Validate in dev + add a smoke test**
