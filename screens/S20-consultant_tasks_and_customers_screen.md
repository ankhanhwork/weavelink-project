# Screen Spec: S20 Consultant Tasks and Customers

| Field | Value |
|---|---|
| Screen ID | `S20` |
| Screen name | Consultant Tasks and Customers |
| Actor | Sales |
| Priority | P2 |
| Belongs to module | [MFG-08](../specs/spec-MFG-08.md) |
| Route | `/consultant/tasks?tab=assigned,customers` |
| Mockup image | img/S20-consultant_tasks_and_customers_screen.png |
| Status | Resolved implementation specification |

## 1. Purpose

**Shown when:** The consultant sees only their assigned design requests and CRM customers. Design-task status and CRM consultation status are presented separately. All identifiers and permissions come from the server session; list filters are allowlisted and recoverable failures preserve entered values.

**The user leaves this screen when:** An authorized action in section 5 succeeds, the user follows a role-allowed global route, or they return to the validated originating route.

## 2. Mockup

![Historical visual reference](img/S20-consultant_tasks_and_customers_screen.png)

Written behavior below takes precedence over obsolete sample content.

## 3. Element inventory

| # | Element | Type | Content / data source | Required | Validation |
|---|---|---|---|---|---|
| 1 | Screen heading | Heading | Consultant Tasks and Customers | Yes | Static route title. |
| 2 | Route | Navigation target | /consultant/tasks?tab=assigned,customers | Yes | Access checked on server. |
| 3 | tab | Field / control | enum: assigned or customers; default assigned | As specified | Both tabs query only the current consultant assignments and assigned customer records. |
| 4 | design_request_status | Field / control | Submitted, UnderReview, FeeProposed, Approved, Assigned, InProgress, Delivered, Cancelled, Rejected | As specified | Display-only task state; only currently assigned Assigned or InProgress work is actionable. |
| 5 | crm_status | Field / control | New, Contacted, InProgress, ClosedWon, ClosedLost | As specified | Applies only to CRM records; transitions follow MFG-08. |
| 6 | customer_id / request_id / buyer_organization_id | Field / control | read-only UUIDs | As specified | Derived from the authorized assignment; organization identifies a Business Buyer or Reseller Shop but grants no staff access. |
| 7 | page / page_size / sort | Field / control | integer / integer / enum | As specified | documented pagination bounds; sort allowlist is updated_at, requested_deadline or status. |
| 8 | API errors | Field / control | standard API error envelope | As specified | 400 malformed; 422 invalid filters/transitions; 403 prohibited action; 404 inaccessible assignment; 409 stale version/state; 503 dependency failure. |
| 9 | Open assigned task | Action | Load assigned customer/request context. | Available when authorized | Destination: S21 |
| 10 | Update CRM status | Action | Apply New→Contacted→InProgress→ClosedWon/ClosedLost; reopen only by Sales Admin. | Available when authorized | Destination: S20 |
| 11 | Switch tab | Action | Show assigned customers only. | Available when authorized | Destination: S20 customers tab |

## 4. States

| State | What the user sees | Trigger |
|---|---|---|
| Loading | Load the S20 Consultant Tasks and Customers view model and show labelled progress; keep writes disabled until route data and authorization are resolved. | Request starts |
| Empty | Show no tasks assigned to this consultant; preserve filters where present and explain eligibility/filter conditions. | Successful query returns no rows |
| Forbidden/not found | Return a safe 401/403/404 for S20 Consultant Tasks and Customers without revealing inaccessible record, customer, staff or payment details. | 401/403/404 |
| Error | For S20 Consultant Tasks and Customers, show the API code, message, field_errors and request_id; preserve safe user-entered values. | Request failure |
| Retry | Retry transient reads for S20 Consultant Tasks and Customers; retry a mutation only with its original idempotency key and identical payload, never as a new side effect. | Recoverable failure |
| Success | Refresh S20 Consultant Tasks and Customers from the committed server response, expose only the next role/state-allowed action and announce the result via aria-live. | Mutation commits |
| Conflict | For a stale S20 Consultant Tasks and Customers version or lifecycle state, reload authoritative data, explain the conflict and require explicit review before resubmission. | 409 |

## 5. Interactions and navigation

| # | Element | User action | System response | Goes to screen |
|---|---|---|---|---|
| 1 | Open assigned task | Activate | Load assigned customer/request context. | S21 |
| 2 | Update CRM status | Activate | Apply New→Contacted→InProgress→ClosedWon/ClosedLost; reopen only by Sales Admin. | S20 |
| 3 | Switch tab | Activate | Show assigned customers only. | S20 customers tab |

Home and public catalog are available to Guest and authenticated users. Customer designs and customer orders are Customer-only; profile and notifications require authentication. Sales Admin routes: S10, S18, S28, S30, S36, S42 and S43. Sales routes: S20 and assigned-only S21. System Admin routes: S39, S40 and S41. The server rechecks internal role, customer ownership and staff assignment for every route and notification target. Back returns to the validated originating route and preserves list filters; without one, use S26 for Customer, S28 for Sales Admin, S20 for Sales, S41 for System Admin, and S01 for Guest.

## 6. Screen-level rules

| Rule ID | Rule | Source |
|---|---|---|
| SR-001 | Access and ownership are checked server-side; do not trust submitted customer, company, role, price, or provider status. Apply 401/403/404 behavior and the field rules above. | Authorization and data ownership requirements |
| SR-002 | IDs are UUIDs; timestamps are UTC and displayed in Asia/Ho_Chi_Minh; money and quantities are integers. Mutations use expected_version; significant create/sign/pay/batch operations use idempotency keys. | Data representation and concurrency requirements |
| SR-003 | Apply the module lifecycle and validation rules linked below; preserve immutable submitted snapshots. | Module specification |
| SR-004 | Selected product and technical defaults are project implementation decisions; do not invent factual company, author, client-approval, or course identifiers. | Project implementation assumptions |

### Acceptance scenarios

1. Consultant sees only assigned tasks/customers; another consultant's ID returns 404.
2. Valid CRM transition follows allowed state graph; reopening closed state requires Sales Admin.

## 7. Linked requirements

| FR ID (from the module spec) | What this screen does for it |
|---|---|
| MFG-08/F-ORD-005 | UI touchpoint for **Assigned Cust View**; this screen defines the visible action/result, while the module spec owns server authorization, validation and persistence. |
| MFG-08/F-ORD-006 | UI touchpoint for **Context View**; this screen defines the visible action/result, while the module spec owns server authorization, validation and persistence. |
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
