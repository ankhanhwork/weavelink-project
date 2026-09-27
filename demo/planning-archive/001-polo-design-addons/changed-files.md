# Changed files

All entries below are new files on `ankhanh/polo-design-demo`. Approved `docs/spec/` and `data/` are unchanged.

| File | Reason |
|---|---|
| `specs/001-polo-design-addons/spec.md` | Record the authorized feature scope and acceptance criteria. |
| `specs/001-polo-design-addons/plan.md` | Select the isolated demo stack and implementation architecture. |
| `specs/001-polo-design-addons/research.md` | Record provider, model, privacy and performance decisions. |
| `specs/001-polo-design-addons/data-model.md` | Define transient draft, artwork and try-on entities. |
| `specs/001-polo-design-addons/contracts/api.md` | Define request, response and error contracts. |
| `specs/001-polo-design-addons/quickstart.md` | Provide startup and validation scenarios. |
| `specs/001-polo-design-addons/tasks.md` | Track implementation and measured verification results. |
| `specs/001-polo-design-addons/checklists/requirements.md` | Record specification quality review. |
| `specs/001-polo-design-addons/changed-files.md` | List every changed file and its purpose. |
| `demo/polo/.gitignore` | Exclude runtime, public weight caches and temporary QA files. |
| `demo/polo/requirements.txt` | Pin installed backend and background-removal dependencies. |
| `demo/polo/requirements-local.txt` | Define optional local AI dependencies. |
| `demo/polo/README.md` | Explain usage, setup, privacy, tests and limitations. |
| `demo/polo/server.py` | Serve the loopback demo and validated memory-only image APIs. |
| `demo/polo/ai.py` | Connect actual local and optional consent-gated hosted AI. |
| `demo/polo/setup_local_ai.py` | Download and verify public model weights with resumable transfers. |
| `demo/polo/web/index.html` | Provide design, gallery, background-review and try-on controls. |
| `demo/polo/web/style.css` | Style the responsive studio interface. |
| `demo/polo/web/app.js` | Manage artwork, processing, draft revisions and session cleanup. |
| `demo/polo/web/render.js` | Render current artwork into fixed polo views and presets. |
| `demo/polo/web/geometry.js` | Project physical artwork through calibrated garment planes and define chest placement. |
| `demo/polo/web/session-guard.js` | Reject personal AI replies belonging to obsolete inputs. |
| `demo/polo/web/assets/polo-views.png` | Supply synthetic photographic blank polo angles. |
| `demo/polo/web/assets/people.png` | Supply synthetic male, female and child preset imagery. |
| `demo/polo/tests/test_server.py` | Verify image boundaries, real solid removal and AI API failures. |
| `demo/polo/tests/session.test.mjs` | Verify asynchronous reply rejection across input/session changes. |
| `demo/polo/tests/geometry.test.mjs` | Verify six angle projections, inverse coordinates and chest bounds/aspect ratio. |
| `demo/polo/tests/fixtures/person.png` | Supply a fictional person for real inference validation. |

Local ignored `.specify/feature.json` selects this feature for Spec Kit. Ignored `.venv/` and `.models/` contain runtime/packages and public weights only. Generated QA outputs outside the repository use fictional inputs; no real customer photograph was saved.

## Current user revision

| Changed file | Reason |
|---|---|
| `demo/polo/web/index.html` | Add fabric choices and wearer-relative chest placement controls. |
| `demo/polo/web/style.css` | Style fabric and chest controls responsively. |
| `demo/polo/web/app.js` | Track fabric in the session draft and apply editable chest shortcuts. |
| `demo/polo/web/render.js` | Correct angled artwork with a calibrated projective mesh and expand front space to include chest. |
| `demo/polo/web/geometry.js` | Share forward/inverse geometry and preserve chest artwork proportions. |
| `demo/polo/tests/geometry.test.mjs` | Verify projection and chest placement numerically. |
| `demo/polo/README.md` | Explain new controls, 2D preview limits and future OpenAI direction. |
| `specs/001-polo-design-addons/spec.md` | Record fabric/chest acceptance and temporary local AI retention. |
| `specs/001-polo-design-addons/plan.md` | Document projective rendering and deferred backend OpenAI integration. |
| `specs/001-polo-design-addons/research.md` | Record provider direction and fabric/angle decisions. |
| `specs/001-polo-design-addons/data-model.md` | Add transient fabric and calibrated print-plane fields. |
| `specs/001-polo-design-addons/tasks.md` | Record revision tasks and actual verification limits. |
| `specs/001-polo-design-addons/changed-files.md` | Enumerate this revision's files and reasons. |

