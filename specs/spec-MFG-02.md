# Spec Document: Profile & Settings


| Field | Value |
| --- | --- |
| Module ID | `MFG-02` |
| Module name | Profile & Settings |
| Spec version | v0.1 |
| Author (team member) | [NEEDS CLARIFICATION: Specify the responsible team member; Group B is named only as the team on the Session 1 scope sheet.] |
| Date | 2026-09-16 |
| Status | Draft |
| Approved by (Client role) | [NEEDS CLARIFICATION: Client approver role and approval are not supplied.] |
| DBIZ2 source | Function List `MFG-02`, No. 12-16, `F-PROF-001` .. `F-PROF-005`; Use Cases: View Profile; Manage profile; Edit Profile; Change password; [NEEDS CLARIFICATION: Use Case IDs are not visible in the supplied table.]; Screens: `S03`, `S06`, `S07`, `S38` |


---

## 1. Purpose and scope (mandatory)

Members can view and update their personal contact information. They can also change their password using their current password.

Source: [docs/function-list.md](../docs/function-list.md), `MFG-02` (No. 12-16); Session 1 MVP PDF, page 1 section 3. [NEEDS CLARIFICATION: Original DBIZ2 Schematic 1.1/1.2 cells are unavailable; the PDF reproduces the project objective but is not Session 3 MVP Scope v3.]

**In scope**

- View Profile
- Edit Profile
- Change Password

No MFG-02 scope or MoSCoW decision appears in the supplied Session 1 MVP table. All DBIZ2 subfunctions below are retained as documentation; this does not authorize release of deferred functions. [NEEDS CLARIFICATION: Supply MVP Scope v3 and Session 3 decisions to confirm current module scope.]

**Out of scope**

- Registration, login and password recovery belong to MFG-01.

**Depends on**

- MFG-01: member account identity; the module consumes `user_id` and the supplied S06 screen links logout to F-USER-006.

## 2. Actors (mandatory)

| Actor | Role in this module | Where it comes from |
| --- | --- | --- |
| Member | Primary — View Profile, Edit Profile, Change Password | Function List `Actor` column, `MFG-02`: F-PROF-001, F-PROF-002, F-PROF-003, F-PROF-004, F-PROF-005 |

Primary identifies the actor performing the listed subfunctions; it does not replace conflicting Use Case or sequence labels. External participants appear in section 4 only when supplied by the source.

## 3. User scenarios and acceptance criteria (mandatory)

[NEEDS CLARIFICATION: P1/P2 scenario ordering is not agreed in the supplied materials; no scenario priority is inferred from Function List High/Medium/Low.]

### US-1 ([NEEDS CLARIFICATION: Scenario priority not agreed.]): View Profile

**Journey.** As a `Member`, I want to `view profile`, so that [NEEDS CLARIFICATION: The Use Case names the goal but does not state a separate scenario benefit.].

Source: `docs/architecture/use-case.md`, line 10, “View Profile”; related FRs `FR-001` / `F-PROF-001`. Actor association in the Use Case: [NEEDS CLARIFICATION: no direct actor association shown].

[NEEDS CLARIFICATION: No detailed Usage Flow or sequence for this use case is supplied; the criterion records the named goal and any explicitly cited Function List outcome. Confirm preconditions, action sequence and failure behavior before treating it as an agreed acceptance test.]

**Acceptance scenarios**

1. **Given** the member is viewing their profile, **When** the member selects View Profile, **Then** their profile is displayed.

### US-2 ([NEEDS CLARIFICATION: Scenario priority not agreed.]): Manage profile

**Journey.** As a `Member`, I want to `manage profile`, so that [NEEDS CLARIFICATION: The Use Case names the goal but does not state a separate scenario benefit.].

Source: `docs/architecture/use-case.md`, line 11, “Manage profile”; related FRs `FR-001` / `F-PROF-001`, `FR-002` / `F-PROF-002`, `FR-003` / `F-PROF-003`, `FR-004` / `F-PROF-004`, `FR-005` / `F-PROF-005`.

[NEEDS CLARIFICATION: No detailed Usage Flow or sequence for this use case is supplied; the criterion records the named goal and any explicitly cited Function List outcome. Confirm preconditions, action sequence and failure behavior before treating it as an agreed acceptance test.]

**Acceptance scenarios**

1. **Given** the member is managing their profile, **When** the member chooses one of the related profile actions, **Then** View Profile, Edit Profile or Change password is entered as identified by the use case.

### US-3 ([NEEDS CLARIFICATION: Scenario priority not agreed.]): Edit Profile

**Journey.** As a `Member`, I want to `edit profile`, so that [NEEDS CLARIFICATION: The Use Case names the goal but does not state a separate scenario benefit.].

Source: `docs/architecture/use-case.md`, line 12, “Edit Profile”; related FRs `FR-002` / `F-PROF-002`, `FR-003` / `F-PROF-003`. Actor association in the Use Case: [NEEDS CLARIFICATION: no direct actor association shown].

[NEEDS CLARIFICATION: No detailed Usage Flow or sequence for this use case is supplied; the criterion records the named goal and any explicitly cited Function List outcome. Confirm preconditions, action sequence and failure behavior before treating it as an agreed acceptance test.]

**Acceptance scenarios**

1. **Given** the member is managing their profile, **When** the member selects Edit Profile, **Then** the editable profile form contains current profile data and submitted changes return database_update_status (F-PROF-002/F-PROF-003); [NEEDS CLARIFICATION: The specific saved/failed display is not documented.].

### US-4 ([NEEDS CLARIFICATION: Scenario priority not agreed.]): Change password

**Journey.** As a `Member`, I want to `change password`, so that [NEEDS CLARIFICATION: The Use Case names the goal but does not state a separate scenario benefit.].

