# Screen Spec: S09 Dony Staff CRM Forgot Password

| Field | Value |
| --- | --- |
| Screen ID | `S09` |
| Screen name | Dony Staff CRM Forgot Password |
| Actor | Guest / Dony employee |
| Priority | Must (MVP) |
| Belongs to module | [MFG-01](../specs/spec-MFG-01.md) |
| Route | `/staff/forgot-password` |
| Mockup image | img/S09-01-staff-forgot-password.png |
| Status | Resolved implementation specification |


## 1. Purpose

**Shown when:** A Dony employee requests recovery from the internal CRM login. Keep staff portal branding and omit all customer storefront navigation. Responses must not disclose whether a work email has a staff account; the reset token remains bound to the employee portal.

**The user leaves this screen when:** The neutral request acknowledgement appears, or they return to staff sign-in.

## 2. Mockup

![Dony staff CRM forgot password](img/S09-01-staff-forgot-password.png)

## 3. Element inventory

| # | Element | Type | Content / data source | Required | Validation |
|---|---|---|---|---|---|
| 1 | Staff heading | Heading | Reset your staff password | Yes | Internal CRM brand. |
| 2 | Work email | Field | Email address | Yes | Normalize; do not reveal account existence. |
| 3 | Send reset link | Action | Queue eligible employee-bound reset email | Yes | Max 3 requests per account/IP/hour. |
| 4 | Acknowledgement | Status | Neutral message for known and unknown emails | After submit | Same content and response behavior. |
| 5 | Back to staff sign-in | Link | Internal CRM login | Yes | Destination: S08. |

## 4. States

**Loading, access, errors and retry:** Show a labelled Loading state while reads resolve. A missing or inaccessible route returns a safe 401/403/404 without disclosing protected records. Error states show the API code, message, field_errors and request_id while preserving safe input. Retry transient reads; retry a mutation only with the original idempotency key and identical payload. Preserve safe user input after recoverable failures.

| State | What the user sees | Trigger |
|---|---|---|
| Empty | Render the work-email recovery form; no account data is shown before submission. | Initial route |
| Success | Show the same neutral acknowledgement whether the address exists; queue a time-limited employee reset link only for an eligible account. | Request accepted |
| Conflict | Explain that the recovery token/request is stale or already replaced and offer a safe way to request a new link; do not reveal account existence. | Stale or replaced request |

## 5. Interactions and navigation

| # | Element | User action | System response | Goes to screen |
|---|---|---|---|---|
| 1 | Send reset link | Submit work email | Return neutral response; queue employee-bound token if eligible | S09 acknowledgement |
| 2 | Back to staff sign-in | Activate link | Return to internal CRM login | S08 |

## 6. Screen-level rules

| Rule ID | Rule | Source |
|---|---|---|
| SR-001 | Check access and ownership on the server; never trust submitted customer, company, role, price, stage or provider status. Apply the documented 401/403/404 behavior and field rules. | Project baseline |
| SR-002 | IDs are UUIDs; timestamps are UTC and displayed in Asia/Ho_Chi_Minh; money and quantities are integers. Mutations use expected versions and idempotency keys where specified. | Project baseline |
| SR-003 | Apply the owning module's lifecycle and validation rules; preserve immutable submitted snapshots and design versions. | Project baseline |
| SR-004 | Use documented project assumptions; do not invent factual company, author, client-approval or course identifiers. | Project baseline |

### Acceptance scenarios

1. Staff recovery is visually and behaviorally distinct from Customer S06.
2. Known and unknown emails receive identical acknowledgement.
3. Eligible requests send only employee-bound links to S10.

## 7. Linked requirements

| FR ID (from the module spec) | What this screen does for it |
|---|---|
| MFG-01/F-USER-007 | Render the employee email-only recovery form. |
| MFG-01/F-USER-008 | Validate employee recovery input and request limits without disclosing account existence. |
| MFG-01/F-USER-009 | Issue/reissue and deliver the hashed employee-portal reset token for eligible requests. |

## 8. Responsive and accessibility notes

Support 360px through desktop; use labelled controls, visible focus, readable contrast and accessible status/error announcements.

## 9. Open questions

| # | Question | Blocking? | Status |
|---|---|---|---|
| 1 | No remaining open questions; staff recovery route and neutral response are resolved. | No | Resolved |

## Completion checklist

- [x] Route, actor, module, priority, and mockup are identified.
- [x] Fields, validation, actions and portal boundary are explicit.
- [x] States, navigation and acceptance scenarios are explicit.
- [x] Responsive and accessibility requirements are documented.
- [x] No unresolved screen-level questions remain.
