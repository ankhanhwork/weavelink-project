# Screen Spec: S18 Consultation Requests and Customers (Retired)

| Field | Value |
|---|---|
| Screen ID | `S18` |
| Screen name | Consultation Requests and Customers |
| Actor | Sales Admin |
| Priority | P2 |
| Belongs to module | [MFG-05](../specs/spec-MFG-05.md) |
| Route | Former `/admin/consultations?tab=requests,customers`; resolve to the authorized S19 lead/request panel; see S19 section 10. |
| Mockup image | img/S18-consultation_requests_and_customers_screen.png (historical) |
| Status | **Retired 2026-09-27 — merged into [S19 Sales Pipeline](S19-consultation_assignment_screen.md)** (decision D-06). Do not implement as a separate screen. |

## 1. Retirement note

S18 is no longer a separate screen. Every function it specified is kept and moved to the Admin side of S19, with the existing MFG-05 rules unchanged (Simple/Complex, rationale, `design_fee_vnd`, customer fee acceptance, reject reason). The earlier content of this file remains available in the repository history.

## 2. Where each S18 function now lives

| Former S18 element | New location | Change |
|---|---|---|
| Requests tab (request list, status, product, customer, requested deadline, committed due) | S19 Board/List with the filters **Design request awaiting assessment** and **Committed due date missing**; request details in the lead detail panel (Design Consultation Summary) | Requests are found through their lead. |
| Customers tab (CRM context) | S19 List view and lead detail panel | Replaced by the Sales Pipeline. |
| Start review (Submitted → UnderReview) | S19 section 3.11, design service assessment | Unchanged rule. |
| Complexity, rationale, fee (Simple → Approved fee 0; Complex → FeeProposed) and Complete assessment | S19 section 3.11 | Unchanged rule. |
| Reject request with customer-visible reason | S19 section 3.11 | Unchanged rule. |
| Assign approved request (to an active Sales, with `committed_due_at`) | Automatic assignment to the current lead owner when the request is eligible; `committed_due_at` set or changed by the Sales Admin in S19 section 3.11 | No manual design-owner selection (D-04). |
| Open request detail | S19 lead detail panel; design work in S21 Design Workspace | — |

## Completion checklist

- [x] Every former S18 function is mapped to its new location.
- [x] Target route resolution and related documentation links are specified in S19 section 10.
