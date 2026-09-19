# S08 — Product Catalog

| Property | Value |
|---|---|
| Route | `/catalog` |
| Module | MFG-04 |
| Roles and ownership | Guest/Member; server enforces role, company, assignment and ownership per D01. |
| Priority | P1 |
| Mockup | Historical mockup: [img/S08-product_catalog_screen.png](img/S08-product_catalog_screen.png); written rules supersede sample text. |

## Purpose and data

The public catalog returns Published products only, with allowlisted search, category, size, color and sort filters. All identifiers and permissions come from the server session; list filters are allowlisted and recoverable failures preserve entered values.

## Fields and validation

| Field | Type / requirement | Validation / source |
|---|---|---|
| q |  optional trimmed search string. | q: optional trimmed search string. |
| category,size,color |  optional allowlisted filters supported by product. | category,size,color: optional allowlisted filters supported by product. |
| sort |  allowlisted (name, unit_price_vnd, created_at) | sort: allowlisted (name, unit_price_vnd, created_at); page>=1, page_size 1..100 default20. |
| Results |  Published products only | Results: Published products only; unit_price_vnd integer. |
| API errors | D02 envelope | 400 malformed; 422 invalid fields; 409 stale/duplicate; 429 rate limit; 503 dependency failure |

## Actions and navigation

| Action | Result | Destination |
|---|---|---|
| Search/filter/sort | Query published products using allowlisted filters and pagination. | S08 |
| Open product | Load public detail after published-state check. | S09 |
### Global navigation access

Home and public catalog are available to Guest and authenticated users. Customer designs, orders, profile and notifications require the customer’s authenticated session. Company Admin routes are S10, S18, S28, S30, S36, S42 and S43; Sales Consultants use S20 and assigned-only S28/S29/S21 access; System Admin routes are S39, S40 and S41. The server rechecks company, membership, ownership and assignment for every route and notification target.
Functions: MFG-04/F-PROD-001, MFG-04/F-PROD-002. Global navigation and back behavior follow D11. Auth return paths must be internal allowlisted routes.

## Workflow transitions

Product card → S09; guest design/order action → S03 with return path; home → S01.

## States

| State | Behavior | Trigger |
|---|---|---|
| Loading | Labelled progress/skeleton; disable duplicate submit. | Request starts |
| Empty | Show no Published products matching search and filters; preserve filters where present and explain eligibility/filter conditions. | Successful query returns no rows |
| Forbidden/not found | Safe message without revealing inaccessible identifiers. | 401/403/404 |
| Error | Show code, message, field_errors, request_id; preserve entered values. | Request failure |
| Retry | Retry reads on transient failure; reuse the same idempotency key only for mutations that require one under D02. | Recoverable failure |
| Success | Show committed state and next valid action; announce via aria-live. | Mutation commits |
| Conflict | Explain stale state; reload; never silently overwrite. | 409 |

## Acceptance scenarios

1. Search and filter return only Published products and preserve page/filter state.
2. Hidden/Archived product never appears even when its identifier is supplied as a filter.

## Responsive and accessibility

Follow D11: 360px through desktop; stack columns and use labelled horizontal-scroll tables on narrow screens; keyboard-operable controls, visible focus, logical headings, associated form labels, aria-live status/error announcements, contrast >=4.5:1 (large text >=3:1), pointer targets >=24px. Preserve form data after recoverable failures; confirm destructive actions; disable duplicate submit while pending and enforce D02 idempotency server-side.

## Source documents

- [MFG-04 specification](../specs/spec-MFG-04.md)
- [Canonical decisions D01-D12](../docs/system-decisions.md)
- [Human factual input register](../docs/user-input-needed.md)
