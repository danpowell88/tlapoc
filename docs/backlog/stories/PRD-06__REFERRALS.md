# Referrals & affiliate credit (non-S4) (placeholder)

> **Epic:** [PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards](../epics/PRD-06.md)  ·  **Key:** `PRD-06/REFERRALS`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 1 pts  ·  **Area:** web

## Background

As a client / owner, I want to refer friends and earn non-S4 credit, so that word-of-mouth growth is rewarded compliantly.
What this is, plainly: a placeholder for refer-a-friend credit — captured now so the rewards model stays referral-ready, built later. Where it sits: Phase 2, after the core membership/rewards mechanics ship; it reuses the rewards engine's non-S4 guardrail. The prototype's Memberships → Referrals screen shows referral/affiliate credit. Per scope, advanced loyalty/referrals are Phase 2 and referral/affiliate credit is non-S4 only (REQ-MEMB-10).

## How it works

Placeholder (Phase 2). Referral/affiliate credit reuses the rewards-engine guardrail: credit is non-S4 (non-Schedule 4) only — no S4 (Schedule 4 prescription-only medicine) incentive (C9). Core membership/rewards mechanics ship first; this is captured so the data model and the non-S4 invariant already accommodate referrals when it's built.

## Requirements

- To refer friends and earn non-S4 credit.
- Deferred (Phase 2+): placeholder, design-only for now.
- Compliance: [C9](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Placeholder — Phase 2; core membership/rewards mechanics ship first.
- [ ] Referral/affiliate credit is non-S4 only (no S4 incentive), reusing the rewards-engine guardrail (C9).
- [ ] Captured so the rewards model stays referral-ready.

## UI designs / screenshots

_Prototype screen: prototype.html — Checkout, Memberships; client-app.html Rewards/Account._

- Prototype: Memberships -> Referrals — referral/affiliate credit concept (Phase 2).

![memb-referrals — prototype screen](../screens/memb-referrals.png)

## Suggested data model

- **Referral** — id, tenant_id, referrer_id, referee_id, credit(non-S4), status
  - _Phase 2; non-S4 credit only — reuses the rewards engine guardrail._

## Technical notes (high level)

- Architecture decisions: [ADR-0014](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-06-payments-memberships-rewards.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-06-payments-memberships-rewards.md)

## Tasks (dev pickup)

- [ ] **Scope & design when pulled into a sprint**
  Deferred placeholder — no build in v1. When pulled in: confirm it still fits scope and the non-S4 (non-Schedule 4) regulatory stance (referral/affiliate credit must be non-S4 only, reusing the rewards-engine guardrail, C9), then break down. Referral credit posts to the same RewardLedger; no S4 (Schedule 4 prescription-only medicine) incentive ever.
