# Owner 'needs attention' exceptions digest

> **Epic:** [PRD-08 — Reporting & compliance dashboards (Governance hub)](../epics/PRD-08.md)  ·  **Key:** `PRD-08/ATTENTION-DIGEST`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web
>
> **Depends on:** `PRD-08/COMPLIANCE-DASH`

## Background

As a owner, I want a single 'needs attention' digest of exceptions across the clinic, so that I can act on what matters without hunting.
An owner digest of exceptions across the platform (REQ-RPT-5).

## How it works

A single owner 'what needs me today' view that aggregates exceptions from across the platform into one list, so the owner acts on what matters without hunting through modules. It pulls credential/insurance expiries (PRD-01 CREDENTIALS), cold-chain excursions and S4 stock discrepancies (PRD-04), data-quality findings (DATA-QUALITY), failed/declined membership payments and autopay dunning (PRD-06), and overdue follow-ups/recalls (PRD-07 Jobs). Each item is a projection over existing signals (ADR-0023) — the digest owns none of them, it surfaces them.
Every item deep-links to its source for action (e.g. the failed-payment item jumps to Members & billing), so the digest is a launchpad, not a dead read screen. It respects role and financial gating: a Reception user sees the operational exceptions they can act on but never money figures; the failed-payment and revenue-bearing items are owner-gated.
Surfaced on the Today/dashboard as the owner exceptions strip, and mirrored as the Governance Overview 'Needs attention' list for the compliance subset.

## Requirements

- A single 'needs attention' digest of exceptions across the clinic.

## Acceptance Criteria

- [ ] The digest aggregates credential/insurance expiries, cold-chain excursions, stock discrepancies, data-quality findings, failed payments and overdue follow-ups/recalls.
- [ ] Each item deep-links to its source module for action.
- [ ] The digest respects role + financial gating (money items owner-only; ops items visible to the acting role).
- [ ] Available as an at-a-glance owner view on Today, mirrored as Governance Overview 'Needs attention'.

## UI designs / screenshots

_Prototype screen: prototype.html — Reports, Governance (Overview/AE & DAEN/Policies/Audit pack)._

- Prototype: Today (dashboard.png) surfaces the owner exceptions digest as a 'Needs attention' strip; each item has a Fix/Open action that deep-links (e.g. failed membership payment → goSub('memberships','members')).
- Mirrored on Governance Overview (gov-overview.png) 'Needs attention' for the compliance subset (AE to submit, policies awaiting sign-off, recalls in progress).
- Money-bearing items (failed payments) hidden/genericised for non-owner roles.

![dashboard — prototype screen](../screens/dashboard.png)

## Suggested data model

- **(read) AttentionDigest** — items[]{kind, severity, summary, source_link, owner_financial(bool)} aggregating CredentialAlert + Excursion + StockDiscrepancy + DataQualityFinding + DunningAttempt + overdue Job
  - _Pure projection over existing signals (ADR-0023); role/financial-gated per item._

## Other

- Source PRD: [PRD-08-reporting-compliance.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-08-reporting-compliance.md)

## Tasks (dev pickup)

- [ ] **Read-model / projection: aggregate exceptions digest**
  Project AttentionDigest items from existing signals — CredentialAlert/insurance expiry (PRD-01), cold-chain Excursion + stock discrepancy (PRD-04), DataQualityFinding (DATA-QUALITY), failed-payment/DunningAttempt (PRD-06), overdue Job/recall (PRD-07). Each item carries kind, severity, a summary, a source deep-link and an owner_financial flag. The digest owns no state — it reads the source projections (ADR-0023).
- [ ] **Web UI: Today 'Needs attention' digest + deep links**
  Render the digest on Today/dashboard as the exceptions strip with per-item Fix/Open actions that deep-link to the source module, and mirror the compliance subset onto Governance Overview's 'Needs attention'. Apply role + financial gating per item (money items owner-only; ops items visible to the acting role). Keep it actionable — no item without a next step.
