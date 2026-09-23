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
    actor Customer as Customer
    actor CompanyAdmin as Sales Admin
    actor Scheduler as Trusted scheduler
    participant CheckoutModule as MFG-06 Checkout
    participant MergeModule as Merge module
    participant Database as Database
    participant OrderModule as MFG-07 Order module
    participant OutboxWorker as Outbox worker
    Customer->>MergeModule: Review versioned policy and opt in on quote
    MergeModule->>CheckoutModule: Save preference and accepted policy version
    CheckoutModule->>Database: Recompute discount and issue replacement quote
    Customer->>CheckoutModule: Submit current quote
    CheckoutModule->>Database: Create AwaitingDigitalApproval order and immutable snapshots
    Note over OrderModule,MergeModule: Digital approval, physical sample approval, contract signing and verified deposit make an order Confirmed
    CompanyAdmin->>MergeModule: View compatible candidate pool and estimate
    MergeModule->>Database: Recompute compatibility, limits and savings
    MergeModule-->>CompanyAdmin: Candidates, exclusions, savings and deadlines
    Scheduler->>MergeModule: Recompute and publish recommendations for compatible rolling 7-day pool
    MergeModule-->>CompanyAdmin: Candidate groups, deadlines, exclusions and savings (including negative net)
    CompanyAdmin->>MergeModule: Review selected members and explicitly start batch
    MergeModule->>Database: Lock and revalidate eligibility, versions, quantity and deadline
    MergeModule->>Database: Create InProduction batch with immutable membership and estimate
    MergeModule->>OrderModule: Atomically advance all selected orders to InProduction
    OutboxWorker-->>Customer: Notify committed batch/status event
    alt No Admin-started batch after rolling seven-day window
        Scheduler->>MergeModule: Process fallback
        MergeModule->>OrderModule: Start Individual Production through MFG-07
        OutboxWorker-->>Customer: Notify individual production fallback
    else Admin declines recommendation
        MergeModule->>Database: Keep order unreserved and eligible until its deadline
    end
```

# MFG-11: Company analytics and export — SD-13

```mermaid
sequenceDiagram
    actor CompanyAdmin as Sales Admin
    participant AnalyticsUI as S43
    participant AnalyticsModule as Analytics module
    participant AuthoritativeDB as Authoritative records
    participant ExportWorker as Export worker
    participant PrivateAssetStore as Private asset store
    CompanyAdmin->>AnalyticsUI: Select date range and metric
    AnalyticsUI->>AnalyticsModule: Request dashboard data
    AnalyticsModule->>AuthoritativeDB: Validate Dony scope and date range
    AnalyticsModule->>AuthoritativeDB: Aggregate scoped orders and accepted payments/refunds
    AuthoritativeDB-->>AnalyticsModule: Source rows and refresh watermark
    AnalyticsModule-->>AnalyticsUI: Typed chart series, totals and refreshed_at
    CompanyAdmin->>AnalyticsUI: Request CSV/XLSX export
    AnalyticsUI->>AnalyticsModule: Dataset, filters, format and idempotency key
    AnalyticsModule->>AuthoritativeDB: Snapshot filters/watermark and queue job
    AnalyticsModule-->>AnalyticsUI: Export ID and queued status
    ExportWorker->>AuthoritativeDB: Read snapshot, enforce columns/row limit and escape formulas
    ExportWorker->>PrivateAssetStore: Store private export
    ExportWorker->>AuthoritativeDB: Mark success and persist asset reference
    CompanyAdmin->>AnalyticsUI: Poll export status
    AnalyticsUI->>AnalyticsModule: Export ID
    AnalyticsModule-->>AnalyticsUI: Success and short-lived authorized link
```

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
