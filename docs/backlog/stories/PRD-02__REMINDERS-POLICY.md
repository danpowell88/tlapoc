# Reminders: cancellation / no-show policy settings

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/REMINDERS-POLICY`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-02/REMINDERS`

## Background

As a owner / manager, I want to configure the cancellation window and no-show rule, so that self-service reschedule/cancel and no-show handling follow our policy.
Plainly: the per-tenant settings that define the cancellation window, the no-show rule, and whether self-service reschedule is allowed. Where it fits: a follow-up to the reminders basic scheduling & dispatch (PRD-02/REMINDERS) that adds the policy these behaviours read. It is the source of truth the self-service endpoints (PRD-02/REMINDERS-SELF-SERVICE) enforce and is surfaced to the client at confirm time (ties to PRD-02/BOOKING-WIZARD). There is no auto-charge in v1. It sits in Reception (PRD-02).

## How it works

The basic story schedules reminders; this follow-up owns the cancellation/no-show policy those self-service behaviours depend on. A per-tenant settings screen configures the cancellation window_hours, the no_show_rule, and allow_self_reschedule.
Settings validate and persist, and surface the plain-language 'no auto-charge in v1' note so the owner understands there is no deposit/charge mechanism in this version.
The policy is shown to the client at confirm time (ties to PRD-02/BOOKING-WIZARD's confirmation step) and is the single source of truth the self-service reschedule/cancel endpoints (PRD-02/REMINDERS-SELF-SERVICE) enforce.

## Requirements

- To configure the cancellation window and no-show rule.

## Acceptance Criteria

- [ ] A per-tenant settings screen configures window_hours, no_show_rule and allow_self_reschedule.
- [ ] Settings validate and persist.
- [ ] The plain-language 'no auto-charge in v1' note is surfaced.
- [ ] The policy is shown to the client at confirm time and is the source of truth the self-service endpoints enforce.

## UI designs / screenshots

- Settings: cancellation/no-show policy (window hours, rule, allow self-reschedule); v1 states 'no auto-charge'.
- The policy is shown to the client at confirm time (booking-wizard.png confirmation step).
- Validated and persisted per tenant.

![schedule — prototype screen](../screens/schedule.png)

## Suggested data model

- **CancellationPolicy** — tenant_id, window_hours, no_show_rule, allow_self_reschedule(bool)
  - _No deposit/auto-charge in v1; governs the self-service reschedule/cancel boundary (PRD-02/REMINDERS-SELF-SERVICE)._

## Other

- Source PRD: [PRD-02-booking-scheduling.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-02-booking-scheduling.md)

## Tasks (dev pickup)

- [ ] **Cancellation / no-show policy settings UI**
  Behaviour: a per-tenant settings screen for window_hours, no_show_rule and allow_self_reschedule. Requirements: validate and persist; surface the plain-language 'no auto-charge in v1' note; the policy is shown to the client at confirm time (ties to BOOKING-WIZARD's confirmation step) and is the source of truth the self-service endpoints enforce.
