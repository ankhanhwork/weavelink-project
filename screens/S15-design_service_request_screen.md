# Screen Spec: S15 Design Service Request

| Field | Value |
|---|---|
| Screen ID | `S15` |
| Screen name | Design Service Request |
| Actor | Customer owner |
| Priority | P3 |
| Belongs to module | [MFG-05](../specs/spec-MFG-05.md) |
| Route | `/design-requests/new?product_id={id}` |
| Mockup image | img/S15-design_service_request_screen.png |
| Status | Resolved implementation specification |

## 1. Purpose

**Shown when:** The customer submits a DesignRequest for an owned Published product, with requirements, optional safe attachments and a deadline at least three calendar days ahead. No fee is displayed or snapshotted at submission; Company Admin assesses complexity afterward. All identifiers and permissions come from the server session; list filters are allowlisted and recoverable failures preserve entered values.

**The user leaves this screen when:** An authorized action in section 5 succeeds, the user follows a role-allowed global route, or they return to the validated originating route.

## 2. Mockup

![S15 historical reference](img/S15-design_service_request_screen.png)

Written behavior below takes precedence over obsolete sample content.

## 3. Element inventory

| # | Element | Type | Content / data source | Required | Validation |
|---|---|---|---|---|---|
| 1 | Screen heading | Heading | Design Service Request | Yes | Static route title. |
| 2 | Route | Navigation target | /design-requests/new?product_id={id} | Yes | Access checked on server. |
| 3 | product_id | Field / control | UUID, must be published in selected company. | As specified | product_id: UUID, must be published in selected company. |
| 4 | requirements | Field / control | required string 20..5000 trimmed chars. | As specified | requirements: required string 20..5000 trimmed chars. |
| 5 | attachment_ids | Field / control | optional private image UUIDs | As specified | attachment_ids: optional private image UUIDs; max5, MIME PNG/JPEG/WebP <=10MiB each, access checked. |
| 6 | requested_deadline | Field / control | optional ISO date >=3 calendar days from submission | As specified | requested_deadline: optional ISO date >=3 calendar days from submission; not guaranteed. |
| 7 | assessment_notice | Read-only text | Simple work is free; Complex fee requires acceptance and is collected only with an eventual order. | Yes | Do not display a fee amount or initiate payment at submission. |
| 8 | API errors | Field / control | standard API error envelope | As specified | 400 malformed; 422 invalid fields; 409 stale/duplicate; 429 rate limit; 503 dependency failure |
| 9 | Submit request | Action | Create Submitted with fee null and requested deadline; persist admin notice and open the owned request in S17. | Available when authorized | Destination: S17 /designs?tab=requests&request_id={id} |
| 10 | Cancel | Action | Discard unsubmitted request. | Available when authorized | Destination: S09 |

## 4. States

| State | What the user sees | Trigger |
|---|---|---|
| Loading | Labelled progress/skeleton; disable duplicate submit. | Request starts |
| Empty | Render the screen-specific form/detail state; if a required route object is absent, show safe not-found and return to the authorized parent route. | Empty initial form or missing detail payload |
| Forbidden/not found | Safe message without revealing inaccessible identifiers. | 401/403/404 |
| Error | Show code, message, field_errors, request_id; preserve entered values. | Request failure |
| Retry | Retry reads on transient failure; reuse the same idempotency key only for mutations that require one for the documented mutation. | Recoverable failure |
| Success | Show committed state and next valid action; announce via aria-live. | Mutation commits |
| Conflict | Explain stale state; reload; never silently overwrite. | 409 |

## 5. Interactions and navigation

| # | Element | User action | System response | Goes to screen |
|---|---|---|---|---|
| 1 | Submit request | Activate | Create Submitted with fee null and requested deadline; persist admin notice and open the owned request in S17. | S17 /designs?tab=requests&request_id={id} |
| 2 | Cancel | Activate | Discard unsubmitted request. | S09 |

Home and public catalog are available to Guest and authenticated users. Customer designs and customer orders are Customer-only; profile and notifications require authentication. Company Admin routes: S10, S18, S28, S30, S36, S42 and S43. Sales Consultant routes: S20 and assigned-only S21. System Admin routes: S39, S40 and S41. The server rechecks role, company, membership, ownership and assignment for every route and notification target. Back returns to the validated originating route and preserves list filters; without one, use S26 for Customer, S28 for Company Admin, S20 for Sales Consultant, S41 for System Admin, and S01 for Guest.

## 6. Screen-level rules

| Rule ID | Rule | Source |
|---|---|---|
| SR-001 | Access and ownership are checked server-side; do not trust submitted customer, company, role, price, or provider status. Apply 401/403/404 behavior and the field rules above. | Authorization and data ownership requirements |
| SR-002 | IDs are UUIDs; timestamps are UTC and displayed in Asia/Ho_Chi_Minh; money and quantities are integers. Mutations use expected_version; significant create/sign/pay/batch operations use idempotency keys. | Data representation and concurrency requirements |
| SR-003 | Apply the module lifecycle and validation rules linked below; preserve immutable submitted snapshots. | Module specification |
| SR-004 | Selected product and technical defaults are project implementation decisions; do not invent factual company, author, client-approval, or course identifiers. | Project implementation assumptions |

### Acceptance scenarios

1. Valid request creates Submitted with fee null, no payment/assignment and one admin notice; opens the S17 request view. Duplicate submission replays the same request.
2. Deadline less than 3 calendar days or requirements outside 20..5000 chars is rejected.

## 7. Linked requirements

| FR ID (from the module spec) | What this screen does for it |
|---|---|
| MFG-05/F-DES-005 | Implements this screen's validated user flow and the linked source function. |
| MFG-05/F-DES-006 | Implements this screen's validated user flow and the linked source function. |
The rules in this screen and its linked module specifications are complete for implementation.

## 8. Responsive and accessibility notes

Support 360px through desktop; stack columns and use labelled horizontal-scroll tables on narrow screens. Controls are keyboard-operable with visible focus, logical headings, associated form labels, and aria-live status/error announcements. Text contrast is at least 4.5:1 (large text 3:1); pointer targets are at least 24px. Preserve user-entered data after recoverable failures. Confirm destructive actions, disable duplicate submit while pending, and enforce idempotency on the server.

## 9. Open questions

| # | Question | Blocking? | Status |
|---|---|---|---|
| 1 | No unresolved screen behavior questions remain; routes, fields, permissions, and defaults are resolved in this specification and its linked module requirements. | No | Resolved |

## Completion checklist

- [x] Route, actor, module, priority, and mockup status are identified.
- [x] Element fields, actions, validation, and data ownership are documented.
- [x] Loading, empty, forbidden, error, retry, success, and conflict states are documented.
- [x] Navigation and acceptance scenarios are explicit.
- [x] Responsive and accessibility requirements follow the shared baseline.
- [x] No unresolved screen-level decisions remain.
