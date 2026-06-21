# App distribution & code-push posture

> **Epic:** [PRD-09 — Apps (Flutter): client & provider](../epics/PRD-09.md)  ·  **Key:** `PRD-09/APP-DISTRIBUTION`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** client-app, provider-app
>
> **Depends on:** `SPRINT-0/FLUTTER`

## Background

As a mobile developer, I want a store-distribution and (where viable) code-push pipeline for both apps, so that we can ship and patch the apps responsibly.
Store distribution + code-push (e.g. Shorebird) where the compliance posture allows (open question) (ADR-0006).

## How it works

Store distribution + (where the compliance posture allows) code-push (e.g. Shorebird) for both Flutter apps from CI, with versioning + minimum-supported-version handling and crash/usage telemetry into observability (ADR-0006).
Lets the clinic ship and responsibly patch the apps.

## Requirements

- A store-distribution and (where viable) code-push pipeline for both apps.

## Acceptance Criteria

- [ ] Both apps distribute via internal/store channels from CI.
- [ ] Code-push viability for the compliance posture is assessed and documented.
- [ ] Versioning + minimum-supported-version handling in place.
- [ ] Crash/usage telemetry feeds observability.

## UI designs / screenshots

_Prototype screen: client-app.html, treatment-room.html, checkin.html, backroom.html._

- No in-app screen — release pipeline + an in-app 'update required' gate for unsupported versions.

## Suggested data model

- **AppRelease** — platform, version, min_supported, channel, code_push_ref?
  - _Code-push viability assessed for compliance._

## Technical notes (high level)

- Architecture decisions: [ADR-0006](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-09-apps-client-provider.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-09-apps-client-provider.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations** — Entities/columns + relationships; tenant_id + RLS.
- [ ] **Backend: domain logic, rules & API endpoint(s)** — Behaviour + invariants + the OpenAPI contract the UI/clients consume.
- [ ] **Client app UI (Flutter)**
- [ ] **Provider app UI (Flutter)**
