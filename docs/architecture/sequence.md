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
    AuthService->>UserAccountDatabase: create user account
    alt [user already exists]
        UserAccountDatabase-->>AuthService: duplicate user
        AuthService-->>AuthController: registration failed
        AuthController-->>AuthUI: return error
        AuthUI-->>Guest: display error message
    else [registration successful]
        UserAccountDatabase-->>AuthService: user created
        AuthService-->>AuthController: registration success
        AuthController-->>AuthUI: return success
        AuthUI-->>Guest: display success message
    end
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
    alt [user not found]
        UserAccountDatabase-->>AuthService: not found
        AuthService-->>AuthController: authentication failed
        AuthController-->>AuthUI: return error
        AuthUI-->>Customer: display error message
    else [user found]
        UserAccountDatabase-->>AuthService: found user
        alt [invalid credentials]
            AuthService-->>AuthController: invalid credentials
            AuthController-->>AuthUI: return error
            AuthUI-->>Customer: display login failed
        else [valid credentials]
            AuthService-->>AuthController: authentication success
            AuthController-->>AuthUI: return success
            AuthUI-->>Customer: display login success
        end
    end
```

# UC-G02: Search products — SD-04 – Search and View Product Detail

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
    participant DesignServiceUI
    participant DesignServiceController
    participant DesignServiceService
    participant PaymentUI
    participant PaymentController
    participant PaymentService
    participant PaymentGateway
    participant ConsultationRequestDatabase

    Customer->>DesignServiceUI: submit design service request
    DesignServiceUI->>DesignServiceController: submit request information
    DesignServiceController->>DesignServiceService: validate request information
    DesignServiceService-->>DesignServiceController: request valid
    DesignServiceController-->>DesignServiceUI: display request summary
    Customer->>DesignServiceUI: click proceed to payment
    DesignServiceUI->>PaymentUI: navigate to payment page
    Customer->>PaymentUI: confirm payment
    PaymentUI->>PaymentController: submit payment
    PaymentController->>PaymentService: create payment request
    PaymentService->>PaymentGateway: redirect payment
    alt [payment successful]
        PaymentGateway-->>PaymentController: payment success
        PaymentController-->>DesignServiceService: confirm payment success
        DesignServiceService->>ConsultationRequestDatabase: save design service request
        ConsultationRequestDatabase-->>DesignServiceService: save success
        DesignServiceService->>PaymentController: request created
        PaymentController-->>PaymentUI: display payment success
        PaymentUI-->>Customer: display confirmation
    else [payment failed]
        PaymentGateway-->>PaymentController: payment failed
        PaymentController-->>PaymentUI: display payment failure
        PaymentUI-->>Customer: display payment error
    end
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
    participant OrderUI
    participant OrderController
    participant OrderService
    participant OrderDatabase
    participant MergedOrderBatchDatabase

    Customer->>OrderUI: submit order information (size, quantity, shipping info)
    OrderUI->>OrderController: submit order
    OrderController->>OrderService: validate order data
    alt [merge selected]
        Customer->>OrderUI: accept merge terms
        OrderUI->>OrderController: confirm merge
        OrderController->>OrderService: add to merge batch
        OrderService->>MergedOrderBatchDatabase: save order reference
    else [no merge]
        OrderService->>OrderService: skip merge
    end
    OrderService->>OrderDatabase: save order (status = Pending Contract)
    OrderDatabase-->>OrderService: order saved
    OrderService-->>OrderController: order created
    OrderController-->>OrderUI: return order summary
    OrderUI-->>Customer: display order summary
```

# UC-C09: View/Sign contract — SD-08: View and Sign Digital Contract

```mermaid
sequenceDiagram
    actor Customer
    participant ContractUI
    participant ContractController
    participant ContractService
    participant ContractDatabase

    Customer->>ContractUI: view contract
    ContractUI->>ContractController: request contract
    ContractController->>ContractService: retrieve contract
    ContractService->>ContractDatabase: get contract data
    ContractDatabase-->>ContractService: contract data
    ContractService-->>ContractController: contract data
    ContractController-->>ContractUI: display contract
    ContractUI-->>Customer: display contract
    Customer->>ContractUI: click sign contract
    ContractUI->>ContractController: submit signing action
    ContractController->>ContractService: process signing
    alt [signing successful]
        ContractService->>ContractDatabase: update contract status = Signed
        ContractDatabase-->>ContractService: update success
        ContractService-->>ContractController: signing success
        ContractController-->>ContractUI: return signed contract
        ContractUI-->>Customer: display signed contract
    else [signing failed]
        ContractService-->>ContractController: signing failed
        ContractController-->>ContractUI: return signing error
        ContractUI-->>Customer: display error message
    end
```

# UC-C12: Make payment — SD-09: Make Order Payment

```mermaid
sequenceDiagram
    actor Customer
    participant PaymentUI
    participant PaymentController
    participant PaymentService
    participant PaymentTransactionDatabase
    participant OrderDatabase
    participant PaymentGateway

    Customer->>PaymentUI: click "Pay Order"
    PaymentUI->>PaymentController: initiate payment
    PaymentController->>PaymentService: create payment transaction
    PaymentService->>PaymentTransactionDatabase: save payment (status = Pending)
    PaymentService->>PaymentGateway: create payment request (API)
    PaymentGateway-->>PaymentService: return payment URL
    PaymentService-->>PaymentController: payment URL
    PaymentController-->>PaymentUI: return payment URL
    PaymentUI->>PaymentGateway: redirect user to payment page
    alt [payment success]
        PaymentGateway-->>PaymentService: payment callback received
        PaymentService->>PaymentTransactionDatabase: update status = Success
        PaymentService->>OrderDatabase: update order status = Ordered
    else [payment failed]
        PaymentGateway-->>PaymentService: payment failed callback
        PaymentService->>PaymentTransactionDatabase: update status = Failed
        PaymentService->>OrderDatabase: update status = Failed
    end
    PaymentService-->>PaymentUI: notify payment result
    PaymentUI-->>Customer: display payment result
```

