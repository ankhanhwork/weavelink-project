# Product design handoff

Canonical requirements: docs/spec/specs/spec-MFG-05.md and S13/S49/S50/S51 screen documents. PNG references retain S13's Dony style. This branch keeps runnable demo/polo; documentation-only branches should select only docs/spec changes and never docs/env/.env.

planning-archive/ contains the former top-level specs/ working documents. They are historical prototype notes, not the approved specification or required template. The original S13 PNG and reproducible HTML mockup source are preserved in polo/web/spec-reference/.

Reuse render.js, geometry.js and print-surface.js for deterministic template mapping, alpha-safe warp and fabric lighting. Reuse session-guard.js/app.js for stale reply checks and ai.py/server.py for backend image editing/validation. Inspect canonical requirements before porting: production authorization/quotas, saved artwork processing provenance and full cancelled/consent-revocation flows must follow the specs, not assume the single-user loopback prototype implements every production rule.

Do not port template-specific grid offsets to another garment; author and visually approve calibrated templates per product. Part 03 uses OpenAI only. Do not inspect .env or copy secrets into source/frontend, branch commits or logs.
