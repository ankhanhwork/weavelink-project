# Spec Document: Sales Consultant


| Field | Value |
| --- | --- |
| Module ID | `MFG-08` |
| Module name | Sales Consultant |
| Spec version | v0.1 |
| Author (team member) | [NEEDS CLARIFICATION: Specify the responsible team member; Group B is named only as the team on the Session 1 scope sheet.] |
| Date | 2026-09-16 |
| Status | Draft |
| Approved by (Client role) | [NEEDS CLARIFICATION: Client approver role and approval are not supplied.] |
| DBIZ2 source | Function List `MFG-08`, No. 60-67, `F-ORD-001` .. `F-ORD-008`; Use Cases: View assignment; Update customer consultation; Assign consultant; Use Case IDs: UC-S01, UC-S02, UC-C19; Screens: `S17`, `S18`, `S19`, `S20`, `S21` |


---

## 1. Purpose and scope (mandatory)

Company administrators can assign customers to sales consultants. Consultants can view their assignments and consultation history and record customer-care progress.

Source: [docs/function-list.md](../docs/function-list.md), `MFG-08` (No. 60-67); Session 1 MVP PDF, page 1 section 3. [NEEDS CLARIFICATION: Original DBIZ2 Schematic 1.1/1.2 cells are unavailable; the PDF reproduces the project objective but is not Session 3 MVP Scope v3.]

**In scope**

- Assign Consultant
- View Assignment
- Update Consult

Session 1 marks consultant assignment and task dashboard as Could. All DBIZ2 subfunctions below are retained as documentation; this does not authorize release of deferred functions. [NEEDS CLARIFICATION: Supply MVP Scope v3 and Session 3 decisions to confirm current module scope.]

**Out of scope**

- Finished-design assignment and delivery notifications are F-DES-009 through F-DES-011 in MFG-05.

**Depends on**

- MFG-05: design-service request and finished-design context at S18/S21.

## 2. Actors (mandatory)

| Actor | Role in this module | Where it comes from |
| --- | --- | --- |
| Company Admin | Primary — Assign Consultant | Function List `Actor` column, `MFG-08`: F-ORD-001, F-ORD-002, F-ORD-003, F-ORD-004 |
| Sales Consultant | Primary — View Assignment, Update Consult | Function List `Actor` column, `MFG-08`: F-ORD-005, F-ORD-006, F-ORD-007, F-ORD-008 |

Primary identifies the actor performing the listed subfunctions; it does not replace conflicting Use Case or sequence labels. External participants appear in section 4 only when supplied by the source.

## 3. User scenarios and acceptance criteria (mandatory)

[NEEDS CLARIFICATION: P1/P2 scenario ordering is not agreed in the supplied materials; no scenario priority is inferred from Function List High/Medium/Low.]

### US-1 ([NEEDS CLARIFICATION: Scenario priority not agreed.]): View assignment

**Journey.** As a `Sales Consultant`, I want to `view assignment`, so that [NEEDS CLARIFICATION: The Use Case names the goal but does not state a separate scenario benefit.].

Source: `docs/architecture/use-case.md`, line 26, “View assignment”; related FRs `FR-005` / `F-ORD-005`, `FR-006` / `F-ORD-006`.

[NEEDS CLARIFICATION: No detailed Usage Flow or sequence for this use case is supplied; the criterion records the named goal and any explicitly cited Function List outcome. Confirm preconditions, action sequence and failure behavior before treating it as an agreed acceptance test.]

**Acceptance scenarios**

1. **Given** the sales consultant has an assignment, **When** the consultant views the assignment, **Then** the assignment is displayed.

### US-2 ([NEEDS CLARIFICATION: Scenario priority not agreed.]): Update customer consultation

**Journey.** As a `Sales Consultant`, I want to `update customer consultation`, so that [NEEDS CLARIFICATION: The Use Case names the goal but does not state a separate scenario benefit.].

Source: `docs/architecture/use-case.md`, line 27, “Update customer consultation”; related FRs `FR-007` / `F-ORD-007`, `FR-008` / `F-ORD-008`.

[NEEDS CLARIFICATION: No detailed Usage Flow or sequence for this use case is supplied; the criterion records the named goal and any explicitly cited Function List outcome. Confirm preconditions, action sequence and failure behavior before treating it as an agreed acceptance test.]

**Acceptance scenarios**

1. **Given** a consultation is available to the sales consultant, **When** the consultant updates customer consultation, **Then** the consultation record reflects new_status and notes as updated_crm_record (MFG-08 F-ORD-008).

### US-3 ([NEEDS CLARIFICATION: Scenario priority not agreed.]): Assign consultant

**Journey.** As a `Company Admin`, I want to `assign consultant`, so that [NEEDS CLARIFICATION: The Use Case names the goal but does not state a separate scenario benefit.].

Source: `docs/architecture/use-case.md`, line 36, “Assign consultant”; related FRs `FR-001` / `F-ORD-001`, `FR-002` / `F-ORD-002`, `FR-003` / `F-ORD-003`, `FR-004` / `F-ORD-004`.

[NEEDS CLARIFICATION: No detailed Usage Flow or sequence for this use case is supplied; the criterion records the named goal and any explicitly cited Function List outcome. Confirm preconditions, action sequence and failure behavior before treating it as an agreed acceptance test.]

**Acceptance scenarios**

1. **Given** a customer is available for assignment, **When** the company administrator assigns a consultant, **Then** the customer record identifies the assigned consultant and the consultant receives the assignment notification (MFG-08 F-ORD-003/F-ORD-004).

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

