#!/usr/bin/env python3
"""Render a product's system map from its source, in the one format every product uses.

Put this file and map.schema.json beside the source, model.json, in the map folder (the folder `model` under the repository's
`docs` folder), then run it from anywhere:

    python3 render_map.py            # check the source, then write product-map.md and gaps.md beside it
    python3 render_map.py --check    # the same checks, and fail if the two files on disk differ from a fresh render
    python3 render_map.py --list     # every subject id with its point
    python3 render_map.py --front    # print the front page
    python3 render_map.py --card ID  # print one subject's card

product-map.md is the front page (five sections; the current release's bets stand under its goal) followed by one card per subject (eleven headings, in a fixed order; one
with nothing to say is left out). gaps.md holds the same counts as the front page's last section, what they count, and at most
seven owner questions. Nothing is written when the source does not match the schema. The exit code is 1 when the schema, a
check or --check fails. A flag (a count outside the usual range, or a placing worth a look) is printed and does not fail.

Derived at each render and never stored: file counts, each path's point, Touches, open work and every count. Not derived: a
subject's tools (the source lists them) and the diagram (the source holds it as text). A folder's point is the first line of its
README, or else the leading comment of its entry file (index.ts, __init__.py and the like); a file's is its leading comment.

File counts and ownership read tracked files, so stage new files, then render. File counts change whenever a file is added
anywhere. Where the render is committed, render and check with --no-file-counts: the render then says nothing about how many
files there are, nor how many of them the subjects own, so an added file does not stale it.

Standard library only. Options: --source, --schema, --root (the repository root), --out (where the two files go) and
--no-file-counts.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path

SKIP_DIRS = {".git", "node_modules", "dist", "build", "__pycache__", ".venv", ".wrangler"}
DOC_TAGS = ("packageDocumentation", "fileoverview", "file", "overview", "description", "summary")  # a tag that opens a description; any other @tag is a directive
ENTRY_FILES = ("index.ts", "index.tsx", "index.js", "index.mjs", "__init__.py", "mod.rs", "doc.go")  # where a folder with no README states its point
FRONT_LIMIT = 10_000  # bytes; over it is a flag
MAX_QUESTIONS = 7
OUTPUTS = ("product-map.md", "gaps.md")


# ---- the schema: the part of JSON Schema that map.schema.json uses ----
def validate(value, schema: dict, root: dict, at: str = "model") -> list[str]:
    if "$ref" in schema:  # a reference stands for its definition; keys beside it only describe
        return validate(value, root["$defs"][schema["$ref"].rsplit("/", 1)[1]], root, at)
    if "const" in schema:
        return [] if value == schema["const"] else [f"{at}: must be {json.dumps(schema['const'])}"]
    if "enum" in schema:
        return [] if value in schema["enum"] else [f"{at}: must be one of {', '.join(json.dumps(v) for v in schema['enum'])}"]
    kind = schema.get("type")
    if kind == "string":
        if not isinstance(value, str):
            return [f"{at}: must be text"]
        if len(value) < schema.get("minLength", 0):
            return [f"{at}: must not be empty"]
        if "pattern" in schema and not re.search(schema["pattern"], value):
            return [f"{at}: {json.dumps(value)} is not allowed. {schema.get('description') or 'It must match ' + schema['pattern']}"]
        return []
    if kind == "array":
        if not isinstance(value, list):
            return [f"{at}: must be a list"]
        errors = []
        if len(value) < schema.get("minItems", 0):
            errors.append(f"{at}: needs at least {schema['minItems']}")
        if len(value) > schema.get("maxItems", len(value)):
            errors.append(f"{at}: takes at most {schema['maxItems']}")
        for n, item in enumerate(value):
            name = item.get("id") or item.get("name") if isinstance(item, dict) else None
            errors += validate(item, schema.get("items") or {}, root, f"{at}[{name if isinstance(name, str) else n}]")
        return errors
    if kind == "object":
        if not isinstance(value, dict):
            return [f"{at}: must be an object"]
        props = schema.get("properties") or {}
        errors = [f"{at}: missing key {json.dumps(key)}" for key in schema.get("required") or [] if key not in value]
        for key, item in value.items():
            if key in props:
                errors += validate(item, props[key], root, f"{at}.{key}")
            elif schema.get("additionalProperties") is False and not any(re.search(p, key) for p in schema.get("patternProperties") or {}):
                errors.append(f"{at}: unknown key {json.dumps(key)} (the schema names: {', '.join(props)})")
        return errors
    return []


# ---- reading the repository ----
def list_files(root: Path) -> list[str]:
    """Every file under the root. Inside a git work tree (the root may be a subfolder of it) these are the files git tracks, so a
    stray or ignored local file never changes a render; anywhere else, a walk of the folder."""
    try:
        inside = subprocess.run(["git", "-C", str(root), "rev-parse", "--is-inside-work-tree"], capture_output=True, text=True)
        if inside.returncode == 0 and inside.stdout.strip() == "true":
            run = subprocess.run(["git", "-C", str(root), "ls-files", "-z"], capture_output=True, check=True)
            return sorted(p for p in run.stdout.decode("utf-8", "replace").split("\0") if p and (root / p).is_file())
    except (OSError, subprocess.CalledProcessError):
        pass
    out = []
    for folder, dirs, files in os.walk(root):
        dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS)
        out += [os.path.relpath(os.path.join(folder, name), root).replace(os.sep, "/") for name in files]
    return sorted(out)


def covers(path: str, target: str) -> bool:
    return target == path or target.startswith(path + "/")


def first_sentence(text: str, limit: int = 180) -> str:
    text = " ".join(text.split())
    cut = re.split(r"(?<=[.!?])\s", text, maxsplit=1)[0]
    return cut if len(cut) <= limit else cut[: limit - 1].rstrip() + "…"


def head(path: Path, limit: int = 6000) -> str:
    try:
        with open(path, encoding="utf-8") as handle:
            return handle.read(limit)
    except (OSError, UnicodeDecodeError):
        return ""


def leading_comment(path: Path) -> str:
    """A file's point: its leading comment or docstring, or a document's first line."""
    lines = head(path).splitlines()
    while lines and (not lines[0].strip() or lines[0].startswith("#!")):
        lines.pop(0)
    if not lines:
        return ""
    first, joined, body = lines[0].lstrip(), "\n".join(lines), []
    if path.suffix in (".md", ".txt", ".rst"):
        body = [first.lstrip("#").replace("**Point:**", "").strip()]
    elif first.startswith(('"""', "'''")):
        body = joined.lstrip()[3:].split(first[:3], 1)[0].splitlines()
    elif first.startswith("/*"):
        body = [re.sub(r"^\s*[*!]+\s?", "", line) for line in joined[joined.index("/*") + 2:].split("*/", 1)[0].splitlines()]
    elif first.startswith("<!--"):
        body = joined[joined.index("<!--") + 4:].split("-->", 1)[0].splitlines()
    else:
        mark = next((m for m in ("///", "//", "--", "#", ";") if first.startswith(m)), None)
        for line in lines if mark else []:
            if not line.lstrip().startswith(mark):
                break
            body.append(line.lstrip()[len(mark):])
    kept: list[str] = []
    for line in body:
        line = re.sub(rf"^@(?:{'|'.join(DOC_TAGS)})\b\s*", "", line.strip())  # the tag is not part of the point
        if not line or set(line) <= set("-=*#/") or line.startswith("@"):  # a directive (@ts-nocheck, @flow, @jest-environment jsdom) is no point
            if kept:
                break
            continue
        kept.append(line)
    return first_sentence(" ".join(kept))


