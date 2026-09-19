# S26 — Customer Order List

| Property | Value |
|---|---|
| Route | `/orders` |
| Module | MFG-07 |
| Roles and ownership | Customer owner; server enforces role, company, assignment and ownership per D01. |
| Priority | P1 |
| Mockup | Historical mockup: [img/S26-customer_order_list_screen.png](img/S26-customer_order_list_screen.png); written rules supersede sample text. |

## Purpose and data

The customer lists only orders they own, with status, order number, placed date, total VND and allowlisted filters. All identifiers and permissions come from the server session; list filters are allowlisted and recoverable failures preserve entered values.

## Fields and validation

| Field | Type / requirement | Validation / source |
|---|---|---|
| page/page_size |  integer page>=1, size1..100 default20 | page/page_size: integer page>=1, size1..100 default20; allowlisted status/date sorting. |
| Rows |  order_id UUID, created_at, status, total_vnd integer, product summary. | Rows: order_id UUID, created_at, status, total_vnd integer, product summary. |
| ownership_scope | session-derived, read-only | Return only the current customer's orders; filters cannot broaden ownership. |
| API errors | D02 envelope | 400 malformed; 422 invalid fields; 409 stale/duplicate; 429 rate limit; 503 dependency failure |

## Actions and navigation

| Action | Result | Destination |
|---|---|---|
| Open order | Load current customer's order detail and actions. | S27 |
| Filter/sort | Query only owned orders. | S26 |
### Global navigation access

Home and public catalog are available to Guest and authenticated users. Customer designs, orders, profile and notifications require the customer’s authenticated session. Company Admin routes are S10, S18, S28, S30, S36, S42 and S43; Sales Consultants use S20 and assigned-only S28/S29/S21 access; System Admin routes are S39, S40 and S41. The server rechecks company, membership, ownership and assignment for every route and notification target.
Functions: MFG-07/F-ORD-001. Global navigation and back behavior follow D11. Auth return paths must be internal allowlisted routes.

## Workflow transitions

Open order → S27; catalog → S08; home → S01.

## States

| State | Behavior | Trigger |
|---|---|---|
| Loading | Labelled progress/skeleton; disable duplicate submit. | Request starts |
| Empty | Show no orders owned by this customer; preserve filters where present and explain eligibility/filter conditions. | Successful query returns no rows |
| Forbidden/not found | Safe message without revealing inaccessible identifiers. | 401/403/404 |
| Error | Show code, message, field_errors, request_id; preserve entered values. | Request failure |
| Retry | Retry reads on transient failure; reuse the same idempotency key only for mutations that require one under D02. | Recoverable failure |
| Success | Show committed state and next valid action; announce via aria-live. | Mutation commits |
| Conflict | Explain stale state; reload; never silently overwrite. | 409 |

## Acceptance scenarios

1. Customer sees only own orders with current status and VND snapshot total.
2. Opening another customer's order id returns 404 without revealing its existence.

## Responsive and accessibility

Follow D11: 360px through desktop; stack columns and use labelled horizontal-scroll tables on narrow screens; keyboard-operable controls, visible focus, logical headings, associated form labels, aria-live status/error announcements, contrast >=4.5:1 (large text >=3:1), pointer targets >=24px. Preserve form data after recoverable failures; confirm destructive actions; disable duplicate submit while pending and enforce D02 idempotency server-side.

## Source documents

- [MFG-07 specification](../specs/spec-MFG-07.md)
- [Canonical decisions D01-D12](../docs/system-decisions.md)
- [Human factual input register](../docs/user-input-needed.md)
