# S23 — Merge Option

| Property | Value |
|---|---|
| Route | `/orders/merge?design_id={id}` |
| Module | MFG-10 |
| Roles and ownership | Customer owner; server enforces role, company, assignment and ownership per D01. |
| Priority | P3 |
| Mockup | Historical mockup: [img/S23-merge_option_screen.png](img/S23-merge_option_screen.png); written rules supersede sample text. |

## Purpose and data

The customer explicitly opts into or out of merging and reviews the fixed 5 percent discount policy before quote calculation. All identifiers and permissions come from the server session; list filters are allowlisted and recoverable failures preserve entered values.

## Fields and validation

| Field | Type / requirement | Validation / source |
|---|---|---|
| merge_opt_in |  explicit boolean | merge_opt_in: explicit boolean; default false; acceptance stores merge policy_version. |
| merge_eligible | server-derived boolean | Enable opt-in only for an eligible design/product; otherwise show the reason and keep the standard route available. |
| merge_discount_vnd |  server floor(subtotal_vnd*5/100) | merge_discount_vnd: server floor(subtotal_vnd*5/100); max 3 extra calendar days; company honors promise without batch. |
| checkout_effect | read-only explanation | Saving preference issues a replacement quote; it creates no batch and applies no merge fee. |
| API errors | D02 envelope | 400 malformed; 422 invalid fields; 409 stale/duplicate; 429 rate limit; 503 dependency failure |

## Actions and navigation

| Action | Result | Destination |
|---|---|---|
| Accept merge policy | Persist explicit opt-in/version then request server quote. | S25 |
| Decline | Persist false and request standard quote. | S25 |
| Read terms | Show versioned conditions without silently accepting. | S24 |
### Global navigation access

Home and public catalog are available to Guest and authenticated users. Customer designs, orders, profile and notifications require the customer’s authenticated session. Company Admin routes are S10, S18, S28, S30, S36, S42 and S43; Sales Consultants use S20 and assigned-only S28/S29/S21 access; System Admin routes are S39, S40 and S41. The server rechecks company, membership, ownership and assignment for every route and notification target.
Functions: MFG-10/F-MER-001, MFG-10/F-MER-002, MFG-10/F-MER-003. Global navigation and back behavior follow D11. Auth return paths must be internal allowlisted routes.

## Workflow transitions

Accept/decline saved → S25 with quote; read terms → S24; back → S22.

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

1. Explicit opt-in stores policy version and server applies floor(subtotal*5/100), without creating a batch.
2. Decline sets no discount; displayed promise still honored if no batch forms.

## Responsive and accessibility

Follow D11: 360px through desktop; stack columns and use labelled horizontal-scroll tables on narrow screens; keyboard-operable controls, visible focus, logical headings, associated form labels, aria-live status/error announcements, contrast >=4.5:1 (large text >=3:1), pointer targets >=24px. Preserve form data after recoverable failures; confirm destructive actions; disable duplicate submit while pending and enforce D02 idempotency server-side.

## Source documents

- [MFG-10 specification](../specs/spec-MFG-10.md)
- [Canonical decisions D01-D12](../docs/system-decisions.md)
- [Human factual input register](../docs/user-input-needed.md)
