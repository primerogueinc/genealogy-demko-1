#!/usr/bin/env python3
"""Validate data/*.json and regenerate docs/index.html and transcripts/.

Run from anywhere:  python3 tools/build.py
"""
import hashlib
import html
import json
import re
import shutil
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
DOCS = ROOT / "docs"
NAMES = ["people", "sources", "documents", "priors", "hypotheses",
         "batches", "folders", "leads", "asks", "decisions"]


def load():
    return {n: json.loads((DATA / f"{n}.json").read_text(encoding="utf-8")) for n in NAMES}


def validate(d):
    errs = []
    ids = {}
    for n in NAMES:
        for row in d[n]:
            if row["id"] in ids:
                errs.append(f"duplicate id {row['id']}")
            ids[row["id"]] = n

    def need(ref, kinds, where):
        if ref is None:
            return
        if ids.get(ref) not in kinds:
            errs.append(f"{where}: {ref!r} is not a known {'/'.join(kinds)} id")

    for p in d["people"]:
        for s in p["sources"]:
            need(s, ("sources", "priors"), p["id"])
    for s in d["sources"]:
        need(s["batch"], ("batches",), s["id"])
        need(s.get("document"), ("documents",), s["id"])
    for doc in d["documents"]:
        need(doc["batch"], ("batches",), doc["id"])
        need(doc["folder"], ("folders",), doc["id"])
        need(doc["source"], ("sources",), doc["id"])
        f = ROOT / doc["file"]
        if not f.is_file():
            errs.append(f"{doc['id']}: missing file {doc['file']}")
        elif hashlib.sha256(f.read_bytes()).hexdigest() != doc["sha256"]:
            errs.append(f"{doc['id']}: sha256 mismatch for {doc['file']}")
    for h in d["hypotheses"]:
        need(h["raised"], ("batches",), h["id"])
        need(h["resolved"], ("batches",), h["id"])
        if not 0 <= h["confidence"] <= 100:
            errs.append(f"{h['id']}: confidence out of range")
        for step in h.get("history", []):
            need(step["batch"], ("batches",), h["id"])
    for b in d["batches"]:
        need(b["folder"], ("folders",), b["id"])
        for key, kinds in (("raised", ("hypotheses",)), ("resolved", ("hypotheses",)),
                           ("revised", ("hypotheses",)), ("people_added", ("people",)),
                           ("sources_added", ("sources",)), ("documents_added", ("documents",))):
            for ref in b.get(key, []):
                need(ref, kinds, b["id"])
    for f in d["folders"]:
        for ref in f["batches"]:
            need(ref, ("batches",), f["id"])
    for l in d["leads"]:
        for ref in l["bears_on"]:
            need(ref, ("hypotheses",), l["id"])
    for a in d["asks"]:
        need(a["raised"], ("batches",), a["id"])
    # every archived file is in the manifest and in documents.json
    manifest = {}
    mf = ROOT / "archive" / "MANIFEST.sha256"
    if mf.is_file():
        for line in mf.read_text(encoding="utf-8").splitlines():
            digest, name = line.split(None, 1)
            manifest[name.strip().lstrip("./")] = digest
    documented = {doc["file"] for doc in d["documents"]}
    for f in sorted((ROOT / "archive").rglob("*")):
        if f.is_file() and f.name not in ("MANIFEST.sha256", ".gitkeep"):
            rel = f.relative_to(ROOT).as_posix()
            if rel not in documented:
                errs.append(f"archived file has no document entry: {rel}")
            if f.relative_to(ROOT / "archive").as_posix() not in manifest:
                errs.append(f"archived file missing from manifest: {rel}")
    return errs


def e(x):
    return html.escape("" if x is None else str(x), quote=True)


