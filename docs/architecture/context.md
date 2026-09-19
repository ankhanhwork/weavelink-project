# System context

WeaveLink is a web platform for made-to-order garments, customer designs and paid design services. This revised context resolves inherited actor boundaries using [D01](../system-decisions.md). A company is a tenant; a customer may purchase from multiple companies, but one order belongs to one company.

```mermaid
flowchart LR
    Guest["Guest"] -->|Browse, register, recover| Platform["WeaveLink"]
    Customer["Customer"] -->|Own designs, requests, orders, signatures| Platform
    Platform -->|Catalog, results and tracking| Customer
    Consultant["Sales Consultant"] -->|Assigned consultations, designs, fulfillment| Platform
    Admin["Company Admin"] -->|Own company products, assignments, contracts, batches| Platform
    Platform -->|Company transactions and analytics| Admin
    SystemAdmin["System Admin"] -->|Company accounts and system operations| Platform
    Platform -->|Redacted audit and job results| SystemAdmin
    Platform -->|Payment, query, refund| Gateway["VNPay sandbox / configured gateway"]
    Gateway -->|Verified server events| Platform
    Platform -->|Outbox delivery| Mail["SMTP / development email sink"]
```

Member denotes authenticated users, not an additional assignable role. Gateway/email are external actors; the worker executes trusted events and scheduled jobs. Production planning is internal; carrier and tracking data are staff-entered and no carrier API is assumed. See the [screen catalogue](../screen-list.md) for entry points.
