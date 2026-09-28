# WeaveLink Data Package

This folder contains the approved Session 5 data-model package for WeaveLink. It translates the product specification in [`docs/spec/`](../docs/spec/) into a traceable entity dictionary, CRUD analysis, conceptual ERD, logical model, review report, and deterministic synthetic seed data.

`docs/spec/` remains the source of truth for product requirements. Files in this folder describe those requirements as data structures; they do not replace or silently amend the specification.

## Contents

| Path | Purpose |
|---|---|
| [`01-entity-dictionary.md`](01-entity-dictionary.md) | Canonical entities, definitions, ownership, aliases, classifications, and approved conflict resolutions. |
| [`02-crud-matrix.md`](02-crud-matrix.md) | Function-to-entity Create/Read/Update/Delete interactions, entity coverage, and resolved anomalies. |
| [`03-erd.mmd`](03-erd.mmd) | Conceptual Mermaid ERD containing entities, cited relationships, cardinality, and optionality only. |
| [`04-data-model.md`](04-data-model.md) | Logical tables, attributes, keys, constraints, citations, and the conceptual ERD embedded unchanged. |
| [`05-review.md`](05-review.md) | Quality rubric, scenario and release-priority coverage, seed exceptions, and integrity-check results. |
| [`seed/`](seed/) | One generated CSV per logical table and the local deterministic generator. |

## Traceability and scope

- Every persisted entity, field group, relationship, and constraint is traceable to relevant material under `docs/spec/`.
- A data type is recorded only when `docs/spec/` declares it; all other field types remain unassigned until the Plan step.
- The logical model covers the approved product scope. Seed coverage distinguishes the Must/MVP, Should, Could, and Won't priorities defined in `docs/spec/mvp-scope-proposal.md`.
- The package does not add behavior that is absent from the specification. Unsupported seed quantities or scenarios are documented as evidence-based exceptions in [`05-review.md`](05-review.md).
- `03-erd.mmd` is a diagram-only file. The copy embedded in `04-data-model.md` must remain unchanged from it.

## Seed data

All CSV content is synthetic. No row may contain data from a real person, organization, payment, order, or product.

The current package contains one CSV for each logical table. Generated files use:

- a header row and logical-model column order;
- rows sorted by primary key;
- deterministic identifiers and values;
- UTF-8 encoding and LF line endings;
- ISO dates and timestamps;
- foreign keys that resolve to rows in the matching CSV;
- only enum values and states supported by the specification.

The retained generator is `data/seed/generate_seed.py`. Run it from the repository root:

```powershell
uv run data/seed/generate_seed.py
```

The script regenerates the CSV files and runs their integrity assertions. A successful run reports every check as `PASS`.

## Git policy

- `data/seed/generate_seed.py` is intentionally ignored and retained locally.
- Generated `data/seed/*.csv` files remain eligible for Git tracking.
- Do not edit generated CSV files manually; update the approved model and generator, then regenerate them.
- Do not modify `docs/spec/` as part of a data-model change unless a human explicitly requests that exact specification change.

## Change workflow

1. Confirm the requirement in `docs/spec/` and its citation.
2. Update the entity dictionary and CRUD matrix when the affected concept or interaction changes.
3. Update the conceptual ERD and keep its embedded copy in the logical model byte-equivalent.
4. Update the logical model without introducing uncited requirements.
5. Regenerate seed CSV files and run all integrity checks.
6. Update the review report with coverage, exceptions, and validation results.