One FR per original Function List subfunction, in source order. FR IDs are local to this module; cite `MFG-08/FR-nnn` with the unchanged Subfunction ID. Original function names and High/Medium/Low values are preserved in each requirement note. MoSCoW values are used only for capabilities explicitly prioritized on page 2 of the Session 1 PDF; [NEEDS CLARIFICATION: Confirm per-subfunction priority mapping and the current Session 3 release scope.]

| FR ID | DBIZ2 Subfunction ID | Requirement (system MUST ...) | Actor | Priority |
| --- | --- | --- | --- | --- |
| FR-001 | F-ORD-001 | The system MUST display a list of potential customers who have not been assigned a consultant.<br/>DBIZ2 function: Assign Consultant; subfunction: Unassigned Cust View; category: Screen; original priority: Medium. | Company Admin | Could |
| FR-002 | F-ORD-002 | The system MUST view customer details and request history for categorization purposes.<br/>DBIZ2 function: Assign Consultant; subfunction: Customer Detail View; category: Screen; original priority: Medium. | Company Admin | Could |
| FR-003 | F-ORD-003 | The system MUST update the customer record to assign a specific sales consultant.<br/>DBIZ2 function: Assign Consultant; subfunction: Assign Sales Logic; category: Process; original priority: Medium. | Company Admin | Could |
| FR-004 | F-ORD-004 | The system MUST send a notification to the consultant regarding the assignment of a new customer.<br/>DBIZ2 function: Assign Consultant; subfunction: Assign Notify Logic; category: Process; original priority: Low. | Company Admin | Could |
| FR-005 | F-ORD-005 | The system MUST display a list of customers currently managed by the consultant.<br/>DBIZ2 function: View Assignment; subfunction: Assigned Cust View; category: Screen; original priority: Medium. | Sales Consultant | Could |
| FR-006 | F-ORD-006 | The system MUST display the full consultation context including interested products and chat history.<br/>DBIZ2 function: View Assignment; subfunction: Context View; category: Screen; original priority: Medium. | Sales Consultant | Could |
| FR-007 | F-ORD-007 | The system MUST display details of the consultation record for the staff to update progress.<br/>DBIZ2 function: Update Consult; subfunction: Consultation Detail; category: Screen; original priority: Medium. | Sales Consultant | Could |
| FR-008 | F-ORD-008 | The system MUST update the customer care status (e.g., Contacted, Closed Deal).<br/>DBIZ2 function: Update Consult; subfunction: Update Status Logic; category: Process; original priority: Medium. | Sales Consultant | Could |

### 5.1 Input / Output contract

Literal Function List field names, types and required flags are preserved. Input and output rows are separate to avoid inventing field-to-field pairings. The template Required column applies to inputs; output required flags appear in Notes / validation. `—` means that side of this row is not applicable, not that a source field was omitted. Object contents, validation ranges and identifier formats are not inferred. [NEEDS CLARIFICATION: Supply nested Object/JSON/Array schemas and field validation where absent; apparent source type errors remain unchanged until clarified.]

| FR ID | Input field | Type | Required | Output field | Type | Notes / validation |
| --- | --- | --- | --- | --- | --- | --- |
| FR-001 | `filter` | String | No | — | — | Function List No. 60, F-ORD-001, Input column. |
| FR-001 | — | — | — | `list_of_leads_customers` | Array<Object> | Output required: Yes. Function List No. 60, F-ORD-001, Output column. |
| FR-002 | `customer_id` | String | Yes | — | — | Function List No. 61, F-ORD-002, Input column. |
| FR-002 | — | — | — | `customer_360_view` | [NEEDS CLARIFICATION: F-ORD-002 output customer_360_view: UI representation type.] | Output required: Yes. Function List No. 61, F-ORD-002, Output column. |
| FR-003 | `customer_id` | String | Yes | — | — | Function List No. 62, F-ORD-003, Input column. |
| FR-003 | `consultant_user_id` | String | Yes | — | — | Function List No. 62, F-ORD-003, Input column. |
| FR-003 | — | — | — | `record_updated_with_assignee` | Object | Output required: Yes. Function List No. 62, F-ORD-003, Output column. |
| FR-004 | `consultant_email` | String | Yes | — | — | Function List No. 63, F-ORD-004, Input column. |
| FR-004 | `customer_info` | Object | Yes | — | — | Function List No. 63, F-ORD-004, Input column. |
| FR-004 | — | — | — | `assignment_notification` | [NEEDS CLARIFICATION: F-ORD-004 output assignment_notification: data type.] | Output required: Yes. Function List No. 63, F-ORD-004, Output column. |
| FR-005 | `consultant_id` | String | Yes | — | — | Function List No. 64, F-ORD-005, Input column. |
| FR-005 | — | — | — | `list_of_assigned_customers` | Array<Object> | Output required: Yes. Function List No. 64, F-ORD-005, Output column. |
| FR-006 | `customer_id` | String | Yes | — | — | Function List No. 65, F-ORD-006, Input column. |
| FR-006 | — | — | — | `interaction_history_logs` | Array<Object> | Output required: Yes. Function List No. 65, F-ORD-006, Output column. |
| FR-007 | `consultation_record_id` | Object | Yes | — | — | Function List No. 66, F-ORD-007, Input column. |
| FR-007 | — | — | — | `detailed_view_with_notes_field` | [NEEDS CLARIFICATION: F-ORD-007 output detailed_view_with_notes_field: UI representation type.] | Output required: Yes. Function List No. 66, F-ORD-007, Output column. |
| FR-008 | `record_id` | Object | Yes | — | — | Function List No. 67, F-ORD-008, Input column. |
| FR-008 | `new_status` | String | Yes | — | — | Function List No. 67, F-ORD-008, Input column. |
| FR-008 | `notes` | [NEEDS CLARIFICATION: F-ORD-008 input notes: data type.] | Yes | — | — | Function List No. 67, F-ORD-008, Input column. |
| FR-008 | — | — | — | `updated_crm_record` | Object | Output required: Yes. Function List No. 67, F-ORD-008, Output column. |

