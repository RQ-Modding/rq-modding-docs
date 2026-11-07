#!/usr/bin/env python3
"""Copies what the docs take from the engine repo.

  python -I -X utf8 scripts/sync.py [--engine PATH] [--check]

  docs/reference/      the API reference, generated from the engine's dist/lua/rq.lua by
                       tools/apidoc/rqdoc.py (never edit these pages by hand)
  docs/changelog.md    the engine's CHANGELOG.md
  docs/.vitepress/engine.json   the loader version and engine commit the pages came from

--engine defaults to ../RQ_modding_xsystem4 (the workspace layout). --check writes nothing and
exits 1 when the committed pages differ from what the engine would give.
Standard library only.
"""
import filecmp
import json
import os
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, "docs")


def generate(engine, out):
    """Writes reference/, changelog.md and engine.json under out (a docs-shaped folder)."""
    rq_lua = os.path.join(engine, "dist", "lua", "rq.lua")
    rqdoc = os.path.join(engine, "tools", "apidoc", "rqdoc.py")
    for p in (rq_lua, rqdoc):
        if not os.path.isfile(p):
            sys.exit("sync: not found: " + p)
    ref = os.path.join(out, "reference")
    subprocess.run([sys.executable, "-I", "-X", "utf8", rqdoc, "md", rq_lua, ref],
                   check=True, stdout=subprocess.DEVNULL)

    with open(os.path.join(engine, "CHANGELOG.md"), encoding="utf-8") as f:
        log = f.read()
    with open(os.path.join(out, "changelog.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write("<!-- Copied from the engine's CHANGELOG.md by scripts/sync.py. Edit it there. -->\n\n")
        f.write(log.replace("\r\n", "\n"))

    subprocess.run([sys.executable, "-I", "-X", "utf8", rqdoc, "json", rq_lua, os.path.join(out, "_model.json")],
                           check=True, stdout=subprocess.DEVNULL)
    with open(os.path.join(out, "_model.json"), encoding="utf-8") as f:
        version = json.load(f)["version"]
    os.remove(os.path.join(out, "_model.json"))
    try:
        commit = subprocess.run(["git", "-C", engine, "rev-parse", "--short", "HEAD"], check=True,
                                capture_output=True, text=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        commit = ""
    os.makedirs(os.path.join(out, ".vitepress"), exist_ok=True)
    with open(os.path.join(out, ".vitepress", "engine.json"), "w", encoding="utf-8", newline="\n") as f:
        json.dump({"version": version, "commit": commit}, f, indent=2)
        f.write("\n")


def same_tree(a, b):
    cmp = filecmp.dircmp(a, b)
    if cmp.left_only or cmp.right_only or cmp.funny_files:
        return False
    _, mismatch, errors = filecmp.cmpfiles(a, b, cmp.common_files, shallow=False)
    if mismatch or errors:
        return False
    return all(same_tree(os.path.join(a, d), os.path.join(b, d)) for d in cmp.common_dirs)


def main(argv):
    engine = os.path.join(os.path.dirname(ROOT), "RQ_modding_xsystem4")
    check = False
    args = list(argv)
    while args:
        a = args.pop(0)
        if a == "--engine" and args:
            engine = args.pop(0)
        elif a == "--check":
            check = True
        else:
            sys.exit(__doc__)
    engine = os.path.abspath(engine)

    with tempfile.TemporaryDirectory() as tmp:
        generate(engine, tmp)
        pairs = [("reference", True), ("changelog.md", False)]
        if check:
            bad = []
            for name, is_dir in pairs:
                new, old = os.path.join(tmp, name), os.path.join(DOCS, name)
                ok = os.path.exists(old) and (same_tree(new, old) if is_dir else filecmp.cmp(new, old, shallow=False))
                if not ok:
                    bad.append(name)
            if bad:
                print("sync --check: out of date: " + ", ".join(bad) + ". Run scripts/sync.py and commit.")
                return 1
            print("sync --check: docs match the engine")
            return 0
        for name, is_dir in pairs:
            dst = os.path.join(DOCS, name)
            if is_dir:
                shutil.rmtree(dst, ignore_errors=True)
                shutil.copytree(os.path.join(tmp, name), dst)
            else:
                shutil.copyfile(os.path.join(tmp, name), dst)
        shutil.copyfile(os.path.join(tmp, ".vitepress", "engine.json"), os.path.join(DOCS, ".vitepress", "engine.json"))
    with open(os.path.join(DOCS, ".vitepress", "engine.json"), encoding="utf-8") as f:
        info = json.load(f)
    print("sync: reference and changelog from RQ MOD %s (%s)" % (info["version"], info["commit"] or "no git"))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
