# Membership: lifecycle (pause / cancel / win-back) → MRR/churn

> **Epic:** [PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards](../epics/PRD-06.md)  ·  **Key:** `PRD-06/MEMBERSHIP-LIFECYCLE`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-06/MEMBERSHIP`

## Background

As a owner, I want to pause, cancel and win back memberships, with each change feeding reporting, so that members can be managed over time and recurring-revenue trends are visible.
Plainly: let a membership move beyond 'active' — pause it without losing the card, cancel future charges, or win a lapsed member back — and record each move so reporting can show MRR (monthly recurring revenue) and churn. Where it fits: a follow-up to the basic membership enrolment (PRD-06/MEMBERSHIP), which starts a membership active; this adds the rest of the lifecycle. Lifecycle transitions emit events for the MRR and churn read-models (PRD-08). Money figures owner-gated (.fin).

## How it works

The basic enrolment (PRD-06/MEMBERSHIP) starts a membership active; this follow-up adds the rest of the lifecycle: join → active → paused → cancelled, with a win-back path. Pause suspends billing without losing the card-on-file; cancel stops future charges; win-back re-activates.
Each transition is tracked and emits events for the MRR (monthly recurring revenue) and churn read-models (PRD-08). Owner-gated money figures throughout (.fin).

## Requirements

- To pause, cancel and win back memberships, with each change feeding reporting.

## Acceptance Criteria

- [ ] A membership can pause (suspends billing without losing the card-on-file), cancel (stops future charges) and win-back (re-activates).
- [ ] Each transition is tracked and emits events for the MRR (monthly recurring revenue) and churn read-models (PRD-08).
- [ ] Pause does not delete the card-on-file; win-back re-activates from where it left off.
- [ ] Owner-gated money figures throughout (.fin).

## UI designs / screenshots

- Prototype: Members & billing — per-member pause / cancel / win-back actions; lifecycle feeds the Overview KPIs and PRD-08 MRR/churn.

![checkout — prototype screen](../screens/checkout.png)

## Suggested data model

- **Membership (extends PRD-06/MEMBERSHIP)** — status(active|paused|cancelled) + win-back transition; emits lifecycle events
  - _Extends the basic Membership; events feed PRD-08 MRR/churn read-models._

## Other

- Source PRD: [PRD-06-payments-memberships-rewards.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-06-payments-memberships-rewards.md)

## Tasks (dev pickup)

- [ ] **Lifecycle transitions (pause / cancel / win-back) + MRR/churn events**
  Behaviour: pause (suspend billing, keep card), cancel (stop future charges), win-back (re-activate); each transition tracked. Requirements: emit events for the PRD-08 MRR (monthly recurring revenue)/churn read-models; pause keeps the card-on-file; owner-only (.fin).
