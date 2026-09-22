# WeaveLink Platform

WeaveLink is a web based client server platform for product browsing, product customization, design services, ordering, payment, contract management, sales consultation, order optimization, analytics, and system administration.

This repository contains the software design documentation for the DBIZ 3 Group B classroom project. It contains specifications, traceability tables, screen descriptions, mockups, and architecture diagrams; no application source code or runtime setup is included. The documents define the complete target system while the MVP scope below determines implementation priority.

## Documentation overview

| Area | Contents | Location |
|---|---|---|
| Function list | 12 MFG modules and 96 module-qualified function entries | [`docs/function-list.md`](docs/function-list.md) |
| Use cases | 49 use cases with resolved actors, relationships, and functions | [`docs/architecture/use-case.md`](docs/architecture/use-case.md) |
| Architecture | Context diagram, system configuration, and end-to-end usage flow | [`docs/architecture/`](docs/architecture/) |
| Sequence diagrams | 10 sequences covering SD-01 through SD-09, including SD-05A and SD-05B | [`docs/architecture/sequence.md`](docs/architecture/sequence.md) |
| Screen catalogue | 43 documented screen entries, including deprecated S16 | [`docs/screen-list.md`](docs/screen-list.md) |
| Screen specifications | 43 detailed screen specs (S16 retained as deprecated); 17 have supplied PNG mockups and 26 explicitly record that no mockup is available | [`screens/`](screens/) |
| Module specifications | Scope, actors, scenarios, flows, requirements, entities, business rules, success criteria, decisions, and traceability | [`specs/`](specs/) |

## Main actors

- `Guest`: browses and searches products, registers, signs in, and requests account recovery.
- `Member`: umbrella term for an authenticated user; manages profile, password, notifications, and logout.
- `Customer`: owns designs and service requests, creates and tracks orders, acknowledges contracts, and pays.
- `Sales Consultant`: works only on assigned consultations and permitted fulfillment records.
- `Company Admin`: manages data belonging to one company, including products, assignments, orders, contracts, payments, batches, and analytics.
- `System Admin`: provisions companies and staff and operates configuration, logs, backup, and restore.
- `Payment Gateway (VNPay)`: external gateway; verified server IPN and reconciliation results are authoritative.

## MFG modules

| Module | Name | Functions | Use cases | Specification |
|---|---|---:|---:|---|
| MFG-01 | Identity & Access | 11 | 5 | [`spec-MFG-01.md`](specs/spec-MFG-01.md) |
| MFG-02 | Profile & Settings | 5 | 4 | [`spec-MFG-02.md`](specs/spec-MFG-02.md) |
| MFG-03 | Company Accounts | 8 | 4 | [`spec-MFG-03.md`](specs/spec-MFG-03.md) |
| MFG-04 | Product Catalog | 11 | 7 | [`spec-MFG-04.md`](specs/spec-MFG-04.md) |
| MFG-05 | Product Design | 13 | 5 | [`spec-MFG-05.md`](specs/spec-MFG-05.md) |
| MFG-06 | Order & Payment | 6 | 2 | [`spec-MFG-06.md`](specs/spec-MFG-06.md) |
| MFG-07 | Order Management | 7 | 3 | [`spec-MFG-07.md`](specs/spec-MFG-07.md) |
| MFG-08 | Sales Consultant | 8 | 3 | [`spec-MFG-08.md`](specs/spec-MFG-08.md) |
| MFG-09 | Contract Management | 9 | 6 | [`spec-MFG-09.md`](specs/spec-MFG-09.md) |
| MFG-10 | Order Optimization (Merge) | 7 | 4 | [`spec-MFG-10.md`](specs/spec-MFG-10.md) |
| MFG-11 | Data Analytics | 3 | 3 | [`spec-MFG-11.md`](specs/spec-MFG-11.md) |
| MFG-12 | System Operations | 8 | 3 | [`spec-MFG-12.md`](specs/spec-MFG-12.md) |
| **Total** | | **96** | **49** | |

## MVP Scope

