# S43 — Analytics Dashboard

| Property | Value |
|---|---|
| Route | `/admin/analytics` |
| Module | MFG-11 |
| Roles and ownership | Company Admin; server enforces role, company, assignment and ownership per D01. |
| Priority | P3 |
| Mockup | No mockup supplied. |

## Purpose and data

The Company Admin views company-scoped read-only metrics for the selected local date range and product filter. Exports use the same metric rules and snapshot watermark. All identifiers and permissions come from the server session; list filters are allowlisted and recoverable failures preserve entered values.

## Fields and validation

| Field | Type / requirement | Validation / source |
|---|---|---|
| date_start / date_end | local dates, inclusive/exclusive | Default last 30 local calendar days; maximum 366 days; reject start >= end. |
| product_id | optional UUID | Same-company product only; filter related orders/requests. |
| revenue_vnd | integer VND aggregates | Accepted ORDER settlement by paid_at less refunds by refunded_at; SERVICE separate; exclude duplicate/late receipts and their refunds. |
| order_count / cancellation_count | integer counts | Count orders by created_at in all states; cancellations shown separately. |
| new_customers | integer count | Distinct customers whose first submitted order in this company falls in range. |
| refreshed_at / timezone | UTC timestamp / Asia/Ho_Chi_Minh | Always display snapshot watermark and local range; zero-data metrics are zero. |
| export_format / export_limit | CSV or XLSX / max 100000 rows | Same filters/formulas/watermark; prevent spreadsheet formula injection. |

## Actions and navigation

| Action | Result | Destination |
|---|---|---|
| Apply date/product filters | Recompute authoritative company-scoped metrics; display timezone/range/refreshed_at. | S43 |
| Export CSV/XLSX | Same filters/formulas and snapshot watermark; <=100000 rows; neutralize formula injection. | S43 |
| Open order | Navigate only to authorized company order detail. | S29 |
### Global navigation access

Home and public catalog are available to Guest and authenticated users. Customer designs, orders, profile and notifications require the customer’s authenticated session. Company Admin routes are S10, S18, S28, S30, S36, S42 and S43; Sales Consultants use S20 and assigned-only S28/S29/S21 access; System Admin routes are S39, S40 and S41. The server rechecks company, membership, ownership and assignment for every route and notification target.
Functions: MFG-11/F-DA-001, MFG-11/F-DA-002, MFG-11/F-DA-003. Global navigation and back behavior follow D11. Auth return paths must be internal allowlisted routes.

## Workflow transitions

Apply filters/export stays S43; order detail → S29; home → S01.

## States

| State | Behavior | Trigger |
|---|---|---|
| Loading | Labelled progress/skeleton; disable duplicate submit. | Request starts |
| Empty | Show no metrics during the selected date range; preserve filters where present and explain eligibility/filter conditions. | Successful query returns no rows |
| Forbidden/not found | Safe message without revealing inaccessible identifiers. | 401/403/404 |
| Error | Show code, message, field_errors, request_id; preserve entered values. | Request failure |
| Retry | Retry reads on transient failure; reuse the same idempotency key only for mutations that require one under D02. | Recoverable failure |
| Success | Show committed state and next valid action; announce via aria-live. | Mutation commits |
| Conflict | Explain stale state; reload; never silently overwrite. | 409 |

## Acceptance scenarios

1. Revenue equals successful ORDER payments minus successful ORDER refunds by their respective timestamps; SERVICE shown separately.
2. Zero-data period shows zeros; export matches filter/formula/watermark and rejects >100000 rows.

## Responsive and accessibility

Follow D11: 360px through desktop; stack columns and use labelled horizontal-scroll tables on narrow screens; keyboard-operable controls, visible focus, logical headings, associated form labels, aria-live status/error announcements, contrast >=4.5:1 (large text >=3:1), pointer targets >=24px. Preserve form data after recoverable failures; confirm destructive actions; disable duplicate submit while pending and enforce D02 idempotency server-side.

## Source documents

- [MFG-11 specification](../specs/spec-MFG-11.md)
- [Canonical decisions D01-D12](../docs/system-decisions.md)
- [Human factual input register](../docs/user-input-needed.md)
