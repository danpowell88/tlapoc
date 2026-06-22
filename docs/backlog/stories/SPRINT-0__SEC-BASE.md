# Security baseline: encryption, headers, dependency & secret scanning

> **Epic:** [SPRINT-0 — Engineering foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/SEC-BASE`  ·  **Type:** Chore  ·  **Stage:** M0  ·  **Priority:** P0  ·  **Estimate:** 3 pts  ·  **Area:** infra
>
> **Depends on:** `SPRINT-0/CICD`

## Background

As a security-minded engineer, I want TLS everywhere, encryption at rest, hardened HTTP headers, least-privilege identities and dependency/secret/code scanning in CI, so that the platform meets its baseline security obligations from day one.
Encryption in transit + at rest, least-privilege, secure headers and automated scanning establish the security posture the compliance docs assume (C10/C21).

## How it works

The baseline security posture: TLS everywhere, encryption at rest, hardened HTTP headers (CSP/HSTS), locked-down CORS, least-privilege service identities, and dependency/secret/SAST scanning in CI gating merges on high-severity findings (C10/C21/ADR-0016).

## Requirements

- TLS everywhere, encryption at rest, hardened HTTP headers, least-privilege identities and dependency/secret/code scanning in CI.
- Compliance: [C10](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria), [C21](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] All traffic is TLS; data stores are encrypted at rest.
- [ ] Security headers (CSP, HSTS, etc.) applied to web; CORS locked down.
- [ ] Dependency, secret and SAST scans run in CI and gate merges on high-severity findings.
- [ ] Service identities follow least-privilege; no shared admin credentials.

## Technical notes (high level)

- Architecture decisions: [ADR-0016](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Implement: Security baseline: encryption, headers, dependency & secret scanning**
  Deliver per the acceptance criteria:
  - All traffic is TLS; data stores are encrypted at rest.
  - Security headers (CSP, HSTS, etc.) applied to web; CORS locked down.
  - Dependency, secret and SAST scans run in CI and gate merges on high-severity findings.
  - Service identities follow least-privilege; no shared admin credentials.
- [ ] **Wire into CI/CD + per-environment config**
  Build/test/deploy steps + env-specific config & secrets; required for merge.
- [ ] **Document setup & usage**
  How to run/operate it; runbook notes for the team.