def slug(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def write_transcripts(d):
    out_root = ROOT / "transcripts"
    if out_root.exists():
        shutil.rmtree(out_root)  # generated; rebuilt from documents.json every run
    for doc in d["documents"]:
        rel = Path(doc["file"]).parent.relative_to("archive")
        out = out_root / rel / f"{doc['id']}_{slug(doc['title'])}.md"
        out.parent.mkdir(parents=True, exist_ok=True)
        r = doc["register"]
        lines = [
            f"# {doc['id']} · {doc['title']}", "",
            f"- **File:** `{doc['file']}`",
            f"- **SHA-256:** `{doc['sha256']}`",
            f"- **Kind:** {doc['kind']}",
            f"- **Language:** {doc['language']}",
            f"- **Collector's label:** {doc['collector_label']}",
            f"- **Parish:** {r['parish']}",
            f"- **Denomination:** {r['denomination']}",
            f"- **Page / reference:** {r['page']} / {r['archive_reference']}",
            f"- **Source id:** {doc['source']} · **Batch:** {doc['batch']} · **Folder:** {doc['folder']}",
            "", "## Transcription", "",
            "| Column | As written | English | Reading |", "|---|---|---|---|",
        ]
        for f in doc["fields"]:
            eng = f["english"] + (f" *({f['note']})*" if f.get("note") else "")
            lines.append(f"| {f['column']} | {f['original']} | {eng} | {f['certainty']} |")
        lines += ["", "## Translation", "", doc["translation"], "", "## Notes", ""]
        lines += [f"- {n}" for n in doc["notes"]]
        out.write_text("\n".join(lines) + "\n", encoding="utf-8")


CSS = """
:root{--bg:#f6f3ec;--card:#fffdf8;--ink:#23201b;--mute:#6f685c;--line:#ddd6c6;--acc:#7a3b2e;--ok:#2f6b4f;--warn:#9a6a12;--bar:#e7e0d0}
@media (prefers-color-scheme:dark){:root{--bg:#191714;--card:#211e1a;--ink:#ebe5d8;--mute:#a39b8b;--line:#3a352d;--acc:#d98e7a;--ok:#7fc3a1;--warn:#e0b25a;--bar:#322d26}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.55 Georgia,'Iowan Old Style','Times New Roman',serif}
.wrap{max-width:1040px;margin:0 auto;padding:0 20px 80px}
header{padding:44px 0 18px;border-bottom:1px solid var(--line)}
h1{font-size:2rem;line-height:1.15;margin:0 0 8px;font-weight:600;letter-spacing:-.01em}
h2{font-size:1.3rem;margin:44px 0 14px;font-weight:600}
h3{font-size:1.02rem;margin:0 0 6px;font-weight:600}
p{margin:0 0 10px}
.sub{color:var(--mute);max-width:70ch}
.sans,nav,table,.pill,.meta,.id,.stat{font-family:system-ui,-apple-system,'Segoe UI',sans-serif}
nav{position:sticky;top:0;background:var(--bg);border-bottom:1px solid var(--line);padding:9px 0;font-size:.84rem;display:flex;gap:16px;flex-wrap:wrap;z-index:5}
nav a{color:var(--mute);text-decoration:none}nav a:hover{color:var(--acc)}
.stats{display:flex;gap:26px;flex-wrap:wrap;margin-top:18px}
.stat b{display:block;font-size:1.5rem;font-weight:600}.stat span{font-size:.78rem;color:var(--mute);text-transform:uppercase;letter-spacing:.06em}
.card{background:var(--card);border:1px solid var(--line);border-radius:6px;padding:16px 18px;margin:0 0 12px}
.id{font-size:.74rem;color:var(--mute);letter-spacing:.03em}
.pill{display:inline-block;font-size:.7rem;padding:1px 8px;border-radius:99px;border:1px solid var(--line);color:var(--mute);margin-left:6px;vertical-align:1px;white-space:nowrap}
.pill.documented,.pill.clear{color:var(--ok);border-color:var(--ok)}
.pill.uncertain,.pill.inferred,.pill.held{color:var(--warn);border-color:var(--warn)}
.pill.demko{color:var(--acc);border-color:var(--acc)}
.meta{font-size:.84rem;color:var(--mute)}
.chain{list-style:none;margin:0;padding:0}
.chain li{position:relative;padding:0 0 14px 26px;border-left:2px solid var(--line);margin-left:8px}
.chain li:last-child{border-left-color:transparent}
.chain li::before{content:'';position:absolute;left:-7px;top:6px;width:12px;height:12px;border-radius:50%;background:var(--card);border:2px solid var(--mute)}
.chain li.mine::before{border-color:var(--acc);background:var(--acc)}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:12px}
.bar{height:6px;background:var(--bar);border-radius:3px;margin:8px 0 10px;overflow:hidden}.bar i{display:block;height:100%;background:var(--acc)}
.conf{float:right;font:600 1.05rem system-ui,sans-serif;color:var(--acc)}
.hist{font-size:.84rem;color:var(--mute);border-top:1px dashed var(--line);margin-top:8px;padding-top:8px}
dl{margin:0;font-size:.92rem}dt{font:600 .72rem system-ui,sans-serif;text-transform:uppercase;letter-spacing:.06em;color:var(--mute);margin-top:8px}dd{margin:0}
.scan{overflow-x:auto;border:1px solid var(--line);border-radius:4px;background:#ddd;margin:10px 0}
.scan img{display:block;height:157px;max-width:none}
.tw{overflow-x:auto}
table{border-collapse:collapse;width:100%;font-size:.86rem}
th,td{text-align:left;padding:7px 10px;border-bottom:1px solid var(--line);vertical-align:top}
th{font-size:.72rem;text-transform:uppercase;letter-spacing:.06em;color:var(--mute);font-weight:600}
td.orig{font-family:Georgia,serif;font-style:italic;font-size:.95rem;white-space:nowrap}
td small{display:block;color:var(--mute)}
code{font:.8rem ui-monospace,Menlo,Consolas,monospace;word-break:break-all}
a{color:var(--acc)}
pre{white-space:pre-wrap;font:.84rem/1.5 ui-monospace,Menlo,Consolas,monospace;margin:0}
blockquote{margin:0;padding-left:14px;border-left:3px solid var(--acc)}
footer{margin-top:50px;padding-top:16px;border-top:1px solid var(--line);font-size:.82rem;color:var(--mute)}
"""


def render(d):
    people = {p["id"]: p for p in d["people"]}
    direct = sorted((p for p in d["people"] if p["ahnentafel"]), key=lambda p: p["ahnentafel"])
    cands = [p for p in d["people"] if not p["ahnentafel"]]
    open_h = [h for h in d["hypotheses"] if h["status"] == "open"]
    P = []
    add = P.append

    def vital(p):
        b = p["birth"]
        bits = [x for x in (b.get("date"), b.get("place")) if x]
        return "b. " + ", ".join(bits) if bits else ""

    add("<header><div class='id'>DEMKO LINE · AI REBUILD · AHNENTAFEL 9 AND ABOVE</div>")
    add("<h1>Maria Demko and her people</h1>")
    add("<p class='sub'>A reconstruction of the ancestry of Maria Demko, wife of Mihaly Duska, "
        "built one folder at a time from a private archive and scored against its own hypotheses. "
        "Nothing here is a proven pedigree until a document links two generations.</p>")
    add("<div class='stats'>")
    for n, lab in ((len(d["batches"]) - 1, "folders processed"), (len(d["documents"]), "documents"),
                   (sum(1 for p in d["people"] if p["proof"] == "documented"), "people on record"),
                   (len(open_h), "open hypotheses"),
                   (sum(1 for h in d["hypotheses"] if h["status"] != "open"), "resolved")):
        add(f"<div class='stat'><b>{n}</b><span>{e(lab)}</span></div>")
    add("</div></header>")
    add("<nav><a href='#line'>Line</a><a href='#batches'>Batch log</a><a href='#documents'>Documents</a>"
        "<a href='#board'>Hypotheses</a><a href='#candidates'>Candidates</a><a href='#priors'>Priors</a>"
        "<a href='#sources'>Sources</a><a href='#leads'>Leads</a><a href='#folders'>Folders</a>"
        "<a href='#asks'>Asks</a><a href='#decisions'>Decisions</a><a href='#agents'>Agents</a></nav>")

    add("<h2 id='line'>The line</h2><ul class='chain'>")
    for p in direct:
        mine = " class='mine'" if p["owner"] == "demko" else ""
        add(f"<li{mine}><span class='id'>{e(p['id'])} · Ahn {p['ahnentafel']}</span><br>"
            f"<b>{e(p['name'])}</b><span class='pill {e(p['proof'])}'>{e(p['proof'])}</span>"
            f"<span class='pill {e(p['owner'])}'>{e(p['owner'])} agent</span>"
            f"<div class='meta'>{e(p['role'])}{' · ' + e(vital(p)) if vital(p) else ''}</div>"
            f"<div class='meta'>{e(p['note'])}</div></li>")
    add("</ul>")

    add("<h2 id='batches'>Batch log</h2>")
    for b in reversed(d["batches"]):
        add(f"<div class='card'><span class='id'>{e(b['id'])} · {e(b['date'])} · {b['files']} file(s)</span>"
            f"<h3>{e(b['title'])}</h3><p>{e(b['blurb'])}</p><div class='meta'>"
            f"Raised: {e(', '.join(b['raised']) or 'none')} · Revised: {e(', '.join(b.get('revised', [])) or 'none')}"
            f" · Resolved: {e(', '.join(b['resolved']) or 'none')}</div></div>")

    add("<h2 id='documents'>Documents</h2>")
    if not d["documents"]:
        add("<p class='meta'>None yet.</p>")
    for doc in d["documents"]:
        ext = Path(doc["file"]).suffix
        r = doc["register"]
        add(f"<div class='card'><span class='id'>{e(doc['id'])} · source {e(doc['source'])} · {e(doc['batch'])}</span>"
            f"<h3>{e(doc['title'])}</h3><div class='meta'>{e(doc['kind'])} · {e(doc['language'])}</div>"
            f"<div class='scan'><img src='media/{e(doc['id'])}{e(ext)}' alt='Scan of {e(doc['title'])}'></div>"
            "<div class='tw'><table><tr><th>Column</th><th>As written</th><th>English</th><th>Reading</th></tr>")
        for f in doc["fields"]:
            note = f"<small>{e(f['note'])}</small>" if f.get("note") else ""
            add(f"<tr><td>{e(f['column'])}</td><td class='orig'>{e(f['original'])}</td>"
                f"<td>{e(f['english'])}{note}</td><td><span class='pill {e(f['certainty'])}'>{e(f['certainty'])}</span></td></tr>")
        add("</table></div><dl><dt>Translation</dt><dd><blockquote>" + e(doc["translation"]) + "</blockquote></dd>")
        add("<dt>Register</dt><dd>Parish: " + e(r["parish"]) + " Denomination: " + e(r["denomination"])
            + " Page: " + e(r["page"]) + ". Reference: " + e(r["archive_reference"]) + ".</dd>")
        add("<dt>Notes</dt><dd>" + "<br>".join(e(n) for n in doc["notes"]) + "</dd>")
        add(f"<dt>Collector's file name</dt><dd>{e(doc['collector_label'])}</dd>"
            f"<dt>Archived as</dt><dd><code>{e(doc['file'])}</code><br><code>sha256 {e(doc['sha256'])}</code></dd></dl></div>")

    add("<h2 id='board'>Hypothesis board</h2><div class='grid'>")
    for h in sorted(d["hypotheses"], key=lambda h: (h["status"] != "open", h["id"])):
        add(f"<div class='card'><span class='conf'>{h['confidence']}%</span><span class='id'>{e(h['id'])}</span>"
            f"<span class='pill'>{e(h['status'])}</span><span class='pill'>raised {e(h['raised'])}</span>"
            + (f"<span class='pill demko'>{e(h['question'])}</span>" if h.get("question") else "") +
            f"<div class='bar'><i style='width:{h['confidence']}%'></i></div><p><b>{e(h['statement'])}</b></p>"
            f"<dl><dt>Basis</dt><dd>{e(h['basis'])}</dd><dt>Test</dt><dd>{e(h['test'])}</dd>")
        if h["resolution"]:
            add(f"<dt>Resolution ({e(h['resolved'])})</dt><dd>{e(h['resolution'])}</dd>")
        add("</dl>")
        for s in h.get("history", []):
            add(f"<div class='hist'><b>{e(s['batch'])}: {s['from']}% → {s['to']}%.</b> {e(s['why'])}</div>")
        add("</div>")
    add("</div>")

    add("<h2 id='candidates'>People on record, not yet on the line</h2>")
    if not cands:
        add("<p class='meta'>None yet.</p>")
    else:
        add("<div class='tw'><table><tr><th>Id</th><th>Name</th><th>Role</th><th>Vital</th><th>Note</th><th>Source</th></tr>")
        for p in cands:
            add(f"<tr><td>{e(p['id'])}</td><td><b>{e(p['name'])}</b></td><td>{e(p['role'])}</td><td>{e(vital(p))}</td>"
                f"<td>{e(p['note'])}</td><td>{e(', '.join(p['sources']))}</td></tr>")
        add("</table></div>")

    add("<h2 id='priors'>Priors</h2><p class='meta'>What Kevin said outside the record. Held apart so the rebuild can be compared with it later.</p>"
        "<div class='tw'><table><tr><th>Id</th><th>Prior</th><th>Origin</th></tr>")
    for p in d["priors"]:
        add(f"<tr><td>{e(p['id'])}</td><td>{e(p['text'])}</td><td>{e(p['origin'])}</td></tr>")
    add("</table></div>")

    add("<h2 id='sources'>Sources</h2><div class='tw'><table><tr><th>Id</th><th>Source</th><th>What it gives</th><th>Weight</th></tr>")
    for s in d["sources"]:
        add(f"<tr><td>{e(s['id'])}</td><td><b>{e(s['title'])}</b><small>{e(s['type'])}</small></td>"
            f"<td>{e(s['extract'])}</td><td>{e(s['reliability'])}</td></tr>")
    add("</table></div>")

    add("<h2 id='leads'>Leads</h2><p class='meta'>Catalogue and web pointers. Not evidence.</p>"
        "<div class='tw'><table><tr><th>Id</th><th>Lead</th><th>Bears on</th></tr>")
    for l in d["leads"]:
        add(f"<tr><td>{e(l['id'])}</td><td>{e(l['text'])} <a href='{e(l['url'])}' rel='noopener'>link</a></td>"
            f"<td>{e(', '.join(l['bears_on']))}</td></tr>")
    add("</table></div>")

    add("<h2 id='folders'>Folders received</h2>")
    if not d["folders"]:
        add("<p class='meta'>None yet.</p>")
    else:
        add("<div class='tw'><table><tr><th>Id</th><th>Path on Kevin's computer</th><th>Files</th><th>Complete</th><th>Also given to</th><th>Kevin's description</th></tr>")
        for f in d["folders"]:
            add(f"<tr><td>{e(f['id'])}</td><td><code>{e(f['path'])}</code></td><td>{f['files_received']}</td>"
                f"<td>{'yes' if f['complete'] else 'no'}</td><td>{e(', '.join(f['shared_with']) or 'no one')}</td>"
                f"<td>{e(f['described_by_kevin'])}</td></tr>")
        add("</table></div>")

    add("<h2 id='asks'>Asks</h2><p class='meta'>Requests to Kevin. Held until a line has been processed, or until he asks.</p>"
        "<div class='tw'><table><tr><th>Id</th><th>Ask</th><th>Why</th><th>Status</th></tr>")
    for a in d["asks"]:
        add(f"<tr><td>{e(a['id'])}</td><td>{e(a['ask'])}</td><td>{e(a['why'])}</td>"
            f"<td><span class='pill {e(a['status'])}'>{e(a['status'])}</span></td></tr>")
    add("</table></div>")

    add("<h2 id='decisions'>Decisions</h2><div class='tw'><table><tr><th>Id</th><th>Date</th><th>Decision</th><th>Why</th></tr>")
    for x in d["decisions"]:
        add(f"<tr><td>{e(x['id'])}</td><td>{e(x['date'])}</td><td>{e(x['decision'])}</td><td>{e(x['why'])}</td></tr>")
    add("</table></div>")

    add("<h2 id='agents'>Agents</h2>")
    for f in sorted((ROOT / "interagent").glob("*.md")):
        if f.name != "README.md":
            add(f"<div class='card'><h3>{e(f.name)}</h3><pre>{e(f.read_text(encoding='utf-8'))}</pre></div>")

    add("<footer>Generated by <code>tools/build.py</code> from <code>data/</code>. "
        "Role and routine: <code>AGENT.md</code>. Living people appear by name only.</footer>")

    return ("<!DOCTYPE html>\n<html lang='en'><head><meta charset='utf-8'>"
            "<meta name='viewport' content='width=device-width,initial-scale=1'>"
            "<title>Demko line · AI rebuild</title><style>" + CSS + "</style></head><body><div class='wrap'>"
            + "\n".join(P) + "</div></body></html>\n")


def main():
    d = load()
    errs = validate(d)
    if errs:
        print("\n".join("ERROR " + x for x in errs))
        sys.exit(1)
    media = DOCS / "media"
    media.mkdir(parents=True, exist_ok=True)
    for doc in d["documents"]:
        shutil.copyfile(ROOT / doc["file"], media / (doc["id"] + Path(doc["file"]).suffix))
    write_transcripts(d)
    (DOCS / "index.html").write_text(render(d), encoding="utf-8")
    (DOCS / ".nojekyll").write_text("", encoding="utf-8")
    print(f"ok: {len(d['people'])} people, {len(d['documents'])} documents, "
          f"{len(d['hypotheses'])} hypotheses, {len(d['batches'])} batches")


if __name__ == "__main__":
    main()
