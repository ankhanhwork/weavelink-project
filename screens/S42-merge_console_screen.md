# S42 — Merge Console

| Property | Value |
|---|---|
| Route | `/admin/merge-batches` |
| Module | MFG-10 |
| Roles and ownership | Company Admin; server enforces role, company, assignment and ownership per D01. |
| Priority | P2 |
| Mockup | No mockup supplied. |

## Purpose and data

The Company Admin selects eligible same-company orders into a batch, reviews the explicit demo savings calculation and transitions batch state under atomic membership rules. All identifiers and permissions come from the server session; list filters are allowlisted and recoverable failures preserve entered values.

## Fields and validation

| Field | Type / requirement | Validation / source |
|---|---|---|
| candidate filters | company, product, material, color, print method, confirmed_at | Only confirmed, paid, signed-current-contract, opted-in, uncancelled, unbatched orders in same company and within 3 days. |
| selected_order_ids | UUID array, minimum 2 | Lock/revalidate atomically; total quantity <=10000; one batch per order. |
| setup_cost_vnd | integer, read-only | Demo assumption 100000; gross saving=(order_count-1)*100000. |
| customer_discount_vnd / estimated_net_saving_vnd | integer VND | Customer discounts=sum merge discounts; net=gross-discounts; show negative value and require acknowledgement. |
| setup_minutes_saved | integer, read-only estimate | (order_count-1)*30; does not alter customer deadline. |
| batch_status | Planned, InProduction, Completed | Only Planned may dissolve; membership immutable after production starts. |

## Actions and navigation

| Action | Result | Destination |
|---|---|---|
| Refresh candidates | Query only candidates satisfying D09 within company. | S42 |
| Estimate | Compute gross/net savings and setup minutes; disclose negative net and require acknowledgement. | S42 |
| Create batch | Require >=2; lock/revalidate all selected orders; create immutable membership. | S42 |
| Start/dissolve/complete | Enforce batch state transitions; dissolution only Planned; production transitions atomic. | S42 |
### Global navigation access

Home and public catalog are available to Guest and authenticated users. Customer designs, orders, profile and notifications require the customer’s authenticated session. Company Admin routes are S10, S18, S28, S30, S36, S42 and S43; Sales Consultants use S20 and assigned-only S28/S29/S21 access; System Admin routes are S39, S40 and S41. The server rechecks company, membership, ownership and assignment for every route and notification target.
Functions: MFG-10/F-MER-004, MFG-10/F-MER-005, MFG-10/F-MER-006, MFG-10/F-MER-007. Global navigation and back behavior follow D11. Auth return paths must be internal allowlisted routes.

## Workflow transitions

Create batch stays S42; batch detail stays S42; linked order → S29; order list → S28.

## States

| State | Behavior | Trigger |
|---|---|---|
| Loading | Labelled progress/skeleton; disable duplicate submit. | Request starts |
| Empty | Show no orders eligible for merge under current policy; preserve filters where present and explain eligibility/filter conditions. | Successful query returns no rows |
| Forbidden/not found | Safe message without revealing inaccessible identifiers. | 401/403/404 |
| Error | Show code, message, field_errors, request_id; preserve entered values. | Request failure |
| Retry | Retry reads on transient failure; reuse the same idempotency key only for mutations that require one under D02. | Recoverable failure |
| Success | Show committed state and next valid action; announce via aria-live. | Mutation commits |
| Conflict | Explain stale state; reload; never silently overwrite. | 409 |

## Acceptance scenarios

1. Batch creation atomically revalidates >=2 eligible same-company orders and total qty <=10000.
2. Negative net savings are visible and require admin acknowledgement; no order price/deadline changes on dissolve.

## Responsive and accessibility

Follow D11: 360px through desktop; stack columns and use labelled horizontal-scroll tables on narrow screens; keyboard-operable controls, visible focus, logical headings, associated form labels, aria-live status/error announcements, contrast >=4.5:1 (large text >=3:1), pointer targets >=24px. Preserve form data after recoverable failures; confirm destructive actions; disable duplicate submit while pending and enforce D02 idempotency server-side.

## Source documents

- [MFG-10 specification](../specs/spec-MFG-10.md)
- [Canonical decisions D01-D12](../docs/system-decisions.md)
- [Human factual input register](../docs/user-input-needed.md)
