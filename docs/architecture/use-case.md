# Use-case catalogue

All 49 inherited UC identifiers remain stable. Actor assignments below are explicit implementation decisions under [D01](../system-decisions.md), replacing indirect/ambiguous diagram associations. Login and password recovery are entered while unauthenticated; Member denotes the authenticated role union. The full actor name, not the UC initial, determines permissions.

| Use case ID | Goal | Primary actor | Other actor / relationship | Canonical functions |
|---|---|---|---|---|
| UC-G01 | View product catalog | Guest | None | MFG-04/F-PROD-001, MFG-04/F-PROD-002 |
| UC-G02 | Search products | Guest | None | MFG-04/F-PROD-003 |
| UC-G03 | Register account | Guest | None | MFG-01/F-USER-001, MFG-01/F-USER-002, MFG-01/F-USER-003 |
| UC-M01 | Log in | Guest | None | MFG-01/F-USER-004, MFG-01/F-USER-005 |
| UC-M02 | Forgot password | Guest | None | MFG-01/F-USER-007, MFG-01/F-USER-008, MFG-01/F-USER-009 |
| UC-M03 | Reset password | Guest | None | MFG-01/F-USER-010, MFG-01/F-USER-011 |
| UC-M04 | Log out | Member | None | MFG-01/F-USER-006 |
| UC-M05 | View Profile | Member | None | MFG-02/F-PROF-001 |
| UC-M06 | Manage profile | Member | UC-M05, UC-M07, UC-M08 | MFG-02/F-PROF-001, MFG-02/F-PROF-002, MFG-02/F-PROF-003, MFG-02/F-PROF-004, MFG-02/F-PROF-005 |
| UC-M07 | Edit Profile | Member | None | MFG-02/F-PROF-002, MFG-02/F-PROF-003 |
| UC-M08 | Change password | Member | None | MFG-02/F-PROF-004, MFG-02/F-PROF-005 |
| UC-C01 | Design product | Customer | UC-C02 | MFG-05/F-DES-001, MFG-05/F-DES-002, MFG-05/F-DES-003 |
| UC-C02 | Product Customization | Customer | Includes UC-C01, UC-C03, UC-C04 | MFG-05/F-DES-001, MFG-05/F-DES-002, MFG-05/F-DES-003 |
| UC-C03 | View saved design | Customer | None | MFG-05/F-DES-004 |
| UC-C04 | Request design service | Customer | None | MFG-05/F-DES-005, MFG-05/F-DES-006, MFG-05/F-DES-007, MFG-05/F-DES-008 |
| UC-C05 | Finalize order | Customer | None | MFG-06/F-PAY-001, MFG-06/F-PAY-002, MFG-06/F-PAY-003 |
| UC-C06 | Choose merge option | Customer | None | MFG-10/F-MER-001, MFG-10/F-MER-002, MFG-10/F-MER-003 |
| UC-C07 | Cancel order | Customer | None | MFG-07/F-ORD-003, MFG-07/F-ORD-004 |
| UC-C08 | Track order status | Customer | None | MFG-07/F-ORD-001, MFG-07/F-ORD-002 |
| UC-C10 | View contract | Customer | UC-C11 | MFG-09/F-CONTR-008, MFG-09/F-CONTR-009 |
| UC-C09 | View/Sign contract | Customer | UC-C10, UC-C11 | MFG-09/F-CONTR-008, MFG-09/F-CONTR-009 |
| UC-C11 | Sign contract | Customer | None | MFG-09/F-CONTR-008, MFG-09/F-CONTR-009 |
| UC-C12 | Make payment | Customer | None | MFG-06/F-PAY-004, MFG-06/F-PAY-005, MFG-06/F-PAY-006 |
| UC-S01 | View assignment | Sales Consultant | None | MFG-08/F-ORD-005, MFG-08/F-ORD-006 |
| UC-S02 | Update customer consultation | Sales Consultant | None | MFG-08/F-ORD-007, MFG-08/F-ORD-008 |
| UC-S03 | Send design to customer | Sales Consultant | None | MFG-05/F-DES-009, MFG-05/F-DES-010, MFG-05/F-DES-011 |
| UC-S04 | Update order status | Sales Consultant | Company Admin (same-company fulfillment) | MFG-07/F-ORD-005, MFG-07/F-ORD-006, MFG-07/F-ORD-007 |
| UC-C14 | Generate contracts | Company Admin | None | MFG-09/F-CONTR-001, MFG-09/F-CONTR-002, MFG-09/F-CONTR-003, MFG-09/F-CONTR-004, MFG-09/F-CONTR-005 |
| UC-C15 | Manage contract templates and unsigned revisions | Company Admin | None | MFG-09/F-CONTR-006, MFG-09/F-CONTR-007 |
| UC-C13 | Manage company contracts | Company Admin | UC-C14, UC-C15 | MFG-09/F-CONTR-001, MFG-09/F-CONTR-002, MFG-09/F-CONTR-003, MFG-09/F-CONTR-004, MFG-09/F-CONTR-005, MFG-09/F-CONTR-006, MFG-09/F-CONTR-007 |
| UC-C17 | View merge-eligible orders | Company Admin | None | MFG-10/F-MER-004, MFG-10/F-MER-005 |
| UC-C18 | Confirm merge batch | Company Admin | None | MFG-10/F-MER-006, MFG-10/F-MER-007 |
| UC-C16 | Optimize order | Company Admin | UC-C17, UC-C18 | MFG-10/F-MER-004, MFG-10/F-MER-005, MFG-10/F-MER-006, MFG-10/F-MER-007 |
| UC-C19 | Assign consultant | Company Admin | None | MFG-08/F-ORD-001, MFG-08/F-ORD-002, MFG-08/F-ORD-003, MFG-08/F-ORD-004 |
| UC-C21 | View dashboard | Company Admin | None | MFG-11/F-DA-001, MFG-11/F-DA-002 |
| UC-C22 | Export data | Company Admin | None | MFG-11/F-DA-003 |
| UC-C20 | Data Analytics | Company Admin | UC-C21, UC-C22 | MFG-11/F-DA-001, MFG-11/F-DA-002, MFG-11/F-DA-003 |
| UC-C24 | Add product | Company Admin | None | MFG-04/F-PROD-004, MFG-04/F-PROD-005, MFG-04/F-PROD-006 |
| UC-C25 | Update product info | Company Admin | None | MFG-04/F-PROD-007, MFG-04/F-PROD-008 |
| UC-C26 | Delete product | Company Admin | None | MFG-04/F-PROD-009, MFG-04/F-PROD-010 |
| UC-C27 | Publish/ Unpublish product | Company Admin | None | MFG-04/F-PROD-011 |
| UC-C23 | Manage product catalog | Company Admin | UC-C24, UC-C25, UC-C26, UC-C27 | MFG-04/F-PROD-004, MFG-04/F-PROD-005, MFG-04/F-PROD-006, MFG-04/F-PROD-007, MFG-04/F-PROD-008, MFG-04/F-PROD-009, MFG-04/F-PROD-010, MFG-04/F-PROD-011 |
| UC-S06 | Add account | System Admin | None | MFG-03/F-ACC-001, MFG-03/F-ACC-002, MFG-03/F-ACC-003, MFG-03/F-ACC-004 |
| UC-S07 | Update account info & role | System Admin | None | MFG-03/F-ACC-005, MFG-03/F-ACC-006 |
| UC-S08 | Delete account | System Admin | None | MFG-03/F-ACC-007, MFG-03/F-ACC-008 |
| UC-S05 | Manage company's user accounts | System Admin | UC-S06, UC-S07, UC-S08 | MFG-03/F-ACC-001, MFG-03/F-ACC-002, MFG-03/F-ACC-003, MFG-03/F-ACC-004, MFG-03/F-ACC-005, MFG-03/F-ACC-006, MFG-03/F-ACC-007, MFG-03/F-ACC-008 |
| UC-S09 | Monitor system logs | System Admin | None | MFG-12/F-SYS-001, MFG-12/F-SYS-002 |
| UC-S10 | Backup & restore data | System Admin | None | MFG-12/F-SYS-003, MFG-12/F-SYS-004, MFG-12/F-SYS-005 |
| UC-S11 | Configure system | System Admin | None | MFG-12/F-SYS-006, MFG-12/F-SYS-007, MFG-12/F-SYS-008 |

UC-C01 is the concrete design-editor child of UC-C02 and uses the same design functions; it does not create a second implementation. UC-C10 is read-only contract access within UC-C09; it shares contract retrieval with UC-C11 without granting signing to staff. UC-C15 covers template creation/versioning and unsigned contract revision. Module specs and [screen catalogue](../screen-list.md) define navigation and success/failure scenarios. No use-case relationship bypasses ownership, state or payment guards.
