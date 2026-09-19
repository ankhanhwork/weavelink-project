# Function catalogue

The complete-system target contains 12 modules and 94 source function entries. All are included; implementation phases are ordering, not exclusions. The module specification linked in each section defines typed input/output contracts, validation, permissions, failures and acceptance criteria. This catalogue is the traceability index, avoiding duplicate schemas that can drift. [Shared decisions](system-decisions.md) apply to every function. Historical High/Medium/Low priorities below are retained for provenance; current phases use D12.

**Identity rule:** F-ORD IDs overlap between MFG-07 and MFG-08. Use the composite module/function key shown below. FR and US IDs are module-local. System event processors execute with verified service authority on behalf of the listed initiating actor; a customer never posts a trusted payment result.

## I. MFG-01: Identity & Access

[Canonical specification](../specs/spec-MFG-01.md) · Phase P1

| No | Use case | Canonical function key | Function | Implementation action | Category | Initiating actor | Source priority |
|---|---|---|---|---|---|---|---|
| 1 | UC-G03 | MFG-01/F-USER-001 | Register Account | Registration Screen | Screen | Guest | High |
| 2 | UC-G03 | MFG-01/F-USER-002 | Register Account | Registration Logic | Process | Guest | High |
| 3 | UC-G03 | MFG-01/F-USER-003 | Register Account | Send email verification link | Process | Guest | High |
| 4 | UC-M01 | MFG-01/F-USER-004 | Log In | Login Screen | Screen | Guest | High |
| 5 | UC-M01 | MFG-01/F-USER-005 | Log In | Authentication Logic | Process | Guest | High |
| 6 | UC-M04 | MFG-01/F-USER-006 | Log Out | Logout Logic | Process | Member | Low |
| 7 | UC-M02 | MFG-01/F-USER-007 | Forgot Password | Forgot Password Screen | Screen | Guest | High |
| 8 | UC-M02 | MFG-01/F-USER-008 | Forgot Password | Identity Validation | Process | Guest | High |
| 9 | UC-M02 | MFG-01/F-USER-009 | Forgot Password | Send password-reset email | Process | System (recovery request) | High |
| 10 | UC-M03 | MFG-01/F-USER-010 | Reset Password | Verify Token Logic | Process | Guest | High |
| 11 | UC-M03 | MFG-01/F-USER-011 | Reset Password | Update Password Logic | Process | Guest | High |

## II. MFG-02: Profile & Settings

[Canonical specification](../specs/spec-MFG-02.md) · Phase P2

| No | Use case | Canonical function key | Function | Implementation action | Category | Initiating actor | Source priority |
|---|---|---|---|---|---|---|---|
| 12 | UC-M05 | MFG-02/F-PROF-001 | View Profile | Profile View | Screen | Member | Medium |
| 13 | UC-M07 | MFG-02/F-PROF-002 | Edit Profile | Edit Profile Form | Screen | Member | Medium |
| 14 | UC-M07 | MFG-02/F-PROF-003 | Edit Profile | Save Profile Logic | Process | Member | Medium |
| 15 | UC-M08 | MFG-02/F-PROF-004 | Change Password | Change Password Form | Screen | Member | Low |
| 16 | UC-M08 | MFG-02/F-PROF-005 | Change Password | Save Password Logic | Process | Member | Low |

## III. MFG-03: Company Accounts

[Canonical specification](../specs/spec-MFG-03.md) · Phase P2

| No | Use case | Canonical function key | Function | Implementation action | Category | Initiating actor | Source priority |
|---|---|---|---|---|---|---|---|
| 17 | UC-S06 | MFG-03/F-ACC-001 | Add Account | Account List View | Screen | System Admin | High |
| 18 | UC-S06 | MFG-03/F-ACC-002 | Add Account | Add Account Form | Screen | System Admin | High |
| 19 | UC-S06 | MFG-03/F-ACC-003 | Add Account | Generate staff invitation | Process | System Admin | High |
| 20 | UC-S06 | MFG-03/F-ACC-004 | Add Account | Save Account Logic | Process | System Admin | High |
| 21 | UC-S07 | MFG-03/F-ACC-005 | Update Account | Account Detail View | Screen | System Admin | Medium |
| 22 | UC-S07 | MFG-03/F-ACC-006 | Update Account | Update Account Logic | Process | System Admin | Medium |
| 23 | UC-S08 | MFG-03/F-ACC-007 | Delete Account | Confirm Delete UI | Screen | System Admin | Low |
| 24 | UC-S08 | MFG-03/F-ACC-008 | Delete Account | Soft-delete company or staff membership | Process | System Admin | Low |

