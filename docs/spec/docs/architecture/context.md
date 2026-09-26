# Context Diagram

```mermaid
flowchart LR
    Guest["Guest"] -->|Browse, register, recover| Platform["WeaveLink"]
    Buyer["Business Buyer"] -->|Commission uniforms for internal use| Platform
    Reseller["Reseller Shop"] -->|Submit own designs and commission production for resale| Platform
    Platform -->|Configurable garment bases, design, sample, order and tracking| Buyer
    Platform -->|Configurable garment bases, design, sample, order and tracking| Reseller
    Consultant["Sales"] -->|Assigned consultations, designs, fulfillment| Platform
    Admin["Sales Admin"] -->|Dony products, assignments, contracts, payments and batches| Platform
    Platform -->|Dony operations and analytics| Admin
    SystemAdmin["System Admin"] -->|Dony staff accounts and system operations| Platform
    Platform -->|Redacted audit and job results| SystemAdmin
    Platform -->|Payment, query, refund| Gateway["VNPay sandbox / configured gateway"]
    Gateway -->|Verified server events| Platform
    Platform -->|Outbox delivery| Mail["SMTP / development email sink"]
    Platform -->|Sanitized intent and approved aggregate facts only| AI["Restricted AI adapter; provider undecided"]
    AI -->|Typed query proposal and explanation; no business actions| Platform
```

Nodes found: 10

Arrows found: 15

Unreadable text: None.

The AI provider/model is chosen and configured at Plan under MFG-11 I-01; its product data boundary and page-memory-only conversation policy are already defined in MFG-11 5.7. It has no direct database or business-action access. Sales Admin alone accesses commercial analytics; System Admin receives redacted operational diagnostics.

Guest catalog browsing remains public but emits no analytics behavior events. Only authenticated Customer interactions and authoritative customer-linked business events feed MFG-11; no guest-to-login identity integration is introduced.