## Centred proof review

| Changed file | Reason |
|---|---|
| `demo/polo/web/render.js` | Remove rejected extra upper tilt and centre offsets. |
| `demo/polo/web/geometry.js` | Remove the rejected registration wrapper and restore direct surface projection. |
| `demo/polo/tests/geometry.test.mjs` | Verify the restored centre-column baseline and mesh validity. |
| `specs/001-polo-design-addons/spec.md` | Record rejection and centred-proof approval requirement. |
| `specs/001-polo-design-addons/plan.md` | Mark rejected calibration and describe identical proof inputs. |
| `specs/001-polo-design-addons/tasks.md` | Track proof preparation and pending visual approval. |
| `specs/001-polo-design-addons/changed-files.md` | List this rollback/review revision's files and reasons. |

## Collar-axis lateral adjustment

| Changed file | Reason |
|---|---|
| `demo/polo/web/render.js` | Move left/right interior X landmarks slightly toward the user-requested collar/body axis while retaining Y and slopes. |
| `specs/001-polo-design-addons/spec.md` | Record feedback from the centred proofs and preserve the agreed geometry scope. |
| `specs/001-polo-design-addons/plan.md` | Document the small row-dependent shifts with collar and boundaries fixed. |
| `specs/001-polo-design-addons/tasks.md` | Record tests and comparable proof images pending review. |
| `specs/001-polo-design-addons/changed-files.md` | List the exact changed files and their reasons. |

## Surface-aware correction

| Changed file | Reason |
|---|---|
| `demo/polo/web/render.js` | Calibrate independent torso grids; shade prints from fabric and exclude the placket. |
| `demo/polo/web/geometry.js` | Interpolate physical artwork coordinates through body landmarks. |
| `demo/polo/tests/geometry.test.mjs` | Check landmarks, chest order and non-folding surface cells. |
| `demo/polo/README.md` | Describe the renderer and actual template-quality limits. |
| `specs/001-polo-design-addons/spec.md` | Record user-authorized surface-aware mockup acceptance. |
| `specs/001-polo-design-addons/plan.md` | Replace flat-plane rendering with the implemented landmark/shading architecture. |
| `specs/001-polo-design-addons/research.md` | Explain reuse of templates and future production asset requirements. |
| `specs/001-polo-design-addons/data-model.md` | Define public surface/occlusion metadata and transient render pixels. |
| `specs/001-polo-design-addons/tasks.md` | Record 16 passing tests and completed browser/mobile/reset checks. |
| `specs/001-polo-design-addons/changed-files.md` | List this correction's exact files and purposes. |

## Logo attachment and position correction

| Changed file | Reason |
|---|---|
| `demo/polo/web/render.js` | Correct vertical angle registration and transfer fabric lighting/texture with bounded fold displacement. |
| `demo/polo/web/print-surface.js` | Render each warped ink pixel once and preserve colour at transparent edges. |
| `demo/polo/tests/print-surface.test.mjs` | Verify seam opacity, transparent edges, clipping and ink lighting. |
| `demo/polo/tests/geometry.test.mjs` | Add the user's lower-torso placement as a cross-view vertical regression. |
| `demo/polo/README.md` | Document the current renderer, tests and approximate geometry limits. |
| `specs/001-polo-design-addons/spec.md` | Record the user's corrected scope: logo attachment and placement, retaining photos. |
| `specs/001-polo-design-addons/plan.md` | Describe single-assignment rasterization and fabric sampling. |
| `specs/001-polo-design-addons/tasks.md` | Record actual regression and visual verification results. |
| `specs/001-polo-design-addons/changed-files.md` | List this follow-up's exact file changes. |

## Upper-chest and centre correction (two angles only)

