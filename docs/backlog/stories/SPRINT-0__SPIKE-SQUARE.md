# Spike — Square AU card-on-file recurring autopay

> **Epic:** [SPRINT-0 — Engineering foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/SPIKE-SQUARE`  ·  **Type:** Spike  ·  **Stage:** M0  ·  **Priority:** P1  ·  **Estimate:** 2 pts  ·  **Area:** integration

## Background

As a engineer, I want a spike confirming Square AU can tokenise a card and run recurring charges with failure/dunning handling, so that the membership autopay design is viable (or an alternative is chosen early).
Membership autopay depends on Square AU supporting tokenised card-on-file recurring charges with failure/dunning handling, and that capability is flagged for feasibility research before PRD-06 memberships commit (ADR-0007). The spike confirms it works in the Square AU sandbox — or surfaces the need for an alternative early.  Output is a go/no-go plus findings feeding PRD-06/PAYMENT-PROVIDER and MEMBERSHIP; PCI posture (no PAN stored, tokens only) must be confirmed.

## How it works

A prototype tokenises a test card and runs a scheduled recurring charge in the Square AU sandbox, then observes failed-charge / retry behaviour so a dunning approach (retry cadence, member notification, suspension) can be outlined for MEMBERSHIP. It confirms the PCI posture from ADR-0007: no PAN ever stored, only provider tokens, keeping PCI scope minimal.
Go/no-go bar: Square AU sandbox tokenises a card and successfully runs a scheduled recurring charge, failure/retry behaviour is observable and a dunning approach is sketched, and the no-PAN/tokens-only posture is verified. If Square AU can't do recurring card-on-file the way memberships need, the spike says so and points at the alternative (the IPaymentProvider abstraction means an adapter swap, ADR-0007).
It's a spike against a sandbox — findings and a recommendation, not production payment code. What carries forward is the confirmed (or rejected) viability and the dunning outline that MEMBERSHIP builds on.

## Requirements

- A spike confirming Square AU can tokenise a card and run recurring charges with failure/dunning handling.

## Acceptance Criteria

- [ ] Prototype tokenises a test card and runs a scheduled recurring charge in Square AU sandbox.
- [ ] Failed-charge / retry behaviour observed; dunning approach outlined.
- [ ] PCI posture confirmed: no PAN stored, only provider tokens (ADR-0007).
- [ ] Go/no-go + findings recorded; feeds PRD-06 memberships.

## Technical notes (high level)

- Architecture decisions: [ADR-0007](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)
- Time-boxed spike — produce findings + a go/no-go, not production code.

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Define the spike scope, questions and go/no-go criteria**
  Frame the autopay-feasibility question and the bar for proceeding with Square.
  - Questions: can Square AU sandbox tokenise a card and run a scheduled recurring charge; what is the failed-charge/retry behaviour; is the no-PAN/tokens-only PCI posture (ADR-0007) achievable?
  - Go/no-go bar: recurring card-on-file works in sandbox, failure/retry observable + a dunning approach outlined, PCI posture confirmed.
  - Time-box and the hand-off (PRD-06 PAYMENT-PROVIDER / MEMBERSHIP).
- [ ] **Build the throwaway sandbox prototype**
  Prove (or disprove) recurring autopay against the Square AU sandbox.
  - Tokenise a test card; schedule and run a recurring charge.
  - Trigger and observe a failed charge + retry behaviour; sketch dunning (retry cadence, notify, suspend).
  - Confirm no PAN is stored anywhere — only Square tokens. Disposable code against sandbox only.
- [ ] **Record go/no-go and findings (incl. PCI posture and the dunning outline)**
  Capture the decision and what MEMBERSHIP should build on.
  - Go/no-go on Square AU recurring autopay; if no-go, point at the IPaymentProvider adapter alternative.
  - The dunning approach outline and the confirmed PCI posture.
  - ADR only if a real provider/architecture decision results.