### 5.2 Business rules

| Rule ID | Rule | Why it exists |
| --- | --- | --- |
| BR-001 | Assigning a customer triggers a notification to the assigned consultant. | F-ORD-003 and F-ORD-004 within MFG-08; the recipient input is consultant_email. Business rationale beyond the stated source is not separately documented. |

## 6. Key entities (mandatory)

| Entity | Attributes (from Input/Output fields) | Relationships |
| --- | --- | --- |
| Customer assignment | `customer_id`, `consultant_user_id`, `record_updated_with_assignee`, `consultant_email`, `customer_info`, `consultant_id`, `list_of_assigned_customers` | [NEEDS CLARIFICATION: Customer assignment: relationship cardinalities and nested field ownership are not specified in the Input/Output contract.] |
| Consultation | `consultation_record_id`, `record_id`, `interaction_history_logs`, `new_status`, `notes`, `updated_crm_record` | [NEEDS CLARIFICATION: Consultation: relationship cardinalities and nested field ownership are not specified in the Input/Output contract.] |

Names above group the literal section 5.1 fields for discussion. They do not introduce tables, extra attributes, foreign keys or relationship cardinalities.

## 7. Screens involved

| Screen ID | Screen name | Priority | Screen Spec file |
| --- | --- | --- | --- |
| S17 | Customer Designs Screen — Shared screen / navigation boundary | [NEEDS CLARIFICATION: S17: Screen List provides no agreed Must/Should priority.] | `screens/S17-customer_designs_screen.md` ([open](../screens/S17-customer_designs_screen.md)) |
| S18 | Consultation Request List Screen (Company Admin) — Direct module screen | [NEEDS CLARIFICATION: S18: Screen List provides no agreed Must/Should priority.] | [NEEDS CLARIFICATION: S18: no Screen Spec file supplied; do not invent a screen-spec filename.] |
| S19 | Consultation Assignment Screen — Direct module screen | [NEEDS CLARIFICATION: S19: Screen List provides no agreed Must/Should priority.] | [NEEDS CLARIFICATION: S19: no Screen Spec file supplied; do not invent a screen-spec filename.] |
| S20 | Consultant Task List Screen — Direct module screen | [NEEDS CLARIFICATION: S20: Screen List provides no agreed Must/Should priority.] | [NEEDS CLARIFICATION: S20: no Screen Spec file supplied; do not invent a screen-spec filename.] |
| S21 | Consultation Detail Screen (Consultant) — Direct module screen | [NEEDS CLARIFICATION: S21: Screen List provides no agreed Must/Should priority.] | [NEEDS CLARIFICATION: S21: no Screen Spec file supplied; do not invent a screen-spec filename.] |

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
| 3 | Use Case IDs: UC-S01, UC-S02, UC-C19 | Unassessed; see final question | Unassigned; see final question | Open |
| 4 | [NEEDS CLARIFICATION: Original DBIZ2 Schematic 1.1/1.2 cells are unavailable; the PDF reproduces the project objective but is not Session 3 MVP Scope v3.] | Unassessed; see final question | Unassigned; see final question | Open |
| 5 | [NEEDS CLARIFICATION: Supply MVP Scope v3 and Session 3 decisions to confirm current module scope.] | Unassessed; see final question | Unassigned; see final question | Open |
| 6 | [NEEDS CLARIFICATION: P1/P2 scenario ordering is not agreed in the supplied materials; no scenario priority is inferred from Function List High/Medium/Low.] | Unassessed; see final question | Unassigned; see final question | Open |
| 7 | [NEEDS CLARIFICATION: Scenario priority not agreed.] | Unassessed; see final question | Unassigned; see final question | Open |
| 8 | [NEEDS CLARIFICATION: The Use Case names the goal but does not state a separate scenario benefit.] | Unassessed; see final question | Unassigned; see final question | Open |
| 9 | [NEEDS CLARIFICATION: No detailed Usage Flow or sequence for this use case is supplied; the criterion records the named goal and any explicitly cited Function List outcome. Confirm preconditions, action sequence and failure behavior before treating it as an agreed acceptance test.] | Unassessed; see final question | Unassigned; see final question | Open |
| 10 | [NEEDS CLARIFICATION: Document missing/invalid inputs and empty-data outcomes not already covered by the supplied screens or sequences.] | Unassessed; see final question | Unassigned; see final question | Open |
| 11 | [NEEDS CLARIFICATION: Document behavior when a required external service or data operation is unavailable; do not infer retries or fallback paths.] | Unassessed; see final question | Unassigned; see final question | Open |
| 12 | [NEEDS CLARIFICATION: Document repeated actions and simultaneous-user outcomes; no concurrency or duplicate-submission rule is supplied.] | Unassessed; see final question | Unassigned; see final question | Open |
| 13 | [NEEDS CLARIFICATION: The supplied overall customer Usage Flow does not show this module; supply the relevant original Mermaid/figure. No flow is invented.] | Unassessed; see final question | Unassigned; see final question | Open |
| 14 | [NEEDS CLARIFICATION: No sequence diagram for this module is supplied; participants and messages cannot be reconstructed as requirements.] | Unassessed; see final question | Unassigned; see final question | Open |
| 15 | [NEEDS CLARIFICATION: Confirm per-subfunction priority mapping and the current Session 3 release scope.] | Unassessed; see final question | Unassigned; see final question | Open |
| 16 | [NEEDS CLARIFICATION: Supply nested Object/JSON/Array schemas and field validation where absent; apparent source type errors remain unchanged until clarified.] | Unassessed; see final question | Unassigned; see final question | Open |
| 17 | [NEEDS CLARIFICATION: F-ORD-002 output customer_360_view: UI representation type.] | Unassessed; see final question | Unassigned; see final question | Open |
| 18 | [NEEDS CLARIFICATION: F-ORD-004 output assignment_notification: data type.] | Unassessed; see final question | Unassigned; see final question | Open |
| 19 | [NEEDS CLARIFICATION: F-ORD-007 output detailed_view_with_notes_field: UI representation type.] | Unassessed; see final question | Unassigned; see final question | Open |
| 20 | [NEEDS CLARIFICATION: F-ORD-008 input notes: data type.] | Unassessed; see final question | Unassigned; see final question | Open |
| 21 | [NEEDS CLARIFICATION: Customer assignment: relationship cardinalities and nested field ownership are not specified in the Input/Output contract.] | Unassessed; see final question | Unassigned; see final question | Open |
| 22 | [NEEDS CLARIFICATION: Consultation: relationship cardinalities and nested field ownership are not specified in the Input/Output contract.] | Unassessed; see final question | Unassigned; see final question | Open |
| 23 | [NEEDS CLARIFICATION: S17: Screen List provides no agreed Must/Should priority.] | Unassessed; see final question | Unassigned; see final question | Open |
| 24 | [NEEDS CLARIFICATION: S18: Screen List provides no agreed Must/Should priority.] | Unassessed; see final question | Unassigned; see final question | Open |
| 25 | [NEEDS CLARIFICATION: S18: no Screen Spec file supplied; do not invent a screen-spec filename.] | Unassessed; see final question | Unassigned; see final question | Open |
| 26 | [NEEDS CLARIFICATION: S19: Screen List provides no agreed Must/Should priority.] | Unassessed; see final question | Unassigned; see final question | Open |
| 27 | [NEEDS CLARIFICATION: S19: no Screen Spec file supplied; do not invent a screen-spec filename.] | Unassessed; see final question | Unassigned; see final question | Open |
| 28 | [NEEDS CLARIFICATION: S20: Screen List provides no agreed Must/Should priority.] | Unassessed; see final question | Unassigned; see final question | Open |
| 29 | [NEEDS CLARIFICATION: S20: no Screen Spec file supplied; do not invent a screen-spec filename.] | Unassessed; see final question | Unassigned; see final question | Open |
| 30 | [NEEDS CLARIFICATION: S21: Screen List provides no agreed Must/Should priority.] | Unassessed; see final question | Unassigned; see final question | Open |
| 31 | [NEEDS CLARIFICATION: S21: no Screen Spec file supplied; do not invent a screen-spec filename.] | Unassessed; see final question | Unassigned; see final question | Open |
| 32 | [NEEDS CLARIFICATION: No agreed measurable user-outcome success criterion is present in the supplied Session 1 scope sheet or DBIZ2 extracts; provide the Session 3 criterion for this module.] | Unassessed; see final question | Unassigned; see final question | Open |
| 33 | [NEEDS CLARIFICATION: Confirm the user task, observable completion outcome, agreed target and evaluation method; none is supplied.] | Unassessed; see final question | Unassigned; see final question | Open |
| 34 | [NEEDS CLARIFICATION: F-ORD-001 through F-ORD-007 duplicate IDs in MFG-07. Preserve both source sets and confirm a module-qualified reference convention.] | Unassessed; see final question | Unassigned; see final question | Open |
| 35 | [NEEDS CLARIFICATION: The Function List assigns customers, while S19 assigns consultants to consultation requests; confirm the assignment subject and cardinality.] | Unassessed; see final question | Unassigned; see final question | Open |
| 36 | [NEEDS CLARIFICATION: Contacted and Closed Deal are examples only; provide the agreed customer-care status set and transitions.] | Unassessed; see final question | Unassigned; see final question | Open |
| 37 | [NEEDS CLARIFICATION: The Use Case connects Sales Consultant to Update order status but this module has no corresponding order-status subfunction; confirm ownership without adding an FR.] | Unassessed; see final question | Unassigned; see final question | Open |
| 38 | [NEEDS CLARIFICATION: S17, [NEEDS CLARIFICATION: Must / Should / Could not given in Screen List]: Must / Should / Could not given in Screen List] Source: `screens/S17-customer_designs_screen.md`, line 16. | Unassessed; see final question | Unassigned; see final question | Open |
| 39 | [NEEDS CLARIFICATION: S17, **The user leaves this screen when:** [NEEDS CLARIFICATION: all exit paths are not specifi: all exit paths are not specified; documented interactions appear in section 5.] Source: `screens/S17-customer_designs_screen.md`, line 25. | Unassessed; see final question | Unassigned; see final question | Open |
| 40 | [NEEDS CLARIFICATION: S17, Search designs input: search field not specified by F-DES-004] Source: `screens/S17-customer_designs_screen.md`, line 51. | Unassessed; see final question | Unassigned; see final question | Open |
| 41 | [NEEDS CLARIFICATION: S17, Search designs input: search matching rules] Source: `screens/S17-customer_designs_screen.md`, line 51. | Unassessed; see final question | Unassigned; see final question | Open |
| 42 | [NEEDS CLARIFICATION: S17, Design row 1 thumbnail: schema] Source: `screens/S17-customer_designs_screen.md`, line 55. | Unassessed; see final question | Unassigned; see final question | Open |
| 43 | [NEEDS CLARIFICATION: S17, Design row 1 name: schema] Source: `screens/S17-customer_designs_screen.md`, line 56. | Unassessed; see final question | Unassigned; see final question | Open |
| 44 | [NEEDS CLARIFICATION: S17, Design row 1 category: schema] Source: `screens/S17-customer_designs_screen.md`, line 57. | Unassessed; see final question | Unassigned; see final question | Open |
| 45 | [NEEDS CLARIFICATION: S17, Design row 1 created date: schema] Source: `screens/S17-customer_designs_screen.md`, line 58. | Unassessed; see final question | Unassigned; see final question | Open |
| 46 | [NEEDS CLARIFICATION: S17, Design row 1 updated date: schema] Source: `screens/S17-customer_designs_screen.md`, line 59. | Unassessed; see final question | Unassigned; see final question | Open |
| 47 | [NEEDS CLARIFICATION: S17, Design row 2 thumbnail: schema] Source: `screens/S17-customer_designs_screen.md`, line 64. | Unassessed; see final question | Unassigned; see final question | Open |
| 48 | [NEEDS CLARIFICATION: S17, Design row 2 name: schema] Source: `screens/S17-customer_designs_screen.md`, line 65. | Unassessed; see final question | Unassigned; see final question | Open |
| 49 | [NEEDS CLARIFICATION: S17, Design row 2 category: schema] Source: `screens/S17-customer_designs_screen.md`, line 66. | Unassessed; see final question | Unassigned; see final question | Open |
| 50 | [NEEDS CLARIFICATION: S17, Design row 2 created date: schema] Source: `screens/S17-customer_designs_screen.md`, line 67. | Unassessed; see final question | Unassigned; see final question | Open |
| 51 | [NEEDS CLARIFICATION: S17, Design row 2 updated date: schema] Source: `screens/S17-customer_designs_screen.md`, line 68. | Unassessed; see final question | Unassigned; see final question | Open |
| 52 | [NEEDS CLARIFICATION: S17, Design row 3 thumbnail: schema] Source: `screens/S17-customer_designs_screen.md`, line 73. | Unassessed; see final question | Unassigned; see final question | Open |
| 53 | [NEEDS CLARIFICATION: S17, Design row 3 name: schema] Source: `screens/S17-customer_designs_screen.md`, line 74. | Unassessed; see final question | Unassigned; see final question | Open |
| 54 | [NEEDS CLARIFICATION: S17, Design row 3 category: schema] Source: `screens/S17-customer_designs_screen.md`, line 75. | Unassessed; see final question | Unassigned; see final question | Open |
| 55 | [NEEDS CLARIFICATION: S17, Design row 3 created date: schema] Source: `screens/S17-customer_designs_screen.md`, line 76. | Unassessed; see final question | Unassigned; see final question | Open |
| 56 | [NEEDS CLARIFICATION: S17, Design row 3 updated date: schema] Source: `screens/S17-customer_designs_screen.md`, line 77. | Unassessed; see final question | Unassigned; see final question | Open |
| 57 | [NEEDS CLARIFICATION: S17, Design row 4 thumbnail: schema] Source: `screens/S17-customer_designs_screen.md`, line 82. | Unassessed; see final question | Unassigned; see final question | Open |
| 58 | [NEEDS CLARIFICATION: S17, Design row 4 name: schema] Source: `screens/S17-customer_designs_screen.md`, line 83. | Unassessed; see final question | Unassigned; see final question | Open |
| 59 | [NEEDS CLARIFICATION: S17, Design row 4 category: schema] Source: `screens/S17-customer_designs_screen.md`, line 84. | Unassessed; see final question | Unassigned; see final question | Open |
| 60 | [NEEDS CLARIFICATION: S17, Design row 4 created date: schema] Source: `screens/S17-customer_designs_screen.md`, line 85. | Unassessed; see final question | Unassigned; see final question | Open |
| 61 | [NEEDS CLARIFICATION: S17, Design row 4 updated date: schema] Source: `screens/S17-customer_designs_screen.md`, line 86. | Unassessed; see final question | Unassigned; see final question | Open |
| 62 | [NEEDS CLARIFICATION: S17, Design row 5 thumbnail: schema] Source: `screens/S17-customer_designs_screen.md`, line 91. | Unassessed; see final question | Unassigned; see final question | Open |
| 63 | [NEEDS CLARIFICATION: S17, Design row 5 name: schema] Source: `screens/S17-customer_designs_screen.md`, line 92. | Unassessed; see final question | Unassigned; see final question | Open |
| 64 | [NEEDS CLARIFICATION: S17, Design row 5 category: schema] Source: `screens/S17-customer_designs_screen.md`, line 93. | Unassessed; see final question | Unassigned; see final question | Open |
| 65 | [NEEDS CLARIFICATION: S17, Design row 5 created date: schema] Source: `screens/S17-customer_designs_screen.md`, line 94. | Unassessed; see final question | Unassigned; see final question | Open |
| 66 | [NEEDS CLARIFICATION: S17, Design row 5 updated date: schema] Source: `screens/S17-customer_designs_screen.md`, line 95. | Unassessed; see final question | Unassigned; see final question | Open |
| 67 | [NEEDS CLARIFICATION: S17, [NEEDS CLARIFICATION: empty designs message]: empty designs message] Source: `screens/S17-customer_designs_screen.md`, line 137. | Unassessed; see final question | Unassigned; see final question | Open |
| 68 | [NEEDS CLARIFICATION: S17, [NEEDS CLARIFICATION: design list loading treatment]: design list loading treatment] Source: `screens/S17-customer_designs_screen.md`, line 138. | Unassessed; see final question | Unassigned; see final question | Open |
| 69 | [NEEDS CLARIFICATION: S17, [NEEDS CLARIFICATION: design list error treatment]: design list error treatment] Source: `screens/S17-customer_designs_screen.md`, line 139. | Unassessed; see final question | Unassigned; see final question | Open |
| 70 | [NEEDS CLARIFICATION: S17, [NEEDS CLARIFICATION: edit/copy/delete confirmation behavior]: edit/copy/delete confirmation behavior] Source: `screens/S17-customer_designs_screen.md`, line 140. | Unassessed; see final question | Unassigned; see final question | Open |
| 71 | [NEEDS CLARIFICATION: S17, About Dony navigation: destination not in Screen List] Source: `screens/S17-customer_designs_screen.md`, line 148. | Unassessed; see final question | Unassigned; see final question | Open |
| 72 | [NEEDS CLARIFICATION: S17, Contact Us navigation: destination not in Screen List] Source: `screens/S17-customer_designs_screen.md`, line 151. | Unassessed; see final question | Unassigned; see final question | Open |
| 73 | [NEEDS CLARIFICATION: S17, Search designs input: filtering behavior] Source: `screens/S17-customer_designs_screen.md`, line 155. | Unassessed; see final question | Unassigned; see final question | Open |
| 74 | [NEEDS CLARIFICATION: S17, Category filter: filter choices] Source: `screens/S17-customer_designs_screen.md`, line 156. | Unassessed; see final question | Unassigned; see final question | Open |
| 75 | [NEEDS CLARIFICATION: S17, Date filter: filter choices] Source: `screens/S17-customer_designs_screen.md`, line 157. | Unassessed; see final question | Unassigned; see final question | Open |
| 76 | [NEEDS CLARIFICATION: S17, Design row 1 copy icon: duplicate behavior] Source: `screens/S17-customer_designs_screen.md`, line 163. | Unassessed; see final question | Unassigned; see final question | Open |
| 77 | [NEEDS CLARIFICATION: S17, Design row 2 copy icon: duplicate behavior] Source: `screens/S17-customer_designs_screen.md`, line 164. | Unassessed; see final question | Unassigned; see final question | Open |
| 78 | [NEEDS CLARIFICATION: S17, Design row 3 copy icon: duplicate behavior] Source: `screens/S17-customer_designs_screen.md`, line 165. | Unassessed; see final question | Unassigned; see final question | Open |
| 79 | [NEEDS CLARIFICATION: S17, Design row 4 copy icon: duplicate behavior] Source: `screens/S17-customer_designs_screen.md`, line 166. | Unassessed; see final question | Unassigned; see final question | Open |
| 80 | [NEEDS CLARIFICATION: S17, Design row 5 copy icon: duplicate behavior] Source: `screens/S17-customer_designs_screen.md`, line 167. | Unassessed; see final question | Unassigned; see final question | Open |
| 81 | [NEEDS CLARIFICATION: S17, Design row 1 delete icon: delete behavior] Source: `screens/S17-customer_designs_screen.md`, line 168. | Unassessed; see final question | Unassigned; see final question | Open |
| 82 | [NEEDS CLARIFICATION: S17, Design row 2 delete icon: delete behavior] Source: `screens/S17-customer_designs_screen.md`, line 169. | Unassessed; see final question | Unassigned; see final question | Open |
| 83 | [NEEDS CLARIFICATION: S17, Design row 3 delete icon: delete behavior] Source: `screens/S17-customer_designs_screen.md`, line 170. | Unassessed; see final question | Unassigned; see final question | Open |
| 84 | [NEEDS CLARIFICATION: S17, Design row 4 delete icon: delete behavior] Source: `screens/S17-customer_designs_screen.md`, line 171. | Unassessed; see final question | Unassigned; see final question | Open |
| 85 | [NEEDS CLARIFICATION: S17, Design row 5 delete icon: delete behavior] Source: `screens/S17-customer_designs_screen.md`, line 172. | Unassessed; see final question | Unassigned; see final question | Open |
| 86 | [NEEDS CLARIFICATION: S17, Zalo contact button: contact destination] Source: `screens/S17-customer_designs_screen.md`, line 183. | Unassessed; see final question | Unassigned; see final question | Open |
| 87 | [NEEDS CLARIFICATION: S17, Telephone contact button: dial behavior] Source: `screens/S17-customer_designs_screen.md`, line 184. | Unassessed; see final question | Unassigned; see final question | Open |
| 88 | [NEEDS CLARIFICATION: S17, Footer Facebook icon: external or in-system destination] Source: `screens/S17-customer_designs_screen.md`, line 185. | Unassessed; see final question | Unassigned; see final question | Open |
| 89 | [NEEDS CLARIFICATION: S17, Footer X icon: external or in-system destination] Source: `screens/S17-customer_designs_screen.md`, line 186. | Unassessed; see final question | Unassigned; see final question | Open |
| 90 | [NEEDS CLARIFICATION: S17, Footer LinkedIn icon: external or in-system destination] Source: `screens/S17-customer_designs_screen.md`, line 187. | Unassessed; see final question | Unassigned; see final question | Open |
| 91 | [NEEDS CLARIFICATION: S17, Footer YouTube icon: external or in-system destination] Source: `screens/S17-customer_designs_screen.md`, line 188. | Unassessed; see final question | Unassigned; see final question | Open |
| 92 | [NEEDS CLARIFICATION: S17, Footer TikTok icon: external or in-system destination] Source: `screens/S17-customer_designs_screen.md`, line 189. | Unassessed; see final question | Unassigned; see final question | Open |
| 93 | [NEEDS CLARIFICATION: S17, Company profile link: external or in-system destination] Source: `screens/S17-customer_designs_screen.md`, line 190. | Unassessed; see final question | Unassigned; see final question | Open |
| 94 | [NEEDS CLARIFICATION: S17, Quality policy link: external or in-system destination] Source: `screens/S17-customer_designs_screen.md`, line 191. | Unassessed; see final question | Unassigned; see final question | Open |
| 95 | [NEEDS CLARIFICATION: S17, Warranty policy link: external or in-system destination] Source: `screens/S17-customer_designs_screen.md`, line 192. | Unassessed; see final question | Unassigned; see final question | Open |
| 96 | [NEEDS CLARIFICATION: S17, Delivery and return policy link: external or in-system destination] Source: `screens/S17-customer_designs_screen.md`, line 193. | Unassessed; see final question | Unassigned; see final question | Open |
| 97 | [NEEDS CLARIFICATION: S17, Second warranty policy link: external or in-system destination] Source: `screens/S17-customer_designs_screen.md`, line 194. | Unassessed; see final question | Unassigned; see final question | Open |
| 98 | [NEEDS CLARIFICATION: S17, Shipping policy link: external or in-system destination] Source: `screens/S17-customer_designs_screen.md`, line 195. | Unassessed; see final question | Unassigned; see final question | Open |
| 99 | [NEEDS CLARIFICATION: S17, Payment methods link: external or in-system destination] Source: `screens/S17-customer_designs_screen.md`, line 196. | Unassessed; see final question | Unassigned; see final question | Open |
| 100 | [NEEDS CLARIFICATION: S17, Business areas link: external or in-system destination] Source: `screens/S17-customer_designs_screen.md`, line 197. | Unassessed; see final question | Unassigned; see final question | Open |
| 101 | [NEEDS CLARIFICATION: S17, FAQ link: external or in-system destination] Source: `screens/S17-customer_designs_screen.md`, line 198. | Unassessed; see final question | Unassigned; see final question | Open |
| 102 | [NEEDS CLARIFICATION: S17, - Smallest supported width: [NEEDS CLARIFICATION: not specified in sources.]: not specified in sources.] Source: `screens/S17-customer_designs_screen.md`, line 214. | Unassessed; see final question | Unassigned; see final question | Open |
| 103 | [NEEDS CLARIFICATION: S17, - What collapses or stacks on a narrow screen: [NEEDS CLARIFICATION: no narrow-screen mock: no narrow-screen mockup or rule provided.] Source: `screens/S17-customer_designs_screen.md`, line 216. | Unassessed; see final question | Unassigned; see final question | Open |
| 104 | [NEEDS CLARIFICATION: S17, - Text that must remain readable (contrast, minimum size): [NEEDS CLARIFICATION: no numeri: no numeric accessibility criteria provided.] Source: `screens/S17-customer_designs_screen.md`, line 218. | Unassessed; see final question | Unassigned; see final question | Open |
| 105 | [NEEDS CLARIFICATION: S17, [NEEDS CLARIFICATION: Screen List does not provide Must / Should / Could priority.]: Screen List does not provide Must / Should / Could priority.] Source: `screens/S17-customer_designs_screen.md`, line 224. | Unassessed; see final question | Unassigned; see final question | Open |
| 106 | [NEEDS CLARIFICATION: S17, [NEEDS CLARIFICATION: smallest supported width, narrow layout, and accessibility minimums are not specified.]: smallest supported width, narrow layout, and accessibility minimums are not specified.] Source: `screens/S17-customer_designs_screen.md`, line 226. | Unassessed; see final question | Unassigned; see final question | Open |
| 107 | [NEEDS CLARIFICATION: S17, [NEEDS CLARIFICATION: Are consultant-provided designs distinguished visually from self-designed designs?]: Are consultant-provided designs distinguished visually from self-designed designs?] Source: `screens/S17-customer_designs_screen.md`, line 227. | Unassessed; see final question | Unassigned; see final question | Open |
| 108 | [NEEDS CLARIFICATION: S17, [NEEDS CLARIFICATION: mockup file uses a descriptive suffix; template assumes img/<SCREEN-ID>.png.]: mockup file uses a descriptive suffix; template assumes img/<SCREEN-ID>.png.] Source: `screens/S17-customer_designs_screen.md`, line 228. | Unassessed; see final question | Unassigned; see final question | Open |
| 109 | [NEEDS CLARIFICATION: S17, - [ ] The mockup is a separate cropped image file, named with the Screen ID. [NEEDS CLARIF: actual image filenames include descriptive suffixes.] Source: `screens/S17-customer_designs_screen.md`, line 234. | Unassessed; see final question | Unassigned; see final question | Open |
| 110 | [NEEDS CLARIFICATION: No Session 3 Clarify meeting notes are supplied; carry over all unresolved decisions once provided.] | Unassessed; see final question | Unassigned; see final question | Open |
| 111 | [NEEDS CLARIFICATION: Original spreadsheet cells and figure numbers are unavailable; the traceability below uses exact supplied Markdown lines and the PDF page/section instead.] | Unassessed; see final question | Unassigned; see final question | Open |
| 112 | [NEEDS CLARIFICATION: Mermaid rendering has not been verified with a Mermaid renderer; source copying and node/edge checks alone do not establish rendering correctness.] | Unassessed; see final question | Unassigned; see final question | Open |
| 113 | [NEEDS CLARIFICATION: Open-question owners and blocking impacts have not been assigned.] | Unassessed; see final question | Unassigned; see final question | Open |

## 11. Traceability to DBIZ2

| Spec section | DBIZ2 source | Location |
| --- | --- | --- |
| 1. Purpose / scope | Function List module heading and all module rows; objective reproduced in Session 1 scope | `docs/function-list.md`, lines 69-77; `MVP_Score-WeaveLink.docx.pdf`, page 1 section 3 and page 2 section 4 |
| 2. Actors | Function List Actor column | `docs/function-list.md`, lines 70-77 |
| 4.1 Usage flow | Supplied customer usage flow | No module path exists in the supplied customer flow; see section 4.1 |
| 8. Success criteria / 9. Assumptions | Available scope document | `MVP_Score-WeaveLink.docx.pdf`, page 1 sections 1-3 and page 2 section 4; no measurable acceptance target or Session 3 document supplied |
| 3. US-1 | Use Case “View assignment” (UC-S01) | `docs/architecture/use-case.md`, line 26 |
| 3. US-2 | Use Case “Update customer consultation” (UC-S02) | `docs/architecture/use-case.md`, line 27 |
| 3. US-3 | Use Case “Assign consultant” (UC-C19) | `docs/architecture/use-case.md`, line 36 |
| 4.2 Sequence | No module sequence supplied | `docs/architecture/sequence.md` contains SD-01 through SD-09 only; none documents this module |
| 5 / 5.1 / 6: FR-001 | `MFG-08` / `F-ORD-001` / Assign Consultant; US-3: Assign consultant | `docs/function-list.md`, line 70, No. 60; Screens: S18, S19; sequence: this behavior is not separately shown in a supplied sequence; Usage Flow: this behavior is not separately shown in the supplied usage flow. Diagrams support only the steps actually shown; the full contract remains sourced to the Function List. |
| 5 / 5.1 / 6: FR-002 | `MFG-08` / `F-ORD-002` / Assign Consultant; US-3: Assign consultant | `docs/function-list.md`, line 71, No. 61; Screens: S19; sequence: this behavior is not separately shown in a supplied sequence; Usage Flow: this behavior is not separately shown in the supplied usage flow. Diagrams support only the steps actually shown; the full contract remains sourced to the Function List. |
| 5 / 5.1 / 6: FR-003 | `MFG-08` / `F-ORD-003` / Assign Consultant; US-3: Assign consultant | `docs/function-list.md`, line 72, No. 62; Screens: S19; sequence: this behavior is not separately shown in a supplied sequence; Usage Flow: this behavior is not separately shown in the supplied usage flow. Diagrams support only the steps actually shown; the full contract remains sourced to the Function List. |
| 5 / 5.1 / 6: FR-004 | `MFG-08` / `F-ORD-004` / Assign Consultant; US-3: Assign consultant | `docs/function-list.md`, line 73, No. 63; Screens: S19; sequence: this behavior is not separately shown in a supplied sequence; Usage Flow: this behavior is not separately shown in the supplied usage flow. Diagrams support only the steps actually shown; the full contract remains sourced to the Function List. |
| 5 / 5.1 / 6: FR-005 | `MFG-08` / `F-ORD-005` / View Assignment; US-1: View assignment | `docs/function-list.md`, line 74, No. 64; Screens: S20; sequence: this behavior is not separately shown in a supplied sequence; Usage Flow: this behavior is not separately shown in the supplied usage flow. Diagrams support only the steps actually shown; the full contract remains sourced to the Function List. |
| 5 / 5.1 / 6: FR-006 | `MFG-08` / `F-ORD-006` / View Assignment; US-1: View assignment | `docs/function-list.md`, line 75, No. 65; Screens: S21; sequence: this behavior is not separately shown in a supplied sequence; Usage Flow: this behavior is not separately shown in the supplied usage flow. Diagrams support only the steps actually shown; the full contract remains sourced to the Function List. |
| 5 / 5.1 / 6: FR-007 | `MFG-08` / `F-ORD-007` / Update Consult; US-2: Update customer consultation | `docs/function-list.md`, line 76, No. 66; Screens: S21; sequence: this behavior is not separately shown in a supplied sequence; Usage Flow: this behavior is not separately shown in the supplied usage flow. Diagrams support only the steps actually shown; the full contract remains sourced to the Function List. |
| 5 / 5.1 / 6: FR-008 | `MFG-08` / `F-ORD-008` / Update Consult; US-2: Update customer consultation | `docs/function-list.md`, line 77, No. 67; Screens: S21; sequence: this behavior is not separately shown in a supplied sequence; Usage Flow: this behavior is not separately shown in the supplied usage flow. Diagrams support only the steps actually shown; the full contract remains sourced to the Function List. |
| 5.2 BR-001 | Explicit source rule | F-ORD-003 and F-ORD-004 within MFG-08; the recipient input is consultant_email. |
| 7. S17 | Customer Designs Screen | `docs/screen-list.md`, line 19; `screens/S17-customer_designs_screen.md`, sections 1, 3-7 and 9 |
| 7. S18 | Consultation Request List Screen (Company Admin) | `docs/screen-list.md`, line 20; Screen Spec not supplied |
| 7. S19 | Consultation Assignment Screen | `docs/screen-list.md`, line 21; Screen Spec not supplied |
| 7. S20 | Consultant Task List Screen | `docs/screen-list.md`, line 22; Screen Spec not supplied |
| 7. S21 | Consultation Detail Screen (Consultant) | `docs/screen-list.md`, line 23; Screen Spec not supplied |

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