| Diagram | Participants | Arrows | Unreadable text |
|---|---:|---:|---|
| SD-01 | 5 | 8 | None |
| SD-02 | 5 | 12 | None |
| SD-03 | 5 | 15 | None |
| SD-04 | 5 | 19 | None |
| SD-05A | 5 | 9 | None |
| SD-05B | 9 | 21 | None |
| SD-06 | 5 | 8 | None |
| SD-07 | 6 | 13 | None |
| SD-08 | 5 | 19 | None |
| SD-09 | 7 | 17 | None |

The first return arrow in the `[payment success]` branch of SD-09 has no visible label in the source image.

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
    OrderModule->>Database: Enforce ownership/company scope, load snapshot and timeline
    Database-->>OrderModule: Authorized order history
    OrderModule-->>OrderUI: Snapshot, status and payment/refund summary
    alt Eligible cancellation
        OrderActor->>OrderModule: Reason, expected version and idempotency key
        OrderModule->>Database: Lock order, validate transition and persist cancellation
        opt Paid order
            OrderModule->>PaymentModule: Request full refund after commit
        end
        OrderModule->>Database: Write notification outbox event
        OutboxWorker-->>OrderActor: Notify cancellation and refund status
    else Fulfillment status update
        OrderActor->>OrderModule: Next status and expected version
        OrderModule->>Database: Validate role, transition and tracking data, commit
        OutboxWorker-->>OrderActor: Notify status and safe tracking link
    end
```

# MFG-08: Assign customer and manage consultation — SD-11

```mermaid
sequenceDiagram
    actor CompanyAdmin as Company Admin
    actor Consultant as Sales Consultant
    participant ConsultationUI as S18-S21
    participant ConsultationModule as Consultation module
    participant Database as Database
    participant OutboxWorker as Outbox worker
    CompanyAdmin->>ConsultationUI: Select same-company customer and consultant
    ConsultationUI->>ConsultationModule: Assignment change with expected version and key
    ConsultationModule->>Database: Validate active membership and lock assignment
    Database-->>ConsultationModule: Current assignment and active requests
    ConsultationModule->>Database: Atomically change assignment and transfer active request ownership
    ConsultationModule->>Database: Append assignment history and outbox event
    OutboxWorker-->>Consultant: Notify new assignment
    Consultant->>ConsultationUI: Open assigned customer
    ConsultationUI->>ConsultationModule: Request customer context
    ConsultationModule->>Database: Check active assignment and load permitted summaries
    Database-->>ConsultationModule: Company-scoped context
    ConsultationModule-->>ConsultationUI: Context and consultation timeline
    Consultant->>ConsultationModule: Update consultation status/notes with expected version
    ConsultationModule->>Database: Validate transition and append interaction event
    ConsultationModule-->>ConsultationUI: Updated consultation and timeline
```

# MFG-10: Merge production and batch lifecycle — SD-12

```mermaid
sequenceDiagram
    actor Customer as Customer
    actor CompanyAdmin as Company Admin
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
    CheckoutModule->>Database: Create PendingContract order and immutable snapshots
    Note over OrderModule,MergeModule: Signing and verified payment make eligible order Confirmed
    CompanyAdmin->>MergeModule: View candidates and request estimate
    MergeModule->>Database: Recompute compatibility, limits and savings
    MergeModule-->>CompanyAdmin: Candidates, exclusions and estimate
    CompanyAdmin->>MergeModule: Create batch with acknowledgement, versions and key
    MergeModule->>Database: Lock and create Planned batch with immutable membership
    CompanyAdmin->>MergeModule: Start batch
    MergeModule->>Database: Commit start and membership state
    MergeModule->>OrderModule: Advance eligible orders to InProduction
    OutboxWorker-->>Customer: Notify committed batch/status event
    alt No batch after three calendar days
        Scheduler->>MergeModule: Process fallback
        MergeModule->>Database: Lock eligible unbatched opted-in orders
        MergeModule->>OrderModule: Advance to InProduction, retain price and due date
        OutboxWorker-->>Customer: Notify individual production fallback
    else Admin dissolves before start
        CompanyAdmin->>MergeModule: Dissolve planned batch
        MergeModule->>Database: Clear active links and retain membership history
    end
```

# MFG-11: Company analytics and export — SD-13

```mermaid
sequenceDiagram
    actor CompanyAdmin as Company Admin
    participant AnalyticsUI as S43
    participant AnalyticsModule as Analytics module
    participant AuthoritativeDB as Authoritative records
    participant ExportWorker as Export worker
    participant PrivateAssetStore as Private asset store
    CompanyAdmin->>AnalyticsUI: Select date range and metric
    AnalyticsUI->>AnalyticsModule: Request dashboard data
    AnalyticsModule->>AuthoritativeDB: Validate company scope and date range
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
