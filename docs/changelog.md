<!-- Copied from the engine's CHANGELOG.md by scripts/sync.py. Edit it there. -->

# Changelog

Each version is the loader version mods see as `rq.version` and declare as `loader` in `mod.json`.
A patch version fixes or adjusts behavior, a minor version adds calls or fields, a major version removes, renames or changes the meaning of a call.

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
