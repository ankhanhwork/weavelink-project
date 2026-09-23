# WeaveLink Platform

WeaveLink is a web-based system for Dony, a made-to-order garment factory. Dony does not sell ready-made clothing from inventory: every commercial order is manufactured for a customer's selected garment specifications, artwork or design, quantity, and production requirements. WeaveLink supports product-base discovery, customization, design services, sample approval, ordering, payment, contract management, sales consultation, production optimization, analytics, and internal administration. The Customer experience is Dony's public storefront; Dony employees use a separate internal CRM and operations portal.

## Dony business model

Dony serves two closely related made-to-order customer models:

- **B2B — Business Buyer:** a company commissions Dony to manufacture uniforms or other garments for its employees or internal use.
- **B2B2C — Reseller Shop:** a clothing shop commissions Dony to manufacture garments from the shop's own design, brand requirements, or specifications, then sells those manufactured garments to the shop's customers.

A Reseller Shop does **not** buy Dony ready-made stock for resale. In both models, Dony manufactures against a customer-specific order. The public Product Catalog therefore represents configurable garment bases, materials, colours, print or embroidery methods, and production rules; it is not an inventory of finished garments available for immediate purchase.

WeaveLink is operated by one manufacturer, Dony. It is not a multi-tenant marketplace and does not provision other manufacturers or customer companies as system operators. A customer account may represent a Business Buyer or Reseller Shop, while `Sales`, `Sales Admin`, and `System Admin` are Dony employees. Information about a buyer's company or shop is customer and billing data, not a tenant or staff-authorization boundary. Customer pages share the storefront header/navigation and footer; employee pages use internal CRM navigation and must not reuse the customer-store shell. Customer authentication routes are `/sign-up`, `/login`, `/forgot-password`, and `/reset-password`; employee routes are `/staff/login`, `/staff/forgot-password`, and `/staff/reset-password`. Both use email/password only, with no Google, Facebook, or other third-party login.

This repository contains the software design documentation for the DBIZ 3 Group B classroom project. It contains specifications, traceability tables, screen descriptions, mockups, and architecture diagrams; no application source code or runtime setup is included. The documents define the complete target system while the MVP scope below determines implementation priority.

## Documentation overview

| Area | Contents | Location |
|---|---|---|
| Function list | 12 MFG modules and 96 module-qualified function entries | [`docs/function-list.md`](docs/function-list.md) |
| Use cases | 49 use cases with resolved actors, relationships, and functions | [`docs/architecture/use-case.md`](docs/architecture/use-case.md) |
| Architecture | Context diagram, system configuration, and end-to-end usage flow | [`docs/architecture/`](docs/architecture/) |
| Sequence diagrams | 10 sequences covering SD-01 through SD-09, including SD-05A and SD-05B | [`docs/architecture/sequence.md`](docs/architecture/sequence.md) |
| Screen catalogue | 45 documented screen entries; S16 is intentionally retired, and Customer/employee authentication screens are separate | [`docs/screen-list.md`](docs/screen-list.md) |
| Screen specifications | 45 detailed screen specs; S16 has no screen or image because design-service fees are not paid as a separate transaction | [`screens/`](screens/) |
| Module specifications | Scope, actors, scenarios, flows, requirements, entities, business rules, success criteria, decisions, and traceability | [`specs/`](specs/) |

## Main actors

- `Guest`: browses and searches products, registers, signs in, and requests account recovery.
- `Member`: umbrella term for an authenticated user; manages profile, password, notifications, and logout.
- `Customer`: the authorized representative of a Business Buyer or Reseller Shop; owns its designs and requests, approves samples, creates and tracks made-to-order production orders, acknowledges contracts, and pays.
- Customer accounts register at `/sign-up` and sign in at `/login` through the storefront shell. Dony employees use the separate internal CRM at `/staff/login`; System Admin provisions staff accounts and invitations through MFG-03. Employees cannot self-register, and neither portal supports Google, Facebook, or other third-party sign-in.
- `Sales`: a Dony employee who works only on assigned consultations, designs, customers, and permitted fulfilment records. Historical DBIZ2 material may call this role `Sales Consultant`.
- `Sales Admin`: a Dony employee who manages Dony's product bases, customer requests, assignments, orders, contracts, payments, merge batches, and analytics. Historical DBIZ2 material may call this role `Company Admin`.
- `System Admin`: a Dony employee who manages Dony staff accounts and operates configuration, logs, backup, and restore. This role does not provision customer companies as system tenants.
- `Payment Gateway (VNPay)`: external gateway; verified server IPN and reconciliation results are authoritative.

## MFG modules

