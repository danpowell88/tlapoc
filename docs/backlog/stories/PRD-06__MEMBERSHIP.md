# Membership join + card-on-file — basic enrolment (core)

> **Epic:** [PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards](../epics/PRD-06.md)  ·  **Key:** `PRD-06/MEMBERSHIP`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-06/PAYMENT-PROVIDER`

## Background

As a client, I want to join a membership and store a card on file, so that I'm enrolled and ready to be billed for member perks.
What this is, plainly: a client joins a monthly plan and stores a card once, so the clinic holds a tokenised card-on-file ready to charge. This is the minimal end-to-end core; the autopay scheduler, failed-payment dunning, lifecycle states, benefit auto-apply and the members list/KPIs are each added as their own follow-ups. Where it sits: it builds on the PAYMENT-PROVIDER card-on-file token and is the first brick of the clinic's recurring-revenue engine; it arrives in the Payments layer after the clinical core. Membership enrolment with a tokenised card-on-file (added online/in-app or at desk) (REQ-MEMB-1/2/3).

## How it works

A MembershipPlan defines name/tier, price, billing period and benefits. A Membership ties a client to a plan with a tokenised card-on-file (a PaymentMethodToken from PAYMENT-PROVIDER), a schedule and a next_charge_at. A scheduled job charges due memberships off-session via IPaymentProvider.recurringCharge.
Dunning: a failed charge doesn't lapse the member immediately — it opens a DunningAttempt sequence — dunning being the scheduled retry-and-chase when a recurring payment fails — (retry on a back-off schedule, notify the client to update their card, and raise a follow-up Job / 'Payment failed · Retry' state) before any cancellation. The members screen shows each member's plan, the card-on-file (last4), next charge date and dunning state, with a manual Retry.
Lifecycle — join / pause / cancel / win-back — is tracked and feeds MRR (monthly recurring revenue) and churn reporting (PRD-08). Benefits and credits (e.g. member pricing, 10% off non-S4, periodic complimentary add-on) auto-apply at checkout; all money figures stay owner-gated.

## Requirements

- To join a membership and store a card on file.

## Acceptance Criteria

- [ ] A client can join a plan, creating a Membership that ties them to the plan with a tokenised card-on-file.
- [ ] The card-on-file can be captured online, in the client app, or at the desk; only the token + brand/last4 are stored (never a PAN).
- [ ] A next_charge_at is set on enrolment; the actual recurring charging is added by the autopay follow-up.
- [ ] All money figures are owner-gated (.fin).

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

- [ ] **Membership model + join (ties client to plan, sets next_charge_at)**
  Behaviour: joining a plan creates a Membership tying the client to a plan_id with a billing schedule and an initial next_charge_at. Requirements: tenant-scoped with RLS (row-level security); plan definitions come from PRD-06/MEMBERSHIP-PLANS; status starts active; all money figures owner-gated (.fin). The recurring charging itself is the autopay follow-up.
- [ ] **Card-on-file capture (online / in-app / desk)**
  Behaviour: the member stores a card once; the token can be captured online, in the client app, or at the desk. A tokenised card-on-file (a PaymentMethodToken from PRD-06/PAYMENT-PROVIDER) is linked to the Membership. Requirements: only the token + brand/last4 are stored (never a PAN — primary account number); the client app shows 'Visa ···· 4242 — Used for membership autopay'; capability/consent appropriate to the surface. NOTE the online/in-app capture is a client-facing capability and arrives LATE in the clinic-first build; the desk capture is available earlier.
