# Spec Document: Data Analytics


| Field | Value |
| --- | --- |
| Module ID | `MFG-11` |
| Module name | Data Analytics |
| Spec version | v0.1 |
| Author (team member) | [NEEDS CLARIFICATION: Specify the responsible team member; Group B is named only as the team on the Session 1 scope sheet.] |
| Date | 2026-09-16 |
| Status | Draft |
| Approved by (Client role) | [NEEDS CLARIFICATION: Client approver role and approval are not supplied.] |
| DBIZ2 source | Function List `MFG-11`, No. 84-86, `F-DA-001` .. `F-DA-003`; Use Cases: View dashboard; Export data; Data Analytics; Use Case IDs: UC-C21, UC-C22, UC-C20; Screens: [NEEDS CLARIFICATION: No matching Screen IDs are supplied.] |


---

## 1. Purpose and scope (mandatory)

Company administrators can view revenue, order, and customer-growth information. They can filter this information and export a report for further use.

Source: [docs/function-list.md](../docs/function-list.md), `MFG-11` (No. 84-86); Session 1 MVP PDF, page 1 section 3. [NEEDS CLARIFICATION: Original DBIZ2 Schematic 1.1/1.2 cells are unavailable; the PDF reproduces the project objective but is not Session 3 MVP Scope v3.]

**In scope**

- View Dashboard
- Export Data

Session 1 marks analytics and data export as Won't for this MVP; the DBIZ2 scope is retained for traceability only. All DBIZ2 subfunctions below are retained as documentation; this does not authorize release of deferred functions. [NEEDS CLARIFICATION: Supply MVP Scope v3 and Session 3 decisions to confirm current module scope.]

**Out of scope**

- Changing orders is specified in MFG-07, rather than the analytics subfunctions.

**Depends on**

- MFG-06/MFG-07: order information underlies the analytics overview; system-configuration.md shows BusinessData feeding AggregatedData. [NEEDS CLARIFICATION: The precise source fields and module interfaces for analytics are not supplied.]

## 2. Actors (mandatory)

| Actor | Role in this module | Where it comes from |
| --- | --- | --- |
| Company Admin | Primary — View Dashboard, Export Data | Function List `Actor` column, `MFG-11`: F-DA-001, F-DA-002, F-DA-003 |

Primary identifies the actor performing the listed subfunctions; it does not replace conflicting Use Case or sequence labels. External participants appear in section 4 only when supplied by the source.

## 3. User scenarios and acceptance criteria (mandatory)

[NEEDS CLARIFICATION: P1/P2 scenario ordering is not agreed in the supplied materials; no scenario priority is inferred from Function List High/Medium/Low.]

### US-1 ([NEEDS CLARIFICATION: Scenario priority not agreed.]): View dashboard

**Journey.** As a `Company Admin`, I want to `view dashboard`, so that [NEEDS CLARIFICATION: The Use Case names the goal but does not state a separate scenario benefit.].

Source: `docs/architecture/use-case.md`, line 37, “View dashboard”; related FRs `FR-001` / `F-DA-001`, `FR-002` / `F-DA-002`. Actor association in the Use Case: [NEEDS CLARIFICATION: no direct actor association shown].

[NEEDS CLARIFICATION: No detailed Usage Flow or sequence for this use case is supplied; the criterion records the named goal and any explicitly cited Function List outcome. Confirm preconditions, action sequence and failure behavior before treating it as an agreed acceptance test.]

**Acceptance scenarios**

1. **Given** the company administrator is using Data Analytics, **When** the administrator views the dashboard, **Then** the dashboard is displayed.

### US-2 ([NEEDS CLARIFICATION: Scenario priority not agreed.]): Export data

**Journey.** As a `Company Admin`, I want to `export data`, so that [NEEDS CLARIFICATION: The Use Case names the goal but does not state a separate scenario benefit.].

Source: `docs/architecture/use-case.md`, line 38, “Export data”; related FRs `FR-003` / `F-DA-003`. Actor association in the Use Case: [NEEDS CLARIFICATION: no direct actor association shown].

