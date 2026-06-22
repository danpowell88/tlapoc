# Membership: members & billing list + overview KPIs

> **Epic:** [PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards](../epics/PRD-06.md)  ·  **Key:** `PRD-06/MEMBERSHIP-MEMBERS`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-06/MEMBERSHIP`

## Background

As a owner, I want a members list with billing status and an overview of membership KPIs, so that I can see who's a member, who's failing payment, and how recurring revenue is tracking.
Plainly: the screen that lists every member with their plan, card and next charge, and an overview of the headline numbers — active members, recurring revenue, failed payments. Where it fits: a follow-up to the basic membership enrolment (PRD-06/MEMBERSHIP) that gives staff/owner the management view; it reflects autopay (PRD-06/MEMBERSHIP-AUTOPAY) and dunning (PRD-06/MEMBERSHIP-DUNNING) state, with failed-payment rows linking to the manual Retry. MRR (monthly recurring revenue) and recurring figures are owner-only (.fin) — Reception may see membership status but not the money. Plan definitions live in PRD-06/MEMBERSHIP-PLANS.

## How it works

The Members & billing screen lists each member with Plan, Since, Autopay (card last4), Next charge and Status (Active / 'Payment failed · Retry'); the Overview tab shows headline KPIs (active members, recurring/mo MRR — monthly recurring revenue, avg tenure, failed payments) and a 'Needs action' panel (failed payment → Fix, renewals this week, referrals→joined).
The MRR/recurring figures are owner-only (.fin) — Reception may see membership status but not the money; failed-payment rows link to the dunning Retry (PRD-06/MEMBERSHIP-DUNNING); the list live-updates as charges/dunning resolve. Plan definitions live in PRD-06/MEMBERSHIP-PLANS. This extends the basic membership enrolment (PRD-06/MEMBERSHIP).

## Requirements

- A members list with billing status and an overview of membership KPIs.

## Acceptance Criteria

- [ ] The Members & billing screen lists each member with Plan, Since, Autopay (card last4), Next charge and Status (Active / 'Payment failed · Retry').
- [ ] The Overview tab shows headline KPIs (active members, recurring/mo MRR, avg tenure, failed payments) and a 'Needs action' panel (failed payment → Fix, renewals this week, referrals→joined).
- [ ] MRR/recurring figures are owner-only (.fin) — Reception may see membership status but not the money; failed-payment rows link to the dunning Retry.
- [ ] The list live-updates as charges/dunning resolve.

## UI designs / screenshots

- Prototype: Memberships → Members & billing — member list with Plan, Since, Autopay (card last4), Next charge, Status (Active / 'Payment failed · Retry'); Overview tab with headline KPIs + a 'Needs action' panel.

![checkout — prototype screen](../screens/checkout.png)

## Suggested data model

- **(read-model over PRD-06/MEMBERSHIP + DunningAttempt)** — member rows + KPIs (active members, MRR, avg tenure, failed payments)
  - _No new entity; MRR figures owner-only (.fin); failed rows link to dunning Retry._

## Other

- Source PRD: [PRD-06-payments-memberships-rewards.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-06-payments-memberships-rewards.md)

## Tasks (dev pickup)

- [ ] **Members & billing list (Plan / Since / Autopay / Next charge / Status)**
  Behaviour: list each member with Plan, Since, Autopay (card last4), Next charge and Status (Active / 'Payment failed · Retry'); failed-payment rows link to the dunning Retry (PRD-06/MEMBERSHIP-DUNNING). Requirements: live-update as charges/dunning resolve; Reception may see status but not money; owner-only (.fin) on recurring figures.
- [ ] **Overview KPIs + 'Needs action' panel**
  Behaviour: the Overview tab shows headline KPIs (active members, recurring/mo MRR — monthly recurring revenue, avg tenure, failed payments) and a 'Needs action' panel (failed payment → Fix, renewals this week, referrals→joined). Requirements: KPI read-model computed server-side; MRR owner-only (.fin); loading/empty/error states.
