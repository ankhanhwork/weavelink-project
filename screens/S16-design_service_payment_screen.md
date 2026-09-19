# Screen Spec: S16 Design Service Payment

| Field | Value |
|---|---|
| Screen ID | `S16` |
| Screen name | Design Service Payment |
| Actor | Customer owner |
| Priority | P3 |
| Belongs to module | [MFG-06](../specs/spec-MFG-06.md) |
| Route | `/design-requests/{request_id}/payment` |
| Mockup image | img/S16-design_service_payment_screen.png |
| Status | Resolved implementation specification |

## 1. Purpose

**Shown when:** The customer pays one AwaitingPayment design-service request at its snapshotted integer VND fee. Only a verified provider event changes it to Paid. All identifiers and permissions come from the server session; list filters are allowlisted and recoverable failures preserve entered values.

**The user leaves this screen when:** An authorized action in section 5 succeeds, the user follows a role-allowed global route, or they return to the validated originating route.

## 2. Mockup

![S16 historical reference](img/S16-design_service_payment_screen.png)

Written behavior below takes precedence over obsolete sample content.

## 3. Element inventory

| # | Element | Type | Content / data source | Required | Validation |
|---|---|---|---|---|---|
| 1 | Screen heading | Heading | Design Service Payment | Yes | Static route title. |
| 2 | Route | Navigation target | /design-requests/{request_id}/payment | Yes | Access checked on server. |
| 3 | request_id / product_id | Field / control | UUID, read-only | As specified | Request belongs to authenticated customer; inaccessible request returns 404. |
| 4 | amount_vnd / currency | Field / control | integer VND snapshot | As specified | Customer cannot edit; fee is fixed at request creation. |
| 5 | payment_attempt_id / status | Field / control | UUID / Pending, Succeeded, Failed, Expired | As specified | One active Pending attempt; new provider reference only after failure/expiry; session expires after 15 minutes. |
| 6 | request_status | Field / control | AwaitingPayment, Paid, Assigned, InProgress, Delivered, Cancelled, Expired | As specified | Refresh from server; display requested_deadline and committed_due_at when available. |
| 7 | requested_deadline / committed_due_at | Field / control | local date / nullable UTC timestamp | As specified | Requested date is preference; committed date is set at assignment. |
| 8 | API errors | Field / control | standard API error envelope | As specified | 400 malformed; 403 prohibited; 404 inaccessible request; 409 stale/state; 422 invalid input; 503 dependency failure |
| 9 | Initiate payment | Action | Create/reuse active Pending SERVICE transaction and redirect to VNPay sandbox/adapter. | Available when authorized | Destination: External VNPay |
| 10 | Return from provider | Action | Treat return as untrusted; poll transaction status. | Available when authorized | Destination: S16 |
| 11 | Cancel unpaid request | Action | Cancel only while AwaitingPayment; expire any pending attempt. | Available when authorized | Destination: S16 |
| 12 | Cancel paid request | Action | Full refund only while Paid and unassigned; reject after assignment. | Available when authorized | Destination: S16 |
| 13 | Verified paid | Action | Show receipt and status; enqueue admin notice; request becomes assignable. | Available when authorized | Destination: S16 / S18 admin |
| 14 | Failed/expired | Action | Preserve request and allow retry with fresh reference when eligible. | Available when authorized | Destination: S16 |

## 4. States

| State | What the user sees | Trigger |
|---|---|---|
| Loading | Labelled progress/skeleton; disable duplicate submit. | Request starts |
| Empty | Show this owned request status and payment instructions; a missing request receives a safe not-found message. | No payment attempt exists yet |
| Forbidden/not found | Safe message without revealing inaccessible identifiers. | 401/403/404 |
| Error | Show code, message, field_errors, request_id; preserve entered values. | Request failure |
| Retry | Retry reads on transient failure; reuse the same idempotency key only for mutations that require one for the documented mutation. | Recoverable failure |
| Success | Show committed state and next valid action; announce via aria-live. | Mutation commits |
| Conflict | Explain stale state; reload; never silently overwrite. | 409 |

## 5. Interactions and navigation

