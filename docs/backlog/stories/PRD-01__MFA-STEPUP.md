# MFA & step-up authentication for sensitive actions

> **Epic:** [PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model)](../epics/PRD-01.md)  ·  **Key:** `PRD-01/MFA-STEPUP`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-01/SIGNIN-UI`

## Background

As a security-conscious clinic, I want MFA for staff and step-up re-authentication on the most sensitive actions, so that high-risk operations can't be performed on a walk-up or hijacked session.
Staff MFA is required; sensitive clinical/medicines/financial actions (e.g. prescribing, S4 custody changes, destruction, data export) may require step-up re-auth. Client MFA policy is an open question.

## How it works

Staff sign-in enforces MFA via Entra (ADR-0004, C10) — strong auth is a baseline, not an option. On top of that, the most sensitive actions require a recent step-up (re-auth) so they can't be performed on a walked-up-to or hijacked session: prescribing, S4 stock custody changes, record destruction (RETENTION), and data export (AUDIT/PRIVACY-RIGHTS). If the session's last strong-auth is too old, the action prompts for step-up; if step-up isn't completed, the action is blocked with a clear prompt.
Recency is the mechanism: each session carries an AuthAssurance (mfa_at, stepup_at, methods). A configured sensitive action checks the recency of stepup_at against a threshold; a fresh step-up satisfies a window of subsequent sensitive actions so the clinician isn't re-prompted constantly mid-procedure.
Every MFA and step-up event is audited (AUTH-AUDIT). Client MFA policy is the PRD's open question (§11) — modelled as configurable per clinic (optional by default, can be required for sensitive client actions) rather than hard-coded, so each clinic resolves it.
Edge cases: step-up failure leaves the underlying record untouched (the sensitive action simply doesn't run); a long procedure with one valid step-up doesn't nag; the set of step-up-gated actions is configuration, not hard-coded, so it can extend without code change.

## Requirements

- MFA for staff and step-up re-authentication on the most sensitive actions.
- Compliance: [C10](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Staff sign-in enforces MFA (via Entra).
- [ ] Configured sensitive actions require a recent/step-up auth or are blocked with a clear prompt.
- [ ] Step-up events are audited.
- [ ] Client MFA policy (optional vs required for sensitive actions) is configurable (open question resolved per clinic).

## UI designs / screenshots

- A step-up prompt (re-auth modal via Entra) appears only when a configured sensitive action is attempted without recent strong auth; otherwise invisible — normal actions are never interrupted.
- A blocked sensitive action (step-up declined/failed) shows a clear reason consistent with the blocked-action banner.

## Suggested data model

- **AuthAssurance** — session_id, mfa_at, stepup_at, methods[]
  - _Sensitive actions check recency of stepup_at against a configured window; a fresh step-up covers subsequent actions in-window._
- **StepUpPolicy** — id, tenant_id, action_key, max_age, client_mfa(optional|required)
  - _Which actions are step-up-gated + the recency window; client MFA configurable per clinic (open question §11)._

## Technical notes (high level)

- Architecture decisions: [ADR-0004](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Enforce staff MFA + model auth assurance/recency**
  Ensure staff sign-in enforces MFA via Entra and capture AuthAssurance per session (mfa_at, stepup_at, methods). Provide the recency check the sensitive-action gate uses, with a window so one fresh step-up covers subsequent in-window actions. Record MFA/step-up events (AUTH-AUDIT).
- [ ] **Step-up gate on sensitive actions (configurable, not hard-coded)**
  Define StepUpPolicy (action_key + max_age) and gate the sensitive actions — prescribing, S4 custody changes, destruction, data export — so an attempt without recent strong auth triggers a step-up re-auth; if not completed, the action is blocked with a clear reason and the underlying record is untouched. The gated-action set is configuration so it extends without code change. Step-up events audited.
- [ ] **Configurable client MFA policy**
  Model client MFA as a per-clinic configuration (optional by default; can be required for sensitive client actions) to resolve PRD §11's open question, rather than hard-coding it. Wire the client sensitive-action paths to honour the tenant's setting.