Source: `docs/architecture/use-case.md`, line 13, “Change password”; related FRs `FR-004` / `F-PROF-004`, `FR-005` / `F-PROF-005`. Actor association in the Use Case: [NEEDS CLARIFICATION: no direct actor association shown].

[NEEDS CLARIFICATION: No detailed Usage Flow or sequence for this use case is supplied; the criterion records the named goal and any explicitly cited Function List outcome. Confirm preconditions, action sequence and failure behavior before treating it as an agreed acceptance test.]

**Acceptance scenarios**

1. **Given** the member is managing their profile, **When** the member selects Change password, **Then** the form requests old and new passwords and the old password is validated before saving the encrypted new password (F-PROF-004/F-PROF-005).

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

One FR per original Function List subfunction, in source order. FR IDs are local to this module; cite `MFG-02/FR-nnn` with the unchanged Subfunction ID. Original function names and High/Medium/Low values are preserved in each requirement note. MoSCoW values are used only for capabilities explicitly prioritized on page 2 of the Session 1 PDF; [NEEDS CLARIFICATION: Confirm per-subfunction priority mapping and the current Session 3 release scope.]

| FR ID | DBIZ2 Subfunction ID | Requirement (system MUST ...) | Actor | Priority |
| --- | --- | --- | --- | --- |
| FR-001 | F-PROF-001 | The system MUST retrieve and display the current user's personal profile details.<br/>DBIZ2 function: View Profile; subfunction: Profile View; category: Screen; original priority: Medium. | Member | [NEEDS CLARIFICATION: No agreed Must/Should/Could priority for this subfunction; preserve the original DBIZ2 priority in the source note.] |
| FR-002 | F-PROF-002 | The system MUST display a form allowing the user to modify their personal contact information.<br/>DBIZ2 function: Edit Profile; subfunction: Edit Profile Form; category: Screen; original priority: Medium. | Member | [NEEDS CLARIFICATION: No agreed Must/Should/Could priority for this subfunction; preserve the original DBIZ2 priority in the source note.] |
| FR-003 | F-PROF-003 | The system MUST save the changes made to the user's personal information into the system.<br/>DBIZ2 function: Edit Profile; subfunction: Save Profile Logic; category: Process; original priority: Medium. | Member | [NEEDS CLARIFICATION: No agreed Must/Should/Could priority for this subfunction; preserve the original DBIZ2 priority in the source note.] |
| FR-004 | F-PROF-004 | The system MUST display an interface requiring entry of the old password and the new password.<br/>DBIZ2 function: Change Password; subfunction: Change Password Form; category: Screen; original priority: Low. | Member | [NEEDS CLARIFICATION: No agreed Must/Should/Could priority for this subfunction; preserve the original DBIZ2 priority in the source note.] |
| FR-005 | F-PROF-005 | The system MUST validate the old password and overwrite it with the encrypted new password.<br/>DBIZ2 function: Change Password; subfunction: Save Password Logic; category: Process; original priority: Low. | Member | [NEEDS CLARIFICATION: No agreed Must/Should/Could priority for this subfunction; preserve the original DBIZ2 priority in the source note.] |

### 5.1 Input / Output contract

Literal Function List field names, types and required flags are preserved. Input and output rows are separate to avoid inventing field-to-field pairings. The template Required column applies to inputs; output required flags appear in Notes / validation. `—` means that side of this row is not applicable, not that a source field was omitted. Object contents, validation ranges and identifier formats are not inferred. [NEEDS CLARIFICATION: Supply nested Object/JSON/Array schemas and field validation where absent; apparent source type errors remain unchanged until clarified.]

| FR ID | Input field | Type | Required | Output field | Type | Notes / validation |
| --- | --- | --- | --- | --- | --- | --- |
| FR-001 | `user_id` | UUID | Yes | — | — | Function List No. 12, F-PROF-001, Input column. |
| FR-001 | — | — | — | `user_profile_object` | Object | Output required: Yes. Function List No. 12, F-PROF-001, Output column. |
| FR-002 | `user_id` | String | Yes | — | — | Function List No. 13, F-PROF-002, Input column. |
| FR-002 | `current_profile_data` | Object | Yes | — | — | Function List No. 13, F-PROF-002, Input column. |
| FR-002 | — | — | — | `editable_form_ui_with_pre_filled_data` | [NEEDS CLARIFICATION: F-PROF-002 output editable_form_ui_with_pre_filled_data: UI representation type.] | Output required: Yes. Function List No. 13, F-PROF-002, Output column. |
| FR-003 | `updated_fields` | Object | Yes | — | — | Function List No. 14, F-PROF-003, Input column. |
| FR-003 | `user_id` | String | Yes | — | — | Function List No. 14, F-PROF-003, Input column. |
| FR-003 | — | — | — | `database_update_status` | String | Output required: Yes. Function List No. 14, F-PROF-003, Output column. |
| FR-003 | — | — | — | `success_notification` | [NEEDS CLARIFICATION: F-PROF-003 output success_notification: data type.] | Output required: Yes. Function List No. 14, F-PROF-003, Output column. |
| FR-004 | [NEEDS CLARIFICATION: F-PROF-004 input: no field specified.] | — | [NEEDS CLARIFICATION: F-PROF-004: input required flag unavailable.] | — | — | Function List No. 15, F-PROF-004, Input column |
| FR-004 | — | — | — | `change_password_form_ui` | [NEEDS CLARIFICATION: F-PROF-004 output change_password_form_ui: UI representation type.] | Output required: Yes. Function List No. 15, F-PROF-004, Output column. |
| FR-005 | `old_password` | String | Yes | — | — | Function List No. 16, F-PROF-005, Input column. |
| FR-005 | `new_password` | String | Yes | — | — | Function List No. 16, F-PROF-005, Input column. |
| FR-005 | — | — | — | `password_changed_event` | String | Output required: Yes. Function List No. 16, F-PROF-005, Output column. |
| FR-005 | — | — | — | `success_alert` | [NEEDS CLARIFICATION: F-PROF-005 output success_alert: data type.] | Output required: Yes. Function List No. 16, F-PROF-005, Output column. |

