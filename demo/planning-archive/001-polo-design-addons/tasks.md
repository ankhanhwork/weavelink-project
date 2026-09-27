# Tasks: Polo Design Add-ons

**Input**: spec.md, plan.md, research.md, data-model.md and contracts/api.md.

## Phase 1: Setup

- [x] T001 Select isolated demo stack and add dependency/ignore configuration in demo/polo/requirements.txt and demo/polo/.gitignore.
- [x] T002 Install isolated runtime and document startup in demo/polo/README.md.

## Phase 2: Foundation

- [x] T003 Implement validated image boundary, memory-only routes, no-store and origin protection in demo/polo/server.py.
- [x] T004 Implement session-only draft and accessible responsive shell in demo/polo/web/index.html and demo/polo/web/style.css.

## Phase 3: US1 - Polo mockups

Independent test: change colour/front/back artwork and inspect six views.

- [x] T005 [P] [US1] Generate synthetic photographic polo view sheet in demo/polo/web/assets/polo-views.png.
- [x] T006 [US1] Implement polo render/mapping and six views in demo/polo/web/render.js.
- [x] T007 [US1] Implement upload/select/bounded placement/front-back and gallery in demo/polo/web/app.js.

## Phase 4: US2 - Background removal

Independent test: remove/apply/cancel/restore without moving artwork.

- [x] T008 [US2] Implement subject and border-connected solid removal in demo/polo/server.py.
- [x] T009 [US2] Implement cutout review and original restore in demo/polo/web/app.js.

## Phase 5: US3 - Try on you

Independent test: presets update; actual photo generation with ready engine; unavailable state remains honest.

- [x] T010 [P] [US3] Generate synthetic male/female/child sheet in demo/polo/web/assets/people.png.
- [x] T011 [US3] Implement current-design preset compositing in demo/polo/web/render.js.
- [x] T012 [US3] Implement local and consent-gated hosted real AI adapters in demo/polo/ai.py.
- [x] T013 [US3] Implement uploaded-photo flow, stale-result protection and session cleanup in demo/polo/web/app.js.
- [x] T014 [US3] Add local model installer and dependency instructions in demo/polo/setup_local_ai.py and demo/polo/requirements-local.txt.
- [x] T015 [US3] Run and verify actual local generated try-on via demo/polo/server.py; report hardware/download blockers separately.

## Phase 6: Validation

- [x] T016 Verify image limits/privacy/provider failure contracts in demo/polo/tests/test_server.py.
- [x] T017 Verify desktop/mobile workflows and asynchronous reply rejection in demo/polo/tests/session.test.mjs; record results in specs/001-polo-design-addons/tasks.md.
- [x] T018 Complete startup/privacy/limitation documentation in demo/polo/README.md.

## Dependencies and execution

Setup -> Foundation -> US1 -> US2 -> US3 -> Validation. Asset-generation tasks T005/T010 can run independently; adapter and rendering research may run concurrently under the Spec Kit research requirement. Each story is independently inspectable after foundation. Implement incrementally; never treat mocked AI contracts as real generation.

## Validation report

