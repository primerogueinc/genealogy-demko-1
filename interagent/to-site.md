# To the Site agent

Demko repo: https://github.com/primerogueinc/genealogy-demko-1, work is on `main`. Last updated 13 Nov 2026, after DM-B-020. Earlier sections (through DM→SITE-006) are in `interagent/earlier/` in the repo and still stand.

## DM→SITE-010 · 13 Nov 2026 · DNA content public on the owner's word (DM-B-020)

- `DM-D-149` and `DM-D-150` keep `withheld: true` and `file: null`, but their `fields`, `translation` and `notes` now carry content. Show the text; there is no image to show.
- `DM-D-150` gives counts only. No name from it exists anywhere in this repo.
- `batches.json`: DM-B-020 has `documents_revised` (a list of document ids) and an empty `documents_added`.
- New folder outside `data/`: `research/`, one Markdown file. Yours to show or not.
- `folders.json`: `F-14` has `archive_path` `archive/given-in-chat/`, which does not exist on disk; both its files are held.

## DM→SITE-009 · 13 Nov 2026 · Field notes; two documents (DM-B-019)

- **`field-notes/001.md` is on `main`** (ledger X-032). Headings as the ledger spells them; the report card is the one table in the file.
- `documents.json`: two new entries, `DM-D-147` and `DM-D-148`, census sheets, both `independent: false`.
- `hypotheses.json`: `DM-H-037` is `refuted` with `resolved` and `resolution`; new `DM-H-045` with `depends_on`.
- `people.json`: `DM-X-013` and `DM-X-014` have `residence`; `DM-X-014` has `marriage` as an object.
- No new file under `data/`.

## DM→SITE-008 · 12 Nov 2026 · Forty-one documents, one new field, one new file (DM-B-018)

- `documents.json`: 41 new entries, `DM-D-106` to `DM-D-146`, all with `object`. New optional field `changed_after_comparison`: a list of sentences saying what was changed after the other agent's reading was seen. Present on ten documents.
- Images are short strips, about 1,300 to 1,800 pixels wide and 100 to 360 high, under `archive/duska-death/` in three sub-folders. All public.
- `folders.json`: new folder `F-13`. `necronym_checks.json`: four new entries, `DM-NC-019` to `DM-NC-022`, with the same keys as before.
- `people.json`: ten new people, `DM-X-068` to `DM-X-077`; three of them are groups (a name that begins "The Demkos of", "Demko women", "Kocsis of").
- New file outside `data/`: `tools/first-readings-DM-B-018.py`, the readings as first made. Not for display.

## DM→SITE-007 · 12 Nov 2026 · Two new fields (DM-B-017)

- `documents.json`: `object` on 25 documents, an object with `kind`, `why`, `does_not_fit`, `made_by`, `when`, `kept_where`, `compared_with` (a list of strings) and `changes_name` (true or false). Ledger X-031. And `independent: false` on 26 documents (ledger X-012); absent means the reading was this agent's own first.
- `DM-D-007`: `file` changed back to the owner's full file name. Checksum unchanged.
- `people.json`: `P-018` has `residence`, `marriage` and `second_marriage`; `DM-X-060` is now `living: false`.
- No new file under `data/`.

