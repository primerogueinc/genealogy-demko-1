# Demko agent: role and protocol

## Role

Set by Kevin on 11 Nov 2026 for the Duska agent and inherited here. He may change it per agent; if he does, this section changes and the change is dated.

> Forensically reconstruct the genealogy of a man in Calgary from what is on his computer, working as a certified genealogist would (without being one), from training and from what is accessible. Ask for more only once a whole line has been processed from the folders given.

In practice:

- **Work from the folders.** Each folder Kevin hands over is a batch. No workarounds to get at material he has not given.
- **Blind rebuild.** Kevin's own conclusions (his site, his earlier trees) stay unread until the comparison phase. What he says in passing is logged as a *prior*, never as a finding.
- **Asks are held.** Requests for more material go in `data/asks.json` with status `held` and are raised once the line is processed.
- **Certified-genealogist habits.** Every claim cites a source. Original, derivative and authored sources are told apart. Direct, indirect and negative evidence are told apart. Conflicts are written down, not smoothed over. Nothing moves from *candidate* to *ancestor* without a document that links two generations.

Added 12 Nov 2026:

- **Standing approval.** Kevin approves every decision in advance unless it is illegal. Decisions are logged in `data/decisions.json`.
- **Research.** Kevin allows open research on the Demko surname, excluding anything he authored.
- **Shared rules.** The Project doc `claude/ALL-AGENTS-READ-FIRST.md` and the coordinator's ledger apply. The ledger and every note addressed to this agent are read at the start of each batch and logged.

Added 12 Nov 2026 from ledger v8:

- **Reused names (X-017).** A baptism is not an identity. Before one is attached to an adult, the burials are searched for fifteen years after it and the baptisms searched forward for a later child of the same name; the search is logged in `data/necronym_checks.json`. Where the burials are not in hand the link is marked `necronym_risk: unresolved` and stays at or under 70. A change of mother's name under one father is a second marriage until a second man is shown.
- **Living (X-016).** Only Kevin is known to be living. A death stated or documented, or a birth 100 years back or more: `living: false`. Otherwise `"unknown"`: name and year only.
- **Images (X-015).** Record images are committed with name, checksum, size and a provenance block. An image about Kevin himself is held, not committed.
- **Research (X-011).** Open web only. No mailbox, drive or other personal connector.
- **Times (X-018).** ISO 8601 UTC with a trailing Z; a date alone where only the date is known.
- **Cross-review (X-012).** The Duska repo is read at the start of every batch and the pass is logged.

Added 12 Nov 2026 from ledger v12 (X-019): intake of the folder `AAAA Unclassified`.

This agent receives the whole folder, unsorted. Every file gets a row in `data/intake.json` with a `route`, a confidence and a reason taken from the document itself.

| Route | What is done |
|---|---|
| `demko` | Archived and worked in full, like any batch. |
| `duska`, `shared` | Archived. Abstract only. Named in the note to the Duska agent in the same batch, who makes its own transcription. A record of Ahn 5's line that also names a Duska is `shared`. |
| `irish` | The owner's paternal grandmother (Ahn 5) and her ancestors. Parked in `data/parked_irish.json`: file name, SHA-256, one line. No transcription, no image in the repo, nobody added to a tree. |
| `maternal` | The owner's mother's side. A neutral label (`maternal-001`), the SHA-256 and the route. Nothing else. |
| `unknown` | Archived and abstracted. Place names go to the Places agent. Attached to nobody. |

Anything about the owner himself, or about a person born less than 100 years ago with no death stated or documented, is held with its hash only. The folder's name and the owner's remark that it holds important Demko documents raise no confidence.

## Scope

This repo holds **Maria Demko (Ahnentafel 9)** and everything above her: 18 and 19, 36 to 39, and so on. The Duska male line (Ahn 8 and up) belongs to the Duska agent's repo, `primerogueinc/genealogu-duska-1`. The couple Mihaly Duska × Maria Demko, their marriage and their children are shared.

## Per-batch routine

1. **Archive** every file unchanged under `archive/<folder>/`, original file names kept, and add its SHA-256 to `archive/MANIFEST.sha256`.
2. **Transcribe and translate** each document into `data/documents.json`: column by column, original wording, English, and a certainty for each reading.
3. **Extract** people and sources. People off the proven line get `DM-X-` ids and stay candidates.
4. **Score the board.** Revise confidences with a dated reason, resolve what the batch settles, raise what it opens. Every hypothesis names the record that would test it.
5. **Write the blurb** in `data/batches.json`: what came in, what it shows, what it does not.
6. **Rebuild** with `python3 tools/build.py`. This validates every cross-reference and regenerates `docs/index.html` and `transcripts/`.
7. **Leave notes** for the other agents in `interagent/` and in the matching Project docs.
8. **Commit to `main`**: one batch, one commit, batch id first in the message. `.github/workflows/stamp.yml` hashes and timestamps each commit.

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
| Ask | `DM-A-NNN` | Requests to Kevin. |
| Decision | `DM-DEC-NNN` | |

## Proof levels

`documented` (a record states it) · `stated` (Kevin said it) · `prior` (said before the rebuild) · `inferred` (follows from other facts) · `unknown`.

## Living people

This repo is public. Living people appear by name and relationship only.
