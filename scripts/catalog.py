#!/usr/bin/env python3
"""Writes the mods' catalog, docs/public/mods.json, from catalog/listed.json and GitHub.

  python -I -X utf8 scripts/catalog.py [--listed PATH] [--out PATH]   (npm run catalog)
  python -I -X utf8 scripts/catalog.py --check [--listed PATH] [--out PATH]

listed.json names each listed mod's repository and the version that was checked, with its tags and
its save note, and the repositories of RQ MOD and (once it has a release) RQ Manager. For RQ MOD's
and RQ Manager's latest releases and for each mod, the script asks GitHub for the release,
the mod.json at its tag and the repository's description and license, downloads every zip and checks
it, and writes mods.json only when nothing is wrong. Its rules:

  - the version in listed.json is the version of mod.json at the tag (v<version> by default);
  - the release has exactly one .zip (or the one listed.json names as "asset"), its SHA-256 is the
    one GitHub gives, and it holds <id>/mod.json and <id>/init.lua with nothing outside <id>/
    (RQ MOD's holds xsystem4/xsystem4.exe, RQ Manager's "RQ Manager/rq-manager.exe");
    the mod.json inside is the one at the tag;
  - no two mods share an id; every dependency is listed; a mod's loader is not newer than
    RQ MOD's latest release (a player could not run it);
  - tags and the save note are the ones catalog.schema.json allows.

GitHub's API needs a token for this many calls: GH_TOKEN or GITHUB_TOKEN, or `gh auth token`.
The token is never printed, and never sent with a download.

--check needs no network: mods.json against docs/public/schemas/catalog.schema.json, and every
entry of listed.json in it at its version, with the same tags and save note. Exits 1 on a problem.
Standard library only.
"""
import argparse
import base64
import datetime
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LISTED = os.path.join(ROOT, "catalog", "listed.json")
OUT = os.path.join(ROOT, "docs", "public", "mods.json")
SCHEMA = os.path.join(ROOT, "docs", "public", "schemas", "catalog.schema.json")
SCHEMA_URL = "https://rq-modding.github.io/rq-modding-docs/schemas/catalog.schema.json"
API = "https://api.github.com/"
AGENT = "rq-modding-docs-catalog"
SUFFIX = "An RQ MOD mod for Rance Quest Magnum."


class Problems(Exception):
    pass


def load_json(path):
    with open(path, encoding="utf-8-sig") as f:
        return json.load(f)


def semver(s):
    """'2.39' or '2.39.0' -> (2, 39, 0); None when it is not one."""
    m = re.fullmatch(r"([0-9]+)(?:\.([0-9]+)(?:\.([0-9]+))?)?", s or "")
    return tuple(int(x or 0) for x in m.groups()) if m else None


# ---------- GitHub ----------

def token():
    for name in ("GH_TOKEN", "GITHUB_TOKEN"):
        if os.environ.get(name):
            return os.environ[name]
    try:
        out = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True, check=True)
        return out.stdout.strip() or None
    except (OSError, subprocess.CalledProcessError):
        return None


class GitHub:
    def __init__(self, tok):
        self.tok = tok
        self.calls = 0

    def get(self, path):
        req = urllib.request.Request(API + path, headers={
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": AGENT,
        })
        if self.tok:
            req.add_header("Authorization", "Bearer " + self.tok)
        self.calls += 1

        def fetch():
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.load(r)
        try:
            return retried(fetch)
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            raise Problems([f"GitHub: {path}: HTTP {e.code} {e.reason}"]) from None

    def file(self, repo, path, ref):
        got = self.get(f"repos/{repo}/contents/{path}?ref={ref}")
        if not got or got.get("encoding") != "base64":
            return None
        return base64.b64decode(got["content"])


def retried(fn, tries=3):
    """fn(), again after a network error or a timeout (up to `tries` times)."""
    for n in range(tries):
        try:
            return fn()
        except urllib.error.HTTPError:
            raise
        except (urllib.error.URLError, TimeoutError, ConnectionError) as e:
            if n == tries - 1:
                raise Problems([f"network: {e}"]) from None
            time.sleep(2 * (n + 1))


def download(url):
    """A public release asset, with no token (the URL redirects to GitHub's file host)."""
    def get():
        req = urllib.request.Request(url, headers={"User-Agent": AGENT})
        with urllib.request.urlopen(req, timeout=120) as r:
            return r.read()
    return retried(get)


def pick_zip(release, name, where, problems):
    zips = [a for a in release.get("assets", []) if a["name"].lower().endswith(".zip")]
    if name:
        zips = [a for a in zips if a["name"] == name]
    if len(zips) != 1:
        problems.append(f"{where}: {len(zips)} zips in release {release.get('tag_name')}"
                        + (f" named {name}" if name else "") + "; expected 1")
        return None
    return zips[0]


