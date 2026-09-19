# S15 — Design Service Request

| Property | Value |
|---|---|
| Route | `/design-requests/new?product_id={id}` |
| Module | MFG-05 |
| Roles and ownership | Customer owner; server enforces role, company, assignment and ownership per D01. |
| Priority | P3 |
| Mockup | Historical mockup: [img/S15-design_service_request_screen.png](img/S15-design_service_request_screen.png); written rules supersede sample text. |

## Purpose and data

The customer submits a DesignRequest for an owned Published product, with requirements, optional safe attachments and a deadline at least three calendar days ahead. The service fee is snapshotted at submission. All identifiers and permissions come from the server session; list filters are allowlisted and recoverable failures preserve entered values.

## Fields and validation

| Field | Type / requirement | Validation / source |
|---|---|---|
| product_id |  UUID, must be published in selected company. | product_id: UUID, must be published in selected company. |
| requirements |  required string 20..5000 trimmed chars. | requirements: required string 20..5000 trimmed chars. |
| attachment_ids |  optional private image UUIDs | attachment_ids: optional private image UUIDs; max5, MIME PNG/JPEG/WebP <=10MiB each, access checked. |
| requested_deadline |  optional ISO date >=3 calendar days from submission | requested_deadline: optional ISO date >=3 calendar days from submission; not guaranteed. |
| fee_vnd |  server default 200000 integer, snapshotted | fee_vnd: server default 200000 integer, snapshotted; status AwaitingPayment. |
| API errors | D02 envelope | 400 malformed; 422 invalid fields; 409 stale/duplicate; 429 rate limit; 503 dependency failure |

## Actions and navigation

| Action | Result | Destination |
|---|---|---|
| Submit request | Create AwaitingPayment request and snapshot fee/deadline; no assignment before successful payment. | S16 |
| Cancel | Discard unsubmitted request. | S09 |
### Global navigation access

Home and public catalog are available to Guest and authenticated users. Customer designs, orders, profile and notifications require the customer’s authenticated session. Company Admin routes are S10, S18, S28, S30, S36, S42 and S43; Sales Consultants use S20 and assigned-only S28/S29/S21 access; System Admin routes are S39, S40 and S41. The server rechecks company, membership, ownership and assignment for every route and notification target.
Functions: MFG-05/F-DES-005, MFG-05/F-DES-006. Global navigation and back behavior follow D11. Auth return paths must be internal allowlisted routes.

## Workflow transitions

Create AwaitingPayment request → S16; cancel → S09 or validated origin.

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

1. Valid request creates AwaitingPayment with 200000 VND default snapshot and no assignment.
2. Deadline less than 3 calendar days or requirements outside 20..5000 chars is rejected.

## Responsive and accessibility

Follow D11: 360px through desktop; stack columns and use labelled horizontal-scroll tables on narrow screens; keyboard-operable controls, visible focus, logical headings, associated form labels, aria-live status/error announcements, contrast >=4.5:1 (large text >=3:1), pointer targets >=24px. Preserve form data after recoverable failures; confirm destructive actions; disable duplicate submit while pending and enforce D02 idempotency server-side.

## Source documents

- [MFG-05 specification](../specs/spec-MFG-05.md)
- [Canonical decisions D01-D12](../docs/system-decisions.md)
- [Human factual input register](../docs/user-input-needed.md)
