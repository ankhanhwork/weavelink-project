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

**Shown when:** The customer reviews the generated contract only after approving the received physical sample. The screen shows bound design/sample evidence, buyer organization snapshot when present, contract total, deposit percentage/amount and remaining-balance formula. MVP acknowledgement requires explicit consent and typed full-name match in the active authenticated session; stronger reauthentication/challenge is full-system only.

**MVP authentication level:** Follow the README MVP slice: the already-authenticated Customer gives explicit consent and types their matching full name; the active Customer session is the authentication evidence. MVP does not require password re-entry or a one-time signing challenge. The stronger reauthentication/challenge flow below is post-MVP and must not block MVP contract acknowledgement.

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
| 9 | signing_challenge | Post-MVP field | one-time token | No (MVP) | Full-system flow: server binds contract UUID/version/content hash; expires in 10 minutes; single use. Omit in MVP. |
| 10 | Idempotency-Key | Field / control | UUID, required | As specified | Same key/payload returns signed version; changed payload returns 409. |
| 11 | signature evidence | Server-generated evidence record | signer, name, consent version, contract hash, timestamp, server IP/user-agent | Yes | MVP records active session, matching name and consent; full-system may also record a challenge digest. |
| 12 | Request signing challenge | Post-MVP action | Require explicit consent, typed name and recent password reauth; issue contract-bound 10m one-use challenge. | Post-MVP only | Destination: S34; MVP signing uses the authenticated session, consent and matching typed name only. |
| 13 | Sign | Action | Verify challenge/hash/version/sample binding and transactionally record evidence; order advances to `AwaitingDeposit`. | Available when authorized | Destination: S35 |
| 14 | Download/view PDF | Action | Authorized private URL; no public asset URL. | Available when authorized | Destination: S34 |
| 15 | design_fee_vnd / source_design_request_id | Read-only price line | Integer VND and originating request reference from order snapshot | Yes | Show separately outside merchandise subtotal, including 0 for free/repeat orders; same fee/total as S25/S35 and PDF; no manual surcharge. |
| 16 | approved sample / payment terms | Read-only evidence | design version, sample ID/version, approved_at, deposit percent/amount and balance formula | Yes | Must match current Approved sample and immutable contract; mismatch blocks signing. |

## 4. States

| State | What the user sees | Trigger |
|---|---|---|
| Loading | Load the S34 Contract Detail (Customer) view model and show labelled progress; keep writes disabled until route data and authorization are resolved. | Request starts |
| Empty | Render the defined initial/empty state for S34 Contract Detail (Customer); if a required route object is absent, return a safe 404 and the authorized parent route. | Empty initial form or missing detail payload |
| Forbidden/not found | Return a safe 401/403/404 for S34 Contract Detail (Customer) without revealing inaccessible record, customer, staff or payment details. | 401/403/404 |
| Error | For S34 Contract Detail (Customer), show the API code, message, field_errors and request_id; preserve safe user-entered values. | Request failure |
| Retry | Retry transient reads for S34 Contract Detail (Customer); retry a mutation only with its original idempotency key and identical payload, never as a new side effect. | Recoverable failure |
| Success | Refresh S34 Contract Detail (Customer) from the committed server response, expose only the next role/state-allowed action and announce the result via aria-live. | Mutation commits |
| Conflict | For a stale S34 Contract Detail (Customer) version or lifecycle state, reload authoritative data, explain the conflict and require explicit review before resubmission. | 409 |

## 5. Interactions and navigation

| # | Element | User action | System response | Goes to screen |
|---|---|---|---|---|
| 1 | Request signing challenge | Post-MVP only | Full-system flow; not used for MVP acknowledgement. | S34 |
| 2 | Sign | Activate | Verify challenge/hash/version/sample binding and transactionally record evidence; order advances to `AwaitingDeposit`. | S35 |
| 3 | Download/view PDF | Activate | Authorized private URL; no public asset URL. | S34 |

Home and public catalog are available to Guest and authenticated users. Customer designs and customer orders are Customer-only; profile and notifications require authentication. Sales Admin routes: S10, S18, S28, S30, S36, S42 and S43. Sales routes: S20 and assigned-only S21. System Admin routes: S39, S40 and S41. The server rechecks internal role, customer ownership and staff assignment for every route and notification target. Back returns to the validated originating route and preserves list filters; without one, use S26 for Customer, S28 for Sales Admin, S20 for Sales, S41 for System Admin, and S01 for Guest.

## 6. Screen-level rules

| Rule ID | Rule | Source |
|---|---|---|
| SR-001 | Access and ownership are checked server-side; do not trust submitted customer, company, role, price, or provider status. Apply 401/403/404 behavior and the field rules above. | Authorization and data ownership requirements |
| SR-002 | IDs are UUIDs; timestamps are UTC and displayed in Asia/Ho_Chi_Minh; money and quantities are integers. Mutations use expected_version; significant create/sign/pay/batch operations use idempotency keys. | Data representation and concurrency requirements |
| SR-003 | Apply the module lifecycle and validation rules linked below; preserve immutable submitted snapshots. | Module specification |
| SR-004 | Selected product and technical defaults are project implementation decisions; do not invent factual company, author, client-approval, or course identifiers. | Project implementation assumptions |

### Acceptance scenarios

1. MVP: correct consent, typed account name and active session record acknowledgement once and moves order to `AwaitingDeposit`; full-system additionally requires recent password and valid contract-bound challenge.
2. Missing/invalid session, mismatched name, stale sample/design/hash/version or missing consent rejects MVP acknowledgement; expired/replayed challenge also rejects the full-system path.
3. Contract/PDF displays the snapshotted design fee separately before signing; it never reads current configuration or adds a second charge.

## 7. Linked requirements

| FR ID (from the module spec) | What this screen does for it |
|---|---|
| MFG-09/F-CONTR-008 | UI touchpoint for **Record authenticated contract acknowledgement**; this screen defines the visible action/result, while the module spec owns server authorization, validation and persistence. |
| MFG-09/F-CONTR-009 | UI touchpoint for **Signed Notify Logic**; this screen defines the visible action/result, while the module spec owns server authorization, validation and persistence. |
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