[NEEDS CLARIFICATION: No detailed Usage Flow or sequence for this use case is supplied; the criterion records the named goal and any explicitly cited Function List outcome. Confirm preconditions, action sequence and failure behavior before treating it as an agreed acceptance test.]

**Acceptance scenarios**

1. **Given** the company administrator is using Data Analytics, **When** the administrator exports data, **Then** a downloadable Excel or CSV report is available (F-DA-003).

### US-3 ([NEEDS CLARIFICATION: Scenario priority not agreed.]): Data Analytics

**Journey.** As a `Company Admin`, I want to `data analytics`, so that [NEEDS CLARIFICATION: The Use Case names the goal but does not state a separate scenario benefit.].

Source: `docs/architecture/use-case.md`, line 39, “Data Analytics”; related FRs `FR-001` / `F-DA-001`, `FR-002` / `F-DA-002`, `FR-003` / `F-DA-003`.

[NEEDS CLARIFICATION: No detailed Usage Flow or sequence for this use case is supplied; the criterion records the named goal and any explicitly cited Function List outcome. Confirm preconditions, action sequence and failure behavior before treating it as an agreed acceptance test.]

**Acceptance scenarios**

1. **Given** the company administrator is using Data Analytics, **When** the administrator selects an analytics action, **Then** View dashboard or Export data is entered.

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

One FR per original Function List subfunction, in source order. FR IDs are local to this module; cite `MFG-11/FR-nnn` with the unchanged Subfunction ID. Original function names and High/Medium/Low values are preserved in each requirement note. MoSCoW values are used only for capabilities explicitly prioritized on page 2 of the Session 1 PDF; [NEEDS CLARIFICATION: Confirm per-subfunction priority mapping and the current Session 3 release scope.]

