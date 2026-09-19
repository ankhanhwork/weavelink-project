# S22 — Create Order

| Property | Value |
|---|---|
| Route | `/orders/new?design_id={id}` |
| Module | MFG-06 |
| Roles and ownership | Customer owner; server enforces role, company, assignment and ownership per D01. |
| Priority | P1 |
| Mockup | Historical mockup: [img/S22-create_order_screen.png](img/S22-create_order_screen.png); written rules supersede sample text. |

## Purpose and data

The customer enters exact recipient name, phone and full delivery address (address line, ward and province), chooses positive integer quantities by supported size, and requests a server-priced quote for an owned eligible design. The server enforces product max_units_per_order. All identifiers and permissions come from the server session; list filters are allowlisted and recoverable failures preserve entered values.

## Fields and validation

| Field | Type / required | Validation and source |
|---|---|---|
| design_id | UUID, required | Customer-owned Saved self-design or Delivered consultant design. D04 |
| design_version / product_version | UUID/version, required | Must match current product rule; changed rules require explicit review. D04/D06 |
| quantity_by_size | object map, required | Supported size keys; each value positive integer; total quantity 1..10000. D06 |
| recipient_name | string, required | Trimmed, 1..100 characters. D06 |
| phone | string, required | 8..15 digits, optional leading +. D06 |
| address_line | string, required | Trimmed, 1..250 characters. D06 |
| ward | string, required | Trimmed, 1..100 characters. D06 |
| province | string, required | Trimmed, 1..100 characters. D06 |
| country | enum, required | Exactly VN. D06 |
| client customer_id/company_id/unit_price/total | prohibited | Resolve identity/company from session; server calculates all prices and total. D01/D06 |
| expected_version / Idempotency-Key | version and UUID, required for mutation | Reject stale state; financially significant order create is idempotent. D02 |
| capacity | server-derived integer | Reject quote if total exceeds product max_units_per_order with 422 CAPACITY_EXCEEDED. D04/D06 |
## Actions and navigation

| Action | Result | Destination |
|---|---|---|
| Get quote | Server computes amounts for design/options/quantities/address; no order created yet. | S25 |
| Select merge | Continue to explicit opt-in/terms. | S23 |
| Select design | Return to owned designs. | S17 |
### Global navigation access

Home and public catalog are available to Guest and authenticated users. Customer designs, orders, profile and notifications require the customer’s authenticated session. Company Admin routes are S10, S18, S28, S30, S36, S42 and S43; Sales Consultants use S20 and assigned-only S28/S29/S21 access; System Admin routes are S39, S40 and S41. The server rechecks company, membership, ownership and assignment for every route and notification target.
Functions: MFG-06/F-PAY-001, MFG-06/F-PAY-003. Global navigation and back behavior follow D11. Auth return paths must be internal allowlisted routes.

## Workflow transitions

Choose merge preference → S23; skip merge defaults standard → S25; choose design → S17.

## States

| State | Behavior | Trigger |
|---|---|---|
| Loading | Labelled progress/skeleton; disable duplicate submit. | Request starts |
| Empty | Render the screen-specific form/detail state; if a required route object is absent, show safe not-found and return to the authorized parent route. | Empty initial form or missing detail payload |
| Forbidden/not found | Safe message without revealing inaccessible identifiers. | 401/403/404 |
| Error | Show code, message, field_errors, request_id; preserve entered values. | Request failure |
| Retry | Retry reads on transient failure; reuse the same idempotency key only for mutations that require one under D02. | Recoverable failure |
| Success | Show committed state and next valid action; announce via aria-live. | Mutation commits |
| Conflict | Explain stale state; reload; never silently overwrite. | 409 |

## Acceptance scenarios

1. Exact VN address, supported size map totaling 1..10000, and owned eligible design pass quote creation.
2. Client-supplied customer/company/price/total is ignored or rejected; invalid phone/address/quantity returns field errors.

## Responsive and accessibility

Follow D11: 360px through desktop; stack columns and use labelled horizontal-scroll tables on narrow screens; keyboard-operable controls, visible focus, logical headings, associated form labels, aria-live status/error announcements, contrast >=4.5:1 (large text >=3:1), pointer targets >=24px. Preserve form data after recoverable failures; confirm destructive actions; disable duplicate submit while pending and enforce D02 idempotency server-side.

## Source documents

- [MFG-06 specification](../specs/spec-MFG-06.md)
- [Canonical decisions D01-D12](../docs/system-decisions.md)
- [Human factual input register](../docs/user-input-needed.md)
