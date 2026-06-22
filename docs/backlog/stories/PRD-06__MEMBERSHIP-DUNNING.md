# Membership: failed-payment dunning (retry-and-chase) + manual Retry

> **Epic:** [PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards](../epics/PRD-06.md)  ·  **Key:** `PRD-06/MEMBERSHIP-DUNNING`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-06/MEMBERSHIP-AUTOPAY`

## Background

As a owner, I want a failed membership charge to trigger a polite retry-and-chase rather than instantly dropping the member, so that recoverable failures are recovered and members aren't lost to a temporary card glitch.
Plainly: when an automatic charge fails, don't lapse the member straight away — retry on a back-off schedule, ask them to update their card, raise a follow-up, and only lapse if it all fails; the desk can also retry by hand. Where it fits: a follow-up to the autopay scheduler (PRD-06/MEMBERSHIP-AUTOPAY), which charges due memberships; this handles the charges that fail. Dunning is the scheduled retry-and-chase when a recurring payment fails. Notices go via INotifier (PRD-07/CHANNELS) and the follow-up lands in the Follow-ups queue (PRD-07/FOLLOWUPS). Money figures owner-gated (.fin).

## How it works

A failed charge does NOT lapse the member immediately — it opens a DunningAttempt sequence (dunning = the scheduled retry-and-chase when a recurring payment fails): back-off retries, a client notice to update their card, a 'Payment failed' state and a follow-up Job; only after the sequence exhausts does the membership lapse.
The members list (PRD-06/MEMBERSHIP-MEMBERS) shows 'Payment failed · Retry' with a manual Retry that re-attempts the current period without skipping it. Notices go via INotifier (PRD-07/CHANNELS); the follow-up lands in the Follow-ups queue (PRD-07/FOLLOWUPS); retries are idempotent. This extends the autopay scheduler (PRD-06/MEMBERSHIP-AUTOPAY). Money figures owner-gated (.fin).

## Requirements

- A failed membership charge to trigger a polite retry-and-chase rather than instantly dropping the member.

## Acceptance Criteria

- [ ] A failed charge opens a DunningAttempt sequence (back-off retries + client notice + follow-up Job) before any lapse.
- [ ] Notices go via INotifier (PRD-07/CHANNELS); the follow-up lands in the Follow-ups queue (PRD-07/FOLLOWUPS).
- [ ] The members list shows 'Payment failed · Retry' with a manual Retry that re-attempts the current period without skipping it.
- [ ] Retries are idempotent; only after the sequence exhausts does the membership lapse. Money figures owner-gated (.fin).

## UI designs / screenshots

- Prototype: Members & billing — a member in 'Payment failed · Retry' status with a manual Retry action; client receives an update-card notice.

![checkout — prototype screen](../screens/checkout.png)

## Suggested data model

- **DunningAttempt** — id, membership_id, attempt_no, at, result(success|failed), next_retry_at
  - _New entity; back-off retry + client notice + Job on failed charge._
- **Membership (extends PRD-06/MEMBERSHIP)** — + status value 'dunning'
  - _Adds the dunning status to the basic Membership lifecycle._

## Other

- Source PRD: [PRD-06-payments-memberships-rewards.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-06-payments-memberships-rewards.md)

## Tasks (dev pickup)

- [ ] **DunningAttempt state machine (back-off retry + notice + Job)**
  Behaviour: a failed charge opens a DunningAttempt sequence — back-off retries, a client notice to update the card, a 'Payment failed' state and a follow-up Job — before any lapse. Requirements: notices via INotifier (PRD-07/CHANNELS); follow-up to PRD-07/FOLLOWUPS; retries idempotent; lapse only after the sequence exhausts; owner-only (.fin).
- [ ] **Manual Retry from the members list**
  Behaviour: the members list shows 'Payment failed · Retry'; a manual Retry re-attempts the current period without skipping it. Requirements: idempotent (no double-bill); reflects the real charge result; owner-only.
