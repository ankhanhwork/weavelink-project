# Screen Spec: S22 Product Mockups

| Field | Value |
|---|---|
| Screen ID | `S22` |
| Screen name | Product Mockups |
| Actor | Customer owner |
| Priority | Should (MVP) |
| Belongs to module | [MFG-05](../specs/spec-MFG-05.md) |
| Route | `/designs/new?product_id={id}&mode=mockups` |
| Mockup image | img/S22-01-product-mockups.png |
| Status | Resolved implementation specification |


## 1. Purpose

**Shown when:** Customer previews the current S20 draft as calibrated 2D garment photos. Six angles like the approved reference: front flat, front shaped, left/right angle, back flat, back shaped. Switching thumbnails is deterministic and requires no AI request. Product templates may support fewer views; show unavailable views with a reason.

**The user leaves this screen when:** They return to S20/S22/S23 within the same draft or follow the existing authorized save/order navigation. Exiting the workspace destroys personal try-on buffers; unsaved design warnings follow S20.

**MVP scope (Should):** release the front and back views first; add the remaining angles of the six-view set when time allows. Views without a prepared template are shown as unavailable.

## 2. Mockup

![S22 Product Mockups](img/S22-01-product-mockups.png)

Illustrative synthetic sample, using S20's Dony storefront style. Fictional polo/artwork do not add a Published catalogue product. Written requirements govern behavior; no personal photo or actual customer information appears in the PNG.

### Mockup deviations

- Hide “Request design service” in the header and “Request a consultant instead” in MVP; S24 is post-MVP.

## 3. Element inventory

| # | Element | Type | Content / data source | Required | Validation |
|---|---|---|---|---|---|
| 1 | Shared mode tabs | Tabs | Design / Mockups / Try on you | Yes | Keep one draft and revision across modes. |
| 2 | Angle gallery | Six thumbnails | Product-supported template views | Yes | Accessible labels and selection; disable missing templates. |
| 3 | Large preview | Image/canvas | Current colour/material and side artwork | Yes | Physical mm positions mapped through calibrated per-view surfaces; correct side only. |
| 4 | Product/fabric summary | Read-only text | Current validated product options | Yes | Do not infer different fabric appearance from an unsupported image. |
| 5 | Back to design | Button | Return without save | Yes | Draft placements preserved. |
| 6 | Save/Continue order | Shared S20 bar | Immutable save / S30 | Yes | Current valid design; Saved version required to order. |
| 7 | Preview disclaimer | Text | Appearance only; not colour/fit/manufacturing proof | Yes | No AI or 3D claim. |

## 4. States

**Loading, access, errors and retry:** Show a labelled Loading state while reads resolve. A missing or inaccessible route returns a safe 401/403/404 without disclosing protected records. Error states show the API code, message, field_errors and request_id while preserving safe input. Retry transient reads; retry a mutation only with the original idempotency key and identical payload. Preserve safe user input after recoverable failures.

| State | What the user sees | Trigger |
|---|---|---|
| Empty | Garment preview without artwork | Draft has no asset on that side |
| Ready/success | Thumbnail and large image match current revision | Templates/draft validate |
| Unsupported | Disabled view or option with reason | Missing product/view/colour/material template |
| Error/retry | Recoverable template error; explicit reload, draft retained | Template/render read failure |
| Conflict | Revalidate current product version before preview/save | Stale product rules or invalid placement |

## 5. Interactions and navigation

| # | User action | System response | Goes to screen |
|---|---|---|---|
| 1 | Select angle | Render same draft into calibrated selected surface | S22 |
| 2 | Design tab | Return to physical placement controls | S20 |
| 3 | Try on you tab | Open presets/personal upload | S23 |
| 4 | Save/Continue order | Existing immutable S20 save/S30 eligibility rules | S25 / S30 |

## 6. Screen-level rules

| Rule ID | Rule | Source |
|---|---|---|
| SR-001 | Check access and ownership on the server; never trust submitted customer, company, role, price, stage or provider status. Apply the documented 401/403/404 behavior and field rules. | Project baseline |
| SR-002 | IDs are UUIDs; timestamps are UTC and displayed in Asia/Ho_Chi_Minh; money and quantities are integers. Mutations use expected versions and idempotency keys where specified. | Project baseline |
| SR-003 | Apply the owning module's lifecycle and validation rules; preserve immutable submitted snapshots and design versions. | Project baseline |
| SR-004 | Use documented project assumptions; do not invent factual company, author, client-approval or course identifiers. | Project baseline |

### Acceptance scenarios

1. A centred logo tracks the collar/placket-to-torso curve in both angled views, not the image bounding-box centre.
2. Chest placement stays on wearer left/right; back views do not contain front assets.
3. Cutout artwork follows perspective, folds, fabric light and placket occlusion without alpha seams.
4. Angle changes make no AI provider request, preserve physical coordinates and share current draft revision.
5. New template geometry requires visual approval at chest, centre and print bounds before release.

## 7. Linked requirements

| FR ID (from the module spec) | What this screen does for it |
|---|---|
| MFG-05/F-DES-015 | Implements the product mockups flow and its validation/session rules. |
| MFG-05/F-DES-001..003 | Shares the validated S20 draft; preserves explicit immutable save/order boundaries. |

## 8. Responsive and accessibility notes

Follow S20: 360px through desktop, navy/gold Dony storefront shell, labelled keyboard-operable tabs/buttons, visible focus and aria-live progress/errors. On narrow screens stack panels; make thumbnails horizontally scrollable and keep primary controls reachable. Text contrast >=4.5:1; controls >=24px. Images have descriptive alt text; alpha comparisons use a labelled checkerboard. Modal focus is trapped and restored to its trigger. Do not use colour alone for status.

## 9. Open questions

| # | Question | Blocking? | Status |
|---|---|---|---|
| 1 | Remaining screen behavior decisions? | No | Resolved by MFG-05 and the user-approved add-on scope. |

## Completion checklist

- [x] Route, actor, module, priority and illustrative image identified.
- [x] Fields, actions, ownership, validation and session boundaries defined.
- [x] Loading/error/retry/conflict/success states and navigation defined.
- [x] Acceptance scenarios and accessibility requirements defined.
