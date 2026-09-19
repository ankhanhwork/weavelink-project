# S18 — Consultation Requests and Customers

| Property | Value |
|---|---|
| Route | `/admin/consultations?tab=requests,customers` |
| Module | MFG-05 |
| Roles and ownership | Company Admin; server enforces role, company, assignment and ownership per D01. |
| Priority | P2 |
| Mockup | No mockup supplied. |

## Purpose and data

The Company Admin switches between paid design requests awaiting assignment and company-scoped consultation/customer records. Only active same-company consultants are eligible for assignment. All identifiers and permissions come from the server session; list filters are allowlisted and recoverable failures preserve entered values.

## Fields and validation

| Field | Type / requirement | Validation / source |
|---|---|---|
| tab | enum: requests or customers; default requests | Requests show paid DesignRequest id, status, product, customer display name, requested_deadline and committed_due_at; customers show consultation id and CRM status. |
| status | allowlisted request or CRM status enum | Filter applies to the selected tab lifecycle only; design request and CRM states remain distinct. |
| product_id | optional UUID | Same-company product filter on requests tab; inaccessible IDs return 404. |
| requested_deadline_from/to | optional local dates | Inclusive start and exclusive end; reject reversed range; display in Asia/Ho_Chi_Minh. |
| page / page_size / sort | integer / integer / enum | D02 bounds; sort allowlist is requested_deadline, created_at or status. |
| customer_id / company_id | server-derived UUIDs | Never accepted as scope input; internal notes visible to authorized staff only. |
| API errors | D02 envelope | 400 malformed; 422 invalid filters; 403 prohibited action; 404 inaccessible request/customer; 429 rate limit; 503 dependency failure. |

## Actions and navigation

| Action | Result | Destination |
|---|---|---|
| Assign paid request | Open assignment with active same-company consultants. | S19 |
| Open request | View status/details and authorized notes. | S21 |
| Switch tab | Preserve company filters and route state. | S18 tab |
| Open customer record | Show staff-only company-scoped consultation context. | S18 customers tab |
### Global navigation access

Home and public catalog are available to Guest and authenticated users. Customer designs, orders, profile and notifications require the customer’s authenticated session. Company Admin routes are S10, S18, S28, S30, S36, S42 and S43; Sales Consultants use S20 and assigned-only S28/S29/S21 access; System Admin routes are S39, S40 and S41. The server rechecks company, membership, ownership and assignment for every route and notification target.
Functions: MFG-08/F-ORD-001, MFG-08/F-ORD-002, MFG-08/F-ORD-003, MFG-08/F-ORD-004; MFG-05/F-DES-008. Global navigation and back behavior follow D11. Auth return paths must be internal allowlisted routes.

## Workflow transitions

Assign paid request → S19; open customer consultation tab → S18?tab=customers; request detail → S21.

## States

| State | Behavior | Trigger |
|---|---|---|
| Loading | Labelled progress/skeleton; disable duplicate submit. | Request starts |
| Empty | Show no paid requests awaiting assignment or customer consultations; preserve filters where present and explain eligibility/filter conditions. | Successful query returns no rows |
| Forbidden/not found | Safe message without revealing inaccessible identifiers. | 401/403/404 |
| Error | Show code, message, field_errors, request_id; preserve entered values. | Request failure |
| Retry | Retry reads on transient failure; reuse the same idempotency key only for mutations that require one under D02. | Recoverable failure |
| Success | Show committed state and next valid action; announce via aria-live. | Mutation commits |
| Conflict | Explain stale state; reload; never silently overwrite. | 409 |

## Acceptance scenarios

1. Unpaid request is not assignable; Paid request appears as eligible within its company only.
2. Customer tab excludes other companies and internal notes remain staff-only.

## Responsive and accessibility

Follow D11: 360px through desktop; stack columns and use labelled horizontal-scroll tables on narrow screens; keyboard-operable controls, visible focus, logical headings, associated form labels, aria-live status/error announcements, contrast >=4.5:1 (large text >=3:1), pointer targets >=24px. Preserve form data after recoverable failures; confirm destructive actions; disable duplicate submit while pending and enforce D02 idempotency server-side.

## Source documents

- [MFG-05 specification](../specs/spec-MFG-05.md)
- [Canonical decisions D01-D12](../docs/system-decisions.md)
- [Human factual input register](../docs/user-input-needed.md)
