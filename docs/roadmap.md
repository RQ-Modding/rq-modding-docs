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

### Next

In order of priority: what the mods that exist today would use.

| Area | What |
| --- | --- |
| Screens | Since 2.20.1 `rq.ui` lists the footer on every screen that shows it, Rance Castle as the screen `castle` with its rooms, and the town tabs on Quests; since 2.31.0 the Party screen's 2nd Army box (its characters, their STATUS buttons and the places a dragged character is dropped on). When a mod asks: names for Trivia, CG mode, Music mode and the castle's bonus rooms, and the castle's rooms as data in `rq.ui.get`. |
| Battle events | Calls for the places mods hook through `rq.ain` today: each line of the battle log, the speeds the turn order is built from, the stun roll, and whether TADA mode is on. |

### Later

When a mod asks for it, or at low priority.

| Area | What |
| --- | --- |
| Faces and pictures | Moving faces, standing pictures and backgrounds, and pictures inside the game's Flash files (cut-ins, effects, marks), came in 2.25.0 ([Pictures](guide/pictures.md)). Later: enemies and fight backgrounds (3D models, their textures), moving pictures inside Flash files, a different face per place (as `rq.battle.set_face` does for fights), moving faces where the game paints them into another picture (the turn order). |
| States | States made by mods came in 2.2.0 (`rq.status`), on the events of 2.1.0; in 2.3.0 a state can down someone at the start of a turn; in 2.26.0 the game's cures and dispels take them, each shows its own number, Persevere, the AUTO button and the battle forecast know them, special skills reach `on_hit`, `immune`, states that last the quest and a `desc` (see [Battle states](guide/states.md)). Later, at low priority: the `desc` on hover with the card's marks side by side. When a mod asks: states kept in the save, the enemies' AI choosing by mod states, states shown between fights, AUTO for a mod's own cure skill. |
| Dialogs | The game's dialogs over Config came in 2.28.0, with "don't ask again" on `rq.ui.ask`. Later: `rq.ui.choose` over Config (it waits for Config to close), when a mod wants a menu from its page. |
| Buff icons | Low priority: several buffs on one card shown side by side, shrunk to fit, instead of taking turns (fading in and out works well today). |
| Music | Music from a mod file came in 2.4.0 (`rq.music`); in 2.27.0 `on_play` tells boss fights, the town, the castle, the opening, the results, the jingle and scenes (with the scene's name) apart, and a pack gets a Config page to turn its tracks on and off (see [Replacing music](guide/music.md)). Not planned: tracks with new numbers (a file for any moment needs none). |
| Quests | Taking a quest from the list came in 2.23.0 (`rq.quests.on_take`, `can_take`, `refresh`), with the game data of three shipped mods (items by place, the world transfer, donations, the Morurun's absorbed items). Later: `rq.quests.start` from the shop, party and castle tabs, not only the hub and the quest list. |
| Dungeon camera | Since 2.30.0 `rq.dungeon.camera` can be called again, as from `rq.dungeon.on_map` for a range per map, and moves the 3D view's cut (`far`). Later: the sky backdrop under outdoor maps, whose edge shows as black corners when the camera is far out, and setting the zoom distance the game keeps, so a mod can put it back after a cave. |
| Equipment | Changing a base-game character's equipment, with a choice to overwrite what they wear (today a replaced weapon goes to the vault). |
| Sprites | Clicks on sprites; attaching a sprite to a part of the game's interface; following a target's scale and rotation. |
| UI kit | The hub's widgets and the game's own pieces shipped from 2.5.0 to 2.29.0 (see the [Changelog](changelog.md)): the game's font, buttons, rows, lists and scroll bars, menus, the vault's and shop's item lists, the keys between widgets, comment windows, bars and digits, skill and item tiles, the game's dialogs, buttons in the game's own menus, number fields, text fields that agents can type into (2.29.0). When a mod asks: in a text field, a selection with copy and cut, several lines, a hidden (password) look, an input method's unfinished text shown in the field, accented letters (the game's font has none, so the field keeps none today), a field as wide as its row, and a ready-made name prompt; the mini skill tiles, dragging an item tile onto an equip slot, switching the status page to another character from a mod, the main minus key, the message window for a mod's page, the frames round bars and digits, an icon button, Frostbuy's racks as a group, a greyed entry and more than 20 entries in the MODS list, a MODS list on the status page for a third mod, a way in to a mod's castle room while the castle is being cleaned. At low priority: a key for the Mods tab. |
| Animation | Animated WebP, with full color and soft edges, came in 2.25.0 for pictures on CG numbers. Later: PNG sequences, and WebP for `rq.image.add_gif` and `rq.sprite`. |
| Game code | `rq.ain.call` and `rq.ain.method` with reference and struct arguments (methods with plain arguments came in 2.16.0, `rq.ain.method`). |
| Sound | Compressed sounds inside Flash files. |
| Lua state | A tail call (`return rq.ui.confirm(...)`) keeps the mod on the stack since 2.24.1 ([Which mod is calling](guide/sandbox.md#which-mod-is-calling)). Later: changes to the shared `rq` and standard library tables, a log line also for changes made in callbacks, and refusing such changes if mods turn out to make them. 2.0.0 logs the ones each `init.lua` makes ([What a mod can reach](guide/sandbox.md#globals)). |

## Tools

- **Animations from your own art.** A tool that builds the game's animation files (`.aff`) from a PNG
  sequence and checks a Flash file against what the engine can play. Unpacking the game's own came in
  2.25.0: `rqmod-ctl flashdump` saves a file's pictures.
- **A browser for the game's files.** Once the API is ready for release: a program in the release that
  opens the game's pictures, sounds, Flash files and 3D textures by number or by name, with the names
  of `rq.ids`, so you can see what CG 10023 is before you replace it. It reads your own game folder;
  nothing of the game ships with it.