def checked_file(asset, data, where, problems):
    """The catalog's file entry for an asset, after its bytes were checked against GitHub's digest."""
    sha = hashlib.sha256(data).hexdigest()
    digest = (asset.get("digest") or "").lower()
    if digest and digest != "sha256:" + sha:
        problems.append(f"{where}: {asset['name']}: SHA-256 {sha} is not GitHub's {digest}")
    if len(data) != asset["size"]:
        problems.append(f"{where}: {asset['name']}: {len(data)} bytes downloaded, GitHub says {asset['size']}")
    return {"name": asset["name"], "url": asset["browser_download_url"], "size": len(data), "sha256": sha}


def day(stamp):
    return (stamp or "")[:10]


# ---------- Writing ----------

def build(listed, gh, fetch=download):
    problems = []

    eng_repo = listed.get("engine", "RQ-Modding/RQ-Mod")
    rel = gh.get(f"repos/{eng_repo}/releases/latest")
    if not rel:
        raise Problems([f"engine: {eng_repo} has no release"])
    version = rel["tag_name"].lstrip("v")
    if not semver(version) or not re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+", version):
        problems.append(f"engine: tag {rel['tag_name']} is not v<major>.<minor>.<patch>")
    name = (rel.get("name") or "").strip()
    stage = name[len(f"RQ MOD {version}"):].strip() if name.startswith(f"RQ MOD {version}") else ""
    asset = pick_zip(rel, None, "engine", problems)
    engine = None
    if asset:
        data = fetch(asset["browser_download_url"])
        zfile = checked_file(asset, data, "engine", problems)
        with zipfile.ZipFile(io.BytesIO(data)) as z:
            if "xsystem4/xsystem4.exe" not in z.namelist():
                problems.append(f"engine: {asset['name']} has no xsystem4/xsystem4.exe")
        engine = {"version": version, "stage": stage, "tag": rel["tag_name"],
                  "published": day(rel.get("published_at")), "notes": rel["html_url"], "zip": zfile}
    engine_v = semver(version)

    # RQ Manager's latest release, once listed.json names its repository.
    manager = None
    mgr_repo = listed.get("manager")
    if mgr_repo:
        rel = gh.get(f"repos/{mgr_repo}/releases/latest")
        if not rel:
            problems.append(f"manager: {mgr_repo} has no release")
        else:
            mv = rel["tag_name"].lstrip("v")
            if not re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+", mv):
                problems.append(f"manager: tag {rel['tag_name']} is not v<major>.<minor>.<patch>")
            asset = pick_zip(rel, None, "manager", problems)
            if asset:
                data = fetch(asset["browser_download_url"])
                mfile = checked_file(asset, data, "manager", problems)
                with zipfile.ZipFile(io.BytesIO(data)) as z:
                    if "RQ Manager/rq-manager.exe" not in z.namelist():
                        problems.append(f"manager: {asset['name']} has no RQ Manager/rq-manager.exe")
                manager = {"version": mv, "tag": rel["tag_name"], "published": day(rel.get("published_at")),
                           "notes": rel["html_url"], "zip": mfile}

    schema = load_json(SCHEMA)
    tags_ok = set(schema["$defs"]["mod"]["properties"]["tags"]["items"]["enum"])
    saves_ok = set(schema["$defs"]["mod"]["properties"]["save"]["enum"])

    mods, ids = [], {}
    for entry in listed.get("mods", []):
        repo, want = entry.get("repo", ""), entry.get("version", "")
        where = repo or "?"
        if not re.fullmatch(r"[A-Za-z0-9._-]+/[A-Za-z0-9._-]+", repo):
            problems.append(f"{where}: repo must be owner/name")
            continue
        bad_tags = [t for t in entry.get("tags", []) if t not in tags_ok]
        if not entry.get("tags") or bad_tags:
            problems.append(f"{where}: tags {entry.get('tags')} (allowed: {', '.join(sorted(tags_ok))})")
        if entry.get("save") not in saves_ok:
            problems.append(f"{where}: save {entry.get('save')!r} (allowed: {', '.join(sorted(saves_ok))})")

        info = gh.get(f"repos/{repo}")
        if not info:
            problems.append(f"{where}: no such repository")
            continue
        if info.get("private"):
            problems.append(f"{where}: the repository is private")
        tag = entry.get("tag") or f"v{want}"
        rel = gh.get(f"repos/{repo}/releases/tags/{tag}")
        if not rel:
            problems.append(f"{where}: no release with the tag {tag}")
            continue
        if rel.get("draft") or rel.get("prerelease"):
            problems.append(f"{where}: release {tag} is a draft or a pre-release")
        raw = gh.file(repo, "mod.json", tag)
        if raw is None:
            problems.append(f"{where}: no mod.json at {tag}")
            continue
        try:
            manifest = json.loads(raw.decode("utf-8-sig"))
        except ValueError as e:
            problems.append(f"{where}: mod.json at {tag}: {e}")
            continue
        mid = manifest.get("id", "")
        if not mid:
            problems.append(f"{where}: mod.json at {tag} has no id")
            continue
        where = f"{mid} ({repo})"
        if manifest.get("version") != want:
            problems.append(f"{where}: listed at {want}, mod.json at {tag} says {manifest.get('version')}")
        if mid in ids:
            problems.append(f"{where}: id already listed by {ids[mid]}")
        ids[mid] = repo
        loader = manifest.get("loader", "")
        if not semver(loader):
            problems.append(f"{where}: loader {loader!r} is not a version")
        elif engine_v and semver(loader) > engine_v:
            problems.append(f"{where}: needs loader {loader}, newer than RQ MOD's release {version}")

        asset = pick_zip(rel, entry.get("asset"), where, problems)
        if not asset:
            continue
        data = fetch(asset["browser_download_url"])
        zfile = checked_file(asset, data, where, problems)
        try:
            with zipfile.ZipFile(io.BytesIO(data)) as z:
                names = z.namelist()
                outside = [n for n in names if not n.startswith(mid + "/")]
                if outside:
                    problems.append(f"{where}: {asset['name']} holds files outside {mid}/: {outside[:3]}")
                for need in ("mod.json", "init.lua"):
                    if f"{mid}/{need}" not in names:
                        problems.append(f"{where}: {asset['name']} has no {mid}/{need}")
                if f"{mid}/mod.json" in names:
                    inner = json.loads(z.read(f"{mid}/mod.json").decode("utf-8-sig"))
                    if inner != manifest:
                        problems.append(f"{where}: the mod.json in {asset['name']} is not the one at {tag}")
        except (zipfile.BadZipFile, ValueError) as e:
            problems.append(f"{where}: {asset['name']}: {e}")

        desc = entry.get("description") or (info.get("description") or "").strip()
        if desc.endswith(SUFFIX):
            desc = desc[: -len(SUFFIX)].strip()
        if not desc:
            problems.append(f"{where}: no description (the repository has none; give one in listed.json)")
        lic = (info.get("license") or {}).get("spdx_id") or ""
        if not lic or lic == "NOASSERTION":
            problems.append(f"{where}: GitHub finds no license in the repository")

        mods.append({
            "id": mid,
            "name": manifest.get("name") or mid,
            "author": manifest.get("author") or info["owner"]["login"],
            "description": desc,
            "tags": entry.get("tags", []),
            "save": entry.get("save"),
            "version": want,
            "loader": loader,
            "dependencies": manifest.get("dependencies", []),
            "loadAfter": manifest.get("loadAfter", []),
            "loadBefore": manifest.get("loadBefore", []),
            "conflicts": manifest.get("conflicts", []),
            "license": lic,
            "repo": info["html_url"],
            "tag": tag,
            "published": day(rel.get("published_at")),
            "zip": zfile,
        })

    for m in mods:
        for dep in m["dependencies"]:
            if dep not in ids:
                problems.append(f"{m['id']}: depends on {dep}, which is not listed")

    if problems:
        raise Problems(problems)
    catalog = {
        "$schema": SCHEMA_URL,
        "format": 1,
        "generated": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d"),
    }
    if manager:
        catalog["manager"] = manager
    catalog["engine"] = engine
    catalog["mods"] = mods
    return catalog


