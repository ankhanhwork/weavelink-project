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

**Shown when:** The customer submits a DesignRequest against a Published Dony garment base, with the Business Buyer's uniform requirements or the Reseller Shop's own artwork, branding and specifications, optional safe attachments and a deadline at least three calendar days ahead. Dony will manufacture only after design, sample and order approval; this is not a ready-made-stock request. No fee is displayed or snapshotted at submission; Sales Admin assesses complexity afterward. All identifiers and permissions come from the server session; list filters are allowlisted and recoverable failures preserve entered values.

**The user leaves this screen when:** An authorized action in section 5 succeeds, the user follows a role-allowed global route, or they return to the validated originating route.

## 2. Mockup

![S15 historical reference](img/S15-design_service_request_screen.png)

Written behavior below takes precedence over obsolete sample content.

## 3. Element inventory

| # | Element | Type | Content / data source | Required | Validation |
|---|---|---|---|---|---|
| 1 | Screen heading | Heading | Design Service Request | Yes | Static route title. |
| 2 | Route | Navigation target | /design-requests/new?product_id={id} | Yes | Access checked on server. |
| 3 | product_id | Field / control | UUID of a Published Dony garment base. | As specified | The product supplies configurable production rules; it is not ready-made stock. |
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
| Loading | Load the S15 Design Service Request view model and show labelled progress; keep writes disabled until route data and authorization are resolved. | Request starts |
| Empty | No Design Service Request records match the current route/filter; preserve inputs and show only the screen’s authorized next action. | Screen has no eligible or matching record |
| Forbidden/not found | Return a safe 401/403/404 for S15 Design Service Request without revealing inaccessible record, customer, staff or payment details. | 401/403/404 |
| Error | For S15 Design Service Request, show the API code, message, field_errors and request_id; preserve safe user-entered values. | Request failure |
| Retry | Retry transient reads for S15 Design Service Request; retry a mutation only with its original idempotency key and identical payload, never as a new side effect. | Recoverable failure |
| Success | Refresh the committed Design Service Request data and show the next action permitted by its lifecycle and actor. | Valid action commits |
| Conflict | The Design Service Request data or lifecycle changed concurrently; reload authoritative state and do not replay a stale mutation. | Stale version, duplicate or invalid lifecycle transition |
## 5. Interactions and navigation

| # | Element | User action | System response | Goes to screen |
|---|---|---|---|---|
| 1 | Submit request | Activate | Create Submitted with fee null and requested deadline; persist admin notice and open the owned request in S17. | S17 /designs?tab=requests&request_id={id} |
| 2 | Cancel | Activate | Discard unsubmitted request. | S09 |

Portal: Customer owner. Route: /design-requests/new?product_id={id}. Back preserves the originating route and filters. Fallback: Customer→S26; Sales Admin→S28; Sales→S20; System Admin→S41; Guest→S01. Enforce role, ownership and assignment before rendering.

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
| MFG-05/F-DES-005 | **Request Service** — Render the design-service request form without a submission fee or payment step. |
| MFG-05/F-DES-006 | **Request Service** — Create a validated Submitted request with idempotency and return S17 request navigation; no submission fee/payment. |


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
