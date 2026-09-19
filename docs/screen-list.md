# Screen catalogue

Complete-system screen routes and access summary. Detailed behavior is in each linked screen specification; global rules are in [system decisions](system-decisions.md). Historical Session 1 MVP exclusions do not remove modules from this target.

| ID | Screen | Route | Roles / ownership | Module | Detailed specification | Mockup status |
|---|---|---|---|---|---|---|
| S01 | Home Page | `/` | Guest | MFG-04 | [S01-home_page.md](../screens/S01-home_page.md) | Historical PNG supplied; D11 rules govern |
| S02 | Sign Up | `/sign-up` | Guest | MFG-01 | [S02-sign_up_screen.md](../screens/S02-sign_up_screen.md) | Historical PNG supplied; D11 rules govern |
| S03 | Log In | `/login` | Guest | MFG-01 | [S03-login_screen.md](../screens/S03-login_screen.md) | Historical PNG supplied; D11 rules govern |
| S04 | Forgot Password | `/forgot-password` | Guest | MFG-01 | [S04-forgot_password_screen.md](../screens/S04-forgot_password_screen.md) | No mockup supplied |
| S05 | Reset Password | `/reset-password?token={token}` | Guest with single-use token | MFG-01 | [S05-reset_password_screen.md](../screens/S05-reset_password_screen.md) | No mockup supplied |
| S06 | User Profile | `/profile` | Member | MFG-02 | [S06-user_profile_screen.md](../screens/S06-user_profile_screen.md) | Historical PNG supplied; D11 rules govern |
| S07 | Change Password | `/profile/change-password` | Member | MFG-02 | [S07-change_password_screen.md](../screens/S07-change_password_screen.md) | No mockup supplied |
| S08 | Product Catalog | `/catalog` | Guest/Member | MFG-04 | [S08-product_catalog_screen.md](../screens/S08-product_catalog_screen.md) | Historical PNG supplied; D11 rules govern |
| S09 | Product Detail | `/products/{product_id}` | Guest/Member | MFG-04 | [S09-product_detail_screen.md](../screens/S09-product_detail_screen.md) | Historical PNG supplied; D11 rules govern |
| S10 | Product List (Company Admin) | `/admin/products` | Company Admin | MFG-04 | [S10-product_list_company_admin_screen.md](../screens/S10-product_list_company_admin_screen.md) | No mockup supplied |
| S11 | Product Create | `/admin/products/new` | Company Admin | MFG-04 | [S11-product_create_screen.md](../screens/S11-product_create_screen.md) | No mockup supplied |
| S12 | Product Edit | `/admin/products/{product_id}/edit` | Company Admin | MFG-04 | [S12-product_edit_screen.md](../screens/S12-product_edit_screen.md) | No mockup supplied |
| S13 | Product Design Tool | `/designs/new?product_id={id}` | Customer owner | MFG-05 | [S13-product_design_tool_screen.md](../screens/S13-product_design_tool_screen.md) | Historical PNG supplied; D11 rules govern |
| S14 | Product Design Rules | `/admin/products/{product_id}/design-rules` | Company Admin | MFG-04 | [S14-product_design_rules_screen.md](../screens/S14-product_design_rules_screen.md) | No mockup supplied |
| S15 | Design Service Request | `/design-requests/new?product_id={id}` | Customer owner | MFG-05 | [S15-design_service_request_screen.md](../screens/S15-design_service_request_screen.md) | Historical PNG supplied; D11 rules govern |
| S16 | Design Service Payment | `/design-requests/{request_id}/payment` | Customer owner | MFG-06 | [S16-design_service_payment_screen.md](../screens/S16-design_service_payment_screen.md) | Historical PNG supplied; D11 rules govern |
| S17 | Customer Designs | `/designs` | Customer owner | MFG-05 | [S17-customer_designs_screen.md](../screens/S17-customer_designs_screen.md) | Historical PNG supplied; D11 rules govern |
| S18 | Consultation Requests and Customers | `/admin/consultations?tab=requests,customers` | Company Admin | MFG-05 | [S18-consultation_requests_and_customers_screen.md](../screens/S18-consultation_requests_and_customers_screen.md) | No mockup supplied |
| S19 | Consultation Assignment | `/admin/design-requests/{request_id}/assignment` | Company Admin | MFG-05 | [S19-consultation_assignment_screen.md](../screens/S19-consultation_assignment_screen.md) | No mockup supplied |
| S20 | Consultant Tasks and Customers | `/consultant/tasks?tab=assigned,customers` | Sales Consultant | MFG-08 | [S20-consultant_tasks_and_customers_screen.md](../screens/S20-consultant_tasks_and_customers_screen.md) | No mockup supplied |
| S21 | Consultation Detail | `/consultant/design-requests/{request_id}` | Assigned Consultant/Company Admin | MFG-08 | [S21-consultation_detail_screen.md](../screens/S21-consultation_detail_screen.md) | No mockup supplied |
| S22 | Create Order | `/orders/new?design_id={id}` | Customer owner | MFG-06 | [S22-create_order_screen.md](../screens/S22-create_order_screen.md) | Historical PNG supplied; D11 rules govern |
| S23 | Merge Option | `/orders/merge?design_id={id}` | Customer owner | MFG-10 | [S23-merge_option_screen.md](../screens/S23-merge_option_screen.md) | Historical PNG supplied; D11 rules govern |
| S24 | Merge Terms | `/merge-terms` | Guest/Customer | MFG-10 | [S24-merge_terms_screen.md](../screens/S24-merge_terms_screen.md) | No mockup supplied |
| S25 | Order Summary | `/orders/summary?quote_id={id}` | Customer owner | MFG-06 | [S25-order_summary_screen.md](../screens/S25-order_summary_screen.md) | Historical PNG supplied; D11 rules govern |
| S26 | Customer Order List | `/orders` | Customer owner | MFG-07 | [S26-customer_order_list_screen.md](../screens/S26-customer_order_list_screen.md) | Historical PNG supplied; D11 rules govern |
| S27 | Customer Order Detail | `/orders/{order_id}` | Customer owner | MFG-07 | [S27-customer_order_detail_screen.md](../screens/S27-customer_order_detail_screen.md) | Historical PNG supplied; D11 rules govern |
| S28 | Order List (Admin) | `/admin/orders` | Company Admin | MFG-07 | [S28-order_list_admin_screen.md](../screens/S28-order_list_admin_screen.md) | No mockup supplied |
| S29 | Order Detail (Admin) | `/admin/orders/{order_id}` | Company Admin/Assigned Consultant | MFG-07 | [S29-order_detail_admin_screen.md](../screens/S29-order_detail_admin_screen.md) | No mockup supplied |
| S30 | Contract Templates and Contracts | `/admin/contracts?tab=templates,contracts` | Company Admin | MFG-09 | [S30-contract_templates_and_contracts_screen.md](../screens/S30-contract_templates_and_contracts_screen.md) | No mockup supplied |
| S31 | Contract Template Create | `/admin/contracts/templates/new` | Company Admin | MFG-09 | [S31-contract_template_create_screen.md](../screens/S31-contract_template_create_screen.md) | No mockup supplied |
| S32 | Contract Template Edit | `/admin/contracts/templates/{template_id}/edit` | Company Admin | MFG-09 | [S32-contract_template_edit_screen.md](../screens/S32-contract_template_edit_screen.md) | No mockup supplied |
| S33 | Contract Detail (Company Admin) | `/admin/contracts/{contract_id}` | Company Admin | MFG-09 | [S33-contract_detail_company_admin_screen.md](../screens/S33-contract_detail_company_admin_screen.md) | No mockup supplied |
| S34 | Contract Detail (Customer) | `/contracts/{contract_id}` | Customer owner | MFG-09 | [S34-contract_detail_screen_customer.md](../screens/S34-contract_detail_screen_customer.md) | Historical PNG supplied; D11 rules govern |
| S35 | Order Payment | `/orders/{order_id}/payment` | Customer owner | MFG-06 | [S35-order_payment_screen.md](../screens/S35-order_payment_screen.md) | Historical PNG supplied; D11 rules govern |
| S36 | Payment Transaction List | `/admin/payments` | Company Admin | MFG-06 | [S36-payment_transaction_list_screen.md](../screens/S36-payment_transaction_list_screen.md) | No mockup supplied |
| S37 | Payment Transaction Detail | `/admin/payments/{payment_id}` | Company Admin | MFG-06 | [S37-payment_transaction_detail_screen.md](../screens/S37-payment_transaction_detail_screen.md) | No mockup supplied |
| S38 | Notification Panel | `/notifications` | Authenticated user | MFG-01 | [S38-notification_panel_screen.md](../screens/S38-notification_panel_screen.md) | No mockup supplied |
| S39 | System Configuration and Backup/Restore | `/system/configuration` | System Admin | MFG-12 | [S39-system_configuration_and_backup_restore_screen.md](../screens/S39-system_configuration_and_backup_restore_screen.md) | No mockup supplied |
| S40 | System Log Viewer | `/system/logs` | System Admin | MFG-12 | [S40-system_log_viewer_screen.md](../screens/S40-system_log_viewer_screen.md) | No mockup supplied |
| S41 | Company and Staff Accounts | `/system/companies` | System Admin | MFG-03 | [S41-company_and_staff_accounts_screen.md](../screens/S41-company_and_staff_accounts_screen.md) | No mockup supplied |
| S42 | Merge Console | `/admin/merge-batches` | Company Admin | MFG-10 | [S42-merge_console_screen.md](../screens/S42-merge_console_screen.md) | No mockup supplied |
| S43 | Analytics Dashboard | `/admin/analytics` | Company Admin | MFG-11 | [S43-analytics_dashboard_screen.md](../screens/S43-analytics_dashboard_screen.md) | No mockup supplied |

All routes enforce D01 authorization on the server. Navigation follows D11; inaccessible object identifiers return 404, prohibited operations 403, and missing authentication 401.
