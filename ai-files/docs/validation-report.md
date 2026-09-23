# Documentation validation report

Final validation is run from the repository root.

| Check | Result |
|---|---|
| `node ai-files/scripts/validate-docs.mjs` | Passed: 10,329 checks; 96 functions, 49 use cases, 45 screens, 181 local links, 47 Mermaid blocks |
| `node ai-files/scripts/validate-docs.mjs --build` | Not run; the non-build validation passed |
| `git diff --check` | Passed; only Git CRLF normalization warnings |
| Clarification-marker scan | Passed; no inherited clarification, task, or placeholder marker remains |
| Original-file dependency scan | Passed; README, docs, specs, and screens do not depend on `ai-files` |

The validator inspects 70 Markdown files, 96 module-qualified functions, 49 use cases, 45 screen specifications (S01-S15 and S17-S46), 181 local links, 47 Mermaid blocks, the original teacher-format heading/table schemas, and checks every current PNG is linked from a screen spec and embedded in that spec. S16 and its retired payment mockup are excluded. Linked images are visual references; written screen behavior takes precedence.

## Out-of-scope observations

The earlier SD-04 heading-format mismatch has been corrected; no current validation errors remain.

The validator checks Mermaid fences/counts but does not parse diagram syntax. Pricing examples are documented acceptance cases and are not independently recalculated by the script.

The documentation validator does not parse Mermaid syntax; its fence/count checks do not establish that diagrams render successfully.

## Limits

This repository contains no application runtime, package manifest, application test suite, or application build command. The documentation build creates a machine-readable index and does not execute future business code. Mermaid blocks are fence-checked and counted but are not processed by a Mermaid renderer. The future VNPay adapter must still run its sandbox, signature, reconciliation, and refund scenarios described in [the adapter contract](integrations/vnpay.md).
