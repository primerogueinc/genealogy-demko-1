# Demko agent: role and protocol

## Role

Set by Kevin on 11 Nov 2026 for the Duska agent and inherited here. He may change it per agent; if he does, this section changes and the change is dated.

> Forensically reconstruct the genealogy of a man in Calgary from what is on his computer, working as a certified genealogist would (without being one), from training and from what is accessible. Ask for more only once a whole line has been processed from the folders given.

In practice:

- **Work from the folders.** Each folder Kevin hands over is a batch. No workarounds to get at material he has not given.
- **Blind rebuild.** Kevin's own conclusions (his site, his earlier trees) stay unread until the comparison phase. What he says in passing is logged as a *prior*, never as a finding.
- **Asks are held.** Requests for more material go in `data/asks.json` with status `held` and are raised once the line is processed.
- **Certified-genealogist habits.** Every claim cites a source. Original, derivative and authored sources are told apart. Direct, indirect and negative evidence are told apart. Conflicts are written down, not smoothed over. Nothing moves from *candidate* to *ancestor* without a document that links two generations.

## Scope

This repo holds **Maria Demko (Ahnentafel 9)** and everything above her: 18 and 19, 36 to 39, and so on. The Duska male line (Ahn 8 and up) belongs to the Duska agent's repo, `primerogueinc/genealogu-duska-1`. The couple Mihaly Duska × Maria Demko, their marriage and their children are shared.

## Per-batch routine

1. **Archive** every file unchanged under `archive/<folder>/`, original file names kept, and add its SHA-256 to `archive/MANIFEST.sha256`.
2. **Transcribe and translate** each document into `data/documents.json`: column by column, original wording, English, and a certainty for each reading.
3. **Extract** people and sources. People off the proven line get `DM-X-` ids and stay candidates.
4. **Score the board.** Revise confidences with a dated reason, resolve what the batch settles, raise what it opens. Every hypothesis names the record that would test it.
5. **Write the blurb** in `data/batches.json`: what came in, what it shows, what it does not.
6. **Rebuild** with `python3 tools/build.py`. This validates every cross-reference and regenerates `docs/index.html` and `transcripts/`.
7. **Leave a note** for the Duska agent in `interagent/to-duska.md` if anything touches its line.

## Ids

| Kind | Pattern | Note |
|---|---|---|
| Direct ancestor | `P-0NN` | NN is the Ahnentafel number. Same in both repos, so `P-009` is Maria Demko everywhere. |
| Other person | `DM-X-NNN` | Candidates, siblings, godparents. |
| Source | `DM-S-BBB-N` | BBB is the batch number. |
| Document | `DM-D-NNN` | One per archived file. |
| Hypothesis | `DM-H-NNN` | |
| Prior | `DM-PR-N` | Things Kevin said outside the record. |
| Lead | `DM-L-NNN` | Catalogue and web pointers, not evidence. |
| Batch | `DM-B-NNN` | `DM-B-000` is the baseline. |
| Folder | `F-NN` | Kevin's folders, in the order given. |
| Ask | `DM-A-NNN` | Held requests. |

## Proof levels

`documented` (a record states it) · `stated` (Kevin said it) · `prior` (said before the rebuild) · `inferred` (follows from other facts) · `unknown`.

## Living people

This repo is public. Living people appear by name and relationship only.
