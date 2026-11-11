<!-- Copied from the engine's CHANGELOG.md by scripts/sync.py. Edit it there. -->

# Changelog

Each version is the loader version mods see as `rq.version` and declare as `loader` in `mod.json`.
A patch version fixes or adjusts behavior, a minor version adds calls or fields, a major version removes, renames or changes the meaning of a call.

## 2.32.0

The map panel and the game's windows (`notes/plans/plan-map-panel-windows.md` in the workspace, phase F of the priority order).
- `rq.gamebutton`'s group `"map"`: tabs on a quest's map, on the 3D view's right edge against the map panel, under the area map and above the Magnum gauge. Up to four, 40 × 44 at x 768 from y 129, 47 apart; a fifth shown entry is not placed and the log says so. Each tab is a button of the panel itself (`T_MapParts`, ids 700101 to 700104), the game's plain grey bar (CG 11009) with the entry's `icon`, so it hides with the panel in a dialog, a fight or an event, and the panel makes it again for each area. `shown` and `enabled` are asked every 200 ms while the map shows, `tip` (a text or a function) is the game's comment window left of the tab, and in the map's key mode (Space) the arrow keys reach the tabs (Left from AREA DISPLAY, Up and Down between them, Right back, Enter). Agents see each tab as `<mod id>.<id>` with its `button` while the map takes input, and `rq.gamebutton.groups` lists the group as `map`.
- `rq.uikit.item_window(items, opts)`: the game's Quest Storage window (CG 11335) holding item tiles (`rq.uikit.item_icon`, the item card as tip), at the game's place (473, 165). Rows of five, 1 to 5 (`rows`; default 3, or 4 with more than 15 items), cut from the game's CG; with more items than fit, page arrows and the page's number in the band. A `title` in the band, an `empty` text, a `cell` callback to draw marks on a tile, and entries with `judged`, `tip` and `disabled`. Modal as a page; it closes by its close button, a right click or Esc. Returns open and the index clicked. In `src/lua/uikit_windows.lua`.
- `rq.uikit.section(text, opts)`: a heading in the quest panel's look (CG 11014: the ★, the band, the gold stripes), the text in the game's font in the heading's gold, sized down to fit, with an optional box under it (`box`, a height). Returns the box's place.
- `rq.uikit.balloon(text, opts)`: text in Frostbuy's speech balloon (CG 11110), wrapped and grown to the text, with the tail where `tail_x` puts it or none (`tail = false`). The tail is not mirrored.
- `rq.uikit.page` takes `style = "parchment"`: Trivia's paper (CG 20001, 700 × 536 at 162, 56 by default, the vines kept and the middle cut), the title and the labels inside in the paper's brown.
- The hub theme has `item_window`, `section`, `balloon` and `parchment`.
- Loot Preview 1.2.0: the Item Previews button over the encounter bar is gone; a `"map"` tab with the game's pouch opens the items in `rq.uikit.item_window`, with a fourth row past 15 items and pages past 20. Game Speed 1.2.1 (no loader change): on a quest's map the F8 note shows under the encounter bar, centered on the 3D view.

## 2.31.0

The Lab and its scripts (`notes/plans/plan-lab-scripts.md` in the workspace, phase D of the priority order).
- `rq.ui.get` and `rqmod-ctl ui` list the Party screen's 2nd Army box while it is open: its cards as `store-N` (N from 0 after the box's scroll), the STATUS of the card under the mouse as `store-status-N`, its close as `store-close`, all in section `party-store`, and the places a dragged character is dropped on, `store-drop` (the box) and `grid-drop` (the grid). `storeUnits` lists the whole 2nd Army as `units` lists the roster, and `storeState` has `topIndex`, `listCount` and `shown`. Agents found the box only by coordinates.
- The stall watch: when `rq.on_frame` has not started for 10 s while the game still pumps its events (its update does not run, or a callback has not returned), the log gets one line with how long, the callback that runs and the mod that registered it, and the AIN call stack; and one line when it runs again. A pause (`rqmod-ctl pause`) does not count. `rqmod-ctl where` writes the same numbers at the top of its file.

## 2.30.0

Phase C of the priority order (`notes/plans/plan-morurun-camera.md` in the workspace).
- `rq.dungeon.camera` can be called again, as from `rq.dungeon.on_map` for a range per map. It found its places by the game's numbers (35, 60, 80), which its first call replaced, so a second call changed nothing in the clamp, the fog or the slider, and put the wheel's step in a second time (the wheel then zoomed by the step times itself). The first call now records where it wrote, and a later call writes the new numbers there. A field left out takes its default again.
- `rq.dungeon.camera`'s new field `far`: where the 3D view is cut (the game's 200, in `CMapMode@Clear`, which each map's `Create` runs). Past a `max` of about 120 the cut at 200 shows black at the top of an outdoor map, and past about 170 it loses the far rows of ground; at 400 the ground stays whole at 180. More than 5 (the near cut), or an error.
- The reference says that the game keeps one zoom distance for every map and clamps it to the range when a map opens, what the cut does, and that the sky backdrop under outdoor maps is a plane of fixed size whose edge can show.
- Camera Zoom 1.1.0: outdoors (eight kinds of area), a zoom out to 150 with the view cut at 400, set in `on_map` by the area's kind. Morurun Items 1.3.0 (no loader change): an empty slot a Morurun opened can absorb a special item.

## 2.29.0

