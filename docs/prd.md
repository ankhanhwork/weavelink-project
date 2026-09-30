# MVP Scope v3: WeaveLink

| Field | Value |
|---|---|
| Status | Approved by Group B, 2026-09-28 |
| Role | Single source for MVP release priority. Module specs, `docs/screen-list.md` and screen Priority fields use the same labels. |

## 1. Priority labels

- **Must**: required for the end-to-end order path: sign up → choose a product → design → order → approve digital design → approve physical sample → sign contract → pay deposit → production and delivery → pay balance → complete.
- **Should**: built immediately after Must; includes the AI features.
- **Could**: built only if time allows.
- **Won't**: excluded from this release.

Routes of unreleased items return 404 and have no navigation link. Seed data replaces any unreleased administration screen that the Must path depends on.

## 2. Must

| # | Item | Module | Screens | Functions | MVP scope |
|---|---|---|---|---|---|
| M-1 | Customer sign-up, email verification, login, logout, password recovery | MFG-01 | S04–S07 | F-USER-001 → 011 | Email/password only |
| M-2 | Staff login and password recovery | MFG-01 | S08–S10 | F-USER-004, 005, 007 → 011 | Seeded staff accounts; no invitation acceptance |
| M-3 | Home, catalog, product detail | MFG-04 | S01, S14, S15 | F-PROD-001, 002 | Browse, category filter, pagination, detail/options |
| M-4 | 2D design tool | MFG-05 | S20 | F-DES-001 → 003 | Front/back, ≤5 uploads, mm placement, canvas preview, immutable saved versions |
| M-5 | Saved-design gallery | MFG-05 | S25 (Saved tab) | F-DES-004 (Saved) | Requested tab hidden |
| M-6 | Create order, quote, order summary | MFG-06 | S30, S33 | F-PAY-001 → 003 | Standard order; `merge_opt_in=false`, `merge_discount_vnd=0`, `design_fee_vnd=0` |
| M-7 | Customer orders | MFG-06, MFG-07 | S34, S35 | F-ORD-001 → 004; MFG-06 FR-003 | Digital-design and sample approval or revision, receipt confirmation, pre-deposit cancellation |
| M-8 | Staff orders | MFG-07 | S36, S37 | F-ORD-005 → 007 | Sales Admin runs sample, production, shipping, delivery evidence and receipt confirmation on the Customer's behalf; Sales is read-only on seeded assignments |
| M-9 | Fixed-template contract | MFG-09 | S39, S38 | F-CONTR-003, 004, 005, 008, 009 | Sales Admin selects Generate; Customer consents and types matching name; not a certified digital signature |
| M-10 | VNPay sandbox deposit and balance | MFG-06 | S40 | F-PAY-004 → 006 | IPN and reconciliation are authoritative; browser return is read-only |
| M-11 | In-app notifications | MFG-01 | S13 | F-USER-012, 013 | List, mark read, reauthorized links; email is secondary |

### 2.1 MVP rules (MFG-06 BR-019)

| # | Full-system rule | MVP rule |
|---|---|---|
| R-1 | Cancellation allowed until `InProduction`, with refund of captured funds (MFG-06 BR-013) | Cancellation only from `AwaitingDigitalApproval` through `AwaitingDeposit` while no deposit has succeeded; `Confirmed` onward returns 409 |
| R-2 | Late deposit on a Cancelled order is refunded automatically | Deposit is recorded, the order is flagged `manual_refund_required`, Sales Admin is notified, and the refund is handled outside the system |
| R-3 | Verified delivery evidence starts a 3-day auto-confirmation timer (MFG-06 BR-007) | No timer; the Customer confirms receipt, or Sales Admin confirms it on the Customer's behalf after recording verified evidence (audited) |
| R-4 | 7-day balance deadline with `Overdue` substate and notifications (MFG-06 BR-014) | `balance_due_at` is displayed only; no Overdue automation |
| R-5 | Sales assignment through MFG-08 | One seeded `CustomerAssignment` links the demo Customer to the demo Sales |

### 2.2 Required seed data