def write(catalog, out):
    tmp = out + ".tmp"
    with open(tmp, "w", encoding="utf-8", newline="\n") as f:
        json.dump(catalog, f, indent=2, ensure_ascii=False)
        f.write("\n")
    os.replace(tmp, out)


# ---------- Checking ----------

def validate(value, schema, root, path, problems):
    """value against the parts of JSON Schema that catalog.schema.json uses."""
    if "$ref" in schema:
        ref = schema["$ref"]
        target = root
        for part in ref.lstrip("#/").split("/"):
            target = target[part]
        merged = dict(target)
        merged.update({k: v for k, v in schema.items() if k != "$ref"})
        schema = merged
    t = schema.get("type")
    types = {"object": dict, "array": list, "string": str, "integer": int}
    if t and not isinstance(value, types[t]) or (t == "integer" and isinstance(value, bool)):
        problems.append(f"{path}: expected {t}")
        return
    if "const" in schema and value != schema["const"]:
        problems.append(f"{path}: expected {schema['const']!r}")
    if "enum" in schema and value not in schema["enum"]:
        problems.append(f"{path}: {value!r} is not one of {schema['enum']}")
    if isinstance(value, str):
        if "pattern" in schema and not re.search(schema["pattern"], value):
            problems.append(f"{path}: {value!r} does not match {schema['pattern']}")
        if len(value) < schema.get("minLength", 0):
            problems.append(f"{path}: too short")
    if isinstance(value, int) and "minimum" in schema and value < schema["minimum"]:
        problems.append(f"{path}: below {schema['minimum']}")
    if isinstance(value, dict):
        for key in schema.get("required", []):
            if key not in value:
                problems.append(f"{path}: missing {key}")
        props = schema.get("properties", {})
        for key, sub in value.items():
            if key in props:
                validate(sub, props[key], root, f"{path}.{key}", problems)
            elif schema.get("additionalProperties") is False:
                problems.append(f"{path}: unknown field {key}")
    if isinstance(value, list):
        if len(value) < schema.get("minItems", 0):
            problems.append(f"{path}: fewer than {schema['minItems']} items")
        if schema.get("uniqueItems") and len({json.dumps(v, sort_keys=True) for v in value}) != len(value):
            problems.append(f"{path}: repeated items")
        if "items" in schema:
            for i, sub in enumerate(value):
                validate(sub, schema["items"], root, f"{path}[{i}]", problems)


