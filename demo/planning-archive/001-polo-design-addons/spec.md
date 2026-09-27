# Feature Specification: Polo Design Add-ons

**Feature Branch**: `ankhanh/polo-design-demo`

**Created**: 2026-09-26

**Status**: Authorized standalone demo extension; not a replacement baseline

**Input**: Remove artwork backgrounds; preview a polo from several fixed angles like reference image 2; show male, female and child presets wearing the current design; accept a real uploaded person photo for AI garment replacement. User confirmed fixed-angle gallery, polo first, real AI upload, session-only images, and autonomous implementation.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Preview the designed polo (Priority: P1)

A customer uploads artwork, places it on the front or back of a polo, changes its colour and views a gallery with a large selected image.

**Why this priority**: Check artwork scale and placement before making production decisions.

**Independent Test**: Place different artwork on each side and visit all six gallery views.

**Acceptance Scenarios**:

1. **Given** a front design, **When** the customer opens Mockups, **Then** six selectable views show the same polo configuration, with the selected view enlarged.
2. **Given** different front/back artwork, **When** front/back views are selected, **Then** each shows only its own surface's artwork.
3. **Given** a colour or placement change, **When** preview is opened, **Then** all views reflect the latest draft without changing physical coordinates.
4. **Given** a placement outside its print area, **When** editing, **Then** the customer receives a correction and the placement stays within bounds.

### User Story 2 - Remove artwork background (Priority: P2)

A customer selects an uploaded image, removes its background, reviews transparency, then applies or discards the result.

**Why this priority**: Avoid unintended background rectangles on printed garments.

**Independent Test**: Upload a subject on a solid background, remove its background and restore the original.

**Acceptance Scenarios**:

1. **Given** a selected image, **When** background removal finishes, **Then** a review displays the original and transparent result before applying.
2. **Given** a reviewed result, **When** Apply is chosen, **Then** only that asset changes and its position/size are preserved.
3. **Given** a discarded result or failed operation, **When** returning to editing, **Then** the original draft is intact.
4. **Given** an applied result, **When** Restore original is selected, **Then** the original uploaded image is restored.

### User Story 3 - Try the design on people (Priority: P3)

A customer sees male/female/child sample mockups wearing their current design, or uploads their own photo and asks AI to replace the upper garment with the designed polo.

**Why this priority**: Help imagine the design in use without promising fit or size accuracy.

**Independent Test**: Inspect all presets, upload a supported photo, generate using a configured AI engine, then end the session and verify images are gone.

**Acceptance Scenarios**:

1. **Given** the current design, **When** Try on you opens, **Then** male, female and child synthetic presets are immediately available and their artwork follows the current front design.
2. **Given** a valid real photo and an available AI engine, **When** Try on is chosen, **Then** the real photo and fully rendered polo are processed and an AI result is displayed.
3. **Given** an unavailable engine, **When** generation is attempted, **Then** a clear service-unavailable message appears; no mockup is misrepresented as AI output.
4. **Given** a pending generation, **When** the design or person changes, **Then** an obsolete response cannot replace a newer result.
5. **Given** an uploaded photo/result, **When** the tab is reloaded or End session is chosen, **Then** the application no longer retains it.

### Edge Cases

- Invalid MIME, corrupted images, images over 10 MiB, more than five artwork files and excessive dimensions are rejected without losing existing edits.
- Front/back draft changes are independent. Empty back artwork produces a blank back mockup.
- Artwork too similar to its background can lose detail; retain original and require review.
- AI failure, timeout or busy status preserves the draft and permits an explicit retry.
- End session invalidates pending callbacks and clears all uploaded data and generated results.
- Hands obscuring the torso, multiple people and cropped photos may reduce AI quality; guidance recommends one clearly visible person.
- Preset child imagery is synthetic. No claim is made that all AI engines support child photo input.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The demo MUST offer one polo garment, independent front/back surfaces, colour and fabric selection and a configurable artwork print area including the chest.
- **FR-002**: It MUST accept at most five PNG/JPEG/WebP artwork assets, each no larger than 10 MiB, and allow bounded non-negative X/Y and positive width/height placement.
- **FR-003**: Mockups MUST provide six fixed-angle thumbnails and an enlarged selected image. A free-rotation 3D viewer is excluded.
- **FR-004**: All mockups and presets MUST use the same current draft configuration, including correct front/back attribution. Angled views MUST project the same physical placement along the garment front plane; changing view MUST NOT independently relocate the logo.
- **FR-005**: Background removal MUST operate on the selected artwork, preserve the original, support review/apply/cancel/restore and preserve placement.
- **FR-006**: Try on you MUST provide male, female and child synthetic sample mockups. Their labels MUST distinguish template previews from generated personal AI results.
- **FR-007**: Try on you MUST accept real uploaded person photos and use the complete rendered polo as the target upper garment for actual AI generation.
- **FR-008**: Generation MUST have pending, success, unavailable, busy and failure states; obsolete results MUST not be installed after input changes.
- **FR-009**: Uploaded artwork/person images and results MUST live only in application memory for the active tab/request. They MUST NOT be written to files, databases, persistent browser storage or request logs.
- **FR-010**: End session/reload MUST clear user images. Personal results MUST be marked illustrative and MUST NOT determine size, fit or production artwork.
- **FR-011**: The current local AI MUST remain temporarily available. The planned production engine MUST use OpenAI API instead of requiring local AI. OpenAI integration is deferred in this revision; credentials remain backend-only, and provider retention/consent MUST be reviewed separately from session-only application storage before activation.
- **FR-012**: The UI MUST work at desktop and narrow mobile widths, offer labelled keyboard controls and announce processing/error states.

