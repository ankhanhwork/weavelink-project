# Documentation validation report

Final validation is run from the repository root.

| Check | Result |
|---|---|
| `node ai-files/scripts/validate-docs.mjs` | Passed: 9,785 checks, 0 errors |
| `node ai-files/scripts/validate-docs.mjs --build` | Passed; generates `ai-files/tmp/documentation-index.json` |
| `git diff --check` | Passed; no whitespace errors |
| Clarification-marker scan | Passed; no inherited clarification, task, or placeholder marker remains |
| Original-file dependency scan | Passed; README, docs, specs, and screens do not depend on `ai-files` |

The validator inspects 68 Markdown files, 94 module-qualified functions, 49 use cases, 43 screen specifications, 147 local links, 29 Mermaid blocks, the original teacher-format heading/table schemas, and the 17 original PNG files. It also requires the exact `Don't have mockup` note for all 26 screens without supplied images.

## Limits

This repository contains no application runtime, package manifest, application test suite, or application build command. The documentation build creates a machine-readable index and does not execute future business code. Mermaid blocks are fence-checked and counted but are not processed by a Mermaid renderer. The future VNPay adapter must still run its sandbox, signature, reconciliation, and refund scenarios described in [the adapter contract](integrations/vnpay.md).
