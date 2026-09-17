# Spec Document: Company Accounts


| Field | Value |
| --- | --- |
| Module ID | `MFG-03` |
| Module name | Company Accounts |
| Spec version | v0.1 |
| Author (team member) | [NEEDS CLARIFICATION: Specify the responsible team member; Group B is named only as the team on the Session 1 scope sheet.] |
| Date | 2026-09-16 |
| Status | Draft |
| Approved by (Client role) | [NEEDS CLARIFICATION: Client approver role and approval are not supplied.] |
| DBIZ2 source | Function List `MFG-03`, No. 17-24, `F-ACC-001` .. `F-ACC-008`; Use Cases: Add account; Update account info & role; Delete account; Manage company's user accounts; Use Case IDs: UC-S06, UC-S07, UC-S08, UC-S05; Screens: [NEEDS CLARIFICATION: No matching Screen IDs are supplied.] |


---

## 1. Purpose and scope (mandatory)

System administrators can add, update, and remove company accounts. These functions support central management of company account information and assigned roles.

Source: [docs/function-list.md](../docs/function-list.md), `MFG-03` (No. 17-24); Session 1 MVP PDF, page 1 section 3. [NEEDS CLARIFICATION: Original DBIZ2 Schematic 1.1/1.2 cells are unavailable; the PDF reproduces the project objective but is not Session 3 MVP Scope v3.]

**In scope**

- Add Account
- Update Account
- Delete Account

Session 1 marks Company Accounts as Won't for this MVP; retaining DBIZ2 requirements here does not put them into the release. All DBIZ2 subfunctions below are retained as documentation; this does not authorize release of deferred functions. [NEEDS CLARIFICATION: Supply MVP Scope v3 and Session 3 decisions to confirm current module scope.]

**Out of scope**

- Personal profile editing belongs to MFG-02.

**Depends on**

- [NEEDS CLARIFICATION: No explicit module dependency contract is supplied; confirm dependencies without deriving new requirements from the architecture.]

## 2. Actors (mandatory)

| Actor | Role in this module | Where it comes from |
| --- | --- | --- |
| System Admin | Primary — Add Account, Update Account, Delete Account | Function List `Actor` column, `MFG-03`: F-ACC-001, F-ACC-002, F-ACC-003, F-ACC-004, F-ACC-005, F-ACC-006, F-ACC-007, F-ACC-008 |

Primary identifies the actor performing the listed subfunctions; it does not replace conflicting Use Case or sequence labels. External participants appear in section 4 only when supplied by the source.

## 3. User scenarios and acceptance criteria (mandatory)

[NEEDS CLARIFICATION: P1/P2 scenario ordering is not agreed in the supplied materials; no scenario priority is inferred from Function List High/Medium/Low.]

### US-1 ([NEEDS CLARIFICATION: Scenario priority not agreed.]): Add account

**Journey.** As a `System Admin`, I want to `add account`, so that [NEEDS CLARIFICATION: The Use Case names the goal but does not state a separate scenario benefit.].

Source: `docs/architecture/use-case.md`, line 45, “Add account”; related FRs `FR-001` / `F-ACC-001`, `FR-002` / `F-ACC-002`, `FR-003` / `F-ACC-003`, `FR-004` / `F-ACC-004`. Actor association in the Use Case: [NEEDS CLARIFICATION: no direct actor association shown].

[NEEDS CLARIFICATION: No detailed Usage Flow or sequence for this use case is supplied; the criterion records the named goal and any explicitly cited Function List outcome. Confirm preconditions, action sequence and failure behavior before treating it as an agreed acceptance test.]

**Acceptance scenarios**

1. **Given** the system administrator is managing company user accounts, **When** the administrator adds an account, **Then** the company account is stored and its new_account_record_id and creation_timestamp are returned (F-ACC-004).

### US-2 ([NEEDS CLARIFICATION: Scenario priority not agreed.]): Update account info & role

**Journey.** As a `System Admin`, I want to `update account info & role`, so that [NEEDS CLARIFICATION: The Use Case names the goal but does not state a separate scenario benefit.].

