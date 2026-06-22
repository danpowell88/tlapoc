# Client app: my care, memberships, rewards & card-on-file

> **Epic:** [PRD-09 — Apps (Flutter): client & provider](../epics/PRD-09.md)  ·  **Key:** `PRD-09/CLIENT-CARE`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** client-app
>
> **Depends on:** `PRD-06/MEMBERSHIP`, `PRD-05/PHOTOS`

## Background

As a client, I want to view my photos, memberships, rewards and balance and add a card-on-file, so that I can self-serve my care and payments.
Clients view consented before/after photos, memberships, rewards/perks and balances, and add a card-on-file for autopay (REQ-APP-1).

## How it works

My care/Rewards/Account tabs: visit history + consent-gated before/after photos (served via short-lived signed URLs, ADR-0009, never on device); points/perks/gift cards over PRD-06; profile, memberships, the client's own balance, and add/replace a tokenised card-on-file (Square) that feeds PRD-06 autopay.
No one-off online checkout (v1 payments are in-person). Self-service for care history and payments.

## Requirements

- To view my photos, memberships, rewards and balance and add a card-on-file.
- Compliance: [C14](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Consent-gated before/after photo viewing.
- [ ] Memberships, rewards/perks and balances visible.
- [ ] Card-on-file can be added in-app (feeds PRD-06 autopay).
- [ ] No one-off online checkout is exposed.

## UI designs / screenshots

_Prototype screen: client-app.html, treatment-room.html, checkin.html, backroom.html._

- Prototype: client-app — My care (visit history, photos gated by image-use consent), Rewards (redeem points, perks, gift cards), Account (profile, memberships, balance, 'Update card on file').
- Photo viewing is image-use-consent-gated and served via signed URLs.

![client-app — prototype screen](../screens/client-app.png)

## Suggested data model

- **(reuses) Photo** — PRD-05 — signed-URL view (ADR-0009), image-use-consent-gated
  - _Never bundled/persisted in the app._
- **(reuses) Membership/RewardLedger/AccountBalance** — PRD-06 — membership, points/perks, client balance
  - _Client sees own figures only._
- **(reuses) PaymentMethodToken** — PRD-06 — provider-tokenised card-on-file (Square)
  - _Feeds autopay; no one-off checkout._

## Other

- Source PRD: [PRD-09-apps-client-provider.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-09-apps-client-provider.md)

## Tasks (dev pickup)

- [ ] **Client app: My care / Rewards / Account + card-on-file**
  My care tab: visit history list and a before/after gallery whose tiles each fetch a per-view signed URL (ADR-0009) and cache transiently; gate the gallery on image-use consent re-checked server-side so a withdrawal hides it immediately. Rewards tab over PRD-06 (points balance, perks, gift-card redeem). Account tab: profile, memberships, the client's own balance, and 'Update card on file' using the Square SDK to tokenise — store no PAN; post the token to PRD-06 for membership autopay. Do not expose any one-off online checkout.
