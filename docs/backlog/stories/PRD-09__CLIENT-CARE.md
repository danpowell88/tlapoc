# Client app: my care, memberships, rewards & card-on-file

> **Epic:** [PRD-09 — Apps (Flutter): client & provider](../epics/PRD-09.md)  ·  **Key:** `PRD-09/CLIENT-CARE`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** client-app
>
> **Depends on:** `PRD-06/MEMBERSHIP`, `PRD-05/PHOTOS`

## Background

As a client, I want to view my photos, memberships, rewards and balance and add a card-on-file, so that I can self-serve my care and payments.
Plainly: the parts of the client app where someone reviews their own care, memberships, rewards and balance, and saves a card for membership billing. Where it fits: a late, outward-facing surface that reuses the modules built earlier (PRD-05 photos, PRD-06 payments/memberships/rewards). Clients view consented before/after photos, memberships, rewards/perks and balances, and add a card-on-file for autopay (REQ-APP-1).

## How it works

My care/Rewards/Account tabs: visit history + consent-gated before/after photos (served via short-lived signed URLs (temporary, expiring links to stored photos), ADR-0009, never on device); points/perks/gift cards over PRD-06; profile, memberships, the client's own balance, and add/replace a tokenised card-on-file (Square) that feeds PRD-06 autopay (automatic recurring membership billing).
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

- [ ] **My care tab: visit history + treatment plan + medicines + documents**
  Behaviour: the My care health hub lists past visits, the ongoing treatment plan (what's due / course progress), the client's own medicines (S4 — Schedule 4 prescription-only medicine — record) and downloadable documents (signed consents, treatment records, receipts, aftercare PDFs). Requirements: all read-only over the owning modules (PRD-05 clinical, PRD-06 commerce) via the API; the medicines view is shown privately and never priced or advertised (AU advertising rules); documents download through the secure channel. The before/after gallery and the day-by-day aftercare are their own siblings (PHOTO-COMPARE, AFTERCARE-GUIDE).
- [ ] **Rewards tab over PRD-06 (points, perks, gift cards, referrals)**
  Behaviour: the Rewards tab shows the membership card, points balance / ledger, member perks, milestones, a give-$25/get-$25 referral with tracking, and gift-card redeem. Requirements: reads PRD-06 reward/membership data, the client's OWN figures only; rewards are never applied to S4 medicines (you can't discount or incentivise a prescription medicine); redemptions post back to PRD-06.
- [ ] **Account tab: profile, memberships, own balance + card-on-file (Square tokenise)**
  Behaviour: the Account tab surfaces profile, memberships, the client's own balance and 'Update card on file'. Requirements: card capture uses the Square SDK (software development kit) to tokenise on-device — no PAN (the raw card number) is ever stored or sent; the token posts to PRD-06 to feed membership autopay (automatic recurring billing); the client sees only their own balances, never clinic revenue; NO one-off online checkout is exposed (v1 payments are in-person). The 'Your data & privacy' entry point (CLIENT-PRIVACY) lives beneath these actions.
