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
| UI kit | The hub's widgets, in four steps. 2.5.0 brought the game's own font for mod text and clips inside clips; 2.6.0 the hub's grey buttons, Rance Castle's rows, the quest list with the game's scroll bar, the town tabs, Frostbuy's rack tiles, the sort column and a page over the hub; 2.7.0 the game's choice menu opened from the hub (`rq.ui.choose`) and its look inside a page (`rq.uikit.options`); 2.8.0 the vault's item rows and lists in the vault and storage styles, its filter column and sub-filters, its sorts and counters, and an item picker; 2.9.0 the shop's and a character's item lists, keys in lists and menus, dragging between the storage and the vault, and calls to lock, sell, donate and store an item (`rq.item`); 2.10.0 buying from the shop (`rq.item.buy`), selling worn gear, the game's SORT in every list, filters on the storage screen, scroll arrows that repeat while held, and menus that scroll; 2.11.0 a top layer over the HUD for dragged icons, comments and tooltips (`rq.hud.top`), the game's faint text shadows, and agents that click as a player does under mod widgets; 2.12.0 the arrow keys and Enter between kit widgets, as the game's screens move their cursor, with Config's Mods tab in the tab row's arrows; 2.13.0 the game's comment window and a tip on every widget; 2.14.0 the game's bars and digit fonts; 2.15.0 the skill tile of the status page; 2.16.0 a way in to a mod from the game's own menus, the SYSTEM menu's MODS row (`rq.gamebutton`) and a mod's room in Rance Castle (`rq.castle.room`); 2.17.0 buttons under the skill window's list (`rq.gamebutton`'s `"skill-window"`), which Potential Skill Pages' Previous / Next now are. Planned next: the rest of the skill list's paging in Lua (the longer list, the page's slice), so potential-skill-pages needs no C of its own. When a mod asks: the status page's button row and Frostbuy's racks as groups, a greyed entry and more than 20 entries in the MODS list. Later: the mini skill tiles, item tiles and the item card, a key for the Mods tab. When a mod asks: the message window for a mod's page, the frames round bars and digits. |
| Faces and pictures | Enemy pictures, and faces in skill cut-ins, big pictures and the status pages. Animated faces, portraits and backgrounds. |
| Dungeons | Which dungeon and floor `rq.dungeon.on_map` is on, so a mod can act per dungeon, and then names for them in `rq.ids`. |
| Buff icons | Several buffs on one card shown side by side, shrunk to fit, instead of taking turns. |
| Sprites | Clicks on sprites; attaching a sprite to a part of the game's interface; following a target's scale and rotation. |
| Quests | `rq.quests.start` from the shop, party and castle tabs, not only the hub and the quest list. An event when the player takes a quest from the list, before the autosave, that can cancel it (`rq.quests.on_take`); the list's buttons drawn again after a change. `rq.quests.set_state(no, 1)` on a quest that is not locked does nothing today (the game's rule): the reference should say so, or the call should write it. |
| Equipment | Changing a base-game character's equipment, with a choice to overwrite what they wear (today a replaced weapon goes to the vault). |
| Screens | A screen name and controls for the town's Rance Castle tab in `rq.ui`, and the footer's buttons (SYSTEM, Vault, Trivia) listed on a quest's map too. The status page for mods: the character shown (`rq.ui.get().status.chara` is 0 today, a bug), a refresh of the card after a change, an event when it opens or changes character. The game's Yes/No and OK dialogs as calls (`rq.ui.confirm`, `rq.ui.notice`). |
| Characters | The items the Morurun absorbed: read the five slots and change one with the game's rules (`rq.chara.absorbed`, `set_absorbed`). |
| Items | An item's row data (name, icon, stats line) from its number, with no instance. An icon button in the kit (`rq.uikit.button` with a CG). An item number's instances by place (`rq.item.find`, `rq.item.count`). The game's dialog with any number of choices (`rq.ui.menu`). |
| World and shop | An event before and after a world transfer, with the old and new world (`rq.world.on_transfer`), and the current world (`rq.world.current`). The donations count and Frostbuy's reward goal as calls (`rq.shop.donations`, `set_donations`, `goal`, `set_goal`). |
| Animation | Sources with full color and soft edges (PNG sequences, animated WebP) beside GIF. |
| Game code | `rq.ain.call` and `rq.ain.method` with reference and struct arguments (methods with plain arguments came in 2.16.0, `rq.ain.method`). |
| Lua state | Changes to the shared `rq` and standard library tables: a log line also for changes made in callbacks, and refusing such changes if mods turn out to make them. 2.0.0 logs the ones each `init.lua` makes ([What a mod can reach](guide/sandbox.md#globals)). |
| Music | Music from a mod file came in 2.4.0 (`rq.music`). Later: tracks with new numbers, `on_play` for the looped ambient sounds, more kinds of moment than fight and dungeon. |
| Sound | Compressed sounds inside Flash files. |

## Tools

- **Animations from your own art.** A tool that builds the game's animation files (`.aff`) from a PNG
  sequence, checks a Flash file against what the engine can play, and unpacks the game's own.
