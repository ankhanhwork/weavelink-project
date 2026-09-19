# MFG-11 — Data Analytics

Implementation specification · Draft · 2026-09-19. Complete-system scope. Traceability: [function list](../docs/function-list.md), rows 84–86; shared contracts: [system decisions](../docs/system-decisions.md) D01, D02, D10, D11; factual provenance: [user input register](../docs/user-input-needed.md).

## Purpose, permissions and screen

Give Company Admin a read-only view of company performance and an export with matching filters. Analytics cannot mutate business records and never crosses company boundaries. System Admin has no implicit access to company analytics. S43 provides metric cards/charts, filters, refreshed-at/timezone, empty/error states, CSV/XLSX export and retry. Screen supports accessible charts with tabular equivalents.

## Data contract

Inputs use `start_date` inclusive and `end_date` exclusive in Asia/Ho_Chi_Minh calendar; default last 30 local calendar days, maximum 366 days. `metric_type` allowlist: revenue, orders, customer_growth (or all); optional `filter_parameters.product_id` must belong to authorized company. D02 paging and errors apply. Results include company_id from session, range, timezone, refreshed_at, metric series and aggregate values. ORDER revenue counts only the single accepted settlement per order by paid_at minus successful refunds of that accepted settlement by refunded_at; legitimate cancellation refunds reduce revenue. Duplicate/late receipts and their offsetting refunds are excluded together from sales revenue and shown only in reconciliation. SERVICE revenue is separately labeled using the corresponding accepted settlement/refund treatment. Order count uses created_at and includes all states, cancellation count separate. Customer growth counts distinct customers on first submitted order to that company in range. Product filter applies to related order/request product. Pending/failed attempts are excluded. Empty data returns zero/empty series.

`ExportRequest(id,company_id,actor_id,filters,format CSV|XLSX,watermark,created_at,status:Queued|Running|Succeeded|Failed,asset_id?,row_count?,error_code?)`. Export is asynchronous: request returns export_id/Queued, poll returns state/progress, only Succeeded returns a private asset link expiring in 10 minutes. Failed dependency/row-limit jobs report actionable error and can be retried with the same idempotency key/payload. Export rows use allowlisted columns by dataset: aggregate revenue date/value/currency; orders order UUID/created_at/status/product UUID/name/quantity/subtotal/discount/shipping/total/accepted-settled amount/accepted refund amount; customers customer UUID/first order date/order count. Exclude duplicate/late receipts and their offsetting refunds from sales exports; no emails, addresses, notes, payment references or secrets. Formula-leading spreadsheet cells are escaped. Max 100,000 rows. Snapshot watermark, timezone and filters accompany output.

## Function contracts

| Function | Inputs | Output |
|---|---|---|
| F-DA-001 Charts View (FR-001) | Optional `date_range` (two local dates, default last 30 days), optional `metric_type` allowlist. | `visual_charts`: typed view model `{range,timezone,refreshed_at,metrics:[{name,unit,points:[{date,value}],total}]}` for revenue, orders, customer growth. Not raw chart markup. |
| F-DA-002 Filter Logic (FR-002) | `filter_parameters` object: optional `start_date`, `end_date`, `product_id`, `metric_type`; page fields where table requested. | `refreshed_dataset_for_charts`: recalculated typed data using same definitions and company scope; zero data returns zeros, invalid range/product 422. |
| F-DA-003 Export Exec Logic (FR-003) | `dataset_selection` enum `{revenue,orders,customers}` or documented multi-selection; `file_format` enum CSV/XLSX (legacy File field means format choice, never client-uploaded file); date/product filters; Idempotency-Key. Follow-up request uses export_id to poll. | Queue job and return `{export_id,status:Queued}`; worker progresses Queued→Running→Succeeded/Failed. Success exposes 10-minute authorized private link plus format,row_count,watermark. Failures expose retryable error code; reject >100,000 rows with 422/narrower-filter guidance. Same key/payload returns same job; changed payload 409. |

## Flow and acceptance

Company Admin opens S43 → server reads company-scoped authoritative facts → charts render with range/watermark → optional filters reload same metric definitions → export creates private snapshot file → authorized download. No aggregation is client-calculated.

Use cases: UC-C21 View Dashboard (F-DA-001..002); UC-C22 Export Data (F-DA-003).

- **Given** valid date filters, **when** F-DA-001 loads, **then** response identifies inclusive start/exclusive end and Asia/Ho_Chi_Minh timezone and returns each metric using D10 definitions.
- **Given** a normal settled order payment and successful refund, **when** revenue is calculated, **then** net ORDER revenue subtracts refund by refunded_at and SERVICE revenue remains separate. Duplicate/late receipts and their offsetting refunds are both excluded; pending/failed attempts contribute zero.
- **Given** no source rows in range, **when** the dashboard loads, **then** it returns zero totals/empty series without fabricated sample values.
- **Given** a product UUID from another company, **when** filter is submitted, **then** 404/422 is returned and no cross-company values are disclosed.
- **Given** end_date is not after start_date or range exceeds 366 days, **when** submitted, **then** 422 field errors appear and previous chart data remains visible.
- **Given** an authorized export is requested, **when** queued, **then** it returns an export ID and status; polling reports Queued/Running/Succeeded/Failed, and only Succeeded exposes the short-lived download link. Repeating the same idempotency key/payload returns the same job; changed payload with same key is 409.
- **Given** an export contains a customer-controlled cell beginning with `=`, `+`, `-` or `@`, **when** written to CSV/XLSX, **then** it is escaped as text to prevent formula execution.
- **Given** source aggregation is unavailable, **when** S43 refreshes, **then** no stale values are presented as current without their watermark; return retryable 503 and preserve filters.

## Traceability and operations

Every query/export is company scoped at server query construction and audited with actor, filter, row count and watermark, without sensitive values. CSV/XLSX files are private assets and expire after 10 minutes at URL layer. F-DA-001..003 map to FR-001..003. Analytics and export are included in complete-system scope; old MVP exclusion is historical.
