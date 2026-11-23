#!/usr/bin/env python3
"""Render a product's product map from its source, in the one format every product uses.

Put this file and map.schema.json beside the source, model.json, in the map folder (the folder `model` under the repository's
`docs` folder), then run it from anywhere:

    python3 render_map.py            # check the source, then write product-map.md and gaps.md beside it
    python3 render_map.py --check    # the same checks, and fail if the two files on disk differ from a fresh render in the same form
    python3 render_map.py --list     # every subject id with its point
    python3 render_map.py --front    # print the front page
    python3 render_map.py --card ID  # print one subject's card
    python3 render_map.py --packet   # check the source, then write product-map.json: the source with what only the repository can derive

product-map.md is the front page (five sections; the current release's bets stand under its goal, then later releases and the paper plan), the
optional sections the source holds (code map, pipelines, agent surface, terms, and any x_ section with a title and rows, drawn the same way for every
product), then one card per subject (three opening lines, Point, Where it sits and Size, then up to nine headings, in a fixed order; one with nothing
to say is left out). gaps.md holds the same counts as
the front page's last section, what they count, and at most seven owner questions, with how many more the source holds. Nothing is written when the source does not match the schema. The
exit code is 1 when the schema, a check or --check fails. A flag (a count outside the usual range, or a placing worth a look) is printed and does not fail.
The tool writes these two files only: a project that wants sections of its own renders them into a file of its own, so --check still passes. It writes no
line saying where the map is edited: `cady product map publish` adds that to the published File.

The packet (--packet) is product-map.json: {schema, source, derived, rendered}. `source` is the map as written; `derived` is what a page cannot
compute without the repository (each path's point and owners, each card's size, Touches, traps and open work, the code map, the gaps, flags, failed
checks and level checks); `rendered` names the commit, the time and the writer (--writer, the URL where the map is edited). It holds no live task
fact: an item with `work` names its task, and a page reads the task's status, headline and Done when itself.

Counted as gaps: a card bet with no reason or no alternative. A missing product line, a kind of research (users, competition, technology) with no pointer, and a subject's level
that is proposed and not yet signed by the owner, are gaps too. A subject over its level's budget is flagged, not failed; a render without
file counts prints that flag and does not write it, so a size never makes the committed render stale. An item with `work` is a task: its
status is in Cady, so the tool counts its paths as planned and draws it as "status in Cady". An owner's bet is the owner's sentence word for word, so one without them is counted on a
line of its own: only the owner can fill it. One subject owns a path; a dimension's `governs` paths are owned by another subject, and their open work and
traps show on both cards. A part's `schema` names the file that defines its shape, or the folder of migrations that does. While it is not written, an
open item of the current release must name that path itself and come before the other open items of its subject. The order of items across subjects is
not checked. A file that needs two owners is not placed twice: an open item of the current release lists it under `splits`, with the path its moved
part goes to. The subject whose part stays owns the file, another subject owns the new path, and the file shows on both cards and is counted on a line of its own.

Derived at each render and never stored: file counts, each path's point, Touches, open work and every count. Not derived: a
subject's tools (the source lists them) and the diagram (the source holds it as text). A folder's point is the first line of its
README, or else the leading comment of its entry file (index.ts, __init__.py and the like); a file's is its leading comment.

File counts and ownership read tracked files, so stage new files, then render. File counts change whenever a file is added
anywhere. Where the render is committed, render with --no-file-counts: the front page and the cards then say nothing about how
many files there are, nor how many of them the subjects own, so an added file does not make them stale. gaps.md says the render
was made that way and how many files no subject owned at that render; --check reads that, checks in the same form with or without
the option, and compares that line with its number left out. The front page names the option in its "Using this map" section.

Standard library only. Options: --source, --schema, --root (the repository root), --out (where the files go), --no-file-counts,
and for --packet: --writer, --sha and --at (both read from git and the clock when left out).
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
UNOWNED_LINE = "- Files no subject owns: "  # in gaps.md of a render without file counts: counted at that render; --check compares the line with its number left out
NO_COUNTS_MARK = "Rendered with `--no-file-counts`"  # how --check knows the form the render on disk was made in
PACKET, PACKET_SCHEMA = "product-map.json", "cady.product-map-packet.v1"
RESEARCH = ("users", "competition", "technology", "assets")  # the paper plan's kinds of research, in the order the front page lists them
REQUIRED_RESEARCH = ("users", "competition", "technology")  # a missing one is a gap; assets is optional
CODE_DEPTH = 2  # folder levels a code map lists below each root when the source does not say


def is_open(item: dict) -> bool:
    """An item not done. An item with `work` is open here: its task holds the status, and the page reads it there."""
    return item.get("status") != "done"


def item_label(item: dict) -> str:
    return f"**{item['id']}** ({item['status']}): {item['text']}" if not item.get("work") else f"**{item['id']}** (task {item['work']}, status in Cady)"


def item_rules(model: dict) -> list[str]:
    """The item rules JSON Schema here cannot state: with `work`, the task holds the text and status; without it, the item states both."""
    errors, seen = [], {}
    for release in model.get("releases") or []:
        for item in release.get("items") or []:
            at = f"model.releases[{release.get('id')}].items[{item.get('id')}]"
            if item.get("work"):
                errors += [f"{at}: has `work`, so its {key} comes from the task; leave out {json.dumps(key)}" for key in ("text", "status") if key in item]
                if seen.setdefault(item["work"], item.get("id")) != item.get("id"):
                    errors.append(f"{at}: names the task {item['work']}, as item {seen[item['work']]} does; an item is one task")
            else:
                errors += [f"{at}: missing key {json.dumps(key)} (or name its task in `work`)" for key in ("text", "status") if key not in item]
    return errors


def sections_of(model: dict) -> list[tuple[str, dict | list]]:
    """The optional sections the source holds, in the order they are drawn: the standard four, then each x_ section with a title and rows."""
    out = [(key, model[key]) for key in ("code_map", "pipelines", "agent_surface", "terms") if model.get(key) or (key == "agent_surface" and key in model)]
    return out + [(key, value) for key, value in model.items() if key.startswith("x_") and isinstance(value, dict)
                  and isinstance(value.get("title"), str) and value["title"].strip() and isinstance(value.get("rows"), list)]


def row_text(row: object) -> str:
    """One row of an x_ section: text as written, or an object's text values joined."""
    if isinstance(row, dict):
        return "; ".join(f"{k}: {v}" for k, v in row.items() if isinstance(v, (str, int, float)) and not isinstance(v, bool))
    return str(row)


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
    if kind == "integer":
        if not isinstance(value, int) or isinstance(value, bool):
            return [f"{at}: must be a whole number"]
        return [f"{at}: must be at least {schema['minimum']}"] if value < schema.get("minimum", value) else []
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
        self.m, self.root, self.file_counts, self.skip = model, root, file_counts, skip
        # the two rendered files are not counted, so a render does not change the next one; with no file counts, no file is listed
        self.files = [f for f in list_files(root) if f not in skip] if file_counts else []
        self.subjects = ([("core", s) for s in model["app"]["core"]] + [("module", s) for s in model["app"]["modules"]]
                         + [("dimension", s) for s in model["dimensions"]])
        self.by_id = {s["id"]: s for _, s in self.subjects}
        self.homes = [(p.rstrip("/"), s["id"]) for _, s in self.subjects for p in s["home"]]
        self.governs = [(p.rstrip("/"), s["id"]) for _, s in self.subjects for p in s.get("governs") or []]
        self.place: dict[str, list[tuple[dict, dict]]] = {}
        for angle in model["framework"]["angles"]:
            for area in angle["areas"]:
                for sid in area["subjects"]:
                    self.place.setdefault(sid, []).append((angle, area))
        self.owner_of_file = {f: self.owner_path(f) for f in self.files}
        releases = model["releases"]
        self.planned = [p.rstrip("/") for item in (releases[0]["items"] if releases else []) if is_open(item) for p in item["paths"]]
        # a file that needs two owners, by the open item that splits it: one row per file, the first item that lists it
        self.split: list[tuple[str, str, dict]] = []
        for item in (i for release in releases for i in release["items"] if is_open(i)):
            for row in item.get("splits") or []:
                if row["file"].rstrip("/") not in [path for path, _, _ in self.split]:
                    self.split.append((row["file"].rstrip("/"), row["to"].rstrip("/"), item))
        self._tracked: list[str] | None = None
        self._sizes: dict[str, tuple[int, int]] = {}
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
        """The subjects a path belongs to: the one that owns it, every subject with a home inside it, and each dimension that governs it."""
        path, best = path.rstrip("/"), self.owner_path(path.rstrip("/"))
        return list(dict.fromkeys(([best[1]] if best else []) + [sid for home, sid in self.homes if covers(path, home)]
                                  + [sid for gov, sid in self.governs if covers(gov, path) or covers(path, gov)]))

    def governed_by(self, sid: str) -> list[str]:
        """The dimensions that set the rules for code this subject owns."""
        mine = [p.rstrip("/") for p in self.by_id[sid]["home"]]  # its home is the governed path or inside it, or it owns the governed path by the longest match
        return list(dict.fromkeys(other for gov, other in self.governs if other != sid
                                  and (any(covers(gov, p) for p in mine) or (self.owner_path(gov) or ("", ""))[1] == sid)))

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
                          ("items", [i["id"] for r in releases for i in r["items"]]), ("questions", [q["id"] for q in self.m["questions"]]),
                          ("pipelines", [pl["id"] for pl in self.m.get("pipelines") or []])):
            errors += [f"two {kind} share the id {i}; an id names one thing" for i in sorted({i for i in ids if ids.count(i) > 1})]
        for _, s in self.subjects:
            count = len(self.place.get(s["id"], []))
            if count != 1:
                errors.append(f"subject {s['id']} is in {count} key areas; it must be in one")
            errors += [f"{s['id']}: home path does not exist and no open item of the current release plans it: {p}" for p in s["home"] if not self.cited(p)]
            errors += [f"{s['id']}: test does not exist (leave `test` out until it does): {g['test']}" for g in s.get("guarantees") or []
                       if g.get("test") and not (self.root / g["test"]).exists()]
            errors += [f"{s['id']}: governed path does not exist and no open item of the current release plans it: {p}" for p in s.get("governs") or [] if not self.cited(p)]
            errors += [f"{s['id']}: {p} is in its own home and a path it governs; a governed path is owned by another subject" for p in s.get("governs") or []
                       if any(covers(h.rstrip("/"), p.rstrip("/")) for h in s["home"])]
            if not s["home"] and not s.get("governs"):
                errors.append(f"subject {s['id']} has no home and governs nothing; it needs a path")
            errors += self.schema_first(s)
        homes: dict[str, str] = {}
        for path, sid in self.homes:
            if homes.setdefault(path, sid) != sid:
                errors.append(f"{path} is a home of both {homes[path]} and {sid}; one subject owns a path")
        errors += [f"a key area names the unknown subject {sid}" for sid in self.place if sid not in self.by_id]
        for loop in self.m["loops"]:
            errors += [f"loop {loop['id']} names the unknown subject {sid}" for sid in loop["nodes"] if sid not in self.by_id]
            errors += [f"loop {loop['id']}: trap file does not exist: {p}" for w in loop.get("watch") or [] for p in w.get("src") or [] if not self.cited(p)]
        for release in self.m["releases"]:  # an item's paths are plans until it is done
            errors += [f"item {item['id']} is done but its path does not exist: {p}" for item in release["items"] if item.get("status") == "done"
                       for p in item["paths"] if not (self.root / p.rstrip("/")).exists()]
        errors += self.split_checks()
        errors += self.section_checks()
        for q in self.m["questions"]:
            if q.get("blocks") and q["blocks"] != "product" and q["blocks"] not in self.by_id and q["blocks"] not in [r["id"] for r in self.m["releases"]]:
                errors.append(f"question {q['id']} blocks {q['blocks']}, which is not product, a release id or a subject id")
        return errors

    def schema_first(self, s: dict) -> list[str]:
        """A part's schema path is the file that defines its shape, or a folder of migrations. While it is not written, an open item of the
        current release names that path itself, and that item comes before the other open items of this subject: the shape is settled before
        the code that builds on it. One message per path, however many parts share it. The order across subjects is not checked."""
        errors, sid = [], s["id"]
        items = [i for i in (self.m["releases"][0]["items"] if self.m["releases"] else []) if is_open(i)]
        for path in dict.fromkeys((part.get("schema") or "").rstrip("/") for part in s.get("parts") or []):
            if not path:
                continue
            if (self.root / path).exists():
                continue
            writes = [n for n, i in enumerate(items) if path in [p.rstrip("/") for p in i["paths"]]]
            if not writes:
                errors.append(f"{sid}: the schema file {path} does not exist and no open item of the current release names it; an item that writes it names that path")
                continue
            early = [i["id"] for i in items[:writes[0]] if sid in {o for p in i["paths"] for o in self.owners(p)}]
            if early:
                errors.append(f"{sid}: item {', '.join(early)} comes before {items[writes[0]]['id']}, which writes the schema file {path}; the schema item comes first")
        return errors

    def section_checks(self) -> list[str]:
        """The paths and subjects the optional sections and the research name exist, and a term is defined once."""
        errors = []
        research = self.m["product"].get("research") or {}
        errors += [f"research ({kind}): path does not exist: {ref}" for kind in RESEARCH for ref in research.get(kind) or []
                   if not ref.startswith("file:") and not (self.root / ref).exists()]
        errors += [f"code map: root does not exist: {p}" for p in (self.m.get("code_map") or {}).get("roots") or [] if not (self.root / p).is_dir()]
        errors += [f"pipeline {pl['id']} is owned by the unknown subject {pl['owner']}" for pl in self.m.get("pipelines") or []
                   if pl.get("owner") and pl["owner"] not in self.by_id]
        surface = self.m.get("agent_surface") or {}
        errors += [f"agent surface: method {row['name']} is owned by the unknown subject {row['owner']}" for row in surface.get("methods") or [] if row["owner"] not in self.by_id]
        words = [t["term"].strip().lower() for t in self.m.get("terms") or []]
        errors += [f"the term {w!r} is defined twice; a word is defined once" for w in sorted({w for w in words if words.count(w) > 1})]
        return errors

    def item_cards(self, item: dict) -> list[str]:
        """The subjects an item shows on: each that owns or governs one of its paths."""
        return list(dict.fromkeys(o for p in item["paths"] for o in self.owners(p)))

    def split_checks(self) -> list[str]:
        """A row of an item's `splits` names a file that needs two owners and the path its moved part goes to. The item is open and in
        the current release and names both in `paths`; the file exists and one subject owns it; a second subject owns the new path by its
        `home`, so a dimension that only governs the file is not the second owner. Checked for each file, not for the item."""
        errors = []
        for number, release in enumerate(self.m["releases"]):
            for item in release["items"]:
                paths, listed = [p.rstrip("/") for p in item["paths"]], [row["file"].rstrip("/") for row in item.get("splits") or []]
                for path, to in dict.fromkeys((row["file"].rstrip("/"), row["to"].rstrip("/")) for row in item.get("splits") or []):
                    owner, second, mark = self.owner_path(path), self.owner_path(to), f"item {item['id']} lists {path} under `splits`"
                    if item.get("status") == "done":
                        errors.append(f"{mark} and is done; a split that has landed leaves the list")
                        continue
                    if number:
                        errors.append(f"{mark} and is not in the current release; the item that splits a file is an open item of the current release")
                    errors += [f"{mark} and does not name {missing} in `paths`" for missing in (path, to) if missing not in paths]
                    if not (self.root / path).is_file():
                        errors.append(f"{mark}, which is not a file in the repository")
                    elif not owner:
                        errors.append(f"{mark}, which no subject owns; the subject whose part stays owns it")
                    elif to in listed or not second or second[1] == owner[1]:
                        errors.append(f"{mark} and moves its part to {to}, which " + ("is itself a file to split" if to in listed else "no subject owns" if not second
                                      else f"{owner[1]} owns too") + "; a second subject names the new path as a `home`")
        return errors

    def split_rows(self, sid: str | None = None) -> list[str]:
        """One line per file that needs two owners: who owns it, the item, and where the moved part goes. With a subject, only the two it concerns."""
        rows = []
        for path, to, item in self.split:
            owner, second = self.owner_path(path), self.owner_path(to)
            name = lambda found: self.by_id[found[1]]["name"] if found else "no subject"
            if sid is None or sid in [found[1] for found in (owner, second) if found]:
                rows.append(f"`{path}` needs two owners: {name(owner)} owns it; **{item['id']}** moves part of it to `{to}` ({name(second)}).")
        return rows

    def flag(self) -> list[str]:
        flags = []
        if not 5 <= len(self.subjects) <= 40:
            flags.append(f"{plural(len(self.subjects), 'subject')}; 5 to 40 is usual")
        if not 3 <= len(self.m["product"]["bets"]) <= 7:
            flags.append(f"the product has {plural(len(self.m['product']['bets']), 'bet')}; three to seven is usual")
        flags += [f"angle {a['name']} has {plural(len(a['areas']), 'key area')}; two to five is usual" for a in self.m["framework"]["angles"] if len(a["areas"]) < 2]
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
        flags += [f"{sid} governs {path}, which no subject owns; list it as a `home` of the subject that owns it" for path, sid in self.governs
                  if not self.owner_path(path) and not any(covers(path, home) for home, _ in self.homes)]
        flags += self.budget_flags() if self.file_counts else []  # without file counts a size never changes the committed render
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
                cards = self.item_cards(item)
                if is_open(item) and ((sid is None and not cards) or sid in cards):
                    out.append(item)
        return out

    def shares(self, sid: str) -> list[str]:
        mine = [p.rstrip("/") for p in self.by_id[sid]["home"]]
        return list(dict.fromkeys(other for path, other in self.homes if other != sid and any(covers(p, path) or covers(path, p) for p in mine)))

    def tracked(self) -> list[str]:
        """Every tracked file, read once whether or not this render shows file counts: sizes and the code map need them."""
        if self._tracked is None:
            self._tracked = self.files if self.file_counts else [f for f in list_files(self.root) if f not in self.skip]
        return self._tracked

    def size(self, sid: str) -> tuple[int, int]:
        """The files and lines a subject owns (by the longest matching home), counted now. A file with a NUL byte counts no lines."""
        if not self._sizes:
            for f in self.tracked():
                owner = self.owner_path(f)
                if not owner:
                    continue
                try:
                    data = (self.root / f).read_bytes()
                except OSError:
                    continue
                files, lines = self._sizes.get(owner[1], (0, 0))
                self._sizes[owner[1]] = (files + 1, lines + (0 if b"\0" in data[:4096] else data.count(b"\n") + (1 if data and not data.endswith(b"\n") else 0)))
            self._sizes.setdefault("", (0, 0))
        return self._sizes.get(sid, (0, 0))

    def budget_flags(self) -> list[str]:
        """A line per subject over its level's budget. In a render without file counts they are printed, not written."""
        out = []
        for sid, row in self.level_checks().items():
            if row["over"]:
                budget = self.by_id[sid]["level"].get("budget") or {}
                said = f"{plural(row['files'], 'file')}, {plural(row['lines'], 'line')}; " if self.file_counts else ""
                out.append(f"{self.by_id[sid]['name']} is over its level's budget ({said}budget "
                           + ", ".join(plural(budget[k], k[:-1]) for k in ("files", "lines") if k in budget) + "); growing it further is a task to rank first")
        return out

    def level_checks(self) -> dict[str, dict]:
        """Each subject with a level: its size now and whether it is over its budget (the budget itself is in the source)."""
        out = {}
        for _, s in self.subjects:
            level = s.get("level")
            if not level:
                continue
            files, lines = self.size(s["id"])
            budget = level.get("budget") or {}
            over = any(now > budget[k] for k, now in (("files", files), ("lines", lines)) if k in budget)
            out[s["id"]] = {"files": files, "lines": lines, "over": over}
        return out

    def research_missing(self) -> list[str]:
        research = self.m["product"].get("research") or {}
        return [kind for kind in REQUIRED_RESEARCH if not research.get(kind)]

    def counts(self) -> dict:
        bets = [(s, b) for _, s in self.subjects for b in s.get("bets") or []]
        guarantees = [(s, g) for _, s in self.subjects for g in s.get("guarantees") or []]
        mine = [x for x in bets if x[1]["origin"] != "owner"]  # an owner's bet is their sentence as written: only they can add a reason or an alternative
        return {"bets": len(bets), "no_reason": [x for x in mine if not x[1].get("why")], "no_instead": [x for x in mine if not x[1].get("instead_of")],
                "owner_bare": [x for x in bets if x[1]["origin"] == "owner" and not (x[1].get("why") and x[1].get("instead_of"))],
                "guarantees": len(guarantees), "no_test": [x for x in guarantees if not x[1].get("test")],
                "items_no_card": self.open_items(None), "traps_no_card": self.traps(None), "split": self.split_rows(),
                "unowned": sum(1 for f in self.files if not self.owner_of_file[f]),
                "research_missing": self.research_missing(),
                "levels_proposed": [s for _, s in self.subjects if (s.get("level") or {}).get("origin") == "proposed"],
                "line_missing": [] if self.m["product"].get("line") else ["the product line"]}

    def unowned_now(self) -> int:
        """How many files no subject owns, read from the repository now, whether or not this render shows file counts."""
        return sum(1 for f in (self.files if self.file_counts else list_files(self.root)) if f not in self.skip and not self.owner_path(f))

    def count_lines(self) -> list[str]:
        c = self.counts()
        return [f"- Bets with no recorded reason: {len(c['no_reason'])} of {c['bets']}.",
                f"- Bets with no \"instead of\": {len(c['no_instead'])} of {c['bets']}.",
                f"- Owner bets as written, with no reason or no \"instead of\": {len(c['owner_bare'])}.",
                f"- Guarantees citing no test: {len(c['no_test'])} of {c['guarantees']}.",
                f"- Open items on no card: {len(c['items_no_card'])}.",
                f"- Traps on no card: {len(c['traps_no_card'])}.",
                f"- Files that need two owners, each with an item that splits it: {len(c['split'])}.",
                f"- Product line missing: {len(c['line_missing'])}.",
                f"- Kinds of research with no pointer (users, competition, technology): {len(c['research_missing'])} of {len(REQUIRED_RESEARCH)}.",
                f"- Levels proposed and not yet signed by the owner: {len(c['levels_proposed'])}."]

    # the front page: five sections
    def front(self) -> str:
        m, product, c = self.m, self.m["product"], self.counts()
        line = product.get("line")
        o = [f"# {product['name']}: product map", ""] + ([f"**{line['text']}**" + (" (proposed)" if line["origin"] == "proposed" else ""), ""] if line else []) + [
             "Read down: each section explains the one below it. A subject's card holds the depth, and the code wins over the map.", "",
             "## 1. The point", ""] + ([] if line and line["text"].strip() == product["point"].strip() else [product["point"], ""])  # a line that is the point shows once
        if m["releases"]:
            release = m["releases"][0]
            o += [f"**Current release, {release['name']}**" + (f" (set by {release['by']})" if release.get("by") else "") + f": {release['point']}", ""]
            o += [bet_line(b) for b in release.get("bets") or []] + ([""] if release.get("bets") else [])
        else:
            o += ["No release is recorded.", ""]
        if len(m["releases"]) > 1:
            o += ["### Later releases", ""]
            o += [f"- **{r['name']}:** {r['point']} (" + ", ".join(x for x in (
                      plural(sum(1 for i in r["items"] if not i.get("work") and is_open(i)), "open item"),
                      plural(sum(1 for i in r["items"] if i.get("work")), "task") if any(i.get("work") for i in r["items"]) else "") if x) + ")" for r in m["releases"][1:]] + [""]
        research = product.get("research") or {}
        o += ["### Paper plan", "", "The research the plan stands on, by kind; it comes before the build. A users, competition or technology kind with no pointer is a gap.", ""]
        o += [f"- **{kind.title()}:** " + (", ".join(f"`{ref}`" for ref in research[kind]) if research.get(kind) else "missing." if kind in REQUIRED_RESEARCH else "none (optional).")
              for kind in RESEARCH] + [""]
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
              f"is fixed in the same change: edit `model.json`, then run `render_map.py{'' if self.file_counts else ' --no-file-counts'}`.", ""]
        kinds = {kind: sum(1 for k, _ in self.subjects if k == kind) for kind in ("core", "module", "dimension")}
        o += ["## 5. State of the map", "",
              f"{plural(len(self.subjects), 'subject')} ({kinds['core']} core, {plural(kinds['module'], 'module')}, {plural(kinds['dimension'], 'dimension')})"
              + (f" own {len(self.files) - c['unowned']} of {plural(len(self.files), 'file')}" if self.file_counts else "")
              + ". Counts are over card bets; `gaps.md` lists what they count.", ""]
        o += self.count_lines() + [f"- Checks: {'passed' if not self.errors else plural(len(self.errors), 'failure') + ', listed in `gaps.md`'}.", ""]
        return "\n".join(o)

    # a card: three opening lines, then up to nine headings in this order; one with nothing to say is left out
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
        if s.get("level"):
            level = s["level"]
            o += ["### Level", "", f"**Simplest form:** {level['simplest']}", ""]
            o += ["**Not now:** " + "; ".join(x.rstrip(".") for x in level["not_now"]) + ".", ""] if level["not_now"] else []
            if level.get("budget"):
                o += ["**Budget:** at most " + ", ".join(plural(level["budget"][k], k[:-1]) for k in ("files", "lines") if k in level["budget"]) + ".", ""]
            o += [("Set by the owner" + (f" ({level['source']})" if level.get("source") else "") if level["origin"] == "owner"
                   else "Proposed; the owner has not signed it") + ". Anything under Not now first needs an owner bet on this subject.", ""]
        if s.get("parts"):
            o += ["### What it is made of", ""] + [f"- **{p['name']}:** {p['point']}" + (f" Schema: `{p['schema']}`" if p.get("schema") else "") for p in s["parts"]] + [""]
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
        for path in (p.rstrip("/") for p in s.get("governs") or []):
            owner = self.owner_path(path)
            o.append(f"- `{path}` (governed" + (f", owned by {self.by_id[owner[1]]['name']}" if owner else "") + f"): {path_point(self.root, path) if (self.root / path).exists() else 'planned, not yet written'}")
        o += [f"- {row}" for row in self.split_rows(sid)]
        o.append("")
        if tools:
            o += ["### Its tools", ""] + [f"- `{t['name']}`: {t['point']}" for t in tools] + [""]
        loops, shares, rules = [lp for lp in self.m["loops"] if sid in lp["nodes"]], self.shares(sid), self.governed_by(sid)
        pipes = [pl for pl in self.m.get("pipelines") or [] if pl.get("owner") == sid]
        methods = [r for r in (self.m.get("agent_surface") or {}).get("methods") or [] if r["owner"] == sid]
        if loops or shares or rules or pipes or methods:
            o += ["### Touches", ""]
            for lp in loops:
                others = ", ".join(self.by_id[x]["name"] for x in lp["nodes"] if x != sid and x in self.by_id)
                o.append(f"- Loop **{lp['name']}**: {lp['point']}" + (f" With: {others}." if others else ""))
            if shares:
                o.append("- Shares code with: " + ", ".join(self.by_id[x]["name"] for x in shares) + ".")
            if rules:
                o.append("- Rules set by: " + ", ".join(self.by_id[x]["name"] for x in rules) + ".")
            if pipes:
                o.append("- Pipelines: " + ", ".join(pl["name"] for pl in pipes) + ".")
            if methods:
                o.append("- Agent surface: " + plural(len(methods), "method") + ".")
            o.append("")
        items = self.open_items(sid)
        if items:
            o += ["### Open work", ""] + [f"- {item_label(i)}" for i in items] + [""]
        elif not self.m["releases"]:
            o += ["### Open work", "", "No tracker or roadmap is recorded.", ""]
        return "\n".join(o)

    def code_map(self) -> list[dict]:
        """Every folder under the code map's roots, to its depth: path, depth below its root, point and owning subject."""
        spec = self.m.get("code_map") or {}
        depth, rows = spec.get("depth") or CODE_DEPTH, []
        for root in (r.rstrip("/") for r in spec.get("roots") or []):
            found = {root: 0}
            for f in self.tracked():
                if covers(root, f) and f != root:
                    parts = f[len(root) + 1:].split("/")[:-1]
                    for n in range(1, min(depth, len(parts)) + 1):
                        found.setdefault(root + "/" + "/".join(parts[:n]), n)
            for path in sorted(found):
                owner = self.owner_path(path)
                rows.append({"path": path, "depth": found[path], "point": path_point(self.root, path), "owner": owner[1] if owner else None})
        return rows

    def sections(self) -> str:
        """The optional sections, each drawn only when the source holds it, the same way for every product."""
        o: list[str] = []
        name = lambda sid: self.by_id[sid]["name"] if sid in self.by_id else sid
        for key, value in sections_of(self.m):
            if key == "code_map":
                o += ["## Code map", "", "Every folder under the roots, with its point and the subject that owns it.", ""]
                o += [f"{'  ' * row['depth']}- `{row['path']}`" + (f" ({name(row['owner'])})" if row["owner"] else "") + f": {row['point']}" for row in self.code_map()] + [""]
            elif key == "pipelines":
                o += ["## Pipelines", "", "The stages from a change to a release, each check with how it runs and what a red blocks.", ""]
                for pl in value:
                    o += [f"### {pl['name']}", ""] + ([" ".join(x for x in (pl.get("point", ""), f"Owned by {name(pl['owner'])}." if pl.get("owner") else "") if x), ""]
                                                     if pl.get("point") or pl.get("owner") else [])
                    for stage in pl["stages"]:
                        o += [f"**{stage['name']}**", ""] + [f"- {c['name']}" + (f": `{c['command']}`" if c.get("command") else "") + f". Gate: {c['gate']}."
                                                             + (f" {c['point']}" if c.get("point") else "") for c in stage["checks"]] + [""]
            elif key == "agent_surface":
                o += ["## Agent surface", "", "What the product ships to agents, each owned by a subject.", ""]
                holders = [(s["name"], s["tools"]) for _, s in self.subjects if s.get("tools")]
                if holders:  # a tool is written once, on its subject: listed here by name, with its point on that card
                    o += ["### Tools", "", "Each subject's tools, by name; the subject's card says what each does.", ""]
                    o += [f"- **{holder}:** " + ", ".join(f"`{t['name']}`" for t in tools) for holder, tools in holders] + [""]
                if value.get("methods"):
                    o += ["### Methods", ""] + [f"- `{r['name']}` ({name(r['owner'])}): {r['point']}" for r in value["methods"]] + [""]
            elif key == "terms":
                o += ["## Terms", ""] + [f"- **{t['term']}:** {t['definition']}" for t in value] + [""]
            else:
                o += [f"## {value['title'].strip()}", ""] + ([value["point"], ""] if isinstance(value.get("point"), str) and value["point"] else [])
                o += [f"- {row_text(row)}" for row in value["rows"]] + [""]
        return "\n".join(o)

    def product_map(self) -> str:
        extra = self.sections()
        return self.front() + "\n" + (extra + "\n" if extra else "") + "\n".join(self.card(s["id"]) for _, s in self.subjects)

    def gap_rows(self) -> list[dict]:
        """The gaps as rows a page can draw: each kind with its count and the lines it counts."""
        c = self.counts()
        return [{"id": gid, "label": label, "count": len(rows), "rows": rows} for gid, label, rows in (
            ("no_reason", "Bets with no recorded reason", [f"{s['name']}: {b['bet']}" for s, b in c["no_reason"]]),
            ("no_instead", "Bets with no \"instead of\"", [f"{s['name']}: {b['bet']}" for s, b in c["no_instead"]]),
            ("owner_bare", "Owner bets as written, with no reason or no \"instead of\"", [f"{s['name']}: {b['bet']}" for s, b in c["owner_bare"]]),
            ("no_test", "Guarantees citing no test", [f"{s['name']}: {g['text']}" for s, g in c["no_test"]]),
            ("items_no_card", "Open items on no card", [item_label(i) for i in c["items_no_card"]]),
            ("traps_no_card", "Traps on no card", [f"{lp['name']}: {w['when']}" for lp, w in c["traps_no_card"]]),
            ("split", "Files that need two owners", c["split"]),
            ("line_missing", "Product line missing", c["line_missing"]),
            ("research_missing", "Kinds of research with no pointer", c["research_missing"]),
            ("levels_proposed", "Levels proposed and not yet signed by the owner", [s["name"] for s in c["levels_proposed"]]))]

    def packet(self, sha: str | None, at: str, writer: str | None) -> dict:
        """product-map.json: the source as written, what only the repository can derive, and who rendered it. No live task fact."""
        research = [ref for refs in (self.m["product"].get("research") or {}).values() for ref in refs if not ref.startswith("file:")]
        items = [i for r in self.m["releases"] for i in r["items"]]
        cited = [p.rstrip("/") for _, s in self.subjects for p in s["home"] + (s.get("governs") or [])]
        cited += [p.rstrip("/") for i in items for p in i["paths"]] + [p for lp in self.m["loops"] for w in lp.get("watch") or [] for p in w.get("src") or []]
        cited += research + [row["file"] for i in items for row in i.get("splits") or []]
        code = self.code_map()
        cited = list(dict.fromkeys(cited + [row["path"] for row in code]))
        cards = {}
        for kind, s in self.subjects:
            sid, placed = s["id"], self.place.get(s["id"]) or []
            files, lines = self.size(sid)
            cards[sid] = {"kind": kind, "where": [placed[0][0]["id"], placed[0][1]["id"]] if placed else None, "size": {"files": files, "lines": lines},
                          "touches": {"loops": [lp["id"] for lp in self.m["loops"] if sid in lp["nodes"]], "shares": self.shares(sid), "rules": self.governed_by(sid)},
                          "traps": [{"loop": lp["id"], "watch": lp["watch"].index(w)} for lp, w in self.traps(sid)],
                          "open_items": [i["id"] for i in self.open_items(sid)], "splits": self.split_rows(sid)}
        return {"schema": PACKET_SCHEMA, "source": self.m,
                "derived": {"points": {p: (path_point(self.root, p) if (self.root / p).exists() else None) for p in cited},
                            "owners": {p: self.owners(p) for p in cited}, "cards": cards,
                            "items": {i["id"]: {"cards": self.item_cards(i)} for i in items},
                            "code_map": code, "gaps": self.gap_rows(), "flags": self.flags, "errors": self.errors,
                            "levels": self.level_checks()},
                "rendered": {"sha": sha, "at": at, "writer": writer}}

    def gaps(self, unowned_note: bool = False) -> str:
        """The gaps list. With `unowned_note`, a render without file counts still says how many files no subject owned when it was made."""
        c = self.counts()
        o = [f"# {self.m['product']['name']}: gaps", "", "Derived at each render from `model.json`; counts are over card bets.", ""] + self.count_lines()
        if unowned_note and not self.file_counts:
            o.append(f"{UNOWNED_LINE}{self.unowned_now()}. {NO_COUNTS_MARK}, so the number is counted when the render is made and `--check` does not compare it.")
        o.append("")
        if self.errors:
            o += ["## Failed checks", ""] + [f"- {e}" for e in self.errors] + [""]
        if self.flags:
            o += ["## Flags", ""] + [f"- {f}" for f in self.flags] + [""]
        for title, rows in ((g["label"], g["rows"]) for g in self.gap_rows()):
            if rows:
                o += [f"## {title}", ""] + [f"- {row}" for row in rows] + [""]
        questions, more = sorted(self.m["questions"], key=lambda q: not q.get("blocks"))[:MAX_QUESTIONS], len(self.m["questions"]) - MAX_QUESTIONS
        o += ["## Owner questions", ""] + ([f"{n}. {q['text']}" + (f" (blocks {q['blocks']})" if q.get("blocks") else "") for n, q in enumerate(questions, 1)] or ["None recorded."]) + [""]
        o += [f"{more} more in `model.json`.", ""] if more > 0 else []
        return "\n".join(o)


