# Screen Spec: S22 Create Order

| Field | Value |
|---|---|
| Screen ID | `S22` |
| Screen name | Create Order |
| Actor | Customer owner |
| Priority | P1 |
| Belongs to module | [MFG-06](../specs/spec-MFG-06.md) |
| Route | `/orders/new?design_id={id}` |
| Mockup image | `img/S22-create_order_screen.png` |
| Status | Resolved implementation specification |

## 1. Purpose

**Shown when:** The customer enters exact recipient name, phone and full delivery address (address line, ward and province), chooses positive integer quantities by supported size, and requests a server-priced quote for an owned eligible design. The server enforces product max_units_per_order. All identifiers and permissions come from the server session; list filters are allowlisted and recoverable failures preserve entered values.

**The user leaves this screen when:** An authorized action in section 5 succeeds, the user follows a role-allowed global route, or they return to the validated originating route.

## 2. Mockup

![S22 historical reference](img/S22-create_order_screen.png)

Written behavior below takes precedence over obsolete sample content.

## 3. Element inventory

| # | Element | Type | Content / data source | Required | Validation |
|---|---|---|---|---|---|
| 1 | Screen heading | Heading | Create Order | Yes | Static route title. |
| 2 | Route | Navigation target | /orders/new?design_id={id} | Yes | Access checked on server. |
| 3 | design_id | Field / control | UUID, required | As specified | Customer-owned Saved self-design or Delivered consultant design. |
| 4 | design_version / product_version | Field / control | UUID/version, required | As specified | Must match current product rule; changed rules require explicit review. |
| 5 | quantity_by_size | Field / control | object map, required | As specified | Supported size keys; each value positive integer; total quantity 1..10000. |
| 6 | recipient_name | Field / control | string, required | As specified | Trimmed, 1..100 characters. |
| 7 | phone | Field / control | string, required | As specified | 8..15 digits, optional leading +. |
| 8 | address_line | Field / control | string, required | As specified | Trimmed, 1..250 characters. |
| 9 | ward | Field / control | string, required | As specified | Trimmed, 1..100 characters. |
| 10 | province | Field / control | string, required | As specified | Trimmed, 1..100 characters. |
| 11 | country | Field / control | enum, required | As specified | Exactly VN. |
| 12 | client customer_id/company_id/unit_price/total | Field / control | prohibited | As specified | Resolve identity/company from session; server calculates all prices and total. |
| 13 | expected_version / Idempotency-Key | Field / control | version and UUID, required for mutation | As specified | Reject stale state; financially significant order create is idempotent. |
| 14 | capacity | Field / control | server-derived integer | As specified | Reject quote if total exceeds product max_units_per_order with 422 CAPACITY_EXCEEDED. |
| 15 | Get quote | Action | Server computes amounts for design/options/quantities/address; no order created yet. | Available when authorized | Destination: S25 |
| 16 | Select merge | Action | Continue to explicit opt-in/terms. | Available when authorized | Destination: S23 |
| 17 | Select design | Action | Return to owned designs. | Available when authorized | Destination: S17 |

## 4. States

| State | What the user sees | Trigger |
|---|---|---|
| Loading | Labelled progress/skeleton; disable duplicate submit. | Request starts |
| Empty | Render the screen-specific form/detail state; if a required route object is absent, show safe not-found and return to the authorized parent route. | Empty initial form or missing detail payload |
| Forbidden/not found | Safe message without revealing inaccessible identifiers. | 401/403/404 |
| Error | Show code, message, field_errors, request_id; preserve entered values. | Request failure |
| Retry | Retry reads on transient failure; reuse the same idempotency key only for mutations that require one for the documented mutation. | Recoverable failure |
| Success | Show committed state and next valid action; announce via aria-live. | Mutation commits |
| Conflict | Explain stale state; reload; never silently overwrite. | 409 |

## 5. Interactions and navigation

| # | Element | User action | System response | Goes to screen |
|---|---|---|---|---|
| 1 | Get quote | Activate | Server computes amounts for design/options/quantities/address; no order created yet. | S25 |
| 2 | Select merge | Activate | Continue to explicit opt-in/terms. | S23 |
| 3 | Select design | Activate | Return to owned designs. | S17 |

Home and public catalog are available to Guest and authenticated users. Customer designs and customer orders are Customer-only; profile and notifications require authentication. Company Admin routes: S10, S18, S28, S30, S36, S42 and S43. Sales Consultant routes: S20 and assigned-only S21. System Admin routes: S39, S40 and S41. The server rechecks role, company, membership, ownership and assignment for every route and notification target. Back returns to the validated originating route and preserves list filters; without one, use S26 for Customer, S28 for Company Admin, S20 for Sales Consultant, S41 for System Admin, and S01 for Guest.

## 6. Screen-level rules

| Rule ID | Rule | Source |
|---|---|---|
| SR-001 | Access and ownership are checked server-side; do not trust submitted customer, company, role, price, or provider status. Apply 401/403/404 behavior and the field rules above. | Authorization and data ownership requirements |
| SR-002 | IDs are UUIDs; timestamps are UTC and displayed in Asia/Ho_Chi_Minh; money and quantities are integers. Mutations use expected_version; significant create/sign/pay/batch operations use idempotency keys. | Data representation and concurrency requirements |
| SR-003 | Apply the module lifecycle and validation rules linked below; preserve immutable submitted snapshots. | Module specification |
| SR-004 | Selected product and technical defaults are project implementation decisions; do not invent factual company, author, client-approval, or course identifiers. | Project implementation assumptions |

### Acceptance scenarios

1. Exact VN address, supported size map totaling 1..10000, and owned eligible design pass quote creation.
2. Client-supplied customer/company/price/total is ignored or rejected; invalid phone/address/quantity returns field errors.

## 7. Linked requirements

| FR ID (from the module spec) | What this screen does for it |
|---|---|
| MFG-06/F-PAY-001 | Implements this screen's validated user flow and the linked source function. |
| MFG-06/F-PAY-003 | Implements this screen's validated user flow and the linked source function. |
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