def path_point(root: Path, path: str) -> str:
    full = root / path
    if full.is_dir():
        for name in ("README.md", "README"):
            for line in head(full / name).splitlines():
                if line.strip():
                    return first_sentence(line.strip().lstrip("#").strip()) or "no point stated"
        return next((point for point in (leading_comment(full / name) for name in ENTRY_FILES) if point), "no point stated")
    return leading_comment(full) or "no point stated"


def plural(count: int, word: str) -> str:
    return f"{count} {word}{'' if count == 1 else 's'}"


def bet_line(bet: dict, why: bool = False) -> str:
    line = f"- **{bet['bet'].rstrip('.')}.**"
    if bet.get("instead_of"):
        line += f" Instead of: {bet['instead_of'].rstrip('.')}."
    return line + (f" Why: {bet['why']}" if why and bet.get("why") else "")


class Map:
    """A source that matched the schema, joined with the repository it describes."""

    def __init__(self, model: dict, root: Path, skip: tuple[str, ...] = (), file_counts: bool = True):
        self.m, self.root, self.file_counts = model, root, file_counts
        # the two rendered files are not counted, so a render does not change the next one; with no file counts, no file is listed
        self.files = [f for f in list_files(root) if f not in skip] if file_counts else []
        self.subjects = ([("core", s) for s in model["app"]["core"]] + [("module", s) for s in model["app"]["modules"]]
                         + [("dimension", s) for s in model["dimensions"]])
        self.by_id = {s["id"]: s for _, s in self.subjects}
        self.homes = [(p.rstrip("/"), s["id"]) for _, s in self.subjects for p in s["home"]]
        self.place: dict[str, list[tuple[dict, dict]]] = {}
        for angle in model["framework"]["angles"]:
            for area in angle["areas"]:
                for sid in area["subjects"]:
                    self.place.setdefault(sid, []).append((angle, area))
        self.owner_of_file = {f: self.owner_path(f) for f in self.files}
        releases = model["releases"]
        self.planned = [p.rstrip("/") for item in (releases[0]["items"] if releases else []) if item["status"] != "done" for p in item["paths"]]
        self.errors = self.check()
        self.flags = self.flag()

    # ownership: when paths nest, the longest matching path owns the file
    def owner_path(self, target: str) -> tuple[str, str] | None:
        best = None
        for path, sid in self.homes:
            if covers(path, target) and (best is None or len(path) > len(best[0])):
                best = (path, sid)
        return best

    def owners(self, path: str) -> list[str]:
        """The subjects a path belongs to: the one that owns it, and every subject with a home inside it."""
        path, best = path.rstrip("/"), self.owner_path(path.rstrip("/"))
        return list(dict.fromkeys(([best[1]] if best else []) + [sid for home, sid in self.homes if covers(path, home)]))

    def owned(self, sid: str) -> list[str]:
        return [f for f in self.files if self.owner_of_file[f] and self.owner_of_file[f][1] == sid]

    def cited(self, path: str) -> bool:
        """A cited path is good when it exists, or when an open item of the current release plans it."""
        path = path.rstrip("/")
        return (self.root / path).exists() or any(covers(p, path) or covers(path, p) for p in self.planned)

    # the checks made on every change
    def check(self) -> list[str]:
        errors = []
        angles, releases = self.m["framework"]["angles"], self.m["releases"]
        every_bet = [b for holder in [self.m["product"], *angles, *releases, *(s for _, s in self.subjects)] for b in holder.get("bets") or []]
        for kind, ids in (("subjects", [s["id"] for _, s in self.subjects]), ("angles", [a["id"] for a in angles]),
                          ("key areas", [area["id"] for a in angles for area in a["areas"]]), ("bets", [b["id"] for b in every_bet]),
                          ("loops", [lp["id"] for lp in self.m["loops"]]), ("releases", [r["id"] for r in releases]),
                          ("items", [i["id"] for r in releases for i in r["items"]]), ("questions", [q["id"] for q in self.m["questions"]])):
            errors += [f"two {kind} share the id {i}; an id names one thing" for i in sorted({i for i in ids if ids.count(i) > 1})]
        for _, s in self.subjects:
            count = len(self.place.get(s["id"], []))
            if count != 1:
                errors.append(f"subject {s['id']} is in {count} key areas; it must be in one")
            errors += [f"{s['id']}: home path does not exist and no open item of the current release plans it: {p}" for p in s["home"] if not self.cited(p)]
            errors += [f"{s['id']}: test does not exist (leave `test` out until it does): {g['test']}" for g in s.get("guarantees") or []
                       if g.get("test") and not (self.root / g["test"]).exists()]
        homes: dict[str, str] = {}
        for path, sid in self.homes:
            if homes.setdefault(path, sid) != sid:
                errors.append(f"{path} is a home of both {homes[path]} and {sid}; one subject owns a path")
        errors += [f"a key area names the unknown subject {sid}" for sid in self.place if sid not in self.by_id]
        for loop in self.m["loops"]:
            errors += [f"loop {loop['id']} names the unknown subject {sid}" for sid in loop["nodes"] if sid not in self.by_id]
            errors += [f"loop {loop['id']}: trap file does not exist: {p}" for w in loop.get("watch") or [] for p in w.get("src") or [] if not self.cited(p)]
        for release in self.m["releases"]:  # an item's paths are plans until it is done
            errors += [f"item {item['id']} is done but its path does not exist: {p}" for item in release["items"] if item["status"] == "done"
                       for p in item["paths"] if not (self.root / p.rstrip("/")).exists()]
        for q in self.m["questions"]:
            if q.get("blocks") and q["blocks"] != "product" and q["blocks"] not in self.by_id and q["blocks"] not in [r["id"] for r in self.m["releases"]]:
                errors.append(f"question {q['id']} blocks {q['blocks']}, which is not product, a release id or a subject id")
        return errors

    def flag(self) -> list[str]:
        flags = []
        if not 5 <= len(self.subjects) <= 40:
            flags.append(f"{plural(len(self.subjects), 'subject')}; a map has 5 to 40")
        if not 3 <= len(self.m["product"]["bets"]) <= 7:
            flags.append(f"the product has {plural(len(self.m['product']['bets']), 'bet')}; it has three to seven")
        flags += [f"angle {a['name']} has {plural(len(a['areas']), 'key area')}; an angle has two to five" for a in self.m["framework"]["angles"] if len(a["areas"]) < 2]
        names = {a["name"].strip().lower() for a in self.m["framework"]["angles"]}
        if "qa" not in names:
            flags.append("no angle is named QA; a map keeps one")
        logic = {s["id"] for kind, s in self.subjects if kind != "dimension"}
        for a in self.m["framework"]["angles"]:
            placed = [sid for area in a["areas"] for sid in area["subjects"] if sid in self.by_id]
            if any(sid in logic for sid in placed) and any(sid not in logic for sid in placed):
                flags.append(f"angle {a['name']} holds both core or module subjects and dimensions; Business logic holds the first, the other angles the dimensions")
        if not self.m["product"].get("diagram"):
            flags.append("the product has no diagram")
        size = len(self.front().encode("utf-8"))
        if size > FRONT_LIMIT:
            flags.append(f"the front page is {size} bytes; keep it under about {FRONT_LIMIT}")
        return flags

    # derived for a card
    def traps(self, sid: str | None) -> list[tuple[dict, dict]]:
        """A trap shows on the card that owns a file it cites, or on every subject of its loop when no subject owns one. None: on no card."""
        out = []
        for loop in self.m["loops"]:
            for watch in loop.get("watch") or []:
                cards = list(dict.fromkeys(o for p in watch.get("src") or [] for o in self.owners(p))) or loop["nodes"]
                if (sid is None and not cards) or sid in cards:
                    out.append((loop, watch))
        return out

    def open_items(self, sid: str | None) -> list[dict]:
        """The items not done whose paths a subject owns. None: those no subject owns."""
        out = []
        for release in self.m["releases"]:
            for item in release["items"]:
                cards = {o for p in item["paths"] for o in self.owners(p)}
                if item["status"] != "done" and ((sid is None and not cards) or sid in cards):
                    out.append(item)
        return out

    def shares(self, sid: str) -> list[str]:
        mine = [p.rstrip("/") for p in self.by_id[sid]["home"]]
        return list(dict.fromkeys(other for path, other in self.homes if other != sid and any(covers(p, path) or covers(path, p) for p in mine)))

    def counts(self) -> dict:
        bets = [(s, b) for _, s in self.subjects for b in s.get("bets") or []]
        guarantees = [(s, g) for _, s in self.subjects for g in s.get("guarantees") or []]
        return {"bets": len(bets), "no_reason": [x for x in bets if not x[1].get("why")], "no_instead": [x for x in bets if not x[1].get("instead_of")],
                "guarantees": len(guarantees), "no_test": [x for x in guarantees if not x[1].get("test")],
                "items_no_card": self.open_items(None), "traps_no_card": self.traps(None),
                "unowned": sum(1 for f in self.files if not self.owner_of_file[f])}

    def count_lines(self) -> list[str]:
        c = self.counts()
        return [f"- Bets with no recorded reason: {len(c['no_reason'])} of {c['bets']}.",
                f"- Bets with no \"instead of\": {len(c['no_instead'])} of {c['bets']}.",
                f"- Guarantees citing no test: {len(c['no_test'])} of {c['guarantees']}.",
                f"- Open items on no card: {len(c['items_no_card'])}.",
                f"- Traps on no card: {len(c['traps_no_card'])}."]

    # the front page: five sections
    def front(self) -> str:
        m, product, c = self.m, self.m["product"], self.counts()
        o = [f"# {product['name']}: system map", "",
             "Read down: each section explains the one below it. A subject's card holds the depth, and the code wins over the map.", "",
             "## 1. The point", "", product["point"], ""]
        if m["releases"]:
            release = m["releases"][0]
            o += [f"**Current release, {release['name']}**" + (f" (set by {release['by']})" if release.get("by") else "") + f": {release['point']}", ""]
            o += [bet_line(b) for b in release.get("bets") or []] + ([""] if release.get("bets") else [])
        else:
            o += ["No release is recorded.", ""]
        o += ["## 2. How it runs, and why it is built this way", ""]
        o += [product["frame"], ""] if product.get("frame") else []
        o += ["```", *product["diagram"], "```", ""] if product.get("diagram") else []
        o += ["The product's bets, each beside the option it replaced. Everything below follows from them.", ""]
        o += [bet_line(b) for b in product["bets"]] + [""]
        o += ["## 3. Decision tree", "", "Read by angle, then key area. An angle's bets hold for everything under it. Each subject's point and decisions are on its card.", ""]
        for angle in m["framework"]["angles"]:
            o += [f"**{angle['name']}.** {angle['point']}", ""]
            if angle.get("bets"):
                o += ["Bets:", ""] + [bet_line(b) for b in angle["bets"]] + [""]
            o += ["Key areas:", ""]
            for area in angle["areas"]:
                members = ", ".join(self.by_id[s]["name"] for s in area["subjects"] if s in self.by_id)
                o.append(f"- **{area['name']}:** {area['point']}" + (f" {members}." if members else " No subject yet."))
            o.append("")
        o += ["## 4. Using this map", "",
              "Find the angle, then the key area, then the subject named on its line. Its card is the heading with its name below; "
              "`render_map.py --card <id>` prints one card and `--list` every id. Read this code lists the paths a subject owns; when "
              "paths nest, the longest matching path owns the file. Where a card and the code disagree, the code is right and the map "
              "is fixed in the same change: edit `model.json`, then run `render_map.py`.", ""]
        kinds = {kind: sum(1 for k, _ in self.subjects if k == kind) for kind in ("core", "module", "dimension")}
        o += ["## 5. State of the map", "",
              f"{plural(len(self.subjects), 'subject')} ({kinds['core']} core, {plural(kinds['module'], 'module')}, {plural(kinds['dimension'], 'dimension')})"
              + (f" own {len(self.files) - c['unowned']} of {plural(len(self.files), 'file')}" if self.file_counts else "")
              + ". Counts are over card bets; `gaps.md` lists what they count.", ""]
        o += self.count_lines() + [f"- Checks: {'passed' if not self.errors else plural(len(self.errors), 'failure') + ', listed in `gaps.md`'}.", ""]
        return "\n".join(o)

    # a card: eleven headings in this order; one with nothing to say is left out
    def card(self, sid: str) -> str:
        s = self.by_id[sid]
        placed = self.place.get(sid) or []
        where = " > ".join(x["name"] for x in placed[0]) if placed else "not placed"
        if s.get("register_ids"):
            where += f"; register {', '.join(s['register_ids'])}"
        if s.get("owner"):
            where += f"; owner {s['owner']}"
        tools, bets, guarantees = s.get("tools") or [], s.get("bets") or [], s.get("guarantees") or []
        size = [plural(len(self.owned(sid)), "file")] if self.file_counts else []
        size += [plural(len(x), word) for x, word in ((tools, "tool"), (guarantees, "guarantee"), (bets, "bet")) if x]
        o = [f"## {s['name']}", "", f"**Point:** {s['point']}", "", f"**Where it sits:** {where}.", ""] + (["**Size:** " + ", ".join(size) + ".", ""] if size else [])
        if s.get("parts"):
            o += ["### What it is made of", ""] + [f"- **{p['name']}:** {p['point']}" for p in s["parts"]] + [""]
        if bets:
            o += ["### Why it is this way", ""] + [bet_line(b, why=True) for b in bets] + [""]
        if guarantees:
            o += ["### Must stay true", ""] + [f"- {g['text']} " + (f"Test: `{g['test']}`" if g.get("test") else "**No test cited.**") for g in guarantees] + [""]
        traps = self.traps(sid)
        if traps:
            o += ["### Known traps", ""]
            o += [f"- **{w['when'].rstrip('.')}:** {w['then']}" + (" See " + ", ".join(f"`{p}`" for p in w["src"]) + "." if w.get("src") else "") for _, w in traps] + [""]
        o += ["### Read this code", ""]
        for path in (p.rstrip("/") for p in s["home"]):
            count = f" ({plural(sum(1 for f in self.files if self.owner_of_file[f] == (path, sid)), 'file')})" if self.file_counts else ""
            o.append(f"- `{path}`{count}: {path_point(self.root, path) if (self.root / path).exists() else 'planned, not yet written'}")
        o.append("")
        if tools:
            o += ["### Its tools", ""] + [f"- `{t['name']}`: {t['point']}" for t in tools] + [""]
        loops, shares = [lp for lp in self.m["loops"] if sid in lp["nodes"]], self.shares(sid)
        if loops or shares:
            o += ["### Touches", ""]
            for lp in loops:
                others = ", ".join(self.by_id[x]["name"] for x in lp["nodes"] if x != sid and x in self.by_id)
                o.append(f"- Loop **{lp['name']}**: {lp['point']}" + (f" With: {others}." if others else ""))
            if shares:
                o.append("- Shares code with: " + ", ".join(self.by_id[x]["name"] for x in shares) + ".")
            o.append("")
        items = self.open_items(sid)
        if items:
            o += ["### Open work", ""] + [f"- **{i['id']}** ({i['status']}): {i['text']}" for i in items] + [""]
        elif not self.m["releases"]:
            o += ["### Open work", "", "No tracker or roadmap is recorded.", ""]
        return "\n".join(o)

    def product_map(self) -> str:
        return self.front() + "\n" + "\n".join(self.card(s["id"]) for _, s in self.subjects)

    def gaps(self) -> str:
        c = self.counts()
        o = [f"# {self.m['product']['name']}: gaps", "", "Derived at each render from `model.json`; counts are over card bets.", ""] + self.count_lines() + [""]
        if self.errors:
            o += ["## Failed checks", ""] + [f"- {e}" for e in self.errors] + [""]
        if self.flags:
            o += ["## Flags", ""] + [f"- {f}" for f in self.flags] + [""]
        for title, rows in (("Bets with no recorded reason", [f"{s['name']}: {b['bet']}" for s, b in c["no_reason"]]),
                            ("Bets with no \"instead of\"", [f"{s['name']}: {b['bet']}" for s, b in c["no_instead"]]),
                            ("Guarantees citing no test", [f"{s['name']}: {g['text']}" for s, g in c["no_test"]]),
                            ("Open items on no card", [f"**{i['id']}** ({i['status']}): {i['text']}" for i in c["items_no_card"]]),
                            ("Traps on no card", [f"{lp['name']}: {w['when']}" for lp, w in c["traps_no_card"]])):
            if rows:
                o += [f"## {title}", ""] + [f"- {row}" for row in rows] + [""]
        questions = sorted(self.m["questions"], key=lambda q: not q.get("blocks"))[:MAX_QUESTIONS]
        o += ["## Owner questions", ""] + ([f"{n}. {q['text']}" + (f" (blocks {q['blocks']})" if q.get("blocks") else "") for n, q in enumerate(questions, 1)] or ["None recorded."]) + [""]
        return "\n".join(o)


