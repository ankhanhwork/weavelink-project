# Screen Spec: S51 Virtual Try On

| Field | Value |
|---|---|
| Screen ID | `S51` |
| Screen name | Virtual Try On |
| Actor | Customer owner |
| Priority | P2 |
| Belongs to module | [MFG-05](../specs/spec-MFG-05.md) |
| Route | `/designs/new?product_id={id}&mode=try-on` |
| Mockup image | img/S51-virtual_try_on_screen.png |
| Status | Resolved implementation specification |

## 1. Purpose

**Shown when:** Customer sees synthetic male/female/child mockups of the current designed polo and may upload their own photo for OpenAI image editing. Presets work without an API call. Uploading a photo never automatically transmits it. The customer explicitly consents and starts generation. Preview is illustrative, not a size/fit guarantee or production asset.

**The user leaves this screen when:** They return to S13/S50/S51 within the same draft or follow the existing authorized save/order navigation. Exiting the workspace destroys personal try-on buffers; unsaved design warnings follow S13.

## 2. Mockup

![S51 Virtual Try On](img/S51-virtual_try_on_screen.png)

Illustrative synthetic sample, using S13's Dony storefront style. Fictional polo/artwork do not add a Published catalogue product. Written requirements govern behavior; no personal photo or actual customer information appears in the PNG.

## 3. Element inventory

| # | Element | Type | Content / data source | Required | Validation |
|---|---|---|---|---|---|
| 1 | Preset gallery | Three labelled cards | Synthetic male, female, child | Yes | Immediately show designed polo; clearly label deterministic mockup, not AI output. |
| 2 | Personal upload | File chooser | One PNG/JPEG/WebP photo | Optional | <=10 MiB, <=16M pixels, actual MIME/scan; recommend one person and visible torso. |
| 3 | Photo card / Remove | Thumbnail and button | Current photo, session-only label | After upload | Replacement/removal revokes consent and discards previous/pending result. |
| 4 | Provider disclosure / consent | Text + unchecked checkbox | Photo and polo sent to OpenAI, provider retention and API cost | Before generation | Explicit opt-in per photo; provider policies separate from application session-only storage. |
| 5 | Try on me | Primary button | Backend OpenAI image edit | Photo + valid design + consent + available engine | Disable duplicate generation; no automatic retry; API key never in browser. |
| 6 | Progress / Cancel | Overlay/status and action | Current job progress | Pending | Cancel discards application result; provider processing/billing may continue. |
| 7 | Original/result comparison | Toggle and image | Current session photo/generated result | Result available | Reject mismatched revision/photo/session; never save/download as manufacturing design. |
| 8 | Back to design / Mockups | Mode tabs | Shared draft | Yes | Design retained; leaving destroyed session clears personal buffers. |

## 4. States

| State | What the user sees | Trigger |
|---|---|---|
| Preset/empty | Synthetic model preview and upload prompt | No personal photo |
| Photo ready | Input photo; consent unchecked; generation disabled until consent | Valid upload |
| Generating | Progress and cancellation; no duplicate submit | Consent-gated explicit generation |
| Success | Generated preview and original toggle | Matching current job/revision/photo/session |
| Error | Safe provider/connection/timeout/quota message; photo/design retained | 400/422/429/502/503/504 |
| Unavailable | OpenAI not configured; presets and design remain usable | Backend reports unavailable |
| Stale/cancelled | Ignore result; show current draft/input | Design/photo/session changed or cancel |
| Forbidden/not found | Safe 401/403/404 | Ownership/authorization fails |
| Retry | Explicit generation after reviewing error and consent | Customer initiates again; no silent paid replay |

## 5. Interactions and navigation

| # | User action | System response | Goes to screen |
|---|---|---|---|
| 1 | Select preset | Show current polo on labelled synthetic person | S51 |
| 2 | Upload/replace photo | Validate in session, reset consent/result | S51 |
| 3 | Consent + Try on me | Backend sends two images to OpenAI; no client credential | S51 |
| 4 | Compare original/result | Toggle images without another API call | S51 |
| 5 | Remove/cancel/end session | Clear personal state, invalidate job | S51 / originating route |
| 6 | Design/Mockups | Return to shared draft | S13 / S50 |

## 6. Screen-level rules

| Rule ID | Rule | Source |
|---|---|---|
| SR-001 | Server enforces owner authorization and current product rules; private errors do not disclose other customer data. | MFG-05 |
| SR-002 | Preserve immutable saved designs; preview processing never changes an ordered snapshot or makes a draft orderable. | S13 / MFG-05 BR-001 |
| SR-003 | Personal photos/results remain session-only; template and explicitly saved artwork storage are separate. | MFG-05 BR-010–012 |

### Acceptance scenarios

1. Upload alone makes no provider request; unchecked consent blocks generation on client and server.
2. AI input order is person first and designed polo second; backend returns a result with the matching design revision.
3. Photo replacement or design edit invalidates a pending reply; a cancelled session cannot receive an old result.
4. Personal photo/result never enters save/order payloads, browser storage, application image files or logs.
5. Missing key, connection failure, invalid request, quota and timeout give actionable safe errors without raw provider data/secret leakage.
6. Original comparison and presets cost no API call; failed generation leaves S13 draft usable.

## 7. Linked requirements

| FR ID (from the module spec) | What this screen does for it |
|---|---|
| MFG-05/F-DES-016 | Implements the virtual try on flow and its validation/session rules. |
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