| FR ID | DBIZ2 Subfunction ID | Requirement (system MUST ...) | Actor | Priority |
| --- | --- | --- | --- | --- |
| FR-001 | F-DA-001 | The system MUST display statistical charts regarding revenue, orders, and customer growth.<br/>DBIZ2 function: View Dashboard; subfunction: Charts View; category: Screen; original priority: Medium. | Company Admin | [NEEDS CLARIFICATION: Outside MVP (Session 1 Won't); no Must/Should/Could implementation priority is agreed.] |
| FR-002 | F-DA-002 | The system MUST apply time or product filters to update the chart data accordingly.<br/>DBIZ2 function: View Dashboard; subfunction: Filter Logic; category: Process; original priority: Medium. | Company Admin | [NEEDS CLARIFICATION: Outside MVP (Session 1 Won't); no Must/Should/Could implementation priority is agreed.] |
| FR-003 | F-DA-003 | The system MUST process data and generate a downloadable report file in Excel or CSV format.<br/>DBIZ2 function: Export Data; subfunction: Export Exec Logic; category: Process; original priority: Medium. | Company Admin | [NEEDS CLARIFICATION: Outside MVP (Session 1 Won't); no Must/Should/Could implementation priority is agreed.] |

### 5.1 Input / Output contract

Literal Function List field names, types and required flags are preserved. Input and output rows are separate to avoid inventing field-to-field pairings. The template Required column applies to inputs; output required flags appear in Notes / validation. `—` means that side of this row is not applicable, not that a source field was omitted. Object contents, validation ranges and identifier formats are not inferred. [NEEDS CLARIFICATION: Supply nested Object/JSON/Array schemas and field validation where absent; apparent source type errors remain unchanged until clarified.]

| FR ID | Input field | Type | Required | Output field | Type | Notes / validation |
| --- | --- | --- | --- | --- | --- | --- |
| FR-001 | `date_range` | DateTime | No | — | — | Function List No. 84, F-DA-001, Input column. |
| FR-001 | `metric_type` | String | No | — | — | Function List No. 84, F-DA-001, Input column. |
| FR-001 | — | — | — | `visual_charts` | [NEEDS CLARIFICATION: F-DA-001 output visual_charts: data type.] | Output required: Yes. Function List No. 84, F-DA-001, Output column. |
| FR-002 | `filter_parameters` | Object | No | — | — | Function List No. 85, F-DA-002, Input column. |
| FR-002 | — | — | — | `refreshed_dataset_for_charts` | [NEEDS CLARIFICATION: F-DA-002 output refreshed_dataset_for_charts: data type.] | Output required: Yes. Function List No. 85, F-DA-002, Output column. |
| FR-003 | `dataset_selection` | [NEEDS CLARIFICATION: F-DA-003 input dataset_selection: data type.] | Yes | — | — | Function List No. 86, F-DA-003, Input column. |
| FR-003 | `file_format` | File | Yes | — | — | Function List No. 86, F-DA-003, Input column. |
| FR-003 | — | — | — | `downloadable_file_url` | URL | Output required: Yes. Function List No. 86, F-DA-003, Output column. |

### 5.2 Business rules

| Rule ID | Rule | Why it exists |
| --- | --- | --- |
| BR-001 | Report exports support Excel or CSV format. | F-DA-003 explicitly limits the described export formats to these two. Business rationale beyond the stated source is not separately documented. |

## 6. Key entities (mandatory)

| Entity | Attributes (from Input/Output fields) | Relationships |
| --- | --- | --- |
| Analytics selection/result | `date_range`, `metric_type`, `filter_parameters`, `visual_charts`, `refreshed_dataset_for_charts` | [NEEDS CLARIFICATION: Analytics selection/result: relationship cardinalities and nested field ownership are not specified in the Input/Output contract.] |
| Export | `dataset_selection`, `file_format`, `downloadable_file_url` | [NEEDS CLARIFICATION: Export: relationship cardinalities and nested field ownership are not specified in the Input/Output contract.] |

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

- No separate module assumption is explicitly documented in the supplied sources. No assumption has been added to fill missing requirements.

## 10. Open questions

| # | Question | Blocking? | Owner | Status |
| --- | --- | --- | --- | --- |
| 1 | [NEEDS CLARIFICATION: Specify the responsible team member; Group B is named only as the team on the Session 1 scope sheet.] | Unassessed; see final question | Unassigned; see final question | Open |
| 2 | [NEEDS CLARIFICATION: Client approver role and approval are not supplied.] | Unassessed; see final question | Unassigned; see final question | Open |
| 3 | Use Case IDs: UC-C21, UC-C22, UC-C20 | Unassessed; see final question | Unassigned; see final question | Open |
| 4 | [NEEDS CLARIFICATION: No matching Screen IDs are supplied.] | Unassessed; see final question | Unassigned; see final question | Open |
| 5 | [NEEDS CLARIFICATION: Original DBIZ2 Schematic 1.1/1.2 cells are unavailable; the PDF reproduces the project objective but is not Session 3 MVP Scope v3.] | Unassessed; see final question | Unassigned; see final question | Open |
| 6 | [NEEDS CLARIFICATION: Supply MVP Scope v3 and Session 3 decisions to confirm current module scope.] | Unassessed; see final question | Unassigned; see final question | Open |
| 7 | [NEEDS CLARIFICATION: The precise source fields and module interfaces for analytics are not supplied.] | Unassessed; see final question | Unassigned; see final question | Open |
| 8 | [NEEDS CLARIFICATION: P1/P2 scenario ordering is not agreed in the supplied materials; no scenario priority is inferred from Function List High/Medium/Low.] | Unassessed; see final question | Unassigned; see final question | Open |
| 9 | [NEEDS CLARIFICATION: Scenario priority not agreed.] | Unassessed; see final question | Unassigned; see final question | Open |
| 10 | [NEEDS CLARIFICATION: The Use Case names the goal but does not state a separate scenario benefit.] | Unassessed; see final question | Unassigned; see final question | Open |
| 11 | [NEEDS CLARIFICATION: no direct actor association shown] | Unassessed; see final question | Unassigned; see final question | Open |
| 12 | [NEEDS CLARIFICATION: No detailed Usage Flow or sequence for this use case is supplied; the criterion records the named goal and any explicitly cited Function List outcome. Confirm preconditions, action sequence and failure behavior before treating it as an agreed acceptance test.] | Unassessed; see final question | Unassigned; see final question | Open |
| 13 | [NEEDS CLARIFICATION: Document missing/invalid inputs and empty-data outcomes not already covered by the supplied screens or sequences.] | Unassessed; see final question | Unassigned; see final question | Open |
| 14 | [NEEDS CLARIFICATION: Document behavior when a required external service or data operation is unavailable; do not infer retries or fallback paths.] | Unassessed; see final question | Unassigned; see final question | Open |
| 15 | [NEEDS CLARIFICATION: Document repeated actions and simultaneous-user outcomes; no concurrency or duplicate-submission rule is supplied.] | Unassessed; see final question | Unassigned; see final question | Open |
| 16 | [NEEDS CLARIFICATION: The supplied overall customer Usage Flow does not show this module; supply the relevant original Mermaid/figure. No flow is invented.] | Unassessed; see final question | Unassigned; see final question | Open |
| 17 | [NEEDS CLARIFICATION: No sequence diagram for this module is supplied; participants and messages cannot be reconstructed as requirements.] | Unassessed; see final question | Unassigned; see final question | Open |
| 18 | [NEEDS CLARIFICATION: Confirm per-subfunction priority mapping and the current Session 3 release scope.] | Unassessed; see final question | Unassigned; see final question | Open |
| 19 | [NEEDS CLARIFICATION: Outside MVP (Session 1 Won't); no Must/Should/Could implementation priority is agreed.] | Unassessed; see final question | Unassigned; see final question | Open |
| 20 | [NEEDS CLARIFICATION: Supply nested Object/JSON/Array schemas and field validation where absent; apparent source type errors remain unchanged until clarified.] | Unassessed; see final question | Unassigned; see final question | Open |
| 21 | [NEEDS CLARIFICATION: F-DA-001 output visual_charts: data type.] | Unassessed; see final question | Unassigned; see final question | Open |
| 22 | [NEEDS CLARIFICATION: F-DA-002 output refreshed_dataset_for_charts: data type.] | Unassessed; see final question | Unassigned; see final question | Open |
| 23 | [NEEDS CLARIFICATION: F-DA-003 input dataset_selection: data type.] | Unassessed; see final question | Unassigned; see final question | Open |
| 24 | [NEEDS CLARIFICATION: Analytics selection/result: relationship cardinalities and nested field ownership are not specified in the Input/Output contract.] | Unassessed; see final question | Unassigned; see final question | Open |
| 25 | [NEEDS CLARIFICATION: Export: relationship cardinalities and nested field ownership are not specified in the Input/Output contract.] | Unassessed; see final question | Unassigned; see final question | Open |
| 26 | [NEEDS CLARIFICATION: No matching module screen is identified in the Screen List.] | Unassessed; see final question | Unassigned; see final question | Open |
| 27 | [NEEDS CLARIFICATION: No agreed measurable user-outcome success criterion is present in the supplied Session 1 scope sheet or DBIZ2 extracts; provide the Session 3 criterion for this module.] | Unassessed; see final question | Unassigned; see final question | Open |
| 28 | [NEEDS CLARIFICATION: Confirm the user task, observable completion outcome, agreed target and evaluation method; none is supplied.] | Unassessed; see final question | Unassigned; see final question | Open |
| 29 | [NEEDS CLARIFICATION: No analytics/export screen IDs or screen specs are supplied; provide the existing DBIZ2 mapping.] | Unassessed; see final question | Unassigned; see final question | Open |
| 30 | [NEEDS CLARIFICATION: What are the agreed revenue, order and customer-growth definitions and filter semantics?] | Unassessed; see final question | Unassigned; see final question | Open |
| 31 | [NEEDS CLARIFICATION: F-DA-001 date_range is typed DateTime and F-DA-003 file_format is typed File; confirm these types without silently replacing them.] | Unassessed; see final question | Unassigned; see final question | Open |
| 32 | [NEEDS CLARIFICATION: No Session 3 Clarify meeting notes are supplied; carry over all unresolved decisions once provided.] | Unassessed; see final question | Unassigned; see final question | Open |
| 33 | [NEEDS CLARIFICATION: Original spreadsheet cells and figure numbers are unavailable; the traceability below uses exact supplied Markdown lines and the PDF page/section instead.] | Unassessed; see final question | Unassigned; see final question | Open |
| 34 | [NEEDS CLARIFICATION: Mermaid rendering has not been verified with a Mermaid renderer; source copying and node/edge checks alone do not establish rendering correctness.] | Unassessed; see final question | Unassigned; see final question | Open |
| 35 | [NEEDS CLARIFICATION: Open-question owners and blocking impacts have not been assigned.] | Unassessed; see final question | Unassigned; see final question | Open |

## 11. Traceability to DBIZ2

| Spec section | DBIZ2 source | Location |
| --- | --- | --- |
| 1. Purpose / scope | Function List module heading and all module rows; objective reproduced in Session 1 scope | `docs/function-list.md`, lines 96-99; `MVP_Score-WeaveLink.docx.pdf`, page 1 section 3 and page 2 section 4 |
| 2. Actors | Function List Actor column | `docs/function-list.md`, lines 97-99 |
| 4.1 Usage flow | Supplied customer usage flow | No module path exists in the supplied customer flow; see section 4.1 |
| 8. Success criteria / 9. Assumptions | Available scope document | `MVP_Score-WeaveLink.docx.pdf`, page 1 sections 1-3 and page 2 section 4; no measurable acceptance target or Session 3 document supplied |
| 3. US-1 | Use Case “View dashboard” (UC-C21) | `docs/architecture/use-case.md`, line 37 |
| 3. US-2 | Use Case “Export data” (UC-C22) | `docs/architecture/use-case.md`, line 38 |
| 3. US-3 | Use Case “Data Analytics” (UC-C20) | `docs/architecture/use-case.md`, line 39 |
| 4.2 Sequence | No module sequence supplied | `docs/architecture/sequence.md` contains SD-01 through SD-09 only; none documents this module |
| 5 / 5.1 / 6: FR-001 | `MFG-11` / `F-DA-001` / View Dashboard; US-1: View dashboard; US-3: Data Analytics | `docs/function-list.md`, line 97, No. 84; Screens: not mapped in supplied Screen List; sequence: this behavior is not separately shown in a supplied sequence; Usage Flow: this behavior is not separately shown in the supplied usage flow. Diagrams support only the steps actually shown; the full contract remains sourced to the Function List. |
| 5 / 5.1 / 6: FR-002 | `MFG-11` / `F-DA-002` / View Dashboard; US-1: View dashboard; US-3: Data Analytics | `docs/function-list.md`, line 98, No. 85; Screens: not mapped in supplied Screen List; sequence: this behavior is not separately shown in a supplied sequence; Usage Flow: this behavior is not separately shown in the supplied usage flow. Diagrams support only the steps actually shown; the full contract remains sourced to the Function List. |
| 5 / 5.1 / 6: FR-003 | `MFG-11` / `F-DA-003` / Export Data; US-2: Export data; US-3: Data Analytics | `docs/function-list.md`, line 99, No. 86; Screens: not mapped in supplied Screen List; sequence: this behavior is not separately shown in a supplied sequence; Usage Flow: this behavior is not separately shown in the supplied usage flow. Diagrams support only the steps actually shown; the full contract remains sourced to the Function List. |
| 5.2 BR-001 | Explicit source rule | F-DA-003 explicitly limits the described export formats to these two. |

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
