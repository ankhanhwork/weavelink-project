# VNPay adapter contract

Protocol baseline: PAY 2.1.0, sandbox first. Reviewed 2026-09-19. Business settlement, idempotency and refund rules are WeaveLink decisions [D08](../system-decisions.md), not gateway guarantees.

## Protocol requirements

Use `vnp_Version=2.1.0`, command `pay`, merchant code, unique attempt reference, `VND`, and `vnp_Amount=amount_vnd*100`. Dates use `yyyyMMddHHmmss` in GMT+7. Include create/expiry dates, customer IP, locale, order description/type and registered return URL. Select HMAC-SHA512; sort parameter names and encode consistently with the official signing examples; exclude signature fields before verifying callbacks. Compare signatures in constant time. Server IPN changes stored state; browser return displays it. IPN responses use `RspCode`: 00 committed, 02 already processed, 01 unknown reference, 04 wrong amount, 97 invalid signature, 99 processing error. Use the documented sandbox payment URL. [Official PAY integration](https://sandbox.vnpayment.vn/apis/docs/thanh-toan-pay/pay.html).

Query/refund use POST JSON to the merchant transaction API with command-specific field ordering for checksums; do not reuse payment-query-string signing. Preserve original transaction reference/date. Full refund uses transaction type 02. An accepted API request is not proof of settlement: inspect verified transaction status, amount and merchant/reference. Duplicate/processing responses require reconciliation, not a fresh blind refund. Verify response signatures with the command-specific response schema. [Official query and refund integration](https://sandbox.vnpayment.vn/apis/docs/truy-van-hoan-tien/querydr%26refund.html).

## WeaveLink boundary decisions

- Persist attempt/reference before redirect. Hosted-payment URLs come only from the configured adapter; never accept arbitrary redirect destinations.
- Map normalized verified success to D08. Only one successful attempt fulfills a resource; extra received funds create a refund obligation. Retain provider codes separately from business enums.
- API routes: `GET /api/payments/vnpay/ipn`, `GET /payments/vnpay/return`, and authenticated `GET /api/payments/:id`. Return route resolves the attempt to S16 or S35 and reauthenticates the owner when their session expired. It never takes ownership from a query parameter.
- Until reconciliation is conclusive, show Processing with last_checked_at. Query first after the 15-minute attempt expiry, then 5/30 minutes later; after three unsuccessful checks notify Company Admin for manual retry in S37. Unknown status does not authorize another active attempt.
- Keep journal/event deduplication outside restorable business snapshots. Acknowledge during maintenance only after durable ingress; replay before reopening business writes.
- Demo amounts must be positive and at most 9999999999 VND, satisfying the protocol's scaled 12-digit amount field; reject out-of-range quotes/fees before payment. No free SERVICE checkout in this version.
- Secret references and merchant configuration are provisioned per deployment/company, never in Git. Missing configuration returns a clear service-unavailable state; never fall back silently to a fake paid result.

## Required adapter tests when code is implemented

Known-good signing vector; bad hash; altered amount/reference/merchant; successful IPN before/after return; duplicate and out-of-order IPN; expired session with late success; competing attempts; cancellation race; query success versus actual transaction status; duplicate refund after timeout; outage and reconciliation; restore replay. These are acceptance requirements, not tests claimed to have run in this documentation-only repository.
