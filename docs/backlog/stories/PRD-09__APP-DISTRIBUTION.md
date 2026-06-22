# App distribution & code-push posture

> **Epic:** [PRD-09 — Apps (Flutter): client & provider](../epics/PRD-09.md)  ·  **Key:** `PRD-09/APP-DISTRIBUTION`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** client-app, provider-app
>
> **Depends on:** `SPRINT-0/FLUTTER`

## Background

As a mobile developer, I want a store-distribution and (where viable) code-push pipeline for both apps, so that we can ship and patch the apps responsibly.
Store distribution + code-push (e.g. Shorebird) where the compliance posture allows (open question) (ADR-0006).

## How it works

Store/internal distribution from CI for both Flutter flavours, with versioning + minimum-supported-version handling and an in-app 'update required' gate (enforced server-side too). Code-push (e.g. Shorebird) viability is assessed and documented against the compliance posture (open question — likely OK for the client app, constrained for the clinical provider app). Crash/usage telemetry feeds observability (ADR-0006).
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

- No in-app feature screen — release pipeline + an in-app 'update required' gate for unsupported versions.

## Suggested data model

- **AppRelease** — platform, version, min_supported, channel, code_push_ref?
  - _Code-push viability assessed for the compliance posture._

## Technical notes (high level)

- Architecture decisions: [ADR-0006](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-09-apps-client-provider.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-09-apps-client-provider.md)

## Tasks (dev pickup)

- [ ] **CI distribution pipeline for both app flavours**
  Build + sign both Flutter flavours in CI and distribute to internal then store channels (TestFlight / Play internal → store). Per-store signing and secrets handling.
- [ ] **Versioning + minimum-supported-version + 'update required' gate**
  Stamp each release with a version and a minimum-supported-version. In-app 'update required' gate blocks unsupported builds; enforce the floor server-side too (API rejects unsupported clients) so the gate can't be skipped.
- [ ] **Assess + document code-push (Shorebird) compliance viability**
  Assess Shorebird/code-push against the compliance posture and document the decision per flavour: likely acceptable for the client app, constrained for the clinical provider app (OTA Dart changes to a clinical record surface). Record the outcome (open question in the PRD), don't assume it.
- [ ] **Crash + usage telemetry into observability**
  Wire crash and usage telemetry from both apps into the platform observability stack so regressions and adoption are visible. Respect the privacy posture (no PHI in telemetry).
