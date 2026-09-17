# Spec Document: System Operations


| Field | Value |
| --- | --- |
| Module ID | `MFG-12` |
| Module name | System Operations |
| Spec version | v0.1 |
| Author (team member) | [NEEDS CLARIFICATION: Specify the responsible team member; Group B is named only as the team on the Session 1 scope sheet.] |
| Date | 2026-09-16 |
| Status | Draft |
| Approved by (Client role) | [NEEDS CLARIFICATION: Client approver role and approval are not supplied.] |
| DBIZ2 source | Function List `MFG-12`, No. 87-94, `F-SYS-001` .. `F-SYS-008`; Use Cases: Monitor system logs; Backup & restore data; Configure system; Use Case IDs: UC-S09, UC-S10, UC-S11; Screens: `S39`, `S40` |


---

## 1. Purpose and scope (mandatory)

System administrators can inspect activity logs and maintain system settings. They can also back up information and restore a previously saved version.

Source: [docs/function-list.md](../docs/function-list.md), `MFG-12` (No. 87-94); Session 1 MVP PDF, page 1 section 3. [NEEDS CLARIFICATION: Original DBIZ2 Schematic 1.1/1.2 cells are unavailable; the PDF reproduces the project objective but is not Session 3 MVP Scope v3.]

**In scope**

- System Logs
- Backup Data
- Restore Data
- Config System

Session 1 marks system operations as Won't for this MVP; the DBIZ2 scope is retained for traceability only. All DBIZ2 subfunctions below are retained as documentation; this does not authorize release of deferred functions. [NEEDS CLARIFICATION: Supply MVP Scope v3 and Session 3 decisions to confirm current module scope.]

**Out of scope**

- Company-account creation, update and deletion belong to MFG-03.

**Depends on**

- [NEEDS CLARIFICATION: No explicit module dependency contract is supplied; confirm dependencies without deriving new requirements from the architecture.]

## 2. Actors (mandatory)

| Actor | Role in this module | Where it comes from |
| --- | --- | --- |
| System Admin | Primary — System Logs, Backup Data, Restore Data, Config System | Function List `Actor` column, `MFG-12`: F-SYS-001, F-SYS-002, F-SYS-003, F-SYS-004, F-SYS-005, F-SYS-006, F-SYS-007, F-SYS-008 |

Primary identifies the actor performing the listed subfunctions; it does not replace conflicting Use Case or sequence labels. External participants appear in section 4 only when supplied by the source.

## 3. User scenarios and acceptance criteria (mandatory)

[NEEDS CLARIFICATION: P1/P2 scenario ordering is not agreed in the supplied materials; no scenario priority is inferred from Function List High/Medium/Low.]

### US-1 ([NEEDS CLARIFICATION: Scenario priority not agreed.]): Monitor system logs

**Journey.** As a `System Admin`, I want to `monitor system logs`, so that [NEEDS CLARIFICATION: The Use Case names the goal but does not state a separate scenario benefit.].

Source: `docs/architecture/use-case.md`, line 49, “Monitor system logs”; related FRs `FR-001` / `F-SYS-001`, `FR-002` / `F-SYS-002`.

[NEEDS CLARIFICATION: No detailed Usage Flow or sequence for this use case is supplied; the criterion records the named goal and any explicitly cited Function List outcome. Confirm preconditions, action sequence and failure behavior before treating it as an agreed acceptance test.]

**Acceptance scenarios**

1. **Given** system activity logs are available, **When** the system administrator monitors system logs, **Then** the logs are available to inspect.

### US-2 ([NEEDS CLARIFICATION: Scenario priority not agreed.]): Backup & restore data

**Journey.** As a `System Admin`, I want to `backup & restore data`, so that [NEEDS CLARIFICATION: The Use Case names the goal but does not state a separate scenario benefit.].

Source: `docs/architecture/use-case.md`, line 50, “Backup & restore data”; related FRs `FR-003` / `F-SYS-003`, `FR-004` / `F-SYS-004`, `FR-005` / `F-SYS-005`.

