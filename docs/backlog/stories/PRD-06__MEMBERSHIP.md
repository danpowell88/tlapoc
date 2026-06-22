# Memberships with automatic autopay & dunning

> **Epic:** [PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards](../epics/PRD-06.md)  ·  **Key:** `PRD-06/MEMBERSHIP`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-06/PAYMENT-PROVIDER`

## Background

As a client, I want to join a membership and have my card auto-charged on schedule, so that I get member perks without manual payments.
What this is, plainly: clients join a monthly plan, store a card once, and the platform charges that card automatically on schedule — chasing politely if a charge fails rather than dropping the member. Where it sits: it builds on the PAYMENT-PROVIDER card-on-file token and is the clinic's recurring-revenue engine; it arrives in the Payments layer after the clinical core, and its lifecycle feeds reporting (PRD-08). Membership plans/tiers with automatic recurring billing from a tokenised card-on-file (added online/in-app or at desk) and failed-payment dunning — the scheduled retry-and-chase when a recurring payment fails — (REQ-MEMB-1/2/3).

## How it works

A MembershipPlan defines name/tier, price, billing period and benefits. A Membership ties a client to a plan with a tokenised card-on-file (a PaymentMethodToken from PAYMENT-PROVIDER), a schedule and a next_charge_at. A scheduled job charges due memberships off-session via IPaymentProvider.recurringCharge.
Dunning: a failed charge doesn't lapse the member immediately — it opens a DunningAttempt sequence — dunning being the scheduled retry-and-chase when a recurring payment fails — (retry on a back-off schedule, notify the client to update their card, and raise a follow-up Job / 'Payment failed · Retry' state) before any cancellation. The members screen shows each member's plan, the card-on-file (last4), next charge date and dunning state, with a manual Retry.
Lifecycle — join / pause / cancel / win-back — is tracked and feeds MRR (monthly recurring revenue) and churn reporting (PRD-08). Benefits and credits (e.g. member pricing, 10% off non-S4, periodic complimentary add-on) auto-apply at checkout; all money figures stay owner-gated.

## Requirements

- To join a membership and have my card auto-charged on schedule.

## Acceptance Criteria

- [ ] A membership auto-charges on schedule from a stored token (card added online/in-app or in person).
- [ ] A failed charge triggers a dunning (retry-and-chase) recovery sequence (retry + client notice + follow-up) before lapse, with a manual Retry.
- [ ] Lifecycle (join/pause/cancel/win-back) is tracked and feeds MRR (monthly recurring revenue)/churn reporting (PRD-08).
- [ ] Benefits/credits auto-apply at checkout; all money figures are owner-gated.

## UI designs / screenshots

- Prototype: Memberships -> Members & billing — member list with Plan, Since, Autopay (card last4), Next charge, Status (Active / 'Payment failed · Retry'); Plans & packages defines tiers; '+ New plan'.
- Client app: join + add/update card-on-file (Visa ···· 4242 'Used for membership autopay'); 'Glow Club renews 1 Jul · autopay is on'.

![memb-members — prototype screen](../screens/memb-members.png)

## Suggested data model

- **MembershipPlan** — id, tenant_id, name, tier, price, period, benefits[]
  - _Owner-defined tiers._
- **Membership** — id, client_id, plan_id, token_ref, schedule, status(active|paused|cancelled|dunning), next_charge_at, since
  - _Autopay via IPaymentProvider.recurringCharge; lifecycle -> MRR (monthly recurring revenue)/churn (PRD-08)._
- **DunningAttempt** — id, membership_id, attempt_no, at, result(success|failed), next_retry_at
  - _Back-off retry + client notice + Job on failed charge._

## Other

- Source PRD: [PRD-06-payments-memberships-rewards.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-06-payments-memberships-rewards.md)

## Tasks (dev pickup)

- [ ] **Membership join + card-on-file capture (online / in-app / desk)**
  Behaviour: a client joins a plan and stores a card once; the token can be captured online, in the client app, or at the desk. A Membership ties the client to a plan with a tokenised card-on-file (a PaymentMethodToken from PAYMENT-PROVIDER), a billing schedule and a next_charge_at. Requirements: only the token + brand/last4 are stored (never a PAN — primary account number); the client app shows 'Visa ···· 4242 — Used for membership autopay' and 'renews 1 Jul · autopay is on'; capability/consent appropriate to the surface. NOTE this is a client-facing/online capability and arrives LATE in the clinic-first build.
- [ ] **Autopay scheduler (off-session recurring charge)**
  Behaviour: a scheduled job picks up memberships where next_charge_at <= now and charges the stored card off-session via IPaymentProvider.recurringCharge, then advances next_charge_at to the next period. Requirements: idempotent per period (a retry never double-bills the same period); each charge writes a ProviderTxn and feeds the Closeout/Xero like any payment; autopay is built on the Square card-on-file recurring spike (SPIKE-SQUARE). All money figures owner-gated.
- [ ] **Failed-payment dunning (retry-and-chase) state machine + manual Retry**
  Behaviour: a failed charge does NOT lapse the member immediately — it opens a DunningAttempt sequence (dunning = the scheduled retry-and-chase when a recurring payment fails): back-off retries, a client notice to update their card, a 'Payment failed' state and a follow-up Job; only after the sequence exhausts does the membership lapse. The members list shows 'Payment failed · Retry' with a manual Retry. Requirements: notices go via INotifier (PRD-07); the follow-up lands in the Follow-ups queue (PRD-07/FOLLOWUPS); retries are idempotent; the manual Retry re-attempts the current period without skipping it.
- [ ] **Membership lifecycle (join / pause / cancel / win-back) -> MRR/churn**
  Behaviour: the membership moves through join → active → paused → cancelled, with a win-back path; each transition is tracked. Requirements: lifecycle transitions emit events for the MRR (monthly recurring revenue) and churn read-models (PRD-08); pause suspends billing without losing the card-on-file; cancel stops future charges; win-back re-activates. Owner-gated money figures throughout.
- [ ] **Member benefits / credits auto-apply at checkout (non-S4 only)**
  Behaviour: a member's benefits and credits apply automatically at the till — member pricing, 10% off non-S4, periodic complimentary add-on — appearing as deduction lines on the sale (PRD-06/POS). Requirements: benefits NEVER apply to an S4 (Schedule 4 prescription-only medicine) line (C9) — re-checked server-side against the live line schedule; the per-plan benefit set is defined by the plan (PRD-06/MEMBERSHIP-PLANS); money figures owner-gated.
- [ ] **Members & billing list UI + overview KPIs**
  Behaviour: the Members & billing screen lists each member with Plan, Since, Autopay (card last4), Next charge and Status (Active / 'Payment failed · Retry'); the Overview tab shows headline KPIs (active members, recurring/mo MRR, avg tenure, failed payments) and a 'Needs action' panel (failed payment → Fix, renewals this week, referrals→joined). Requirements: the MRR/recurring figures are owner-only (.fin) — Reception may see membership status but not the money; failed-payment rows link to the dunning Retry; live-update as charges/dunning resolve. Plan definitions live in PRD-06/MEMBERSHIP-PLANS.
