# S21 — Consultation Detail

| Property | Value |
|---|---|
| Route | `/consultant/design-requests/{request_id}` |
| Module | MFG-08 |
| Roles and ownership | Assigned Consultant/Company Admin; server enforces role, company, assignment and ownership per D01. |
| Priority | P2 |
| Mockup | No mockup supplied. |

## Purpose and data

The Company Admin or currently assigned consultant sees one authorized consultation, its customer requirements, internal notes, deadline and design delivery controls. All identifiers and permissions come from the server session; list filters are allowlisted and recoverable failures preserve entered values.

## Fields and validation

| Field | Type / requirement | Validation / source |
|---|---|---|
| request_id |  UUID | request_id: UUID; consultant must be assigned or Company Admin in same company. |
| requirements / attachment_ids | read-only request snapshot | Show requirements and authorized 10-minute private asset links; do not expose public URLs. |
| internal_notes |  staff-only text | internal_notes: staff-only text; never returned to customer APIs. |
| final_design |  validated product options and safe private assets | final_design: validated product options and safe private assets; upload constraints per D02. |
| expected_version / delivery payload | version plus validated design | Delivery requires the current request version and creates an immutable design version. |
| API errors | D02 envelope | 400 malformed; 422 invalid fields; 409 stale/duplicate; 429 rate limit; 503 dependency failure |

## Actions and navigation

| Action | Result | Destination |
|---|---|---|
| Update consultation | Apply permitted CRM transition with version check; notes remain staff-only. | S21 |
| Deliver design | Validate assets/options; create immutable version; notify owner after commit. | S20 |
| Reopen closed CRM | Company Admin only; set InProgress with audit. | S21 |
### Global navigation access

Home and public catalog are available to Guest and authenticated users. Customer designs, orders, profile and notifications require the customer’s authenticated session. Company Admin routes are S10, S18, S28, S30, S36, S42 and S43; Sales Consultants use S20 and assigned-only S28/S29/S21 access; System Admin routes are S39, S40 and S41. The server rechecks company, membership, ownership and assignment for every route and notification target.
Functions: MFG-08/F-ORD-007, MFG-08/F-ORD-008; MFG-05/F-DES-009, MFG-05/F-DES-010, MFG-05/F-DES-011. Global navigation and back behavior follow D11. Auth return paths must be internal allowlisted routes.

## Workflow transitions

Deliver design → S20 assigned tab and customer notified; admin review → S18; cancel → S20.

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

1. Assigned consultant may deliver validated design, creating immutable version and notifying customer after commit.
2. Unassigned consultant cannot retrieve private attachments or internal notes.

## Responsive and accessibility

Follow D11: 360px through desktop; stack columns and use labelled horizontal-scroll tables on narrow screens; keyboard-operable controls, visible focus, logical headings, associated form labels, aria-live status/error announcements, contrast >=4.5:1 (large text >=3:1), pointer targets >=24px. Preserve form data after recoverable failures; confirm destructive actions; disable duplicate submit while pending and enforce D02 idempotency server-side.

## Source documents

- [MFG-08 specification](../specs/spec-MFG-08.md)
- [Canonical decisions D01-D12](../docs/system-decisions.md)
- [Human factual input register](../docs/user-input-needed.md)
