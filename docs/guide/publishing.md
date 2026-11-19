# Sharing a mod

A mod is its folder. To share it, zip the folder so that the zip holds the folder itself
(`hello-mod/mod.json`, `hello-mod/init.lua`, ...), and players extract it into `mods`.

## Before you share

- **`id`** is final. Saves keep `rq.savedata` and `rq.store` data under it, and other mods name it
  in their lists.
  Text ids (`"hellomod:lens"`) are final too: a save holds the numbers they turn into.
- **`loader`** is the lowest RQ MOD version that has every call you use. Each entry in the
  [API reference](../reference/index.md) shows when it was added and changed.
- **`version`** goes up with every release, so players and bug reports can tell them apart.
- **A README** for players: what the mod does, its keys and settings, and what it changes in a save.
- **A license.** Without one, others may not reuse your code. The RQ Modding mods use MIT. Code examples from these docs are public domain (CC0), so they can go
  into a mod under any license.

Only files in the mod's folder are reachable from its Lua, so ship everything it reads (images,
sounds, data) inside the folder.

## Changes to a save

Say in the README when the mod writes to the save: characters it recruits, items it gives, quests it
unlocks. Those stay in the save after the mod is removed. Values in `rq.savedata` stay in a file
beside each save (`RanceQuestMagnum_030.rqmod.json`) and those in `rq.store` in `rqmod-store.json`
in the save profile; the game ignores both without the mod, and the loader keeps a removed mod's
`rq.savedata` in case it comes back.

## Testing

Test with a copy of your save, and with the other mods you expect players to run. Check
`logs\rqmod.log` for errors from your mod. When you change an `on_*` callback that other mods also
use (a skill's text, damage, a shop's stock), test it with those mods too, since load order decides
who runs last.

## Start from the template

The [mod template](https://github.com/RQ-Modding/rq-mod-template) is a repository to start a mod
from. **Use this template** on GitHub makes a repository of your own with `mod.json` (with its
schema, so the editor completes and checks it), `init.lua`, editor settings for `rq.lua`, a README
for players, `TESTING.md` for testers, a changelog and the MIT license. Its README lists what to
fill in.

It has a release workflow too. Raise `version` in `mod.json`, add its section to `CHANGELOG.md`,
commit, then push a tag with the same version:

```sh
git tag v1.0.0
git push origin v1.0.0
```

The workflow checks the tag against `mod.json`, zips the folder as above (`<id>-1.0.0.zip`, holding
`<id>/mod.json`, `<id>/init.lua`, ...) and publishes it as a GitHub release, with that version's
section of the changelog as its notes.

## Getting your mod listed

The [Mods](../mods.md) page lists the mods we checked, each at the version we checked. To ask for
yours, open a [List a mod](https://github.com/RQ-Modding/rq-modding-docs/issues/new?template=list-a-mod.yml)
issue in the docs' repository, with:

- a public repository with a license that lets players share it;
- a GitHub release whose one zip holds the mod's folder (`<id>/mod.json`, `<id>/init.lua`, ...), as
  the template's release workflow makes it;
- a `loader` in `mod.json` no newer than RQ MOD's latest release, and every dependency already on
  the Mods page;
- a one-line description of the repository, which the page shows;
- a README that says what the mod changes and, under **Saves**, what stays in a save after it is
  removed.

Before a mod is listed, we read its code (a mod can change the save and the game's code), start the
game with it, and check that its zip is the one GitHub published. The page shows that release. Each
newer release gets the same check before the page moves to it, so open the issue again (or comment
on it) when you release a version you want listed.
