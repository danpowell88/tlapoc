# Media storage & signed-URL service

> **Epic:** [SPRINT-0 — Engineering foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/MEDIA-STORAGE`  ·  **Type:** Chore  ·  **Stage:** M0  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** backend, infra
>
> **Depends on:** `SPRINT-0/IAC`, `SPRINT-0/API`

## Background

As a backend developer, I want a media service for encrypted AU-resident blob storage with signed-URL upload/download, so that photos/documents are stored and served securely and consistently.
Clinical photos and documents must be stored centrally in AU, served via short-lived signed URLs, and never persisted on personal devices (C14/ADR-0009). A shared media service underpins PRD-05 photos and PRD-09 capture.

## How it works

Blob storage is AU-resident and encrypted at rest (IAC), and there is no public or unsigned access path — every read and write goes through a short-lived signed URL minted by the service. Clients (web and Flutter) request a signed URL, upload directly to Blob (so large media doesn't stream through the API), and download the same way; the URL expires quickly so a leaked link is short-lived.
Minting a signed URL is consent- and capability-checked and audited: the service verifies the caller has the capability and that image-use consent permits the access (ADR-0009, C14) before issuing the URL, and records an AuditEvent (who accessed which media, when) so media access is part of the trail. A MediaObject row holds the metadata (owner ref, content type, blob path) — access is always via signed URL, never a stored public link.
Upload and download are demonstrated from both web and Flutter to prove the round-trip. The device-side guarantee (no persistence beyond a transient encrypted cache, ADR-0009) is the provider app's responsibility (SPIKE-OFFLINE proved the pattern); this service guarantees the central, residency-correct, signed-only, audited storage.

## Requirements

- A media service for encrypted AU-resident blob storage with signed-URL upload/download.
- Compliance: [C14](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria), [C21](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Blob storage is AU-resident and encrypted at rest; access is via short-lived signed URLs only.
- [ ] Upload + download flows are demonstrated from web and Flutter.
- [ ] Media access is consent- and capability-checked and audited.
- [ ] No public/unsigned access to media is possible.

## Suggested data model

- **MediaObject** — id, tenant_id, owner_ref, blob_path(AU), content_type, created_at; consent_ref
  - _Access via short-lived signed URL only; no public/unsigned path; mint is consent/capability-checked and audited (ADR-0009/C14)._

## Technical notes (high level)

- Architecture decisions: [ADR-0009](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md), [ADR-0016](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Build the signed-URL upload/download service over AU-resident encrypted Blob**
  Provide secure, residency-correct media handling with no public access.
  - AU-resident, encrypted-at-rest Blob (IAC); every read/write via a short-lived signed URL minted by the service — no public/unsigned path.
  - Direct-to-Blob upload/download (large media doesn't stream through the API); URLs expire quickly.
  - A MediaObject row holds metadata; access is always via signed URL, never a stored public link.
- [ ] **Gate signed-URL minting on consent + capability and audit every access**
  Make media access governed and traceable.
  - Before issuing a URL, verify the caller's capability AND that image-use consent permits the access (ADR-0009, C14).
  - Record an AuditEvent (who/what media/when) on access via AUDIT-INFRA so media reads are in the trail.
  - Demonstrate upload + download from both web and Flutter.
- [ ] **Document the media service and the device non-retention contract**
  Write the guide PRD-05/09 build on.
  - How to request signed URLs, the consent/capability/audit gating, and the no-public-access rule.
  - The device-side guarantee (no persistence beyond a transient encrypted cache, purge after sync) that the provider app must honour — proven by SPIKE-OFFLINE — and how it uploads through this service.
