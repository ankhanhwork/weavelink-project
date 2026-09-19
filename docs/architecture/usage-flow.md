# End-to-end usage flow

Implementation flow revised 2026-09-19 under [system decisions](../system-decisions.md). Retains the DBIZ2 journey while resolving persistence, payment and merge boundaries. See the [screen catalogue](../screen-list.md) for routes.

```mermaid
flowchart TD
    Browse["S01 / S08 / S09: public browsing"] --> Auth{"Authenticated customer?"}
    Auth -->|No| Login["S02 verification / S03 login"]
    Login --> Choice
    Auth -->|Yes| Choice{"Design route"}
    Choice -->|Self-design| Editor["S13: validate and save design"]
    Choice -->|Service| Request["S15: persist AwaitingPayment request"]
    Request --> ServicePay["S16: SERVICE payment"]
    ServicePay -->|Verified success| Assign["S18 / S19: assign paid request"]
    ServicePay -->|Failure| ServiceRetry{"Retry or cancel?"}
    ServiceRetry -->|Retry before expiry| ServicePay
    ServiceRetry -->|Cancel or expire| ServiceEnd["Cancelled / Expired request"]
    Assign --> Delivery["S20 / S21: deliver design"]
    Delivery --> Designs["S17: owned orderable designs"]
    Editor --> Designs
    Designs --> OrderInput["S22: sizes and shipping"]
    OrderInput --> Merge{"S23: opt in?"}
    Merge -->|Yes| Policy["S24: accept merge policy"]
    Policy --> Review["S25: review server quote"]
    Merge -->|No| Review
    Review -->|Expired or changed| OrderInput
    Review -->|Submit once| Persist["PendingContract order and preference only"]
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

Server guards D05..D09 control transitions. Browser redirects, email delivery and display labels never change business state independently. Customers reopen orders in S26/S27 while awaiting admin contract generation; generation failure leaves PendingContract visible and retryable by admin. Signing failure without a stale version stays S34 and preserves consent input safely.

## Staff and operations paths

- Company Admin: S10 -> S11/S12/S14 for products; S18 -> S19 for assignments; S28 -> S29 -> S33 for contracts; S30 -> S31/S32 for templates; S36 -> S37 for reconciliation/refunds; S42 for batches; S43 for analytics/export.
- Sales Consultant: S20 -> S21 for assigned consultations and design delivery; S28/S29 expose only assigned customer orders and fulfillment actions.
- System Admin: S41 for companies/staff; S39 for configuration/backup/restore; S40 for redacted audit logs.
- All authenticated roles: S06 profile, S07 password, S38 notifications. Recovery enters S04/S05 before login.
