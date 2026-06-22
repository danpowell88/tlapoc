# Client app: my care, memberships, rewards & card-on-file

> **Epic:** [PRD-09 — Apps (Flutter): client & provider](../epics/PRD-09.md)  ·  **Key:** `PRD-09/CLIENT-CARE`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** client-app
>
> **Depends on:** `PRD-06/MEMBERSHIP`, `PRD-05/PHOTOS`

## Background

As a client, I want to view my photos, memberships, rewards and balance and add a card-on-file, so that I can self-serve my care and payments.
Clients view consented before/after photos, memberships, rewards/perks and balances, and add a card-on-file for autopay (REQ-APP-1).

## How it works

In the app the client views consented before/after photos, memberships, rewards/perks and balances, and adds a card-on-file for autopay (feeds PRD-06). No one-off online checkout is exposed.
Self-service for care history and payments.

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

- Prototype: client app (client-app.png) tabs — My care (visit history, photos with consent), Rewards (redeem points, gift cards), Account (update card on file).
- Photo viewing is image-use-consent-gated.

![client-app — prototype screen](../screens/client-app.png)

## Suggested data model

- **(reuses)** — Photo (PRD-05), Membership/RewardLedger/AccountBalance (PRD-06), PaymentMethodToken
  - _Card-on-file feeds PRD-06 autopay; no one-off checkout._

## Other

- Source PRD: [PRD-09-apps-client-provider.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-09-apps-client-provider.md)

## Tasks (dev pickup)

- [ ] **Client app UI (Flutter)**
  Build on the Flutter client app: the client-app per the UI spec. Wire to the API with loading/empty/error states; capability-gate controls; responsive; show the blocked-action banner / gate chips where gated; respect owner-only .fin gating for money figures.
  Key elements (from the prototype):
  - Prototype: client app (client-app.png) tabs — My care (visit history, photos with consent), Rewards (redeem points, gift cards), Account (update card on file).
  - Photo viewing is image-use-consent-gated.
