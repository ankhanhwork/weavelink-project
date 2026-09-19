# S35 — Order Payment

| Property | Value |
|---|---|
| Route | `/orders/{order_id}/payment` |
| Module | MFG-06 |
| Roles and ownership | Customer owner; server enforces role, company, assignment and ownership per D01. |
| Priority | P1 |
| Mockup | Historical mockup: [img/S35-order_payment_screen.png](img/S35-order_payment_screen.png); written rules supersede sample text. |

## Purpose and data

The customer pays the exact server-snapshotted order total in integer VND through VNPay. Browser returns trigger status polling; verified callbacks alone confirm payment. Retry reuses an eligible pending attempt or creates a new attempt after failure/expiry. All identifiers and permissions come from the server session; list filters are allowlisted and recoverable failures preserve entered values.

## Fields and validation

| Field | Type / required | Validation and source |
|---|---|---|
| order_id | UUID, required | Current customer owns order; current Contract Signed; order AwaitingPayment. D07/D08 |
| subtotal_vnd | integer, required | Immutable quote/order snapshot; sum quantity times unit price plus option surcharges. D06 |
| merge_discount_vnd | integer, required | floor(subtotal_vnd*5/100) only when accepted merge preference exists; otherwise 0. D06/D09 |
| shipping_vnd | integer, required | 30000 VND snapshot. D06 |
| merge_fee_vnd | integer, required | 0 VND. D06 |
| tax_vnd | integer, required | 0 VND under classroom demo pricing assumption. D06 |
| total_vnd | integer, required | subtotal - discount + shipping + fee + tax; server snapshot only. D06 |
| payment_method | enum | VNPay only in this release; external sandbox/provider route. D08 |
| transaction_id | UUID | Returned browser route is lookup-only; poll status, never mark paid from browser. D08 |
| Idempotency-Key | UUID, required on initiation | Same key/payload returns same attempt; changed payload conflicts. D02/D08 |
| promo_code/marketing_consent/second merge consent | absent | No promo controls; merge policy is already snapshotted at order submission. D06 |
## Actions and navigation

| Action | Result | Destination |
|---|---|---|
| Initiate/retry payment | Reuse active Pending attempt or create new provider reference after failure; use server snapshot amount. | External VNPay |
| Browser return | Ignore claimed success, poll authoritative transaction. | S35 |
| Verified success | Show receipt/result and order status Confirmed. | S27 |
| Failed/expired/processing | Keep order AwaitingPayment; show retry/processing without false success. | S35 |
### Global navigation access

Home and public catalog are available to Guest and authenticated users. Customer designs, orders, profile and notifications require the customer’s authenticated session. Company Admin routes are S10, S18, S28, S30, S36, S42 and S43; Sales Consultants use S20 and assigned-only S28/S29/S21 access; System Admin routes are S39, S40 and S41. The server rechecks company, membership, ownership and assignment for every route and notification target.
Functions: MFG-06/F-PAY-002, MFG-06/F-PAY-004, MFG-06/F-PAY-005, MFG-06/F-PAY-006. Global navigation and back behavior follow D11. Auth return paths must be internal allowlisted routes.

## Workflow transitions

Open payment provider; browser return → S35 polling status; confirmed → S27; cancel/back → S27.

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

1. For Signed/AwaitingPayment order, show exact subtotal/discount/shipping/fee/tax/total integer VND and initiate 15m attempt.
2. Browser return cannot mark paid; verified callback confirms once, while failed/expired stays AwaitingPayment and enables retry.

## Responsive and accessibility

Follow D11: 360px through desktop; stack columns and use labelled horizontal-scroll tables on narrow screens; keyboard-operable controls, visible focus, logical headings, associated form labels, aria-live status/error announcements, contrast >=4.5:1 (large text >=3:1), pointer targets >=24px. Preserve form data after recoverable failures; confirm destructive actions; disable duplicate submit while pending and enforce D02 idempotency server-side.

## Source documents

- [MFG-06 specification](../specs/spec-MFG-06.md)
- [Canonical decisions D01-D12](../docs/system-decisions.md)
- [Human factual input register](../docs/user-input-needed.md)