| Module | Name | Functions | Use cases | Specification |
|---|---|---:|---:|---|
| MFG-01 | Identity & Access | 11 | 5 | [`spec-MFG-01.md`](specs/spec-MFG-01.md) |
| MFG-02 | Profile & Settings | 5 | 4 | [`spec-MFG-02.md`](specs/spec-MFG-02.md) |
| MFG-03 | Dony Staff Accounts | 8 | 4 | [`spec-MFG-03.md`](specs/spec-MFG-03.md) |
| MFG-04 | Product Catalog | 11 | 7 | [`spec-MFG-04.md`](specs/spec-MFG-04.md) |
| MFG-05 | Product Design | 13 | 5 | [`spec-MFG-05.md`](specs/spec-MFG-05.md) |
| MFG-06 | Order & Payment | 6 | 2 | [`spec-MFG-06.md`](specs/spec-MFG-06.md) |
| MFG-07 | Order Management | 7 | 3 | [`spec-MFG-07.md`](specs/spec-MFG-07.md) |
| MFG-08 | Sales | 8 | 3 | [`spec-MFG-08.md`](specs/spec-MFG-08.md) |
| MFG-09 | Contract Management | 9 | 6 | [`spec-MFG-09.md`](specs/spec-MFG-09.md) |
| MFG-10 | Order Optimization (Merge) | 7 | 4 | [`spec-MFG-10.md`](specs/spec-MFG-10.md) |
| MFG-11 | Data Analytics | 3 | 3 | [`spec-MFG-11.md`](specs/spec-MFG-11.md) |
| MFG-12 | System Operations | 8 | 3 | [`spec-MFG-12.md`](specs/spec-MFG-12.md) |
| **Total** | | **96** | **49** | |

## MVP Scope

The MVP scope is defined by feature priority. It does not remove lower-priority modules from the complete-system documentation.

| Priority | Feature / Item | MFG | Notes |
|---|---|---|---|
| **Must** | Role-based Authentication & Access (Customer, Sales, Sales Admin) | MFG-01 | Required login/authorization roles; initial Dony staff identities are pre-provisioned because staff-account administration is deferred |
| **Must** | Product Catalog (browse, search, view product detail) | MFG-04 | Entry point for choosing a base product |
| **Must** | Product Design Workspace (self-design, upload artwork, preview, save design) | MFG-05 | Core customization workflow |
| **Must** | Order & Payment (standard checkout, VNPay deposit and balance, order creation) | MFG-06 | MVP uses the standard single-order path; merge pricing/batching is deferred with MFG-10. The order path also requires the minimum MFG-07/MFG-09 slices below before the MVP is complete. |
| **Should** | Order Tracking & Status Updates | MFG-07 | Full tracking automation is deferred; the MVP-required slice uses authenticated Dony staff to record sample preparation/dispatch, production and shipment, with Customer sample approval and receipt confirmation. |
| **Should** | Digital Contract Generation & E-signature acknowledgement | MFG-09 | Full template administration/signature enhancements are deferred; the MVP-required slice uses one fixed contract template, immutable order/sample terms, and a recorded Customer acceptance before deposit. |
| **Could** | Order Optimization / Merge | MFG-10 | Valuable after order volume increases; MFG-10 v3 is the canonical source for merge-policy formulas and numeric assumptions. |
| **Could** | Assessed Design Service Request | MFG-05 | Simple work is free; accepted Complex fee is collected with the first order from the delivered design |
| **Could** | Sales Assignment & Task Dashboard | MFG-08 | Needed when consultation volume requires a dedicated queue |
| **Won't** | Profile & Settings | MFG-02 | Deferred from MVP; hide Profile/S06 and Change Password/S07 navigation/routes while retaining account recovery in MFG-01. |
| **Won't** | Data Analytics Dashboard & Data Export | MFG-11 | Deferred until sufficient order history exists |
| **Won't** | Dony Staff Account Administration & System Operations | MFG-03, MFG-12 | Invitation/role-management UI, configurable operations, logs, backup and restore are deferred. Pre-provision one `Sales Admin` for order/sample/contract operations, one `Sales` identity for role/assignment checks, and one `System Admin` bootstrap identity; also seed one verified Customer test account. These are demo identities, not self-registration or live credentials. |

### MVP Priority Summary

- **Must:** MFG-01, MFG-04, self-design in MFG-05, and MFG-06.
- **Should:** Full MFG-07 and MFG-09 capabilities beyond the minimum order-completion slices required for the MVP vertical path.
- **Could:** assessed design service in MFG-05, MFG-08, and MFG-10.
- **Won't:** MFG-02 profile/settings screens, MFG-03 staff-account UI, MFG-11 analytics, and MFG-12 system-operations screens are omitted in MVP. Hide the Profile/S06 link; account recovery remains available through the relevant Customer or staff recovery screens.

**MVP implementation slice:** “Should” describes the full MFG-07/MFG-09 modules, not permission to omit their order-critical minimums. Implement one end-to-end standard order path in this sequence:

