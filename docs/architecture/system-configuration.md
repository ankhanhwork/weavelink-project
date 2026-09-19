# 1.3b System Overall Configuration

This system provides services via the Web in a client-server format. The diagram shows logical boundaries; they may be deployed as one modular application.

```mermaid
flowchart TD
    PublicUI["Storefront"] --> Edge["HTTPS API: session, CSRF, authorization"]
    StaffUI["Staff and operations UI"] --> Edge
    Edge --> Identity["MFG-01 / 02 / 03"]
    Edge --> Business["MFG-04 through 10"]
    Edge --> Analytics["MFG-11"]
    Edge --> Ops["MFG-12"]
    Identity --> DB[("Transactional database")]
    Business --> DB
    Analytics --> DB
    Ops --> DB
    Business --> Assets["Private designs and PDFs"]
    DB --> Worker["Durable outbox and scheduled worker"]
    Worker --> Mail["SMTP / email sink"]
    Business --> VNPay["VNPay adapter"]
    VNPay --> Journal["Durable payment-event journal"]
    Journal --> Worker
    Worker --> DB
    Ops --> Backups["Encrypted database and asset backups"]
    Ops --> Journal
```

Nodes found: 15

Arrows found: 18

Unreadable text: None.
