# S36 — Payment Transaction List

| Property | Value |
|---|---|
| Route | `/admin/payments` |
| Module | MFG-06 |
| Roles and ownership | Company Admin; server enforces role, company, assignment and ownership per D01. |
| Priority | P2 |
| Mockup | No mockup supplied. |

## Purpose and data

The Company Admin lists same-company payment transactions and refunds using provider status, purpose, amount, timestamps and order/request reference filters. All identifiers and permissions come from the server session; list filters are allowlisted and recoverable failures preserve entered values.

## Fields and validation

| Field | Type / requirement | Validation / source |
|---|---|---|
| purpose | enum: ORDER or SERVICE | Filter uses active Company Admin company scope. |
| status / refund_status | allowlisted transaction/refund enums | Filter Pending, Succeeded, Failed or Expired where applicable. |
| date_from / date_to | optional local dates | Inclusive start, exclusive end; display Asia/Ho_Chi_Minh. |
| rows | payment_id, resource_id, integer amount_vnd, currency, status, created_at | Mask provider references; omit card secrets and other-company data. |
| page / page_size / sort | integer / integer / enum | D02 bounds; sort by created_at, amount_vnd or status. |
| API errors | D02 envelope | 400 malformed; 403 prohibited; 404 inaccessible payment; 422 invalid filters; 503 dependency failure. |

## Actions and navigation

| Action | Result | Destination |
|---|---|---|
| Open transaction | Load redacted payment/refund detail. | S37 |
| Filter list | Preserve allowlisted filters and pagination on refresh/back. | S36 |
### Global navigation access

Home and public catalog are available to Guest and authenticated users. Customer designs, orders, profile and notifications require the customer’s authenticated session. Company Admin routes are S10, S18, S28, S30, S36, S42 and S43; Sales Consultants use S20 and assigned-only S28/S29/S21 access; System Admin routes are S39, S40 and S41. The server rechecks company, membership, ownership and assignment for every route and notification target.
Functions: MFG-06/F-PAY-005. Global navigation and back behavior follow D11. Auth return paths must be internal allowlisted routes.

## Workflow transitions

Open transaction → S37; home → S01.

## States

| State | Behavior | Trigger |
|---|---|---|
| Loading | Labelled progress/skeleton; disable duplicate submit. | Request starts |
| Empty | Show no company payment transactions matching filters; preserve filters where present and explain eligibility/filter conditions. | Successful query returns no rows |
| Forbidden/not found | Safe message without revealing inaccessible identifiers. | 401/403/404 |
| Error | Show code, message, field_errors, request_id; preserve entered values. | Request failure |
| Retry | Retry reads on transient failure; reuse the same idempotency key only for mutations that require one under D02. | Recoverable failure |
| Success | Show committed state and next valid action; announce via aria-live. | Mutation commits |
| Conflict | Explain stale state; reload; never silently overwrite. | 409 |

## Acceptance scenarios

1. List contains company-scoped ORDER/SERVICE attempts with masked provider refs and page bounds.
2. Cross-company payment is absent; pending attempts are not represented as revenue.

## Responsive and accessibility

Follow D11: 360px through desktop; stack columns and use labelled horizontal-scroll tables on narrow screens; keyboard-operable controls, visible focus, logical headings, associated form labels, aria-live status/error announcements, contrast >=4.5:1 (large text >=3:1), pointer targets >=24px. Preserve form data after recoverable failures; confirm destructive actions; disable duplicate submit while pending and enforce D02 idempotency server-side.

## Source documents

- [MFG-06 specification](../specs/spec-MFG-06.md)
- [Canonical decisions D01-D12](../docs/system-decisions.md)
- [Human factual input register](../docs/user-input-needed.md)
