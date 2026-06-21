# Media storage & signed-URL service

> **Epic:** [SPRINT-0 — Sprint 0 — Foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/MEDIA-STORAGE`  ·  **Type:** Chore  ·  **Stage:** M0  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** backend, infra
>
> **Depends on:** `SPRINT-0/IAC`, `SPRINT-0/API`

## Background

Sprint 0 — Foundations & setup — Everything the team needs in place before feature work begins: repositories and solution structure, CI/CD, cloud environments in Australia East, identity wiring for staff and clients, the Postgres + RLS data baseline, the API/web/app shells, a shared design system, observability, a security baseline, and the four de-risk spikes called out in the docs index.

As a backend developer, I want a media service for encrypted AU-resident blob storage with signed-URL upload/download, so that photos/documents are stored and served securely and consistently.

Clinical photos and documents must be stored centrally in AU, served via short-lived signed URLs, and never persisted on personal devices (C14/ADR-0009). A shared media service underpins PRD-05 photos and PRD-09 capture.

## Requirements

- A media service for encrypted AU-resident blob storage with signed-URL upload/download.
- Must satisfy compliance obligation(s): C14, C21.

## Acceptance Criteria

- [ ] Blob storage is AU-resident and encrypted at rest; access is via short-lived signed URLs only.
- [ ] Upload + download flows are demonstrated from web and Flutter.
- [ ] Media access is consent- and capability-checked and audited.
- [ ] No public/unsigned access to media is possible.

## UI designs / screenshots

Non-UI / platform scaffolding — no prototype screen.

## Technical notes (high level)

Stack: .NET API (domain/services); Azure / CI-CD / IaC.
Architecture decisions: ADR-0009, ADR-0016 (see docs/adr/decision-log.md).
Depends on: SPRINT-0/IAC, SPRINT-0/API.

## Other

Epic: SPRINT-0 — Sprint 0 — Foundations & setup.
Source PRD: docs/prds/PRD-01-foundations-tenancy.md.
Backlog key: SPRINT-0/MEDIA-STORAGE.
Phase: 0 · Priority: P1 · Estimate: 3 pts.
Compliance criteria: C14, C21.

## Tasks (dev pickup)

- [ ] **Implement: Media storage & signed-URL service**
- [ ] **Wire into CI/CD + per-environment config**
- [ ] **Document setup & usage**
- [ ] **Validate in dev + add a smoke test**
