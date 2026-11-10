# Roadmap

What is planned or wanted for RQ MOD and its API. Nothing here has a date. When an item ships, it
moves to the [Changelog](changelog.md).

## Planned

- **More names.** `rq.ids` (1.15.0) names characters, classes, items, quests, skills and states.
  1.16.0 adds monsters, races, character types, elements, item kinds and skill targets, 2.4.0
  music tracks, and 2.24.0 map kinds. Still to come: map layouts (many layouts carry several areas'
  names, so a quest and an area are the stable key), and, when the API takes their numbers, traps,
  chest contents, directions and battle results.
- **A mod template.** A repository to start a mod from: `mod.json` with its schema, `init.lua`,
  editor settings for `rq.lua`, a README, a changelog, a license, and a workflow that zips a release.
- **One page of docs in the release.** The API reference as one HTML file inside the release zip, for
  reading offline.

## Wanted in the API

In order of priority: first what the most mods, existing or new, would use.

| Area | What |
| --- | --- |
| Lua state | `rq.mod.id` seeing the mod through a tail call (`return rq.ui.confirm(...)`), so its entries are not filed under `_`. Later: changes to the shared `rq` and standard library tables, a log line also for changes made in callbacks, and refusing such changes if mods turn out to make them. 2.0.0 logs the ones each `init.lua` makes ([What a mod can reach](guide/sandbox.md#globals)). |
| Faces and pictures | Enemy pictures, and faces in skill cut-ins, big pictures and the status pages. Animated faces, portraits and backgrounds. |
| States | States made by mods came in 2.2.0 (`rq.status`), on the events of 2.1.0, and in 2.3.0 a state can down someone at the start of a turn when its definition says so. Later: the game's cures and buff dispels taking mod states, a damage number per state, the AI's cures and the battle forecast knowing them, a help text on hover, states that last past a fight. |
| Buff icons | Several buffs on one card shown side by side, shrunk to fit, instead of taking turns. |
| Music | Music from a mod file came in 2.4.0 (`rq.music`). Later: more kinds of moment than fight and dungeon (boss, town, scene), `on_play` for the looped ambient sounds, a page to turn a pack's tracks on and off, tracks with new numbers. |
| Quests | Taking a quest from the list came in 2.23.0 (`rq.quests.on_take`, `can_take`, `refresh`), with the game data of three shipped mods (items by place, the world transfer, donations, the Morurun's absorbed items). Later: `rq.quests.start` from the shop, party and castle tabs, not only the hub and the quest list. |
| Equipment | Changing a base-game character's equipment, with a choice to overwrite what they wear (today a replaced weapon goes to the vault). |
| Sprites | Clicks on sprites; attaching a sprite to a part of the game's interface; following a target's scale and rotation. |
| UI kit | The hub's widgets and the game's own pieces shipped from 2.5.0 to 2.22.0 (see the [Changelog](changelog.md)): the game's font, buttons, rows, lists and scroll bars, menus, the vault's and shop's item lists, the keys between widgets, comment windows, bars and digits, skill and item tiles, the game's dialogs, buttons in the game's own menus, number fields. Next: the mini skill tiles, a key for the Mods tab, the game's dialogs over Config, "don't ask again" on `rq.ui.ask`, dragging an item tile onto an equip slot, switching the status page to another character from a mod. When a mod asks: a text field agents can type into, the main minus key, the message window for a mod's page, the frames round bars and digits, an icon button, Frostbuy's racks as a group, a greyed entry and more than 20 entries in the MODS list, a MODS list on the status page for a third mod, a way in to a mod's castle room while the castle is being cleaned. |
| Screens | Since 2.20.1 `rq.ui` lists the footer on every screen that shows it, Rance Castle as the screen `castle` with its rooms, and the town tabs on Quests. Later, when asked: names for Trivia, CG mode, Music mode and the castle's bonus rooms, the castle's rooms as data in `rq.ui.get`, and the Party screen's 2nd Army box (its characters and their STATUS buttons). |
| Animation | Sources with full color and soft edges (PNG sequences, animated WebP) beside GIF. |
| Game code | `rq.ain.call` and `rq.ain.method` with reference and struct arguments (methods with plain arguments came in 2.16.0, `rq.ain.method`). |
| Sound | Compressed sounds inside Flash files. |

## Tools

- **Animations from your own art.** A tool that builds the game's animation files (`.aff`) from a PNG
  sequence, checks a Flash file against what the engine can play, and unpacks the game's own.
