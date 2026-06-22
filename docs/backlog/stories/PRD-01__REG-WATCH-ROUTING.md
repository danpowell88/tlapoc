# Reg-watch: role-targeted routing to digest + Follow-ups

> **Epic:** [PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model)](../epics/PRD-01.md)  ·  **Key:** `PRD-01/REG-WATCH-ROUTING`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-01/REG-WATCH`

## Background

As a owner, I want credential expiry alerts routed to the people who can act and tracked to acknowledgement, so that the right person sees each warning and there is a record they actioned it.
Plainly: an expiry alert shouldn't shout at everyone — this routes each credential alert to the people who can act on it (Lead nurse, nurse practitioner, owner), lands it in the owner's 'needs attention' digest and the clinic to-do queue, and audits who acknowledged it. Where it fits: a follow-up to the registration/PII/CPD expiry-alerting core (PRD-01/REG-WATCH) — that story raises the alerts and auto-lapses canInject; this adds where the alerts go and the acknowledge trail. The watch and auto-lapse stay in the core; this is purely the routing/acknowledge layer on top.

## How it works

Credential alerts are role-targeted by concern rather than broadcast: registration / insurance / CPD currency is a Lead / NP (nurse practitioner) / owner concern (the stockAlert / compliance / hr concerns in the persona model), not every RN (registered nurse)'s, so the warning lands with someone who can renew or cover.
Open alerts feed two surfaces — the owner needs-attention digest (PRD-08/ATTENTION-DIGEST) and the unified Follow-ups queue (ADR-0023) as expiry tasks — so an expiry is both visible at a glance and actionable as a job. Acknowledge / dismiss on an alert writes an audit event so there is a record of who saw and actioned each warning, and the whole path is idempotent so a daily re-scan never duplicates an open alert.

## Requirements

- Credential expiry alerts routed to the people who can act and tracked to acknowledgement.

## Acceptance Criteria

- [ ] Alerts are routed by concern (compliance / hr / stockAlert) to Lead / NP / owner — not to every RN.
- [ ] Open alerts project into the owner needs-attention digest (PRD-08/ATTENTION-DIGEST) and as expiry tasks into the Follow-ups queue (ADR-0023).
- [ ] Acknowledge / dismiss writes an audit event (who / when).
- [ ] Routing/acknowledge is idempotent — a re-scan does not duplicate an open alert.

## UI designs / screenshots

- Prototype: the credential alerts surface as amber/red items routed to Lead/NP/owner; an acknowledge/dismiss action on an alert is audited.
- Open alerts mirror into the owner needs-attention digest (PRD-08/ATTENTION-DIGEST) and the Follow-ups queue as expiry tasks.
- Routing is concern-driven (compliance/hr/stockAlert), not every-RN broadcast.

## Suggested data model

- **CredentialAlert (extends PRD-01/REG-WATCH)** — uses existing acknowledged_by / acknowledged_at; routed by concern; projects to ATTENTION-DIGEST + Follow-ups
  - _No new entity — adds the routing/acknowledge layer over the CredentialAlert the core already raises._

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Concern-based routing to digest + Follow-ups**
  Behaviour: route open CredentialAlerts by concern (compliance / hr / stockAlert) to Lead / NP (nurse practitioner) / owner — not every RN (registered nurse) — and project them into the owner needs-attention digest (PRD-08/ATTENTION-DIGEST) and as expiry tasks into the Follow-ups queue (ADR-0023). Requirements: idempotent so a re-scan does not duplicate an open alert; the alert is the prompt to renew, the auto-lapse (REG-WATCH core) is the actual gate.
- [ ] **Audited acknowledge / dismiss**
  Behaviour: acknowledge / dismiss on an alert records who saw and actioned it. Requirements: writes an audit event (actor / when); a dismissed-then-re-raised condition does not create a duplicate open alert.
