# S16 — Design Service Payment

| Property | Value |
|---|---|
| Route | `/design-requests/{request_id}/payment` |
| Module | MFG-06 |
| Roles and ownership | Customer owner; server enforces role, company, assignment and ownership per D01. |
| Priority | P3 |
| Mockup | Historical mockup: [img/S16-design_service_payment_screen.png](img/S16-design_service_payment_screen.png); written rules supersede sample text. |

## Purpose and data

The customer pays one AwaitingPayment design-service request at its snapshotted integer VND fee. Only a verified provider event changes it to Paid. All identifiers and permissions come from the server session; list filters are allowlisted and recoverable failures preserve entered values.

## Fields and validation

| Field | Type / requirement | Validation / source |
|---|---|---|
| request_id / product_id | UUID, read-only | Request belongs to authenticated customer; inaccessible request returns 404. |
| amount_vnd / currency | integer VND snapshot | Customer cannot edit; fee is fixed at request creation. |
| payment_attempt_id / status | UUID / Pending, Succeeded, Failed, Expired | One active Pending attempt; new provider reference only after failure/expiry; session expires after 15 minutes. |
| request_status | AwaitingPayment, Paid, Assigned, InProgress, Delivered, Cancelled, Expired | Refresh from server; display requested_deadline and committed_due_at when available. |
| requested_deadline / committed_due_at | local date / nullable UTC timestamp | Requested date is preference; committed date is set at assignment. |
| API errors | D02 envelope | 400 malformed; 403 prohibited; 404 inaccessible request; 409 stale/state; 422 invalid input; 503 dependency failure |

## Actions and navigation

| Action | Result | Destination |
|---|---|---|
| Initiate payment | Create/reuse active Pending SERVICE transaction and redirect to VNPay sandbox/adapter. | External VNPay |
| Return from provider | Treat return as untrusted; poll transaction status. | S16 |
| Cancel unpaid request | Cancel only while AwaitingPayment; expire any pending attempt. | S16 |
| Cancel paid request | Full refund only while Paid and unassigned; reject after assignment. | S16 |
| Verified paid | Show receipt and status; enqueue admin notice; request becomes assignable. | S16 / S18 admin |
| Failed/expired | Preserve request and allow retry with fresh reference when eligible. | S16 |
### Global navigation access

Home and public catalog are available to Guest and authenticated users. Customer designs, orders, profile and notifications require the customer’s authenticated session. Company Admin routes are S10, S18, S28, S30, S36, S42 and S43; Sales Consultants use S20 and assigned-only S28/S29/S21 access; System Admin routes are S39, S40 and S41. The server rechecks company, membership, ownership and assignment for every route and notification target.
Functions: MFG-05/F-DES-007, MFG-05/F-DES-008; MFG-06/F-PAY-004, MFG-06/F-PAY-005, MFG-06/F-PAY-006. Global navigation and back behavior follow D11. Auth return paths must be internal allowlisted routes.

## Workflow transitions

Return from gateway/poll status on S16; Paid, Assigned, InProgress, Delivered, Cancelled and Expired remain visible here. Delivered design appears in S17. Company Admin assigns through S19; no staff notes appear to customer.

## States

| State | Behavior | Trigger |
|---|---|---|
| Loading | Labelled progress/skeleton; disable duplicate submit. | Request starts |
| Empty | Show this owned request status and payment instructions; a missing request receives a safe not-found message. | No payment attempt exists yet |
| Forbidden/not found | Safe message without revealing inaccessible identifiers. | 401/403/404 |
| Error | Show code, message, field_errors, request_id; preserve entered values. | Request failure |
| Retry | Retry reads on transient failure; reuse the same idempotency key only for mutations that require one under D02. | Recoverable failure |
| Success | Show committed state and next valid action; announce via aria-live. | Mutation commits |
| Conflict | Explain stale state; reload; never silently overwrite. | 409 |

## Acceptance scenarios

1. Verified SERVICE IPN settles once and makes request Paid; duplicate callback has no duplicate effect.
2. Browser return claiming paid only displays Processing until verified callback/reconciliation.
3. Paid/Assigned/InProgress states show the committed due date when present; a Delivered request links to the immutable design in S17, while an eligible cancellation shows its independent refund state.

## Responsive and accessibility

Follow D11: 360px through desktop; stack columns and use labelled horizontal-scroll tables on narrow screens; keyboard-operable controls, visible focus, logical headings, associated form labels, aria-live status/error announcements, contrast >=4.5:1 (large text >=3:1), pointer targets >=24px. Preserve form data after recoverable failures; confirm destructive actions; disable duplicate submit while pending and enforce D02 idempotency server-side.

## Source documents

- [MFG-06 specification](../specs/spec-MFG-06.md)
- [Canonical decisions D01-D12](../docs/system-decisions.md)
- [Human factual input register](../docs/user-input-needed.md)
