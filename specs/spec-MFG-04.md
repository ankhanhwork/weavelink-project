# MFG-04 — Product Catalog

Implementation specification · Draft · 2026-09-19. Complete-system scope. Traceability: [function list](../docs/function-list.md), rows 25–35; shared contracts: [system decisions](../docs/system-decisions.md) D01–D04, D06, D09, D11; factual provenance: [user input register](../docs/user-input-needed.md).

## Purpose, access and screens

Provide public discovery of published products and company-scoped catalog/rule administration. Guest can browse/search published products of Active companies only. Company Admin can manage products in their company. System Admin does not implicitly manage product content. Every route/object is checked server-side. Screens: S08 catalog grid/search, S09 product details, S10 Company Admin product dashboard, S11 product create, S12 product edit, S14 product design rules for the same product (corrected legacy duplicate title). S14 edits sizes, colors, materials, print methods/areas, options/surcharges and `max_units_per_order`; 2D print-area preview is required, 3D is not. Mutations use optimistic versioning and loading/empty/error/success states.

## Entities and invariants

`Product(id: UUID,company_id: UUID,name,sku,description,category,unit_price_vnd:int,supported_sizes[],colors[],materials[],print_methods[],design_rules,max_units_per_order:int,image_asset_ids[],status Draft|Published|Hidden|Archived,version,created_at,updated_at)`. SKU uniqueness is `(company_id,sku)`; product routes/public canonical URLs use globally unique UUID. Amounts nonnegative integer VND; options/surcharges are nonnegative integer VND per unit. `max_units_per_order` is a finite integer 1..10000, not warehouse stock or reservation capacity. Publish requires name, SKU, price, category, at least one safe image, supported sizes/colors/materials and max_units_per_order. Images PNG/JPEG/WebP, max 10 MiB each and five/request, validate actual MIME and scan. Archive is terminal, removes public visibility and preserves references. Draft/Hidden/Archived are unavailable for checkout; products in Suspended/Deleted companies are omitted from public catalog and cannot start new design/order/payment activity. Product/rule/capacity changes invalidate unconsumed quotes; submitted orders retain immutable snapshots. Quote and submission total size quantity must be <= max_units_per_order; otherwise 422 `CAPACITY_EXCEEDED`. Capacity is not decremented/reserved; accepted work is scheduled in batching/production queues.

## Function contracts (FR-001..011)

| Function | Actor / inputs | Result and rules |
|---|---|---|
| F-PROD-001 Catalog Grid View (FR-001) | Guest; optional `category_filter` UUID/slug, required `page_number` >=1, optional allowlisted `sorting_option` (name, price, updated_at asc/desc), page_size 1..100. | S08 view model of Published products in grid: image, name, starting price, category, pagination. Empty result is empty array with metadata. |
| F-PROD-002 Product Detail View (FR-002) | Guest; canonical route `product_id` UUID. Internal company-scoped management lookup may use `(company_id,sku)` but public clients may not submit an unscoped SKU. | S09 details, images, specs/options, price and design entry point; Hidden/Draft/Archived are 404 publicly. |
| F-PROD-003 Search Result View (FR-003) | Guest; optional `search_keyword` <=100 trimmed chars, optional filters category/size/color/material/price range, pagination. | Filtered Published products, relevance/name/price sorting; no match returns empty list. Invalid filter/range 422. |
| F-PROD-004 Management Dashboard (FR-004) | Company Admin session; company ID from session; filters/page. | S10 management view for same-company products and permission-derived actions; no submitted credentials/permissions are trusted. |
| F-PROD-005 Add Product Form (FR-005) | Company Admin session; no body. | S11 create form model with content fields and image upload constraints; draft can be saved incomplete. |
| F-PROD-006 Save Product Logic (FR-006) | name 1..150, `sku` 1..64, `price` integer VND, description <=5000, category, supported attributes, `max_units_per_order` integer 1..10000, image UUIDs; idempotency key. | Create Draft and return `new_product_id`, status/version. Reject invalid/foreign assets, negative price, duplicate `(company_id,sku)`, invalid capacity; publish is separate validation. |
| F-PROD-007 Edit Product Form (FR-007) | `product_id` UUID and same-company Company Admin. | S12 prefills editable current product values and version; foreign-company/missing identifier 404. |
| F-PROD-008 Update Product Logic (FR-008) | `product_id`, allowlisted `changed_attributes`, `expected_version`. | Atomic update returns record/version. Validate each changed field; rule-affecting edit increments product_version and invalidates quotes; ordered snapshots remain unchanged. Stale version 409. |
| F-PROD-009 Delete Prompt UI (FR-009) | Same-company Company Admin, product UUID. | S12 confirmation with product identity and impact; require explicit confirm and expected version. |
| F-PROD-010 Delete Product Logic (FR-010) | Confirmed product UUID and expected_version. | Set status Archived (soft delete), hide immediately from catalog and retain order/design references. Repeat archive is success; any stale write 409. |
| F-PROD-011 Toggle Status Logic (FR-011) | Product UUID, requested target Published or Hidden, expected_version. | Explicit set (not blind toggle) to avoid retry race; Published validation is all-or-nothing. Return updated dashboard view/status/version; Archived cannot transition. |

## Flow and acceptance

Use cases: UC-G01 View Catalog (F-PROD-001..002); UC-G02 Search Product (F-PROD-003); UC-C24 Add Product (F-PROD-004..006); UC-C25 Update Product (F-PROD-007..008); UC-C26 Delete Product (F-PROD-009..010); UC-C27 Publish Product (F-PROD-011). Guest opens S08 → applies search/category filters → opens S09 → views options and enters design flow. Company Admin enters S10 → creates Draft in S11 or edits content in S12 → S14 edits rules/capacity → validates → publishes; hiding/archive removes public listing while submitted-order snapshots remain.

- **Given** published products exist, **when** a Guest opens S08 with valid page/filter, **then** only Published products for Active companies appear with accurate pagination and integer VND prices.
- **Given** search has no matches, **when** filters apply, **then** empty results and clear filters action appear; malformed page, sort or range returns 400/422 and does not broaden the query.
- **Given** a Company Admin uploads an executable renamed as an image or a file over 10 MiB, **when** saved, **then** upload is rejected and no product references it.
- **Given** a Draft lacks required attributes or safe image, **when** publish is requested, **then** 422 field errors identify missing fields and status remains Draft/Hidden.
- **Given** another company's admin guesses a product UUID, **when** they read or mutate it, **then** response is 404 and no change occurs.
- **Given** two edits use one product version, **when** they race, **then** one commits and the stale save returns 409; retry cannot overwrite the newer value.
- **Given** a product referenced by a submitted order, **when** admin archives or edits it, **then** new public selection/quotes are blocked or invalidated while order snapshot remains intact.
- **Given** a product status is Published, **when** admin sets Hidden, **then** it disappears from public search/catalog immediately; repeating the same target is a no-op success.
- **Given** admin edits S14 design rules or max_units_per_order, **when** saved, **then** S14 changes product version and unconsumed quotes expire; future design/quote validation uses new rules. Quantity above max_units_per_order returns 422 CAPACITY_EXCEEDED. Existing orders retain their captured version.

## Errors and traceability

All list operations follow D02 pagination; all writes require expected_version, create requests use idempotency. Product images are private assets with authorized expiring URLs; strings render as text. S08/S09 failures use retryable service errors without exposing drafts. All eleven F-PROD IDs map one-to-one to matching FR IDs. Historical MVP exclusions do not constrain the complete system.