The text field (`notes/plans/plan-text-field.md` in the workspace, phase B of the priority order).
- `rq.uikit.input(text, opts)`: a text field in the kit's number-field look (`opts`: `w`, `max` 1 to 255 bytes, `label`, `placeholder`, `focus`, `disabled`, place, `id`, `tip`, `nav`). A click or Enter under the keys' cursor types into it; `focus = true` types from the update it first shows. Enter keeps the text, a click outside keeps it, Esc puts back the old one; it returns the text, `changed` and how a typing ended (`"enter"`, `"esc"`, `"away"`). One field types at a time, number fields included. While it types, every key is hidden from the game, the arrows are the caret's, and Esc does not close Config or `rq.uikit.page`. Listed as `input-<id>` with the text as `value` and `selected` while it types. In `src/lua/uikit.lua`.
- `rq.hud.text_begin` has a caret: typed text goes in at it, Backspace and Delete erase on each side, Left, Right, Home and End move it, and Ctrl+V pastes the system clipboard (without its line breaks and the characters the game's font cannot draw). Held, Backspace, Delete and the arrows repeat (250 ms, then every 50 ms). The keys are read from the keys' state each update, so `rq.input.set_key`, `rqmod-ctl key` and `hold` work them; Backspace was a key handler that agents never reached. Control characters are dropped. `rq.hud.text_value` returns the caret as a third value (bytes before it).
- `rq.input.type(text)`: types text into the text input that is on, at its caret; returns how many characters went in, or false while none is on. `rqmod-ctl type` does the same while a text input is on (any UTF-8 text; before, only letters, digits and space, as key pulses, which make no typed text).
- `rq.uikit.typing` names a text field that types too.
- `rq.uikit.page` with a title: the box `fn` gets starts at the title tab's bottom edge, 8 pixels higher than before, so the tab touches what it titles, as the hub's current tab touches its screen (Moru, 2026-11-11: the Save Manager's list and Morurun Items' slots stood apart from their tabs).
- `rqmod-ctl ui`: a widget's `value` past 159 bytes is cut between characters, so the JSON stays UTF-8.
- Save Profiles 1.1.0: the title screen's button and the Save Manager drawn with the kit in the hub's theme (`rq.uikit.page`, `list`, `button`), the keys' cursor, Play and Delete asked with `rq.ui.confirm` (Delete on No), and the name prompt a small page on the top layer with `rq.uikit.input`. Agents type a name with `rqmod-ctl type`.

## 2.28.0

Dialogs and Config (`notes/plans/plan-dialogs-config.md` in the workspace, phase A of the priority order).
- `rq.ui.confirm`, `notice` and `ask` show over Config, on any of its tabs, with a mod's page between Config and the dialog, so a button on a mod's Config page can ask with the game's own dialog. They opened under Config, out of sight. While Config runs (`T_Config::run`), the game's menu (`T_Select::create`, z 9991) and its comment window (`T_Comment::create`, 9801) are raised to z 16000 and 16100, above Config (15000 to 15010) and under the game's debug overlays (18000 up), and the HUD splits at the menu's z there. In `src/lua/dialog.lua`; the constants are a local's start value, which `rq.ain.patch_int` does not reach, so the kit has a helper of its own in `src/modloader.c` (not part of `rq`). The game never opens its own dialog in Config.
- `rq.ui.get` lists a dialog over Config as the screen `select`, with Config under it.
- `rq.ui.ask` takes `remember`, `remember_label` and `remember_answer`: the game's "don't ask again" row under the rows, as `rq.ui.confirm` has it, with the same keys (1 to 99 the game's switch, a text the mod's own question). `remember_answer` is the id of the row the call returns while the question is off; default the first row. The row and its note count 2 rows and a separator in the window's 20.
- `rq.ui.get` on `quests`: while a quest is chosen, the list's rows (`quest-N`) are not `enabled`. The game reads none of them then (`T_Quest::checkInput` skips them while the list is locked) until Cancel lets the quest go, and it stays chosen after its question is answered No. Agents took it for a hover lost after a dialog (`notes/lua-api-gaps.md`).
- Keep Donations 1.2.0: Set asks with `rq.ui.confirm` over Config, in place of its own Yes and No buttons. Gem Lady Trade 1.3.0: its question has the "don't ask again" row of the game's switch 11, "Take Quest".

## 2.27.0

Music, the rest (`notes/plans/plan-music-rest.md` in the workspace, priority #7 of the API work). Lua in `src/lua/music.lua`; `rq.ain.stack` and the volume in C.
- `rq.music.on_play`'s `ctx.kind` tells more moments, read from who called the game's music: `"boss"` (a boss fight, `ボス戦闘処理`; it was `"fight"`), `"town"` (`システム曲_再生`), `"castle"`, `"opening"` (`ＯＰ曲_再生`), `"result"`, `"jingle"` (a girl monster joins) and `"scene"` (a game scene or a mod's `rq.scene.play`); these were `"other"`. `"other"` is left for the extras, the system bar, a save's load, the title and a mod's `rq.music.play`.
- New ctx fields: `scene` (the game's scene function that asks for the track, such as `"ランス／城汎用"`), `boss` (the boss's monster number), `enemies` (the fight's monster numbers), `area` and `map_kind` (on a quest's map) and `world`. The last five are read when a callback reads them.
- `rq.music.page(opts)`: a page in Config's Mods tab for a pack, with a switch for each track the mod replaced and each moment it names (`opts.moments`), a play button per track, and all on and all off. A track switched off plays the game's file, at once when it plays now. The switches are kept for every save profile. `rq.music.enabled(key)` reads a switch; `rq.uikit.music_list(opts)` draws the same rows on a mod's own page.
- `rq.music.replace` on a track the player switched off checks and keeps the file, and its info has `off = true`.
- `rq.music.restore` brings back the replacement of the mod below in load order (it was the game's track).
- `volume` takes 0 to 200 (was 0 to 100): above 100 raises a quiet file.
- `rq.music.play` and `stop` are `"other"` to `on_play`, whatever screen they are called from.
- `rq.ain.stack(max)`: the names of the game's functions on its call stack, innermost first.
- The reference no longer says `on_play` misses the looped ambient sounds: the game never starts one (`ループ効果音`); the rain and wind of its scenes are music tracks (201 to 213), which `on_play` sees.
- `rq.music` now loads after `rq.uikit` and `rq.config`.

## 2.26.0

Mod states, the rest (`notes/plans/plan-mod-states-rest.md` in the workspace, priority #5 of the API work). Lua in `src/lua/status.lua` and `src/lua/battle.lua`, over the game's own functions, except the forecast flag.
- The game's dispels take mod states: `cured_by` has a new class, `"dispel"`. A hit that does damage with a skill of function 89 (quietly), Pop Pulse (491), Divine Erosion Wave (519), Guna Beam (515, half the time; where the target had a ▲, the state goes when the ▲ goes) or a Gunner's basic attack with Erasure Arrows (257), and Electroshock (183) on a target with no protection, take the states with `"dispel"`; the hit's log line gets `" (<name> canceled)"`, as for the game's ▲.
- `"all"` reaches two more of the game's cures: skill 475 at the start of the bearer's turn, when the game's own roll cured nothing (the first such state that rolls 50%, in the order they came), and Am Powder (498) when it heals no HP and cures no ▼ (the oldest such state, with `" X recovered from <name>."` in the log).
- `cured_by` defaults to `{ "dispel" }` for a good state; it was `{}`. `{}` still keeps a state from the game, so a good state that must not be dispelled says `cured_by = {}`.
- The AUTO button's Status Restore aims at an ally with a mod state it cures, as at a poisoned one.
- A number per state: each state's `ctx:damage` and `ctx:heal` show as a number of their own at the turn start, after the game's poison and regeneration, with the HP bar moving step by step; a lethal one shows the death on its own number. `ctx:damage(n, { apart = true })` and `ctx:heal(n, { apart = true })` do it in a plain `rq.battle.on_turn`.
- Persevere: a state's lethal damage meets skills 481 and 247 as a hit does (247 half the time, once a fight, with the game's own flag), and the log gets " (Persevere activated)". `persevere = false` in a definition makes a doom nothing stops. In a plain `on_turn`, `ctx:damage(n, { lethal = true, persevere = true })`; there it stays off by default.
- `rq.battle.on_hit` also runs after a special skill (action kind 3: the taunt, stuns, poisons, captures, and a mod's skill patched to `action = 3`), with `kind = "special"` and `damage` the HP the target lost.
- The battle forecast: `rq.combat.on_magic` runs for it too, so a state's `magic` shows in the damage word, as `physical` and `accuracy` already did. `forecast` on `PhysicalCtx`, `AccuracyCtx`, `CritCtx` and `MagicCtx` is true when the game only forecasts; the C patches read the 条件 argument of `物理ダメージ計算`, `命中計算` and `クリティカル計算` (`src/modloader_chara.c`). `rq.battle.on_forecast(fn)` adds text to the forecast line.
- Immunity: `immune` in a definition (`boss`, `barrier`, `races`, `types`, `charas`); `rq.status.set_immune(no, what, on)` makes a character number immune to a state or a tag, whichever mod defined it; `rq.status.immune(iic, id)` answers.
- `lasts = "quest"`: the state stays on an ally from fight to fight until the quest ends, however it ends, or a new quest is taken (reason `"quest_end"`). It can be added outside a fight during a quest, shows on the card when the next fight starts, and counts its turns only in fights. `rq.status.list` gives it outside a fight.
- `desc` in a definition: a few lines for players. The fight screen shows it with priority #6.
- `rq.status.info` gives `persevere`, `lasts`, `immune` and `desc`. `rq.status.add` returns nil and a reason when it puts nothing on: `"no_fight"`, `"no_quest"`, `"down"` or `"immune"`.
- Kaoru Quincy QoL 1.3.0 keeps Determination towards Victory as an `rq.status` state, with no change in the game.

## 2.25.0

Pictures past the fight cards (`notes/plans/plan-more-pictures.md` in the workspace, priority #4 of the API work).
- Moving pictures: a GIF or an animated WebP given to `rq.image.add` or `replace`, or as a character's `face` or `portrait`, is a moving picture. Its first frame is the CG; the game shows the frames wherever it shows the CG whole: a scene's background, standing picture, face and event CG, and the faces on character cards (the town's party bar, the Party screen, the status page, fights, where `rq.battle.set_face` wins). Where the game copies part of the CG or draws on it, and in `compose`, `rq.hud` and `rq.sprite`'s `cg`, it is the still. Every frame is fitted as the still is. `opts.fps` and `opts.clock` set the speed, as in `rq.sprite`. The file is read when it is set, so a bad one raises the error there. Up to 64 moving pictures, 1024 frames each and 64 million pixels in all. A sprite draws the frame in place of its CG while it shows that CG whole: the engine clears the mark when the game draws on the sprite, and `T_Sprite::stretchCg` (the card faces) is wrapped to set it. Parts draw the frame in place of their CG at the same size. The game is drawn again only while a moving picture was on screen in the last quarter second. In `src/modloader_image.c`, `src/modloader_sprite.c`, `src/sprite.c` and `src/parts/render.c`.
- `rq.image.info` gives a moving picture's `frames`, `ms` (one loop) and `drawn` (the game drew it in the last quarter second).
- `rq.image.flash_bitmap(file, id, path[, opts])`: a still picture from the mod's folder on one bitmap of a game Flash file (a cut-in, a battle effect, a mark), fitted to the bitmap's size so the file's placement and motion stay. nil for `path` gives the game's bitmap back. New loads of the file show it. `rq.image.flash_bitmaps(file)` lists a file's bitmaps with their sizes and whether a mod's picture is on them. In `src/modloader_image.c` and `src/parts/flash.c`.
- `rqmod-ctl flashdump NAME DIR`: every bitmap of a game Flash file saved as `<id>_<w>x<h>.png`, as `cgdump` does for CGs. `rqmod-ctl` sends its arguments as UTF-8, so Japanese file names reach the engine; `cgdump` is in its help.
- Fix: `rq.image.add` or `replace` that raised an error for its options or its file (a file not in the mod's folder, an unknown `fit`) did so after making the image's slot, so a half-made image stayed: `info` said `mod`, the number could show no picture, and it counted toward the 256. The call now checks everything first and leaves things as they were.
- Animated WebP is read with libwebpdemux, linked into the engine.

## 2.24.1

The mod behind a tail call (`notes/plans/plan-mod-tail-calls.md` in the workspace, priority #3 of the API work).
- A tail call into another file's Lua function (`return rq.ui.confirm(...)`) is a plain call: the caller's frame stays on the stack. So `rq.mod.id`, and everything that names entries by the calling mod, finds the mod through it: `rq.ui.confirm`'s `remember` (it was filed under `_`), `rq.gamebutton`, `rq.castle.room`, `rq.music`'s paths, `rq.status`, and the mod id in the error lines of `rq.dungeon` and the game-data calls. `error(msg, 2)` in an `rq.*` function now names the mod's line, and `rq.traceback` shows the mod's frame where it said `(...tail calls...)`. A tail call within one file stays a tail call, so a loop or recursion written that way runs as before; a chain of tail calls across files grows the stack as plain recursion does. It is a change in Lua's VM (`OP_TAILCALL` in `third_party/lua/lvm.c`, listed in `third_party/lua/RQ-PATCHES.md`); Lua 5.4.7's own test suite passes on it.
- One lookup for the calling mod: the `rq.log` tag, debug keys, image keys, `rq.item.edit`, `rq.roster`, `rq.sprite` owners and the read flags of mod text use the mod's `id` from `mod.json`, as `rq.mod.id` does. They used the name of its folder, which differs only when a player renames the folder: then debug keys were not removed when the mod reloaded, and the log named the folder. A renamed mod's text shows as unread once. The lookup keeps its answers by file, so it costs no more than before. In `src/modloader.c` and `src/modloader_sandbox.c`.
- The reference: `rq.mod.id`, `rq.ui.confirm` and `rq.log`.

## 2.24.0

Which dungeon and which area (`notes/plans/plan-dungeon-areas.md` in the workspace, priority #2 of the API work). The calls are Lua, in `src/lua/dungeon.lua`, over the game's own globals and functions.
- `rq.dungeon.on_area(fn)`: runs once each time the party enters an area of a quest (at the start, through a portal, by the quest's script), after the game's `ＱＭ登録`. Not when the game builds the map screen again, as `on_map` does after a save and for the result screen.
- The area's data: `area` (1 to 16, a cell of the quest's 4 by 4 area map), `row`, `col`, `name`, `kind` (the map kind, `◆ＭＡＰ基礎型`), `first` (not visited yet in this run) and `stratum` (the Malgrid Dungeon's stratum: 1 to 10 on its quests, the Xth Stratum's own count on quest 147). On `on_area`'s and `on_map`'s `ctx`; `quest`, `area`, `row`, `col`, `kind` and `stratum` in `rq.dungeon.info()`.
- `rq.dungeon.areas()`: the quest's area map as the game draws it, with the areas found, the routes, the party's area and the goal, and whether the game hides the map on this quest.
- `rq.ids.map_kind`: the 22 map kinds. The game names none; the names come from the places that use each kind, and the docs list them.
- The reference says when `on_map` runs, and that its `map` is the map layout number.

## 2.23.0

Game data that Gem Lady Trade, Morurun Items and Keep Donations read and wrote through `rq.ain` (`notes/plans/plan-game-data.md` in the workspace, priority #1 of the API work). The calls in Lua are in `src/lua/gamedata.lua`, over the game's own functions.
- `rq.items()` rows have `no` (the item number), `place` (the game's `存在`: 7 the vault, 11 the storage, 8 quest storage, 20 and up worn) and `lock` (locked in the vault). Fix: the list runs to the game's last used item slot; it stopped at 1024 rows, so a large vault lost rows with no sign. In `src/modloader_query.c`.
- `rq.item.find(no, opts)` and `rq.item.count(no, opts)`: an item number's instances by place (`"vault"`, `"storage"`, `"quest"`, `"worn"` or a number, one or a list, in that order) and by the vault lock. With no `opts`, `count` is the game's own count (worn, the vault and the storage). In `src/modloader_item.c`.
- `rq.world.current()`, `rq.world.on_transfer(fn)` and `on_transfer_after(fn)`: the world, and the game's world transfer before and after its reset (`ワールド切り替え処理`), with the world and the one before. The reference lists what the reset changes.
- `rq.shop.donations()` and `rq.shop.set_donations(count, goal)`: the donations count and Frostbuy's reward goal, with her rules in the reference.
- `rq.quests.on_take(fn)`: the quest list's Take, before the game's question and its autosave; the callback may wait on a dialog and returns nil (the game's way), true (taken, no question) or false (not taken). `rq.quests.can_take(no)`: the game's `クエスト_有効`, which lights Take. `rq.quests.refresh()`: the list drawn again with the chosen quest's buttons, as after the favorite button.
- `rq.quests.set_state(no, 1)` on a quest already available or cleared writes the state: the game's `Ｑ状態` takes 1 only from 0, so the call did nothing there (`notes/lua-api-gaps.md`).
- `rq.chara.absorbed(iic)` and `rq.chara.set_absorbed(iic, slot, no)`: the five items a Morurun absorbed (`ＣＦＡ` 17 to 21), changed with the game's rules on what can be absorbed, then the character recalculated.
- The reference: `rq.item.get`'s `place` lists 11, the storage.

## 2.22.1

- `rq.uikit.item_icon`: no REMOVE, and D does nothing, on an item that cannot be taken off (`rq.item.get(ii).locked`, the game's `外せません`), as the status page leaves it out. It was shown, and pressed, on every item. Found by the Lab's `uikit-items` (`notes/plans/plan-lab-coverage.md` in the workspace, T6). In `src/lua/uikit_vault.lua`.
- `rq.ui.get`: Trivia, CG mode, Music mode and the castle's Gal monsters' and Poster rooms are the screen `other`, with the footer only, as 2.20.1 meant. They run inside the town's or the castle's loop, so they were reported as `hub` or `castle`, with that screen's tabs under them. In a fight only `system` of the footer is listed, as the game shows it. Found by the Lab's `ui-screens` (T8). In `src/modloader_ui.c`.
- `rq.battle.start` away from a quest's map (the town, Rance Castle, the Party screen, Quests): the screen it started from is drawn again after the fight, with its footer. The fight's black layer stayed over it and the footer was gone, so the town was black until a tab was opened. During such a fight `rq.ui.get` says `battle`; it named the screen under it, so the Lab could not play a fight started on the Party screen. The fight's own Party screen (Switch) is still `party-edit`, over the fight: it is told from the town's by its z. Found by the Lab's `statuspage` (its level-up fight from the town). In `src/modloader_state.c` and `src/modloader_ui.c`.
- `rq.skilllist`: another character in the open skill window (its scroll bar, or the wheel over it) starts on page 1, as opening the window does. It kept the page shown, so page 2 of one character became page 2 of the next. Found by the Lab's `skill-window` (T17). In `src/lua/skilllist.lua`.
- `rq.castle.room`'s `chara` is a character number (`rq.ids.chara`), as the reference says: the loader gave the number to `Ｃ顔ＣＧ`, which takes a roster slot, so Lia's 54 showed Shitomone Chappie's face. The face is now the character's, and none while they are not in the roster. Found by the Lab's `castle-room` (T10). In `src/lua/castle.lua`.
- The reference says that `rq.mod.id` cannot see a mod through a tail call: after `return rq.ui.confirm(...)` a remembered question is filed under `_` (`notes/lua-api-gaps.md`, found by `ui-dialogs`, T14).

## 2.22.0

A number field, and constants of the game's code a mod can change while the game runs (`notes/plans/plan-ui-kit-leftovers.md` in the workspace, section 17), for the Config pages of Custom TADA Mode 1.1.0, Kaoru Quincy QoL 1.2.0 and Keep Donations 1.1.0:
- `rq.uikit.stepper(value, opts)`: a whole number in a framed box between - and +. Shift for `big` steps, held buttons repeat (400 ms, then 80 ms), the wheel, Page Up and Page Down under the keys' cursor. A click on the number, or Enter, types into it from the digit keys (so `rqmod-ctl type` can), Enter keeps, Esc puts back. Listed as `stepper-<id>`, `selected` while it types. In `src/lua/uikit.lua`.
- `rq.uikit.typing()`: the field typing now, or nil.
- `rq.uikit.page`: Esc that ends a field's typing does not close the page (`src/lua/uikit_hub.lua`).
- `rq.ain.patch_int_after` also returns the places it changed; `rq.ain.set_code_int(place, value)` writes one again and `rq.ain.code_int(place)` reads it (`src/modloader.c`). A place is found again after a later install wraps the function (at its code address) or moves and grows its body (by the opcodes around it).

Found in the Lab: the game's Yes/No dialog (`rq.ui.confirm`) opens under Config, out of sight, so a Config page asks on the page itself (in `notes/lua-api-gaps.md`).

## 2.21.0

The game's item tile and item card in the kit (`notes/plans/plan-ui-kit-leftovers.md` in the workspace, section 16), in `src/lua/uikit_vault.lua`:
- `rq.uikit.item_icon(item, opts)`: an item's tile as the status page's equip slots draw it (`T_ItemIcon`): the icon, 100 by 100 or `size`, with its rank badge, and the game's yellow frame under the mouse, the keys' cursor and while `current`. Its tip is the item card, left of the tile, after 500 ms from the mouse and at once from the keys. `remove` adds the status page's REMOVE button (or D from the keys). nil is an empty slot. `judged = false` gives the UNIDENTIFIED card.
- `rq.uikit.item_card(item, opts)` and `item_card_size()`: the game's item card (`T_ItemComment`, CG 10402 with the item's row; CG 10403 over it for an item not identified), on the top layer, kept on the screen as the game keeps it.
- `item_row` draws its parts with the card's code.
- `rq.ui.get` lists the card with the type "card", which takes no click (`modloader_ui.c`).
- `weight` in a text style with `font = "game"`: the game's font weight, 0 to 1000 (`modloader_hud.c`).

Fixes to the item row (`item_row`, the vault, the storage and the shop), found by matching the card to the game's pixel for pixel:
- The stats' numbers are drawn at the game's weight 70, as `T_StoreComment` draws them; they were at 0, so thinner.
- The name is centered as `T_DrawText` centers it, `(202 - w) / 2` rounded down; it sat 1 px to the right.
- The level bar's text is at the bar's top, as `T_StoreList` draws it; it was centered down the bar, 2 px low.

## 2.20.1

`rq.ui.get` on every screen (`notes/plans/plan-ui-kit-leftovers.md` in the workspace, section 15), in `modloader_ui.c`:
- The footer (`system`, `vault`, `trivia`, the party cards and the money line) is listed on every screen whose own loop takes its clicks, not only the town, Frostbuy and the Party screen: Quests, Rance Castle, the status page, the vault, a quest's map, a fight, and an unnamed screen that shows it.
- Rance Castle is the screen `castle` (it was `other`, with bare sprites): its rooms are `room-<area>`, with the room's name as the label and its floor (with ` new` for the NEW mark) as the value, greyed as the game greys them; a mod's room (`rq.castle.room`) is listed the same way. Its town tabs are `frostbuy`, `party` and `quests`. `rq.sprite`'s `keep = "screen"` sees `castle` too.
- Quests lists the town tabs (`rance-castle`, `frostbuy`, `party`).
- Fixed: the SYSTEM menu opened over Quests or the status page was reported as the screen under it; it is `system-menu`.
## 2.20.0

The status page for mods (`notes/plans/plan-ui-kit-leftovers.md` in the workspace, section 14). Lua over the game's own page (`src/lua/statuspage.lua`, `src/lua/gamebutton.lua`, `src/lua/item.lua`); the C changes are the fix below and a switch only the loader's own Lua gets.
- `rq.gamebutton`'s group `"status"`: icon buttons in a character's status page's title row, the only free room on the page, right to left from the X (x 472 and 436, y 61, 32 × 29), up to two. `icon` is the CG drawn on the page's own background, with the game's hover frame, pressed and greyed looks. `shown`, `enabled` and `tip` may be functions of the character, asked on every draw of the card. A click runs `on_click` with the page open; the arrow keys reach them from the Special slot; `tip` shows the game's comment window with the label as its title. Agents see them as `<mod id>.<id>` on the `status` screen.
- `rq.statuspage`: `chara()`, `mode()`, `refresh()` (the card drawn again, no sound, the item list beside it rebuilt), and `on_open`, `on_chara`, `on_update`, `on_close`.
- `rq.item.info(no)`: an item number's row data with no instance in the game, read as the game's own lookups by number read it. `rq.item.on_create` listeners do not see its temporary instance.
- Fixed: `rq.ui.get().status.chara` was always 0; it is the character shown.

## 2.19.0

The game's dialogs as calls (`notes/plans/plan-ui-kit-leftovers.md` in the workspace, section 13), in `src/lua/dialog.lua`:
- `rq.ui.confirm(text, opts)`: the game's Yes / No, which waits for the answer. `remember` adds the game's "don't ask again" row: 1 to 99 is the game's own switch, a text the mod's own question, kept in `rqmod-global.json`, listed on a Confirmations page in Config's Mods tab and turned back on by Config's Resetting.
- `rq.ui.notice(text, opts)`: the game's OK.
- `rq.ui.ask(text, rows, opts)`: the game's dialog with any choices, which waits for the answer.
- In a mod's text only `\n` starts a line (`@` and `$` are drawn as `＠` and `＄`; `game = true` for the game's texts), and a text longer than 3 lines gets a row for each 3. Nothing is shown (nil) while another dialog is being built or shows.
- `rq.ui.get`: `select.message`, the dialog's text rows.
- `rq.item`'s questions are refused while any dialog shows, not only their own.

## 2.18.0

The rest of Potential Skill Pages in Lua (`notes/plans/plan-ui-kit-leftovers.md` in the workspace, section 12): `rq.skilllist` is Lua over the game's own code (`src/lua/skilllist.lua`), and the engine's 1170 lines of C for it (`modloader_skilllist.c`, its bytecode patches and replaced bodies) are gone.
- `rq.ain.set_global_len(name, ..., size)`: makes an array global longer or shorter, as the game's `Realloc` does.
- `rq.skilllist`: the game's three buy-list arrays are made 145 long (rows 1 to 144, were 143 in the engine's copy) whenever the game fills them, `スキルポン` stops at row 145, and while the window builds its list the game's own count and row reads answer the page's 36. The game's buy and its cost read the arrays as they are. Rows 61 to 144 are emptied when the window closes, so a save holds what the game's own 60 rows would. Callbacks have no limit (were 16).
- `rq.skilllist.install()` with buttons: Previous Page and Next Page are now the calling mod's `"skill-window"` entries (`<mod id>.skilllist-prev` / `-next`), placed in the order entries were added; `on_buttons` gets their ids (200101 to 200104, were 200037 and 200038). Their look is the same.
- `rq.chara.offers` and `set_offer` work on the game's arrays only.
- `rqmod-ctl ui`: `skillShop.page` and `pages` come from `rq.skilllist.page()` and `page_count()`.

## 2.17.0

Phase 5 of what the hub UI kit left (`notes/plans/plan-ui-kit-leftovers.md` in the workspace, section 11), its second part: the skill window. Lua over the game's own buttons; the only C change is an option of `rq.skilllist.install`.
- `rq.gamebutton`'s group `"skill-window"`: buttons under the Potential Skills list, in the castle buttons' look (CG 11153, the label in the game's font), two to a row under the list's picture (x 531 and 745, y 660 and 692), up to four. They are the game's own buttons in the list's button group, made again with each build of the list; `enabled` greys one as the game does. A click runs `on_click` with the window open. The arrow keys reach them from a column's last skill, and `tip` shows the game's skill comment. Agents see them as `<mod id>.<id>` on the `skill-shop` screen. `groups()` lists the group with each entry's `placed`, `button`, `x` and `y`.
- `rq.skilllist.install(opts)`: `buttons = false` leaves out the engine's Previous Page and Next Page. They stay for mods made before, now at y 660 (were 652), under the list's picture instead of over its last rows.
- `rq.skilllist.page()`: the page shown. `rq.skilllist.refresh()`: builds the list again for the character shown, as the game does after a buy.

## 2.16.0

Phase 5 of what the hub UI kit left (`notes/plans/plan-ui-kit-leftovers.md` in the workspace, section 10): buttons of mods in the game's own menus, made by the game itself. All of it is Lua over one new C call.
- `rq.castle.room(spec)`: a mod's room in Rance Castle. It is one of the game's own castle areas (30 to 50, which the game leaves free), made each time the castle opens, as the Gal monsters and Poster rooms are: the game draws its button, name, face and NEW mark and moves the keys to it. It goes on its floor (default B2F), or the nearest floor with a free cell that time; the game's rooms never move. A click runs `on_enter`; the castle stays open. The handle has `area`, `floor`, `where`, `set` and `remove`. `rq.castle.rooms()` lists them. `rq.castle()` and `rq.castle.get()` are as before.
- `rq.gamebutton.add(spec)`: an entry in the SYSTEM menu. While any entry exists the menu has one more row, MODS, under Save (or Suspend Save), in the menu's painted look (its own letters and the game's key icon, through `rq.image.compose`); the keys reach it, and it is greyed while no entry is enabled. Picking it lists the enabled entries in the game's choice menu, with their `tip`. The handle has `id`, `set` and `remove`. `rq.gamebutton.groups()` lists them.
- `rq.ain.method(path, name, ...)`: calls a method of the game on the struct a global reaches, with plain arguments as `rq.ain.call`.
- `rq.ui.get` and `rqmod-ctl ui`: the MODS row is the control `mods` of the `system-menu` screen.

## 2.15.0

Phase 4 of what the hub UI kit left (`notes/plans/plan-ui-kit-leftovers.md` in the workspace), its last part: the game's skill tile. All of it is Lua.
- `rq.uikit.skill_button(skill, opts)`: a skill's tile as the status page draws it, to the pixel: the CG of its panel color, the name fitted in the game's font, a mark for each rank above 1 (`rank`, or the character's with `chara`), the uses in the level digits (`count`, or the character's), `long` (the 167-wide tile), `disabled` (greyed as the game greys a skill), the hovered look and the game's frames. Its tip is the game's comment for the skill. With `skill` nil and `slot`, the empty slot with its number.
- `rq.uikit.number`: `tint`.
- `rq.ui.get` and `rqmod-ctl ui`: a tile is listed with the type "skill" and the skill number as `value`; an empty slot with the type "slot", which is never the `hover` and never makes a game control `covered`.

## 2.14.0

Phase 4 of what the hub UI kit left (`notes/plans/plan-ui-kit-leftovers.md` in the workspace), its second part: the game's gauges and digit fonts. All of it is Lua.
- `rq.uikit.bar(value, max, opts)`: the game's bars (`T_Bar`), a CG cut to `value / max`, to the pixel: `style` for the game's own (HP on the cards, the mini cards and monsters, EXP, charisma, quests, the upright Magnum gauge), or any `cg`, or a `color`; `dir = "up"`; `anim`, the value moving in a straight line as the game's bars do. Only the bar; the frames are parts of each screen's background. It takes no click; `tip` works on it.
- `rq.uikit.number`: the game's digit fonts by name (`"hp"`, `"level"`, `"level_max"`, `"status"`, `"small"`, `"world"`, `"gallery"`, with `"gold"`) or any CG cut in 10 cells; `hyphen` for an 11th cell, "-". It returns its place. A negative number with a digit font draws as 0, as the game's (before, the gold digits left out the minus).
- `rq.ui.get` and `rqmod-ctl ui`: a bar is listed with the type "bar" and the value it shows. A bar or a comment window is never the `hover`, and never makes a game control `covered`.

## 2.13.0

Phase 4 of what the hub UI kit left (`notes/plans/plan-ui-kit-leftovers.md` in the workspace), its first part: the game's comment window. All of it is Lua but one field.
- `rq.uikit.comment(text, opts)`: the game's comment window (`T_Comment`), its look and layout to the pixel: the paper window with three borders and a shadow, a `header`, the text wrapped at 520 pixels as the game wraps it, red `sub` lines, and the game's red `style`. At the mouse, or at `x`, `y`, kept on the screen as the game's. On the top layer; it takes no clicks and covers no game control. `rq.uikit.comment_size` gives its size.
- `tip` and `tip_wait` on every widget that takes a click: the comment window after the mouse or the keys' cursor stays on the widget 500 ms, with the game's sound; at the mouse, or at the widget's edge from the keys. `tips` on `tabs`, `choice` and `sort`, `tip` on `list` and `quest_list` rows.
- `rq.uikit.options`: a row's `comment` is the game's comment window right of the menu, at the row, after 500 ms, as the game's menu shows it (before, a plain box at once). The hub theme's `options.comment` style is gone.
- `rq.hud.text_width`: `measure = true` with `font = "game"` gives the width as the game's windows reckon it (its `MeasureText`), not the drawn line's.
- `rq.ui.get` and `rqmod-ctl ui`: a comment window is listed with the type "comment" and its text as `value`; it never makes a game control `covered`.

## 2.12.0

Phase 3 of what the hub UI kit left (`notes/plans/plan-ui-kit-leftovers.md` in the workspace): the keyboard, as the game's own screens use it. All of it is Lua but one field.
- The kit's keys cursor: the arrow keys move one cursor between the widgets that take a click, and Enter clicks the one under it. The mouse and the keys share it, as the game's selection: the mouse over a widget puts the cursor there, and the mouse is never moved. An arrow goes to the nearest widget that way, and wraps when there is none. In a list (`list`, `quest_list`, `options`, `item_list`) Up and Down go through its rows, also those out of sight, and the list scrolls to follow. A focused slider moves by Page Down (up) and Page Up (down), 5% or its `step`, as Config's sliders.
- `rq.uikit.keys(opts)`: the kit takes the arrows, Enter, Page Up and Page Down on this update and hides them from the game. `edge(dir)` is called when an arrow finds nothing that way, and the cursor then does not wrap. `rq.uikit.page` calls it; elsewhere the kit's widgets stay for the mouse. `rq.uikit.focused()` and `rq.uikit.focus(id)` read and set the cursor.
- `nav` on every widget: where its arrows go, by id (a table or a function of the arrow), or false to leave it out of the cursor.
- Config's Mods tab: the tab row's Left and Right reach it; Down from a tab on the Mods page gives the cursor to the page's list, and Up from the page's top widget gives it back to the tab row.
- `rq.hud.block_keys(keys)`: only the keys in the list, by name or code. Without a list, every key as before.
- `rq.ui.get` and `rqmod-ctl ui`: `focused = true` on the kit control under the keys' cursor.
- `rq.uikit.options`: the rows are on the kit's cursor (it wraps); `keys` makes it take the keys and Esc picks Return. A cursor the mouse put on a row goes when the mouse leaves every row, as the game's buttons do (before, it stayed on the last row hovered). `rq.uikit.item_list` with `keys`: Up and Down go on to a widget outside at the list's ends.
- Fix: the kit's held keys repeated after 400 ms, every 80 ms; the game's do after 250 ms, every 50 ms, and so do the kit's now (`item_list`, `options`, `page`'s Esc).

## 2.11.0

Phase 2 of what the hub UI kit left (`notes/plans/plan-ui-kit-leftovers.md` in the workspace): a layer over the HUD, the game's faint shadows, and agents that click as a player does.
- `rq.hud.top(fn)`: what `fn` draws goes on a top layer, drawn after every other HUD draw of the update, from every mod. Inside it the clip starts at the whole screen; the clip from outside comes back after it, also on an error. Drawing only: clicks are still decided in call order. `rq.uikit.top(fn)` is the same for widgets.
- `rq.uikit.item_list`: the dragged icon is drawn once, by the list it came from, on the top layer, so a widget drawn after the lists or a clip no longer covers or cuts it. `rq.uikit.options`: a row's comment box is on the top layer too.
- `shadow.a` in the game-font text style (`rq.hud.text`, `text_width`, `rq.image.compose` text layers): the shadow's opacity, 0 to 255, times the text's. The hub theme's sort labels have the game's white shadow at 64.
- Agents: a click `rqmod-ctl` drives is held back by `rq.hud.block_game_input` as a player's is (before, it reached the game's control under a kit widget). `rq.ui.get` and `rqmod-ctl ui` mark a game control `covered` when every point of it is under a kit widget of the last update, or while a page captures the mouse; `rqmod-ctl press` refuses it ("covered by a mod's widget"), and `rq.ui.aim` aims a game control away from kit widgets over it.

## 2.10.0

Phase 1 of what the hub UI kit left (`notes/plans/plan-ui-kit-leftovers.md` in the workspace): the lists and the shop, as the game does them. All of it is Lua over the game's own calls.
- `rq.item.buy(ii, opts)`: buys an item from the shop's stock as the shop's drag does, with the game's "Purchase ...?" question, its "Not enough money." notice, the money and the shop's spent total. `chara` buys onto a character and equips it, as the drag onto a party member does. `ask = false` buys at once.
- `rq.item.sell` and `donate` take an item a character wears: it comes off first, after the game's question, with the game's "cannot be removed" notice for one that cannot; one that vanishes when taken off is refused.
- `rq.uikit.scrollbar`: the arrows and the track move on the press, as the game's; held, they wait 250 ms and move again on every update. The track stops at the mouse. (Before, they moved once, on the release.)
- `rq.uikit.sort`: `again` (a button that can be clicked while current) and a third return, the button clicked.
- `rq.uikit.item_picker`: the game's SORT ("Default Sort" and the mode's short name) at the bottom right of the column, in place of the sort button under it; the column's grey goes down to the panel's foot. The sort starts at the stores' saved mode (`アイテムソートモード`) and a new one is saved, as the game's stores do; the menu has the game's rows (no "Default" row). A new sort goes back to the top.
- `rq.uikit.item_storage`: the vault's filter column and SORT, applied to both lists, as the game's storage screen does; the counts are of the lists as filtered. Fix: it sorted by item number whatever the stores' saved mode, so its order differed from the game's when the player had picked a sort.
- `rq.uikit.options`: `h` (default and at most 762); past it the rows under the message scroll, with the game's scroll bar right of the base, by the wheel, the bar and the keys' cursor.

## 2.9.0

What phase 4 of the hub UI kit left for later: a mod can lock, sell, donate and store items as the vault does, and the vault's widgets get the shop's and a character's lists, keys, dragging and two-line names. All of it is Lua over the game's own calls (`src/lua/item.lua`, `src/lua/uikit_vault.lua`).
- `rq.item.lock(ii, on)`, `rq.item.sell(ii, opts)`, `rq.item.donate(ii, opts)`, `rq.item.store(ii, where)`: what the vault's LOCK / UNDO LOCK, SELL and DONATE buttons and the storage screen's drag do, with the game's own calls, sounds, restock, gold and donation count. Sell and donate ask the game's question first (`ask = false` skips it); they refuse a locked item, as the vault hides those buttons on one. Only items in the vault or the storage.
- `rq.uikit.item_row` and `item_list`: the shop's style (`"shop"`: green, the price in gold digits, no LOCKED) and a character's equip list (`"equip"`). A name too long at 12 pixels wraps in two lines of 12, as the game's does, instead of being cut. A locked row no longer shows SELL and DONATE. `item_data` has `discard` (the game lets it go).
- `rq.uikit.item_list`: `keys` (Up, Down, Page Up, Page Down, Home, End, Enter, and L, S, D on the current row, repeating as the game's) and a fifth return, `chosen`; `drag` (a group: rows are dragged between the group's lists, and `rq.uikit.item_dropped(group)` returns the row dropped).
- `rq.uikit.item_storage(opts)`: the game's storage screen, the storage and the vault side by side with their counts; dragging a row moves the item (`rq.item.store`).
- `rq.uikit.filters`: `style` ("vault", "shop" without Locked / Unlocked, "equip" with Equippable / Unequippable); the state has `equip` and `chara`, and `item_filter` tests them with the vault's `アイテム倉庫_一覧_装備タイプ確認`.
- `rq.uikit.item_picker`: `where = "shop"` (the shop's stock, place 6) and `"quest"` (the quest storage, place 8), `chara` (a character's equip list), `keys`; the row style and the column follow the place. It lists again after an `rq.item` change. A click on the current row picks it again.
- `rq.uikit.options`: `keys` (Up and Down move a cursor that wraps, Enter picks, Esc picks Return).
- `rq.uikit.number`: `align` and `gap`.
- Fix: the picker's list did not go back to its top when a filter changed (it reset a state of the wrong name).

## 2.8.0

The vault's lists and filters, phase 4 of the hub UI kit (`notes/plans/plan-ui-kit-hub.md` in the workspace). The widgets are drawn from the game's own CGs, and the data, the filters and the sorts are the game's own calls.
- `rq.uikit.item_data(ii)`: an item instance's row data from the game (name, level line, stats line, icon, rank, kind, lock, price, place, the classes that may equip it). `rq.uikit.item_refresh(ii)` makes lists read it again at once.
- `rq.uikit.item_row(row, opts)`: a vault item row, as the game draws it, with the stats line wrapped and colored as the game's (its `|` and backquote marks, white numbers), the vault or storage background, and the LOCK / UNDO LOCK, SELL and DONATE buttons. A row can be an instance or a table of your own.
- `rq.uikit.item_list(rows, index, opts)`: the vault's list of 6 rows with the game's scroll bar.
- `rq.uikit.filters(state, opts)`: the vault's filter column (categories, classes, Locked / Unlocked) and the sub-filter panel of the picked category, with the vault's toggles; `rq.uikit.item_filter(list, state)` applies a state with the vault's own tests.
- `rq.uikit.item_sort(list, mode)` sorts with the vault's comparers; `rq.uikit.item_sorts()` lists the modes with the game's names.
- `rq.uikit.number(value, opts)`: the vault's counter font, or the gold digits.
- `rq.uikit.item_picker(opts)`: a picker over the items in the vault, the storage or both, laid out as the vault (list, filters, count, a sort button that opens the game's sort menu). It returns the instance picked and moves nothing.
- The hub theme has the vault's pieces (`vault`, `filters`). The vault's widgets are in their own file, `src/lua/uikit_vault.lua`.

## 2.7.0

The options list, phase 3 of the hub UI kit (`notes/plans/plan-ui-kit-hub.md` in the workspace).
- `rq.ui.choose(items, fn, opts)`: opens the game's own choice menu outside a scene, on the hub or any of the game's screens, and calls `fn` with the picked row's id (0 when cancelled). Rows as in `rq.scene.choice`, with any value as an id; `message` rows on top, a Return row (`back`), `cursor`, `x`, `y`. It opens at the next update and waits for the System menu, Config, a scene, or another choice menu.
- `rq.ui.choosing()`: true while the game's choice menu shows (the game's own, `rq.scene.choice` or `rq.ui.choose`).
- `rq.uikit.options(items, opts)`: the choice menu's look as a widget inside a page, not modal: the green base, the grey rows (tall with fewer than 3), separators, a text panel, comments and a Return row. The hub theme has its pieces (`options`).
- While the game's choice menu shows, the HUD is drawn under it (before, a mod's HUD covered it), `rq.uikit` widgets take no input and are not listed for `rqmod-ctl`, and `rq.hud.capture_mouse` does nothing. A `rq.uikit.page` stays open under the menu; the right click, Space or Esc that ends the menu does not close it.
- The game's choice menu now counts as a modal screen for Item Previews (the wrap on `T_Select` named a method the game does not have, so nothing was wrapped).

## 2.6.0

The hub's widgets in `rq.uikit`, phase 2 of the hub UI kit (`notes/plans/plan-ui-kit-hub.md` in the workspace). They are drawn from the game's own CGs and write in its own font.
- `rq.uikit.themes.hub`: Config's theme with the hub's pieces added. Hub widgets take their pieces from the theme in use, else from it, so a copy of it can change some.
- `rq.uikit.button` takes `opts.style`: "large" (Rance Castle's rooms), "choice" and "choice_tall" (the choice menu's), "short" (the footer's Vault and Trivia). A long text gets smaller and tighter until it fits, as the game's `FitText2` does. With the hub theme in use, a button without a style is "large".
- `rq.uikit.tabs` takes `opts.style = "town"`: the hub's town tabs, the current one orange.
- New: `castle_row` (a castle room with its face, NEW and heart or MORU RUN mark), `quest_row` (number, yellow name, the clear count in its box), `quest_list` (13 rows with the game's scroll bar; the wheel, the arrows, the track and a drag scroll it), `scrollbar` (the game's scroll bar on its own), `rack` (a Frostbuy rack tile, drawn from shapes since the shop's are painted), `sort` (the sort column), `close` (the windows' close button) and `page` (a page of a mod's own over the hub: modal, closed by its close button, a right click or Esc).
- `rq.uikit.list` has the game's scroll bar with a theme that has `scroll`, such as the hub theme.
- `rq.hud.capture_mouse()`: for this update the game sees no mouse, buttons or wheel, also when `rqmod-ctl` drives the mouse, so a page over the game works for agents as for players. `rq.uikit.page` uses it.
- The hub's widgets are in their own file, `src/lua/uikit_hub.lua`, built into the exe beside `uikit.lua`.

## 2.5.0

The game's own font for mod text, the first piece of the UI kit for the hub (`notes/plans/plan-ui-kit-hub.md` in the workspace).
- `rq.hud.text` takes `font = "game"`: the game draws the text in its own font (`face` 256, 257 or 258), letter by letter with the spacing its English text uses, as on its buttons, lists and the castle. `outline` and `shadow` give its edges, `space` and `spacing` its letter spacing, and `valign = "center"` centers it as the game centers button labels. Each different text is drawn once and kept; up to 512 different texts draw on one update. `rq.hud.text_width` takes the same style and then also gives the height.
- `rq.image.compose` text layers take `font = "game"` with the same fields.
- `rq.hud.clip_push(x, y, w, h)` narrows the clip to a box inside the one before, and `rq.hud.clip_pop()` goes back. `rq.hud.clip(x, y, w, h)` is the box they start from. `rq.uikit.list` uses them, so a list stays inside a clip of your own (before, its clip replaced yours).
- `rqmod-ctl cgdump` answers on a screen that draws no frame, such as the disclaimer (before, it waited until the pipe's timeout, and the pipe stopped answering).

## 2.4.0

`rq.music`: a mod's own music file plays where the game plays one of its tracks.
- `replace(no, path, opts)` puts a file behind a game track's number, wherever the game plays it, and `restore(no)` takes the calling mod's back. The game goes on with the number, so its crossfades, Config's music volume, saves and the system bar work as before. `opts`: `loop_start` / `loop_end` in seconds, `volume` (the file's own, 0 to 100), and `name`, which the extras' music room shows.
- Files: OGG (Vorbis or Opus), FLAC, WAV or MP3, mono or stereo, streamed from the disk. A file loops forever unless the game plays the track once. It loops between its loop points: the options, else `LOOPSTART` with `LOOPLENGTH` or `LOOPEND` tags in the file, in samples, else the whole file.
- `on_play(fn)` runs before the game starts a track, with `ctx.no`, `ctx.playing`, `ctx.kind` ("fight", "dungeon" or "other"), `ctx.quest` and `ctx.loops`. `ctx:file(path, opts)` plays a file for this time only, and `ctx:track(no)` another game track. When a track already plays with another file than it should now, it starts again.
- `info(no)` gives a track's name, whether the game has it, the mod's file with its loop points and length, or the game track's length. `current()` gives the track that plays now: its number, name, the mod's file, the position and the length. `play(no, opts)` plays a track as the game does (`restart`, `once`), and `stop()` stops the music.
- Two mods on one track: the later one in load order wins, and the log names both. A number the game has not raises an error. In `init.lua`, before the game opens its music, it is instead checked at the first frame, logged and dropped.
- The C half is in `src/modloader_music.c`: when the game prepares a music channel, the engine asks it first. The file plays on the track's own mixer, with a volume scale on top of the game's fades. The rest is Lua inside the engine (`src/lua/music.lua`).

`rq.ids.music`: the game's 59 named tracks (`音楽の名前`), such as `INDOOR_CRAWL_R8` (1) and `BATTLE_2_R8` (52). `rq.ids.find`, `find_all` and `name` take the kind `music`.

## 2.3.0

Lethal turn damage: a mod state may now down its bearer.
- `ctx:damage(n, opts)` in `rq.battle.on_turn` takes `{ lethal = true, source = killer }`. With `lethal`, the HP may reach 0. The character then goes down, shown as the game shows a death: the enemy fades and drops its gold, or the ally's card turns red. `rq.battle.on_down` runs, and the turn passes. Without `lethal`, the HP still stops at 1, as poison's does.
- The dying character's own death skills act: Hanny Zippo brings it back at full HP, once a fight, and Rich Enemy doubles the gold. With a `source` that is in the fight and not down, the game's own death handling runs with that killer, so Kalar's curse acts too.
- When the action ends, the game checks for the end of the fight, as it does after an attack: the last enemy's death wins the fight, and the last ally's loses it.
- `ctx.downed` is true once a lethal damage downed the character. After that, `ctx:damage` and `ctx:heal` do nothing in that turn start.
- `rq.status` definitions take `lethal = true`, default false. Their `on_turn` damage may then down the bearer, with the state's `source` as the killer, and `rq.status.info` reports it. Once the bearer is down, the states after it do not tick that turn.
- A familiar never goes down this way. Persevere does not save a character from lethal turn damage, as it does not from poison.

Docs: `rq.combat.on_accuracy` now names the game's limits that come after its callbacks. An ally's attack hits at least 20% of the time, an enemy's at least 40%, and an enemy's at most 80% to 100% by the target's evasion.

## 2.2.0

`rq.status`: battle states made by mods, such as a burn, a bleed, a regeneration, a freeze or a weaken, in one registry every mod shares.
- `define(id, def)` takes an id `"<mod>:<name>"` and a definition: kind ("bad" / "good"), turns, how adding it again stacks ("refresh", "add", "keep" or a most-stacks number), what cures it, tags, an icon, and callbacks for each of the bearer's turn starts (`on_turn`, with the `rq.battle.on_turn` context), for its coming and going, and for physical hits, spells and accuracy by or on the bearer.
- `add`, `get`, `list`, `remove` and `cure` (by id, kind or tag, for a mod's own medicine) work on any mod's state; `info` tells about a definition; `on_add` and `on_remove` report every mod's.

Rules:
- A state lives only in its fight. It goes when the fight ends, when its bearer goes down (unless `keep_on_down`), when its turns run out, when it is cured, or when a mod removes it.
- Turns are the bearer's own: they count down at the end of each of its turns, and a state added in the bearer's own turn skips that one.
- The game's cure skills cure mod states too: Status Restore, Encourage and Self-Healing every state cured by `"all"` (the default for bad states), First Aid those cured by `"poison"`. A support skill number in `cured_by` cures it too.
- A state with an icon shows as a buff on the card, with its turns left.
- Lua inside the engine (`src/lua/status.lua`), built on the 2.1.0 events and public calls.

## 2.1.0

The first part of battle states made by mods: three events a mod state is built on. The shared state system, `rq.status`, comes next.

- `rq.battle.on_turn(fn)` runs at the start of every turn in a fight, for allies, enemies and familiars, after the game's own start of a turn (the stun ended, the poison and regeneration done). `ctx:damage(n)` takes HP and shows it as the game's damage number, stopping at 1 HP as poison does; `ctx:heal(n)` gives HP, up to the most HP, with the game's regeneration effect; `ctx:skip()` makes the turn pass, as a stun does; `ctx:log(text)` adds to the turn's log line. It also runs on the turn a stun ends, with `ctx.passing` true. `ctx` has `iic`, `unit`, `side` and `turn`.
- `rq.battle.on_hit(fn)` runs after each physical or magic attack on a target, once per hit (multi-hit skills, skills on many targets, counters), with `attacker`, `defender`, `skill`, `kind`, `damage`, `missed`, `crit`, `downed` and `counter`. `ctx:log(text)` adds to that hit's log line. A turn that only starts a charge is not reported.
- `rq.combat.on_magic(fn)` returns a percent of a spell's final damage, as the final percent of `on_physical` does for physical hits. The percents of every callback multiply.

Each returns a remover. An error in one callback is logged and the next still runs. The three are Lua inside the engine (`src/lua/battle.lua`), over `rq.ain.hook`.

## 2.0.0

Each mod has its own global variables and its own `require` cache. Before, all mods shared one global table and `package.loaded`: a global set without `local` in one mod was seen and overwritten by every other, and when two mods each had a `util.lua`, `require("util")` gave the second mod the first one's. Now a global stays in its mod, and so does every chunk the mod loads (`init.lua`, `require`, and `load`, `loadfile` and `dofile` when given no `env`), with the callbacks made there. Names a mod has not set itself (`rq`, `string`, `pairs`...) are still found as before. Inside a mod `_G` is its own table, `package.loaded` its own cache, and `pairs(_G)` lists only its own globals. The metatable of `_G` is protected, so `setmetatable(_G, ...)` raises an error.

Mods share on purpose instead: what a mod's `init.lua` returns is its shared value. A mod that lists its id in `dependencies` gets it with `require("<id>")`; any mod gets it with the new `rq.mod.get(id)`. It is the same value, not a copy. A library's own modules and globals stay its own, also when another mod calls its functions. Added `rq.mod`: `get`, `id` (the calling mod's id) and `list` (the mods that finished loading).

The `rq` table and the standard library tables (`string`, `table`, `math`, `utf8`, `coroutine`, `os`, `io`) stay one table for every mod. After each mod's `init.lua`, the loader logs each field it added, changed or removed in them, such as `my-mod changed rq.log, in a table every mod shares` (`rq` three levels deep, names starting with `_` skipped, at most 20 lines per mod). It only logs; the change stays. Changes made later, in callbacks, are not logged.

Also: a module file that does not compile now raises `error loading module ...` (before, `require` said the file was not found). `loadfile` takes its third argument, `env`, as Lua's does (it was ignored). The mod a call belongs to (for files, `require` and `rq.mod.id`) is the one whose code is nearest on the stack, so a library's code counts as the library.

Tools: `rqmod-ctl where` samples the game thread five times, 200 ms apart, and writes its native stack (with symbols), the AIN call stack and the last log lines to `logs\rqmod-where-<time>.txt`, for a game that hangs. The pipe answers it while the game thread is stuck.

Major, because code that relied on another mod's globals no longer sees them. No shipped mod did. Mods keep running on 2.0.0 unchanged; only a mod that uses `rq.mod` or shares a value needs `"loader": "2.0.0"`.

## 1.16.1

`rq.ain.find` writes each function's name in its log line (`find 'Encount' fno=10733 T_Player@checkEncount`); before, the line gave only the number, which no `rq.ain` call takes. The docs gain a guide on finding and using the game's functions.

## 1.16.0

More kinds in `rq.ids`: `monster` (372 monsters, as `rq.battle.start` takes them: `rq.ids.monster.COCKROACH` is 358; the extractor loads each number into the game's scratch slot, as the game does to name one), and, each read from the game's own name functions, `race` (16, `rq.ids.race.HANNY` is 8), `chara_type` (6, `HUMANOID` is 22), `element` (6, `NOTHING` to `FIRE`), `item_kind` (17 weapon and armor kinds, `SWORD`, `SHORTSWORD`, `SPEAR`, `GLOVE`, ...) and `target` (8 skill target codes, `MELEE` to `RANDOM_TARGET`; the game names these in Japanese only, so their English names are ours). `rq.ids.find`, `find_all` and `name` take the new kinds, and the error for an unknown kind lists them all. Some repeated names now have keys without the number beside their numbered ones, from `data/ids/preferred.tsv`: the plain key for the version players know (`rq.ids.skill.FORTUNE` is 448, `FIRE_BLAST` is 169, `rq.ids.chara.RICK_ADDISON` is 93; 19 in all) and keys of their own for the other versions (`CAPTURE_EX`, `USE_IBEPROFUN_EX`, `USE_IBEPROFUN_EX_PLUS`, `STAMINA_BOOST_1`, `ATTACK_BOOST_1`, `MAGIC_BOOST_1`). `rq.ids.find` gives the plain key's number for a repeated name ("Fortune" is 448) and finds the keys of their own. The extractor also reads the game's class and state lists, and `gen_ids.py` fails when they differ from `rq.ids.class` and `rq.ids.state`. The engine's CI runs `gen_ids.py --check`. The numbers of existing keys did not change.

## 1.15.0

`rq.ids`: the game's numbers by name, so a mod can write `rq.ids.skill.FORTUNE_448` or `rq.ids.item.POISON_MASK` instead of 448 or 195. Six kinds: `chara` (89 characters), `class` (8), `item` (304), `quest` (199), `skill` (486) and `state` (4). Keys are the English name in upper snake case; a name the game uses for several numbers gets the number as a suffix on each. A missing key raises an error, and nothing in `rq.ids` can be changed. `rq.ids.find(kind, name)` looks up a name (without case or punctuation, é as e) and says when it is ambiguous, `rq.ids.find_all(kind, text)` lists every number whose name holds a text, and `rq.ids.name(kind, no)` gives a number's name. Editors complete the keys from the new `lua/rq_ids.lua`. The names come from the game through the public calls (`tools/ids/extract.lua`) into `data/ids`, and `tools/ids/gen_ids.py` builds the module, the annotations and the docs' data tables from them; only names and numbers, no game text.

## 1.14.2

Docs. Every namespace, function and type in `rq.lua` is written in the reference format (summary, details, `Since:` and `Changed:` lines, parameters with units and defaults, named returns, examples), with the details of the old HTML guide merged in and each claim checked against the engine. Corrections: `rq.chara.set_buff` does not need `install_flame`; `rq.battle.set_drop` raises an error only for a value of the wrong type; `rq.hud.block_keys` and the `text_*` calls date from 0.3.0; `rq.item.equipped` takes one argument. The 22 `rq.scene` commands that had no entry are documented. No behavior changed.

## 1.14.1

Docs and tooling. `rq.lua` now declares `rq.skilllist`, `rq.debug` and `rq.agent`, so editors complete them; `rq.speed` is written in the new reference format. The agent pipe answers `apidump` with every `rq.*` entry the engine exposes before mods load, for the docs coverage check (`tools/apidoc`). The window title shows RQ MOD and the loader version, and the window and exe use the RQ MOD icon.

## 1.14.0

Added `rq.scene.start` and `rq.scene.active`: a scene from any place, at the next frame, one at a time, after the System menu, Config or a scene of the game's own. Tried in every place the game has (see Places under `rq.scene`). Item Previews also hide while Config opened from a message is up.

## 1.13.0

The title during a mod scene, or under any Lua call that waits in the game, no longer leaves Lua's calls open: they end with the error `"rq: the game went to the title"` before the reset, so a scene's coroutine ends and no level of Lua's C call budget is lost. Added `rq.on_reset`. `rq.sprite.on_reset` now answers the remove function it was documented with. A hook whose callback the title cut off runs again. `rq.ui.get` lists the System button in a fight.

## 1.12.0

Added `rq.battle.set_face` and `get_face`: a face per character on the fight cards only, lasting or for a while, from a CG or a GIF, drawn in the place of the game's face so its moves, shakes and flashes stay. Added `rq.battle.on_hp`: every HP change in a fight, and the first sight of each character on a card.

## 1.11.0

`rq.sprite` `attach`: follow a battle card by place (`card`) or by character (`chara`), another mod sprite, or a game sprite, with `x`, `y` and `z` added to the target's. Hidden with it, and gone with it or at the end of the fight. `s:get()` adds `attach` and `drawn`.

## 1.10.0

`rq.sprite` shows GIFs (`gif`, `fps`, `s:play`, `s:stop`, `s:frame`, `s:playing`) and moves over time (`s:to` with `ms`, `delay`, `ease` and `on_end`, `s:moving`, `s:halt`), on the game's clock or `clock = "real"`.

## 1.9.0

Added `rq.sprite`: sprites a mod makes once and changes later, among the game's own in z order, so its windows cover them. CG, part of a CG, fill or text; scale, turn, alpha, tint, add colour and blend. `rq.sprite.scene` and the pipe's `scene` command list the game's scene back to front. A load and the title remove every mod sprite (`rq.sprite.on_reset`).

## 1.8.0

Added `rq.config`: a Mods tab in the game's Config screen, with a page per mod. Added `rq.image.compose`, `rq.store.global`, `rq.agent.widgets` and `rq.uikit.layers`. Kit widgets are listed in `rqmod-ctl ui`. `rq.hud.text` and `rq.hud.text_width` take `bold`. HUD text is in VL PGothic, each letter at its own width, so `rq.hud.text_width` gives smaller numbers for Latin text than before.

## 1.7.0

Added `rq.uikit`: label, button, checkbox, choice, slider, tabs, panel, list and a menu with levels, in the look of Config, with row and column layout. Added `rq.input.scroll`. `rq.hud.text` style takes `edge = false`.

## 1.6.0

Pieces for game-styled HUDs. `rq.hud.cg` takes `{src, w, h, alpha, tint}` to draw a part of a CG, stretched, faded or tinted. Added `rq.hud.cg_size` and `rq.hud.clip`. `rq.hud.text` style takes `a`, and `w`, `h`, `align`, `valign` to place text in a box. `rq.input.mouse` also returns the left button's press and release for this frame. Fixed: with more than 48 different CGs drawn, `hud.cg` showed the first CG instead of the asked one; it now holds 160 and draws nothing past that.

## 1.5.0

Added `rq.dungeon.place_player`, `rq.dungeon.grid({whole = true})`, `room.no` and `reach` on each event. `rq.battle.set_mark` takes a third argument for one character or one card.

## 1.4.0

Added `rq.sound`: `play` (a game number or a WAV, OGG, FLAC, Opus or MP3 file in the mod folder), `play_flash` and `flash_info` (a sound inside a Flash file), `stop`, `playing`, `set_volume`.

## 1.3.1

Fixed: skip mode passed mod text the player never read, because every `rq.scene` line shared one read flag; each line now has its own, kept in `rqmod-msgskip.dat` beside the game's file. `rq.battle.on_down` no longer fires again for a character who is already down.

## 1.3.0

Added `rq.ain.patch_int_after`, which finds a constant by the global read before it. Fixed: `rq.ain.patch_int` and `patch_float` found nothing in a function the loader wraps, such as `Ｔ戦闘前初期化`; they now reach the game's code.

## 1.2.1

Fixed: `rq.chara.edit` did not show on a character already in a save until the game recalculated that character (a fight, a level, new gear). Each edited character is now recalculated once right after a save loads.

## 1.2.0

Added `rq.speed.set` and `get`: the game clock can run faster than real time, with sound and the save's play time kept real.

## 1.1.0

Changed: `rqmod.log`, `rqmod.prev.log`, the crash reports and `rqmod-unclean-*.log` live in a `logs` folder beside `mods`, no longer inside it. The first start moves the files an older loader left in `mods`.

## 1.0.0

Removed: the root aliases `rq.dungeon_camera`, `rq.patch_float`, `rq.skip_msgbox`, `rq.skip_sdl_msgbox` and `rq.find`. Use `rq.dungeon.camera`, `rq.ain.patch_float`, `rq.ain.skip_msgbox`, `rq.ain.skip_sdl_msgbox` (added) and `rq.ain.find`. Fixed: `rq.battle.skill_usable` said true for a greyed-out button during select, so Space in `space-standby` used Standby with no uses left. Sounds inside Flash files (battle effects, coins, achievements, level up) and other sounds with no entry in the game's list now play on the Sound Effects volume instead of Master alone.

## 0.31.0

Added `rq.battle.install_states`, `states` and `set_state`, and the mod `mods/states-at-once`.

## 0.30.0

Added `rq.battle.set_mark`. `set_buff` and `set_rank_buff` take `order`, `x`, `y`, `layer` and `pinned`. `buffs` says `pinned`, and lists someone switched out by order. Fixed: after going to the title from a fight made by `rq.battle.start`, `rq.party.set` and `rq.battle.start` kept answering that a battle was on.

## 0.29.0

Added `rq.battle.set_rank_buff` and `on_switch`. Changed: `set_buff` stores the buff by character, so it no longer passes to whoever takes the card, and `buffs` answers for someone switched out. `set_flame` goes with the character when the party changes places. The control list of a fight has `switch` when the game allows a switch.

## 0.28.0

`rq.battle.set_buff` and `buffs` accept enemies. Changed: enemy cards now show all their marks in turn, with or without mods.

## 0.27.1

`rq.battle.set_buff`: a still icon is drawn as a mark of the game, under the game's windows, and a number that is no CG raises an error. New text on a GIF buff shows at once. A buff and a flame on one card now take turns.

## 0.27.0

A save under a Lua call is refused wherever it comes from, and a load there ends with a clear error in place of a crash.

## 0.26.0

Added `rq.battle.time` and `set_time`. A bad character or skill number in `rq.chara`, `rq.orb`, `rq.skill` and `rq.shop.stock` no longer closes the game: calls that write raise a Lua error, and calls that read answer 0 or an empty table. `rq.ain.call` refuses the game's save and load functions.

## 0.25.0

Added `rq.battle.on_use`, `rq.dungeon.grid` and `rq.dungeon.place`.

## 0.24.0

`rq.ain.global`, `set_global` and `global_len` take field names to go into a struct. An index on a plain value now raises an error, where it could read an unrelated array.

## 0.23.0

Added `rq.quests.start`. Every `on_*` call, `rq.on_frame` and `rq.ain.hook` now return a function that removes the callback. `rq.log` names the mod through the loader's own Lua functions. `rq.ain.call` raises an error for a method instead of calling it with no object.

## 0.22.0

Added `rq.party.get` and `set`, `rq.battle.start` and `force_hit`, `rq.random.seed` and `fix`, `rq.ain.global`, `set_global` and `global_len`. Chest rolls and `rq.item` loot rolls now use the game's generator, so `rq.random` reaches them.

## 0.21.0

Added `rq.ui.shot` and `shot_result`. `rq.ui.aim` no longer needs a `rq.ui.get` before it. Changed: a chunk made with `load()` now always belongs to the mod that loads it, whatever name it asks for, so `rq.log` shows the mod and `io` reaches its folder. `rq.ui` says `other` instead of `title` on a screen with few or no controls, and `boot` only before the first named screen.

## 0.20.0

Added `rq.input.code`, `set_key`, `set_mouse`, `wheel` and `release`, `rq.ui.get` and `aim`, `rq.time_ms` and `rq.traceback`. An error in `rq.on_frame` is logged once per new text instead of on every call.

## 0.19.1

Calls that need the running game, such as `rq.skill.get` and `rq.hud.text_width`, raise a Lua error at the top level of a mod instead of crashing the game. Some of them, such as `rq.chara.get`, returned nil there before.

## 0.19.0

Added `rq.image.add_gif`, `remove_gif` and `gif_info`. `rq.battle.set_buff` takes `anim`.

## 0.18.1

Fixed a crash when `face` or `portrait` was a file path in `rq.chara.define` or `edit`. Custom character numbers no longer log a TADA error line.

## 0.18.0

Added `rq.scene`, `rq.ain.call`, `rq.ain.hook`, `rq.quests.current`, `rq.quests.on_event` and `rq.quests.on_event_after`.

## 0.17.0

Added `rq.ain.patch_int`. Shipped the `nozomi-okita-qol` and `copandon-dot-qol` mods.

## 0.16.0

Added `rq.battle.set_buff` and `buffs`. Changed: ally cards now show all their marks in turn, with or without mods, and `set_flame` no longer replaces Protect, Berserk, Stealth or Barrier. `install_flame` is still accepted but no longer needed.

## 0.15.0

Added `weapon`, `armor`, `item`, `special` in the character template, the `gear` chest pool in `rq.loot`, a grey placeholder for items without an icon. Changed: `rq.item.edit` now reaches instances already in the save; `rq.loot.add` without `pool` now includes `gear`; those four fields in `rq.chara.edit` no longer write an instance number.

## 0.14.0

Added `info.pct` in `rq.chest.on_attempt`. Changed: `rq.chara.on_recalc`, `rq.skill.on_describe`, `rq.chest.on_attempt` / `on_result`, `rq.orb.on_heal`, `rq.counter.on_guard_counter`, `rq.battle.on_select_key` and `rq.skilllist.on_open` / `on_page` / `on_buttons` now keep every mod's callback (before, the last one won).

## 0.13.0

Added `rq.battle.on_support`, a list of offers and a `points` price in `rq.chara.on_offer`. Changed: `rq.chara.on_offer`, `rq.combat.on_physical`, `on_accuracy` and `on_crit` now keep every mod's callback (before, the last one won). Shipped the `kaoru-quincy-qol` mod.

## 0.12.0

Added `rq.combat.on_crit`, `defender_type` in the physical and crit contexts, `rq.battle.on_down`, `rq.battle.install_flame` / `set_flame`.

## 0.11.0

Added `rq.item.equip(ii, iic)`.

## 0.10.0

Added `rq.item.remove(ii)`. Shipped the `binoculars` mod.

## 0.9.0

Added `rq.shop.on_buy`, `rq.loot.add / remove / on_pick` (chest pools item, special, rare, ultra), `rq.battle.get_drop / set_drop`, `rq.quests.on_end`, `rq.dungeon.on_map`; `group` and `rank` in the battle contexts; `party` in the quest-end context. Changed: `rq.shop.on_stock` now keeps every mod's callback (before, the last one won). `rq.shop.stock / in_stock` accept text ids.

## 0.8.0

Added `rq.item`: `define`, `give`, `get`, `set`, `transform`, `edit`, `equipped`, `number`, `id_of`, `on_create`. Item icons accept a file path (100x100). The engine grows the restock array and wraps `Ｉ生成／固有データ／Ａ`, `Ｉ生成` and `Ｔアイテム屋／入荷品` the first time `rq.item` is used.

## 0.7.0

Added `rq.quests.on_clear`, `state`, `set_state`, `unlock`, `new_this_run` (`rq.quests()` still lists quests). The engine wraps the tail of `クエスト終了処理／クリアフラグ` the first time `on_clear` is used.

## 0.6.0

Added `rq.image` (`add`, `replace`, `restore`, `info`): PNG, JPEG and WebP files from the mod folder served as game CGs. `face` and `portrait` in `rq.chara.define / edit / set` now accept a file path. `rq.chara.recruit` and `dismiss` refresh the Party tab's character list. The engine asks the image registry first in `asset_cg_load`, `asset_exists` and the CG metrics calls.

## 0.5.0

Added `rq.battle.on_start` / `on_end`, `rq.skill.patch`, text ids for skills (`define` now returns the id; `get` and `sort_as` accept them), more fields in `rq.skill.get`, `rq.chara.recalc`, and battle-state fields in `rq.chara.get / set` (`status guard stealth berserk bless_all barrier atk_buff def_buff charge`). Up to 128 skill define / patch calls (was 32).

## 0.4.0

Added the character roster API on `rq.chara`: `define`, `recruit`, `find`, `is_recruited`, `dismiss`, `number`, `id_of`, `edit`, `get`, `set`, `skill_points`, `add_skill_points`, `forget`, `on_create`, `on_forget`; and `rq.store` (`get`, `set`, `delete`, `keys`). The engine now wraps `Ｃ生成`, `Ｃ生成／キャラデータ` and `ＣＳ削除` the first time one of these is used.

## 0.3.0

Added `rq.saves`; `rq.hud.block_keys`, `text_begin`, `text_value`, `text_end`; `rq.agent.control` rect form documented. Changed: `rq.on_frame` now keeps one callback per mod (before, the last mod to register replaced the others). Engine draws the main-menu version banner.

## 0.2.0

First versioned loader: manifests, dependencies, load order, sandbox, `rq.*` modules up to `rq.battle`.
