# Roadmap

What is planned or wanted for RQ MOD and its API. Nothing here has a date. When an item ships, it
moves to the [Changelog](changelog.md).

## Planned

- **More names.** `rq.ids` (1.15.0) names characters, classes, items, quests, skills and states.
  1.16.0 adds monsters, races, character types, elements, item kinds and skill targets. Still to
  come: maps and dungeons (the game names them per quest and floor, not per map), and, when the API
  takes their numbers, traps, chest contents, directions, battle results and music.
- **A mod template.** A repository to start a mod from: `mod.json` with its schema, `init.lua`,
  editor settings for `rq.lua`, a README, a changelog, a license, and a workflow that zips a release.
- **One page of docs in the release.** The API reference as one HTML file inside the release zip, for
  reading offline.

## Wanted in the API

In order of priority: first what the most mods, existing or new, would use.

| Area | What |
| --- | --- |
| States | States made by mods came in 2.2.0 (`rq.status`), on the events of 2.1.0, and in 2.3.0 a state can down someone at the start of a turn when its definition says so. Later: a damage number per state, the AI's cures and the battle forecast knowing them, the game's buff dispels taking good states. |
| Music | Music from a mod file in place of the game's, for soundtrack replacements and music per quest or fight. |
| UI kit | More of the game's own UI beyond Config (message and help windows, skill and item buttons, lists, scrollbars, number fonts, gauges); arrow-key moves between kit widgets; a key for the Mods tab; lists inside a mod's own clip. |
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
| Sound | Compressed sounds inside Flash files. |

## Tools

- **Animations from your own art.** A tool that builds the game's animation files (`.aff`) from a PNG
  sequence, checks a Flash file against what the engine can play, and unpacks the game's own.