- **FR-013**: The demo MUST offer 100% cotton and 65/35 cotton-polyester fabric selections, following the approved fictional material options in MFG-04. These are demo choices for the polo, not additions to Dony catalogue data. Fabric selection MUST remain in the transient draft and invalidate personal AI results. Current photos illustrate one piqué construction; no fabric-specific physical simulation is claimed.
- **FR-014**: Front artwork MUST support wearer-left chest, wearer-right chest and centre placement shortcuts, followed by free numeric/drag adjustment. Chest shortcuts default to 70 mm width with bounded aspect-aware height; front print mapping MUST include chest space.

### Key Entities

- **Draft**: session-only polo colour, current surface, revision and artwork placements; not an orderable saved version.
- **Artwork**: original image, active image, optional reviewed cutout and dimensions.
- **Mockup View**: template, surface, angle and print mapping.
- **Person Input**: synthetic preset or private uploaded photo.
- **Try-on Result**: generated image tied to exact person and design revision; discarded when outdated.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: All six mockup views can be selected and reflect the latest colour and correct surface artwork.
- **SC-002**: Removing a solid background yields transparent background pixels; apply/cancel/restore preserves placement in every validation scenario.
- **SC-003**: All three sample categories are visible before a personal photo is uploaded.
- **SC-004**: A configured AI engine processes at least one uploaded photo into an actual generated try-on image; lack of runtime readiness is reported separately from code verification.
- **SC-005**: Reload/end-session leaves no uploaded image/result recoverable in application storage; stale response tests pass.
- **SC-006**: The workflow remains usable at 390px and desktop widths with no page-level horizontal overflow.

## Assumptions

- User authorization on 2026-09-26 supplies the new requirements; this feature does not silently amend `docs/spec/` or `data/`.
- Baseline MFG-05/S13 continues to own production validation, immutable saves, ownership and order eligibility. The standalone demo has no login, saved designs, fees or checkout and is explicitly labelled a demo.
- Reference screenshots define gallery interaction, not their T-shirt product, price, sleeve editing or cart controls.
- Demo polo dimensions/colour palette are illustrative local configuration, not new approved Dony product rules or modifications to seed data.
- Six views means front flat, front worn shape, left three-quarter, right three-quarter, back flat and back worn shape.
- Presets use photorealistic synthetic source images with deterministic artwork compositing, not precomputed personal AI results.
- AI engine/model availability, downloadable weights and hardware are deployment dependencies. A missing engine is not satisfied by a fake result.

## Revision: fabric, chest logos and API direction

User requested this revision on 2026-09-26. Verify a chest logo and a central logo across front/volume/left/right views against collar/placket/body landmarks; preserve millimetres and front/back isolation. Select each fabric, then End session: selection returns to the default and all user assets disappear. Baseline and data stay read-only.

### Revision: surface-aware deterministic mockups

On 2026-09-26 the user authorized continued correction after the four-point projection remained visibly inadequate. Angled views must use independent body landmarks rather than a subdivided flat homography, transfer blank-garment shading without changing artwork alpha, and exclude the placket from print compositing. Wearer-relative chest sides and original physical placement remain stable across view selection. Mockups do not invoke generative AI. Existing synthetic photos remain illustrative; a production template kit and exact fold simulation are not claimed by this change.

User subsequently clarified that the issues are logo attachment and position, not a request to replace the blank garment. Keep existing images. Validate the actual 119/214/70/70 mm lower-torso placement across front/angles, preserve transparency at mesh boundaries without repeated alpha compositing, transfer local fabric texture and apply bounded fold displacement. Treat numerical checks as regression protection, not evidence that the user accepts visual quality.

Latest user correction applies only to the two angled photos: reverse the upper-chest print slope to follow upward folds, smoothly blend into the accepted lower-torso mapping, and adjust centred prints slightly left on the left angle / right on the right angle. Preserve lower-torso height and fold direction, editor coordinates and all four other garment views.

The user rejected the resulting upper tilt/offset implementation and requested centred left/right proofs for approval. Restore the preceding renderer and remove those extra corrections. Use identical artwork, colour, dimensions and physical centre on both proof images; wait for the user's visual review before introducing another calibration. Previous regression test counts do not constitute visual approval.

After reviewing the centred proofs, the user requested a small leftward move on the left angle and rightward move on the right angle, aligned to the curved axis descending from the collar/placket. Calibrate only the interior X landmarks of those two views. Keep Y landmarks, fold direction, physical artwork inputs and all other views unchanged. Regenerate comparable proofs for review.

OpenAI is the selected future engine. The official image-generation guide supports image edits and multiple reference images: https://developers.openai.com/api/docs/guides/image-generation . Planned inputs are the person photograph, rendered polo, artwork placement and chosen fabric; preserve face/pose/background and replace only the garment. This is an image-editing approach to evaluate, not a guarantee of exact garment/logo fidelity. Model selection, API integration, cost/latency validation and provider retention review belong to the later migration. Current local model/code/weights are retained at the user's request.


## OpenAI-only try-on migration (2026-09-27)

Supersedes earlier local/FASHN try-on notes: part 03 now uses OpenAI image edits, with the person and designed polo as inputs. No local try-on fallback or installation flow remains. Part 01 background removal is independent and retained. Credentials live in ignored docs/env/.env (or backend process environment), never frontend, status, logs or version control. Agents must not read secret files. Git ignore and agent instructions do not prevent filesystem access by authorized machine users/agents. App images remain session-only; OpenAI retention policies apply after explicit consent. Paid real-image validation awaits the user entering a key locally.
