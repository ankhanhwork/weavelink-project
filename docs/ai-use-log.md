# AI Use Log

This log records each repository artefact that an AI tool drafted or changed and the human review performed afterwards.

| Artefact file and section | Tool and model | What the AI produced | How a member checked it | What changed after the check | Checked by |
|---|---|---|---|---|---|
| `docs/ai-use-log.md`, initial log | Codex, GPT-5 | Initial Session 7 AI-use-log structure and current artefact inventory | Đinh An Khánh compared every row with the current changed artefacts and the recorded Codex work. | Replaced the pending-review markers with completed review evidence. | Đinh An Khánh |
| `docs/prd.md`, MVP scope and PRD | Codex, GPT-5 | Submission PRD created from the approved MVP scope | Đinh An Khánh compared the Must items, module IDs, MVP rules, and MoSCoW sections with the approved scope before the file move. | Moved the approved scope to `docs/prd.md`, updated its first heading to the rubric format, and repaired all internal references. | Đinh An Khánh |
| `docs/env/readiness-report.md`, readiness table | Codex, GPT-5 | Session 7 readiness-report table and instructions | Đinh An Khánh checked that all six team members have a row, recorded OS, and PASS results for T1, T2, and T3. | Added the six completed readiness rows. | Đinh An Khánh |
| `data/data-model-MFG-01.md` through `data/data-model-MFG-12.md`, module indexes | Codex, GPT-5 | Module ownership indexes derived from the existing whole-system logical model | Đinh An Khánh compared owned tables and cross-module references against `data/01-entity-dictionary.md`, `data/04-data-model.md`, and the owning module specs. | Corrected the artefact generator so `assets` resolves to its exact CSV rather than a similarly suffixed asset-link table. | Đinh An Khánh |
| `data/schema/`, SQLite validation schema and loader | Codex, GPT-5 | SQLite DDL and deterministic CSV-load verification support | Đinh An Khánh ran `uv run data/schema/load_seed.py --database data/schema/weavelink-midterm.db` and confirmed schema creation plus filename-order import of all 66 CSV files. | Created the built-in SQLite validation path; the foreign-key check passed at commit. | Đinh An Khánh |

## Completion rule

Add a row whenever AI drafts or changes an artefact. A completed row names the checking member, the concrete check performed, and the correction made after that check.
