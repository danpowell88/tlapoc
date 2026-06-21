# Campaigns (external-tool handoff) (placeholder)

> **Epic:** [PRD-07 — Communications, reminders & recall](../epics/PRD-07.md)  ·  **Key:** `PRD-07/CAMPAIGNS`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 1 pts  ·  **Area:** integration

## Background

As a owner, I want campaign capability, so that I can run promotions.
The prototype shows a Comms → Campaigns screen, but advertising/campaign tooling was withdrawn from scope (ADR-0034 withdrawn) — email campaigns and social belong in the clinic's external tools (Mailchimp, Meta Business Suite). Tracked as a placeholder to reconcile prototype vs scope.

## How it works

Placeholder: advertising/campaign tooling was withdrawn from scope (ADR-0034 withdrawn) — email campaigns and social belong in the clinic's external tools (Mailchimp, Meta Business Suite). The platform may expose consented audience segments for export. Any in-app campaign must honour TGA/AHPRA rules and the no-public-S4-pricing rule (C9).
Tracked to reconcile the prototype's Campaigns screen with the scope cut.

## Requirements

- Campaign capability.
- Deferred (Phase 2+): placeholder, design-only for now.
- Compliance: [C9](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria), [C23](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Placeholder — advertising/campaign content is produced in external tools, not the platform.
- [ ] The platform exposes consented audience export / segments for those tools where appropriate (C23).
- [ ] If ever built in-app, it must honour TGA/AHPRA advertising rules and the no-public-S4-pricing rule (C9).

## UI designs / screenshots

- Prototype: Comms -> Campaigns (marketing-camp.png) exists as a concept; real campaigns run in external tools.

## Suggested data model

- **AudienceSegment (export)** — consented clients matching filters
  - _Export to external tools; no in-app advertising engine._

## Technical notes (high level)

- Stack: Ports-and-adapters integration
- Architecture decisions: [ADR-0034](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-07-comms-reminders-recall.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-07-comms-reminders-recall.md)

## Tasks (dev pickup)

- [ ] **Scope & design when pulled into a sprint** — Deferred placeholder — no build yet.
- [ ] **Confirm it still fits scope / regulatory stance**