def check(listed, catalog):
    problems = []
    schema = load_json(SCHEMA)
    validate(catalog, schema, schema, "mods.json", problems)
    if problems:
        return problems
    if listed.get("manager") and not catalog.get("manager"):
        problems.append("manager: listed, not in mods.json (run npm run catalog)")
    if catalog.get("manager") and not listed.get("manager"):
        problems.append("manager: in mods.json, not listed")
    by_repo = {m["repo"].lower().replace("https://github.com/", ""): m for m in catalog["mods"]}
    seen = set()
    for entry in listed.get("mods", []):
        repo = entry.get("repo", "").lower()
        m = by_repo.get(repo)
        if not m:
            problems.append(f"{entry.get('repo')}: listed, not in mods.json (run npm run catalog)")
            continue
        seen.add(repo)
        if m["version"] != entry.get("version"):
            problems.append(f"{m['id']}: listed at {entry.get('version')}, mods.json has {m['version']} (run npm run catalog)")
        if m["tags"] != entry.get("tags") or m["save"] != entry.get("save"):
            problems.append(f"{m['id']}: tags or save note differ from listed.json (run npm run catalog)")
    for repo, m in by_repo.items():
        if repo not in seen:
            problems.append(f"{m['id']}: in mods.json, not listed")
    ids = [m["id"] for m in catalog["mods"]]
    if len(set(ids)) != len(ids):
        problems.append("mods.json: two mods share an id")
    return problems


def main(argv):
    ap = argparse.ArgumentParser(description="Write or check the mods' catalog (docs/public/mods.json).")
    ap.add_argument("--check", action="store_true", help="check mods.json offline; write nothing")
    ap.add_argument("--listed", default=LISTED, help="the list of listed mods (catalog/listed.json)")
    ap.add_argument("--out", default=OUT, help="the catalog to write or check (docs/public/mods.json)")
    args = ap.parse_args(argv)
    listed = load_json(args.listed)

    if args.check:
        if not os.path.isfile(args.out):
            print(f"catalog: {args.out} is missing (run npm run catalog)")
            return 1
        problems = check(listed, load_json(args.out))
        for p in problems:
            print("catalog: " + p)
        if problems:
            return 1
        print(f"catalog: mods.json matches listed.json ({len(listed.get('mods', []))} mods)")
        return 0

    tok = token()
    if not tok:
        print("catalog: no GitHub token (GH_TOKEN, GITHUB_TOKEN or gh auth login); trying without one")
    gh = GitHub(tok)
    try:
        catalog = build(listed, gh)
    except Problems as e:
        for p in e.args[0]:
            print("catalog: " + p)
        print(f"catalog: nothing written ({len(e.args[0])} problem(s), {gh.calls} GitHub calls)")
        return 1
    problems = check(listed, catalog)
    if problems:
        for p in problems:
            print("catalog: " + p)
        return 1
    write(catalog, args.out)
    mgr = f", RQ Manager {catalog['manager']['version']}" if catalog.get("manager") else ""
    print(f"catalog: RQ MOD {catalog['engine']['version']}{mgr} and {len(catalog['mods'])} mods written to "
          f"{os.path.relpath(args.out, ROOT)} ({gh.calls} GitHub calls)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
