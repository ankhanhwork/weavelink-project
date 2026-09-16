# Context Diagram

```mermaid
flowchart LR
    CompanyAdmin[COMPANY ADMIN]
    SystemAdmin[SYSTEM ADMIN]
    SalesConsultant[SALE CONSULTANT]
    Weavelink[WEAVELINK]
    PaymentGateway[PAYMENT GATEWAY]
    Customer[CUSTOMER]

    CompanyAdmin -->|Generate & Update Contract<br/>Assign Consultant| Weavelink
    Weavelink -->|Dashboard Data<br/>Sale Report| CompanyAdmin
    SystemAdmin -->|Account Info<br/>Assign Roles| Weavelink
    Weavelink -->|Monitor System Logs<br/>Backup & Restore Data<br/>Configure System| SystemAdmin
    SalesConsultant -->|Customer Status Update<br/>Consultation Note| Weavelink
    Weavelink -->|Lead List & Information<br/>Assignment| SalesConsultant
    Weavelink -->|Payment Info| PaymentGateway
    PaymentGateway -->|Transaction Status| Weavelink
    Weavelink -->|Product Catalog<br/>Order Status<br/>Digital Contract| Customer
    Customer -->|Account Info<br/>Order Request<br/>Design Draft| Weavelink
```

Nodes found: 6

Arrows found: 10

Unreadable text: None.
