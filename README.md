# Demko line: an AI rebuild

A batch-by-batch reconstruction of the ancestry of **Maria Demko**, wife of Mihaly Duska and great-grandmother of Kevin J.S. Duska Jr.

    Kevin J.S. Duska Jr. → Kevin John Duska → Stefan Duska → Mihaly Duska × Maria Demko

The work is done by an AI agent from folders of documents handed over one at a time, without sight of the earlier human research, so the two can be compared afterwards. The sister repo for the Duska male line is [`primerogueinc/genealogu-duska-1`](https://github.com/primerogueinc/genealogu-duska-1).

## Where things are

| Path | What |
|---|---|
| `docs/index.html` | The front end. Generated; open it in a browser. |
| `data/` | The record: people, sources, documents, hypotheses, priors, leads, batches, folders, asks. |
| `archive/` | Every file received, unchanged, with `MANIFEST.sha256`. |
| `transcripts/` | One transcription and translation per document. Generated from `data/documents.json`. |
| `interagent/` | Notes between this agent and the Duska agent. |
| `AGENT.md` | The agent's role, scope and routine. |
| `tools/build.py` | Validates the data and regenerates `docs/` and `transcripts/`. |

## Rebuild

    python3 tools/build.py

## Status

See the batch log on the front end. Nothing here is a proven pedigree until the board says so.
