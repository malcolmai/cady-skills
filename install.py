#!/usr/bin/env python3
"""Adopt the Cady agents your company runs: copy each agent's skill folders from this library into your host.

Run it from a clone of the library. The first run also copies the company system (the Executive and the orchestrator) and the
core skills every agent reads. A folder you already have is never overwritten ("kept yours"), so a re-run changes nothing.

  python3 install.py --list                                   # the agents this library holds
  python3 install.py --host claude-code --add gtm,marketing   # into ./.claude/skills
  python3 install.py --host codex --add product               # into $CODEX_HOME/skills (default ~/.codex), front door included
  python3 install.py --host claude-code --remove marketing    # deletes only folders identical to the library's

Standard library only. Nothing is fetched; the files come from this checkout.
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def tree(path: Path) -> dict[str, bytes]:
    return {p.relative_to(path).as_posix(): p.read_bytes() for p in sorted(path.rglob("*")) if p.is_file()}


def names_for(roster: dict, agents: list[str]) -> list[str]:
    names = list(roster["core"])
    for key in agents:
        names += [roster["agents"][key]["card"], *roster["agents"][key]["skills"]]
    return list(dict.fromkeys(names))


def inside(root: Path, name: str) -> Path:
    path = (root / name).resolve()
    if root.resolve() not in path.parents:
        raise SystemExit(f"install.py: refusing {name!r}: it is outside {root}")
    return path


def main(argv: list[str] | None = None) -> int:
    roster = json.loads((HERE / "roster.json").read_text())
    ap = argparse.ArgumentParser(description="Adopt Cady agents from this library into your host.")
    ap.add_argument("--host", choices=("claude-code", "codex"))
    ap.add_argument("--dest", type=Path, help="where skills/ lives (default: ./.claude, or $CODEX_HOME for Codex)")
    ap.add_argument("--add", default="", help="comma-separated agents to adopt (see --list)")
    ap.add_argument("--remove", default="", help="comma-separated agents to remove (only folders identical to the library's)")
    ap.add_argument("--list", action="store_true", help="list the agents this library holds and exit")
    args = ap.parse_args(argv)
    if args.list:
        for key, a in roster["agents"].items():
            print(f"{key:24} {a['family']:12} {a['label']}{' (always)' if key in roster['system'] else ''}: {a['purpose']}")
        return 0
    if not args.host:
        ap.error("--host is required (claude-code or codex)")
    split = lambda s: [x.strip() for x in s.split(",") if x.strip()]
    add, remove = split(args.add), split(args.remove)
    for key in add + remove:
        if key not in roster["agents"]:
            ap.error(f"unknown agent {key!r}; run --list")
    if add and remove:
        ap.error("pass --add or --remove, not both")
    if [k for k in remove if k in roster["system"]]:
        ap.error("the company system (company, orchestrator) always runs and cannot be removed")
    dest = (args.dest or (Path(os.environ.get("CODEX_HOME") or Path.home() / ".codex") if args.host == "codex" else Path.cwd() / ".claude")).expanduser()
    skills = dest / "skills"
    if skills.is_symlink():
        ap.error(f"{skills} is a symlink; point --dest at the real folder")
    wanted = [(n, HERE / "library" / n) for n in names_for(roster, [*roster["system"], *add])]
    if args.host == "codex":
        wanted.append(("cady", HERE / roster["front_door"]))
    if remove:
        adopted = [k for k in roster["agents"] if k not in remove and (skills / roster["agents"][k]["card"]).is_dir()]
        keep = set(names_for(roster, adopted)) | {"cady"}
        for name in names_for(roster, remove):
            if name in keep:
                continue
            if (skills / name).is_symlink():  # judged before resolving, so a link is never followed or deleted through
                print(f"  kept {name}: it is a symlink, not a folder this installer made")
                continue
            src, target = HERE / "library" / name, inside(skills, name)
            if not target.is_dir():
                continue
            if tree(target) == tree(src):
                shutil.rmtree(target)
                print(f"  removed {name}")
            else:
                print(f"  kept {name}: it differs from this library (you edited it, or the library changed since you adopted it)")
    else:
        for name, src in wanted:
            if not src.is_dir():
                print(f"  skipped {name} (not in this library)")
                continue
            if (skills / name).is_symlink():
                print(f"  kept {name}: it is a symlink, not a folder this installer made")
                continue
            target = inside(skills, name)
            if target.exists():
                print(f"  kept yours: {name}")
            else:
                shutil.copytree(src, target)
                print(f"  added {name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
