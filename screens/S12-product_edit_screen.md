# S12 — Product Edit

| Property | Value |
|---|---|
| Route | `/admin/products/{product_id}/edit` |
| Module | MFG-04 |
| Roles and ownership | Company Admin; server enforces role, company, assignment and ownership per D01. |
| Priority | P2 |
| Mockup | No mockup supplied. |

## Purpose and data

Product edits are version-checked against the current company-owned product. Publishing requires all D04 fields; submitted order snapshots remain unchanged. All identifiers and permissions come from the server session; list filters are allowlisted and recoverable failures preserve entered values.

## Fields and validation

| Field | Type / required | Validation and source |
|---|---|---|
| product_id | UUID, required | Current company-owned product. D01/D04 |
| name/sku/category | string, required | Same constraints as S11; SKU unique within company. D04 |
| unit_price_vnd | integer, required | Nonnegative integer VND. D02/D04 |
| supported options/capacity | arrays/integer | Current product rules; max_units_per_order 1..10000. D04 |
| expected_version | version, required | Stale edit returns 409. D02 |
| quote consequence | server state | Rule changes invalidate old quote for review; submitted snapshots unchanged. D04 |
## Actions and navigation

| Action | Result | Destination |
|---|---|---|
| Save changes | Check expected_version; persist changes; invalidate/requote affected unpaid quote. | S10 |
| Edit design rules | Open rules editor. | S14 |
| Cancel | Discard edits. | S10 |
### Global navigation access

Home and public catalog are available to Guest and authenticated users. Customer designs, orders, profile and notifications require the customer’s authenticated session. Company Admin routes are S10, S18, S28, S30, S36, S42 and S43; Sales Consultants use S20 and assigned-only S28/S29/S21 access; System Admin routes are S39, S40 and S41. The server rechecks company, membership, ownership and assignment for every route and notification target.
Functions: MFG-04/F-PROD-007, MFG-04/F-PROD-008. Global navigation and back behavior follow D11. Auth return paths must be internal allowlisted routes.

## Workflow transitions

Save returns S10; design rules → S14; cancel → S10.

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

1. A current-version update saves and increments product version; stale version returns 409.
2. Changed rules invalidate affected outstanding quote for explicit review; signed/submitted snapshots remain unchanged.

## Responsive and accessibility

Follow D11: 360px through desktop; stack columns and use labelled horizontal-scroll tables on narrow screens; keyboard-operable controls, visible focus, logical headings, associated form labels, aria-live status/error announcements, contrast >=4.5:1 (large text >=3:1), pointer targets >=24px. Preserve form data after recoverable failures; confirm destructive actions; disable duplicate submit while pending and enforce D02 idempotency server-side.

## Source documents

- [MFG-04 specification](../specs/spec-MFG-04.md)
- [Canonical decisions D01-D12](../docs/system-decisions.md)
- [Human factual input register](../docs/user-input-needed.md)
