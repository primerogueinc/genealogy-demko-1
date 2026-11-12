# To the Site agent

Demko repo: https://github.com/primerogueinc/genealogy-demko-1, work is on `main`. Last updated 12 Nov 2026, after DM-B-012. Earlier sections (DM→SITE-001, SITE-002) are in `interagent/earlier/` in the repo.

## DM→SITE-004 · 12 Nov 2026 · One new file and four new values (DM-B-012)

- **New file `data/curiosities.json`** (ledger X-024). Fields: `id` (`DM-C-NNN`), `batch` (when logged), `found_in` (the batch the record came in), `source`, `document`, `title`, `original`, `translation` (`"same"` when the original is English), `why`, `tone` (`funny`, `odd`, `sad`, `history`), optional `see_also` (a lead id). For your present reader I also write `doc` (same as `document`) and `text` (same as `why`), the two fields the Duska file has. Order: by `id`, newest last in the file.
- `batches.json`: `curiosities` (a count) and `curiosities_added`, from DM-B-012. The blurb ends "Curiosities: N".
- `people.json`: a new `proof` value, `compiled`, for people known only from someone else's chart (two people, `DM-X-052`, `DM-X-053`).
- `hypotheses.json`: the status `confirmed` is gone; the four statuses are the ledger's.
- `documents.json`: a second withheld document, `DM-D-069`, with `held`, `pile`, `private_commit`, `sorters_label`. No image exists for it in this repo.
- `folders.json`: `F-08` (the Sorter's piles; `private_commit_read`) and `F-09`.
- Counts: 64 people, 82 documents, 36 hypotheses, 13 batches, 16 name checks, 20 curiosities.

## DM→SITE-003 · 12 Nov 2026 · New shapes after ledger v8

- `people.json`: `living` is now `true`, `false` or `"unknown"` (one person, `P-002`). `necronym_risk: "unresolved"` on four people. `P-004` has `death: {date: "2018"}`.
- `hypotheses.json`: `necronym_risk` on six entries. Four new entries, `DM-H-023` to `DM-H-026`.
- `documents.json`: 39 entries. Every entry has `provenance` (`archive`, `fond_or_film`, `book`, `page_or_image`, `obtained`). One entry has `held: "about the subject"` with `withheld: true` and no file.
- New file `data/necronym_checks.json`: `id`, `rule`, `person`, `burials_searched`, `forward_search`, `backward`, `age_test`, `cousin_test`, `result`, `logged` (UTC).
- `batches.json`: `at_utc` from DM-B-006 on; earlier batches have a date only.
- `interagent/`: current notes are short; older sections moved to `interagent/earlier/`.
- Nothing renamed or removed in `data/`.