def main(argv: list[str] | None = None) -> int:
    here = Path(__file__).resolve().parent
    ap = argparse.ArgumentParser(description="Render a product's system map from model.json. Stage new files, then render: file counts and ownership read tracked files.")
    ap.add_argument("--source", type=Path, default=here / "model.json", help="the map source (default: model.json beside this file)")
    ap.add_argument("--schema", type=Path, default=here / "map.schema.json", help="the schema (default: map.schema.json beside this file)")
    ap.add_argument("--root", type=Path, help="the repository root (default: two folders above the source)")
    ap.add_argument("--out", type=Path, help="where product-map.md and gaps.md go (default: beside the source)")
    ap.add_argument("--check", action="store_true", help="write nothing; fail if a check fails or the files on disk differ from a fresh render")
    ap.add_argument("--list", action="store_true", help="print every subject id with its point")
    ap.add_argument("--front", action="store_true", help="print the front page")
    ap.add_argument("--card", metavar="ID", help="print one subject's card")
    ap.add_argument("--no-file-counts", action="store_true", help="leave file counts out, and with them how many of the repository's files the subjects own; where the render is committed, render and check with it, so an added file does not stale it")
    args = ap.parse_args(argv)
    source = args.source.resolve()
    root, out = (args.root or source.parent.parent.parent).resolve(), (args.out or source.parent).resolve()
    try:
        model, schema = json.loads(source.read_text(encoding="utf-8")), json.loads(args.schema.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        print(f"render_map: {exc}", file=sys.stderr)
        return 1
    problems = validate(model, schema, schema)
    if problems:
        print(f"render_map: {source.name} does not match {args.schema.name}; nothing written:", file=sys.stderr)
        print("\n".join(f"  {p}" for p in problems), file=sys.stderr)
        return 1
    built = Map(model, root, tuple(os.path.relpath(folder / name, root).replace(os.sep, "/") for folder in {out, source.parent} for name in OUTPUTS),
                file_counts=not args.no_file_counts)
    if args.list or args.front or args.card:
        if args.card and args.card not in built.by_id:
            print(f"render_map: no subject {args.card}; --list prints the ids", file=sys.stderr)
            return 1
        print("\n".join(f"{s['id']}\t{kind}\t{s['point']}" for kind, s in built.subjects) if args.list else built.front() if args.front else built.card(args.card))
        return 0
    rendered = {"product-map.md": built.product_map(), "gaps.md": built.gaps()}
    stale = []
    for name in OUTPUTS:
        text = rendered[name].rstrip("\n") + "\n"
        if args.check:
            if not (out / name).is_file() or (out / name).read_text(encoding="utf-8") != text:
                stale.append(name)
        else:
            out.mkdir(parents=True, exist_ok=True)
            (out / name).write_text(text, encoding="utf-8")
    print(f"render_map: {plural(len(built.subjects), 'card')}, front page {len(built.front().encode('utf-8'))} bytes" + ("" if args.check else f", written to {out}"))
    for line in built.flags:
        print(f"flag: {line}")
    for line in built.errors:
        print(f"check failed: {line}", file=sys.stderr)
    for name in stale:
        print(f"check failed: {name} is missing or differs from a fresh render; run render_map.py", file=sys.stderr)
    return 1 if built.errors or stale else 0


if __name__ == "__main__":
    sys.exit(main())