| Changed file | Reason |
|---|---|
| `demo/polo/web/geometry.js` | Blend the upper-chest slope and bounded centre correction into the existing garment mapping. |
| `demo/polo/web/render.js` | Apply opposite slope/centre parameters only on left and right angled photos. |
| `demo/polo/tests/geometry.test.mjs` | Verify upper slope reversal, preserved lower heights, unchanged other views and safe mesh cells. |
| `specs/001-polo-design-addons/spec.md` | Record the user's region-specific and two-view-only requirements. |
| `specs/001-polo-design-addons/plan.md` | Describe blending thresholds and small horizontal corrections. |
| `specs/001-polo-design-addons/tasks.md` | Record numerical and visual checks. |
| `specs/001-polo-design-addons/changed-files.md` | Enumerate this revision's files and reasons. |

## Additional small angle alignment

| Changed file | Reason |
|---|---|
| `demo/polo/web/render.js` | Move interior surface columns a further 0.004 left/right in the respective angled views; preserve height, tilt and upper anchor. |
| `specs/001-polo-design-addons/changed-files.md` | Record the user's additional small alignment adjustment and its verification. |

Validation: all 22 geometry, print raster and session tests pass. Compare the two updated collar-axis proof screenshots before approval.

## Second small angle alignment

- demo/polo/web/render.js: shift interior angle columns another 0.004 outward in the same user-requested directions, retaining vertical coordinates and collar anchors.
- specs/001-polo-design-addons/changed-files.md: record this additional adjustment.

Validation: 22 regression tests pass; fresh left/right proof screenshots supplied for review.

## Additional four-pixel angle alignment

- demo/polo/web/render.js: shift interior angle columns another 4/512 normalized units left/right respectively, preserving vertical coordinates and collar anchors.
- specs/001-polo-design-addons/changed-files.md: record the requested four-pixel adjustment.

Validation: all 22 regression tests pass; updated paired proof images supplied for visual review.

## Second four-pixel angle alignment

- demo/polo/web/render.js: shift interior angled-view columns a further 4/512 left/right respectively, keeping height and collar anchors.
- specs/001-polo-design-addons/changed-files.md: record this follow-up adjustment and paired visual proofs.

## Approved left angle; final right adjustment

- demo/polo/web/render.js: preserve the user-approved left angle and move only the right-angle interior columns another 2/512 to the right.
- specs/001-polo-design-addons/changed-files.md: record left-angle approval and the right-only adjustment.

Validation: all 22 regression tests pass; a fresh right-angle proof is supplied for review.


## OpenAI-only part 03

| File | Reason |
|---|---|
| demo/polo/ai.py | Replace local/FASHN adapters with OpenAI image edits and sanitized errors. |
| demo/polo/server.py | Remove unused local try-on model environment configuration. |
| demo/polo/web/app.js | Require OpenAI availability and transmission consent. |
| demo/polo/web/index.html | Name OpenAI and disclose API charging in consent. |
| demo/polo/.env (ignored) | Empty server credential slot; never commit or inspect after user fills it. |
| demo/polo/.env.example | Shareable empty configuration template. |
| demo/polo/AGENTS.md | Instruct agents not to inspect secret files or log credentials. |
| demo/polo/setup_local_ai.py (removed) | Remove local try-on installer. |
| demo/polo/requirements-local.txt (removed) | Remove local try-on dependency manifest. |
| demo/polo/tests/test_server.py | Replace local-provider tests with mocked OpenAI/security contracts. |
| demo/polo/README.md | Document setup, secret boundaries and provider retention. |
| specs/001-polo-design-addons/spec.md, plan.md, tasks.md | Supersede temporary local-provider plans with this migration. |
| specs/001-polo-design-addons/changed-files.md | Record exact migration scope. |


## Credential path relocation

- demo/polo/ai.py: resolve docs/env/.env from the repository root, independent of current directory.
- demo/polo/README.md: update the credential setup path.
- specs/001-polo-design-addons/spec.md, plan.md, tasks.md: update the credential location.
- specs/001-polo-design-addons/changed-files.md: record this relocation.

The secret file was not opened or modified by the agent.
