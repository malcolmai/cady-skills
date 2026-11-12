#!/usr/bin/env python3
"""Install the skills for a company's Cady roster from this library: for each agent it runs, its role card and the skills that card lists.

Run it from a clone of the library. The first run installs the company system (the Executive and the orchestrator) and the
core skills every agent reads; add the agents your Executive designed with --add. Each run syncs the host to the roster and
records what it wrote in a lock file, so a later run from a newer library updates what you have not edited and keeps what you
have, with the new version beside it as <file>.upstream to merge by hand.

  python3 install.py --host claude-code                  # into ./.claude (skills and the shared references they link)
  python3 install.py --host claude-code --add gtm,marketing
  python3 install.py --host codex                        # into $CODEX_HOME (default ~/.codex), front door included
  python3 install.py --list                              # the agents this library holds
  python3 install.py --host claude-code --update         # after pulling a newer library: same roster, newer files

Standard library only. Nothing is fetched: the files come from this checkout. Agent files are not written here: the Cady CLI's
`cady setup agents` writes them, and each names its role card skill, which this installs.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
LOCK = "cady-roster.lock.json"
POINTER = re.compile(r" \(`\.\./([a-z0-9-]+)/SKILL\.md`\)")
SAFE_NAME = re.compile(r"[a-z0-9][a-z0-9-]*")
SAFE_REF = re.compile(r"[A-Za-z0-9_][A-Za-z0-9_.-]*\.md")


def inside(dest: Path, rel: str) -> Path:
    """dest/rel, refusing any path that would land outside dest (a lock or roster entry with .. or an absolute path)."""
    root = dest.resolve()
    path = (dest / rel).resolve()
    if path != root and root not in path.parents:
        raise SystemExit(f"install.py: refusing {rel!r}: it is outside {dest}")
    return dest / rel


def load_roster() -> dict:
    return json.loads((HERE / "roster.json").read_text())


def default_dest(host: str) -> Path:
    if host == "codex":
        return Path(os.environ.get("CODEX_HOME") or Path.home() / ".codex")
    return Path.cwd() / ".claude"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def skill_files(name: str, installed: set[str]) -> dict[str, bytes]:
    """One library skill as installed: its folder under skills/, with pointers to skills this roster lacks reduced to the name."""
    src = HERE / "library" / name
    out: dict[str, bytes] = {}
    for path in sorted(p for p in src.rglob("*") if p.is_file()):
        data = path.read_bytes()
        if path.name == "SKILL.md":
            data = POINTER.sub(lambda m: m.group(0) if m.group(1) in installed else "", data.decode()).encode()
        out[f"skills/{name}/{path.relative_to(src).as_posix()}"] = data
    return out


def desired(roster: dict, host: str, agents: list[str]) -> dict[str, bytes]:
    """Every file the roster puts on the host, by path relative to the destination."""
    names: list[str] = list(roster["core"])
    for key in agents:
        a = roster["agents"][key]
        names += [a["card"], *a["skills"]]
    missing = [n for n in dict.fromkeys(names) if not (HERE / "library" / n / "SKILL.md").is_file()]
    for name in missing:  # a fork that dropped a skill a card still lists: say so rather than install around it
        print(f"  skipped: {name} (named by the roster but not in this library)")
    names = [n for n in dict.fromkeys(names) if n not in missing]
    for name in names:
        if not SAFE_NAME.fullmatch(name):
            raise SystemExit(f"install.py: refusing skill name {name!r} in roster.json")
    installed = set(names)
    files: dict[str, bytes] = {}
    shared: set[str] = set()
    for name in names:
        files.update(skill_files(name, installed))
        shared.update(roster["skills"].get(name, {}).get("shared", []))
    for ref in sorted(shared):
        if not SAFE_REF.fullmatch(ref):
            raise SystemExit(f"install.py: refusing reference name {ref!r} in roster.json")
        files[f"references/{ref}"] = (HERE / "references" / ref).read_bytes()
    if host == "codex":
        door = HERE / roster["front_door"]
        for path in sorted(p for p in door.rglob("*") if p.is_file()):
            files[f"skills/cady/{path.relative_to(door).as_posix()}"] = path.read_bytes()
    return files


def sync(dest: Path, files: dict[str, bytes], lock: dict, dry: bool) -> dict:
    """Write the roster's files: new or unedited ones are replaced, edited ones kept with the new text beside them."""
    before: dict[str, str] = lock.get("files", {})
    report = {"written": [], "kept": [], "removed": [], "left": []}
    after: dict[str, str] = {}
    for rel, data in sorted(files.items()):
        path = inside(dest, rel)
        new = sha(data)
        after[rel] = new
        if path.is_file():
            local = sha(path.read_bytes())
            if local == new:
                continue
            delivered = {before.get(rel), *lock.get("history", {}).get(rel, [])} - {None}
            if local not in delivered:
                # Yours, not the library's: an edit, or a file this roster never delivered (no lock, or an agent added back).
                # Keep it; when the library's text differs from what it last delivered, put the new text beside it.
                if new != before.get(rel):
                    report["kept"].append(rel)
                    if not dry:
                        inside(dest, rel + ".upstream").write_bytes(data)
                continue
        report["written"].append(rel)
        if not dry:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
    for rel, old in sorted(before.items()):
        if rel in files:
            continue
        path = inside(dest, rel)
        if path.is_file() and sha(path.read_bytes()) not in {old, *lock.get("history", {}).get(rel, [])}:
            report["left"].append(rel)
            continue
        report["removed"].append(rel)
        if not dry and path.is_file():
            path.unlink()
            for parent in path.parents:
                if parent == dest or not parent.is_dir() or any(parent.iterdir()):
                    break
                parent.rmdir()
    report["files"] = after
    # Every version the library has delivered for a file: restoring any of them is not a company edit.
    history = {}
    for rel in after:
        seen = [before.get(rel), *lock.get("history", {}).get(rel, [])]
        history[rel] = [h for h in dict.fromkeys(seen) if h and h != after[rel]][:8]
    report["history"] = {rel: h for rel, h in history.items() if h}
    return report


