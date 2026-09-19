# S13 — Product Design Tool

| Property | Value |
|---|---|
| Route | `/designs/new?product_id={id}` |
| Module | MFG-05 |
| Roles and ownership | Customer owner; server enforces role, company, assignment and ownership per D01. |
| Priority | P1 |
| Mockup | Historical mockup: [img/S13-product_design_tool_screen.png](img/S13-product_design_tool_screen.png); written rules supersede sample text. |

## Purpose and data

The customer edits a private 2D design tied to an owned product version. Saving creates a version; ordered snapshots are never overwritten. All identifiers and permissions come from the server session; list filters are allowlisted and recoverable failures preserve entered values.

## Fields and validation

| Field | Type / requirement | Validation / source |
|---|---|---|
| product_id/product_version |  required immutable selection | product_id/product_version: required immutable selection; unsupported or changed version requires reload. |
| size/color/material/print_method |  required values from current product rules. | size/color/material/print_method: required values from current product rules. |
| uploaded image |  PNG/JPEG/WebP, actual MIME checked, <=10MiB each, max5 | uploaded image: PNG/JPEG/WebP, actual MIME checked, <=10MiB each, max5; scan unsafe content. |
| print-area coordinates |  bounded to configured printable area | print-area coordinates: bounded to configured printable area; saved config versioned; drafts not orderable. |
| API errors | D02 envelope | 400 malformed; 422 invalid fields; 409 stale/duplicate; 429 rate limit; 503 dependency failure |

## Actions and navigation

| Action | Result | Destination |
|---|---|---|
| Preview | Render 2D configuration using current product rule and safe assets. | S13 |
| Save design | Persist immutable version owned by customer. | S17 |
| Continue to order | Allowed only saved design. | S22 |
| Request consultant | Start design service request. | S15 |
### Global navigation access

Home and public catalog are available to Guest and authenticated users. Customer designs, orders, profile and notifications require the customer’s authenticated session. Company Admin routes are S10, S18, S28, S30, S36, S42 and S43; Sales Consultants use S20 and assigned-only S28/S29/S21 access; System Admin routes are S39, S40 and S41. The server rechecks company, membership, ownership and assignment for every route and notification target.
Functions: MFG-05/F-DES-001, MFG-05/F-DES-002, MFG-05/F-DES-003. Global navigation and back behavior follow D11. Auth return paths must be internal allowlisted routes.

## Workflow transitions

Save eligible self-design → S17; order saved design → S22; request design service → S15; cancel → S09.

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

1. Saved design stores product and rule versions plus customer ownership; image is private scanned asset.
2. Draft cannot be ordered; invalid coordinate or changed rule blocks save and preserves editable configuration.

## Responsive and accessibility

Follow D11: 360px through desktop; stack columns and use labelled horizontal-scroll tables on narrow screens; keyboard-operable controls, visible focus, logical headings, associated form labels, aria-live status/error announcements, contrast >=4.5:1 (large text >=3:1), pointer targets >=24px. Preserve form data after recoverable failures; confirm destructive actions; disable duplicate submit while pending and enforce D02 idempotency server-side.

## Source documents

- [MFG-05 specification](../specs/spec-MFG-05.md)
- [Canonical decisions D01-D12](../docs/system-decisions.md)
- [Human factual input register](../docs/user-input-needed.md)
