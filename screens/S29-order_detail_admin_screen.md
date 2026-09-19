# S29 — Order Detail (Admin)

| Property | Value |
|---|---|
| Route | `/admin/orders/{order_id}` |
| Module | MFG-07 |
| Roles and ownership | Company Admin/Assigned Consultant; server enforces role, company, assignment and ownership per D01. |
| Priority | P2 |
| Mockup | No mockup supplied. |

## Purpose and data

The Company Admin sees any same-company order; a consultant sees only an order tied to their current assignment. Mutations follow order state and expected_version. All identifiers and permissions come from the server session; list filters are allowlisted and recoverable failures preserve entered values.

## Fields and validation

| Field | Type / requirement | Validation / source |
|---|---|---|
| order_id / snapshots | UUID and read-only data | Same company or assigned consultant only; price, address, design and contract snapshots cannot be edited. |
| target_status / expected_version | required mutation inputs | Permit only the next D07 fulfillment state from the current version. |
| carrier / tracking_number | strings required for Shipped | Server records shipped_at; Delivered records delivered_at. |
| cancellation_reason | string 1..500, Company Admin only | Require current cancellation eligibility; assigned consultants cannot cancel. |
| contract_action | Company Admin only | Open S33 to create/revise an unsigned version; never mutate a Signed contract. |
| API errors | D02 envelope | 400 malformed; 422 invalid fields; 409 stale/duplicate; 429 rate limit; 503 dependency failure |

## Actions and navigation

| Action | Result | Destination |
|---|---|---|
| Generate contract | Snapshot current order/customer data and chosen template. | S33 |
| Update fulfillment | Apply only next D07 transition; consultant assignment guard; record tracking/dates. | S29 |
| Cancel order | Company Admin with reason and eligibility; consultants cannot cancel. | S28 |
| Merge batch | Open batch console. | S42 |
### Global navigation access

Home and public catalog are available to Guest and authenticated users. Customer designs, orders, profile and notifications require the customer’s authenticated session. Company Admin routes are S10, S18, S28, S30, S36, S42 and S43; Sales Consultants use S20 and assigned-only S28/S29/S21 access; System Admin routes are S39, S40 and S41. The server rechecks company, membership, ownership and assignment for every route and notification target.
Functions: MFG-07/F-ORD-005, MFG-07/F-ORD-006, MFG-07/F-ORD-007. Global navigation and back behavior follow D11. Auth return paths must be internal allowlisted routes.

## Workflow transitions

Generate/replace contract → S33; valid fulfillment update remains S29; merge console → S42; order list → S28.

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

1. Only valid next fulfillment transition is applied; shipment requires carrier, tracking and timestamp.
2. Consultant cannot cancel order or bypass payment/contract gates; stale order version returns 409.

## Responsive and accessibility

Follow D11: 360px through desktop; stack columns and use labelled horizontal-scroll tables on narrow screens; keyboard-operable controls, visible focus, logical headings, associated form labels, aria-live status/error announcements, contrast >=4.5:1 (large text >=3:1), pointer targets >=24px. Preserve form data after recoverable failures; confirm destructive actions; disable duplicate submit while pending and enforce D02 idempotency server-side.

## Source documents

- [MFG-07 specification](../specs/spec-MFG-07.md)
- [Canonical decisions D01-D12](../docs/system-decisions.md)
- [Human factual input register](../docs/user-input-needed.md)
