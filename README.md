# WeaveLink — implementation specifications

WeaveLink is a made-to-order garment platform covering catalog, design services, checkout, payment, contracts, fulfillment, production batches, analytics and administration.

This repository contains **documentation, not application source code**. The complete-system baseline covers **12 MFG modules, 94 module-qualified function entries, 49 use cases and 43 detailed screens**, with 17 inherited PNG mockups. All modules are included; historical MVP exclusions do not limit this target.

## Start here

1. Read [system decisions](docs/system-decisions.md): shared data, role/tenant rules, lifecycles, pricing, side effects and implementation defaults.
2. Read [system configuration](docs/architecture/system-configuration.md) and [usage flow](docs/architecture/usage-flow.md).
3. Locate the relevant module using the table below and its [function catalogue](docs/function-list.md).
4. Use the [screen catalogue](docs/screen-list.md), [use cases](docs/architecture/use-case.md), [sequences](docs/architecture/sequence.md) and [acceptance checklist](docs/acceptance-checklist.md).
5. Consult the [VNPay adapter contract](docs/integrations/vnpay.md) before implementing payment.

The only pending factual-information register is [user-input-needed.md](docs/user-input-needed.md). It contains human/course/company/source-provenance facts; implementation behavior is decided in the specifications.

## Modules

| Module | Scope | Functions | Specification |
|---|---|---:|---|
| MFG-01 | Identity and access | 11 | [Spec](specs/spec-MFG-01.md) |
| MFG-02 | Profile and settings | 5 | [Spec](specs/spec-MFG-02.md) |
| MFG-03 | Company and staff accounts | 8 | [Spec](specs/spec-MFG-03.md) |
| MFG-04 | Product catalog and design rules | 11 | [Spec](specs/spec-MFG-04.md) |
| MFG-05 | Designs and paid design requests | 11 | [Spec](specs/spec-MFG-05.md) |
| MFG-06 | Checkout, order creation and payment | 6 | [Spec](specs/spec-MFG-06.md) |
| MFG-07 | Order tracking, cancellation and fulfillment | 7 | [Spec](specs/spec-MFG-07.md) |
| MFG-08 | Consultant assignment and customer care | 8 | [Spec](specs/spec-MFG-08.md) |
| MFG-09 | Templates, contracts and signing | 9 | [Spec](specs/spec-MFG-09.md) |
| MFG-10 | Merge preference and production batches | 7 | [Spec](specs/spec-MFG-10.md) |
| MFG-11 | Analytics and exports | 3 | [Spec](specs/spec-MFG-11.md) |
| MFG-12 | Configuration, logs, backup and recovery | 8 | [Spec](specs/spec-MFG-12.md) |
| **Total** | | **94** | |

## Canonical conventions and scope

- Preserve legacy MFG/F/FR/UC/S/SD/ILF IDs. **F-ORD identifiers overlap in MFG-07 and MFG-08**: always qualify cross-module references, for example MFG-07/F-ORD-003 (cancel order) versus MFG-08/F-ORD-003 (assign consultant). FR and scenario IDs are also module-local.
- S01–S40 remain; S14 is clarified as product design-rule editing. S41 company/staff accounts, S42 merge console and S43 analytics close uncovered UI needs. Missing historical images are documented, not fabricated.
- Member is the authenticated-user umbrella. System Admin, Company Admin, Sales Consultant and Customer have explicit server-side access boundaries.
- Shared rules are authoritative. Money is integer VND; order, contract, payment, request and batch states are distinct. A browser payment return never authorizes settlement.
- New prices, deadlines, retention and signature behavior are **documented implementation decisions** for this classroom system, not claimed facts from unavailable DBIZ2/session PDFs or actual client approval.
- PNGs remain original visual references. Written specs override obsolete sample prices, ambiguous buttons and missing failure behavior. Git history retains the previous transcriptions; the current docs form one consistent target.

## Validation

Requires Node.js with support for ES modules; no external package install is required.

```powershell
node scripts/validate-docs.mjs
node scripts/validate-docs.mjs --build
git diff --check
```

The build option emits a documentation index at `tmp/documentation-index.json`; this is not an application build. The checker validates function/use-case/screen coverage, local links, placeholders, qualified IDs, Markdown fence/table structure and worked pricing examples. It does not execute future business code or prove runtime behavior. See the [validation report](docs/validation-report.md) for actual results and limits.
