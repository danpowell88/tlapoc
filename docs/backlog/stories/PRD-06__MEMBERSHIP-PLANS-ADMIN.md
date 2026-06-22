# Membership plans: capability-gated admin, audit & member-term preservation

> **Epic:** [PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards](../epics/PRD-06.md)  ·  **Key:** `PRD-06/MEMBERSHIP-PLANS-ADMIN`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-06/MEMBERSHIP-PLANS`

## Background

As a owner / manager, I want plan edits to be capability-gated and audited, with existing members keeping their terms, so that pricing changes are controlled and no active member is silently re-priced.
Plainly: lock plan editing to owner/manager, log every change, and make a price change apply only to new sign-ups so current members keep what they joined on until explicitly migrated. Where it fits: a follow-up to the basic plans core (PRD-06/MEMBERSHIP-PLANS), which defines plans with the non-S4 constraint; this adds the governance around editing them. Price/MRR (monthly recurring revenue) figures are owner-only (.fin). This is the live-pricing path that the read-only PRD-06/PRICING-WHATIF planner proposes into.

## How it works

The basic plans core (PRD-06/MEMBERSHIP-PLANS) defines plans with the non-S4 benefit constraint; this follow-up adds the governance: add/edit/archive a plan is gated to owner/manager capability and every change writes an AuditEvent. A price change applies to new sign-ups while existing members keep their terms until explicitly migrated — no silent re-pricing of active members.
Price + MRR (monthly recurring revenue) figures are owner-only (.fin). 'Apply' here is the live-pricing path that the read-only PRD-06/PRICING-WHATIF planner proposes into.

## Requirements

- Plan edits to be capability-gated and audited, with existing members keeping their terms.

## Acceptance Criteria

- [ ] Add/edit/archive a plan is gated to owner/manager capability and every change writes an AuditEvent.
- [ ] A price change applies to new sign-ups while existing members keep their terms until explicitly migrated (no silent re-pricing).
- [ ] Price + MRR (monthly recurring revenue) figures are owner-only (.fin).
- [ ] 'Apply' here is the live-pricing path that PRD-06/PRICING-WHATIF proposes into.

## UI designs / screenshots

- Prototype: Memberships -> Plans & packages — per-card Edit/Archive gated to owner/manager; a migrate-existing-members prompt on price change; owner-only (.fin) on price/MRR.

![checkout — prototype screen](../screens/checkout.png)

## Suggested data model

- **AuditEvent (ref)** — actor, plan_id, change, at
  - _Plan changes audited; admin capability-gated; existing members keep terms until migrated._

## Other

- Source PRD: [PRD-06-payments-memberships-rewards.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-06-payments-memberships-rewards.md)

## Tasks (dev pickup)

- [ ] **Capability-gated plan admin + audit + member-term preservation**
  Behaviour: add/edit/archive a plan is gated to owner/manager capability and every change writes an AuditEvent; a price change applies to new sign-ups while existing members keep their terms until explicitly migrated. Requirements: no silent re-pricing of active members; price + MRR (monthly recurring revenue) figures are owner-only (.fin); 'Apply' here is the live-pricing path that PRD-06/PRICING-WHATIF proposes into.
