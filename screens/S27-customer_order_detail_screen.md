# S27 — Customer Order Detail

| Property | Value |
|---|---|
| Route | `/orders/{order_id}` |
| Module | MFG-07 |
| Roles and ownership | Customer owner; server enforces role, company, assignment and ownership per D01. |
| Priority | P1 |
| Mockup | Historical mockup: [img/S27-customer_order_detail_screen.png](img/S27-customer_order_detail_screen.png); written rules supersede sample text. |

## Purpose and data

The customer sees one owned order’s immutable design, quantity, delivery, price, contract, payment and production snapshots, with actions enabled by current status. All identifiers and permissions come from the server session; list filters are allowlisted and recoverable failures preserve entered values.

## Fields and validation

| Field | Type / requirement | Validation / source |
|---|---|---|
| order_id / item_snapshot | UUID and read-only snapshot | Owner only; show immutable quantities, address and price breakdown. |
| status enum |  PendingContract, AwaitingPayment, Confirmed, InProduction, Shipped, Delivered, Cancelled. | status enum: PendingContract, AwaitingPayment, Confirmed, InProduction, Shipped, Delivered, Cancelled. |
| contract / payment / refund / batch | read-only related projections | Display authoritative current states and nullable batch_id; never infer state from email/browser return. |
| cancellation_eligibility / reason | server boolean plus required string 1..500 | Allow only PendingContract, AwaitingPayment or pre-production unbatched Confirmed; paid cancellation starts full refund. |
| carrier / tracking_number / shipped_at / delivered_at | read-only fulfillment fields | Required/displayed only for the corresponding Shipped/Delivered states. |
| API errors | D02 envelope | 400 malformed; 422 invalid fields; 409 stale/duplicate; 429 rate limit; 503 dependency failure |

## Actions and navigation

| Action | Result | Destination |
|---|---|---|
| Cancel order | Confirm; enforce state/no-batch/preproduction; schedule full refund if paid. | S26 |
| Pay | Available only after current contract Signed and status AwaitingPayment. | S35 |
| View contract | Open authorized current contract. | S34 |
### Global navigation access

Home and public catalog are available to Guest and authenticated users. Customer designs, orders, profile and notifications require the customer’s authenticated session. Company Admin routes are S10, S18, S28, S30, S36, S42 and S43; Sales Consultants use S20 and assigned-only S28/S29/S21 access; System Admin routes are S39, S40 and S41. The server rechecks company, membership, ownership and assignment for every route and notification target.
Functions: MFG-07/F-ORD-002, MFG-07/F-ORD-003, MFG-07/F-ORD-004. Global navigation and back behavior follow D11. Auth return paths must be internal allowlisted routes.

## Workflow transitions

Pay signed order → S35; open contract → S34; cancel eligible order → S26; back → S26.

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

1. Cancellation succeeds only in allowed preproduction unbatched state; paid eligible cancel schedules full refund.
2. Cancellation after batch assignment or production start returns 409 and leaves order unchanged.

## Responsive and accessibility

Follow D11: 360px through desktop; stack columns and use labelled horizontal-scroll tables on narrow screens; keyboard-operable controls, visible focus, logical headings, associated form labels, aria-live status/error announcements, contrast >=4.5:1 (large text >=3:1), pointer targets >=24px. Preserve form data after recoverable failures; confirm destructive actions; disable duplicate submit while pending and enforce D02 idempotency server-side.

## Source documents

- [MFG-07 specification](../specs/spec-MFG-07.md)
- [Canonical decisions D01-D12](../docs/system-decisions.md)
- [Human factual input register](../docs/user-input-needed.md)