1. **Bootstrap and access:** pre-provision the seed identities listed above; support Customer, Sales and Sales Admin authentication/authorization. Sales Admin is the MVP operational owner and lands on S28 after login; it can perform required Dony sample, contract and order updates without MFG-08 assignment queues. Seeded Sales and System Admin accounts are for authentication/authorization testing only: after login they land on public S01, with no staff-only MVP functions; attempts to open deferred S20/S41 or other unauthorized staff routes return 404/403 per the route-disclosure rule. System Admin is bootstrap-only; MFG-03/MFG-12 management screens are not MVP deliverables.
2. **Catalog and design:** seed at least one complete, Published Dony product base with valid variants, size/colour/material/print options, prices, assets and compatible design rules before release; Customers browse it and self-design/save through MFG-04/MFG-05. MVP does not require product-admin CRUD screens. Exclude assessed design service and merge opt-in/discounts from MVP checkout.
3. **Quote, order and physical sample:** create a standard quote and order; Customer approves the digital design; Sales Admin manually records sample preparation and dispatch evidence/tracking; Customer records sample receipt and approval. A requested revision returns to a new design/quote approval cycle.
4. **Contract and deposit:** after sample approval, Sales Admin explicitly selects Generate in S33; the system generates the Customer's immutable contract from the single fixed Dony template (no automatic generation or template picker in MVP). Record consent, authenticated Customer acceptance/name, contract version and timestamp before allowing the exact VNPay deposit. This application acknowledgement is not represented as a certified digital signature.
5. **Production, delivery and balance:** Sales Admin manually advances the paid order through InProduction and Shipped with required evidence/tracking. The Customer confirms receipt, or the system auto-confirms under MFG-06 BR-007 after its 3-calendar-day dispute window if no dispute is filed; only then allow the exact VNPay balance. The classroom balance deadline is 7 calendar days after verified delivery. Verified deposit/balance notifications, cancellation/refund protections and final order completion remain mandatory; staff cannot mark an order paid manually.

## Use Case ID convention

Use Case IDs use the format `UC-<actor initial><number>`:

- `UC-G01` to `UC-G03`: Guest.
- `UC-M01` to `UC-M08`: Member or unauthenticated account-access flow.
- `UC-C01` to `UC-C27`: Customer or Sales Admin; consult the actor column rather than inferring from the initial.
- `UC-S01` to `UC-S11`: Sales or System Admin; consult the actor column rather than inferring from the initial.

The authoritative actor association is recorded in [`docs/architecture/use-case.md`](docs/architecture/use-case.md). Because MFG-07 and MFG-08 both inherit `F-ORD-*` IDs, cross-module references always include the module, for example `MFG-07/F-ORD-003` and `MFG-08/F-ORD-003`.

## Architecture and flows

1. [`context.md`](docs/architecture/context.md) shows actors and external services around WeaveLink.
2. [`system-configuration.md`](docs/architecture/system-configuration.md) shows logical frontend, backend, storage, worker, and integration boundaries.
3. [`usage-flow.md`](docs/architecture/usage-flow.md) follows both design routes through contract, payment, production, and delivery.
4. [`sequence.md`](docs/architecture/sequence.md) records the detailed message flows.

## Traceability

The documents retain the original identifier layers: `MFG-*`, `UC-*`, `F-*`, module-local `FR-*`, 45 active screen IDs (`S01`–`S15` and `S17`–`S46`; S16 is retired), `SD-*`, and `ILF-*`. Each module spec maps its scenarios, requirements, screens, entities, business rules, and success criteria back to these identifiers.

When documentation conflicts, apply this precedence for release scope and behavior: (1) README MVP implementation slice and explicit policy decisions, (2) relevant module specification, (3) screen specification, (4) architecture sequence diagram. The `MVP` column in [`docs/screen-list.md`](docs/screen-list.md) is authoritative only for whether a screen/subset ships. Screen `P1/P2/P3` and function-list `High/Medium/Low` are artefact-local rankings and do not replace project MoSCoW scope. Business-rule values must be defined in the owning module spec; lower-level documents reference them rather than redefining them.

## Open clarification areas

The project is a classroom demo, uses clearly labelled fictional organization/contact data, has no external approver, and requires no further DBIZ2 source comparison. For a runnable classroom MVP, use the explicitly fictional demo assumptions in MFG-04 (MOQ 10 and sample volume-tier/surcharge data), MFG-06 (30,000 VND shipping, zero demo tax, full refund before InProduction, 3-day receipt-dispute window, and 7-day balance deadline), and S22 (minimum Buyer Organization snapshot for Business Buyer/Reseller Shop). MFG-05's existing design, asset, approval and revision logic remains authoritative; this project does not replace it with a simplified canvas or an invented revision cap. These values are coursework defaults, not verified Dony commercial commitments or legal/tax advice; replace them with approved business/legal values before production deployment.

## Suggested reading order

1. [`docs/architecture/context.md`](docs/architecture/context.md)
2. [`docs/architecture/system-configuration.md`](docs/architecture/system-configuration.md)
3. [`docs/architecture/use-case.md`](docs/architecture/use-case.md)
4. [`docs/function-list.md`](docs/function-list.md)
5. The relevant module file in [`specs/`](specs/)
6. The linked screen and sequence documents
