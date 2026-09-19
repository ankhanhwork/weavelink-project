# S09 — Product Detail

| Property | Value |
|---|---|
| Route | `/products/{product_id}` |
| Module | MFG-04 |
| Roles and ownership | Guest and authenticated user; design/request actions require Customer capability. |
| Priority | P1 |
| Mockup | Historical mockup: [img/S09-product_detail_screen.png](img/S09-product_detail_screen.png); written rules supersede sample text. |

## Purpose and data

The product detail shows the current Published product version, supported options, capacity and safe images. Hidden, Archived or inaccessible products return not found. All identifiers and permissions come from the server session; list filters are allowlisted and recoverable failures preserve entered values.

## Fields and validation

| Field | Type / requirement | Validation / source |
|---|---|---|
| product_id |  UUID path | product_id: UUID path; inaccessible/unpublished product returns 404. |
| name, company_id, SKU, category |  read-only product data. | name, company_id, SKU, category: read-only product data. |
| unit_price_vnd |  integer >=0 | unit_price_vnd: integer >=0; no client price edits. |
| sizes/colors/materials/capacity |  only currently supported options | sizes/colors/materials/capacity: only currently supported options; no checkout if Hidden/Archived. |
| API errors | D02 envelope | 400 malformed; 422 invalid fields; 409 stale/duplicate; 429 rate limit; 503 dependency failure |

## Actions and navigation

| Action | Result | Destination |
|---|---|---|
| Customize | Customer opens a design bound to current product_version; Guest/non-Customer authenticates with safe return_to. | S13 or S03 |
| Request design service | Customer opens DesignRequest form; Guest/non-Customer authenticates with safe return_to. | S15 or S03 |
| Back to results | Preserve catalog filters. | S08 |
### Global navigation access

Home and public catalog are available to Guest and authenticated users. Customer designs, orders, profile and notifications require the customer’s authenticated session. Company Admin routes are S10, S18, S28, S30, S36, S42 and S43; Sales Consultants use S20 and assigned-only S28/S29/S21 access; System Admin routes are S39, S40 and S41. The server rechecks company, membership, ownership and assignment for every route and notification target.
Functions: MFG-04/F-PROD-002. Global navigation and back behavior follow D11. Auth return paths must be internal allowlisted routes.

## Workflow transitions

Customize → S13; request consultant design → S15; back to catalog → S08.

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

1. Published product detail shows supported options and integer VND price from server.
2. Hidden/Archived/inaccessible product id returns 404; no checkout action is offered.

## Responsive and accessibility

Follow D11: 360px through desktop; stack columns and use labelled horizontal-scroll tables on narrow screens; keyboard-operable controls, visible focus, logical headings, associated form labels, aria-live status/error announcements, contrast >=4.5:1 (large text >=3:1), pointer targets >=24px. Preserve form data after recoverable failures; confirm destructive actions; disable duplicate submit while pending and enforce D02 idempotency server-side.

## Source documents

- [MFG-04 specification](../specs/spec-MFG-04.md)
- [Canonical decisions D01-D12](../docs/system-decisions.md)
- [Human factual input register](../docs/user-input-needed.md)
