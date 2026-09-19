# S20 — Consultant Tasks and Customers

| Property | Value |
|---|---|
| Route | `/consultant/tasks?tab=assigned,customers` |
| Module | MFG-08 |
| Roles and ownership | Sales Consultant; server enforces role, company, assignment and ownership per D01. |
| Priority | P2 |
| Mockup | No mockup supplied. |

## Purpose and data

The consultant sees only their assigned design requests and CRM customers. Design-task status and CRM consultation status are presented separately. All identifiers and permissions come from the server session; list filters are allowlisted and recoverable failures preserve entered values.

## Fields and validation

| Field | Type / requirement | Validation / source |
|---|---|---|
| tab | enum: assigned or customers; default assigned | Both tabs query only the current consultant assignments and same-company customer records. |
| design_request_status | AwaitingPayment, Paid, Assigned, InProgress, Delivered, Cancelled, Expired | Display-only task state; only currently assigned Paid or InProgress work is actionable. |
| crm_status | New, Contacted, InProgress, ClosedWon, ClosedLost | Applies only to CRM records; transitions follow MFG-08. |
| customer_id / request_id / company_id | read-only UUIDs | Derived from authorized assignment/session; another consultant's identifier returns 404. |
| page / page_size / sort | integer / integer / enum | D02 bounds; sort allowlist is updated_at, requested_deadline or status. |
| API errors | D02 envelope | 400 malformed; 422 invalid filters/transitions; 403 prohibited action; 404 inaccessible assignment; 409 stale version/state; 503 dependency failure. |

## Actions and navigation

| Action | Result | Destination |
|---|---|---|
| Open assigned task | Load assigned customer/request context. | S21 |
| Update CRM status | Apply New→Contacted→InProgress→ClosedWon/ClosedLost; reopen only by Company Admin. | S20 |
| Switch tab | Show assigned customers only. | S20 customers tab |
### Global navigation access

Home and public catalog are available to Guest and authenticated users. Customer designs, orders, profile and notifications require the customer’s authenticated session. Company Admin routes are S10, S18, S28, S30, S36, S42 and S43; Sales Consultants use S20 and assigned-only S28/S29/S21 access; System Admin routes are S39, S40 and S41. The server rechecks company, membership, ownership and assignment for every route and notification target.
Functions: MFG-08/F-ORD-005, MFG-08/F-ORD-006. Global navigation and back behavior follow D11. Auth return paths must be internal allowlisted routes.

## Workflow transitions

Open assigned task → S21; customer tab → S20?tab=customers; home → S01.

## States

| State | Behavior | Trigger |
|---|---|---|
| Loading | Labelled progress/skeleton; disable duplicate submit. | Request starts |
| Empty | Show no tasks assigned to this consultant; preserve filters where present and explain eligibility/filter conditions. | Successful query returns no rows |
| Forbidden/not found | Safe message without revealing inaccessible identifiers. | 401/403/404 |
| Error | Show code, message, field_errors, request_id; preserve entered values. | Request failure |
| Retry | Retry reads on transient failure; reuse the same idempotency key only for mutations that require one under D02. | Recoverable failure |
| Success | Show committed state and next valid action; announce via aria-live. | Mutation commits |
| Conflict | Explain stale state; reload; never silently overwrite. | 409 |

## Acceptance scenarios

1. Consultant sees only assigned tasks/customers; another consultant's ID returns 404.
2. Valid CRM transition follows allowed state graph; reopening closed state requires Company Admin.

## Responsive and accessibility

Follow D11: 360px through desktop; stack columns and use labelled horizontal-scroll tables on narrow screens; keyboard-operable controls, visible focus, logical headings, associated form labels, aria-live status/error announcements, contrast >=4.5:1 (large text >=3:1), pointer targets >=24px. Preserve form data after recoverable failures; confirm destructive actions; disable duplicate submit while pending and enforce D02 idempotency server-side.

## Source documents

- [MFG-08 specification](../specs/spec-MFG-08.md)
- [Canonical decisions D01-D12](../docs/system-decisions.md)
- [Human factual input register](../docs/user-input-needed.md)
