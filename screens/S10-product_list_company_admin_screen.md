# S10 — Product List (Company Admin)

| Property | Value |
|---|---|
| Route | `/admin/products` |
| Module | MFG-04 |
| Roles and ownership | Company Admin; server enforces role, company, assignment and ownership per D01. |
| Priority | P2 |
| Mockup | No mockup supplied. |

## Purpose and data

The Company Admin sees products belonging to the selected active company, with Draft, Published, Hidden and Archived status and product-level actions. All identifiers and permissions come from the server session; list filters are allowlisted and recoverable failures preserve entered values.

## Fields and validation

| Field | Type / requirement | Validation / source |
|---|---|---|
| q |  optional trimmed search | q: optional trimmed search; status: Draft, Published, Hidden, Archived. |
| page / page_size / sort / filters | pagination and allowlisted query | page >=1; page_size 1..100, default 20; reject unknown sort/filter fields. |
| Each row |  product UUID, SKU, name, state, unit_price_vnd integer, updated_at, version. | Each row: product UUID, SKU, name, state, unit_price_vnd integer, updated_at, version. |
| company_scope | session-derived, read-only | Resolve company from active membership; ignore/reject a submitted company_id. |
| API errors | D02 envelope | 400 malformed; 422 invalid fields; 409 stale/duplicate; 429 rate limit; 503 dependency failure |

## Actions and navigation

| Action | Result | Destination |
|---|---|---|
| Create product | Open create form. | S11 |
| Edit content | Open company-owned product form. | S12 |
| Edit design rules | Open rule form for same product. | S14 |
| Publish/hide/archive | Confirm and apply allowed state transition; archive terminal and removes public listing. | S10 |
### Global navigation access

Home and public catalog are available to Guest and authenticated users. Customer designs, orders, profile and notifications require the customer’s authenticated session. Company Admin routes are S10, S18, S28, S30, S36, S42 and S43; Sales Consultants use S20 and assigned-only S28/S29/S21 access; System Admin routes are S39, S40 and S41. The server rechecks company, membership, ownership and assignment for every route and notification target.
Functions: MFG-04/F-PROD-004, MFG-04/F-PROD-005, MFG-04/F-PROD-006, MFG-04/F-PROD-007, MFG-04/F-PROD-008, MFG-04/F-PROD-009, MFG-04/F-PROD-010, MFG-04/F-PROD-011. Global navigation and back behavior follow D11. Auth return paths must be internal allowlisted routes.

## Workflow transitions

Create → S11; edit content → S12; edit design rules → S14; row details → S09; home → S01.

## States

| State | Behavior | Trigger |
|---|---|---|
| Loading | Labelled progress/skeleton; disable duplicate submit. | Request starts |
| Empty | Show no company products matching filters; preserve filters where present and explain eligibility/filter conditions. | Successful query returns no rows |
| Forbidden/not found | Safe message without revealing inaccessible identifiers. | 401/403/404 |
| Error | Show code, message, field_errors, request_id; preserve entered values. | Request failure |
| Retry | Retry reads on transient failure; reuse the same idempotency key only for mutations that require one under D02. | Recoverable failure |
| Success | Show committed state and next valid action; announce via aria-live. | Mutation commits |
| Conflict | Explain stale state; reload; never silently overwrite. | 409 |

## Acceptance scenarios

1. Company Admin sees only own-company products and can archive after confirmation.
2. Publishing fails until all D04 required content/options/capacity/safe image checks pass.

## Responsive and accessibility

Follow D11: 360px through desktop; stack columns and use labelled horizontal-scroll tables on narrow screens; keyboard-operable controls, visible focus, logical headings, associated form labels, aria-live status/error announcements, contrast >=4.5:1 (large text >=3:1), pointer targets >=24px. Preserve form data after recoverable failures; confirm destructive actions; disable duplicate submit while pending and enforce D02 idempotency server-side.

## Source documents

- [MFG-04 specification](../specs/spec-MFG-04.md)
- [Canonical decisions D01-D12](../docs/system-decisions.md)
- [Human factual input register](../docs/user-input-needed.md)