Source: `docs/architecture/use-case.md`, line 46, “Update account info & role”; related FRs `FR-005` / `F-ACC-005`, `FR-006` / `F-ACC-006`. Actor association in the Use Case: [NEEDS CLARIFICATION: no direct actor association shown].

[NEEDS CLARIFICATION: No detailed Usage Flow or sequence for this use case is supplied; the criterion records the named goal and any explicitly cited Function List outcome. Confirm preconditions, action sequence and failure behavior before treating it as an agreed acceptance test.]

**Acceptance scenarios**

1. **Given** the system administrator is managing an existing company account, **When** the administrator updates account information and role, **Then** the account record contains the modified information or assigned role and a change log entry is returned (F-ACC-006).

### US-3 ([NEEDS CLARIFICATION: Scenario priority not agreed.]): Delete account

**Journey.** As a `System Admin`, I want to `delete account`, so that [NEEDS CLARIFICATION: The Use Case names the goal but does not state a separate scenario benefit.].

Source: `docs/architecture/use-case.md`, line 47, “Delete account”; related FRs `FR-007` / `F-ACC-007`, `FR-008` / `F-ACC-008`. Actor association in the Use Case: [NEEDS CLARIFICATION: no direct actor association shown].

[NEEDS CLARIFICATION: No detailed Usage Flow or sequence for this use case is supplied; the criterion records the named goal and any explicitly cited Function List outcome. Confirm preconditions, action sequence and failure behavior before treating it as an agreed acceptance test.]

**Acceptance scenarios**

1. **Given** the system administrator is managing an existing company account, **When** the administrator deletes the account, **Then** the confirmed account is marked deleted or removed (F-ACC-008); [NEEDS CLARIFICATION: Soft deletion versus permanent removal is unresolved; this criterion cannot choose a mode.].

### US-4 ([NEEDS CLARIFICATION: Scenario priority not agreed.]): Manage company's user accounts

**Journey.** As a `System Admin`, I want to `manage company's user accounts`, so that [NEEDS CLARIFICATION: The Use Case names the goal but does not state a separate scenario benefit.].

Source: `docs/architecture/use-case.md`, line 48, “Manage company's user accounts”; related FRs `FR-001` / `F-ACC-001`, `FR-002` / `F-ACC-002`, `FR-003` / `F-ACC-003`, `FR-004` / `F-ACC-004`, `FR-005` / `F-ACC-005`, `FR-006` / `F-ACC-006`, `FR-007` / `F-ACC-007`, `FR-008` / `F-ACC-008`.

[NEEDS CLARIFICATION: No detailed Usage Flow or sequence for this use case is supplied; the criterion records the named goal and any explicitly cited Function List outcome. Confirm preconditions, action sequence and failure behavior before treating it as an agreed acceptance test.]

**Acceptance scenarios**

1. **Given** the system administrator is managing company user accounts, **When** the administrator chooses a related account action, **Then** Add account, Update account info & role or Delete account is entered.

### Edge cases

- [NEEDS CLARIFICATION: Document missing/invalid inputs and empty-data outcomes not already covered by the supplied screens or sequences.]
- [NEEDS CLARIFICATION: Document behavior when a required external service or data operation is unavailable; do not infer retries or fallback paths.]
- [NEEDS CLARIFICATION: Document repeated actions and simultaneous-user outcomes; no concurrency or duplicate-submission rule is supplied.]

## 4. Flows (mandatory)

### 4.1 Usage flow

[NEEDS CLARIFICATION: The supplied overall customer Usage Flow does not show this module; supply the relevant original Mermaid/figure. No flow is invented.]

### 4.2 Sequence for the main flow

[NEEDS CLARIFICATION: No sequence diagram for this module is supplied; participants and messages cannot be reconstructed as requirements.]

## 5. Functional requirements (mandatory)

One FR per original Function List subfunction, in source order. FR IDs are local to this module; cite `MFG-03/FR-nnn` with the unchanged Subfunction ID. Original function names and High/Medium/Low values are preserved in each requirement note. MoSCoW values are used only for capabilities explicitly prioritized on page 2 of the Session 1 PDF; [NEEDS CLARIFICATION: Confirm per-subfunction priority mapping and the current Session 3 release scope.]

