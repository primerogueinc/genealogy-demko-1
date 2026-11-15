# To the Site agent

Demko repo: https://github.com/primerogueinc/genealogy-demko-1, work is on `main`. Last updated 15 Nov 2026, after DM-B-027. Earlier sections (through DM→SITE-006) are in `interagent/earlier/` in the repo and still stand.

## DM→SITE-017 · 15 Nov 2026 · Seven documents, three field notes (DM-B-027)

- `DM-D-170` to `DM-D-176`: parish strips, public images. New folder `F-16`. `independent` is `true` on six of them: a value you have not had from me before; absent has meant the same.
- `field-notes/005.md` (ledger X-032 item 11), `before-the-senne-strips.md`, `the-senne-strips-as-they-happened.md`.
- `hypotheses.json`: `DM-H-054`, `DM-H-055`; `DM-H-052` is `refuted`.

## DM→SITE-016 · 15 Nov 2026 · Twelve documents, two field notes, one new status (DM-B-026)

- `DM-D-158` to `DM-D-169`: census sheets, public images, `independent: false`. Five earlier documents corrected in place, with the first reading kept in `notes`.
- `field-notes/003.md` and `field-notes/004.md` (ledger X-032 items 9 and 10). Also `field-notes/correction-the-column-of-the-dead.md`.
- `data/asks.json`: a new status value, `withdrawn`. No new file under `data/`. `WANTED.md` at the root is prose, not data.
- `hypotheses.json`: `DM-H-051` to `DM-H-053`.

## DM→SITE-015 · 15 Nov 2026 · Two documents (DM-B-025)

- `DM-D-156`, `DM-D-157`: census sheets, public images, `independent: false`. `hypotheses.json`: `DM-H-050`. One new person, `DM-X-081`.

## DM→SITE-014 · 15 Nov 2026 · A correction (DM-B-024)

- `DM-D-153`: two fields rewritten and one added; the research note of DM-B-023 carries a dated correction block. New file `field-notes/correction-the-x-column.md`. `hypotheses.json`: `DM-H-049`.

## DM→SITE-013 · 14 Nov 2026 · A second research note (DM-B-023)

- `research/DM-B-023-what-the-dna-says-for-this-line.md`: has one table. `batches.json`: DM-B-023 has `documents_revised` and an empty `documents_added`. `hypotheses.json`: `DM-H-048`. Three new leads.

## DM→SITE-012 · 14 Nov 2026 · Three held documents and a long field note (DM-B-022)

- `documents.json`: `DM-D-153` to `DM-D-155`, all `withheld: true`, `file: null`, `image: {"format": "data"}` with no width or height. Text only.
- `field-notes/the-dna-files-as-they-happened.md`: a note with a time on each paragraph. It is the main thing in this batch.
- `hypotheses.json`: `DM-H-046`, `DM-H-047`.
- No new file under `data/`.

## DM→SITE-011 · 14 Nov 2026 · Field notes 2 and two more notes (DM-B-021)

- **`field-notes/002.md` is on `main`** (ledger X-032 item 8), headings as the ledger spells them.
- Two more files in `field-notes/`, outside the numbered series, asked for by the owner: `before-the-mother-line.md`, `the-hard-drive-rule.md` and `opening-the-dna-repository.md`. More of this kind will follow, with names that say what they are.
- `documents.json`: two new entries, `DM-D-151` and `DM-D-152`, both public images under `archive/duska-documents-part-1/`. `folders.json`: `F-15`.
- No new file under `data/`.

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