def main(argv: list[str] | None = None) -> int:
    roster = load_roster()
    ap = argparse.ArgumentParser(description="Install or update a company's Cady roster from this library.")
    ap.add_argument("--host", choices=("claude-code", "codex"))
    ap.add_argument("--dest", type=Path, help="where to install (default: ./.claude, or $CODEX_HOME for Codex)")
    ap.add_argument("--add", default="", help="comma-separated agents to add, for example gtm,marketing (see --list)")
    ap.add_argument("--remove", default="", help="comma-separated agents to remove")
    ap.add_argument("--update", action="store_true", help="resync the roster in the lock file to this library")
    ap.add_argument("--list", action="store_true", help="list the agents this library holds and exit")
    ap.add_argument("--dry-run", action="store_true", help="say what would change and write nothing")
    args = ap.parse_args(argv)
    if args.list:
        for key, a in roster["agents"].items():
            tag = " (always)" if key in roster["system"] else ""
            print(f"{key:24} {a['family']:12} {a['label']}{tag}: {a['purpose']}")
        return 0
    if not args.host:
        ap.error("--host is required (claude-code or codex)")
    dest = (args.dest or default_dest(args.host)).expanduser()
    lock_path = dest / LOCK
    lock = json.loads(lock_path.read_text()) if lock_path.is_file() else {}
    if args.update and not lock:
        ap.error(f"no roster at {dest} ({LOCK} not found); run without --update to install, or pass --dest")
    if lock and lock.get("host") != args.host:
        ap.error(f"{lock_path} was installed for {lock.get('host')}; pass that --host or another --dest")
    agents = list(lock.get("agents") or roster["system"])
    gone = [k for k in agents if k not in roster["agents"]]
    if gone:  # an agent this library lacks: drop it; the sync deletes its unedited files and leaves edited ones in place
        print(f"  dropped from the roster (not in this library): {', '.join(gone)}")
        agents = [k for k in agents if k not in gone]
    split = lambda s: [x.strip() for x in s.split(",") if x.strip()]
    for key in split(args.add) + split(args.remove):
        if key not in roster["agents"]:
            ap.error(f"unknown agent {key!r}; run --list")
    agents += [k for k in split(args.add) if k not in agents]
    removing = [k for k in split(args.remove) if k in roster["system"]]
    if removing:
        ap.error(f"{', '.join(removing)}: the company system always runs and cannot be removed")
    agents = [k for k in agents if k not in split(args.remove)]
    report = sync(dest, desired(roster, args.host, agents), lock, args.dry_run)
    if not args.dry_run:
        dest.mkdir(parents=True, exist_ok=True)
        lock_path.write_text(json.dumps({"schema": "cady.roster-lock.v1", "host": args.host, "library": roster["library"],
                                         "agents": agents,
                                         "files": report["files"], "history": report["history"]}, indent=2) + "\n")
    verb = "would change" if args.dry_run else "changed"
    print(f"Cady roster for {args.host} at {dest}: {', '.join(agents)} (library {roster['library']['tag']})")
    print(f"  {verb}: {len(report['written'])} written, {len(report['removed'])} removed")
    for rel in report["kept"]:
        print(f"  kept your edit: {rel} (the new version is {rel}.upstream; merge it by hand, then delete it)")
    for rel in report["left"]:
        print(f"  left in place: {rel} (no longer in the roster, but you edited it)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
