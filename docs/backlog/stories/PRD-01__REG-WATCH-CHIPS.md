# Reg-watch: amber early-warning countdown chips

> **Epic:** [PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model)](../epics/PRD-01.md)  ·  **Key:** `PRD-01/REG-WATCH-CHIPS`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-01/REG-WATCH`

## Background

As a manager, I want amber early-warning chips showing how soon a credential renews or how far CPD is behind, so that I act before a registration or insurance lapses rather than after.
Plainly: the small amber 'Renews in Nd' and 'CPD behind X/Yh' chips that appear on the People and Compliance views before anything lapses, so a renewal is prompted early rather than discovered late. Where it fits: a follow-up to the registration/PII/CPD expiry-alerting core (PRD-01/REG-WATCH) that adds the early-warning visual cue on the credential views. The chip is a read-only derived signal off the credential expiry/CPD figures — it does not gate anything; the auto-lapse in the core is the gate.

## How it works

The amber early-warning chips give a visible head-start before a lapse: a 'Renews in Nd' chip on registration or cosmetic insurance within the ≤40-day warning window (the prototype's threshold), and a 'CPD behind X/Yh' chip when CPD (continuing professional development) done is under the required threshold. They render on the People & credentials and Compliance views alongside the derived status.
The chip is a read-only derived signal computed from the credential expiry / CPD figures — never a hand-set field — so it stays correct as dates move. It does not gate anything: the auto-lapse in the core (PRD-01/REG-WATCH) is the gate; the chip is the early prompt. The same items also surface in the owner needs-attention digest (PRD-08) and the Follow-ups queue.

## Requirements

- Amber early-warning chips showing how soon a credential renews or how far CPD is behind.

## Acceptance Criteria

- [ ] Amber 'Renews in Nd' chips show on the People & Compliance views for registration/insurance within the warning window (≤40 days).
- [ ] A 'CPD behind X/Yh' chip shows when CPD done is under the required threshold.
- [ ] The countdown is derived from the credential expiry / CPD figures (read-only signal, not an editable field).
- [ ] The same items also surface in the owner needs-attention digest and Follow-ups.

## UI designs / screenshots

- Prototype: amber early-warning chips ('Renews in Nd' for reg/insurance ≤40 days out, 'CPD behind X/Yh' when CPD is under threshold) on the People & Compliance views.
- Read-only derived signal off the credential expiry/CPD figures, not an editable field; the same items also surface in the owner needs-attention digest and Follow-ups.

## Suggested data model

- **(derived) ExpiryCountdown** — from Credential.expiry / CPD done-vs-required → 'Renews in Nd' (≤40d) / 'CPD behind X/Yh'
  - _Read-only derived signal over the existing Credential figures (PRD-01/CREDENTIALS); no new write model; not a gate._

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Amber early-warning countdown chips on People & Compliance views**
  Behaviour: surface the amber early-warning chips — 'Renews in Nd' for registration/insurance ≤40 days out, 'CPD behind X/Yh' when CPD (continuing professional development) is under threshold — on the People & credentials and Compliance views. Requirements: the countdown is derived from the credential expiry/CPD figures (read-only signal, not an editable field); the same items also surface in the owner needs-attention digest and Follow-ups; the chip is the early prompt, not the gate (the auto-lapse in REG-WATCH is the gate).
