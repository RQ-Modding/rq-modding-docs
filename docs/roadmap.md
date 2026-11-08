# Roadmap

What is planned or wanted for RQ MOD and its API. Nothing here has a date. When an item ships, it
moves to the [Changelog](changelog.md).

## Planned

- **More names.** `rq.ids` (1.15.0) names characters, classes, items, quests, skills and states.
  1.16.0 adds monsters, races, character types, elements, item kinds and skill targets, and 2.4.0
  music tracks. Still to come: maps and dungeons (the game names them per quest and floor, not per
  map), and, when the API takes their numbers, traps, chest contents, directions and battle results.
- **A mod template.** A repository to start a mod from: `mod.json` with its schema, `init.lua`,
  editor settings for `rq.lua`, a README, a changelog, a license, and a workflow that zips a release.
- **One page of docs in the release.** The API reference as one HTML file inside the release zip, for
  reading offline.

## Wanted in the API

In order of priority: first what the most mods, existing or new, would use.

| Area | What |
| --- | --- |
| States | States made by mods came in 2.2.0 (`rq.status`), on the events of 2.1.0, and in 2.3.0 a state can down someone at the start of a turn when its definition says so. Later: a damage number per state, the AI's cures and the battle forecast knowing them, the game's buff dispels taking good states. |
| UI kit | The hub's widgets, in four steps. 2.5.0 brought the game's own font for mod text and clips inside clips; 2.6.0 the hub's grey buttons, Rance Castle's rows, the quest list with the game's scroll bar, the town tabs, Frostbuy's rack tiles, the sort column and a page over the hub; 2.7.0 the game's choice menu opened from the hub (`rq.ui.choose`) and its look inside a page (`rq.uikit.options`); 2.8.0 the vault's item rows and lists in the vault and storage styles, its filter column and sub-filters, its sorts and counters, and an item picker; 2.9.0 the shop's and a character's item lists, keys in lists and menus, dragging between the storage and the vault, and calls to lock, sell, donate and store an item (`rq.item`); 2.10.0 buying from the shop (`rq.item.buy`), selling worn gear, the game's SORT in every list, filters on the storage screen, scroll arrows that repeat while held, and menus that scroll; 2.11.0 a top layer over the HUD for dragged icons, comments and tooltips (`rq.hud.top`), the game's faint text shadows, and agents that click as a player does under mod widgets; 2.12.0 the arrow keys and Enter between kit widgets, as the game's screens move their cursor, with Config's Mods tab in the tab row's arrows. Planned, high priority: mod buttons inside the game's own button groups, so mods like potential-skill-pages need no C of their own. Later: message and help windows, gauges, a key for the Mods tab. |
| Faces and pictures | Enemy pictures, and faces in skill cut-ins, big pictures and the status pages. Animated faces, portraits and backgrounds. |
| Dungeons | Which dungeon and floor `rq.dungeon.on_map` is on, so a mod can act per dungeon, and then names for them in `rq.ids`. |
| Buff icons | Several buffs on one card shown side by side, shrunk to fit, instead of taking turns. |
| Sprites | Clicks on sprites; attaching a sprite to a part of the game's interface; following a target's scale and rotation. |
| Quests | `rq.quests.start` from the shop, party and castle tabs, not only the hub and the quest list. |
| Equipment | Changing a base-game character's equipment, with a choice to overwrite what they wear (today a replaced weapon goes to the vault). |
| Screens | A screen name and controls for the town's Rance Castle tab in `rq.ui`. |
| Animation | Sources with full color and soft edges (PNG sequences, animated WebP) beside GIF. |
| Game code | `rq.ain.call` with reference and struct arguments, and methods. |
| Lua state | Changes to the shared `rq` and standard library tables: a log line also for changes made in callbacks, and refusing such changes if mods turn out to make them. 2.0.0 logs the ones each `init.lua` makes ([What a mod can reach](guide/sandbox.md#globals)). |
| Music | Music from a mod file came in 2.4.0 (`rq.music`). Later: tracks with new numbers, `on_play` for the looped ambient sounds, more kinds of moment than fight and dungeon. |
| Sound | Compressed sounds inside Flash files. |

## Tools

- **Animations from your own art.** A tool that builds the game's animation files (`.aff`) from a PNG
  sequence, checks a Flash file against what the engine can play, and unpacks the game's own.
