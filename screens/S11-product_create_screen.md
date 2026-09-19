# S11 — Product Create

| Property | Value |
|---|---|
| Route | `/admin/products/new` |
| Module | MFG-04 |
| Roles and ownership | Company Admin; server enforces role, company, assignment and ownership per D01. |
| Priority | P2 |
| Mockup | No mockup supplied. |

## Purpose and data

Product creation validates all fields required for publication; a draft can be saved before publication requirements are complete. All identifiers and permissions come from the server session; list filters are allowlisted and recoverable failures preserve entered values.

## Fields and validation

| Field | Type / required | Validation and source |
|---|---|---|
| name | string, required | 1..120 trimmed characters. D04 |
| sku | string, required | Unique within company. D04 |
| category | string, required | Allowlisted configured category. D04 |
| unit_price_vnd | integer, required | Nonnegative; never floating point. D02/D04 |
| supported_sizes/colors/materials | arrays, required to publish | At least one of each; values from configured options. D04 |
| max_units_per_order | integer, required | 1..10000; quote exceeding capacity returns 422 CAPACITY_EXCEEDED. D04 refinement |
| image_asset_ids | UUID array | At least one safe image to publish; PNG/JPEG/WebP <=10MiB each, max5. D02/D04 |
## Actions and navigation

| Action | Result | Destination |
|---|---|---|
| Save draft | Validate SKU/options/price and create Draft product. | S12 |
| Save and publish | Require all D04 publish fields/images then transition to Published. | S10 |
| Cancel | Discard create form. | S10 |
### Global navigation access

Home and public catalog are available to Guest and authenticated users. Customer designs, orders, profile and notifications require the customer’s authenticated session. Company Admin routes are S10, S18, S28, S30, S36, S42 and S43; Sales Consultants use S20 and assigned-only S28/S29/S21 access; System Admin routes are S39, S40 and S41. The server rechecks company, membership, ownership and assignment for every route and notification target.
Functions: MFG-04/F-PROD-005, MFG-04/F-PROD-006. Global navigation and back behavior follow D11. Auth return paths must be internal allowlisted routes.

## Workflow transitions

Successful create saves Draft and opens S12; cancel → S10.

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

1. Valid product creates Draft with company-unique SKU and integer price.
2. Duplicate SKU or invalid image returns field errors; no partial product is saved.

## Responsive and accessibility

Follow D11: 360px through desktop; stack columns and use labelled horizontal-scroll tables on narrow screens; keyboard-operable controls, visible focus, logical headings, associated form labels, aria-live status/error announcements, contrast >=4.5:1 (large text >=3:1), pointer targets >=24px. Preserve form data after recoverable failures; confirm destructive actions; disable duplicate submit while pending and enforce D02 idempotency server-side.

## Source documents

- [MFG-04 specification](../specs/spec-MFG-04.md)
- [Canonical decisions D01-D12](../docs/system-decisions.md)
- [Human factual input register](../docs/user-input-needed.md)
