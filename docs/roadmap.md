# Roadmap

What is planned or wanted for RQ MOD and its API, in no fixed order. Nothing here has a date. When an
item ships, it moves to the [Changelog](changelog.md).

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

| Area | What |
| --- | --- |
| Lua state | A `require` cache per mod by default, so two mods with a `util.lua` do not meet, and an explicit way for library mods to share code and data with the mods that depend on them. Today mods share one Lua state ([What a mod can reach](guide/sandbox.md#require)). |
| Quests | `rq.quests.start` from the shop, party and castle tabs, not only the hub and the quest list. |
| Game code | `rq.ain.call` with reference and struct arguments, and methods. |
| Sprites | Clicks on sprites; attaching a sprite to a part of the game's interface; following a target's scale and rotation. |
| Faces and pictures | Enemy pictures, and faces in skill cut-ins, big pictures and the status pages. Animated faces, portraits and backgrounds. |
| Animation | Sources with full color and soft edges (PNG sequences, animated WebP) beside GIF. |
| Sound | Music from a mod file in place of the game's; compressed sounds inside Flash files. |
| UI kit | More of the game's own UI beyond Config (message and help windows, skill and item buttons, lists, scrollbars, number fonts, gauges); arrow-key moves between kit widgets; a key for the Mods tab; lists inside a mod's own clip. |
| States | States made by mods, such as a burn, that live beside the game's own. |

## Tools

- **Animations from your own art.** A tool that builds the game's animation files (`.aff`) from a PNG
  sequence, checks a Flash file against what the engine can play, and unpacks the game's own.
