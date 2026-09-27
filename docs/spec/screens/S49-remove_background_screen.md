# Screen Spec: S49 Remove Background

| Field | Value |
|---|---|
| Screen ID | `S49` |
| Screen name | Remove Background |
| Actor | Customer owner |
| Priority | P1 |
| Belongs to module | [MFG-05](../specs/spec-MFG-05.md) |
| Route | S13 modal; `/designs/new?product_id={id}&mode=design&dialog=remove-background&asset_id={asset_id}` |
| Mockup image | img/S49-remove_background_screen.png |
| Status | Resolved implementation specification |

## 1. Purpose

**Shown when:** Customer reviews removal on a selected owned draft artwork. Does not save a design. Returning to S13 applies only an explicitly reviewed result; cancel/close leaves artwork unchanged. Modal may be opened only for an eligible selected asset. Direct links reconstruct authorization/draft selection before opening.

**The user leaves this screen when:** They return to S13/S50/S51 within the same draft or follow the existing authorized save/order navigation. Exiting the workspace destroys personal try-on buffers; unsaved design warnings follow S13.

## 2. Mockup

![S49 Remove Background](img/S49-remove_background_screen.png)

Illustrative synthetic sample, using S13's Dony storefront style. Fictional polo/artwork do not add a Published catalogue product. Written requirements govern behavior; no personal photo or actual customer information appears in the PNG.

## 3. Element inventory

| # | Element | Type | Content / data source | Required | Validation |
|---|---|---|---|---|---|
| 1 | Original/result comparison | Two labelled image panels | Selected artwork and transparent result on checkerboard | Yes | Original remains immutable in session. |
| 2 | Removal method | Select | Subject segmentation / Solid background | Yes | Solid mode removes border-connected colours only; subject failures offer solid fallback. |
| 3 | Tolerance | Slider/numeric | Integer 5–100, default 35 | Solid only | Larger tolerance expands eligible background; no internal disconnected colour removal. |
| 4 | Remove background | Button | Start transient processing | Yes | Disabled while pending; validate actual PNG/JPEG/WebP, <=10 MiB, <=16M pixels. |
| 5 | Apply / Cancel / Close | Buttons | Confirm result or dismiss | Yes | Apply only current successful output; preserve X/Y/width/height, side, selected asset; increment draft revision. |
| 6 | Restore original | S13 action | Original image from this draft session | After apply | Restores pixels, retains physical placement; no persistent undo guarantee after session ends. |

## 4. States

| State | What the user sees | Trigger |
|---|---|---|
| Loading/processing | Original visible, result progress; Apply disabled | Processing request starts |
| Ready | Method/tolerance controls, checkerboard result slot | Eligible selection |
| Success | Current original/result comparison; Apply enabled | Processing completes for matching asset/session |
| Error | Safe actionable code/message; original preserved | Unsafe input, segmentation unavailable, network/rate-limit failure |
| Conflict | Discard late result; ask to process current artwork | Asset removed/replaced, revision/session changes |
| Retry | Explicit Remove again with current input | Recoverable error; no automatic save |
| Forbidden/not found | Safe 401/403/404 without asset disclosure | Ownership/authorization fails |

## 5. Interactions and navigation

| # | User action | System response | Goes to screen |
|---|---|---|---|
| 1 | Remove | Validate and process; never save automatically | S49 |
| 2 | Apply | Replace draft pixels, retain geometry, invalidate try-on | S13 |
| 3 | Cancel/Close/Escape | Discard review; restore focus to trigger | S13 |
| 4 | Restore original (S13) | Restore original within current session | S13 |

## 6. Screen-level rules

| Rule ID | Rule | Source |
|---|---|---|
| SR-001 | Server enforces owner authorization and current product rules; private errors do not disclose other customer data. | MFG-05 |
| SR-002 | Preserve immutable saved designs; preview processing never changes an ordered snapshot or makes a draft orderable. | S13 / MFG-05 BR-001 |
| SR-003 | Personal photos/results remain session-only; template and explicitly saved artwork storage are separate. | MFG-05 BR-010–012 |

### Acceptance scenarios

1. White background around an illustration disappears while disconnected white details inside remain.
2. Apply on a chest logo retains exact side and X/Y/width/height; transparent edges have no dark halo.
3. Cancel, error and late output never mutate the draft; successful apply can be restored in-session.
4. A processed artwork is persisted only through S13 explicit validated save; review buffers are transient.

## 7. Linked requirements

| FR ID (from the module spec) | What this screen does for it |
|---|---|
| MFG-05/F-DES-014 | Implements the remove background flow and its validation/session rules. |
| MFG-05/F-DES-001..003 | Shares the validated S13 draft; preserves explicit immutable save/order boundaries. |

## 8. Responsive and accessibility notes

Follow S13: 360px through desktop, navy/gold Dony storefront shell, labelled keyboard-operable tabs/buttons, visible focus and aria-live progress/errors. On narrow screens stack panels; make thumbnails horizontally scrollable and keep primary controls reachable. Text contrast >=4.5:1; controls >=24px. Images have descriptive alt text; alpha comparisons use a labelled checkerboard. Modal focus is trapped and restored to its trigger. Do not use colour alone for status.

## 9. Open questions

| # | Question | Blocking? | Status |
|---|---|---|---|
| 1 | Remaining screen behavior decisions? | No | Resolved by MFG-05 and the user-approved add-on scope. |

## Completion checklist

- [x] Route, actor, module, priority and illustrative image identified.
- [x] Fields, actions, ownership, validation and session boundaries defined.
- [x] Loading/error/retry/conflict/success states and navigation defined.
- [x] Acceptance scenarios and accessibility requirements defined.
