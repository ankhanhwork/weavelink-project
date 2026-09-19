# S01 — Home Page

| Property | Value |
|---|---|
| Route | `/` |
| Module | MFG-04 |
| Roles and ownership | Guest and all authenticated roles; server filters staff/customer data by D01. |
| Priority | P1 |
| Mockup | Historical mockup: [img/S01-home_page.png](img/S01-home_page.png); written rules supersede sample text. |

## Purpose and data

The landing page queries only currently Published products and configured public company contacts. It keeps sign-up, sign-in, catalog browsing and named information panels available without exposing staff data. All identifiers and permissions come from the server session; list filters are allowlisted and recoverable failures preserve entered values.

## Fields and validation

| Field | Type / requirement | Validation / source |
|---|---|---|
| product_id |  UUID, nullable | product_id: UUID, nullable; only Published products with public-safe name/image/price. |
| company_name/contact_links |  strings from configured company profile | company_name/contact_links: strings from configured company profile; omit unknown contacts. |
| navigation_visibility | role-derived | Show Sign up/Sign in to Guest; render authenticated navigation from server permissions. |
| API errors | D02 envelope | 400 malformed; 422 invalid fields; 409 stale/duplicate; 429 rate limit; 503 dependency failure |

## Actions and navigation

| Action | Result | Destination |
|---|---|---|
| Browse published item | Open product detail. | S09 |
| Start customization/request | Preserve intended route through sign-in when needed. | S13 or S15 |
| About/contact/help/policies | Open named content panel on S01; show configured contacts only. | S01 panel |
### Global navigation access

Home and public catalog are available to Guest and authenticated users. Customer designs, orders, profile and notifications require the customer’s authenticated session. Company Admin routes are S10, S18, S28, S30, S36, S42 and S43; Sales Consultants use S20 and assigned-only S28/S29/S21 access; System Admin routes are S39, S40 and S41. The server rechecks company, membership, ownership and assignment for every route and notification target.
Functions: MFG-04/F-PROD-001. Global navigation and back behavior follow D11. Auth return paths must be internal allowlisted routes.

## Workflow transitions

Sign up → S02; sign in → S03; browse → S08; about/contact/help/policies open named panel on S01.

## States

| State | Behavior | Trigger |
|---|---|---|
| Loading | Labelled progress/skeleton; disable duplicate submit. | Request starts |
| Empty | Show no Published products or configured public links; preserve filters where present and explain eligibility/filter conditions. | Successful query returns no rows |
| Forbidden/not found | Safe message without revealing inaccessible identifiers. | 401/403/404 |
| Error | Show code, message, field_errors, request_id; preserve entered values. | Request failure |
| Retry | Retry reads on transient failure; reuse the same idempotency key only for mutations that require one under D02. | Recoverable failure |
| Success | Show committed state and next valid action; announce via aria-live. | Mutation commits |
| Conflict | Explain stale state; reload; never silently overwrite. | 409 |

## Acceptance scenarios

1. When no published products exist, show an honest empty catalog panel and continue navigation.
2. When no company contact is configured, hide contact/social links and render no fabricated values.

## Responsive and accessibility

Follow D11: 360px through desktop; stack columns and use labelled horizontal-scroll tables on narrow screens; keyboard-operable controls, visible focus, logical headings, associated form labels, aria-live status/error announcements, contrast >=4.5:1 (large text >=3:1), pointer targets >=24px. Preserve form data after recoverable failures; confirm destructive actions; disable duplicate submit while pending and enforce D02 idempotency server-side.

## Source documents

- [MFG-04 specification](../specs/spec-MFG-04.md)
- [Canonical decisions D01-D12](../docs/system-decisions.md)
- [Human factual input register](../docs/user-input-needed.md)
