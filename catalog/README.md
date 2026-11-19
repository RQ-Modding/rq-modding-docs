# The mods' catalog

`listed.json` names the mods the site lists, each at the release that was checked. From it,
`scripts/catalog.py` writes `docs/public/mods.json`, which the Download and Mods pages are built from
and RQ Manager reads. Its format is `docs/public/schemas/catalog.schema.json`.

## An entry

```json
{ "repo": "RQ-Modding/binoculars", "version": "1.2.4", "tags": ["items", "dungeons"], "save": "stays" }
```

| Field | What |
| --- | --- |
| `repo` | The mod's public GitHub repository, `owner/name`. |
| `version` | The checked version: `mod.json`'s at the release's tag. |
| `tags` | One or more of `characters`, `skills`, `items`, `battle`, `dungeons`, `quests`, `shops`, `interface`, `modes`, `saves`, `fixes`. |
| `save` | `none`: removing the mod leaves the game's save as the game expects it. `stays`: the save keeps things the mod made, or removing it changes the save (the README's Saves section says how). |
| `tag` | Optional: the release's tag when it is not `v<version>`. |
| `asset` | Optional: the zip's name when the release has more than one. |
| `description` | Optional: the description to show when the repository's own does not fit. |

The name, author, `loader`, dependencies and conflicts come from `mod.json` at the tag, the
description and license from the repository.

At the top of `listed.json`, `engine` names RQ MOD's repository, and `manager` RQ Manager's (since
its first release, 1.0.0; without it `mods.json` has no `manager` entry and the Download page does
not name the Manager). The script takes each one's latest release and checks its zip: RQ MOD's holds
`xsystem4/xsystem4.exe`, RQ Manager's `RQ Manager/rq-manager.exe`. A newer release of either needs
only `npm run catalog`.

## Listing a mod, or a newer version

1. Check it: the code read, the game started with it (the Lab's `smoke`), and for RQ Modding's mods
   `check-release.ps1 -Mod <id>`.
2. Add or change its entry here.
3. `npm run catalog`. It asks GitHub for every release, downloads every zip and checks it, and writes
   `mods.json` only when all is right. It needs a GitHub token: `GH_TOKEN`, `GITHUB_TOKEN`, or
   `gh auth login`.
4. Commit `listed.json` and `mods.json` together.

`npm run catalog -- --check` checks `mods.json` against `listed.json` and the schema with no network;
the deploy runs it before the build.