- Requirements checklist: 15 checked, 0 unchecked, PASS; no extension hooks registered.
- Installed isolated Python 3.12 runtime, pinned dependencies, official pinned local AI package and public weights. CPU-only hardware; no paid hosted request.
- Backend contracts: 21 tests; covers actual image decoding/limits, real solid-background alpha, interior colour preservation, unchanged original, privacy headers/origin, busy/unavailable/provider errors and CPU profile selection.
- Frontend reply gate: 7 Node tests; late replies rejected after design/person/session/job changes or incorrect/missing server revision.
- Browser verification: all six gallery selectors; distinct back upload stays separate; blank back uses no front artwork; full-area placement checked in both angled views after edge-margin correction; three presets; actual file chooser photo upload and source display; missing-engine message; background subject/solid review, apply/cancel/restore; X/Y/size preserved; placement clamped; End session leaves 0 assets. Reload removes uploaded photo.
- Real subject-removal request completed HTTP 200 in 6.1 seconds, output alpha range 0..255, using fictional imagery.
- Responsive checks: 390 x 844 (content width 375, no horizontal overflow), desktop 1440 x 1000. Keyboard-operated tabs/buttons and background dialog verified.
- JavaScript syntax checks passed; no existing baseline or seed files modified. Source review found no persistent browser storage, customer image writes, body logging or embedded credentials.
- Real AI experimental reduced-resolution run: HTTP 200, 299.3 seconds, actual generated image. Visual inspection FAILED acceptable polo appearance: collar lost, lower torso not fully replaced. The preview profile is opt-in, never presented as quality acceptance.
- Real AI native 864 x 576 / 20-step run: HTTP 200 in 2443.8 seconds (40 minutes 44 seconds), using the fictional fixture and rendered Forest polo. Visual inspection PASS for demo: polo collar/buttons, full green upper garment and flower artwork present; original pose/background broadly preserved. Small lettering remains blurred/altered. One fictional input establishes this demonstration, not quality across all people/poses. Native is the default; GPU is recommended for interactive speed. All 18 tasks complete.
- QA screenshots/results use fictional input and live outside the repository. Actual customer photos remain session/request-only. Image/model outputs are illustrative; exact print geometry comes from the original artwork/draft.

### Acceptance coverage

| Criterion | Evidence |
|---|---|
| SC-001 | Six selectable current-draft views; separate back artwork and angle-edge checks. |
| SC-002 | Actual alpha processing and browser apply/cancel/restore preserve 95/35/110/110 placement. |
| SC-003 | Male/female/child synthetic presets visible and selectable. |
| SC-004 | Actual native local AI result inspected; request used revision 1 / local engine. |
| SC-005 | End session, reload, memory-only source review and seven reply-gate tests. Request RAM lasts until any running inference completes, as documented. |
| SC-006 | Desktop and 390px browser checks; no horizontal overflow. |

## User revision tasks

- [x] T019 Record future OpenAI migration and temporary local AI retention in spec.md, plan.md and research.md.
- [x] T020 Replace independent angle placement with calibrated projective mapping in demo/polo/web/render.js and geometry.js.
- [x] T021 Add fabric selection, chest-inclusive print space and editable chest shortcuts in demo/polo/web/index.html, app.js and style.css.
- [x] T022 Verify geometry/drag round trips, chest-side placement, fabric reset and desktop/mobile UI; record this revision's validation.

Revision validation: 14 Node tests pass (seven geometry/chest tests and seven existing session reply tests). Browser inspection confirmed the fabric selection and wearer-left chest control, and inspected the updated left-angle mesh without diagonal clipping seams. Final right-angle visual inspection and the new controls' mobile/reset checks remain pending: browser control was interrupted by new input, then the browser URL policy rejected reconnection. The implementation resets fabric to cotton in the existing end-session handler; this revision does not claim an observed reset or fresh mobile screenshot. Chest artwork fits a maximum 70 mm width / 90 mm height while retaining its aspect ratio. Current local AI was not modified or rerun.

## Surface-aware correction validation (supersedes pending browser checks above)

- [x] T023 Replace flat angle projection with independently calibrated body landmarks and boundary clipping.
- [x] T024 Transfer blank-garment shading, preserve alpha and mask the button placket.
- [x] T025 Validate both chest sides on both angles, central artwork, mobile overflow and session reset.

16 Node tests pass: nine geometry tests (including exact landmark interpolation and positive triangle orientation across all surface cells) and seven reply-guard tests. JavaScript syntax check passes. Browser inspected wearer-left and wearer-right chest logos on both angles; central artwork was checked with opaque background on the left and transparent background on the right. No console errors observed. At 390 px, document width is 375 px (no horizontal overflow). Changing fabric to blend then ending the QA session visibly restores cotton and zero assets. Screenshots outside the repository: `polo-surface-chest-left.jpg` and `polo-surface-centre-right.jpg`. Images used are synthetic demo artwork. Existing real-person tab was not reloaded. Local AI was unchanged and not invoked. Exact fold displacement and production template consistency remain asset-quality limits, not passing test claims.
# Logo attachment and position follow-up

