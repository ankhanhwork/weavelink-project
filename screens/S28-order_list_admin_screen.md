# S28 — Order List (Admin)

| Property | Value |
|---|---|
| Route | `/admin/orders` |
| Module | MFG-07 |
| Roles and ownership | Company Admin / Assigned Consultant; consultant sees only assigned orders and permitted actions. |
| Priority | P2 |
| Mockup | No mockup supplied. |

## Purpose and data

The Company Admin sees orders for the active company and may filter by status, date, product and assigned consultant. The assigned consultant has access only to assigned orders and permitted actions. All identifiers and permissions come from the server session; list filters are allowlisted and recoverable failures preserve entered values.

## Fields and validation

| Field | Type / requirement | Validation / source |
|---|---|---|
| page / page_size / filters | paginated query | Follow D02; allow only status, date, product and customer filters. |
| Rows company-scoped |  order_id, customer display name, status, total_vnd, created_at, version. | Rows company-scoped: order_id, customer display name, status, total_vnd, created_at, version. |
| company_or_assignment_scope | server-derived | Company Admin sees same-company rows; consultant sees assigned-customer rows; System Admin has no implicit access. |
| API errors | D02 envelope | 400 malformed; 422 invalid fields; 409 stale/duplicate; 429 rate limit; 503 dependency failure |

## Actions and navigation

| Action | Result | Destination |
|---|---|---|
| Open order | Company Admin opens any same-company order; consultant opens assigned order only. | S29 |
| Update status | Company Admin or assigned consultant may advance allowed production status; consultant cannot cancel or manage merge/contract operations. | S29 |
| Merge console | Company Admin only; open eligible merge candidates. | S42 |
### Global navigation access

Home and public catalog are available to Guest and authenticated users. Customer designs, orders, profile and notifications require the customer’s authenticated session. Company Admin routes are S10, S18, S28, S30, S36, S42 and S43; Sales Consultants use S20 and assigned-only S28/S29/S21 access; System Admin routes are S39, S40 and S41. The server rechecks company, membership, ownership and assignment for every route and notification target.
Functions: MFG-07/F-ORD-005, MFG-07/F-ORD-006, MFG-07/F-ORD-007. Global navigation and back behavior follow D11. Auth return paths must be internal allowlisted routes.

## Workflow transitions

Open order → S29; open merge candidates → S42; home → S01.

## States

| State | Behavior | Trigger |
|---|---|---|
| Loading | Labelled progress/skeleton; disable duplicate submit. | Request starts |
| Empty | Show no company orders or orders assigned to this consultant; preserve filters where present and explain eligibility/filter conditions. | Successful query returns no rows |
| Forbidden/not found | Safe message without revealing inaccessible identifiers. | 401/403/404 |
| Error | Show code, message, field_errors, request_id; preserve entered values. | Request failure |
| Retry | Retry reads on transient failure; reuse the same idempotency key only for mutations that require one under D02. | Recoverable failure |
| Success | Show committed state and next valid action; announce via aria-live. | Mutation commits |
| Conflict | Explain stale state; reload; never silently overwrite. | 409 |

## Acceptance scenarios

1. Company Admin list filters cannot return another company's order or financial data.
2. Allowlisted status/date filter returns stable pagination and preserves filter state on detail/back.
3. Assigned Consultant sees only assigned-customer orders and fulfillment actions; merge, cancellation, contract and financial-administration actions stay hidden and are rejected server-side.

## Responsive and accessibility

Follow D11: 360px through desktop; stack columns and use labelled horizontal-scroll tables on narrow screens; keyboard-operable controls, visible focus, logical headings, associated form labels, aria-live status/error announcements, contrast >=4.5:1 (large text >=3:1), pointer targets >=24px. Preserve form data after recoverable failures; confirm destructive actions; disable duplicate submit while pending and enforce D02 idempotency server-side.

## Source documents

- [MFG-07 specification](../specs/spec-MFG-07.md)
- [Canonical decisions D01-D12](../docs/system-decisions.md)
- [Human factual input register](../docs/user-input-needed.md)
