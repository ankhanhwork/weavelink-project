# UC-G01: View product catalog — SD-01: Browse Product Catalog (Guest)

```mermaid
sequenceDiagram
    actor Guest
    participant ProductUI
    participant ProductController
    participant ProductService
    participant ProductCatalogDatabase

    Guest->>ProductUI: access website
    ProductUI->>ProductController: request product catalog
    ProductController->>ProductService: get product list
    ProductService->>ProductCatalogDatabase: retrieve products
    ProductCatalogDatabase-->>ProductService: product list
    ProductService-->>ProductController: return products
    ProductController-->>ProductUI: send catalog data
    ProductUI-->>Guest: display product catalog
```

# UC-G03: Register account — SD-02: Sign Up

```mermaid
sequenceDiagram
    actor Guest
    participant AuthUI
    participant AuthController
    participant AuthService
    participant UserAccountDatabase

    Guest->>AuthUI: enter registration information
    AuthUI->>AuthController: submit registration
    AuthController->>AuthService: register user
    AuthService->>UserAccountDatabase: register normalized email idempotently
    alt [email is new]
        UserAccountDatabase-->>AuthService: create Customer account
        AuthService->>AuthService: queue verification message
    else [email already registered]
        UserAccountDatabase-->>AuthService: no mutation
    end
    Note over AuthService,AuthUI: Both paths return the same 202 response and generic acknowledgement, never reveal whether the address exists.
    AuthService-->>AuthController: registration accepted (same response shape)
    AuthController-->>AuthUI: HTTP 202 generic acknowledgement
    AuthUI-->>Guest: display generic next-step message
```

# UC-M01: Log in — SD-03: Log In

```mermaid
sequenceDiagram
    actor Customer
    participant AuthUI
    participant AuthController
    participant AuthService
    participant UserAccountDatabase

    Customer->>AuthUI: enter login credentials
    AuthUI->>AuthController: submit login request
    AuthController->>AuthService: authenticate user
    AuthService->>UserAccountDatabase: find user
    alt [unknown identity or invalid credentials]
        AuthService-->>AuthController: generic authentication failure
        AuthController-->>AuthUI: HTTP 401 Invalid email or password
        AuthUI-->>Customer: display the same login failure message
    else [valid credentials]
        AuthService-->>AuthController: authentication success
        AuthController-->>AuthUI: return success
        AuthUI-->>Customer: display login success
    end
```

# UC-G02: Search products — SD-04: Search and View Product Detail

```mermaid
sequenceDiagram
    actor Customer
    participant ProductUI
    participant ProductController
    participant ProductService
    participant ProductCatalogDatabase

    Customer->>ProductUI: enter search keyword
    ProductUI->>ProductController: submit query
    ProductController->>ProductService: search product
    ProductService->>ProductCatalogDatabase: retrieve product information
    ProductCatalogDatabase-->>ProductService: search result
    alt [Product not found]
        ProductService-->>ProductController: empty result
        ProductController-->>ProductUI: empty result
        ProductUI-->>Customer: display "No product found"
    else [Product found]
        ProductService-->>ProductController: product list
        ProductController-->>ProductUI: product list
        ProductUI-->>Customer: display product list
        Customer->>ProductUI: select product
        ProductUI->>ProductController: request product detail
        ProductController->>ProductService: get product detail
        ProductService->>ProductCatalogDatabase: retrieve product detail
        ProductCatalogDatabase-->>ProductService: product detail
        ProductService-->>ProductController: return detail
        ProductController-->>ProductUI: send product detail
        ProductUI-->>Customer: display product detail
    end
```

## UC-G02 extension: Product Finder (MFG-04/F-PROD-012, Should)

