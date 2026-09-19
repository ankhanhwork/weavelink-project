# S25 — Order Summary

| Property | Value |
|---|---|
| Route | `/orders/summary?quote_id={id}` |
| Module | MFG-06 |
| Roles and ownership | Customer owner; server enforces role, company, assignment and ownership per D01. |
| Priority | P1 |
| Mockup | Historical mockup: [img/S25-order_summary_screen.png](img/S25-order_summary_screen.png); written rules supersede sample text. |

## Purpose and data

The customer reviews an unexpired server quote with integer VND line amounts, delivery address, selected merge policy and expiry before submitting the order. All identifiers and permissions come from the server session; list filters are allowlisted and recoverable failures preserve entered values.

## Fields and validation

| Field | Type / requirement | Validation / source |
|---|---|---|
| quote_id |  UUID | quote_id: UUID; server quote lasts 30 minutes and binds product/design/policy versions. |
| subtotal_vnd |  sum(quantity*(unit_price_vnd+option_surcharge_vnd)), integer. | subtotal_vnd: sum(quantity*(unit_price_vnd+option_surcharge_vnd)), integer. |
| merge_discount_vnd |  floor(subtotal*5/100) when opted-in | merge_discount_vnd: floor(subtotal*5/100) when opted-in; else 0. |
| price_breakdown | integer VND, read-only | Show snapshotted subtotal, discount, shipping, merge fee, tax and total; default shipping is 30000, merge fee/tax are 0. |
| quote_id / expected_version / Idempotency-Key | required submission contract | Never submit a client total; an expired/superseded quote returns to requote and explicit review. |
| API errors | D02 envelope | 400 malformed; 422 invalid fields; 409 stale/duplicate; 429 rate limit; 503 dependency failure |

## Actions and navigation

| Action | Result | Destination |
|---|---|---|
| Submit order | Revalidate unexpired quote and versions; atomically create PendingContract order/snapshots with idempotency. | S34 |
| Edit quantities/address | Requote and show changed breakdown before submit. | S22 |
| Change merge preference | Requote with explicit preference. | S23 |
### Global navigation access

Home and public catalog are available to Guest and authenticated users. Customer designs, orders, profile and notifications require the customer’s authenticated session. Company Admin routes are S10, S18, S28, S30, S36, S42 and S43; Sales Consultants use S20 and assigned-only S28/S29/S21 access; System Admin routes are S39, S40 and S41. The server rechecks company, membership, ownership and assignment for every route and notification target.
Functions: MFG-06/F-PAY-002, MFG-06/F-PAY-003. Global navigation and back behavior follow D11. Auth return paths must be internal allowlisted routes.

## Workflow transitions

Submit quote → S34 contract detail; edit inputs → S22; return to merge choice → S23.

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

1. Valid unexpired quote submission creates one PendingContract order and immutable address/price snapshots.
2. Expired quote or changed product/design version requires requote and review; duplicate same key returns same order.

## Responsive and accessibility

Follow D11: 360px through desktop; stack columns and use labelled horizontal-scroll tables on narrow screens; keyboard-operable controls, visible focus, logical headings, associated form labels, aria-live status/error announcements, contrast >=4.5:1 (large text >=3:1), pointer targets >=24px. Preserve form data after recoverable failures; confirm destructive actions; disable duplicate submit while pending and enforce D02 idempotency server-side.

## Source documents

- [MFG-06 specification](../specs/spec-MFG-06.md)
- [Canonical decisions D01-D12](../docs/system-decisions.md)
- [Human factual input register](../docs/user-input-needed.md)