### 5.2 Business rules

| Rule ID | Rule | Why it exists |
| --- | --- | --- |
| BR-001 | Changing a password validates the old password before replacing it with the encrypted new password. | F-PROF-005 explicitly requires old-password validation; no extra strength rule is supplied. Business rationale beyond the stated source is not separately documented. |

## 6. Key entities (mandatory)

| Entity | Attributes (from Input/Output fields) | Relationships |
| --- | --- | --- |
| Profile | `user_id`, `user_profile_object`, `current_profile_data`, `updated_fields` | [NEEDS CLARIFICATION: Profile: relationship cardinalities and nested field ownership are not specified in the Input/Output contract.] |
| Password change | `old_password`, `new_password`, `password_changed_event` | [NEEDS CLARIFICATION: Password change: relationship cardinalities and nested field ownership are not specified in the Input/Output contract.] |

Names above group the literal section 5.1 fields for discussion. They do not introduce tables, extra attributes, foreign keys or relationship cardinalities.

## 7. Screens involved

| Screen ID | Screen name | Priority | Screen Spec file |
| --- | --- | --- | --- |
| S03 | Login Screen — Shared screen / navigation boundary | [NEEDS CLARIFICATION: S03: Screen List provides no agreed Must/Should priority.] | `screens/S03-login_screen.md` ([open](../screens/S03-login_screen.md)) |
| S06 | User Profile Screen — Direct module screen | [NEEDS CLARIFICATION: S06: Screen List provides no agreed Must/Should priority.] | `screens/S06-user_profile_screen.md` ([open](../screens/S06-user_profile_screen.md)) |
| S07 | Change Password Screen — Direct module screen | [NEEDS CLARIFICATION: S07: Screen List provides no agreed Must/Should priority.] | [NEEDS CLARIFICATION: S07: no Screen Spec file supplied; do not invent a screen-spec filename.] |
| S38 | Notification Panel Screen — Shared screen / navigation boundary | [NEEDS CLARIFICATION: S38: Screen List provides no agreed Must/Should priority.] | [NEEDS CLARIFICATION: S38: no Screen Spec file supplied; do not invent a screen-spec filename.] |

Existing descriptive filenames are retained. Business navigation and notification-panel touchpoints are listed as shared boundaries; this module does not acquire their owning requirements. Screen Specs contain pre-existing “module spec unavailable” notes: these are resolved as file-existence issues by this delivery, not as behavioral approvals.

## 8. Success criteria (mandatory)

| SC ID | Criterion | How it is measured |
| --- | --- | --- |
| SC-001 | [NEEDS CLARIFICATION: No agreed measurable user-outcome success criterion is present in the supplied Session 1 scope sheet or DBIZ2 extracts; provide the Session 3 criterion for this module.] | [NEEDS CLARIFICATION: Confirm the user task, observable completion outcome, agreed target and evaluation method; none is supplied.] |

The source states feature priorities and project goals, not agreed outcome thresholds. No timing, conversion, cost-saving or technical-performance target is introduced.

## 9. Assumptions

- No separate module assumption is explicitly documented in the supplied sources. No assumption has been added to fill missing requirements.

## 10. Open questions

