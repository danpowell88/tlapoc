# Checkout, memberships & pricing — overview

> Taking payment in person, the membership/loyalty engine, and the owner's pricing planner. The books
> themselves live in **Xero** — this area is the point-of-sale and the commercial levers. Primary owners:
> **Reception** (POS), **Owner** (memberships & pricing).

## What's in this area

| Function | What it does | When it's used | Primary role(s) |
|---|---|---|---|
| Checkout / POS | In-person payment (Square card + cash + gift card); upsell cues; post-pay rebook | End of every visit | Reception |
| Rewards at checkout | Apply member rewards — **non-S4 only** | At payment | Reception |
| Memberships & packages | Plans, packages, autopay (card-on-file) + dunning retry | Sign-up + billing cycle | Reception, Owner |
| Loyalty & referrals | Points, referral credit — **non-S4 value only** | Ongoing | Reception, Owner |
| Gift cards | Issue + redeem | Ad hoc | Reception |
| Pricing & what-if | Model price/plan changes and the revenue/MRR impact before applying | Planning | Owner |

## Workflows

### 1 · Checkout & rebook  — *Reception*

```mermaid
flowchart TD
  A[Visit set For checkout] --> B[Open cart - services + products]
  B --> C{Member?}
  C -->|Yes| D[Apply reward - non-S4 only]
  C -->|No| E[Offer membership / restock]
  D --> F[Take payment - Square / cash / gift card]
  E --> F
  F --> G[Invoice + payment sync to Xero]
  G --> H[Post-pay rebook on the treatment interval]
  H --> I[Visit Done -> recall set]
```

### 2 · Membership autopay & dunning  — *system + Reception*

```mermaid
flowchart TD
  A[Billing day] --> B[Charge card-on-file]
  B --> C{Success?}
  C -->|Yes| D[Receipt + Xero sync]
  C -->|No| E[Dunning retry schedule]
  E --> F{Recovered?}
  F -->|Yes| D
  F -->|No| G[Failed-payment job to Reception<br/>shown in owner exceptions]
```

### 3 · Pricing what-if  — *Owner*

```mermaid
flowchart LR
  A[Owner edits a price/plan] --> B[Model on read-models<br/>+ churn/elasticity assumption]
  B --> C[Projected revenue / MRR impact]
  C --> D{Apply?}
  D -->|Yes| E[Apply via audited catalogue admin]
  D -->|No| F[Discard - nothing changed live]
```

## Roles at a glance

| Role | Responsibilities in this area |
|---|---|
| **Reception** | Take payment, apply rewards, sell memberships/gift cards, rebook |
| **Owner** | Sets prices, plans & deals; runs what-if; sees MRR & dunning exceptions |
| **All staff** | Rewards/discounts are blocked on anything S4 by construction |

## Related

- Requirements: `REQ-PAY-6`, `REQ-MEMB-8/9/10`, compliance `C9/C23`
- ADRs: **ADR-0007** (payment provider), **ADR-0014** (S4 flag blocks rewards), **ADR-0022** (pricing what-if)
- PRDs: [PRD-06](../prds/PRD-06-payments-memberships-rewards.md)