## IV. MFG-04: Product Catalog

[Canonical specification](../specs/spec-MFG-04.md) · Phase P1

| No | Use case | Canonical function key | Function | Implementation action | Category | Initiating actor | Source priority |
|---|---|---|---|---|---|---|---|
| 25 | UC-G01 | MFG-04/F-PROD-001 | View Catalog | Catalog Grid View | Screen | Guest | High |
| 26 | UC-G01 | MFG-04/F-PROD-002 | View Catalog | Product Detail View | Screen | Guest | High |
| 27 | UC-G02 | MFG-04/F-PROD-003 | Search Product | Search Result View | Screen | Guest | Medium |
| 28 | UC-C24 | MFG-04/F-PROD-004 | Add Product | Management Dashboard | Screen | Company Admin | Medium |
| 29 | UC-C24 | MFG-04/F-PROD-005 | Add Product | Add Product Form | Screen | Company Admin | High |
| 30 | UC-C24 | MFG-04/F-PROD-006 | Add Product | Save Product Logic | Process | Company Admin | High |
| 31 | UC-C25 | MFG-04/F-PROD-007 | Update Product | Edit Product Form | Screen | Company Admin | Medium |
| 32 | UC-C25 | MFG-04/F-PROD-008 | Update Product | Update Product Logic | Process | Company Admin | Medium |
| 33 | UC-C26 | MFG-04/F-PROD-009 | Delete Product | Delete Prompt UI | Screen | Company Admin | Low |
| 34 | UC-C26 | MFG-04/F-PROD-010 | Delete Product | Archive product | Process | Company Admin | Low |
| 35 | UC-C27 | MFG-04/F-PROD-011 | Publish Product | Publish or hide product | Screen | Company Admin | Low |

## V. MFG-05: Product Design

[Canonical specification](../specs/spec-MFG-05.md) · Phase P1

| No | Use case | Canonical function key | Function | Implementation action | Category | Initiating actor | Source priority |
|---|---|---|---|---|---|---|---|
| 36 | UC-C02 | MFG-05/F-DES-001 | Design Product | Design Workspace | Screen | Customer | High |
| 37 | UC-C02 | MFG-05/F-DES-002 | Design Product | Preview Logic | Process | Customer | High |
| 38 | UC-C02 | MFG-05/F-DES-003 | Design Product | Save Design Logic | Process | Customer | High |
| 39 | UC-C03 | MFG-05/F-DES-004 | View Designs | Saved Designs List | Screen | Customer | Medium |
| 40 | UC-C04 | MFG-05/F-DES-005 | Request Service | Request Form | Screen | Customer | Medium |
| 41 | UC-C04 | MFG-05/F-DES-006 | Request Service | Create Request Logic | Process | Customer | Medium |
| 42 | UC-C04 | MFG-05/F-DES-007 | Request Service | Apply verified SERVICE payment result | Process | Customer | High |
| 43 | UC-C04 | MFG-05/F-DES-008 | Request Service | Notify admin of paid design request | Process | Customer | Medium |
| 44 | UC-S03 | MFG-05/F-DES-009 | Send Design | Customer Select View | Screen | Sales Consultant | Medium |
| 45 | UC-S03 | MFG-05/F-DES-010 | Send Design | Push Design Logic | Process | Sales Consultant | High |
| 46 | UC-S03 | MFG-05/F-DES-011 | Send Design | Notify Customer Logic | Process | Sales Consultant | Medium |

## VI. MFG-06: Order & Payment

[Canonical specification](../specs/spec-MFG-06.md) · Phase P1

