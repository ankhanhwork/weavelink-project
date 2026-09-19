# Documentation validation report

Final run: 2026-09-19, from the repository root.

| Check | Result |
|---|---|
| `node scripts/validate-docs.mjs` | Passed: 7,016 checks, 0 errors |
| `node scripts/validate-docs.mjs --build` | Passed; generated `tmp/documentation-index.json` |
| `git diff --check` | Passed; no whitespace errors |
| Unresolved-placeholder scan | Passed; no unresolved-question markers, task markers, stale missing-spec claims or invalid use-case marker |

The validator inspected 68 Markdown files, 94 unique module-qualified functions, 49 unique use cases, 43 screen specifications, 279 local links, 19 Mermaid code blocks and four independently recalculated price examples. It also checks every function/FR and owned use-case reference per module, screen catalogue coverage, module links, qualified function references, selected high-risk screen semantics, local targets, table structure, code-fence balance, screen/use-case/function IDs, the single human-input register and the original 17 PNG count.

## Limits

This repository contains no application runtime, package manifest, application test suite or application build command, so no executable product was built or tested. The documentation build creates a machine-readable index; it does not render Markdown/Mermaid or prove future code behavior. Mermaid blocks were counted and fence-balanced, not processed by a Mermaid renderer. VNPay behavior was reconciled against the official sandbox protocol pages, but the future adapter must still run the sandbox/security cases in [the adapter contract](integrations/vnpay.md). The scenarios in [acceptance-checklist.md](acceptance-checklist.md) are required future application tests, not claims that those flows have run.