- [x] T026 Reproduce the user's current synthetic logo at X119/Y214/W70/H70 without reloading their draft.
- [x] T027 Correct the angled print interval; remove repeated triangle compositing and premultiply alpha while sampling.
- [x] T028 Transfer local fabric light/texture, add bounded angle fold displacement, and inspect the actual placement across front/left/right.

Validation: 20 Node tests pass, including a vertical-drift regression for the user's lower-torso placement, no alpha gaps/doubling across the shared mesh edge, no dark transparent fringe, print-boundary transparency and ink-light response. Browser inspected the reproduced 119/214/70/70 placement at front and both angles, and wearer-left chest at both angles. Console has no observed errors. QA screenshots outside the repo: `polo-print-position-left.jpg`, `polo-print-position-right.jpg`, `polo-print-chest-left.jpg`. These checks use the existing synthetic sample and demonstrate the current implementation, not user acceptance or exact fold physics. Original user tab remains loaded with its draft; open the freshly kept QA tab to see the new renderer. Existing photos, AI adapters and storage behavior are unchanged. No ImageGen call was made after the user corrected the scope.
# Upper-chest angle correction

- [x] T029 Add a smoothly blended upper-chest slope and small opposite centre shifts exclusively to angled views.
- [x] T030 Verify slope direction, lower-height preservation, other-view invariance and positive mesh orientation.

22 Node tests pass. New tests verify opposite upper slope directions on left/right images, identical lower Y geometry from Y120 mm onward, unchanged other four views, prescribed centre shifts and positive orientation for every final mesh cell. Browser inspected upper-chest artwork on both angles with its opaque square background deliberately retained to make edge orientation visible. Central print comparison is also inspected in the fresh QA tab. No blank image, AI or user-draft storage changes. This records implementation checks, not a claim of exact manufacturing geometry.
# Centred proof review after rejection

- [x] T031 Remove rejected upper-chest tilt and lateral offset; restore prior landmark mapping.
- [x] T032 Render identical centred artwork on left/right angles for review (X80/Y100/W140/H140 mm, ivory, synthetic cutout).
- [ ] T033 Obtain user visual approval before further angle calibration.

22 regression tests pass after replacing the rejected-slope test with a centre-column baseline check. Both proof views are prepared from the running app; no customer image/draft is persisted or reloaded. Review images are synthetic screenshots outside the repository. Their purpose is comparison and approval, not a claim that the position is accepted.
# Collar-axis proof adjustment

- [x] T034 Apply the user's small opposing lateral moves along the collar-to-body curve; retain all Y values and slope logic.
- [x] T035 Export comparable ivory/centred/cutout angle proofs with the same 80/100/140/140 mm input.

22 existing geometry/raster/session tests pass after calibration. The top anchor and outer columns are untouched; interior columns move together, up to six source pixels. Review screenshots outside the repository: `approval-collar-axis-left.jpg`, `approval-collar-axis-right.jpg`. Visual acceptance remains pending; no assertion of final approval is made.


## OpenAI-only try-on migration (2026-09-27)

Supersedes earlier local/FASHN try-on notes: part 03 now uses OpenAI image edits, with the person and designed polo as inputs. No local try-on fallback or installation flow remains. Part 01 background removal is independent and retained. Credentials live in ignored docs/env/.env (or backend process environment), never frontend, status, logs or version control. Agents must not read secret files. Git ignore and agent instructions do not prevent filesystem access by authorized machine users/agents. App images remain session-only; OpenAI retention policies apply after explicit consent. Paid real-image validation awaits the user entering a key locally.
