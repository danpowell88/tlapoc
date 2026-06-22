# Client app: account, memberships & card-on-file

> **Epic:** [PRD-09 — Apps (Flutter): client & provider](../epics/PRD-09.md)  ·  **Key:** `PRD-09/CLIENT-ACCOUNT`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-09/CLIENT-CARE`, `PRD-06/MEMBERSHIP`

## Background

As a client, I want to manage my profile and memberships and save a card on file, so that my membership bills automatically without me re-entering a card.
Plainly: the Account tab of the client app — profile, memberships, the client's own balance, and saving a card so membership billing can run automatically. Where it fits: a follow-up to the My care health hub (PRD-09/CLIENT-CARE) that adds the account + card-on-file surface; the card feeds the payments module's autopay (PRD-06). There is no one-off online checkout — v1 payments are in-person — and the privacy surface (CLIENT-PRIVACY) lives beneath these actions.

## How it works

The Account tab surfaces profile, memberships, the client's own balance and 'Update card on file'. Card capture uses the Square SDK (software development kit) to tokenise on-device — no PAN (the raw card number) is ever stored or sent; the token posts to PRD-06 to feed membership autopay (automatic recurring billing).
The client sees only their own balances, never clinic revenue. NO one-off online checkout is exposed (v1 payments are in-person). The 'Your data & privacy' entry point (CLIENT-PRIVACY) lives beneath these account actions.

## Requirements

- To manage my profile and memberships and save a card on file.

## Acceptance Criteria

- [ ] The Account tab surfaces profile, memberships and the client's own balance.
- [ ] Card capture tokenises on-device (Square SDK) — no PAN is ever stored or sent — and the token feeds PRD-06 membership autopay.
- [ ] The client sees only their own balances, never clinic revenue.
- [ ] No one-off online checkout is exposed (v1 payments are in-person); the 'Your data & privacy' entry point (CLIENT-PRIVACY) lives beneath these actions.

## UI designs / screenshots

- Prototype: client-app — Account (profile, memberships, balance, 'Update card on file').
- Card tokenised on-device (Square); no PAN stored; feeds autopay; no one-off checkout.
- 'Your data & privacy' entry point sits beneath the account actions (CLIENT-PRIVACY).

![client-app — prototype screen](../screens/client-app.png)

## Suggested data model

- **(reuses) Membership/AccountBalance** — PRD-06 — memberships + the client's own balance
  - _Extends CLIENT-CARE; client sees own figures only, never clinic revenue._
- **(reuses) PaymentMethodToken** — PRD-06 — provider-tokenised card-on-file (Square)
  - _Feeds autopay; no one-off checkout; no PAN stored on device._

## Other

- Source PRD: [PRD-09-apps-client-provider.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-09-apps-client-provider.md)

## Tasks (dev pickup)

- [ ] **Account tab: profile, memberships, own balance + card-on-file (Square tokenise)**
  Behaviour: the Account tab surfaces profile, memberships, the client's own balance and 'Update card on file'. Requirements: card capture uses the Square SDK (software development kit) to tokenise on-device — no PAN (the raw card number) is ever stored or sent; the token posts to PRD-06 to feed membership autopay (automatic recurring billing); the client sees only their own balances, never clinic revenue; NO one-off online checkout is exposed (v1 payments are in-person). The 'Your data & privacy' entry point (CLIENT-PRIVACY) lives beneath these actions.
