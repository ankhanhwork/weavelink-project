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
| [`06-edge-case-register.md`](06-edge-case-register.md) | Enumerated lifecycle, boundary, privacy, and data-rule fixture coverage. |
| [`07-end-to-end-traceability.md`](07-end-to-end-traceability.md) | PRD-to-FR-to-field-to-seed-to-screen index and three reviewer-ready trace examples. |
| [`data-model-MFG-01.md` ... `data-model-MFG-12.md`](.) | Per-module data-model views; each persisted entity has exactly one schema owner module. |
| [`schema/`](schema/) | SQLite validation schema, deterministic filename-order loader, and execution instructions. |
| [`seed/`](seed/) | One generated, numerically ordered CSV per logical table and the deterministic generator. |
| [`tools/check_data_package.py`](tools/check_data_package.py) | Checks catalogue, ERD, schema, seed, ownership, phone-type, and unique-constraint consistency. |
| [`tools/check_end_to_end_traceability.py`](tools/check_end_to_end_traceability.py) | Checks FR coverage and the three exact trace fixtures. |

## Traceability and scope

- Every persisted entity, field group, relationship, and constraint is traceable to relevant material under `docs/spec/`.
- The canonical logical model records only types declared by `docs/spec/`. The SQLite validation schema uses conservative physical types inferred from the synthetic seed shape; it validates this Session 7 data package and does not select the future application stack.
- The logical model covers the approved product scope. Seed coverage distinguishes the Must/MVP, Should, Could, and Won't priorities defined in `docs/prd.md`.
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

The script validates the complete in-memory package before writing any CSV file, then regenerates the files. A successful run reports every check as `PASS`.

CSV files have a two-digit filename prefix. The prefixes are the approved deterministic load order for the SQLite validation schema; do not rename an individual seed file manually.

## SQLite schema and seed-load check

The Session 7 validation database is **SQLite**. It proves that the schema can create an empty database and that all seed CSV files load in filename order with foreign-key validation. It is not a decision about the future application technology stack.

No external database installation is required; the loader uses Python's standard-library `sqlite3`. From the repository root:

```powershell
uv run data/schema/load_seed.py --database data/schema/weavelink-midterm.db
```

The loader creates the `.db` file, runs `schema-MFG-01.sql` through `schema-MFG-12.sql`, then imports every `data/seed/*.csv` file in ascending filename order inside one transaction. Foreign keys are deferred because approved cross-module records contain deliberate cycles; SQLite validates them at commit. A successful run ends with `PASS SQLite schema creation and filename-order seed load.` The generated `.db` file is a local verification artefact and is git-ignored.

## Git policy

- `data/seed/generate_seed.py`, `data/seed/seed-order.json`, and generated `data/seed/*.csv` files are version-controlled.
- Do not edit generated CSV files manually; update the approved model and generator, then regenerate them.
- Do not modify `docs/spec/` as part of a data-model change unless a human explicitly requests that exact specification change.

## Change workflow

1. Confirm the requirement in `docs/spec/` and its citation.
2. Update the entity dictionary and CRUD matrix when the affected concept or interaction changes.
3. Update the conceptual ERD and keep its embedded copy in the logical model byte-equivalent.
4. Update the logical model without introducing uncited requirements.
5. Regenerate seed CSV files and run all integrity checks.
6. Run the SQLite schema-and-seed-load check.
7. Update the review report with coverage, exceptions, and validation results.