| No | Use case | Canonical function key | Function | Implementation action | Category | Initiating actor | Source priority |
|---|---|---|---|---|---|---|---|
| 47 | UC-C05 | MFG-06/F-PAY-001 | Finalize Order | Checkout View | Screen | Customer | High |
| 48 | UC-C05 | MFG-06/F-PAY-002 | Finalize Order | Order Summary View | Screen | Customer | High |
| 49 | UC-C05 | MFG-06/F-PAY-003 | Finalize Order | Create Order Logic | Process | Customer | High |
| 50 | UC-C12 | MFG-06/F-PAY-004 | Make Payment | Payment Request Gen | Process | Customer | High |
| 51 | UC-C12 | MFG-06/F-PAY-005 | Make Payment | IPN Handler Logic | Process | Customer | High |
| 52 | UC-C12 | MFG-06/F-PAY-006 | Make Payment | Receipt View | Screen | Customer | Medium |

## VII. MFG-07: Order Management

[Canonical specification](../specs/spec-MFG-07.md) · Phase P1

| No | Use case | Canonical function key | Function | Implementation action | Category | Initiating actor | Source priority |
|---|---|---|---|---|---|---|---|
| 53 | UC-C08 | MFG-07/F-ORD-001 | Track Order | Order List View | Screen | Customer | Medium |
| 54 | UC-C08 | MFG-07/F-ORD-002 | Track Order | Order Detail View | Screen | Customer | Medium |
| 55 | UC-C07 | MFG-07/F-ORD-003 | Cancel Order | Cancel eligible order and request refund if paid | Process | Customer | Medium |
| 56 | UC-C07 | MFG-07/F-ORD-004 | Cancel Order | Cancel Notify Logic | Process | Customer | Medium |
| 57 | UC-S04 | MFG-07/F-ORD-005 | Update Status | Admin Order Dashboard | Screen | Company Admin | Medium |
| 58 | UC-S04 | MFG-07/F-ORD-006 | Update Status | Status Update Logic | Process | Company Admin | High |
| 59 | UC-S04 | MFG-07/F-ORD-007 | Update Status | Status Notify Logic | Process | Company Admin | Medium |

## VIII. MFG-08: Sales Consultant

[Canonical specification](../specs/spec-MFG-08.md) · Phase P2

| No | Use case | Canonical function key | Function | Implementation action | Category | Initiating actor | Source priority |
|---|---|---|---|---|---|---|---|
| 60 | UC-C19 | MFG-08/F-ORD-001 | Assign Consultant | Unassigned Cust View | Screen | Company Admin | Medium |
| 61 | UC-C19 | MFG-08/F-ORD-002 | Assign Consultant | Customer Detail View | Screen | Company Admin | Medium |
| 62 | UC-C19 | MFG-08/F-ORD-003 | Assign Consultant | Assign Sales Logic | Process | Company Admin | Medium |
| 63 | UC-C19 | MFG-08/F-ORD-004 | Assign Consultant | Assign Notify Logic | Process | Company Admin | Low |
| 64 | UC-S01 | MFG-08/F-ORD-005 | View Assignment | Assigned Cust View | Screen | Sales Consultant | Medium |
| 65 | UC-S01 | MFG-08/F-ORD-006 | View Assignment | Context View | Screen | Sales Consultant | Medium |
| 66 | UC-S02 | MFG-08/F-ORD-007 | Update Consult | Consultation Detail | Screen | Sales Consultant | Medium |
| 67 | UC-S02 | MFG-08/F-ORD-008 | Update Consult | Update Status Logic | Process | Sales Consultant | Medium |

## IX. MFG-09: Contract Management

[Canonical specification](../specs/spec-MFG-09.md) · Phase P1

| No | Use case | Canonical function key | Function | Implementation action | Category | Initiating actor | Source priority |
|---|---|---|---|---|---|---|---|
| 68 | UC-C14 | MFG-09/F-CONTR-001 | Generate Contract | Template Select View | Screen | Company Admin | High |
| 69 | UC-C14 | MFG-09/F-CONTR-002 | Generate Contract | Template Detail View | Screen | Company Admin | High |
| 70 | UC-C14 | MFG-09/F-CONTR-003 | Generate Contract | Fill Contract Logic | Process | Company Admin | High |
| 71 | UC-C14 | MFG-09/F-CONTR-004 | Generate Contract | Render PDF Logic | Process | Company Admin | High |
| 72 | UC-C14 | MFG-09/F-CONTR-005 | Generate Contract | Ready Notify Logic | Process | Company Admin | High |
| 73 | UC-C15 | MFG-09/F-CONTR-006 | Update Contract | List contracts and manage versioned templates | Screen | Company Admin | Medium |
| 74 | UC-C15 | MFG-09/F-CONTR-007 | Update Contract | Replace unsigned contract and notify customer | Process | Company Admin | High |
| 75 | UC-C11 | MFG-09/F-CONTR-008 | Sign Contract | Record authenticated contract acknowledgement | Process | Customer | High |
| 76 | UC-C11 | MFG-09/F-CONTR-009 | Sign Contract | Signed Notify Logic | Process | Customer | High |