| FR ID | DBIZ2 Subfunction ID | Requirement (system MUST ...) | Actor | Priority |
| --- | --- | --- | --- | --- |
| FR-001 | F-ACC-001 | The system MUST display a list of existing subsidiary accounts with search filter capabilities.<br/>DBIZ2 function: Add Account; subfunction: Account List View; category: Screen; original priority: High. | System Admin | [NEEDS CLARIFICATION: Outside MVP (Session 1 Won't); no Must/Should/Could implementation priority is agreed.] |
| FR-002 | F-ACC-002 | The system MUST display an input form to add a new company account or employee.<br/>DBIZ2 function: Add Account; subfunction: Add Account Form; category: Screen; original priority: High. | System Admin | [NEEDS CLARIFICATION: Outside MVP (Session 1 Won't); no Must/Should/Could implementation priority is agreed.] |
| FR-003 | F-ACC-003 | The system MUST automatically generate a temporary password or invitation token for the new account.<br/>DBIZ2 function: Add Account; subfunction: Credential Generation; category: Process; original priority: High. | System Admin | [NEEDS CLARIFICATION: Outside MVP (Session 1 Won't); no Must/Should/Could implementation priority is agreed.] |
| FR-004 | F-ACC-004 | The system MUST store the new company account information into the system database.<br/>DBIZ2 function: Add Account; subfunction: Save Account Logic; category: Process; original priority: High. | System Admin | [NEEDS CLARIFICATION: Outside MVP (Session 1 Won't); no Must/Should/Could implementation priority is agreed.] |
| FR-005 | F-ACC-005 | The system MUST display detailed information of a specific company account for viewing or editing.<br/>DBIZ2 function: Update Account; subfunction: Account Detail View; category: Screen; original priority: Medium. | System Admin | [NEEDS CLARIFICATION: Outside MVP (Session 1 Won't); no Must/Should/Could implementation priority is agreed.] |
| FR-006 | F-ACC-006 | The system MUST update changes regarding the company account information or assigned roles.<br/>DBIZ2 function: Update Account; subfunction: Update Account Logic; category: Process; original priority: Medium. | System Admin | [NEEDS CLARIFICATION: Outside MVP (Session 1 Won't); no Must/Should/Could implementation priority is agreed.] |
| FR-007 | F-ACC-007 | The system MUST display a confirmation prompt and basic info before deleting the account.<br/>DBIZ2 function: Delete Account; subfunction: Confirm Delete UI; category: Screen; original priority: Low. | System Admin | [NEEDS CLARIFICATION: Outside MVP (Session 1 Won't); no Must/Should/Could implementation priority is agreed.] |
| FR-008 | F-ACC-008 | The system MUST perform a soft delete or permanent removal of the account record.<br/>DBIZ2 function: Delete Account; subfunction: Delete Account Logic; category: Process; original priority: Low. | System Admin | [NEEDS CLARIFICATION: Outside MVP (Session 1 Won't); no Must/Should/Could implementation priority is agreed.] |

### 5.1 Input / Output contract

Literal Function List field names, types and required flags are preserved. Input and output rows are separate to avoid inventing field-to-field pairings. The template Required column applies to inputs; output required flags appear in Notes / validation. `—` means that side of this row is not applicable, not that a source field was omitted. Object contents, validation ranges and identifier formats are not inferred. [NEEDS CLARIFICATION: Supply nested Object/JSON/Array schemas and field validation where absent; apparent source type errors remain unchanged until clarified.]

| FR ID | Input field | Type | Required | Output field | Type | Notes / validation |
| --- | --- | --- | --- | --- | --- | --- |
| FR-001 | `filter_criteria` | Object | No | — | — | Function List No. 17, F-ACC-001, Input column. |
| FR-001 | `pagination_index` | Integer | No | — | — | Function List No. 17, F-ACC-001, Input column. |
| FR-001 | — | — | — | `list_of_company_accounts` | Array<Object> | Output required: Yes. Function List No. 17, F-ACC-001, Output column. |
| FR-002 | [NEEDS CLARIFICATION: F-ACC-002 input: no field specified.] | — | [NEEDS CLARIFICATION: F-ACC-002: input required flag unavailable.] | — | — | Function List No. 18, F-ACC-002, Input column |
| FR-002 | — | — | — | `account_creation_form_ui` | [NEEDS CLARIFICATION: F-ACC-002 output account_creation_form_ui: UI representation type.] | Output required: Yes. Function List No. 18, F-ACC-002, Output column. |
| FR-003 | `new_user_email` | String | Yes | — | — | Function List No. 19, F-ACC-003, Input column. |
| FR-003 | `role_id` | String | Yes | — | — | Function List No. 19, F-ACC-003, Input column. |
| FR-003 | — | — | — | `temporary_password_string_invite_url` | URL | Output required: Yes. Function List No. 19, F-ACC-003, Output column. |
| FR-004 | `company_name` | String | Yes | — | — | Function List No. 20, F-ACC-004, Input column. |
| FR-004 | `tax_id` | String | Yes | — | — | Function List No. 20, F-ACC-004, Input column. |
| FR-004 | `address` | String | Yes | — | — | Function List No. 20, F-ACC-004, Input column. |
| FR-004 | `admin_contact_info` | Object | Yes | — | — | Function List No. 20, F-ACC-004, Input column. |
| FR-004 | — | — | — | `new_account_record_id` | Object | Output required: Yes. Function List No. 20, F-ACC-004, Output column. |
| FR-004 | — | — | — | `creation_timestamp` | DateTime | Output required: Yes. Function List No. 20, F-ACC-004, Output column. |
| FR-005 | `company_account_id` | String | Yes | — | — | Function List No. 21, F-ACC-005, Input column. |
| FR-005 | — | — | — | `detailed_account_data_object` | Object | Output required: Yes. Function List No. 21, F-ACC-005, Output column. |
| FR-006 | `account_id` | String | Yes | — | — | Function List No. 22, F-ACC-006, Input column. |
| FR-006 | `modified_fields` | Object | Yes | — | — | Function List No. 22, F-ACC-006, Input column. |
| FR-006 | — | — | — | `updated_record` | Object | Output required: Yes. Function List No. 22, F-ACC-006, Output column. |
| FR-006 | — | — | — | `change_log_entry` | [NEEDS CLARIFICATION: F-ACC-006 output change_log_entry: data type.] | Output required: Yes. Function List No. 22, F-ACC-006, Output column. |
| FR-007 | `account_id_to_be_deleted` | String | Yes | — | — | Function List No. 23, F-ACC-007, Input column. |
| FR-007 | — | — | — | `confirmation_modal` | [NEEDS CLARIFICATION: F-ACC-007 output confirmation_modal: UI representation type.] | Output required: Yes. Function List No. 23, F-ACC-007, Output column. |
| FR-008 | `confirmed_account_id` | String | Yes | — | — | Function List No. 24, F-ACC-008, Input column. |
| FR-008 | — | — | — | `record_marked_as_deleted_removed` | Object | Output required: Yes. Function List No. 24, F-ACC-008, Output column. |

### 5.2 Business rules

| Rule ID | Rule | Why it exists |
| --- | --- | --- |
| BR-001 | Account removal follows confirmation of the selected account. | F-ACC-007 presents confirmation and F-ACC-008 consumes confirmed_account_id; deletion mode is unresolved. Business rationale beyond the stated source is not separately documented. |

## 6. Key entities (mandatory)

| Entity | Attributes (from Input/Output fields) | Relationships |
| --- | --- | --- |
| Company account | `company_name`, `tax_id`, `address`, `admin_contact_info`, `new_account_record_id`, `creation_timestamp`, `company_account_id`, `account_id`, `modified_fields`, `updated_record`, `confirmed_account_id`, `record_marked_as_deleted_removed` | [NEEDS CLARIFICATION: Company account: relationship cardinalities and nested field ownership are not specified in the Input/Output contract.] |
| Account invitation | `new_user_email`, `role_id`, `temporary_password_string_invite_url` | [NEEDS CLARIFICATION: Account invitation: relationship cardinalities and nested field ownership are not specified in the Input/Output contract.] |

Names above group the literal section 5.1 fields for discussion. They do not introduce tables, extra attributes, foreign keys or relationship cardinalities.

## 7. Screens involved

| Screen ID | Screen name | Priority | Screen Spec file |
| --- | --- | --- | --- |
| — | [NEEDS CLARIFICATION: No matching module screen is identified in the Screen List.] | — | — |

Existing descriptive filenames are retained. Business navigation and notification-panel touchpoints are listed as shared boundaries; this module does not acquire their owning requirements. Screen Specs contain pre-existing “module spec unavailable” notes: these are resolved as file-existence issues by this delivery, not as behavioral approvals.

## 8. Success criteria (mandatory)

| SC ID | Criterion | How it is measured |
| --- | --- | --- |
| SC-001 | [NEEDS CLARIFICATION: No agreed measurable user-outcome success criterion is present in the supplied Session 1 scope sheet or DBIZ2 extracts; provide the Session 3 criterion for this module.] | [NEEDS CLARIFICATION: Confirm the user task, observable completion outcome, agreed target and evaluation method; none is supplied.] |

The source states feature priorities and project goals, not agreed outcome thresholds. No timing, conversion, cost-saving or technical-performance target is introduced.

## 9. Assumptions

- Session 1 page 2 states a single admin login is enough at launch when deferring full account/system administration. [NEEDS CLARIFICATION: Confirm whether this documented Session 1 assumption remains valid in Session 3.]

## 10. Open questions

| # | Question | Blocking? | Owner | Status |
| --- | --- | --- | --- | --- |
| 1 | [NEEDS CLARIFICATION: Specify the responsible team member; Group B is named only as the team on the Session 1 scope sheet.] | Unassessed; see final question | Unassigned; see final question | Open |
| 2 | [NEEDS CLARIFICATION: Client approver role and approval are not supplied.] | Unassessed; see final question | Unassigned; see final question | Open |
| 3 | Use Case IDs: UC-S06, UC-S07, UC-S08, UC-S05 | Unassessed; see final question | Unassigned; see final question | Open |
| 4 | [NEEDS CLARIFICATION: No matching Screen IDs are supplied.] | Unassessed; see final question | Unassigned; see final question | Open |
| 5 | [NEEDS CLARIFICATION: Original DBIZ2 Schematic 1.1/1.2 cells are unavailable; the PDF reproduces the project objective but is not Session 3 MVP Scope v3.] | Unassessed; see final question | Unassigned; see final question | Open |
| 6 | [NEEDS CLARIFICATION: Supply MVP Scope v3 and Session 3 decisions to confirm current module scope.] | Unassessed; see final question | Unassigned; see final question | Open |
| 7 | [NEEDS CLARIFICATION: No explicit module dependency contract is supplied; confirm dependencies without deriving new requirements from the architecture.] | Unassessed; see final question | Unassigned; see final question | Open |
| 8 | [NEEDS CLARIFICATION: P1/P2 scenario ordering is not agreed in the supplied materials; no scenario priority is inferred from Function List High/Medium/Low.] | Unassessed; see final question | Unassigned; see final question | Open |
| 9 | [NEEDS CLARIFICATION: Scenario priority not agreed.] | Unassessed; see final question | Unassigned; see final question | Open |
| 10 | [NEEDS CLARIFICATION: The Use Case names the goal but does not state a separate scenario benefit.] | Unassessed; see final question | Unassigned; see final question | Open |
| 11 | [NEEDS CLARIFICATION: no direct actor association shown] | Unassessed; see final question | Unassigned; see final question | Open |
| 12 | [NEEDS CLARIFICATION: No detailed Usage Flow or sequence for this use case is supplied; the criterion records the named goal and any explicitly cited Function List outcome. Confirm preconditions, action sequence and failure behavior before treating it as an agreed acceptance test.] | Unassessed; see final question | Unassigned; see final question | Open |
| 13 | [NEEDS CLARIFICATION: Soft deletion versus permanent removal is unresolved; this criterion cannot choose a mode.] | Unassessed; see final question | Unassigned; see final question | Open |
| 14 | [NEEDS CLARIFICATION: Document missing/invalid inputs and empty-data outcomes not already covered by the supplied screens or sequences.] | Unassessed; see final question | Unassigned; see final question | Open |
| 15 | [NEEDS CLARIFICATION: Document behavior when a required external service or data operation is unavailable; do not infer retries or fallback paths.] | Unassessed; see final question | Unassigned; see final question | Open |
| 16 | [NEEDS CLARIFICATION: Document repeated actions and simultaneous-user outcomes; no concurrency or duplicate-submission rule is supplied.] | Unassessed; see final question | Unassigned; see final question | Open |
| 17 | [NEEDS CLARIFICATION: The supplied overall customer Usage Flow does not show this module; supply the relevant original Mermaid/figure. No flow is invented.] | Unassessed; see final question | Unassigned; see final question | Open |
| 18 | [NEEDS CLARIFICATION: No sequence diagram for this module is supplied; participants and messages cannot be reconstructed as requirements.] | Unassessed; see final question | Unassigned; see final question | Open |
| 19 | [NEEDS CLARIFICATION: Confirm per-subfunction priority mapping and the current Session 3 release scope.] | Unassessed; see final question | Unassigned; see final question | Open |
| 20 | [NEEDS CLARIFICATION: Outside MVP (Session 1 Won't); no Must/Should/Could implementation priority is agreed.] | Unassessed; see final question | Unassigned; see final question | Open |
| 21 | [NEEDS CLARIFICATION: Supply nested Object/JSON/Array schemas and field validation where absent; apparent source type errors remain unchanged until clarified.] | Unassessed; see final question | Unassigned; see final question | Open |
| 22 | [NEEDS CLARIFICATION: F-ACC-002 input: no field specified.] | Unassessed; see final question | Unassigned; see final question | Open |
| 23 | [NEEDS CLARIFICATION: F-ACC-002: input required flag unavailable.] | Unassessed; see final question | Unassigned; see final question | Open |
| 24 | [NEEDS CLARIFICATION: F-ACC-002 output account_creation_form_ui: UI representation type.] | Unassessed; see final question | Unassigned; see final question | Open |
| 25 | [NEEDS CLARIFICATION: F-ACC-006 output change_log_entry: data type.] | Unassessed; see final question | Unassigned; see final question | Open |
| 26 | [NEEDS CLARIFICATION: F-ACC-007 output confirmation_modal: UI representation type.] | Unassessed; see final question | Unassigned; see final question | Open |
| 27 | [NEEDS CLARIFICATION: Company account: relationship cardinalities and nested field ownership are not specified in the Input/Output contract.] | Unassessed; see final question | Unassigned; see final question | Open |
| 28 | [NEEDS CLARIFICATION: Account invitation: relationship cardinalities and nested field ownership are not specified in the Input/Output contract.] | Unassessed; see final question | Unassigned; see final question | Open |
| 29 | [NEEDS CLARIFICATION: No matching module screen is identified in the Screen List.] | Unassessed; see final question | Unassigned; see final question | Open |
| 30 | [NEEDS CLARIFICATION: No agreed measurable user-outcome success criterion is present in the supplied Session 1 scope sheet or DBIZ2 extracts; provide the Session 3 criterion for this module.] | Unassessed; see final question | Unassigned; see final question | Open |
| 31 | [NEEDS CLARIFICATION: Confirm the user task, observable completion outcome, agreed target and evaluation method; none is supplied.] | Unassessed; see final question | Unassigned; see final question | Open |
| 32 | [NEEDS CLARIFICATION: Confirm whether this documented Session 1 assumption remains valid in Session 3.] | Unassessed; see final question | Unassigned; see final question | Open |
| 33 | [NEEDS CLARIFICATION: F-ACC-003 types temporary_password_string_invite_url as URL although the description allows a temporary password; which output shape applies?] | Unassessed; see final question | Unassigned; see final question | Open |
| 34 | [NEEDS CLARIFICATION: F-ACC-004 types new_account_record_id as Object; confirm whether this is an identifier or record.] | Unassessed; see final question | Unassigned; see final question | Open |
| 35 | [NEEDS CLARIFICATION: Does F-ACC-008 soft-delete or permanently remove an account, and what happens to related records?] | Unassessed; see final question | Unassigned; see final question | Open |
| 36 | [NEEDS CLARIFICATION: No company-account screen is identified in the supplied Screen List; provide existing DBIZ2 screen IDs and specs.] | Unassessed; see final question | Unassigned; see final question | Open |
| 37 | [NEEDS CLARIFICATION: No Session 3 Clarify meeting notes are supplied; carry over all unresolved decisions once provided.] | Unassessed; see final question | Unassigned; see final question | Open |
| 38 | [NEEDS CLARIFICATION: Original spreadsheet cells and figure numbers are unavailable; the traceability below uses exact supplied Markdown lines and the PDF page/section instead.] | Unassessed; see final question | Unassigned; see final question | Open |
| 39 | [NEEDS CLARIFICATION: Mermaid rendering has not been verified with a Mermaid renderer; source copying and node/edge checks alone do not establish rendering correctness.] | Unassessed; see final question | Unassigned; see final question | Open |
| 40 | [NEEDS CLARIFICATION: Open-question owners and blocking impacts have not been assigned.] | Unassessed; see final question | Unassigned; see final question | Open |

## 11. Traceability to DBIZ2

| Spec section | DBIZ2 source | Location |
| --- | --- | --- |
| 1. Purpose / scope | Function List module heading and all module rows; objective reproduced in Session 1 scope | `docs/function-list.md`, lines 21-29; `MVP_Score-WeaveLink.docx.pdf`, page 1 section 3 and page 2 section 4 |
| 2. Actors | Function List Actor column | `docs/function-list.md`, lines 22-29 |
| 4.1 Usage flow | Supplied customer usage flow | No module path exists in the supplied customer flow; see section 4.1 |
| 8. Success criteria / 9. Assumptions | Available scope document | `MVP_Score-WeaveLink.docx.pdf`, page 1 sections 1-3 and page 2 section 4; no measurable acceptance target or Session 3 document supplied |
| 3. US-1 | Use Case “Add account” (UC-S06) | `docs/architecture/use-case.md`, line 45 |
| 3. US-2 | Use Case “Update account info & role” (UC-S07) | `docs/architecture/use-case.md`, line 46 |
| 3. US-3 | Use Case “Delete account” (UC-S08) | `docs/architecture/use-case.md`, line 47 |
| 3. US-4 | Use Case “Manage company's user accounts” (UC-S05) | `docs/architecture/use-case.md`, line 48 |
| 4.2 Sequence | No module sequence supplied | `docs/architecture/sequence.md` contains SD-01 through SD-09 only; none documents this module |
| 5 / 5.1 / 6: FR-001 | `MFG-03` / `F-ACC-001` / Add Account; US-1: Add account; US-4: Manage company's user accounts | `docs/function-list.md`, line 22, No. 17; Screens: not mapped in supplied Screen List; sequence: this behavior is not separately shown in a supplied sequence; Usage Flow: this behavior is not separately shown in the supplied usage flow. Diagrams support only the steps actually shown; the full contract remains sourced to the Function List. |
| 5 / 5.1 / 6: FR-002 | `MFG-03` / `F-ACC-002` / Add Account; US-1: Add account; US-4: Manage company's user accounts | `docs/function-list.md`, line 23, No. 18; Screens: not mapped in supplied Screen List; sequence: this behavior is not separately shown in a supplied sequence; Usage Flow: this behavior is not separately shown in the supplied usage flow. Diagrams support only the steps actually shown; the full contract remains sourced to the Function List. |
| 5 / 5.1 / 6: FR-003 | `MFG-03` / `F-ACC-003` / Add Account; US-1: Add account; US-4: Manage company's user accounts | `docs/function-list.md`, line 24, No. 19; Screens: not mapped in supplied Screen List; sequence: this behavior is not separately shown in a supplied sequence; Usage Flow: this behavior is not separately shown in the supplied usage flow. Diagrams support only the steps actually shown; the full contract remains sourced to the Function List. |
| 5 / 5.1 / 6: FR-004 | `MFG-03` / `F-ACC-004` / Add Account; US-1: Add account; US-4: Manage company's user accounts | `docs/function-list.md`, line 25, No. 20; Screens: not mapped in supplied Screen List; sequence: this behavior is not separately shown in a supplied sequence; Usage Flow: this behavior is not separately shown in the supplied usage flow. Diagrams support only the steps actually shown; the full contract remains sourced to the Function List. |
| 5 / 5.1 / 6: FR-005 | `MFG-03` / `F-ACC-005` / Update Account; US-2: Update account info & role; US-4: Manage company's user accounts | `docs/function-list.md`, line 26, No. 21; Screens: not mapped in supplied Screen List; sequence: this behavior is not separately shown in a supplied sequence; Usage Flow: this behavior is not separately shown in the supplied usage flow. Diagrams support only the steps actually shown; the full contract remains sourced to the Function List. |
| 5 / 5.1 / 6: FR-006 | `MFG-03` / `F-ACC-006` / Update Account; US-2: Update account info & role; US-4: Manage company's user accounts | `docs/function-list.md`, line 27, No. 22; Screens: not mapped in supplied Screen List; sequence: this behavior is not separately shown in a supplied sequence; Usage Flow: this behavior is not separately shown in the supplied usage flow. Diagrams support only the steps actually shown; the full contract remains sourced to the Function List. |
| 5 / 5.1 / 6: FR-007 | `MFG-03` / `F-ACC-007` / Delete Account; US-3: Delete account; US-4: Manage company's user accounts | `docs/function-list.md`, line 28, No. 23; Screens: not mapped in supplied Screen List; sequence: this behavior is not separately shown in a supplied sequence; Usage Flow: this behavior is not separately shown in the supplied usage flow. Diagrams support only the steps actually shown; the full contract remains sourced to the Function List. |
| 5 / 5.1 / 6: FR-008 | `MFG-03` / `F-ACC-008` / Delete Account; US-3: Delete account; US-4: Manage company's user accounts | `docs/function-list.md`, line 29, No. 24; Screens: not mapped in supplied Screen List; sequence: this behavior is not separately shown in a supplied sequence; Usage Flow: this behavior is not separately shown in the supplied usage flow. Diagrams support only the steps actually shown; the full contract remains sourced to the Function List. |
| 5.2 BR-001 | Explicit source rule | F-ACC-007 presents confirmation and F-ACC-008 consumes confirmed_account_id; deletion mode is unresolved. |

---

## Completion checklist

Tick every box before you call this spec done.

- [x] Every subfunction of this module in the DBIZ2 Function List appears as an FR row.
- [ ] Every Input and Output field has a type and a required flag.
- [ ] Every Mermaid block renders without an error.
- [ ] Every node and arrow in the Mermaid flow exists in the original DBIZ2 diagram, and nothing
     was invented. (Check this against the picture, line by line.)
- [x] At least one business rule is written that is not visible in any diagram.
- [ ] Every screen this module touches is listed with an existing Screen Spec file.
- [ ] Success criteria contain no technology words.
- [ ] Open questions carry the unresolved items from the Session 3 Clarify meeting.
- [ ] The traceability table points to real cells and figures, not "see the report".

Unchecked items remain unverified or blocked by the clarification items above. The success-criteria box remains open because the agreed criteria themselves are missing.

---

Template source: adapted from GitHub Spec Kit `templates/spec-template.md`

(github.com/github/spec-kit, accessed 09/2026), mapped onto the DBIZ2 Product Design Package.

DBIZ3, VJCBI College - FTU.
