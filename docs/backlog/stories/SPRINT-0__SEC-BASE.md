# Security baseline: encryption, headers, dependency & secret scanning

> **Epic:** [SPRINT-0 — Engineering foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/SEC-BASE`  ·  **Type:** Chore  ·  **Stage:** M0  ·  **Priority:** P0  ·  **Estimate:** 3 pts  ·  **Area:** infra
>
> **Depends on:** `SPRINT-0/CICD`

## Background

As a security-minded engineer, I want TLS everywhere, encryption at rest, hardened HTTP headers, least-privilege identities and dependency/secret/code scanning in CI, so that the platform meets its baseline security obligations from day one.
Encryption in transit + at rest, least-privilege, secure headers and automated scanning establish the security posture the compliance docs assume (C10/C21).

## How it works

All traffic is TLS end to end and data stores are encrypted at rest (Postgres, Blob, Key Vault — much of this is platform-default but is asserted and verified here). The web app sends hardened HTTP security headers (CSP, HSTS, X-Content-Type-Options, frame-ancestors), and CORS is locked down to known origins rather than wildcarded.
CI runs three scan classes and gates merges on high-severity findings: dependency scanning (vulnerable packages), secret scanning (coordinated with SECRETS — no committed secrets), and SAST (static analysis of the code). High-severity findings block the PR, making the security gate enforceable through CICD/GOV rather than advisory.
Service identities follow least-privilege — each service/pipeline uses a scoped managed identity, with no shared admin credentials — so a compromised component has minimal blast radius. The posture (what's encrypted, which headers, which scans, the identity model) is documented as the security baseline the platform builds on.

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

- [ ] **Enforce TLS + encryption at rest, harden HTTP headers and lock down CORS**
  Assert and verify the transport/storage/edge security baseline.
  - TLS on all traffic; encryption at rest verified on Postgres, Blob and Key Vault (coordinate with IAC defaults).
  - Security headers on web: CSP, HSTS, X-Content-Type-Options, frame-ancestors, referrer policy.
  - CORS restricted to known origins (no wildcard); document the allowed-origin list per environment.
- [ ] **Add dependency, secret and SAST scanning to CI and gate merges on high-severity findings**
  Make the security scans blocking through the pipeline.
  - Dependency scanning (vulnerable packages), secret scanning (coordinated with SECRETS), and SAST stages in CI.
  - High-severity findings fail the PR (GOV marks these required); documented triage/suppression process for false positives.
  - Runs across all surfaces (.NET, Angular, Flutter).
- [ ] **Apply least-privilege service identities and document the security baseline**
  Minimise blast radius and write down the posture.
  - Each service/pipeline uses a scoped managed identity; no shared admin credentials anywhere (ties to SECRETS/IAC).
  - Document the baseline: what's encrypted, which headers, the scan suite + gates, the identity model — the reference the platform's security posture is measured against (C10/C21/ADR-0016).
