# Quiet windows: cost-per-treatment / savings framing

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/QUIET-WINDOWS-COST`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-02/QUIET-WINDOWS`

## Background

As a owner, I want each quiet window to show the cost of leaving it idle, so that I can see the financial reason to fill it.
Plainly: the owner-only dollar framing on each quiet window — an idle chair spreads fixed staff cost across fewer treatments, so cost-per-treatment rises. Where it fits: a follow-up to the quiet-windows basic detection (PRD-02/QUIET-WINDOWS) that adds the financial rationale on top of the window list. It honours owner-only financial gating: all money figures sit behind the .fin capability and are stripped for non-owner roles. It sits in the Reception schedule (PRD-02).

## How it works

The basic panel lists quiet windows; this follow-up adds the why. Each window is framed with the consequence of leaving it idle — fixed staff cost spread across fewer treatments raises cost-per-treatment — with an estimated dollar figure so the owner can weigh whether to fill it.
The financial framing respects owner-only financial gating: the server strips all dollar/cost figures for non-owner roles (the .fin capability). A non-owner such as Reception still sees the window and the prompt to fill it, but never the money.
This is purely additive over the basic list — it adds a money annotation, not a new detection mechanism.

## Requirements

- Each quiet window to show the cost of leaving it idle.

## Acceptance Criteria

- [ ] Each window shows the business reason to fill it (an idle chair raises staff cost-per-treatment), with an estimated figure.
- [ ] All dollar/cost figures are owner-only and stripped for non-owner roles (the .fin capability).
- [ ] Non-owners see the window and the prompt to fill it, but no money figures.

## UI designs / screenshots

- 'Quiet windows to fill' panel header with a savings icon and the one-line rationale (filling idle chairs cuts staff cost-per-treatment).
- An owner-only cost/savings figure on each window card, rendered only when the .fin capability is present.
- Non-owner roles see the window and Fill prompt with the money figures hidden.

![schedule — prototype screen](../screens/schedule.png)

## Suggested data model

- **(extends QUIET-WINDOWS)** — no new entities; adds a derived owner-only cost-per-treatment estimate per QuietWindow
  - _Money figures gated behind .fin (owner-only) and stripped server-side for non-owner roles._

## Other

- Source PRD: [PRD-02-booking-scheduling.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-02-booking-scheduling.md)

## Tasks (dev pickup)

- [ ] **Cost-per-treatment estimate per window (.fin-gated)**
  Behaviour: annotate each quiet window with the cost of leaving it idle — an idle chair raises staff cost-per-treatment — and an estimated figure. Requirements: all dollar/cost figures are owner-only and stripped server-side for non-owner roles (the .fin capability); non-owners see the window and the prompt to fill it, but no money.