[NEEDS CLARIFICATION: No detailed Usage Flow or sequence for this use case is supplied; the criterion records the named goal and any explicitly cited Function List outcome. Confirm preconditions, action sequence and failure behavior before treating it as an agreed acceptance test.]

**Acceptance scenarios**

1. **Given** the system administrator is performing backup or restore, **When** the administrator selects the corresponding action, **Then** a manual backup produces a backup file and status, or restoring a selected backup produces system_restoration_status (F-SYS-004/F-SYS-005); [NEEDS CLARIFICATION: The supplied use case groups backup and restore; detailed preconditions, failure outcomes and completion display are absent.].

### US-3 ([NEEDS CLARIFICATION: Scenario priority not agreed.]): Configure system

**Journey.** As a `System Admin`, I want to `configure system`, so that [NEEDS CLARIFICATION: The Use Case names the goal but does not state a separate scenario benefit.].

Source: `docs/architecture/use-case.md`, line 51, “Configure system”; related FRs `FR-006` / `F-SYS-006`, `FR-007` / `F-SYS-007`, `FR-008` / `F-SYS-008`.

[NEEDS CLARIFICATION: No detailed Usage Flow or sequence for this use case is supplied; the criterion records the named goal and any explicitly cited Function List outcome. Confirm preconditions, action sequence and failure behavior before treating it as an agreed acceptance test.]

**Acceptance scenarios**

1. **Given** the system administrator is configuring the system, **When** the administrator changes configuration, **Then** the changes are validated and saved, and an alert is sent to the administrator group (F-SYS-007/F-SYS-008).

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

One FR per original Function List subfunction, in source order. FR IDs are local to this module; cite `MFG-12/FR-nnn` with the unchanged Subfunction ID. Original function names and High/Medium/Low values are preserved in each requirement note. MoSCoW values are used only for capabilities explicitly prioritized on page 2 of the Session 1 PDF; [NEEDS CLARIFICATION: Confirm per-subfunction priority mapping and the current Session 3 release scope.]

