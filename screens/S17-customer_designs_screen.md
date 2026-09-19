# S17 — Customer Designs

| Property | Value |
|---|---|
| Route | `/designs` |
| Module | MFG-05 |
| Roles and ownership | Customer owner; server enforces role, company, assignment and ownership per D01. |
| Priority | P3 |
| Mockup | Historical mockup: [img/S17-customer_designs_screen.png](img/S17-customer_designs_screen.png); written rules supersede sample text. |

## Purpose and data

The customer sees only owned saved designs and consultant deliveries, with product/version context and actions valid for each design state. All identifiers and permissions come from the server session; list filters are allowlisted and recoverable failures preserve entered values.

## Fields and validation

| Field | Type / requirement | Validation / source |
|---|---|---|
| tab | enum: Draft, Saved, Delivered | Filter scoped to authenticated customer_id. |
| design_id / design_version / product_id | UUID / integer version / UUID | Show latest owned version and associated product version. |
| status | Draft, Saved, Delivered | Draft is editable but not orderable; Saved self-design and Delivered consultant design are orderable. |
| preview_asset_id | private UUID | Access-checked expiring URL; customer-owned assets only. |
| updated_at | UTC timestamp | Display in Asia/Ho_Chi_Minh. |
| API errors | D02 envelope | 400 malformed; 404 inaccessible design; 409 stale version; preserve filters on retry. |

## Actions and navigation

| Action | Result | Destination |
|---|---|---|
| Edit saved design | Create new design version; never alter ordered snapshot. | S13 |
| Order design | Permit saved self-design or delivered consultant design only. | S22 |
| Request design service | Create new request for selected product. | S15 |
### Global navigation access

Home and public catalog are available to Guest and authenticated users. Customer designs, orders, profile and notifications require the customer’s authenticated session. Company Admin routes are S10, S18, S28, S30, S36, S42 and S43; Sales Consultants use S20 and assigned-only S28/S29/S21 access; System Admin routes are S39, S40 and S41. The server rechecks company, membership, ownership and assignment for every route and notification target.
Functions: MFG-05/F-DES-004. Global navigation and back behavior follow D11. Auth return paths must be internal allowlisted routes.

## Workflow transitions

Edit saved design → S13; order eligible design → S22; request new design service → S15; home → S01.

## States

| State | Behavior | Trigger |
|---|---|---|
| Loading | Labelled progress/skeleton; disable duplicate submit. | Request starts |
| Empty | Show no owned designs in the selected state; preserve filters where present and explain eligibility/filter conditions. | Successful query returns no rows |
| Forbidden/not found | Safe message without revealing inaccessible identifiers. | 401/403/404 |
| Error | Show code, message, field_errors, request_id; preserve entered values. | Request failure |
| Retry | Retry reads on transient failure; reuse the same idempotency key only for mutations that require one under D02. | Recoverable failure |
| Success | Show committed state and next valid action; announce via aria-live. | Mutation commits |
| Conflict | Explain stale state; reload; never silently overwrite. | 409 |

## Acceptance scenarios

1. Only own designs appear; Saved and Delivered records offer order action while Draft does not.
2. An ordered design edit creates a new version and cannot mutate order snapshot.

## Responsive and accessibility

Follow D11: 360px through desktop; stack columns and use labelled horizontal-scroll tables on narrow screens; keyboard-operable controls, visible focus, logical headings, associated form labels, aria-live status/error announcements, contrast >=4.5:1 (large text >=3:1), pointer targets >=24px. Preserve form data after recoverable failures; confirm destructive actions; disable duplicate submit while pending and enforce D02 idempotency server-side.

## Source documents

- [MFG-05 specification](../specs/spec-MFG-05.md)
- [Canonical decisions D01-D12](../docs/system-decisions.md)
- [Human factual input register](../docs/user-input-needed.md)
