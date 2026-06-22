# Credentials: AHPRA PIE register auto-verification

> **Epic:** [PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model)](../epics/PRD-01.md)  ·  **Key:** `PRD-01/CREDENTIALS-PIE`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-01/CREDENTIALS`

## Background

As a owner, I want to auto-verify a practitioner's AHPRA registration against the AHPRA PIE register, so that registration currency is confirmed from the source, not just keyed in by hand.
Plainly: a verify button on each credential that checks the practitioner's registration straight against the AHPRA (Australian Health Practitioner Regulation Agency) register over its Practitioner Information Exchange (PIE) lookup, instead of someone confirming it by hand. Where it fits: a follow-up to the staff-credentials core (PRD-01/CREDENTIALS) — that story ships with a first-class manual-verify (a recorded verified-on date); this adds the automated AHPRA lookup on top, while keeping the manual fallback always present. The register status pulled by PIE feeds the same canInject gate the core derives, so a PIE-pulled lapse blocks injecting exactly like a manual one.

## How it works

AHPRA register auto-verification via the Practitioner Information Exchange (PIE — the AHPRA Practitioner Information Exchange register lookup) lets a verify action on a registration credential confirm the practitioner's number, type and status directly against the AHPRA register rather than relying on a hand-keyed entry. On success it stamps verified_method=pie and verified_on so the record shows it was machine-verified and when.
PIE is approval-gated SOAP, so it is treated as best-effort: the first-class manual-verify path from the core (PRD-01/CREDENTIALS) — storing verified_method=manual + verified_on — is always present as a fallback when PIE is unavailable or not approved for the tenant. A status change pulled from PIE (e.g. lapsed or suspended) is treated exactly like any other credential change: it feeds the canInject (the single derived gate deciding whether a clinician may inject right now) derivation owned by CREDENTIALS, so a PIE-pulled lapse blocks injecting automatically.
The verify action is gated to owner/lead (team:manage) and every verify (PIE or manual) is audited so there is a record of who confirmed each registration and how.

## Requirements

- To auto-verify a practitioner's AHPRA registration against the AHPRA PIE register.

## Acceptance Criteria

- [ ] A verify action on a registration credential attempts AHPRA PIE auto-verification where approved and records verified_method=pie + verified_on.
- [ ] PIE is treated as best-effort: the first-class manual-verify (verified_method=manual + verified_on) is always available as a fallback.
- [ ] A status pulled from PIE (current / lapsed / suspended) feeds the canInject derivation (CREDENTIALS) like any other credential change.
- [ ] The verify action is gated to owner/lead (team:manage) and audited.

## UI designs / screenshots

- Prototype: Team → People & credentials (team-people.png) — the per-credential verify action with a PIE auto-verify attempt and a manual-verify fallback storing a verified-on date.
- On the credential detail view, the verify control shows the last verified method (PIE / manual) and verified-on date; a failed PIE attempt falls back to manual without losing the action.
- Gated to owner/lead (team:manage); the verify writes an audit entry.

## Suggested data model

- **Credential (extends PRD-01/CREDENTIALS)** — uses existing verified_method(pie|manual) + verified_on
  - _No new entity — this story wires the PIE auto-verify path onto the existing Credential.verified_method/verified_on; the manual path is already in the core._

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **AHPRA PIE auto-verify path with manual fallback**
  Behaviour: a verify action on a registration credential that attempts AHPRA (Australian Health Practitioner Regulation Agency) PIE (the AHPRA Practitioner Information Exchange register lookup) auto-verification where approved, falling back to the first-class manual-verify (from CREDENTIALS) when PIE is unavailable or not approved. Requirements: PIE is approval-gated SOAP — treat as best-effort; record verified_method (pie|manual) + verified_on either way; the verify action is gated to owner/lead (team:manage) and audited.
- [ ] **Feed PIE-pulled status into canInject**
  Behaviour: a status pulled from PIE (current / lapsed / suspended) updates the registration credential and feeds the canInject (the single derived cleared-to-inject gate) derivation owned by CREDENTIALS, so a PIE-pulled lapse or suspension blocks injecting automatically. Requirements: treat a PIE status change exactly like any other credential change (recompute canInject); no separate gate — this story only supplies a fresher status to the existing derivation.
