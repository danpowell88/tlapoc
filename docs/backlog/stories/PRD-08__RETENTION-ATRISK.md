# Retention: at-risk / lapsed worklist + reactivation hand-off

> **Epic:** [PRD-08 — Reporting & compliance dashboards (Governance hub)](../epics/PRD-08.md)  ·  **Key:** `PRD-08/RETENTION-ATRISK`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-08/RETENTION-COHORTS`

## Background

As a owner, I want an at-risk / lapsed client list I can act on, with a one-click hand-off into recall, so that I can win back clients who are slipping away rather than just watching the number.
Plainly: the actionable list beside the cohort grid — clients past their expected return window, each with last-seen, a reason they're at-risk and (owner-only) the value at risk, plus a one-click 'queue reactivation' that hands them into the recall worklist. Where it fits: a follow-up to the retention cohort analysis (PRD-08/RETENTION-COHORTS) that adds the worklist counterpart to the cohort grid. It reads the same reporting read-models (PRD-08/READ-MODELS) and hands off to the follow-up/recall queue (PRD-07) so a number becomes a call, never a dead end. Operational signals are visible to managers; any lifetime-value / dollar figure is owner-only (.fin).

## How it works

Alongside the cohort grid (PRD-08/RETENTION-COHORTS) sits the at-risk / lapsed worklist: clients past their expected return cadence for their treatment type, each showing last-seen, an at-risk reason (e.g. 'anti-wrinkle client, 14 weeks since last visit') and — owner-only — their value at risk. The list is the actionable counterpart to the headline retention rate on BUSINESS-DASH.
Acting on a client hands straight off to the recall / win-back loop: a one-click 'queue reactivation' action creates a reactivation follow-up job (PRD-07) so the report drives a call rather than just describing a problem; the hand-off honours the client's marketing-consent state and is idempotent (no duplicate job for the same client). Rows deep-link into the client 360 profile.
This reads from the reporting read-models (PRD-08/READ-MODELS) over appointment, client and visit data and is date/window-aware like the rest of Reports. Cadence and at-risk reason are operational; any lifetime-value / dollar figure is owner-gated (.fin) and stripped for non-owner roles.

## Requirements

- An at-risk / lapsed client list I can act on, with a one-click hand-off into recall.

## Acceptance Criteria

- [ ] An at-risk / lapsed list surfaces clients past their expected return window, each with last-seen, value and a reason they are at-risk.
- [ ] Each at-risk client has a one-click hand-off that creates a reactivation follow-up job (PRD-07), respecting marketing consent.
- [ ] The reactivation action is idempotent (no duplicate job for the same client); rows deep-link into the client 360 profile.
- [ ] Operational signals are visible to managers; any lifetime-value / dollar figure is owner-only (.fin).

## UI designs / screenshots

- Prototype: Reports → Retention & rebooking (reports.png, goRep('retention')) — the 'At-risk & lapsed clients' card (repAtRisk) with an 'Open follow-ups →' action.
- At-risk list: client, last-seen, at-risk reason, value-at-risk (.fin owner-only), and a per-row 'queue reactivation' hand-off into Follow-ups.
- Date presets shared with the business view; operational signals visible to managers, money owner-gated.

![reports — prototype screen](../screens/reports.png)

## Suggested data model

- **(read) AtRiskClient** — client_id, last_seen, treatment_type, expected_cadence, at_risk_reason, value_at_risk
  - _Clients past expected return cadence; value_at_risk owner-gated (.fin); feeds the reactivation hand-off._

## Other

- Source PRD: [PRD-08-reporting-compliance.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-08-reporting-compliance.md)

## Tasks (dev pickup)

- [ ] **Read-model / projection: at-risk & lapsed clients**
  Behaviour: project AtRiskClient = clients past the expected return cadence for their treatment type, with last-seen, an at-risk reason and (owner-only) value-at-risk. Requirements: cadence is per treatment type; value_at_risk is tagged owner-financial and stripped for non-owner roles; expose the underlying client ids so the list drills into the 360 profile.
- [ ] **At-risk list UI + reactivation hand-off to Follow-ups**
  Behaviour: render the at-risk / lapsed list (client, last-seen, reason, value-at-risk) with a per-row 'queue reactivation' action and an 'Open follow-ups →' link. Requirements: the hand-off creates a reactivation follow-up job (PRD-07) honouring marketing consent; value-at-risk is .fin owner-only; rows deep-link into the client 360 profile; the reactivation action is idempotent (no duplicate job for the same client).