| # | Element | User action | System response | Goes to screen |
|---|---|---|---|---|
| 1 | Initiate payment | Activate | Create/reuse active Pending SERVICE transaction and redirect to VNPay sandbox/adapter. | External VNPay |
| 2 | Return from provider | Activate | Treat return as untrusted; poll transaction status. | S16 |
| 3 | Cancel unpaid request | Activate | Cancel only while AwaitingPayment; expire any pending attempt. | S16 |
| 4 | Cancel paid request | Activate | Full refund only while Paid and unassigned; reject after assignment. | S16 |
| 5 | Verified paid | Activate | Show receipt and status; enqueue admin notice; request becomes assignable. | S16 / S18 admin |
| 6 | Failed/expired | Activate | Preserve request and allow retry with fresh reference when eligible. | S16 |

Home and public catalog are available to Guest and authenticated users. Customer designs and customer orders are Customer-only; profile and notifications require authentication. Company Admin routes: S10, S18, S28, S30, S36, S42 and S43. Sales Consultant routes: S20 and assigned-only S21. System Admin routes: S39, S40 and S41. The server rechecks role, company, membership, ownership and assignment for every route and notification target. Back returns to the validated originating route and preserves list filters; without one, use S26 for Customer, S28 for Company Admin, S20 for Sales Consultant, S41 for System Admin, and S01 for Guest.

## 6. Screen-level rules

| Rule ID | Rule | Source |
|---|---|---|
| SR-001 | Access and ownership are checked server-side; do not trust submitted customer, company, role, price, or provider status. Apply 401/403/404 behavior and the field rules above. | Authorization and data ownership requirements |
| SR-002 | IDs are UUIDs; timestamps are UTC and displayed in Asia/Ho_Chi_Minh; money and quantities are integers. Mutations use expected_version; significant create/sign/pay/batch operations use idempotency keys. | Data representation and concurrency requirements |
| SR-003 | Apply the module lifecycle and validation rules linked below; preserve immutable submitted snapshots. | Module specification |
| SR-004 | Selected product and technical defaults are project implementation decisions; do not invent factual company, author, client-approval, or course identifiers. | Project implementation assumptions |

### Acceptance scenarios

1. Verified SERVICE IPN settles once and makes request Paid; duplicate callback has no duplicate effect.
2. Browser return claiming paid only displays Processing until verified callback/reconciliation.
3. Paid/Assigned/InProgress states show the committed due date when present; a Delivered request links to the immutable design in S17, while an eligible cancellation shows its independent refund state.

## 7. Linked requirements

| FR ID (from the module spec) | What this screen does for it |
|---|---|
| MFG-05/F-DES-007 | Implements this screen's validated user flow and the linked source function. |
| MFG-05/F-DES-008 | Implements this screen's validated user flow and the linked source function. |
| MFG-06/F-PAY-005 | Implements this screen's validated user flow and the linked source function. |
| MFG-06/F-PAY-006 | Implements this screen's validated user flow and the linked source function. |
Additional linked modules: [MFG-05](../specs/spec-MFG-05.md).

The rules in this screen and its linked module specifications are complete for implementation.

## 8. Responsive and accessibility notes

Support 360px through desktop; stack columns and use labelled horizontal-scroll tables on narrow screens. Controls are keyboard-operable with visible focus, logical headings, associated form labels, and aria-live status/error announcements. Text contrast is at least 4.5:1 (large text 3:1); pointer targets are at least 24px. Preserve user-entered data after recoverable failures. Confirm destructive actions, disable duplicate submit while pending, and enforce idempotency on the server.

## 9. Open questions

| # | Question | Blocking? | Status |
|---|---|---|---|
| 1 | No unresolved screen behavior questions remain; routes, fields, permissions, and defaults are resolved in this specification and its linked module requirements. | No | Resolved |

## Completion checklist

- [x] Route, actor, module, priority, and mockup status are identified.
- [x] Element fields, actions, validation, and data ownership are documented.
- [x] Loading, empty, forbidden, error, retry, success, and conflict states are documented.
- [x] Navigation and acceptance scenarios are explicit.
- [x] Responsive and accessibility requirements follow the shared baseline.
- [x] No unresolved screen-level decisions remain.
