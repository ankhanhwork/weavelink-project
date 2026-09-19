# Screen Spec: S34 Contract Detail (Customer)

| Field | Value |
|---|---|
| Screen ID | `S34` |
| Screen name | Contract Detail (Customer) |
| Actor | Customer owner |
| Priority | P1 |
| Belongs to module | [MFG-09](../specs/spec-MFG-09.md) |
| Route | `/contracts/{contract_id}` |
| Mockup image | `img/S34-contract_detail_screen_customer.png` |
| Status | Resolved implementation specification |

## 1. Purpose

**Shown when:** The customer reviews the generated contract and signs only after explicit consent, typed full-name match, recent password reauthentication and a one-time contract-bound challenge. Signing records immutable evidence. All identifiers and permissions come from the server session; list filters are allowlisted and recoverable failures preserve entered values.

**The user leaves this screen when:** An authorized action in section 5 succeeds, the user follows a role-allowed global route, or they return to the validated originating route.

## 2. Mockup

![S34 historical reference](img/S34-contract_detail_screen_customer.png)

Written behavior below takes precedence over obsolete sample content.

## 3. Element inventory

| # | Element | Type | Content / data source | Required | Validation |
|---|---|---|---|---|---|
| 1 | Screen heading | Heading | Contract Detail (Customer) | Yes | Static route title. |
| 2 | Route | Navigation target | /contracts/{contract_id} | Yes | Access checked on server. |
| 3 | contract_id | Field / control | UUID, required | As specified | Customer must own associated order; inaccessible ID returns 404. |
| 4 | pdf_asset_id | Field / control | private UUID | As specified | Authorized expiring download URL (10 minutes); no public asset URL. |
| 5 | consent | Field / control | boolean, required true | As specified | Explicit acceptance of displayed consent text version; checkbox alone does not sign. |
| 6 | consent_text_version | Field / control | version, required | As specified | Persisted with evidence. |
| 7 | typed_full_name | Field / control | string, required | As specified | 1..100; trimmed/casefold match to authenticated profile full_name. |
| 8 | password | Field / control | secret, required at signing | As specified | Reauthenticate; valid within 5 minutes; never logged or stored in evidence. |
| 9 | signing_challenge | Field / control | one-time token, required | As specified | Server binds contract UUID/version/content hash; expires in 10 minutes; single use. |
| 10 | Idempotency-Key | Field / control | UUID, required | As specified | Same key/payload returns signed version; changed payload returns 409. |
| 11 | signature evidence | Field / control | server-generated record | As specified | signer, name, consent version, hash, timestamp, server IP/user-agent, challenge digest. |
| 12 | Request signing challenge | Action | Require explicit consent, typed name and recent password reauth; issue contract-bound 10m one-use challenge. | Available when authorized | Destination: S34 |
| 13 | Sign | Action | Verify challenge/hash/version and transactionally record evidence; order advances to AwaitingPayment. | Available when authorized | Destination: S35 |
| 14 | Download/view PDF | Action | Authorized private URL; no public asset URL. | Available when authorized | Destination: S34 |

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
| 1 | Request signing challenge | Activate | Require explicit consent, typed name and recent password reauth; issue contract-bound 10m one-use challenge. | S34 |
| 2 | Sign | Activate | Verify challenge/hash/version and transactionally record evidence; order advances to AwaitingPayment. | S35 |
| 3 | Download/view PDF | Activate | Authorized private URL; no public asset URL. | S34 |

Home and public catalog are available to Guest and authenticated users. Customer designs and customer orders are Customer-only; profile and notifications require authentication. Company Admin routes: S10, S18, S28, S30, S36, S42 and S43. Sales Consultant routes: S20 and assigned-only S21. System Admin routes: S39, S40 and S41. The server rechecks role, company, membership, ownership and assignment for every route and notification target. Back returns to the validated originating route and preserves list filters; without one, use S26 for Customer, S28 for Company Admin, S20 for Sales Consultant, S41 for System Admin, and S01 for Guest.

## 6. Screen-level rules

| Rule ID | Rule | Source |
|---|---|---|
| SR-001 | Access and ownership are checked server-side; do not trust submitted customer, company, role, price, or provider status. Apply 401/403/404 behavior and the field rules above. | Authorization and data ownership requirements |
| SR-002 | IDs are UUIDs; timestamps are UTC and displayed in Asia/Ho_Chi_Minh; money and quantities are integers. Mutations use expected_version; significant create/sign/pay/batch operations use idempotency keys. | Data representation and concurrency requirements |
| SR-003 | Apply the module lifecycle and validation rules linked below; preserve immutable submitted snapshots. | Module specification |
| SR-004 | Selected product and technical defaults are project implementation decisions; do not invent factual company, author, client-approval, or course identifiers. | Project implementation assumptions |

### Acceptance scenarios

1. Correct consent, typed profile name, recent password and valid contract-bound challenge records evidence once and moves order to AwaitingPayment.
2. Expired/replayed challenge, changed hash/version or missing consent rejects signing; checkbox alone never signs.

## 7. Linked requirements

| FR ID (from the module spec) | What this screen does for it |
|---|---|
| MFG-09/F-CONTR-008 | Implements this screen's validated user flow and the linked source function. |
| MFG-09/F-CONTR-009 | Implements this screen's validated user flow and the linked source function. |
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
