# WeaveLink Platform

WeaveLink is a web based client server platform for product browsing, product customization, design services, ordering, payment, contract management, sales consultation, order optimization, analytics, and system administration.

This repository contains the software design documentation for the platform. It currently contains specifications, traceability tables, screen descriptions, mockups, and architecture diagrams; no application source code or runtime setup instructions are included.

## Documentation overview

| Area | Contents | Location |
|---|---|---|
| Function list | 12 MFG modules and 94 functions with 94 subfunction entries and annotated inputs/outputs | [`docs/function-list.md`](docs/function-list.md) |
| Use cases | 49 use cases with generated IDs, actors, and subfunction relationships | [`docs/architecture/use-case.md`](docs/architecture/use-case.md) |
| Architecture | Context diagram, system configuration, and usage flow | [`docs/architecture/context.md`](docs/architecture/context.md), [`docs/architecture/system-configuration.md`](docs/architecture/system-configuration.md), [`docs/architecture/usage-flow.md`](docs/architecture/usage-flow.md) |
| Sequence diagrams | 10 sequences covering SD-01 through SD-09, including SD-05A and SD-05B | [`docs/architecture/sequence.md`](docs/architecture/sequence.md) |
| Screen catalogue | 40 documented screen entries | [`docs/screen-list.md`](docs/screen-list.md) |
| Screen specifications | 17 detailed screen specs with matching PNG mockups | [`screens/`](screens/) and [`screens/img/`](screens/img/) |
| Module specifications | Detailed scope, actors, scenarios, acceptance criteria, flows, requirements, entities, rules, and traceability | [`specs/`](specs/) |

## Main actors

- `Guest`: browses products, searches products, and registers an account.
- `Member`: signs in, manages profile settings, and uses account recovery and logout.
- `Customer`: customizes products, requests design services, places and tracks orders, signs contracts, and pays.
- `Sales Consultant`: views assignments, manages consultations, sends completed designs, and updates order status.
- `Company Admin`: manages products, contracts, order optimization, analytics, and consultant assignments.
- `System Admin`: manages company accounts, system logs, backups, restores, and system configuration.
- `Payment Gateway (VNPay)`: external payment service used by payment flows.

## MFG modules

| Module | Name | Functions | Use cases | Specification |
|---|---|---:|---:|---|
| MFG-01 | Identity & Access | 11 | 5 | [`spec-MFG-01.md`](specs/spec-MFG-01.md) |
| MFG-02 | Profile & Settings | 5 | 4 | [`spec-MFG-02.md`](specs/spec-MFG-02.md) |
| MFG-03 | Company Accounts | 8 | 4 | [`spec-MFG-03.md`](specs/spec-MFG-03.md) |
| MFG-04 | Product Catalog | 11 | 7 | [`spec-MFG-04.md`](specs/spec-MFG-04.md) |
| MFG-05 | Product Design | 11 | 5 | [`spec-MFG-05.md`](specs/spec-MFG-05.md) |
| MFG-06 | Order & Payment | 6 | 2 | [`spec-MFG-06.md`](specs/spec-MFG-06.md) |
| MFG-07 | Order Management | 7 | 3 | [`spec-MFG-07.md`](specs/spec-MFG-07.md) |
| MFG-08 | Sales Consultant | 8 | 3 | [`spec-MFG-08.md`](specs/spec-MFG-08.md) |
| MFG-09 | Contract Management | 9 | 6 | [`spec-MFG-09.md`](specs/spec-MFG-09.md) |
| MFG-10 | Order Optimization (Merge) | 7 | 4 | [`spec-MFG-10.md`](specs/spec-MFG-10.md) |
| MFG-11 | Data Analytics | 3 | 3 | [`spec-MFG-11.md`](specs/spec-MFG-11.md) |
| MFG-12 | System Operations | 8 | 3 | [`spec-MFG-12.md`](specs/spec-MFG-12.md) |
| **Total** | | **94** | **49** | |

## Use Case ID convention

Use Case IDs use the format `UC-<actor initial><number>`:

- `UC-G01` to `UC-G03`: Guest
- `UC-M01` to `UC-M08`: Member
- `UC-C01` to `UC-C27`: Customer or Company Admin
- `UC-S01` to `UC-S11`: Sales Consultant or System Admin

The same initial is shared when two actor names begin with the same letter. The complete actor association is recorded in [`docs/architecture/use-case.md`](docs/architecture/use-case.md).

## Architecture and flows

1. [`context.md`](docs/architecture/context.md) shows the actors and external payment gateway around the WeaveLink platform.
2. [`system-configuration.md`](docs/architecture/system-configuration.md) describes the frontend services, API gateway/load balancer, backend services, external API, and data storage layer.
3. [`usage-flow.md`](docs/architecture/usage-flow.md) shows the customer journey from entering the website through registration, product selection, design, merge policy, contract signing, payment, and completion.
4. [`sequence.md`](docs/architecture/sequence.md) records the detailed message flow for browsing, authentication, product search, design, service requests, saved designs, orders, contracts, and payments.

## Traceability

The documentation uses the following identifier layers:

- `MFG-01` through `MFG-12`: functional modules.
- `UC-*`: use cases.
- `F-*`: functions and subfunctions from the function list.
- `FR-*`: module-local functional requirements in the specs.
- `S01` through `S40`: screen IDs.
- `SD-*`: sequence diagram IDs.
- `ILF-*`: information or data storage items shown in the system configuration.

Each module spec links its scenarios and functional requirements back to the function list, use-case table, screen catalogue, and supplied diagrams.

## Open clarification areas

Several source documents contain explicit `[NEEDS CLARIFICATION: ...]` markers. The main unresolved areas are:

- scenario priority and release scope are not fully agreed;
- some use case actor associations are indirect in the original diagram;
- detailed flows and sequences are unavailable for some use cases;
- input/output schemas, validation rules, and exact data types are incomplete for some functions;
- some screen IDs in the catalogue do not yet have a matching detailed screen-spec file;
- payment, contract, notification, backup, and configuration failure behavior needs confirmation.

These markers are retained in the relevant specifications instead of being replaced with assumptions.

## Suggested reading order

1. [`docs/architecture/context.md`](docs/architecture/context.md)
2. [`docs/architecture/system-configuration.md`](docs/architecture/system-configuration.md)
3. [`docs/architecture/use-case.md`](docs/architecture/use-case.md)
4. [`docs/function-list.md`](docs/function-list.md)
5. The relevant module file in [`specs/`](specs/)
6. The linked screen and sequence documents
