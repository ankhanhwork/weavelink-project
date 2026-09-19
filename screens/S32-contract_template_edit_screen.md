# S32 — Contract Template Edit

| Property | Value |
|---|---|
| Route | `/admin/contracts/templates/{template_id}/edit` |
| Module | MFG-09 |
| Roles and ownership | Company Admin; server enforces role, company, assignment and ownership per D01. |
| Priority | P2 |
| Mockup | No mockup supplied. |

## Purpose and data

The Company Admin edits a template by creating a new version. Existing contracts retain the exact template version and rendered snapshot they used. All identifiers and permissions come from the server session; list filters are allowlisted and recoverable failures preserve entered values.

## Fields and validation

| Field | Type / requirement | Validation / source |
|---|---|---|
| template_id / current version | UUID plus read model | Load same-company name, structured body, status and version before editing. |
| new template_body |  safe text and allowlisted placeholders | new template_body: safe text and allowlisted placeholders; creates immutable new version. |
| expected_version | required integer | Stale save returns 409; previous immutable versions remain linked to existing contracts. |
| API errors | D02 envelope | 400 malformed; 422 invalid fields; 409 stale/duplicate; 429 rate limit; 503 dependency failure |

## Actions and navigation

| Action | Result | Destination |
|---|---|---|
| Save new version | Check expected_version and create immutable version. | S30 templates tab |
| Publish version | Activate the validated new version for future contracts. | S30 templates tab |
| Archive template | Disable future use; preserve versions referenced by contracts. | S30 templates tab |
| Cancel | Discard edits. | S30 templates tab |
### Global navigation access

Home and public catalog are available to Guest and authenticated users. Customer designs, orders, profile and notifications require the customer’s authenticated session. Company Admin routes are S10, S18, S28, S30, S36, S42 and S43; Sales Consultants use S20 and assigned-only S28/S29/S21 access; System Admin routes are S39, S40 and S41. The server rechecks company, membership, ownership and assignment for every route and notification target.
Functions: MFG-09/F-CONTR-006, MFG-09/F-CONTR-007. Global navigation and back behavior follow D11. Auth return paths must be internal allowlisted routes.

## Workflow transitions

Save new version → S30 templates tab; cancel → S30.

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

1. Edit creates a new version while prior version referenced by a contract remains immutable.
2. Stale expected_version returns 409 and reload preserves prior active version.

## Responsive and accessibility

Follow D11: 360px through desktop; stack columns and use labelled horizontal-scroll tables on narrow screens; keyboard-operable controls, visible focus, logical headings, associated form labels, aria-live status/error announcements, contrast >=4.5:1 (large text >=3:1), pointer targets >=24px. Preserve form data after recoverable failures; confirm destructive actions; disable duplicate submit while pending and enforce D02 idempotency server-side.

## Source documents

- [MFG-09 specification](../specs/spec-MFG-09.md)
- [Canonical decisions D01-D12](../docs/system-decisions.md)
- [Human factual input register](../docs/user-input-needed.md)