The MVP scope is defined by feature priority. It does not remove lower-priority modules from the complete-system documentation.

| Priority | Feature / Item | MFG | Notes |
|---|---|---|---|
| **Must** | Role-based Authentication & Access (Customer, Sales Consultant, Company Admin) | MFG-01 | Foundation for secure role-aware access |
| **Must** | Product Catalog (browse, search, view product detail) | MFG-04 | Entry point for choosing a base product |
| **Must** | Product Design Workspace (self-design, upload artwork, preview, save design) | MFG-05 | Core customization workflow |
| **Must** | Order & Payment (checkout, VNPay integration, order creation) | MFG-06 | Core revenue workflow |
| **Should** | Order Tracking & Status Updates | MFG-07 | Manual tracking is an acceptable temporary launch fallback |
| **Should** | Digital Contract Generation & E-signature acknowledgement | MFG-09 | Email or paper contract is an acceptable temporary launch fallback |
| **Could** | Order Optimization / Merge | MFG-10 | Valuable after order volume increases |
| **Could** | Assessed Design Service Request | MFG-05 | Simple work is free; accepted Complex fee is collected with the first order from the delivered design |
| **Could** | Sales Consultant Assignment & Task Dashboard | MFG-08 | Needed when consultation volume requires a dedicated queue |
| **Won't** | Data Analytics Dashboard & Data Export | MFG-11 | Deferred until sufficient order history exists |
| **Won't** | Company Accounts & System Operations | MFG-03, MFG-12 | One configured admin is sufficient for the MVP |

### MVP Priority Summary

- **Must:** MFG-01, MFG-04, self-design in MFG-05, and MFG-06.
- **Should:** MFG-07 and MFG-09.
- **Could:** assessed design service in MFG-05, MFG-08, and MFG-10.
- **Won't:** MFG-03, MFG-11, and MFG-12 for the MVP release.

## Use Case ID convention

Use Case IDs use the format `UC-<actor initial><number>`:

- `UC-G01` to `UC-G03`: Guest.
- `UC-M01` to `UC-M08`: Member or unauthenticated account-access flow.
- `UC-C01` to `UC-C27`: Customer or Company Admin; consult the actor column rather than inferring from the initial.
- `UC-S01` to `UC-S11`: Sales Consultant or System Admin; consult the actor column rather than inferring from the initial.

The authoritative actor association is recorded in [`docs/architecture/use-case.md`](docs/architecture/use-case.md). Because MFG-07 and MFG-08 both inherit `F-ORD-*` IDs, cross-module references always include the module, for example `MFG-07/F-ORD-003` and `MFG-08/F-ORD-003`.

## Architecture and flows

1. [`context.md`](docs/architecture/context.md) shows actors and external services around WeaveLink.
2. [`system-configuration.md`](docs/architecture/system-configuration.md) shows logical frontend, backend, storage, worker, and integration boundaries.
3. [`usage-flow.md`](docs/architecture/usage-flow.md) follows both design routes through contract, payment, production, and delivery.
4. [`sequence.md`](docs/architecture/sequence.md) records the detailed message flows.

## Traceability

The documents retain the original identifier layers: `MFG-*`, `UC-*`, `F-*`, module-local `FR-*`, `S01` through `S43`, `SD-*`, and `ILF-*`. Each module spec maps its scenarios, requirements, screens, entities, business rules, and success criteria back to these identifiers.

## Open clarification areas

All inherited clarification markers and open questions have been resolved as implementation decisions in the relevant specification. The project is a classroom demo, uses clearly labelled fictional organization/contact data, has no external approver, and requires no further DBIZ2 source comparison. No unresolved item currently blocks implementation.

## Suggested reading order

1. [`docs/architecture/context.md`](docs/architecture/context.md)
2. [`docs/architecture/system-configuration.md`](docs/architecture/system-configuration.md)
3. [`docs/architecture/use-case.md`](docs/architecture/use-case.md)
4. [`docs/function-list.md`](docs/function-list.md)
5. The relevant module file in [`specs/`](specs/)
6. The linked screen and sequence documents