- At least one Published product with variants, sizes, colours, materials, print options, volume-tier prices, images and design rules.
- One active fixed contract template.
- Accounts: one Sales Admin, one Sales, one System Admin, one verified Customer.
- One `CustomerAssignment` for the demo Customer and demo Sales.
- All data is synthetic; no real personal data or live credentials.

## 3. Should

| # | Item | Module | Screens | Functions | Scope |
|---|---|---|---|---|---|
| SH-1 | AI Compare | MFG-04 | S14, S15 | F-PROD-013 | 2–4 Published products in one branch; Guests can view results; catalogue data only |
| SH-2 | AI product advisory | MFG-04 | S14 | F-PROD-014 | Free-form questions grounded in the Published catalogue; login required; 4 suggestions by default, 8 max |
| SH-3 | AI virtual try-on | MFG-05 | S23 | F-DES-016 | Synthetic presets; personal photo only after explicit consent; session-only; never a design asset or order attachment |
| SH-4 | Background removal | MFG-05 | S21 | F-DES-014 | Review/apply/cancel; placement unchanged |
| SH-5 | Multi-angle mockups | MFG-05 | S22 | F-DES-015 | Front/back views first; remaining angles if time allows |
| SH-6 | Keyword search and Product Finder | MFG-04 | S14 | F-PROD-003, 012 | |
| SH-7 | Profile and change password | MFG-02 | S11, S12 | F-PROF-001 → 005 | |
| SH-8 | Product administration | MFG-04 | S16–S18 | F-PROD-004 → 011 | Seed data stays the demo source |
| SH-9 | Payment list and reconciliation | MFG-06 | S41, S42 | F-PAY-005 (reconcile) | No in-system refund |
| SH-10 | About and Contact | — | S02, S03 | — | Static pages |
| SH-11 | Analytics Overview | MFG-11 | S47 (Overview) | F-DA-001, 002 (Overview) | Revenue, cash, orders, cancellations, new customers; no funnel or AI |

The AI provider and model are chosen at Plan. If an AI service is unavailable, the feature shows a safe error and the Must path is unaffected.

## 4. Could

| # | Item | Module | Screens | Functions |
|---|---|---|---|---|
| C-1 | Design-rules editor | MFG-04 | S19 | F-PROD-007, 008 (rules) |
| C-2 | Assessed design service and staff design collaboration | MFG-05 | S24, S25 (Requested), S26, S29 | F-DES-005 → 013, 017 → 021 |
| C-3 | Sales pipeline and assignment | MFG-08 | S27, S28 | F-SALES-001 → 008 |
| C-4 | Contract template administration and regeneration | MFG-09 | S43–S45 | F-CONTR-001, 002, 006, 007 |
| C-5 | Staff accounts and invitation acceptance | MFG-03 | S48, S08 (invitation) | F-ACC-001 → 008 |
| C-6 | Full cancellation/refund, auto-confirmation timer and Overdue | MFG-06, MFG-07 | S35, S37, S42 | MFG-06 BR-007, BR-013, BR-014 |
| C-7 | Analytics funnel, prompt analysis and export | MFG-11 | S47 | F-DA-003, 004, 006 |
| C-8 | Order merge | MFG-10 | S31, S32, S46 | F-MER-001 → 007 |

## 5. Won't

| Item | Module | Screens | Replacement |
|---|---|---|---|
| System configuration, backup and restore | MFG-12 | S49 | Environment configuration (`.env`) |
| System log viewer | MFG-12 | S50 | Standard runtime application logs |

## 6. MVP done criteria

- A demo Customer completes: sign up → design → order → digital approval → sample receipt and approval → contract → VNPay deposit → receipt → balance → `Completed`.
- A sample revision returns the order to `AwaitingDigitalApproval` with new design/quote versions; prior evidence is kept.
- No gate can be skipped (contract before sample approval, deposit before contract, balance before receipt).
- Deposit plus balance equals the contract total in integer VND; duplicate IPNs never settle twice.
- Cancellation succeeds only before a successful deposit.
- Sales sees only assigned-customer orders; Sales Admin sees all; a Customer sees only their own orders.
- Unreleased routes return 404 and have no navigation link.
