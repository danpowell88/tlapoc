# Media storage & signed-URL service

> **Epic:** [SPRINT-0 — Engineering foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/MEDIA-STORAGE`  ·  **Type:** Chore  ·  **Stage:** M0  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** backend, infra
>
> **Depends on:** `SPRINT-0/IAC`, `SPRINT-0/API`

## Background

As a backend developer, I want a media service for encrypted AU-resident blob storage with signed-URL upload/download, so that photos/documents are stored and served securely and consistently.
Clinical photos and documents must be stored centrally in AU, served via short-lived signed URLs, and never persisted on personal devices (C14/ADR-0009). A shared media service underpins PRD-05 photos and PRD-09 capture.

## How it works

A media service: AU-resident, encrypted blob storage served only via short-lived signed URLs, with consent- and capability-checked, audited access and no public/unsigned path (C14/C21/ADR-0009/0016). Underpins PRD-05 photos and PRD-09 capture — media is never persisted on personal devices.

## Requirements

- A media service for encrypted AU-resident blob storage with signed-URL upload/download.
- Compliance: [C14](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria), [C21](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Blob storage is AU-resident and encrypted at rest; access is via short-lived signed URLs only.
- [ ] Upload + download flows are demonstrated from web and Flutter.
- [ ] Media access is consent- and capability-checked and audited.
- [ ] No public/unsigned access to media is possible.

## Suggested data model

- **MediaObject** — id, tenant_id, owner_ref, blob_path(AU), content_type, created_at; access via signed URL only
  - _No public access; consent/capability-checked._

## Technical notes (high level)

- Architecture decisions: [ADR-0009](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md), [ADR-0016](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Implement: Media storage & signed-URL service**
- [ ] **Wire into CI/CD + per-environment config**
- [ ] **Document setup & usage**
