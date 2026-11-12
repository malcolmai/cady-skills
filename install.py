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
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
LOCK = "cady-roster.lock.json"
POINTER = re.compile(r" \(`\.\./([a-z0-9-]+)/SKILL\.md`\)")
SAFE_NAME = re.compile(r"[a-z0-9][a-z0-9-]*")
SAFE_REF = re.compile(r"[A-Za-z0-9_][A-Za-z0-9_.-]*\.md")


def atomic_write(path: Path, data: bytes) -> None:
    """Write a new file and swap it in, so a hard link elsewhere keeps its text and an interrupted run leaves no half file."""
    fd, tmp = tempfile.mkstemp(dir=path.parent, prefix=f".{path.name}.", suffix=".cady-tmp")  # a name no file holds yet
    try:
        mask = os.umask(0); os.umask(mask)
        os.fchmod(fd, 0o666 & ~mask)  # the usual permissions for a new file, not mkstemp's owner-only ones
        with os.fdopen(fd, "wb") as handle:
            handle.write(data)
        os.replace(tmp, path)
    except BaseException:
        Path(tmp).unlink(missing_ok=True)
        raise


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
    """Bring dest to the roster: plan every change, check every path stays inside dest, then make the changes.

    A file is the library's only while it matches a version the library delivered (the lock's files and history); any other
    file is the company's and is never overwritten or deleted. When the library's text for a company file changes, the new
    text goes beside it as <file>.upstream; an .upstream the installer did not write is never overwritten either.
    """
    before: dict[str, str] = lock.get("files", {})
    history: dict[str, list[str]] = lock.get("history", {})
    ours_up: dict[str, str] = lock.get("upstreams", {})
    report: dict = {"written": [], "kept": [], "removed": [], "left": [], "blocked": [], "beside": []}
    plan: list[tuple[str, str, bytes | None]] = []
    after: dict[str, str] = {}
    upstreams: dict[str, str] = {}

    def read(rel: str) -> str | None:
        path = dest / rel
        return sha(path.read_bytes()) if path.is_file() else None

    def drop_our_upstream(rel: str) -> None:
        up = rel + ".upstream"
        if rel in ours_up and read(up) == ours_up[rel]:
            plan.append(("unlink", up, None))

    for rel, data in sorted(files.items()):
        new = sha(data)
        after[rel] = new
        local = read(rel)
        if local == new:
            drop_our_upstream(rel)
            continue
        delivered = {before.get(rel), *history.get(rel, [])} - {None}
        if local is not None and local not in delivered:
            up = rel + ".upstream"
            current = read(up)
            if current == new:
                upstreams[rel] = new  # it already holds the library's text
            elif current is None and ours_up.get(rel) == new:
                upstreams[rel] = new  # you merged and deleted the one we wrote for this text; nothing new to put beside it
            elif current is None or (rel in ours_up and current == ours_up[rel]):
                plan.append(("write", up, data))
                upstreams[rel] = new
                report["kept"].append(rel)
                report["beside"].append(up)
            else:
                report["blocked"].append(rel)
            continue
        plan.append(("write", rel, data))
        report["written"].append(rel)
        drop_our_upstream(rel)
    for rel, old in sorted(before.items()):
        if rel in files:
            continue
        local = read(rel)
        if local is not None and local not in {old, *history.get(rel, [])}:
            report["left"].append(rel)
            continue
        if local is not None:
            report["removed"].append(rel)
            plan.append(("unlink", rel, None))
        drop_our_upstream(rel)
    for _, rel, _ in plan:  # every path is checked before the first change, so a refusal leaves dest untouched
        inside(dest, rel)
        hop = dest
        parts = Path(rel).parts
        for i, part in enumerate(parts):  # no folder or file on the way may be a link, and each folder must be a folder
            hop = hop / part
            if hop.is_symlink():
                raise SystemExit(f"install.py: refusing {rel!r}: {hop.relative_to(dest)} is a symlink")
            last = i == len(parts) - 1
            if hop.exists() and ((not last and not hop.is_dir()) or (last and not hop.is_file())):
                raise SystemExit(f"install.py: refusing {rel!r}: {hop.relative_to(dest)} is in the way (move it, then run again)")
    # An .upstream the installer wrote earlier stays recorded as ours while it is still there unchanged.
    for rel, digest in ours_up.items():
        if rel not in upstreams and ("unlink", rel + ".upstream", None) not in plan and read(rel + ".upstream") == digest:
            upstreams[rel] = digest
    if not dry:
        for op, rel, data in plan:
            path = dest / rel
            if op == "write":  # (an .upstream write is counted in report["beside"])
                path.parent.mkdir(parents=True, exist_ok=True)
                atomic_write(path, data)
            else:
                path.unlink()
                for parent in path.parents:
                    if parent == dest or not parent.is_dir() or any(parent.iterdir()):
                        break
                    parent.rmdir()
    report["files"] = after
    report["upstreams"] = upstreams
    # Every version the library has delivered for a file: restoring any of them is not a company edit.
    report["history"] = {rel: h for rel in after
                         if (h := [v for v in dict.fromkeys([before.get(rel), *history.get(rel, [])]) if v and v != after[rel]])}
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
    lock_path = inside(dest, LOCK)
    if lock_path.is_symlink() or (lock_path.exists() and not lock_path.is_file()):
        ap.error(f"{lock_path} must be a plain file inside {dest}; move it aside, then run again")
    try:
        lock = json.loads(lock_path.read_text()) if lock_path.is_file() else {}
    except (OSError, ValueError) as e:
        ap.error(f"{lock_path} is not a readable lock ({e}); fix or remove it, then run again")
    shape = {"files": dict, "history": dict, "upstreams": dict, "agents": list}
    def well_formed(lock: object) -> bool:
        if not isinstance(lock, dict) or any(k in lock and not isinstance(lock[k], kind) for k, kind in shape.items()):
            return False
        strs = lambda xs: all(isinstance(x, str) for x in xs)
        return (strs(lock.get("agents", [])) and strs(lock.get("files", {}).values()) and strs(lock.get("upstreams", {}).values())
                and all(isinstance(v, list) and strs(v) for v in lock.get("history", {}).values()))
    if not well_formed(lock):
        ap.error(f"{lock_path} is not a roster lock (expected an object with files, history and upstreams objects and an agents list); fix or remove it, then run again")
    if args.update and not lock:
        ap.error(f"no roster at {dest} ({LOCK} not found); run without --update to install, or pass --dest")
    if lock and lock.get("host") != args.host:
        ap.error(f"{lock_path} was installed for {lock.get('host')}; pass that --host or another --dest")
    agents = list(lock.get("agents") or roster["system"])
    gone = [k for k in agents if k not in roster["agents"]]
    if gone:  # an agent this library lacks: drop it; the sync deletes its unedited files and leaves edited ones in place
        print(f"  dropped from the roster (not in this library): {', '.join(gone)}")
        agents = [k for k in agents if k not in gone]
    missing_system = [k for k in roster["system"] if k not in agents]
    if missing_system:  # the company system always runs, whatever the lock says
        if lock:
            print(f"  added to the roster (the company system always runs): {', '.join(missing_system)}")
        agents = missing_system + agents
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
        atomic_write(lock_path, (json.dumps({"schema": "cady.roster-lock.v1", "host": args.host, "library": roster["library"],
                                         "agents": agents,
                                         "files": report["files"], "history": report["history"],
                                         "upstreams": report["upstreams"]}, indent=2) + "\n").encode())
    verb = "would change" if args.dry_run else "changed"
    print(f"Cady roster for {args.host} at {dest}: {', '.join(agents)} (library {roster['library']['tag']})")
    print(f"  {verb}: {len(report['written'])} written, {len(report['removed'])} removed"
          + (f", {len(report['beside'])} .upstream written beside your edits" if report["beside"] else ""))
    for rel in report["kept"]:
        print(f"  kept your edit: {rel} (the new version is {rel}.upstream; merge it by hand, then delete it)")
    for rel in report["blocked"]:
        print(f"  kept your edit: {rel} (the library changed it, but {rel}.upstream is yours, so the new text was not written)")
    for rel in report["left"]:
        print(f"  left in place: {rel} (no longer in the roster, but you edited it)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
