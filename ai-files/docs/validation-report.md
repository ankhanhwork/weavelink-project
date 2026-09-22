# Documentation validation report

Final validation is run from the repository root.

| Check | Result |
|---|---|
| `node ai-files/scripts/validate-docs.mjs` | Failed: 9,877 checks, 1 pre-existing sequence-heading error; 0 new errors |
| `node ai-files/scripts/validate-docs.mjs --build` | Generated `ai-files/tmp/documentation-index.json` with passed=false and the same pre-existing error |
| `git diff --check` | Unavailable: no .git metadata in this checkout; added-line whitespace checked against the pre-edit snapshot |
| Clarification-marker scan | Passed; no inherited clarification, task, or placeholder marker remains |
| Original-file dependency scan | Passed; README, docs, specs, and screens do not depend on `ai-files` |

The validator inspects 68 Markdown files, 96 module-qualified functions, 49 use cases, 43 screen specifications (including deprecated S16; its historical PNG is retained), 144 local links, 47 Mermaid blocks, the original teacher-format heading/table schemas, and the 17 original PNG files. It also requires the exact `Don't have mockup` note for all 26 screens without supplied images.

## Out-of-scope observations

The untouched baseline also fails with `Sequence heading format or ID set changed` (9,813 checks). In docs/architecture/sequence.md, the existing SD-04 heading uses an en dash after its ID instead of the colon required by the validator. It is unchanged under the approved scope; the validator logic is unchanged. The prior report/index counts were stale; counts above come from the actual run.

Existing SD-07 creates a checkout batch contrary to the locked no-batch-at-checkout rule; SD-09 uses Ordered/Failed order transitions contrary to the locked lifecycle. These unrelated diagrams are unchanged. Existing SD-10..SD-14 headings and the baseline total of 47 Mermaid blocks also predate this change; sequence inventory wording outside SD-05B is not revised. The acceptance checklist's existing claim that the validator independently checks worked pricing examples is not implemented by the script and remains an out-of-scope observation.

The documentation validator does not parse Mermaid syntax; its fence/count checks do not establish that diagrams render successfully.

## Limits

This repository contains no application runtime, package manifest, application test suite, or application build command. The documentation build creates a machine-readable index and does not execute future business code. Mermaid blocks are fence-checked and counted but are not processed by a Mermaid renderer. The future VNPay adapter must still run its sandbox, signature, reconciliation, and refund scenarios described in [the adapter contract](integrations/vnpay.md).