## X. MFG-10: Order Optimization (Merge)

[Canonical specification](../specs/spec-MFG-10.md) · Phase P2

| No | Use case | Canonical function key | Function | Implementation action | Category | Initiating actor | Source priority |
|---|---|---|---|---|---|---|---|
| 77 | UC-C06 | MFG-10/F-MER-001 | Select Merge | Merge Option View | Screen | Customer | Medium |
| 78 | UC-C06 | MFG-10/F-MER-002 | Select Merge | Merge Terms View | Screen | Customer | Low |
| 79 | UC-C06 | MFG-10/F-MER-003 | Select Merge | Save Preference Logic | Process | Customer | Medium |
| 80 | UC-C17 | MFG-10/F-MER-004 | View Eligible | Merge Console View | Screen | Company Admin | High |
| 81 | UC-C17 | MFG-10/F-MER-005 | View Eligible | Estimate setup savings and setup time saved | Process | Company Admin | High |
| 82 | UC-C18 | MFG-10/F-MER-006 | Confirm Merge | Batch Exec Logic | Process | Company Admin | High |
| 83 | UC-C18 | MFG-10/F-MER-007 | Confirm Merge | Merge Notify Logic | Process | Company Admin | Medium |

## XI. MFG-11: Data Analytics

[Canonical specification](../specs/spec-MFG-11.md) · Phase P3

| No | Use case | Canonical function key | Function | Implementation action | Category | Initiating actor | Source priority |
|---|---|---|---|---|---|---|---|
| 84 | UC-C21 | MFG-11/F-DA-001 | View Dashboard | Charts View | Screen | Company Admin | Medium |
| 85 | UC-C21 | MFG-11/F-DA-002 | View Dashboard | Filter Logic | Process | Company Admin | Medium |
| 86 | UC-C22 | MFG-11/F-DA-003 | Export Data | Export Exec Logic | Process | Company Admin | Medium |

## XII. MFG-12: System Operations

[Canonical specification](../specs/spec-MFG-12.md) · Phase P3

| No | Use case | Canonical function key | Function | Implementation action | Category | Initiating actor | Source priority |
|---|---|---|---|---|---|---|---|
| 87 | UC-S09 | MFG-12/F-SYS-001 | System Logs | Log List View | Screen | System Admin | Low |
| 88 | UC-S09 | MFG-12/F-SYS-002 | System Logs | Search Log View | Screen | System Admin | Low |
| 89 | UC-S10 | MFG-12/F-SYS-003 | Backup Data | Backup Option View | Screen | System Admin | Medium |
| 90 | UC-S10 | MFG-12/F-SYS-004 | Backup Data | Backup Exec Logic | Process | System Admin | High |
| 91 | UC-S10 | MFG-12/F-SYS-005 | Restore Data | Restore Exec Logic | Process | System Admin | High |
| 92 | UC-S11 | MFG-12/F-SYS-006 | Config System | Settings Form | Screen | System Admin | Medium |
| 93 | UC-S11 | MFG-12/F-SYS-007 | Config System | Save Config Logic | Process | System Admin | High |
| 94 | UC-S11 | MFG-12/F-SYS-008 | Config System | Config Notify Logic | Process | System Admin | Low |

## Cross-cutting extensions

Email verification consumption belongs to MFG-01/F-USER-003; design-rule editing to MFG-04/F-PROD-007 and F-PROD-008; payment reconciliation/refunds to MFG-06/F-PAY-005 and MFG-07/F-ORD-003; notification inbox/read state to the existing notification-producing functions plus the shared outbox (S38); account invitations and company/staff lifecycle to MFG-03/F-ACC-001..008 (S41); batch dissolve/start/fallback to MFG-10/F-MER-006 (S42). These complete source functions without inventing colliding IDs.
