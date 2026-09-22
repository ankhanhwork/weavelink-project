```mermaid
flowchart TD
    Browse["S01 / S08 / S09: public browsing"] --> Auth{"Authenticated customer?"}
    Auth -->|No| Login["S02 verification / S03 login"]
    Login --> Choice
    Auth -->|Yes| Choice{"Design route"}
    Choice -->|Self-design| Editor["S13: validate and save design"]
    Choice -->|Service| Request["S15: persist Submitted; notify Admin"]
    Request --> Status["S17: owned request status"]
    Status --> Assessment["S18: UnderReview complexity assessment"]
    Assessment -->|Simple fee 0| Approved["Approved request"]
    Assessment -->|Complex| Proposal["S17: FeeProposed; accept exact amount"]
    Proposal -->|Accept fee| Approved
    Assessment -->|Reject with reason| Rejected["Rejected request"]
    Status -->|Cancel| ServiceEnd["Cancelled request; no refund"]
    Assessment -->|Cancel| ServiceEnd
    Proposal -->|Cancel| ServiceEnd
    Approved -->|Cancel before assignment| ServiceEnd
    Approved --> Assign["S19: assign approved request"]
    Assign --> Delivery["S20 / S21: deliver design"]
    Delivery --> Designs["S17: owned orderable designs"]
    Editor --> Designs
    Designs --> OrderInput["S22: sizes and shipping"]
    OrderInput --> Merge{"S23: opt in?"}
    Merge -->|Yes| Policy["S24: accept merge policy"]
    Policy --> Review["S25: review quote and separate design fee"]
    Merge -->|No| Review
    Review -->|Expired or changed| OrderInput
    Review -->|Submit once| Persist["PendingContract order; atomic first-order fee allocation"]
    Persist --> Contract["S29 / S33: admin generates Ready contract"]
    Contract --> Sign["S34: PDF, reauthentication, signing"]
    Sign -->|Stale version| Contract
    Sign -->|Committed signature| Pay["S35: ORDER payment; AwaitingPayment"]
    Pay -->|Failed or expired attempt| Retry{"Retry or cancel?"}
    Retry -->|Retry| Pay
    Retry -->|Cancel| Cancel["S27: Cancelled; refund if paid"]
    Pay -->|Verified settlement| Confirmed["Confirmed order"]
    Confirmed -->|Eligible cancellation and no batch| Cancel
    Confirmed -->|Merge opted in| Batch["S42: batch or individual fallback"]
    Confirmed -->|Standard| Production["S29: InProduction"]
    Batch --> Production
    Production --> Shipped["S29: carrier and tracking; Shipped"]
    Shipped --> Delivered["S27 / S29: Delivered"]
```

Nodes found: 30

Arrows found: 41

Unreadable text: None.