| FR ID | DBIZ2 Subfunction ID | Requirement (system MUST ...) | Actor | Priority |
| --- | --- | --- | --- | --- |
| FR-001 | F-SYS-001 | The system MUST display a list of system activity logs and user behaviors.<br/>DBIZ2 function: System Logs; subfunction: Log List View; category: Screen; original priority: Low. | System Admin | [NEEDS CLARIFICATION: Outside MVP (Session 1 Won't); no Must/Should/Could implementation priority is agreed.] |
| FR-002 | F-SYS-002 | The system MUST provide a search interface to filter logs by keywords or date range.<br/>DBIZ2 function: System Logs; subfunction: Search Log View; category: Screen; original priority: Low. | System Admin | [NEEDS CLARIFICATION: Outside MVP (Session 1 Won't); no Must/Should/Could implementation priority is agreed.] |
| FR-003 | F-SYS-003 | The system MUST display options for manual or scheduled database backups.<br/>DBIZ2 function: Backup Data; subfunction: Backup Option View; category: Screen; original priority: Medium. | System Admin | [NEEDS CLARIFICATION: Outside MVP (Session 1 Won't); no Must/Should/Could implementation priority is agreed.] |
| FR-004 | F-SYS-004 | The system MUST execute a full database backup and generate a confirmation record.<br/>DBIZ2 function: Backup Data; subfunction: Backup Exec Logic; category: Process; original priority: High. | System Admin | [NEEDS CLARIFICATION: Outside MVP (Session 1 Won't); no Must/Should/Could implementation priority is agreed.] |
| FR-005 | F-SYS-005 | The system MUST restore the system to the state of a previously saved backup version.<br/>DBIZ2 function: Restore Data; subfunction: Restore Exec Logic; category: Process; original priority: High. | System Admin | [NEEDS CLARIFICATION: Outside MVP (Session 1 Won't); no Must/Should/Could implementation priority is agreed.] |
| FR-006 | F-SYS-006 | The system MUST display system configuration parameters (SMTP, API Key) for editing.<br/>DBIZ2 function: Config System; subfunction: Settings Form; category: Screen; original priority: Medium. | System Admin | [NEEDS CLARIFICATION: Outside MVP (Session 1 Won't); no Must/Should/Could implementation priority is agreed.] |
| FR-007 | F-SYS-007 | The system MUST validate validity and save configuration changes into the system.<br/>DBIZ2 function: Config System; subfunction: Save Config Logic; category: Process; original priority: High. | System Admin | [NEEDS CLARIFICATION: Outside MVP (Session 1 Won't); no Must/Should/Could implementation priority is agreed.] |
| FR-008 | F-SYS-008 | The system MUST send an alert to the Admin group regarding recent system configuration changes.<br/>DBIZ2 function: Config System; subfunction: Config Notify Logic; category: Process; original priority: Low. | System Admin | [NEEDS CLARIFICATION: Outside MVP (Session 1 Won't); no Must/Should/Could implementation priority is agreed.] |

### 5.1 Input / Output contract

Literal Function List field names, types and required flags are preserved. Input and output rows are separate to avoid inventing field-to-field pairings. The template Required column applies to inputs; output required flags appear in Notes / validation. `—` means that side of this row is not applicable, not that a source field was omitted. Object contents, validation ranges and identifier formats are not inferred. [NEEDS CLARIFICATION: Supply nested Object/JSON/Array schemas and field validation where absent; apparent source type errors remain unchanged until clarified.]

| FR ID | Input field | Type | Required | Output field | Type | Notes / validation |
| --- | --- | --- | --- | --- | --- | --- |
| FR-001 | `log_level` | Object | Yes | — | — | Function List No. 87, F-SYS-001, Input column. |
| FR-001 | `date` | DateTime | Yes | — | — | Function List No. 87, F-SYS-001, Input column. |
| FR-001 | — | — | — | `logs_table_view` | [NEEDS CLARIFICATION: F-SYS-001 output logs_table_view: UI representation type.] | Output required: Yes. Function List No. 87, F-SYS-001, Output column. |
| FR-002 | `search_query_string` | String | No | — | — | Function List No. 88, F-SYS-002, Input column. |
| FR-002 | — | — | — | `filtered_log_results` | [NEEDS CLARIFICATION: F-SYS-002 output filtered_log_results: data type.] | Output required: Yes. Function List No. 88, F-SYS-002, Output column. |
| FR-003 | `admin_privileges` | [NEEDS CLARIFICATION: F-SYS-003 input admin_privileges: data type.] | Yes | — | — | Function List No. 89, F-SYS-003, Input column. |
| FR-003 | — | — | — | `backup_controls_ui` | [NEEDS CLARIFICATION: F-SYS-003 output backup_controls_ui: UI representation type.] | Output required: Yes. Function List No. 89, F-SYS-003, Output column. |
| FR-004 | `backup_command_trigger` | [NEEDS CLARIFICATION: F-SYS-004 input backup_command_trigger: data type.] | Yes | — | — | Function List No. 90, F-SYS-004, Input column. |
| FR-004 | — | — | — | `backup_file` | File | Output required: Yes. Function List No. 90, F-SYS-004, Output column. |
| FR-004 | — | — | — | `status` | String | Output required: Yes. Function List No. 90, F-SYS-004, Output column. |
| FR-005 | `selected_backup_file_id` | String | Yes | — | — | Function List No. 91, F-SYS-005, Input column. |
| FR-005 | — | — | — | `system_restoration_status` | String | Output required: Yes. Function List No. 91, F-SYS-005, Output column. |
| FR-006 | [NEEDS CLARIFICATION: F-SYS-006 input: no field specified.] | — | [NEEDS CLARIFICATION: F-SYS-006: input required flag unavailable.] | — | — | Function List No. 92, F-SYS-006, Input column |
| FR-006 | — | — | — | `configuration_form_ui` | [NEEDS CLARIFICATION: F-SYS-006 output configuration_form_ui: UI representation type.] | Output required: Yes. Function List No. 92, F-SYS-006, Output column. |
| FR-007 | `key_value_pairs_of_config` | Object | Yes | — | — | Function List No. 93, F-SYS-007, Input column. |
| FR-007 | — | — | — | `system_config_updated` | [NEEDS CLARIFICATION: F-SYS-007 output system_config_updated: data type.] | Output required: Yes. Function List No. 93, F-SYS-007, Output column. |
| FR-008 | `change_log` | [NEEDS CLARIFICATION: F-SYS-008 input change_log: data type.] | Yes | — | — | Function List No. 94, F-SYS-008, Input column. |
| FR-008 | `admin_group_id` | String | Yes | — | — | Function List No. 94, F-SYS-008, Input column. |
| FR-008 | — | — | — | `security_alert_email` | String | Output required: Yes. Function List No. 94, F-SYS-008, Output column. |

### 5.2 Business rules

| Rule ID | Rule | Why it exists |
| --- | --- | --- |
| BR-001 | Saving configuration changes requires validity checking and an alert to the administrator group. | F-SYS-007 specifies validation and F-SYS-008 specifies the alert; exact valid values are not supplied. Business rationale beyond the stated source is not separately documented. |

## 6. Key entities (mandatory)

| Entity | Attributes (from Input/Output fields) | Relationships |
| --- | --- | --- |
| Activity log | `log_level`, `date`, `search_query_string`, `filtered_log_results` | [NEEDS CLARIFICATION: Activity log: relationship cardinalities and nested field ownership are not specified in the Input/Output contract.] |
| Backup | `backup_command_trigger`, `backup_file`, `status`, `selected_backup_file_id`, `system_restoration_status` | [NEEDS CLARIFICATION: Backup: relationship cardinalities and nested field ownership are not specified in the Input/Output contract.] |
| Configuration | `key_value_pairs_of_config`, `system_config_updated`, `change_log`, `admin_group_id`, `security_alert_email` | [NEEDS CLARIFICATION: Configuration: relationship cardinalities and nested field ownership are not specified in the Input/Output contract.] |

Names above group the literal section 5.1 fields for discussion. They do not introduce tables, extra attributes, foreign keys or relationship cardinalities.

## 7. Screens involved

| Screen ID | Screen name | Priority | Screen Spec file |
| --- | --- | --- | --- |
| S39 | System Configuration Screen — Direct module screen | [NEEDS CLARIFICATION: S39: Screen List provides no agreed Must/Should priority.] | [NEEDS CLARIFICATION: S39: no Screen Spec file supplied; do not invent a screen-spec filename.] |
| S40 | System Log Viewer Screen — Direct module screen | [NEEDS CLARIFICATION: S40: Screen List provides no agreed Must/Should priority.] | [NEEDS CLARIFICATION: S40: no Screen Spec file supplied; do not invent a screen-spec filename.] |

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
| 3 | Use Case IDs: UC-S09, UC-S10, UC-S11 | Unassessed; see final question | Unassigned; see final question | Open |
| 4 | [NEEDS CLARIFICATION: Original DBIZ2 Schematic 1.1/1.2 cells are unavailable; the PDF reproduces the project objective but is not Session 3 MVP Scope v3.] | Unassessed; see final question | Unassigned; see final question | Open |
| 5 | [NEEDS CLARIFICATION: Supply MVP Scope v3 and Session 3 decisions to confirm current module scope.] | Unassessed; see final question | Unassigned; see final question | Open |
| 6 | [NEEDS CLARIFICATION: No explicit module dependency contract is supplied; confirm dependencies without deriving new requirements from the architecture.] | Unassessed; see final question | Unassigned; see final question | Open |
| 7 | [NEEDS CLARIFICATION: P1/P2 scenario ordering is not agreed in the supplied materials; no scenario priority is inferred from Function List High/Medium/Low.] | Unassessed; see final question | Unassigned; see final question | Open |
| 8 | [NEEDS CLARIFICATION: Scenario priority not agreed.] | Unassessed; see final question | Unassigned; see final question | Open |
| 9 | [NEEDS CLARIFICATION: The Use Case names the goal but does not state a separate scenario benefit.] | Unassessed; see final question | Unassigned; see final question | Open |
| 10 | [NEEDS CLARIFICATION: No detailed Usage Flow or sequence for this use case is supplied; the criterion records the named goal and any explicitly cited Function List outcome. Confirm preconditions, action sequence and failure behavior before treating it as an agreed acceptance test.] | Unassessed; see final question | Unassigned; see final question | Open |
| 11 | [NEEDS CLARIFICATION: The supplied use case groups backup and restore; detailed preconditions, failure outcomes and completion display are absent.] | Unassessed; see final question | Unassigned; see final question | Open |
| 12 | [NEEDS CLARIFICATION: Document missing/invalid inputs and empty-data outcomes not already covered by the supplied screens or sequences.] | Unassessed; see final question | Unassigned; see final question | Open |
| 13 | [NEEDS CLARIFICATION: Document behavior when a required external service or data operation is unavailable; do not infer retries or fallback paths.] | Unassessed; see final question | Unassigned; see final question | Open |
| 14 | [NEEDS CLARIFICATION: Document repeated actions and simultaneous-user outcomes; no concurrency or duplicate-submission rule is supplied.] | Unassessed; see final question | Unassigned; see final question | Open |
| 15 | [NEEDS CLARIFICATION: The supplied overall customer Usage Flow does not show this module; supply the relevant original Mermaid/figure. No flow is invented.] | Unassessed; see final question | Unassigned; see final question | Open |
| 16 | [NEEDS CLARIFICATION: No sequence diagram for this module is supplied; participants and messages cannot be reconstructed as requirements.] | Unassessed; see final question | Unassigned; see final question | Open |
| 17 | [NEEDS CLARIFICATION: Confirm per-subfunction priority mapping and the current Session 3 release scope.] | Unassessed; see final question | Unassigned; see final question | Open |
| 18 | [NEEDS CLARIFICATION: Outside MVP (Session 1 Won't); no Must/Should/Could implementation priority is agreed.] | Unassessed; see final question | Unassigned; see final question | Open |
| 19 | [NEEDS CLARIFICATION: Supply nested Object/JSON/Array schemas and field validation where absent; apparent source type errors remain unchanged until clarified.] | Unassessed; see final question | Unassigned; see final question | Open |
| 20 | [NEEDS CLARIFICATION: F-SYS-001 output logs_table_view: UI representation type.] | Unassessed; see final question | Unassigned; see final question | Open |
| 21 | [NEEDS CLARIFICATION: F-SYS-002 output filtered_log_results: data type.] | Unassessed; see final question | Unassigned; see final question | Open |
| 22 | [NEEDS CLARIFICATION: F-SYS-003 input admin_privileges: data type.] | Unassessed; see final question | Unassigned; see final question | Open |
| 23 | [NEEDS CLARIFICATION: F-SYS-003 output backup_controls_ui: UI representation type.] | Unassessed; see final question | Unassigned; see final question | Open |
| 24 | [NEEDS CLARIFICATION: F-SYS-004 input backup_command_trigger: data type.] | Unassessed; see final question | Unassigned; see final question | Open |
| 25 | [NEEDS CLARIFICATION: F-SYS-006 input: no field specified.] | Unassessed; see final question | Unassigned; see final question | Open |
| 26 | [NEEDS CLARIFICATION: F-SYS-006: input required flag unavailable.] | Unassessed; see final question | Unassigned; see final question | Open |
| 27 | [NEEDS CLARIFICATION: F-SYS-006 output configuration_form_ui: UI representation type.] | Unassessed; see final question | Unassigned; see final question | Open |
| 28 | [NEEDS CLARIFICATION: F-SYS-007 output system_config_updated: data type.] | Unassessed; see final question | Unassigned; see final question | Open |
| 29 | [NEEDS CLARIFICATION: F-SYS-008 input change_log: data type.] | Unassessed; see final question | Unassigned; see final question | Open |
| 30 | [NEEDS CLARIFICATION: Activity log: relationship cardinalities and nested field ownership are not specified in the Input/Output contract.] | Unassessed; see final question | Unassigned; see final question | Open |
| 31 | [NEEDS CLARIFICATION: Backup: relationship cardinalities and nested field ownership are not specified in the Input/Output contract.] | Unassessed; see final question | Unassigned; see final question | Open |
| 32 | [NEEDS CLARIFICATION: Configuration: relationship cardinalities and nested field ownership are not specified in the Input/Output contract.] | Unassessed; see final question | Unassigned; see final question | Open |
| 33 | [NEEDS CLARIFICATION: S39: Screen List provides no agreed Must/Should priority.] | Unassessed; see final question | Unassigned; see final question | Open |
| 34 | [NEEDS CLARIFICATION: S39: no Screen Spec file supplied; do not invent a screen-spec filename.] | Unassessed; see final question | Unassigned; see final question | Open |
| 35 | [NEEDS CLARIFICATION: S40: Screen List provides no agreed Must/Should priority.] | Unassessed; see final question | Unassigned; see final question | Open |
| 36 | [NEEDS CLARIFICATION: S40: no Screen Spec file supplied; do not invent a screen-spec filename.] | Unassessed; see final question | Unassigned; see final question | Open |
| 37 | [NEEDS CLARIFICATION: No agreed measurable user-outcome success criterion is present in the supplied Session 1 scope sheet or DBIZ2 extracts; provide the Session 3 criterion for this module.] | Unassessed; see final question | Unassigned; see final question | Open |
| 38 | [NEEDS CLARIFICATION: Confirm the user task, observable completion outcome, agreed target and evaluation method; none is supplied.] | Unassessed; see final question | Unassigned; see final question | Open |
| 39 | [NEEDS CLARIFICATION: Confirm whether this documented Session 1 assumption remains valid in Session 3.] | Unassessed; see final question | Unassigned; see final question | Open |
| 40 | [NEEDS CLARIFICATION: What are the documented backup schedule, retention, restore selection and restore-impact rules?] | Unassessed; see final question | Unassigned; see final question | Open |
| 41 | [NEEDS CLARIFICATION: Which configuration keys are valid and what validation does F-SYS-007 apply?] | Unassessed; see final question | Unassigned; see final question | Open |
| 42 | [NEEDS CLARIFICATION: No Session 3 Clarify meeting notes are supplied; carry over all unresolved decisions once provided.] | Unassessed; see final question | Unassigned; see final question | Open |
| 43 | [NEEDS CLARIFICATION: Original spreadsheet cells and figure numbers are unavailable; the traceability below uses exact supplied Markdown lines and the PDF page/section instead.] | Unassessed; see final question | Unassigned; see final question | Open |
| 44 | [NEEDS CLARIFICATION: Mermaid rendering has not been verified with a Mermaid renderer; source copying and node/edge checks alone do not establish rendering correctness.] | Unassessed; see final question | Unassigned; see final question | Open |
| 45 | [NEEDS CLARIFICATION: Open-question owners and blocking impacts have not been assigned.] | Unassessed; see final question | Unassigned; see final question | Open |

## 11. Traceability to DBIZ2

| Spec section | DBIZ2 source | Location |
| --- | --- | --- |
| 1. Purpose / scope | Function List module heading and all module rows; objective reproduced in Session 1 scope | `docs/function-list.md`, lines 100-108; `MVP_Score-WeaveLink.docx.pdf`, page 1 section 3 and page 2 section 4 |
| 2. Actors | Function List Actor column | `docs/function-list.md`, lines 101-108 |
| 4.1 Usage flow | Supplied customer usage flow | No module path exists in the supplied customer flow; see section 4.1 |
| 8. Success criteria / 9. Assumptions | Available scope document | `MVP_Score-WeaveLink.docx.pdf`, page 1 sections 1-3 and page 2 section 4; no measurable acceptance target or Session 3 document supplied |
| 3. US-1 | Use Case “Monitor system logs” (UC-S09) | `docs/architecture/use-case.md`, line 49 |
| 3. US-2 | Use Case “Backup & restore data” (UC-S10) | `docs/architecture/use-case.md`, line 50 |
| 3. US-3 | Use Case “Configure system” (UC-S11) | `docs/architecture/use-case.md`, line 51 |
| 4.2 Sequence | No module sequence supplied | `docs/architecture/sequence.md` contains SD-01 through SD-09 only; none documents this module |
| 5 / 5.1 / 6: FR-001 | `MFG-12` / `F-SYS-001` / System Logs; US-1: Monitor system logs | `docs/function-list.md`, line 101, No. 87; Screens: S40; sequence: this behavior is not separately shown in a supplied sequence; Usage Flow: this behavior is not separately shown in the supplied usage flow. Diagrams support only the steps actually shown; the full contract remains sourced to the Function List. |
| 5 / 5.1 / 6: FR-002 | `MFG-12` / `F-SYS-002` / System Logs; US-1: Monitor system logs | `docs/function-list.md`, line 102, No. 88; Screens: S40; sequence: this behavior is not separately shown in a supplied sequence; Usage Flow: this behavior is not separately shown in the supplied usage flow. Diagrams support only the steps actually shown; the full contract remains sourced to the Function List. |
| 5 / 5.1 / 6: FR-003 | `MFG-12` / `F-SYS-003` / Backup Data; US-2: Backup & restore data | `docs/function-list.md`, line 103, No. 89; Screens: S39; sequence: this behavior is not separately shown in a supplied sequence; Usage Flow: this behavior is not separately shown in the supplied usage flow. Diagrams support only the steps actually shown; the full contract remains sourced to the Function List. |
| 5 / 5.1 / 6: FR-004 | `MFG-12` / `F-SYS-004` / Backup Data; US-2: Backup & restore data | `docs/function-list.md`, line 104, No. 90; Screens: S39; sequence: this behavior is not separately shown in a supplied sequence; Usage Flow: this behavior is not separately shown in the supplied usage flow. Diagrams support only the steps actually shown; the full contract remains sourced to the Function List. |
| 5 / 5.1 / 6: FR-005 | `MFG-12` / `F-SYS-005` / Restore Data; US-2: Backup & restore data | `docs/function-list.md`, line 105, No. 91; Screens: S39; sequence: this behavior is not separately shown in a supplied sequence; Usage Flow: this behavior is not separately shown in the supplied usage flow. Diagrams support only the steps actually shown; the full contract remains sourced to the Function List. |
| 5 / 5.1 / 6: FR-006 | `MFG-12` / `F-SYS-006` / Config System; US-3: Configure system | `docs/function-list.md`, line 106, No. 92; Screens: S39; sequence: this behavior is not separately shown in a supplied sequence; Usage Flow: this behavior is not separately shown in the supplied usage flow. Diagrams support only the steps actually shown; the full contract remains sourced to the Function List. |
| 5 / 5.1 / 6: FR-007 | `MFG-12` / `F-SYS-007` / Config System; US-3: Configure system | `docs/function-list.md`, line 107, No. 93; Screens: S39; sequence: this behavior is not separately shown in a supplied sequence; Usage Flow: this behavior is not separately shown in the supplied usage flow. Diagrams support only the steps actually shown; the full contract remains sourced to the Function List. |
| 5 / 5.1 / 6: FR-008 | `MFG-12` / `F-SYS-008` / Config System; US-3: Configure system | `docs/function-list.md`, line 108, No. 94; Screens: S39; sequence: this behavior is not separately shown in a supplied sequence; Usage Flow: this behavior is not separately shown in the supplied usage flow. Diagrams support only the steps actually shown; the full contract remains sourced to the Function List. |
| 5.2 BR-001 | Explicit source rule | F-SYS-007 specifies validation and F-SYS-008 specifies the alert; exact valid values are not supplied. |
| 7. S39 | System Configuration Screen | `docs/screen-list.md`, line 41; Screen Spec not supplied |
| 7. S40 | System Log Viewer Screen | `docs/screen-list.md`, line 42; Screen Spec not supplied |

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
