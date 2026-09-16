# SD-01: Browse Product Catalog (Guest)

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

# SD-02: Sign Up

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

# SD-03: Log In

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

# SD-04 – Search and View Product Detail

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

# SD-05A: Self Design Product

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

# SD-05B: Request Design Service

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

# SD-06: View Saved Design

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

# SD-07: Create Order

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

# SD-08: View and Sign Digital Contract

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

# SD-09: Make Order Payment

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
        PaymentGateway-->>PaymentService:
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
