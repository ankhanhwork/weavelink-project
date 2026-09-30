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
| Function list | 12 MFG modules; module-qualified function entries including the Sales/design collaboration extension | [`docs/function-list.md`](docs/function-list.md) |
| Use cases | 52 use cases with resolved actors, relationships, and functions | [`docs/architecture/use-case.md`](docs/architecture/use-case.md) |
| Architecture | Context diagram, system configuration, and end-to-end usage flow | [`docs/architecture/`](docs/architecture/) |
| Sequence diagrams | Business and operations sequences through SD-14, including SD-05A/05B and SD-13A prompt analysis | [`docs/architecture/sequence.md`](docs/architecture/sequence.md) |
| Screen catalogue | Workflow-grouped screens S01 through S50 with one MVP label per screen | [`docs/screen-list.md`](docs/screen-list.md) |
| Screen specifications | Detailed specifications and mockups for the current screens | [`screens/`](screens/) |
| Module specifications | Scope, actors, scenarios, flows, requirements, entities, business rules, success criteria, decisions, and traceability | [`specs/`](specs/) |
| MVP scope | Approved Must/Should/Could/Won't release scope, MVP rules and seed data | [`docs/prd.md`](../prd.md) |

## Main actors

- `Guest`: browses and searches products, registers, signs in, and requests account recovery.
- `Member`: umbrella term for an authenticated user; manages profile, password, notifications, and logout.
- `Customer`: the authorized representative of a Business Buyer or Reseller Shop; owns its designs and requests, approves samples, creates and tracks made-to-order production orders, acknowledges contracts, and pays.
- Customer accounts register at `/sign-up` and sign in at `/login` through the storefront shell. Dony employees use the separate internal CRM at `/staff/login`; System Admin provisions staff accounts and invitations through MFG-03. Employees cannot self-register, and neither portal supports Google, Facebook, or other third-party sign-in.
- `Sales`: a Dony employee who works only on assigned consultations, designs, customers, and permitted fulfilment records.
- `Sales Admin`: a Dony employee who manages Dony's product bases, customer requests, assignments, orders, contracts, payments, merge batches, and analytics.
- `System Admin`: a Dony employee who manages Dony staff accounts and operates configuration, logs, backup, and restore. This role does not provision customer companies as system tenants.
- `Payment Gateway (VNPay)`: external gateway; verified server IPN and reconciliation results are authoritative.

## MFG modules

| Module | Name | Functions | Use cases | Specification |
|---|---|---:|---:|---|
| MFG-01 | Identity & Access | 13 | 6 | [`spec-MFG-01.md`](specs/spec-MFG-01.md) |
| MFG-02 | Profile & Settings | 5 | 4 | [`spec-MFG-02.md`](specs/spec-MFG-02.md) |
| MFG-03 | Dony Staff Accounts | 8 | 4 | [`spec-MFG-03.md`](specs/spec-MFG-03.md) |
| MFG-04 | Product Catalog | 14 | 9 | [`spec-MFG-04.md`](specs/spec-MFG-04.md) |
| MFG-05 | Product Design | 21 | 5 | [`spec-MFG-05.md`](specs/spec-MFG-05.md) |
| MFG-06 | Order & Payment | 6 | 2 | [`spec-MFG-06.md`](specs/spec-MFG-06.md) |
| MFG-07 | Order Management | 7 | 3 | [`spec-MFG-07.md`](specs/spec-MFG-07.md) |
| MFG-08 | Sales | 8 | 3 | [`spec-MFG-08.md`](specs/spec-MFG-08.md) |
| MFG-09 | Contract Management | 9 | 6 | [`spec-MFG-09.md`](specs/spec-MFG-09.md) |
| MFG-10 | Order Optimization (Merge) | 7 | 4 | [`spec-MFG-10.md`](specs/spec-MFG-10.md) |
| MFG-11 | Data Analytics | 5 | 3 | [`spec-MFG-11.md`](specs/spec-MFG-11.md) |
| MFG-12 | System Operations | 8 | 3 | [`spec-MFG-12.md`](specs/spec-MFG-12.md) |
| **Total** | | **111** | **52** | |

## MVP Scope

The approved release scope is defined in [`docs/prd.md`](../prd.md), which is the single source for MVP priority. Each screen carries one MVP label (Must / Should / Could / Won't) in [`docs/screen-list.md`](docs/screen-list.md) and in its own Priority field; module FR priorities use the same labels. The complete-system documentation is retained for Should and Could items.

| Priority | Scope summary |
|---|---|
| **Must** | End-to-end standard order path: Customer and staff authentication (MFG-01), notifications (S13), catalog browse/detail (MFG-04), 2D self-design and saved-design gallery (MFG-05), quote, order, digital-design and physical-sample approval, fixed-template contract, VNPay deposit and balance (MFG-06, MFG-07, MFG-09). |
| **Should** | AI Compare, AI product advisory and AI virtual try-on; background removal and multi-angle mockups; keyword search and Product Finder; profile and change password (MFG-02); product administration S16–S18; payment list/reconciliation S41/S42; About/Contact; analytics Overview (S47). |
| **Could** | Design-rules editor (S19), assessed design service (S24, S26, S29), Sales pipeline and assignment (MFG-08), contract template administration (S43–S45), staff accounts (MFG-03), post-deposit cancellation with in-system refund, receipt auto-confirmation timer and Overdue handling, analytics funnel/AI/export, merge (MFG-10). |
| **Won't** | System operations (MFG-12): S49 configuration/backup/restore and S50 system logs. |

**MVP implementation slice:** implement one end-to-end standard order path in this sequence:

1. **Bootstrap and access:** seed the demo identities listed in the MVP scope (one Sales Admin, one Sales, one System Admin and one verified Customer) and one `CustomerAssignment` linking the demo Customer to the demo Sales. Sales Admin is the operational owner and lands on S36. Sales lands on S36 with read-only access to assigned-customer orders; an unassigned Sales account sees an empty list. System Admin is bootstrap-only and lands on S01. Routes of unreleased items return 404 and have no navigation link.
2. **Catalog and design:** seed at least one complete Published product base; Customers browse it and self-design/save through MFG-04/MFG-05. Checkout has no merge option and `design_fee_vnd=0`.
3. **Quote, order and physical sample:** create a standard quote and order; the Customer approves the digital design; Sales Admin records sample preparation and dispatch; the Customer records sample receipt and approval. A requested revision returns to a new design/quote approval cycle.
4. **Contract and deposit:** after sample approval, Sales Admin explicitly selects Generate in S39 using the single fixed template; the Customer acknowledges it in S38 with consent and matching typed name before paying the exact VNPay deposit. This acknowledgement is not a certified digital signature.
5. **Production, delivery and balance:** Sales Admin advances the paid order through InProduction and Shipped and records verified delivery evidence. The Customer confirms receipt, or Sales Admin confirms it on the Customer's behalf (MFG-06 BR-019); the exact VNPay balance then completes the order. Staff cannot mark an order paid.

**MVP rules (MFG-06 BR-019):** cancellation only before a successful deposit; no in-system refund (a late deposit on a Cancelled order is flagged for manual refund); no 3-day auto-confirmation timer; `balance_due_at` is displayed without Overdue automation.

Business rules have a single source: the owning module specification.

## Suggested reading order

1. [Architecture context](docs/architecture/context.md)
2. [System configuration](docs/architecture/system-configuration.md)
3. [Use cases](docs/architecture/use-case.md)
4. [Function list](docs/function-list.md)
5. The relevant module specification in [specs/](specs/)
6. Its linked screen specifications and [sequence diagrams](docs/architecture/sequence.md)
