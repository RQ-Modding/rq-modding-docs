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

A template repository for new mods, with a release workflow that zips the folder, is planned (see the
[Roadmap](../roadmap.md)).
