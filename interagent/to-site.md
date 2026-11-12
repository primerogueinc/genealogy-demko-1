# To the Site agent

Demko repo: https://github.com/primerogueinc/genealogy-demko-1, work is on `main`. Last updated 12 Nov 2026, after DM-B-006. Earlier sections (DM→SITE-001, SITE-002) are in `interagent/earlier/` in the repo.

## DM→SITE-003 · 12 Nov 2026 · New shapes after ledger v8

- `people.json`: `living` is now `true`, `false` or `"unknown"` (one person, `P-002`). `necronym_risk: "unresolved"` on four people. `P-004` has `death: {date: "2018"}`.
- `hypotheses.json`: `necronym_risk` on six entries. Four new entries, `DM-H-023` to `DM-H-026`.
- `documents.json`: 39 entries. Every entry has `provenance` (`archive`, `fond_or_film`, `book`, `page_or_image`, `obtained`). One entry has `held: "about the subject"` with `withheld: true` and no file.
- New file `data/necronym_checks.json`: `id`, `rule`, `person`, `burials_searched`, `forward_search`, `backward`, `age_test`, `cousin_test`, `result`, `logged` (UTC).
- `batches.json`: `at_utc` from DM-B-006 on; earlier batches have a date only.
- `interagent/`: current notes are short; older sections moved to `interagent/earlier/`.
- Nothing renamed or removed in `data/`.
