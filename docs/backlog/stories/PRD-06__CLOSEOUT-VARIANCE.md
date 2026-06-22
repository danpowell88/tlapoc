# Closeout: Square-batch variance detection & annotation

> **Epic:** [PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards](../epics/PRD-06.md)  ·  **Key:** `PRD-06/CLOSEOUT-VARIANCE`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-06/CLOSEOUT`

## Background

As a owner, I want the closeout to flag card-vs-Square-batch and counted-vs-recorded variances prominently, so that a miskeyed cash sale or missed refund is caught the same day.
Plainly: highlight any gap between what the system recorded and what actually happened — counted cash vs recorded, and the card total vs the Square (the card-payment provider) batch — so it can be explained rather than buried. Where it fits: a follow-up to the basic daily closeout (PRD-06/CLOSEOUT), which records a simple counted-vs-recorded difference; this adds the Square-batch comparison and a prominent, annotatable variance surface. Figures are owner-gated (.fin).

## How it works

The basic closeout (PRD-06/CLOSEOUT) records a counted-vs-recorded cash difference; this follow-up adds the card side — flagging card_total against the Square (the card-payment provider) batch — and makes variances prominent rather than buried, so a miskeyed cash sale or missed refund is caught the same trading day.
A variance can be annotated with an explanation before the closeout is locked. All figures are owner-gated (.fin).

## Requirements

- The closeout to flag card-vs-Square-batch and counted-vs-recorded variances prominently.

## Acceptance Criteria

- [ ] The closeout flags card_total against the Square (the card-payment provider) batch, not just counted-vs-recorded cash.
- [ ] Variances are surfaced prominently (not buried) so they are caught the same day.
- [ ] A variance can be annotated with an explanation before the closeout is locked.
- [ ] Variance figures are owner-gated (.fin).

## UI designs / screenshots

- Prototype: Closeout — variance highlight (counted vs recorded; card vs Square batch) with an annotation field, shown before the lock step.

![checkout — prototype screen](../screens/checkout.png)

## Suggested data model

- **Closeout (extends PRD-06/CLOSEOUT)** — + variance, variance_note; compares card_total to the Square batch
  - _Extends the basic Closeout; no new entity._

## Other

- Source PRD: [PRD-06-payments-memberships-rewards.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-06-payments-memberships-rewards.md)

## Tasks (dev pickup)

- [ ] **Card-vs-Square-batch + counted-vs-recorded variance flagging**
  Behaviour: the closeout computes and prominently highlights variance = counted − recorded and flags card_total vs the Square (the card-payment provider) batch. Requirements: surfaced prominently (not buried); owner-only (.fin); reads the day's Payment rows + the Square batch figure.
- [ ] **Variance annotation before lock**
  Behaviour: a variance can be annotated with an explanation before the closeout is locked. Requirements: the note persists on the Closeout and is audited; owner-only.