The Must full-search flow above remains available. When enabled, suggestions and paginated results share the matching rules in [MFG-04 sections 5.3–5.4](../../specs/spec-MFG-04.md#53-keyword-matching-model-f-prod-012) and [S08](../../screens/S08-product_catalog_screen.md). Physical index storage is a Plan decision. No search analytics are introduced.

```mermaid
sequenceDiagram
    actor Buyer as Guest/Member
    participant S08
    participant SearchService
    participant Catalogue
    Buyer->>S08: focus empty field or type query
    S08->>SearchService: settled q and active scope/filters
    SearchService->>SearchService: validate q <=100 and allowlisted constraints
    alt invalid input
        SearchService-->>S08: 400/422; preserve input, no broader search
    else valid input
        SearchService->>Catalogue: current Published/version-eligible candidate data
        Catalogue-->>SearchService: public products under active constraints
        alt trimmed query empty
            SearchService-->>S08: at most 4 featured products
        else keyword entered
            SearchService->>SearchService: normalise and match all query tokens; rank
            SearchService-->>S08: at most 10 matches, total count, stored attribute reasons
            S08-->>Buyer: four visible rows or labelled no-match alternatives
        end
        S08->>S08: discard responses for previous query/filter state
        Buyer->>S08: choose product or full results
        Note over S08,Catalogue: S09 rechecks Published status; full S08 search keeps query/filters
    end
```
# UC-C02: Design product — SD-05A: Self Design Product

```mermaid
sequenceDiagram
    actor Customer
    participant DesignUI
    participant DesignController
    participant DesignService
    participant CustomerDesignDatabase

    Customer->>DesignUI: customize product design
    DesignUI->>DesignController: submit design
    DesignController->>DesignService: process design
    alt [save success]
        DesignService->>CustomerDesignDatabase: save design
        CustomerDesignDatabase-->>DesignService: saved
        DesignService-->>DesignController: save success
    else [save failed]
        DesignService-->>DesignController: save failed
    end
    DesignController-->>DesignUI: display save result
    DesignUI-->>Customer: display save confirmation
```

# UC-C04: Request design service — SD-05B: Request Design Service

```mermaid
sequenceDiagram
    actor Customer
    actor CompanyAdmin as Sales Admin
    participant RequestUI as S15 / S17
    participant AdminUI as S18
    participant DesignModule
    participant Database
    participant Outbox

    Customer->>RequestUI: Submit validated request on S15
    RequestUI->>DesignModule: Create request with idempotency key
    DesignModule->>Database: Atomically save Submitted and admin outbox event
    DesignModule-->>RequestUI: Request ID, navigate to S17 request view
    Outbox-->>CompanyAdmin: Notify submitted request
    CompanyAdmin->>AdminUI: Start review with expected version
    AdminUI->>DesignModule: Transition Submitted to UnderReview
    CompanyAdmin->>AdminUI: Record complexity, rationale and fee or rejection reason
    AdminUI->>DesignModule: Assess with expected version and key
    alt Simple
        DesignModule->>Database: Approve with fee 0 and customer outbox event
    else Complex
        DesignModule->>Database: Save FeeProposed, amount/version and customer outbox event
        Outbox-->>Customer: Review proposal in S17, no payment now
        Customer->>RequestUI: Accept exact fee and proposal version
        RequestUI->>DesignModule: Accept with expected version and key
        DesignModule->>Database: Atomically record acceptance and Approved, admin outbox event
    else Rejected
        DesignModule->>Database: Save Rejected with reason and customer outbox event
    end
    opt Customer cancels before assignment
        Customer->>RequestUI: Confirm cancellation in eligible state
        RequestUI->>DesignModule: Cancel with expected version and key
        DesignModule->>Database: Lock, cancel only unassigned eligible request, no refund
    end
    CompanyAdmin->>AdminUI: Open S19 for Approved request
    AdminUI->>DesignModule: Assign through MFG-08 with expected versions
    DesignModule->>Database: Lock, assign only if still Approved, conflicting cancellation returns 409
```

# UC-C03: View saved design — SD-06: View Saved Design

```mermaid
sequenceDiagram
    actor Customer
    participant SavedDesignUI
    participant SavedDesignController
    participant SavedDesignService
    participant SavedDesignDatabase

    Customer->>SavedDesignUI: view saved design
    SavedDesignUI->>SavedDesignController: request design
    SavedDesignController->>SavedDesignService: get design
    SavedDesignService->>SavedDesignDatabase: retrieve design
    SavedDesignDatabase-->>SavedDesignService: design data
    SavedDesignService-->>SavedDesignController: return design
    SavedDesignController-->>SavedDesignUI: send design
    SavedDesignUI-->>Customer: display design
```

# UC-C05: Finalize order — SD-07: Create Order

```mermaid
sequenceDiagram
    actor Customer
    participant OrderUI as S22-S25
    participant CheckoutService
    participant Database
    participant OutboxWorker

    Customer->>OrderUI: Enter quantities, VN delivery address and merge preference
    OrderUI->>CheckoutService: Request server-priced quote
    CheckoutService->>Database: Validate design/product/policy and save expiring quote
    Database-->>CheckoutService: Immutable quote and commercial breakdown
    CheckoutService-->>OrderUI: Quote for explicit review
    Customer->>OrderUI: Submit current quote with idempotency key
    OrderUI->>CheckoutService: Create made-to-order order
    CheckoutService->>Database: Lock quote and create AwaitingDigitalApproval order
    CheckoutService->>Database: Persist timeline and notification outbox
    CheckoutService-->>OrderUI: Created order and next action S27
    OutboxWorker-->>Customer: Notify digital-design approval required
```

# UC-C09: View/Sign contract — SD-08: View and Sign Digital Contract

```mermaid
sequenceDiagram
    actor Customer
    participant ContractUI as S34
    participant ContractService
    participant Database
    participant OutboxWorker

    Customer->>ContractUI: Open current Ready contract
    ContractUI->>ContractService: Request owned contract version
    ContractService->>Database: Verify PendingContract and current Approved sample
    Database-->>ContractService: PDF/hash, sample and deposit terms
    ContractService-->>ContractUI: Authorized review model and signing challenge
    Customer->>ContractUI: Consent, typed name, recent password and challenge
    ContractUI->>ContractService: Sign current version with idempotency key
    ContractService->>Database: Lock contract/order and revalidate version/hash/sample
    alt Evidence valid
        ContractService->>Database: Save evidence, Signed, order AwaitingDeposit
        ContractService->>Database: Write notification outbox
        ContractService-->>ContractUI: Signed receipt and deposit next action
        OutboxWorker-->>Customer: Send authorized signed-copy notice
    else Evidence stale or invalid
        ContractService-->>ContractUI: Reject without signature or order transition
    end
```

# UC-C12: Make payment — SD-09: Pay Deposit or Remaining Balance

```mermaid
sequenceDiagram
    actor Customer
    participant PaymentUI as S35
    participant PaymentService
    participant Database
    participant VNPay

    Customer->>PaymentUI: Pay available DEPOSIT or BALANCE
    PaymentUI->>PaymentService: order ID, purpose and idempotency key
    PaymentService->>Database: Verify purpose-specific payable state and exact amount
    PaymentService->>Database: Create/reuse one Pending attempt for order and purpose
    PaymentService->>VNPay: Create signed hosted-payment request
    VNPay-->>PaymentUI: Browser redirect/return is display only
    VNPay->>PaymentService: Authoritative signed server callback
    PaymentService->>Database: Verify merchant, reference, purpose, amount and uniqueness
    alt Accepted DEPOSIT
        PaymentService->>Database: Succeeded, AwaitingDeposit to Confirmed
    else Accepted BALANCE
        PaymentService->>Database: Succeeded, DeliveredAwaitingBalance to Completed
    else Failure, mismatch or late cancelled receipt
        PaymentService->>Database: Preserve order gate, audit and refund late captured money
    end
    PaymentUI->>PaymentService: Poll transaction status
    PaymentService-->>PaymentUI: Authoritative purpose, amount, state and next action
```

| Diagram | Participants | Arrows | Unreadable text |
|---|---:|---:|---|
| SD-01 | 5 | 8 | None |
| SD-02 | 5 | 12 | None |
| SD-03 | 5 | 15 | None |
| SD-04 | 5 | 19 | None |
| SD-05A | 5 | 9 | None |
| SD-05B | 7 | 22 | None |
| SD-06 | 5 | 8 | None |
| SD-07 | 5 | 11 | None |
| SD-08 | 5 | 13 | None |
| SD-09 | 5 | 13 | None |

# MFG-07: Track, cancel and fulfill order — SD-10

```mermaid
sequenceDiagram
    actor OrderActor as Customer or authorized staff
    participant OrderUI as S26-S29
    participant OrderModule as Order module
    participant Database as Database
    participant PaymentModule as MFG-06 Payment
    participant OutboxWorker as Outbox worker
    OrderActor->>OrderUI: Request own or authorized order view
    OrderUI->>OrderModule: Order ID and session
    OrderModule->>Database: Enforce customer ownership or staff role/assignment scope, load snapshot and timeline
    Database-->>OrderModule: Authorized order history
    OrderModule-->>OrderUI: Snapshot, status and payment/refund summary
    alt Eligible cancellation
        OrderActor->>OrderModule: Reason, expected version and idempotency key
        OrderModule->>Database: Lock order, validate transition and persist cancellation
        opt Captured refundable amount
            OrderModule->>PaymentModule: Request policy-based refund after commit
        end
        OrderModule->>Database: Write notification outbox event
        OutboxWorker-->>OrderActor: Notify cancellation and refund status
    else Fulfillment, receipt or settlement event
        OrderActor->>OrderModule: Authorized lifecycle event and expected version
        OrderModule->>Database: Validate event owner, transition and evidence, commit
        OutboxWorker-->>OrderActor: Notify status and safe tracking link
    end
```

# MFG-08: Assign customer and manage consultation — SD-11

```mermaid
sequenceDiagram
    actor CompanyAdmin as Sales Admin
    actor Consultant as Sales
    participant ConsultationUI as S18-S21
    participant ConsultationModule as Consultation module
    participant Database as Database
    participant OutboxWorker as Outbox worker
    CompanyAdmin->>ConsultationUI: Select Dony customer and consultant
    ConsultationUI->>ConsultationModule: Assignment change with expected version and key
    ConsultationModule->>Database: Validate active Dony StaffAccount and lock assignment
    Database-->>ConsultationModule: Current assignment and active requests
    ConsultationModule->>Database: Atomically change assignment and transfer active request ownership
    ConsultationModule->>Database: Append assignment history and outbox event
    OutboxWorker-->>Consultant: Notify new assignment
    Consultant->>ConsultationUI: Open assigned customer
    ConsultationUI->>ConsultationModule: Request customer context
    ConsultationModule->>Database: Check active assignment and load permitted summaries
    Database-->>ConsultationModule: Authorized customer context and optional buyer organization
    ConsultationModule-->>ConsultationUI: Context and consultation timeline
    Consultant->>ConsultationModule: Update consultation status/notes with expected version
    ConsultationModule->>Database: Validate transition and append interaction event
    ConsultationModule-->>ConsultationUI: Updated consultation and timeline
```

# MFG-10: Merge production and batch lifecycle — SD-12

```mermaid
sequenceDiagram
    actor Customer
    actor Admin as Sales Admin
    participant Checkout as MFG-06
    participant Merge as MFG-10
    participant Order as MFG-07
    participant Scheduler
    Customer->>Checkout: Choose standard or offered flexible terms and policy
    Checkout->>Checkout: Check materials/capacity, snapshot price and readiness-based terms
    Note over Checkout,Order: Design/sample approval, contract signing and deposit establish production_ready_at
    Order->>Merge: Ready Confirmed order; derive day-7 wait and separate 8-14-day production dates
    Merge-->>Admin: Existing open run first, otherwise flexible group or individual plan
    Admin->>Merge: Approve schedule/addition with expected versions
    Merge->>Merge: Persist exclusively assigned sewing membership and approved schedule
    Note over Merge,Order: Scheduled assignment is not InProduction
    Admin->>Merge: Lock membership, then explicitly start on schedule
    Merge->>Order: Atomically advance all locked members to InProduction
    alt Flexible waiting deadline without approved feasible placement
        Scheduler->>Merge: Detect expiry; send deduplicated approval-required notice
        Admin->>Merge: Review; approve individual plan and explicitly start
        Merge->>Order: Advance only after explicit human approval/start
    end
    Note over Customer,Order: Preserve each customer's price, deadline and private order tracking
```

# MFG-11: Dony analytics, funnel and matching export — SD-13

```mermaid
sequenceDiagram
    actor Admin as Sales Admin
    participant UI as S43
    participant Metrics as Shared authorized metric layer
    participant DB as Authoritative facts and validated events
    participant Results as Protected result snapshots
    participant Worker as Export worker
    participant Assets as Private asset store
    Admin->>UI: Select tab, filters, unit, cohort, observation mode and cutoff
    UI->>Metrics: Typed query with current session
    Metrics->>Metrics: Authorize Sales Admin and validate context
    Metrics->>DB: Read consistent snapshot with evidence coverage
    DB-->>Metrics: Scoped facts, original events and watermark
    Metrics->>Results: Record result, definitions, cutoff and coverage
    Metrics-->>UI: Result ID, business or funnel metrics, waiting detail
    Admin->>UI: Export selected result as CSV or XLSX
    UI->>Metrics: Result ID, dataset, format and idempotency key
    Metrics->>Results: Reauthorize result and queue matching export
    Metrics-->>UI: Export job ID and state
    Worker->>Results: Read original result snapshot, not current filters
    Worker->>Worker: Enforce column allowlist, row cap and formula escaping
    Worker->>Assets: Store private export
    Worker->>Results: Persist success or actionable failure
    Admin->>UI: Poll and download
    UI->>Metrics: Authorized job request
    Metrics-->>UI: Job state#59, successful private URL expires within 10 minutes and before file expiry
```

When the original snapshot cannot be reproduced, export fails explicitly instead of substituting current data. Interaction evidence cannot settle orders; committed timeline/outbox events are projected idempotently. MFG-11 5.3 owns resolved authenticated product-entry/intent/order formulas and coverage; 5.7 owns 12-month reporting and seven-day result/export lifetimes. Guest views are neither collected nor replayed at login.

# MFG-11: Grounded prompt analysis — SD-13A

```mermaid
sequenceDiagram
    actor Admin as Sales Admin
    participant UI as S43 AI panel
    participant Metrics as Shared authorized metric layer
    participant AI as Restricted AI adapter
    participant Results as Protected facts and result snapshots
    Admin->>UI: Ask about active result and selected stage
    UI->>Metrics: Prompt and original context result ID
    Metrics->>Metrics: Recheck role and sanitize prompt
    Metrics->>AI: Allowed metric schema and sanitized intent
    AI-->>Metrics: Typed query proposal or clarification
    alt Ambiguous or unsupported plan
        Metrics-->>UI: Clarification or unsupported state#59; no arbitrary query
    else Changed context
        Metrics-->>UI: Proposed context for explicit Apply
        Admin->>UI: Apply proposed context
        UI->>Metrics: Validated proposed context
    end
    opt Validated and explicitly applied context
        Metrics->>Results: Execute bounded authorized metric query
        Results-->>Metrics: Aggregate result, definitions, cutoff and coverage
        Metrics->>AI: Minimum aggregate facts with opaque evidence IDs
        AI-->>Metrics: Structured findings, references and labeled hypotheses
        Metrics->>Metrics: Validate numeric fields, claims and evidence links
        Metrics-->>UI: Grounded answer or safe insufficient/unavailable state
    end
    Admin->>UI: Open answer source after filters change
    UI->>Metrics: Original source result ID and stage
    Metrics->>Results: Fresh authorization#59; load original result
    Metrics-->>UI: Original context or explicit snapshot unavailable
```

For unchanged valid context, the existing applied dashboard context satisfies the Apply condition. Model failure does not disable deterministic charts or exports. Provider/model selection and runtime limits remain Plan item I-01; the product retention rules are resolved in MFG-11 5.7. No external provider or direct model database access is implied. Prompt/answer conversation is transient processing plus memory in the active page, not a persistent history. Closing/reloading/leaving that page or losing the session clears it; source results expire after seven days and must not be silently refreshed.

# MFG-12: System operations, backup, restore and configuration — SD-14

```mermaid
sequenceDiagram
    actor SystemAdmin as System Admin
    actor Scheduler as Trusted scheduler
    participant OperationsUI as S39-S40
    participant OperationsModule as System operations module
    participant OperationalDB as Database and external journal
    participant JobWorker as Job worker
    participant BackupStore as Backup/asset store
    participant OutboxWorker as Outbox worker
    SystemAdmin->>OperationsUI: Request audit, backup status or configuration
    OperationsUI->>OperationsModule: Authorized request with filters
    OperationsModule->>OperationalDB: Derive admin privilege, read redacted logs/status/config
    OperationalDB-->>OperationsModule: Scoped operational data
    OperationsModule-->>OperationsUI: View model with secrets masked
    alt Backup requested or scheduled
        SystemAdmin->>OperationsModule: Trigger backup with idempotency key
        Scheduler->>OperationsModule: Scheduled backup trigger
        OperationsModule->>OperationalDB: Audit and enqueue serialized job
        JobWorker->>OperationalDB: Snapshot database and transaction watermark
        JobWorker->>BackupStore: Store encrypted base/assets and verified manifest
        JobWorker->>OperationalDB: Record verified completion
    else Restore requested
        SystemAdmin->>OperationsModule: Backup ID, confirmation, reauth and expected version
        OperationsModule->>OperationalDB: Acquire restore lock, audit and enqueue job
        JobWorker->>BackupStore: Verify base, assets, checksums and continuous log chain
        JobWorker->>OperationalDB: Restore to committed pre-maintenance watermark
        JobWorker->>OperationalDB: Reconcile external payment journal, activate only if valid
    else Configuration changed
        SystemAdmin->>OperationsModule: Allowlisted patch, reauth and expected version
        OperationsModule->>OperationalDB: Validate full patch and atomically activate version
        OperationsModule->>OperationalDB: Append audit and notification outbox event
        OutboxWorker-->>SystemAdmin: Notify changed key names/version only
    end
```
