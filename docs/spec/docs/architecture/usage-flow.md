```mermaid
flowchart TD
    Browse["S01 / S14 / S15: public browsing"] --> Auth{"Authenticated customer?"}
    Auth -->|No| Login["S04 verification / S05 login"]
    Login --> Choice
    Auth -->|Yes| Choice{"Design route"}
    Choice -->|Existing saved design| Designs
    Choice -->|Self-design| Editor["S20: validate and save design"]
    Choice -->|Service| Request["S24: persist Submitted; notify Admin"]
    Request --> Status["S26: owned request status / fee acceptance"]
    Status --> Assessment["S27: UnderReview complexity assessment"]
    Assessment -->|Simple fee 0| Approved["Approved request"]
    Assessment -->|Complex| Proposal["S26: FeeProposed; accept exact amount"]
    Proposal -->|Accept fee| Approved
    Assessment -->|Reject with reason| Rejected["Rejected request"]
    Status -->|Cancel| ServiceEnd["Cancelled request; no refund"]
    Assessment -->|Cancel| ServiceEnd
    Proposal -->|Cancel| ServiceEnd
    Approved -->|Cancel before assignment| ServiceEnd
    Approved --> Assign["S27: eligible request follows lead owner; due may be missing"]
    Assign --> Delivery["S29: create and share immutable version"]
    Delivery --> Feedback["S26: review versions and reply / request revision"]
    Feedback -->|Revision| Delivery
    Feedback -->|Owner approval| Designs["S25: owned orderable designs"]
    Editor --> Designs
    Designs --> OrderInput["S30: sizes and shipping"]
    OrderInput -->|MVP standard path| Review
    OrderInput -->|After reviewed MFG-10 activation| Merge{"S31: eligible flexible terms offered and accepted?"}
    Merge -->|Yes| Policy["S32: read terms; explicit acceptance on S31"]
    Policy --> Review["S33: review quote and separate design fee"]
    Merge -->|No| Review
    Review -->|Expired or changed| OrderInput
    Review -->|Submit once| Persist["AwaitingDigitalApproval order; immutable quote snapshot"]
    Persist --> Digital["S35: customer approves digital design"]
    Digital --> Sample["S37: Dony prepares and ships physical sample"]
    Sample --> SampleDecision{"S35: received sample approved?"}
    SampleDecision -->|Revise| Digital
    SampleDecision -->|Approve| Contract["S37 / S39: PendingContract; admin generates Ready contract"]
    Contract --> Sign["S38: PDF, consent and matching name; stronger authentication post-MVP"]
    Sign -->|Stale version| Contract
    Sign -->|Committed signature| Deposit["S40: DEPOSIT payment; AwaitingDeposit"]
    Deposit -->|Failed or expired attempt| Retry{"Retry or cancel?"}
    Retry -->|Retry| Deposit
    Retry -->|Cancel| Cancel["S35: Cancelled; refund if paid"]
    Deposit -->|Verified deposit| Confirmed["Confirmed order"]
    Confirmed -->|Eligible preproduction cancellation; release schedule and revalidate lock| Cancel
    Confirmed -->|MFG-10 active; standard or flexible| Batch["S46: daily-capacity sewing plan; flexible waits 7 workdays then 8-14 production workdays; Admin approves/locks/starts; expiry only notifies"]
    Confirmed -->|MVP standard path| Production["S37: InProduction"]
    Batch --> Production
    Production --> Shipped["S37: carrier and tracking; Shipped"]
    Shipped --> Received["S35 / System: customer receipt or existing proof-based timer; DeliveredAwaitingBalance"]
    Received -->|Positive balance| Balance["S40: BALANCE payment"]
    Received -->|Zero balance; authoritative completion| Completed
    Balance -->|Verified settlement| Completed["Completed order"]
```





The first diagram shows the complete-system business paths; [MVP scope](../../mvp-scope-proposal.md) owns the MVP slice; in the MVP, receipt is confirmed by the Customer or by Sales Admin on the Customer's behalf (MFG-06 BR-019). Service design and merge remain deferred until their modules are active. Returning to an existing design does not imply a new editor/save step. The sample-revision arrow includes the new bound design/quote approval cycle defined by MFG-06.

## Analytics usage (Should extension)

```mermaid
flowchart TD
    Admin[Sales Admin] --> Dashboard[S47: Overview or Journey and conversion]
    Facts[Committed lifecycle facts and validated interactions] --> Metric[Shared metric layer]
    Dashboard --> Context[Validate filters, unit, cohort and cutoff]
    Context --> Metric
    Metric --> Result[Result snapshot, definitions and coverage]
    Result --> Charts[Charts and waiting detail]
    Charts --> Record[Reauthorize and open S37 supporting order]
    Result --> Export[Matching asynchronous private export]
    Result --> Prompt[AI panel with current result and stage]
    Prompt --> Plan[Validate typed plan; Apply changed context]
    Plan --> Metric
    Metric --> Answer[Validate explanation against aggregate evidence]
    Answer --> Source[Original result source or explicit unavailable state]
```

Authenticated product-entry, explicit-intent and order identity/formulas belong to MFG-11. Guest browsing produces no analytics events and is never replayed after login. Explicit new design/reorder creates a new intent; reload/edit/requote/payment retry resumes the existing one. A missing link is not a dropout; sample rework, contract preparation, customer signing and payment waits are separate. AI does not change any node of the business flow. Disabled branches and missing tracking display coverage states instead of artificial zero conversion.

Reporting covers the rolling last 12 calendar months. Observed nonprogression is shown without an inactivity-based abandonment rule. AI conversation remains only on the active dashboard page and is cleared on page reload/close/navigation away, logout or access revocation; closing only the panel may preserve it until that page ends.

Unknown-model leads are triaged only by Sales Admin in S27 before assignment/assessment. S25 is the gallery, S26 owns request and version review. Physical-sample rework remains the existing MFG-06 design/quote cycle without a revision cap or separate sample fee.
