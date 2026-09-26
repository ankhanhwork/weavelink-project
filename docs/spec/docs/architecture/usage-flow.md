```mermaid
flowchart TD
    Browse["S01 / S08 / S09: public browsing"] --> Auth{"Authenticated customer?"}
    Auth -->|No| Login["S02 verification / S03 login"]
    Login --> Choice
    Auth -->|Yes| Choice{"Design route"}
    Choice -->|Existing saved design| Designs
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
    OrderInput -->|MVP standard path| Review
    OrderInput -->|After MFG-10 activation| Merge{"S23: opt in?"}
    Merge -->|Yes| Policy["S24: accept merge policy"]
    Policy --> Review["S25: review quote and separate design fee"]
    Merge -->|No| Review
    Review -->|Expired or changed| OrderInput
    Review -->|Submit once| Persist["AwaitingDigitalApproval order; immutable quote snapshot"]
    Persist --> Digital["S27: customer approves digital design"]
    Digital --> Sample["S29: Dony prepares and ships physical sample"]
    Sample --> SampleDecision{"S27: received sample approved?"}
    SampleDecision -->|Revise| Digital
    SampleDecision -->|Approve| Contract["S29 / S33: PendingContract; admin generates Ready contract"]
    Contract --> Sign["S34: PDF, consent and matching name; stronger authentication post-MVP"]
    Sign -->|Stale version| Contract
    Sign -->|Committed signature| Deposit["S35: DEPOSIT payment; AwaitingDeposit"]
    Deposit -->|Failed or expired attempt| Retry{"Retry or cancel?"}
    Retry -->|Retry| Deposit
    Retry -->|Cancel| Cancel["S27: Cancelled; refund if paid"]
    Deposit -->|Verified deposit| Confirmed["Confirmed order"]
    Confirmed -->|Eligible cancellation and no batch| Cancel
    Confirmed -->|Merge opted in| Batch["S42: system recommends compatible groups for 7 days; Sales Admin reviews and starts batch; scheduler starts individual fallback at expiry"]
    Confirmed -->|Standard| Production["S29: InProduction"]
    Batch --> Production
    Production --> Shipped["S29: carrier and tracking; Shipped"]
    Shipped --> Received["S27 / System: customer receipt or existing proof-based timer; DeliveredAwaitingBalance"]
    Received -->|Positive balance| Balance["S35: BALANCE payment"]
    Received -->|Zero balance; authoritative completion| Completed
    Balance -->|Verified settlement| Completed["Completed order"]
```

Nodes found: 35

Arrows found: 50

Unreadable text: None.


The first diagram shows the complete-system business paths; README owns the MVP slice. Service design and merge remain deferred until their modules are active. Returning to an existing design does not imply a new editor/save step. The sample-revision arrow includes the new bound design/quote approval cycle defined by MFG-06.

## Analytics usage (Should extension)

```mermaid
flowchart TD
    Admin[Sales Admin] --> Dashboard[S43: Overview or Journey and conversion]
    Facts[Committed lifecycle facts and validated interactions] --> Metric[Shared metric layer]
    Dashboard --> Context[Validate filters, unit, cohort and cutoff]
    Context --> Metric
    Metric --> Result[Result snapshot, definitions and coverage]
    Result --> Charts[Charts and waiting detail]
    Charts --> Record[Reauthorize and open S29 supporting order]
    Result --> Export[Matching asynchronous private export]
    Result --> Prompt[AI panel with current result and stage]
    Prompt --> Plan[Validate typed plan; Apply changed context]
    Plan --> Metric
    Metric --> Answer[Validate explanation against aggregate evidence]
    Answer --> Source[Original result source or explicit unavailable state]
```

Authenticated product-entry, explicit-intent and order identity/formulas belong to MFG-11. Guest browsing produces no analytics events and is never replayed after login. Explicit new design/reorder creates a new intent; reload/edit/requote/payment retry resumes the existing one. A missing link is not a dropout; sample rework, contract preparation, customer signing and payment waits are separate. AI does not change any node of the business flow. Disabled branches and missing tracking display coverage states instead of artificial zero conversion.

Reporting covers the rolling last 12 calendar months. Observed nonprogression is shown without an inactivity-based abandonment rule. AI conversation remains only on the active dashboard page and is cleared on page reload/close/navigation away, logout or access revocation; closing only the panel may preserve it until that page ends.
