# Implementation Plan: Polo Design Add-ons

**Branch**: `ankhanh/polo-design-demo` | **Date**: 2026-09-26 | **Spec**: [spec.md](spec.md)

## Summary

Build a self-contained local web demo in `demo/polo/`: browser-native JavaScript/canvas frontend and Python image/AI backend. Six fixed photographic polo mockups, synthetic model previews, local background removal and real uploaded-photo AI inference. No fake AI success fallback.

## Technical Context

**Language/Version**: Python 3.12+, browser ES modules, HTML/CSS.
**Primary Dependencies**: FastAPI, Uvicorn, Pillow, rembg/CPU ONNX; optional FASHN VTON 1.5/PyTorch.
**Storage**: Browser/request RAM only for uploads/results; ignored caches hold model weights only.
**Testing**: Python unittest/TestClient for image validation, privacy and injected AI contracts; browser desktop/mobile QA.
**Target Platform**: Windows local server and modern Chromium, 390px through desktop.
**Project Type**: Standalone demo, no authenticated production workflows.
**Performance Goals**: Immediate canvas redraw; bounded processing states. Measure local CPU inference separately.
**Constraints**: Five artwork assets, 10 MiB each, decoded pixel limit, bounded body size, serial AI inference, no image file writes/logging, stale result protection.
**Scale/Scope**: One illustrative polo, front/back canvas, six mockups, three synthetic presets, one personal result.

## Constitution Check

Pre-research: constitution is an unratified placeholder; follow AGENTS.md. Updated main with pull --ff-only and created member-prefixed branch. User explicitly authorizes this extension and autonomous implementation. Baseline/data remain unchanged. This Plan selects the stack before app code or dependencies are added.

Post-design: PASS. Demo-only settings do not replace Dony product rules. No secrets, real-person repository assets, existing file deletion or push. Requirements checklist passed; no extension hooks registered.

## Project Structure

```text
specs/001-polo-design-addons/
  spec.md, plan.md, research.md, data-model.md, quickstart.md, tasks.md
  checklists/requirements.md, contracts/api.md
 demo/polo/
  server.py, ai.py, requirements.txt, requirements-local.txt
  setup_local_ai.py, README.md, .gitignore, tests/test_server.py
  web/index.html, app.js, render.js, style.css
  web/assets/polo-views.png, people.png
```

**Structure Decision**: Self-contained prototype; browser modules served directly by Python. No database, auth, save versions or ordering. Local AI remains the temporary demo engine. The user selected OpenAI API for the future engine; migration is deferred and will separately validate provider retention/consent.

## Execution

Validate image boundary -> editor and gallery -> background review -> presets and real AI adapters -> tests and visual QA. Attempt model setup and actual generation; report unavailable hardware/downloads separately from code verification.

## Revision implementation

Angled views use a separately calibrated 5 x 5 landmark grid per photographic template. Physical print coordinates interpolate through that grid and render through a 12 x 16 triangle mesh. Centre landmarks follow the placket and body; edge columns follow torso edges. Artwork receives luminance from the original blank garment, with alpha preserved. A placket occlusion polygon removes artwork over buttons. Flat editor retains affine coordinates and inverse projection for dragging. Chest shortcuts and the print domain include upper chest. Material choices remain transient. Existing AI adapters and weights are unchanged; future OpenAI integration remains backend-only.

Templates are reused rather than regenerated: their existing torso contours are suitable for manual landmark calibration. This does not turn independent synthetic photos into a physically consistent 3D garment. Production quality requires a matched photographed/rendered template kit, separate garment masks and more detailed displacement data; that asset work is not claimed complete in this demo.

## Print attachment and placement correction

Normalize angle print-bottom landmarks to the editor's chest-to-hem print interval, instead of stretching the interval to the photo's hem. Use `print-surface.js` to assign destination pixels via barycentric inverse triangle mapping and premultiplied-alpha bilinear sampling. Do not overlap/composite triangle clips. A cached public blank-photo luminance field supplies bounded +/-0.003 image-coordinate fold displacement and ink lighting with local texture. Only public template fields are cached; personalized rasters remain temporary. The latest user clarification explicitly retains the blank templates. No image-generation call was made.

## Rejected upper-chest and centre registration

Only views 2/3 supply `registration`. `garmentPoint` adds opposite upper-chest slopes (-0.055 / +0.065 normalized Y per unit U), fully active through physical Y48 mm and smoothly fading to zero by Y120 mm. Lower Y geometry remains exactly the previous mapping. A bounded lateral correction of -0.012 / +0.012 at the centre fades to zero at the print-area edges, so centre prints move about six pixels at the 512 px source scale without moving the torso boundaries. Other views, editor and presets have no registration and retain their previous geometry.

The user rejected this correction as visually worse. It is removed from active code: no `registration` offsets or extra upper tilt remain. The prior landmark/raster renderer is restored. Prepare one physically centred artwork (X80/Y100/W140/H140 mm; centre X150 mm) on the same garment colour and export both angles for user review before any further calibration. This is a review baseline, not approved final geometry.

### Collar-axis proof adjustment

User feedback on that baseline authorizes small opposing X changes. The collar/top row remains fixed. Interior columns move by 0.008 at the next row, 0.012 through the mid/lower torso, and 0.010 at the print bottom: negative on the left-angle photo and positive on the right-angle photo. At 512 px, the maximum shift is about six pixels. Move interior columns together to retain central-logo width; leave torso boundary columns, every Y landmark and lighting unchanged. This adjusts the curve descending from collar/placket without reintroducing the rejected upper-chest tilt.


## OpenAI-only try-on migration (2026-09-27)

Supersedes earlier local/FASHN try-on notes: part 03 now uses OpenAI image edits, with the person and designed polo as inputs. No local try-on fallback or installation flow remains. Part 01 background removal is independent and retained. Credentials live in ignored docs/env/.env (or backend process environment), never frontend, status, logs or version control. Agents must not read secret files. Git ignore and agent instructions do not prevent filesystem access by authorized machine users/agents. App images remain session-only; OpenAI retention policies apply after explicit consent. Paid real-image validation awaits the user entering a key locally.
