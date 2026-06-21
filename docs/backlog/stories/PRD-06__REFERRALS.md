# Referrals & affiliate credit (non-S4) (placeholder)

> **Epic:** [PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards](../epics/PRD-06.md)  ·  **Key:** `PRD-06/REFERRALS`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 1 pts  ·  **Area:** web

## Background

Payments (in-person POS + autopay), memberships & non-S4 rewards — Commerce for the clinic: in-person POS (Square card-present + recorded cash + gift cards), automatic recurring membership autopay via stored card-on-file, packages/series, and a rewards engine that only ever applies to non-S4 items — driving repeat visits without eroding margin or breaching advertising law.

As a client / owner, I want to refer friends and earn non-S4 credit, so that word-of-mouth growth is rewarded compliantly.

The prototype's Memberships → Referrals screen shows referral/affiliate credit. Per scope, advanced loyalty/referrals are Phase 2 and referral/affiliate credit is non-S4 only (REQ-MEMB-10).

## Requirements

- To refer friends and earn non-S4 credit.
- Traces to requirement(s): REQ-MEMB-10.
- Deferred (Phase 2+): placeholder — design-only for now.

## Acceptance Criteria

- [ ] Placeholder — Phase 2; core membership/rewards mechanics ship first.
- [ ] Referral/affiliate credit is non-S4 only (no S4 incentive), reusing the rewards engine guardrail (C9).
- [ ] Captured so the rewards model stays referral-ready.

## UI designs / screenshots

prototype.html — Checkout, Memberships; client-app.html Rewards/Account.

## Technical notes (high level)

Stack: Angular web (admin/front-desk/public).
Architecture decisions: ADR-0014 (see docs/adr/decision-log.md).

## Other

Epic: PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards.
Source PRD: docs/prds/PRD-06-payments-memberships-rewards.md.
Backlog key: PRD-06/REFERRALS.
Phase: 2+ · Priority: P2 · Estimate: 1 pts.
Compliance criteria: C9.

## Tasks (dev pickup)

- [ ] **Scope & design when pulled into a sprint** — Deferred placeholder — no build yet.
- [ ] **Confirm it still fits scope / regulatory stance**
