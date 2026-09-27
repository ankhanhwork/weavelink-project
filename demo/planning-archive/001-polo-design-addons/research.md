# Research: Polo Design Add-ons

## Runtime

- **Decision**: FastAPI/Pillow backend with browser-native modules/canvas. Isolated ignored Python environment.
- **Rationale**: Direct image processing and optional local PyTorch without a second server/build framework.
- **Alternatives considered**: React/Next.js adds overhead; hosted-only AI cannot promise provider session-only retention.

## Mockups and presets

- **Decision**: Synthetic photographic blank polo and male/female/child contact sheets; authored perspective mappings and canvas compositing for current artwork.
- **Rationale**: Fixed-angle gallery matches the user reference and remains a 2D workflow. Assets contain no real personal data.
- **Alternatives considered**: Free-rotation 3D excluded by user; generating every preview through AI could alter artwork.

## Background removal

- **Decision**: Local rembg u2netp subject extraction and edge-connected solid-background removal. PNG alpha output, review before apply, retain original.
- **Rationale**: No remote image processing; edge-connected removal preserves disconnected interior colours.
- **Alternatives considered**: remove.bg requires credentials and announces migration on 2026-12-01: https://www.remove.bg/api .
- **Primary documentation**: https://github.com/danielgatis/rembg

## Real AI try-on

- **Decision**: Local FASHN VTON 1.5 as privacy-preserving engine; memory-only Pillow input/output and separate weight installer. Explicit unavailable state without weights.
- **Rationale**: No paid credential; all photo processing can stay local.
- **Alternatives considered**: Google hosted VTO requires cloud billing. FASHN v1.6 REST is an optional server-key adapter, disabled by default, requiring external consent.
- **Sources**: https://github.com/fashn-AI/fashn-vton-1.5 and https://fashn.ai/research/vton-1-5 . CPU float32 supported; approximately 2 GB main weights plus pose/parser. Current machine approximately 14 GiB RAM; no CUDA identified. Throughput unverified until actual inference.
- **Delegation**: Spec Kit research agent verified providers/contracts/privacy; no paid call or credential access.

## External option

- **Decision**: FASHN_API_KEY server-only. POST https://api.fashn.ai/v1/run, model tryon-v1.6, base64 person/garment, tops/flat-lay, return_base64; bounded poll /v1/status/{id}.
- **Rationale**: Optional deployment path when local hardware is insufficient.
- **Sources**: https://docs.fashn.ai/api-reference/tryon-v1-6 and https://docs.fashn.ai/api-overview/data-retention-privacy . Temporary input cleanup on completion with one-day backstop; output retrieval 60 minutes; metadata retained. App memory-only is not provider session-only.
- **Children**: https://help.fashn.ai/using-fashn/studio/try-on recommends avoiding child photos. Child presets remain synthetic local mockups, with no live child-input quality claim.

## Verification boundary

Mocked transports prove contracts, not generative quality. Real output required for SC-004. If model downloads/inference fail, keep executable adapters/setup and report the limitation. Never label template compositing as personal AI generation.

## Measured CPU profile decision

- **Decision**: Default native 864 x 576, 20 steps on CPU/GPU. Experimental CPU preview 432 x 288, 12 steps remains opt-in only. Full CPU step measured about 122 seconds. Adapter changes only public pipeline resize/input-shape attributes, not third-party source.
- **Rationale**: Reduced token count completed real inference in 299 seconds, but visual inspection found a missing polo collar and incomplete lower-shirt replacement. Dynamic shape support does not establish generative quality at a different resolution. Native validation is required; the experimental preview is not suitable for visual acceptance.
- **Alternatives considered**: Native CPU profile would take roughly 40 minutes at measured step speed; hosted AI remains optional with credentials/consent.

- **Native validation**: Real HTTP request completed in 2443.8 seconds. Visual inspection confirmed collar/buttons, full green polo and flower artwork. Small lettering remained blurred/altered; only a fictional test input was used. CPU latency prevents interactive use; native quality is preferable to reduced-resolution preview.

## User-directed revision

- **Future AI decision**: OpenAI API replaces local AI as the eventual product engine. Existing local implementation is temporarily retained. Official image-generation documentation supports editing with image references: https://developers.openai.com/api/docs/guides/image-generation . Provider retention is not established by browser session-only storage; validate it before activation. No model/key/API call selected or activated here.
- **Mapping correction**: Independent affine angle maps placed logos away from the placket axis. Calibrated four-point projective planes now share the same physical artwork coordinates. Mesh subdivision renders perspective; overlapping clips avoid antialias seams. Fixed synthetic source photos still limit geometric accuracy versus a calibrated 3D model.
- **Fabric options**: Read-only MFG-04 fictional demo materials are 100% cotton and 65/35 cotton-polyester. Reuse these options for the authorized polo demo; no seed/catalog edits. Same source photo illustrates both compositions, not a fabric simulation.
# Surface-aware mockup correction

The prior subdivided homography was still a flat plane. This revision calibrates 25 independent landmarks per angle against the existing blank photograph: centre follows placket/body, outer columns follow torso. Bilinear cells supply a nonplanar image warp, and triangles render it deterministically. Blank-template luminance modulates artwork RGB; alpha stays intact. A placket polygon excludes buttons from printing. No AI request occurs when selecting a view. Existing synthetic templates are retained and manually calibrated; they are not a matched 3D capture or production asset kit. Visual checks cover both wearer chest sides on both angles, central artwork, transparent artwork and the solid rectangle before background removal. A professional kit would improve colour masks, exact garment consistency and local fold displacement further.