| # | Question | Blocking? | Owner | Status |
| --- | --- | --- | --- | --- |
| 1 | [NEEDS CLARIFICATION: Specify the responsible team member; Group B is named only as the team on the Session 1 scope sheet.] | Unassessed; see final question | Unassigned; see final question | Open |
| 2 | [NEEDS CLARIFICATION: Client approver role and approval are not supplied.] | Unassessed; see final question | Unassigned; see final question | Open |
| 3 | [NEEDS CLARIFICATION: Use Case IDs are not visible in the supplied table.] | Unassessed; see final question | Unassigned; see final question | Open |
| 4 | [NEEDS CLARIFICATION: Original DBIZ2 Schematic 1.1/1.2 cells are unavailable; the PDF reproduces the project objective but is not Session 3 MVP Scope v3.] | Unassessed; see final question | Unassigned; see final question | Open |
| 5 | [NEEDS CLARIFICATION: Supply MVP Scope v3 and Session 3 decisions to confirm current module scope.] | Unassessed; see final question | Unassigned; see final question | Open |
| 6 | [NEEDS CLARIFICATION: P1/P2 scenario ordering is not agreed in the supplied materials; no scenario priority is inferred from Function List High/Medium/Low.] | Unassessed; see final question | Unassigned; see final question | Open |
| 7 | [NEEDS CLARIFICATION: Scenario priority not agreed.] | Unassessed; see final question | Unassigned; see final question | Open |
| 8 | [NEEDS CLARIFICATION: The Use Case names the goal but does not state a separate scenario benefit.] | Unassessed; see final question | Unassigned; see final question | Open |
| 9 | [NEEDS CLARIFICATION: no direct actor association shown] | Unassessed; see final question | Unassigned; see final question | Open |
| 10 | [NEEDS CLARIFICATION: No detailed Usage Flow or sequence for this use case is supplied; the criterion records the named goal and any explicitly cited Function List outcome. Confirm preconditions, action sequence and failure behavior before treating it as an agreed acceptance test.] | Unassessed; see final question | Unassigned; see final question | Open |
| 11 | [NEEDS CLARIFICATION: The specific saved/failed display is not documented.] | Unassessed; see final question | Unassigned; see final question | Open |
| 12 | [NEEDS CLARIFICATION: Document missing/invalid inputs and empty-data outcomes not already covered by the supplied screens or sequences.] | Unassessed; see final question | Unassigned; see final question | Open |
| 13 | [NEEDS CLARIFICATION: Document behavior when a required external service or data operation is unavailable; do not infer retries or fallback paths.] | Unassessed; see final question | Unassigned; see final question | Open |
| 14 | [NEEDS CLARIFICATION: Document repeated actions and simultaneous-user outcomes; no concurrency or duplicate-submission rule is supplied.] | Unassessed; see final question | Unassigned; see final question | Open |
| 15 | [NEEDS CLARIFICATION: The supplied overall customer Usage Flow does not show this module; supply the relevant original Mermaid/figure. No flow is invented.] | Unassessed; see final question | Unassigned; see final question | Open |
| 16 | [NEEDS CLARIFICATION: No sequence diagram for this module is supplied; participants and messages cannot be reconstructed as requirements.] | Unassessed; see final question | Unassigned; see final question | Open |
| 17 | [NEEDS CLARIFICATION: Confirm per-subfunction priority mapping and the current Session 3 release scope.] | Unassessed; see final question | Unassigned; see final question | Open |
| 18 | [NEEDS CLARIFICATION: No agreed Must/Should/Could priority for this subfunction; preserve the original DBIZ2 priority in the source note.] | Unassessed; see final question | Unassigned; see final question | Open |
| 19 | [NEEDS CLARIFICATION: Supply nested Object/JSON/Array schemas and field validation where absent; apparent source type errors remain unchanged until clarified.] | Unassessed; see final question | Unassigned; see final question | Open |
| 20 | [NEEDS CLARIFICATION: F-PROF-002 output editable_form_ui_with_pre_filled_data: UI representation type.] | Unassessed; see final question | Unassigned; see final question | Open |
| 21 | [NEEDS CLARIFICATION: F-PROF-003 output success_notification: data type.] | Unassessed; see final question | Unassigned; see final question | Open |
| 22 | [NEEDS CLARIFICATION: F-PROF-004 input: no field specified.] | Unassessed; see final question | Unassigned; see final question | Open |
| 23 | [NEEDS CLARIFICATION: F-PROF-004: input required flag unavailable.] | Unassessed; see final question | Unassigned; see final question | Open |
| 24 | [NEEDS CLARIFICATION: F-PROF-004 output change_password_form_ui: UI representation type.] | Unassessed; see final question | Unassigned; see final question | Open |
| 25 | [NEEDS CLARIFICATION: F-PROF-005 output success_alert: data type.] | Unassessed; see final question | Unassigned; see final question | Open |
| 26 | [NEEDS CLARIFICATION: Profile: relationship cardinalities and nested field ownership are not specified in the Input/Output contract.] | Unassessed; see final question | Unassigned; see final question | Open |
| 27 | [NEEDS CLARIFICATION: Password change: relationship cardinalities and nested field ownership are not specified in the Input/Output contract.] | Unassessed; see final question | Unassigned; see final question | Open |
| 28 | [NEEDS CLARIFICATION: S03: Screen List provides no agreed Must/Should priority.] | Unassessed; see final question | Unassigned; see final question | Open |
| 29 | [NEEDS CLARIFICATION: S06: Screen List provides no agreed Must/Should priority.] | Unassessed; see final question | Unassigned; see final question | Open |
| 30 | [NEEDS CLARIFICATION: S07: Screen List provides no agreed Must/Should priority.] | Unassessed; see final question | Unassigned; see final question | Open |
| 31 | [NEEDS CLARIFICATION: S07: no Screen Spec file supplied; do not invent a screen-spec filename.] | Unassessed; see final question | Unassigned; see final question | Open |
| 32 | [NEEDS CLARIFICATION: S38: Screen List provides no agreed Must/Should priority.] | Unassessed; see final question | Unassigned; see final question | Open |
| 33 | [NEEDS CLARIFICATION: S38: no Screen Spec file supplied; do not invent a screen-spec filename.] | Unassessed; see final question | Unassigned; see final question | Open |
| 34 | [NEEDS CLARIFICATION: No agreed measurable user-outcome success criterion is present in the supplied Session 1 scope sheet or DBIZ2 extracts; provide the Session 3 criterion for this module.] | Unassessed; see final question | Unassigned; see final question | Open |
| 35 | [NEEDS CLARIFICATION: Confirm the user task, observable completion outcome, agreed target and evaluation method; none is supplied.] | Unassessed; see final question | Unassigned; see final question | Open |
| 36 | [NEEDS CLARIFICATION: F-PROF-001 types user_id as UUID while F-PROF-002/F-PROF-003 type it as String; confirm the shared identifier type.] | Unassessed; see final question | Unassigned; see final question | Open |
| 37 | [NEEDS CLARIFICATION: What editable fields are contained in current_profile_data and updated_fields, and how are S06 fields represented?] | Unassessed; see final question | Unassigned; see final question | Open |
| 38 | [NEEDS CLARIFICATION: S03, [NEEDS CLARIFICATION: Must / Should / Could not given in Screen List]: Must / Should / Could not given in Screen List] Source: `screens/S03-login_screen.md`, line 16. | Unassessed; see final question | Unassigned; see final question | Open |
| 39 | [NEEDS CLARIFICATION: S03, **The user leaves this screen when:** [NEEDS CLARIFICATION: all exit paths are not specifi: all exit paths are not specified; documented interactions appear in section 5.] Source: `screens/S03-login_screen.md`, line 25. | Unassessed; see final question | Unassigned; see final question | Open |
| 40 | [NEEDS CLARIFICATION: S03, Email or phone input: screenshot accepts email or phone, F-USER-005 names username_email] Source: `screens/S03-login_screen.md`, line 46. | Unassessed; see final question | Unassigned; see final question | Open |
| 41 | [NEEDS CLARIFICATION: S03, Email or phone input: validation rule not specified] Source: `screens/S03-login_screen.md`, line 46. | Unassessed; see final question | Unassigned; see final question | Open |
| 42 | [NEEDS CLARIFICATION: S03, Password input: validation rule not specified] Source: `screens/S03-login_screen.md`, line 48. | Unassessed; see final question | Unassigned; see final question | Open |
| 43 | [NEEDS CLARIFICATION: S03, Blank credentials as shown; submit availability [NEEDS CLARIFICATION].: Unspecified requirement; inspect the cited source row.] Source: `screens/S03-login_screen.md`, line 63. | Unassessed; see final question | Unassigned; see final question | Open |
| 44 | [NEEDS CLARIFICATION: S03, [NEEDS CLARIFICATION: authentication loading treatment]: authentication loading treatment] Source: `screens/S03-login_screen.md`, line 64. | Unassessed; see final question | Unassigned; see final question | Open |
| 45 | [NEEDS CLARIFICATION: S03, [NEEDS CLARIFICATION: invalid credential display]: invalid credential display] Source: `screens/S03-login_screen.md`, line 65. | Unassessed; see final question | Unassigned; see final question | Open |
| 46 | [NEEDS CLARIFICATION: S03, Authenticated session; destination determined by redirect_url [NEEDS CLARIFICATION].: Unspecified requirement; inspect the cited source row.] Source: `screens/S03-login_screen.md`, line 66. | Unassessed; see final question | Unassigned; see final question | Open |
| 47 | [NEEDS CLARIFICATION: S03, Sign In submit button: Unspecified requirement; inspect the cited source row.] Source: `screens/S03-login_screen.md`, line 75. | Unassessed; see final question | Unassigned; see final question | Open |
| 48 | [NEEDS CLARIFICATION: S03, Google sign-in: social sign-in behavior] Source: `screens/S03-login_screen.md`, line 76. | Unassessed; see final question | Unassigned; see final question | Open |
| 49 | [NEEDS CLARIFICATION: S03, Apple sign-in: social sign-in behavior] Source: `screens/S03-login_screen.md`, line 77. | Unassessed; see final question | Unassigned; see final question | Open |
| 50 | [NEEDS CLARIFICATION: S03, Facebook sign-in: social sign-in behavior] Source: `screens/S03-login_screen.md`, line 78. | Unassessed; see final question | Unassigned; see final question | Open |
| 51 | [NEEDS CLARIFICATION: S03, [NEEDS CLARIFICATION: no additional screen-level rule documented]: no additional screen-level rule documented] Source: `screens/S03-login_screen.md`, line 85. | Unassessed; see final question | Unassigned; see final question | Open |
| 52 | [NEEDS CLARIFICATION: S03, - Smallest supported width: [NEEDS CLARIFICATION: not specified in sources.]: not specified in sources.] Source: `screens/S03-login_screen.md`, line 96. | Unassessed; see final question | Unassigned; see final question | Open |
| 53 | [NEEDS CLARIFICATION: S03, - What collapses or stacks on a narrow screen: [NEEDS CLARIFICATION: no narrow-screen mock: no narrow-screen mockup or rule provided.] Source: `screens/S03-login_screen.md`, line 98. | Unassessed; see final question | Unassigned; see final question | Open |
| 54 | [NEEDS CLARIFICATION: S03, - Text that must remain readable (contrast, minimum size): [NEEDS CLARIFICATION: no numeri: no numeric accessibility criteria provided.] Source: `screens/S03-login_screen.md`, line 100. | Unassessed; see final question | Unassigned; see final question | Open |
| 55 | [NEEDS CLARIFICATION: S03, [NEEDS CLARIFICATION: Screen List does not provide Must / Should / Could priority.]: Screen List does not provide Must / Should / Could priority.] Source: `screens/S03-login_screen.md`, line 106. | Unassessed; see final question | Unassigned; see final question | Open |
| 56 | [NEEDS CLARIFICATION: S03, [NEEDS CLARIFICATION: smallest supported width, narrow layout, and accessibility minimums are not specified.]: smallest supported width, narrow layout, and accessibility minimums are not specified.] Source: `screens/S03-login_screen.md`, line 108. | Unassessed; see final question | Unassigned; see final question | Open |
| 57 | [NEEDS CLARIFICATION: S03, [NEEDS CLARIFICATION: Can users log in by phone, given function list names username_email?]: Can users log in by phone, given function list names username_email?] Source: `screens/S03-login_screen.md`, line 109. | Unassessed; see final question | Unassigned; see final question | Open |
| 58 | [NEEDS CLARIFICATION: S03, [NEEDS CLARIFICATION: Where does a successful login navigate?]: Where does a successful login navigate?] Source: `screens/S03-login_screen.md`, line 110. | Unassessed; see final question | Unassigned; see final question | Open |
| 59 | [NEEDS CLARIFICATION: S03, [NEEDS CLARIFICATION: mockup file uses a descriptive suffix; template assumes img/<SCREEN-ID>.png.]: mockup file uses a descriptive suffix; template assumes img/<SCREEN-ID>.png.] Source: `screens/S03-login_screen.md`, line 111. | Unassessed; see final question | Unassigned; see final question | Open |
| 60 | [NEEDS CLARIFICATION: S03, - [ ] The mockup is a separate cropped image file, named with the Screen ID. [NEEDS CLARIF: actual image filenames include descriptive suffixes.] Source: `screens/S03-login_screen.md`, line 117. | Unassessed; see final question | Unassigned; see final question | Open |
| 61 | [NEEDS CLARIFICATION: S06, [NEEDS CLARIFICATION: Must / Should / Could not given in Screen List]: Must / Should / Could not given in Screen List] Source: `screens/S06-user_profile_screen.md`, line 16. | Unassessed; see final question | Unassigned; see final question | Open |
| 62 | [NEEDS CLARIFICATION: S06, **The user leaves this screen when:** [NEEDS CLARIFICATION: all exit paths are not specifi: all exit paths are not specified; documented interactions appear in section 5.] Source: `screens/S06-user_profile_screen.md`, line 25. | Unassessed; see final question | Unassigned; see final question | Open |
| 63 | [NEEDS CLARIFICATION: S06, Display name input: field name not defined in F-PROF-002] Source: `screens/S06-user_profile_screen.md`, line 61. | Unassessed; see final question | Unassigned; see final question | Open |
| 64 | [NEEDS CLARIFICATION: S06, Display name input: Unspecified requirement; inspect the cited source row.] Source: `screens/S06-user_profile_screen.md`, line 61. | Unassessed; see final question | Unassigned; see final question | Open |
| 65 | [NEEDS CLARIFICATION: S06, Display name input: validation rule not specified] Source: `screens/S06-user_profile_screen.md`, line 61. | Unassessed; see final question | Unassigned; see final question | Open |
| 66 | [NEEDS CLARIFICATION: S06, Real name input: field name not defined] Source: `screens/S06-user_profile_screen.md`, line 63. | Unassessed; see final question | Unassigned; see final question | Open |
| 67 | [NEEDS CLARIFICATION: S06, Real name input: Unspecified requirement; inspect the cited source row.] Source: `screens/S06-user_profile_screen.md`, line 63. | Unassessed; see final question | Unassigned; see final question | Open |
| 68 | [NEEDS CLARIFICATION: S06, Real name input: validation rule not specified] Source: `screens/S06-user_profile_screen.md`, line 63. | Unassessed; see final question | Unassigned; see final question | Open |
| 69 | [NEEDS CLARIFICATION: S06, Phone input: field name not defined] Source: `screens/S06-user_profile_screen.md`, line 65. | Unassessed; see final question | Unassigned; see final question | Open |
| 70 | [NEEDS CLARIFICATION: S06, Phone input: Unspecified requirement; inspect the cited source row.] Source: `screens/S06-user_profile_screen.md`, line 65. | Unassessed; see final question | Unassigned; see final question | Open |
| 71 | [NEEDS CLARIFICATION: S06, Phone input: validation rule not specified] Source: `screens/S06-user_profile_screen.md`, line 65. | Unassessed; see final question | Unassigned; see final question | Open |
| 72 | [NEEDS CLARIFICATION: S06, Email input: field name not defined] Source: `screens/S06-user_profile_screen.md`, line 67. | Unassessed; see final question | Unassigned; see final question | Open |
| 73 | [NEEDS CLARIFICATION: S06, Email input: Unspecified requirement; inspect the cited source row.] Source: `screens/S06-user_profile_screen.md`, line 67. | Unassessed; see final question | Unassigned; see final question | Open |
| 74 | [NEEDS CLARIFICATION: S06, Email input: validation rule not specified] Source: `screens/S06-user_profile_screen.md`, line 67. | Unassessed; see final question | Unassigned; see final question | Open |
| 75 | [NEEDS CLARIFICATION: S06, Company name input: field name not defined] Source: `screens/S06-user_profile_screen.md`, line 69. | Unassessed; see final question | Unassigned; see final question | Open |
| 76 | [NEEDS CLARIFICATION: S06, Company name input: validation rule not specified] Source: `screens/S06-user_profile_screen.md`, line 69. | Unassessed; see final question | Unassigned; see final question | Open |
| 77 | [NEEDS CLARIFICATION: S06, [NEEDS CLARIFICATION: behavior when profile data is missing]: behavior when profile data is missing] Source: `screens/S06-user_profile_screen.md`, line 103. | Unassessed; see final question | Unassigned; see final question | Open |
| 78 | [NEEDS CLARIFICATION: S06, [NEEDS CLARIFICATION: loading treatment for user_profile_object]: loading treatment for user_profile_object] Source: `screens/S06-user_profile_screen.md`, line 104. | Unassessed; see final question | Unassigned; see final question | Open |
| 79 | [NEEDS CLARIFICATION: S06, [NEEDS CLARIFICATION: save or load error treatment]: save or load error treatment] Source: `screens/S06-user_profile_screen.md`, line 105. | Unassessed; see final question | Unassigned; see final question | Open |
| 80 | [NEEDS CLARIFICATION: S06, F-PROF-003 provides success_notification; placement [NEEDS CLARIFICATION].: Unspecified requirement; inspect the cited source row.] Source: `screens/S06-user_profile_screen.md`, line 106. | Unassessed; see final question | Unassigned; see final question | Open |
| 81 | [NEEDS CLARIFICATION: S06, About Dony navigation: destination not in Screen List] Source: `screens/S06-user_profile_screen.md`, line 114. | Unassessed; see final question | Unassigned; see final question | Open |
| 82 | [NEEDS CLARIFICATION: S06, Contact Us navigation: destination not in Screen List] Source: `screens/S06-user_profile_screen.md`, line 117. | Unassessed; see final question | Unassigned; see final question | Open |
| 83 | [NEEDS CLARIFICATION: S06, Login and Security sidebar item: whether opens S07 or a different screen] Source: `screens/S06-user_profile_screen.md`, line 122. | Unassessed; see final question | Unassigned; see final question | Open |
| 84 | [NEEDS CLARIFICATION: S06, Language sidebar item: language screen/behavior] Source: `screens/S06-user_profile_screen.md`, line 123. | Unassessed; see final question | Unassigned; see final question | Open |
| 85 | [NEEDS CLARIFICATION: S06, Update profile button: Unspecified requirement; inspect the cited source row.] Source: `screens/S06-user_profile_screen.md`, line 130. | Unassessed; see final question | Unassigned; see final question | Open |
| 86 | [NEEDS CLARIFICATION: S06, Cancel button: discard or navigation behavior] Source: `screens/S06-user_profile_screen.md`, line 131. | Unassessed; see final question | Unassigned; see final question | Open |
| 87 | [NEEDS CLARIFICATION: S06, Zalo contact button: contact destination] Source: `screens/S06-user_profile_screen.md`, line 132. | Unassessed; see final question | Unassigned; see final question | Open |
| 88 | [NEEDS CLARIFICATION: S06, Telephone contact button: dial behavior] Source: `screens/S06-user_profile_screen.md`, line 133. | Unassessed; see final question | Unassigned; see final question | Open |
| 89 | [NEEDS CLARIFICATION: S06, Footer Facebook icon: external or in-system destination] Source: `screens/S06-user_profile_screen.md`, line 134. | Unassessed; see final question | Unassigned; see final question | Open |
| 90 | [NEEDS CLARIFICATION: S06, Footer X icon: external or in-system destination] Source: `screens/S06-user_profile_screen.md`, line 135. | Unassessed; see final question | Unassigned; see final question | Open |
| 91 | [NEEDS CLARIFICATION: S06, Footer LinkedIn icon: external or in-system destination] Source: `screens/S06-user_profile_screen.md`, line 136. | Unassessed; see final question | Unassigned; see final question | Open |
| 92 | [NEEDS CLARIFICATION: S06, Footer YouTube icon: external or in-system destination] Source: `screens/S06-user_profile_screen.md`, line 137. | Unassessed; see final question | Unassigned; see final question | Open |
| 93 | [NEEDS CLARIFICATION: S06, Footer TikTok icon: external or in-system destination] Source: `screens/S06-user_profile_screen.md`, line 138. | Unassessed; see final question | Unassigned; see final question | Open |
| 94 | [NEEDS CLARIFICATION: S06, Company profile link: external or in-system destination] Source: `screens/S06-user_profile_screen.md`, line 139. | Unassessed; see final question | Unassigned; see final question | Open |
| 95 | [NEEDS CLARIFICATION: S06, Quality policy link: external or in-system destination] Source: `screens/S06-user_profile_screen.md`, line 140. | Unassessed; see final question | Unassigned; see final question | Open |
| 96 | [NEEDS CLARIFICATION: S06, Warranty policy link: external or in-system destination] Source: `screens/S06-user_profile_screen.md`, line 141. | Unassessed; see final question | Unassigned; see final question | Open |
| 97 | [NEEDS CLARIFICATION: S06, Delivery and return policy link: external or in-system destination] Source: `screens/S06-user_profile_screen.md`, line 142. | Unassessed; see final question | Unassigned; see final question | Open |
| 98 | [NEEDS CLARIFICATION: S06, Second warranty policy link: external or in-system destination] Source: `screens/S06-user_profile_screen.md`, line 143. | Unassessed; see final question | Unassigned; see final question | Open |
| 99 | [NEEDS CLARIFICATION: S06, Shipping policy link: external or in-system destination] Source: `screens/S06-user_profile_screen.md`, line 144. | Unassessed; see final question | Unassigned; see final question | Open |
| 100 | [NEEDS CLARIFICATION: S06, Payment methods link: external or in-system destination] Source: `screens/S06-user_profile_screen.md`, line 145. | Unassessed; see final question | Unassigned; see final question | Open |
| 101 | [NEEDS CLARIFICATION: S06, Business areas link: external or in-system destination] Source: `screens/S06-user_profile_screen.md`, line 146. | Unassessed; see final question | Unassigned; see final question | Open |
| 102 | [NEEDS CLARIFICATION: S06, FAQ link: external or in-system destination] Source: `screens/S06-user_profile_screen.md`, line 147. | Unassessed; see final question | Unassigned; see final question | Open |
| 103 | [NEEDS CLARIFICATION: S06, - Smallest supported width: [NEEDS CLARIFICATION: not specified in sources.]: not specified in sources.] Source: `screens/S06-user_profile_screen.md`, line 166. | Unassessed; see final question | Unassigned; see final question | Open |
| 104 | [NEEDS CLARIFICATION: S06, - What collapses or stacks on a narrow screen: [NEEDS CLARIFICATION: no narrow-screen mock: no narrow-screen mockup or rule provided.] Source: `screens/S06-user_profile_screen.md`, line 168. | Unassessed; see final question | Unassigned; see final question | Open |
| 105 | [NEEDS CLARIFICATION: S06, - Text that must remain readable (contrast, minimum size): [NEEDS CLARIFICATION: no numeri: no numeric accessibility criteria provided.] Source: `screens/S06-user_profile_screen.md`, line 170. | Unassessed; see final question | Unassigned; see final question | Open |
| 106 | [NEEDS CLARIFICATION: S06, [NEEDS CLARIFICATION: Screen List does not provide Must / Should / Could priority.]: Screen List does not provide Must / Should / Could priority.] Source: `screens/S06-user_profile_screen.md`, line 176. | Unassessed; see final question | Unassigned; see final question | Open |
| 107 | [NEEDS CLARIFICATION: S06, [NEEDS CLARIFICATION: smallest supported width, narrow layout, and accessibility minimums are not specified.]: smallest supported width, narrow layout, and accessibility minimums are not specified.] Source: `screens/S06-user_profile_screen.md`, line 178. | Unassessed; see final question | Unassigned; see final question | Open |
| 108 | [NEEDS CLARIFICATION: S06, [NEEDS CLARIFICATION: Screen Overview mentions assigned roles, but none are visible in the mockup. Where are roles displayed?]: Screen Overview mentions assigned roles, but none are visible in the mockup. Where are roles displayed?] Source: `screens/S06-user_profile_screen.md`, line 179. | Unassessed; see final question | Unassigned; see final question | Open |
| 109 | [NEEDS CLARIFICATION: S06, [NEEDS CLARIFICATION: mockup file uses a descriptive suffix; template assumes img/<SCREEN-ID>.png.]: mockup file uses a descriptive suffix; template assumes img/<SCREEN-ID>.png.] Source: `screens/S06-user_profile_screen.md`, line 180. | Unassessed; see final question | Unassigned; see final question | Open |
| 110 | [NEEDS CLARIFICATION: S06, - [ ] The mockup is a separate cropped image file, named with the Screen ID. [NEEDS CLARIF: actual image filenames include descriptive suffixes.] Source: `screens/S06-user_profile_screen.md`, line 186. | Unassessed; see final question | Unassigned; see final question | Open |
| 111 | [NEEDS CLARIFICATION: No Session 3 Clarify meeting notes are supplied; carry over all unresolved decisions once provided.] | Unassessed; see final question | Unassigned; see final question | Open |
| 112 | [NEEDS CLARIFICATION: Original spreadsheet cells and figure numbers are unavailable; the traceability below uses exact supplied Markdown lines and the PDF page/section instead.] | Unassessed; see final question | Unassigned; see final question | Open |
| 113 | [NEEDS CLARIFICATION: Mermaid rendering has not been verified with a Mermaid renderer; source copying and node/edge checks alone do not establish rendering correctness.] | Unassessed; see final question | Unassigned; see final question | Open |
| 114 | [NEEDS CLARIFICATION: Open-question owners and blocking impacts have not been assigned.] | Unassessed; see final question | Unassigned; see final question | Open |

## 11. Traceability to DBIZ2

| Spec section | DBIZ2 source | Location |
| --- | --- | --- |
| 1. Purpose / scope | Function List module heading and all module rows; objective reproduced in Session 1 scope | `docs/function-list.md`, lines 15-20; `MVP_Score-WeaveLink.docx.pdf`, page 1 section 3 and page 2 section 4 |
| 2. Actors | Function List Actor column | `docs/function-list.md`, lines 16-20 |
| 4.1 Usage flow | Supplied customer usage flow | No module path exists in the supplied customer flow; see section 4.1 |
| 8. Success criteria / 9. Assumptions | Available scope document | `MVP_Score-WeaveLink.docx.pdf`, page 1 sections 1-3 and page 2 section 4; no measurable acceptance target or Session 3 document supplied |
| 3. US-1 | Use Case “View Profile” (original ID unavailable) | `docs/architecture/use-case.md`, line 10 |
| 3. US-2 | Use Case “Manage profile” (original ID unavailable) | `docs/architecture/use-case.md`, line 11 |
| 3. US-3 | Use Case “Edit Profile” (original ID unavailable) | `docs/architecture/use-case.md`, line 12 |
| 3. US-4 | Use Case “Change password” (original ID unavailable) | `docs/architecture/use-case.md`, line 13 |
| 4.2 Sequence | No module sequence supplied | `docs/architecture/sequence.md` contains SD-01 through SD-09 only; none documents this module |
| 5 / 5.1 / 6: FR-001 | `MFG-02` / `F-PROF-001` / View Profile; US-1: View Profile; US-2: Manage profile | `docs/function-list.md`, line 16, No. 12; Screens: S06; sequence: this behavior is not separately shown in a supplied sequence; Usage Flow: this behavior is not separately shown in the supplied usage flow. Diagrams support only the steps actually shown; the full contract remains sourced to the Function List. |
| 5 / 5.1 / 6: FR-002 | `MFG-02` / `F-PROF-002` / Edit Profile; US-2: Manage profile; US-3: Edit Profile | `docs/function-list.md`, line 17, No. 13; Screens: S06; sequence: this behavior is not separately shown in a supplied sequence; Usage Flow: this behavior is not separately shown in the supplied usage flow. Diagrams support only the steps actually shown; the full contract remains sourced to the Function List. |
| 5 / 5.1 / 6: FR-003 | `MFG-02` / `F-PROF-003` / Edit Profile; US-2: Manage profile; US-3: Edit Profile | `docs/function-list.md`, line 18, No. 14; Screens: S06; sequence: this behavior is not separately shown in a supplied sequence; Usage Flow: this behavior is not separately shown in the supplied usage flow. Diagrams support only the steps actually shown; the full contract remains sourced to the Function List. |
| 5 / 5.1 / 6: FR-004 | `MFG-02` / `F-PROF-004` / Change Password; US-2: Manage profile; US-4: Change password | `docs/function-list.md`, line 19, No. 15; Screens: S07; sequence: this behavior is not separately shown in a supplied sequence; Usage Flow: this behavior is not separately shown in the supplied usage flow. Diagrams support only the steps actually shown; the full contract remains sourced to the Function List. |
| 5 / 5.1 / 6: FR-005 | `MFG-02` / `F-PROF-005` / Change Password; US-2: Manage profile; US-4: Change password | `docs/function-list.md`, line 20, No. 16; Screens: S07; sequence: this behavior is not separately shown in a supplied sequence; Usage Flow: this behavior is not separately shown in the supplied usage flow. Diagrams support only the steps actually shown; the full contract remains sourced to the Function List. |
| 5.2 BR-001 | Explicit source rule | F-PROF-005 explicitly requires old-password validation; no extra strength rule is supplied. |
| 7. S03 | Login Screen | `docs/screen-list.md`, line 5; `screens/S03-login_screen.md`, sections 1, 3-7 and 9 |
| 7. S06 | User Profile Screen | `docs/screen-list.md`, line 8; `screens/S06-user_profile_screen.md`, sections 1, 3-7 and 9 |
| 7. S07 | Change Password Screen | `docs/screen-list.md`, line 9; Screen Spec not supplied |
| 7. S38 | Notification Panel Screen | `docs/screen-list.md`, line 40; Screen Spec not supplied |

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