def head_sha(root: Path) -> str | None:
    try:
        run = subprocess.run(["git", "-C", str(root), "rev-parse", "HEAD"], capture_output=True, text=True)
    except OSError:
        return None
    return run.stdout.strip() if run.returncode == 0 and run.stdout.strip() else None


def now_iso() -> str:
    import datetime
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main(argv: list[str] | None = None) -> int:
    here = Path(__file__).resolve().parent
    ap = argparse.ArgumentParser(description="Render a product's product map from model.json. Stage new files, then render: file counts and ownership read tracked files.")
    ap.add_argument("--source", type=Path, default=here / "model.json", help="the map source (default: model.json beside this file)")
    ap.add_argument("--schema", type=Path, default=here / "map.schema.json", help="the schema (default: map.schema.json beside this file)")
    ap.add_argument("--root", type=Path, help="the repository root (default: two folders above the source)")
    ap.add_argument("--out", type=Path, help="where product-map.md and gaps.md go (default: beside the source)")
    ap.add_argument("--check", action="store_true", help="write nothing; fail if a check fails or the files on disk differ from a fresh render in the form they were made in (with or without file counts)")
    ap.add_argument("--list", action="store_true", help="print every subject id with its point")
    ap.add_argument("--front", action="store_true", help="print the front page")
    ap.add_argument("--card", metavar="ID", help="print one subject's card")
    ap.add_argument("--packet", action="store_true", help="write product-map.json (the source, what the repository derives, and who rendered it) instead of the two Markdown files")
    ap.add_argument("--writer", help="with --packet: the https URL where the map is edited, kept in the packet")
    ap.add_argument("--sha", help="with --packet: the commit rendered (default: git's HEAD under the root)")
    ap.add_argument("--at", help="with --packet: when it was rendered, as an ISO time (default: now, UTC)")
    ap.add_argument("--no-file-counts", action="store_true", help="leave file counts out of the front page and the cards; where the render is committed, render with it, so an added file does not make it stale (gaps.md keeps the count of files no subject owns, as of the render)")
    args = ap.parse_args(argv)
    source = args.source.resolve()
    root, out = (args.root or source.parent.parent.parent).resolve(), (args.out or source.parent).resolve()
    try:
        model, schema = json.loads(source.read_text(encoding="utf-8")), json.loads(args.schema.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        print(f"render_map: {exc}", file=sys.stderr)
        return 1
    problems = validate(model, schema, schema)
    problems += item_rules(model) if not problems else []
    if problems:
        print(f"render_map: {source.name} does not match {args.schema.name}; nothing written:", file=sys.stderr)
        print("\n".join(f"  {p}" for p in problems), file=sys.stderr)
        return 1
    on_disk = (out / "gaps.md").read_text(encoding="utf-8") if args.check and (out / "gaps.md").is_file() else ""
    no_counts = args.no_file_counts or NO_COUNTS_MARK in on_disk  # --check follows the form the render on disk was made in
    built = Map(model, root, tuple(os.path.relpath(folder / name, root).replace(os.sep, "/") for folder in {out, source.parent} for name in OUTPUTS),
                file_counts=not no_counts)
    if args.list or args.front or args.card:
        if args.card and args.card not in built.by_id:
            print(f"render_map: no subject {args.card}; --list prints the ids", file=sys.stderr)
            return 1
        print("\n".join(f"{s['id']}\t{kind}\t{s['point']}" for kind, s in built.subjects) if args.list else built.front() if args.front else built.card(args.card))
        return 0
    if args.packet:
        if args.writer and not re.match(r"^https://[^\s/@]+(/\S*)?$", args.writer):
            print("render_map: --writer takes an https URL without credentials", file=sys.stderr)
            return 1
        out.mkdir(parents=True, exist_ok=True)
        packet = built.packet(args.sha or head_sha(root), args.at or now_iso(), args.writer)
        (out / PACKET).write_text(json.dumps(packet, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"render_map: packet of {plural(len(built.subjects), 'card')} written to {out / PACKET}")
        for line in built.flags:
            print(f"flag (not a failure): {line}")
        for line in built.errors:
            print(f"check failed: {line}", file=sys.stderr)
        return 1 if built.errors else 0
    rendered = {"product-map.md": built.product_map(), "gaps.md": built.gaps(unowned_note=True)}
    # without file counts only the number on the unowned line is free to differ: the line must be there, once, with the rest of its text
    compared = lambda text: re.sub(rf"(?m)^({re.escape(UNOWNED_LINE)})\d+", r"\1N", text) if no_counts else text
    stale = []
    for name in OUTPUTS:
        text = rendered[name].rstrip("\n") + "\n"
        if args.check:
            if not (out / name).is_file() or compared((out / name).read_text(encoding="utf-8")) != compared(text):
                stale.append(name)
        else:
            out.mkdir(parents=True, exist_ok=True)
            (out / name).write_text(text, encoding="utf-8")
    print(f"render_map: {plural(len(built.subjects), 'card')}, front page {len(built.front().encode('utf-8'))} bytes" + ("" if args.check else f", written to {out}")
          + (f"; no file counts, {plural(built.unowned_now(), 'file')} owned by no subject" if no_counts else ""))
    for line in built.flags + ([] if built.file_counts else built.budget_flags()):
        print(f"flag (not a failure): {line}")
    for line in built.errors:
        print(f"check failed: {line}", file=sys.stderr)
    for name in stale:
        print(f"check failed: {name} is missing or differs from a fresh render; run render_map.py{' --no-file-counts' if no_counts else ''}", file=sys.stderr)
    return 1 if built.errors or stale else 0


if __name__ == "__main__":
    sys.exit(main())
