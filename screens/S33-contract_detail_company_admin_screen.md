# S33 — Contract Detail (Company Admin)

| Property | Value |
|---|---|
| Route | `/admin/contracts/{contract_id}` |
| Module | MFG-09 |
| Roles and ownership | Company Admin; server enforces role, company, assignment and ownership per D01. |
| Priority | P2 |
| Mockup | No mockup supplied. |

## Purpose and data

The Company Admin sees the authorized company contract, status history, generated private PDF and permitted void/supersede controls. All identifiers and permissions come from the server session; list filters are allowlisted and recoverable failures preserve entered values.

## Fields and validation

| Field | Type / requirement | Validation / source |
|---|---|---|
| contract_id / order_id | UUID / UUID | Both belong to active company; inaccessible IDs return 404. |
| status | Draft, Ready, Signed, Superseded, Voided | Controls appear only when allowed by contract state and role. |
| template_version / content_hash | integer / SHA-256 | Generated from immutable order/customer snapshot and selected template version. |
| pdf_asset_id | private UUID, nullable until generated | Private PDF; download uses access-checked expiring URL. |
| ready_at / signed_at | nullable UTC timestamps | Server-set after PDF storage or signature commit. |
| expected_version | integer, required on mutation | Stale replacement/void returns 409; Signed version cannot be edited. |

## Actions and navigation

| Action | Result | Destination |
|---|---|---|
| Generate PDF/publish Ready | Generate and store PDF first; transition only on success, queue notice after commit. | S34 |
| Replace unsigned contract | Create new version; supersede prior unsigned version and notify. | S33 |
| Download PDF | Issue authorized expiring URL. | S33 |
### Global navigation access

Home and public catalog are available to Guest and authenticated users. Customer designs, orders, profile and notifications require the customer’s authenticated session. Company Admin routes are S10, S18, S28, S30, S36, S42 and S43; Sales Consultants use S20 and assigned-only S28/S29/S21 access; System Admin routes are S39, S40 and S41. The server rechecks company, membership, ownership and assignment for every route and notification target.
Functions: MFG-09/F-CONTR-003, MFG-09/F-CONTR-004, MFG-09/F-CONTR-005, MFG-09/F-CONTR-007. Global navigation and back behavior follow D11. Auth return paths must be internal allowlisted routes.

## Workflow transitions

Publish Ready / notify → S34 customer route; back to contracts → S30; signed contracts are read-only.

## States

| State | Behavior | Trigger |
|---|---|---|
| Loading | Labelled progress/skeleton; disable duplicate submit. | Request starts |
| Empty | Render the screen-specific form/detail state; if a required route object is absent, show safe not-found and return to the authorized parent route. | Empty initial form or missing detail payload |
| Forbidden/not found | Safe message without revealing inaccessible identifiers. | 401/403/404 |
| Error | Show code, message, field_errors, request_id; preserve entered values. | Request failure |
| Retry | Retry reads on transient failure; reuse the same idempotency key only for mutations that require one under D02. | Recoverable failure |
| Success | Show committed state and next valid action; announce via aria-live. | Mutation commits |
| Conflict | Explain stale state; reload; never silently overwrite. | 409 |

## Acceptance scenarios

1. Ready is published only after private PDF generation/storage succeeds; then notification enters outbox.
2. Signed contract cannot be edited/replaced; failed PDF leaves prior state and allows retry.

## Responsive and accessibility

Follow D11: 360px through desktop; stack columns and use labelled horizontal-scroll tables on narrow screens; keyboard-operable controls, visible focus, logical headings, associated form labels, aria-live status/error announcements, contrast >=4.5:1 (large text >=3:1), pointer targets >=24px. Preserve form data after recoverable failures; confirm destructive actions; disable duplicate submit while pending and enforce D02 idempotency server-side.

## Source documents

- [MFG-09 specification](../specs/spec-MFG-09.md)
- [Canonical decisions D01-D12](../docs/system-decisions.md)
- [Human factual input register](../docs/user-input-needed.md)
