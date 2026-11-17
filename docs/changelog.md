<!-- Copied from the engine's CHANGELOG.md by scripts/sync.py. Edit it there. -->

# Changelog

Each version is the loader version mods see as `rq.version` and declare as `loader` in `mod.json`.
A patch version fixes or adjusts behavior, a minor version adds calls or fields, a major version removes, renames or changes the meaning of a call.

## 2.59.1

A fix the Lab found with World 3 No Level Cap 1.0.0 (`notes/plans/plan-world3-no-cap.md` in the workspace).
- `rq.ui.get`'s `status.noLimit` is the ∞ the game draws (the status card's `m_bInfinity`, from the game's no-cap check by the character's number). The character's data overwrote it with a cap of 2147483647, which the game never stores (its caps stop at 999, 9999 in World 3), so it was false for every character, Rance too. The `units` rows whose card is shown already read the card. `rq.ui.get`'s doc says where `level`, `levelLimit` and `noLimit` are, and where `noLimit` stays false (the `party` ranks' cards show no cap; rows whose card is not shown read the data).
- The Lab: the new `world3-no-cap` checks World 3 No Level Cap, with `noLimit` on the status page and the shown `units` cards in World 3 and World 1.

## 2.59.0

The status page's MODS list (`notes/plans/plan-status-mods-list.md` in the workspace), as Moru designed it: the title row by the X has room for two mod buttons, and a third had no place.
- `rq.gamebutton`'s `"status"` group: when more than two title entries are shown on a draw of the card and one of them may go in a list, or a shown entry has `list = true`, the title row has one button instead of the cells, **MODS**, over both cells (the look of the page's SKILL SCREEN button, x 436, y 62, 68 × 27). Its click, or Enter on it, opens a list under it: one row per entry, in the order they were added, each the map tabs' grey bar with the entry's icon and its `text`, as wide as the widest row, the tip right of the list under the mouse, darkened while `enabled` is false. A row's click closes the list and runs the entry's `on_click` (from the frame's update, with the page there); a darkened row plays the deny sound. A click off the list, the right button or Esc only close the list; so do another character and the page closing. While it is open the page takes no mouse and no keys: the arrows move between the rows, Enter clicks one. MODS comes and goes with the entries shown on each draw. Up to two entries, nothing changes.
- New fields on a `"status"` title entry: `list` (nil, in the list whenever there is one; false, never: no button while MODS shows; true, the list shows for it even alone), `text` (a string or a function of the character and the mode: the words beside the icon in its row; with `list = true` an entry may have a text and no icon), and `on_state(state, chara, mode)`, called when the entry's place changes. The handle's `state()` gives it: `"button"`, `"row"`, `"aside"` or `"hidden"` (`rq.GameButtonState`). `set` takes `text`.
- `rq.gamebutton.groups()`: the `"status"` group's `list` (`rq.GameButtonList`: shown, open, MODS's button and place, the rows' width and entries), and each entry's `state`, `list`, `row` and `text`; a row's `x` and `y` are its place in the list.
- Agents: MODS is the control `status-mods`; while the list is open each row is the kit's button `button-<mod id>-<id>`.
- `rq.knownskills`' bar and Page Up / Page Down on the status page wait while the list is open over them.
- The Lab: the new `status-mods` checks the rule (MODS for a third entry and for `list = true`, back to cells for two), the rows, the tip, a greyed row, a row's click, the closings, the keys, `on_state` and `state`; `statuspage` shows its second entry only when a cell is free for it.

## 2.58.0

What Rocky Chunk Indicator 1.0.0 needs (`notes/plans/plan-rocky-chunk-indicator.md` in the workspace), from a player's suggestion on the Discord: a mark on the status page for a character who already had a Rocky Chunk's effect, and a question before another chunk goes on such a character.
- `rq.gamebutton`'s `"status"` group has a second spot, `spot = "left"`: icons that are not buttons, at the page's top left (the left end of the LV row, under the class icon), two cells at x 20 and 56, y 90, 32 × 26, apart from the title row's two by the X, which Morurun Items and Loadouts fill. They are made as the title cells are (buttons of the page's own group, their faces composed from the page's background), so they hide with the page and under the game's windows. A left entry has no `on_click` (an error with one): no press, no sound, and the keys pass it by; under the mouse it lights up as the title buttons do and its tip shows with the label as its title, `enabled` false darkens it, `shown` false gives its cell to the next. `spot = "title"` is the default.
- `rq.gamebutton`'s `"status"` entries take `icon` as a function, `icon(chara, mode)`, asked on every draw of the card as `shown`, `enabled` and `tip` are, so an icon can change with the character shown; an answer that is not a CG number leaves the entry out of that draw. `rq.gamebutton.groups()` gives a `"status"` entry's `spot` and the `icon` it shows.
- `rq.item.on_try_equip`: a callback when the player puts an item on a character on the game's screens (a drag onto a character's row in the vault's or the storage screen's equip list, a drag from the shop's rack onto one, a pick in the status page's item list), before the game's own questions, with `rq.TryEquipCtx` (the item, the character, the slot, the item it would replace, `from`). It returns false to stop the attempt, and may ask the player with `rq.ui.confirm` first. It does not run where a grey row, a refusal (the game's or a mod's), `rq.shop.on_can_buy` or not enough money stops the attempt, nor for equips a mod makes. `rq.item.on_can_equip` cannot ask, since the game also runs it for the filters, the equip list's rows and the list of who can wear an item.
- The Lab: the new `rocky-chunk` checks the left spot (the cells, an `icon` function, a silent click, the tip, the keys passing it by) and `rq.item.on_try_equip` on the status page's pick, the vault's drag and the shop's drag, with Rocky Chunk Indicator's question; `statuspage` counts only the title cells for its own entries.

## 2.57.0

The leftovers of the Test Lab's catch-up (`notes/plans/plan-catch-up-leftovers.md` in the workspace, from `plan-lab-catch-up.md` section 6), as recommended there and taken by Moru.
- `rq.item.on_unequip`: a callback each time an item comes off a character, with `rq.UnequipCtx` (the item's instance, number and id, the character, the slot, whether it came off through the game's equip call, the item put in its place, whether the game deleted it as it came off). It hooks `Ｃアイテム外す`, the one place the game takes an item off: REMOVE in the vault and on the status page, a drag, a swap, `rq.item.equip`, `rq.item.remove`, `sell` and `donate` on a worn item, and the game's own removals (a character removed, a Morurun absorbing a Special item, a quest's event). Through the equip call it runs once that call has ended, before `rq.item.on_equip` for the item put in its place. `rq.item.on_equip`'s doc points to it.
- `rq.knownskills`: Page Up and Page Down turn the known skills' page on the status page and in the skill window, with the controls (`install`'s `controls`); held, they turn again after 400 ms and then every 150 ms. The game reads Page Up there only in a message's wait (the backlog) and both only in Config's sliders.
- A gamepad does nothing yet, and the install guide and the README say so: Rance Quest reads the pad through `IbisInputEngine`'s joystick calls, which the engine leaves unimplemented, as upstream xsystem4 does. Pad support is planned later on its own.
- `rq.chara.clear_slot`, `set_slot`, `set_flavor`, `set_uses` and `set_bar` raise an error for a row outside 1 to the list's last row (20, more with `rq.knownskills`). The game checks a row only against its top (21), so a negative row was a fatal VM error that closed the game ("Out of bounds page index"), as the Lab's `badnumbers` found with `clear_slot(20, -1)` in the general run.
- The Lab: the new `unequip` checks `rq.item.on_unequip` (a swap through `rq.item.equip`, the same item again, `rq.item.remove` on a worn item, `Ｃアイテム外す` called as the game's events call it, a Lab item that vanishes, the status page's REMOVE); `known-skills` turns the pages by Page Up and Page Down on the status page and in the skill window; `badnumbers` gets through every call again. The general run at 2.56.1 (122 scenarios, 6424 checks) found the `clear_slot` crash and three stale or flaky checks in the Lab, fixed there.

## 2.56.1

The fixes for what the Test Lab's catch-up found in its section D (`notes/plans/plan-lab-catch-up.md` in the workspace, section 8, F6 to F9), as recommended there and taken by Moru.
- A draw no longer freezes the game. A fight whose last enemy falls in an action that leaves no ally standing ends with the game's result 3, and `戦闘後処理(re)`, the game's work after a fight, ends with a loop that writes the result to the user log and leaves for 1, 2, 4, 5 and 6 only: for 3 it spun for good. The game itself never draws (no skill downs its own user), but a mod can, as the Lab's `fight-start` did by downing Rance in `rq.battle.on_hit` as his hit took the last enemy. The loader's wrapper on `戦闘後処理` (`src/modloader_events.c`) now hands it a 4 for a 3, whose line says "Draw"; nothing else there reads the value, the callers keep their own, and `rq.battle.on_end`'s `result` and `rq.FightResult`'s `code` stay 3 (`how` `"draw"`).
- A skill on the whole party (Recovery Rain) no longer heals the party's empty places. The game's `戦闘味方_全体補助` asked at each of the five places whether its user stood (`戦闘番号_存在確認(nNo)`), not whether a character stood there, so an empty place got the skill too: `rq.combat.on_heal` with `target` 0 and a line with no name in the battle log ("   recovered 224 HP."). The loader changes the call's argument to the place (`nTargetNo`) when `src/lua/combat.lua` loads (`priv.patch_call_local`, `src/modloader.c`), as the game's own `戦闘味方_全体加護` checks it. A downed ally still counts: the check is the place's character, not its HP. The familiar's whole-party skills go through the same function.
- `rq.world.current()` is nil at the title. The game sets its world to 1 when it starts (`Ｔ初期化`, before the title), so this answered 1 there, and what reads it as "a save is loaded" took the title for one: `rq.config.settings`' `"save"` pages were not greyed and took changes that the next load dropped, and `rq.game.mode` answered `"classic"`. The loader now knows a save is loaded from the game's load (`Ｔロード直後処理`: the autosave and the suspend save) or a quest's start (`Ｔクエスト`, a new game's prologue first) until the title shows again (`タイトル画面`), in `src/lua/gamedata.lua`.
- `rq.battle.on_forecast`'s doc: the battle screen asks for the line only for a skill aimed at an enemy, so a skill aimed at an ally gets no line and no call, and for a support skill aimed at an enemy `ctx.text` is "" (the game builds nothing) while the callbacks still run.
- The Lab: `fight-start` plays the draw (`on_end`'s 3, the second value's code 3 and `"draw"`, the user log's "Draw" line); `heals` checks two heals and no line with no name for Recovery Rain with Rance and Lia; `settings` checks the title's `rq.world.current()` and `rq.game.mode()` nil and the `"save"` page's row and Reset greyed there; `monster-define` checks `Ｃログ情報` (the user log's character info) naming a mod's familiar and the Data-less Ghost; the new `monster-gone` makes a suspend save holding a mod's monster (a familiar item) and group (an area's list) and resumes it on a second boot with neither defined: the game group drawn in the group's place, the familiar built as the Data-less Ghost, the monster's kill kept for its return.

## 2.56.0

The fixes for what the Test Lab's catch-up found (`notes/plans/plan-lab-catch-up.md` in the workspace, section 8), made before its section C at Moru's word, with Binoculars 1.2.3 and Pluepet Rare Contract 1.0.1 (which needs 2.56.0 for its long page).
- `rq.ui.get` and `rqmod-ctl ui`: `busy`, what the game runs under the screen. `"event"` while one of a quest's own events runs (`クエスト処理` on the VM's stack: its messages, scenes and fight, with the map read between them, as before a goal's first line), `"fight-end"` while the game waits for a click after a fight (`戦闘後処理`: the result screen over the map, before a placed enemy is counted and removed); the inner one when both run, absent otherwise. Found by `rare-contract` (A3: the Lab took the map before Pastel's scene for the event's end) and earlier by `map-objects` (phase N). The Lab's `t.clear_quest` and `t.to_map` read it.
- `rq.dungeon.exploring()` is false through the game's result flow (`Ｒ８リザルト画面`, wrapped in C). Its background (`T_ResultBack`) builds the map again, and `T_MapParts@create` cleared the result screen's mark, so the map read as walked during the background's 500 ms fade-in: at the end of a quest with fights and no map (Incident at the Church, quest 46), Binoculars 1.2.2 took a pair worn there as gone in and broke it (A4).
- A choice menu too tall for the room under its place goes up just enough to fit on the screen, and the place in the menu's data is put back after (a hook on `T_Select@createBase` in `src/lua/dialog.lua`). It covers `rq.ui.choose`, `rq.scene.choice`, `rq.ui.ask` and the game's own menus; a menu that fits keeps the game's place (its top at y 360), and a centred one is left alone. Pluepet Rare Contract's 19 rows ran past the bottom and its "More..." could not be clicked (A3).
- `rqmod-ctl hover` (and so `press` after it) puts the mouse a pixel to the side for a frame first when it already rests on the control's centre, and on its second try: the game's choice menu takes a row only once the mouse moves. Advance Worlds' "Go to World 3" sits where "Go to World 2" was, so with nothing moving the mouse between the two (a player's clicks through the scene) the hover timed out (B3).
- `rq.ui.quest_storage`'s `"failure"` mode is explained: the game's call at a failed quest's end, which never shows a window, as the quest's end has deleted every Quest Storage item before it (A2).
- The Lab: `t.play_quest` (a quest with no map played to the hub), `t.to_map` through the result screen, `t.clear_quest` on `busy`; `map-objects` checks `busy = "fight-end"`, `binoculars` plays quest 46 with a pair worn, `rare-contract` checks that every row of its long menu is on the screen.

## 2.55.1

RQ Browser becomes Rance Browser 1.0.0, a program in its own repository (`notes/plans/plan-browser-repo.md` in the workspace), from the testers' request that it open other Rance games for the wiki, Rance VI first. No `rq.*` call changes; the version is raised for the program that ships with this loader, as in 2.43.0 and 2.52.1. From now on a new browser version in the package is named in the loader version that carries it, and a browser change alone raises no loader version.
- The package's `xsystem4\rq-browser.exe` is now `xsystem4\rance-browser.exe`, **Rance Browser 1.0.0** (its title says "RQ MOD 2.55.1" beside its version). It reads an `rq-browser.json` beside it when it has no `rance-browser.json`, so the game folder it remembered stays.
- For Rance Quest Magnum nothing else changes: the same tabs, counts, names and Lua lines. The CG details show the format and size in the grid too, and a CG picked from the Names tab is brought into view in the grid.
- The browser opens other System 4 games: Rance VI - Collapse of Zeth (tested; its CGs in labelled groups, its battle effects with their masks, music with its loops, sounds, the `.alk` pictures and the dungeon textures) and others marked "not tested". The Names tab and the Lua lines show for Rance Quest Magnum only.
- The source left this repository: `tools/rq-browser` and `third_party/cimgui` are now `subprojects/rance-browser`, a git submodule of `RQ-Modding/rance-browser` (GPL-2.0-or-later, with Dear ImGui and cimgui). `meson.build` builds it as a subproject with the loader's own `data/ids` and `dist/lua/rq.lua` (meson options `rq_ids_dir` and `rq_lua`), so the build still fails when a Lua line names a call `rq.lua` lacks. The browser shares the engine's libsys4. Clone with `--recurse-submodules`, or run `git submodule update --init --recursive` in a clone made before.

## 2.55.0

The calls Dynamic Immature needs (`notes/plans/plan-dynamic-immature.md` in the workspace), from a tester's request to remove the Immature trait: a Special item that gives its wearer Immature (skill 373) when equipped, one that takes its penalty away, each refused with its reason. In Lua over `rq.ain` (`src/lua/item.lua`, `skills.lua`), but for `only` in C (`src/modloader_scene.c`).
- `rq.item.on_equip(fn)`: a callback each time an item is put on a character, after the game's `キャラ_装備設定` returns true (the vault's and the storage screen's drag, the status page, the shop's buy onto a character, `rq.item.give` with `to`, `rq.item.equip`): the stats are worked out again and a Special item's own effects done. `rq.EquipCtx`: `ii`, `no`, `id`, `iic`, `chara`, `slot` (`"special"`, `"weapon"`, `"armor"`, `"item"`), `kind` and `old` (the instance it replaced, deleted by then when it vanishes). The same instance put on again does not call it.
- `rq.item.on_can_equip`: a refusal's text, `return false, "why"`. The text of the last callback that refused with one counts, unless a later one returns true. A drop on a greyed character in the vault's equip list (`T_EquitItem::setItem` on `g_sEquipDrag.m_sEquip`) shows it in the game's notice instead of "Unable to equip.". The status page's list greys what `アイテム_装備可能` refuses and a grey row cannot be picked, so for that list (`T_StoreItem@getItemActive` on `rq.ain.stack`) an item only a mod refuses with a text stays bright; picking it (`T_Status@equipItem` through `キャラ_装備変更`) shows the text and equips nothing. With no text, the game's behavior is as before.
- `rq.chara.on_has_skill(skill, fn)`: a callback on the game's check for a skill, `ＣＳ番号取得(iic, skill, fg)`, which `ＣＳ有無`, `ＣＳ有無／スタメン` and `ＣＳ総数取得／スタメン` ask through: false answers "no" for that one check (the function is skipped and returns 0), the skill row stays. `rq.HasSkillCtx`: `iic`, `chara`, `skill`, `mode` (`"held"`, `"set"`, `"unset"` for fg 0, 1, 2), `row` (the game's answer) and `caller`, the first function on `rq.ain.stack` past those helpers (`Ｃ再計算` for the stats). The skill table is empty while mods load, so only the range 1 to 1000 is checked.
- `rq.ain.hook`'s `only`: `{ [position] = value or { values } }`, up to 4 int arguments and 16 values each, checked in C before a callback runs (`only_pass` on the frame's locals), so a hook for one skill number on a function the game calls thousands of times a frame costs Lua nothing on the others. Each callback keeps its own `only`; the Lua wrapper that reuses a callback's C cell keys it by `only` too. The errors name the position and the function.
- The Lab scenario `dynamic-immature`: `only` and `on_has_skill` (the caller, the mode, the row), both items through `rq.item.equip` on an adult, a story child and a full list, the stats, a save and a load, the chests at each depth, the refusal texts in the vault and on the status page by drag, the vanish on removal, Frostbuy in the first and third worlds.

## 2.54.0

More known skills than the game's 17, in pages (`notes/plans/plan-known-skill-pages.md` in the workspace), from a tester's request: a character with Better Elemental Knowledge's Brawling Knowledges or Arrows, the passives and a Boost runs out of rows, and the skill window has no room for the skill that would free some. In Lua over `rq.ain` (`src/lua/knownskills.lua`), with Known Skill Pages 1.0.0 as the mod that installs it.
- `rq.knownskills.install{ most, controls }`: every character's skill rows (`Ｃ[iic].スキル`, 21) grow to `most` + 4, and new skills take rows 1 to `most` + 1 (the game's 1 to 18). `most` is 17 to 102, default 34. The game's code is changed where it counts the rows: the 21 of `sＣ`'s constructor (mods load before the game runs, so the boot's characters are made with the longer rows), the 16 row accessors and the 18 loops over the rows, the cap in `ＣＳ空き番号取得`, the hotbar's last row in `ＣＳ空き実装番号取得`, the battle's loop in `Ｔ戦闘前初期化／キャラ` and the 18 of the free-row check `キャラスキル_空き確認`. Every place is counted first, and nothing changes unless all are as expected.
- The save stays the game's: before `セーブデータ_保存` the rows past 18 go into the loader's key in `rq.savedata` and the arrays back to 21 (rows 19 and 20 empty); after it, and after `セーブデータ_読み込み`, they grow and the rows come back. A save made with no mod calling `install` drops that key.
- Pages: while the game builds the known list (`キャラスキル_保有一覧`, the status page's card and the skill window's), `キャラ_スキル数`, `キャラ_スキル番号` and `キャラ_スキル保有` answer the page's 17 and the item effect skill, and the game sorts them as before. The empty item slot (569) is left out, as the game's `キャラ_スキル番号` leaves it out. `rq.knownskills.most`, `page`, `page_count` and `set_page` (which draws the status page or the skill window again).
- The page controls, unless `controls = false`: a scroll bar 14 pixels wide at x 414 beside the status page's known skills (the game's bar cut to its bevels and middle, chosen by Moru from shots), the wheel over the skills, and the game's left and right arrows (CG 10003 and 10004) beside the skill window's KNOWN SKILLS heading. Kit controls `scrollbar-known-pages`, `button-known-prev` and `button-known-next`.
- `rq.ui.get`: `status.knownPage` and `knownPages`, and `skillShop.knownPage` and `knownPages`, once a mod installed the pages (1 page for a character with 17 known skills or fewer).
- `rq.chara.slots` lists the rows past 20 (it stopped at 20), and `rq.chara.skill_room` and `rq.chara.learnable`'s free rows count to the new most. In `src/lua/skills.lua` the rows are read to the array's length.
- `priv.patch_imm(name, local, from, to)`: the private call that changes a number in a function's code, as a plain `PUSH` or as the immediate of a fused compare on a local (`SH_IF_LOC_LT_IMM` and the like), reading each instruction's length from libsys4's table. With `from` equal to `to` it only counts.
- The Lab scenario `known-skills`: the rows, a Boost and Stone Throw past row 18 in stats and a fight, the bar, the wheel and the arrows, a full list at the new most, a save through the SYSTEM menu (the file holds 21 rows) and a load, Skill Again. `Ｃ再計算` with 34 known skills: 1.28 ms a call.

## 2.53.0

A mod's skill that takes the place of others (`notes/plans/plan-better-elemental-knowledge.md` in the workspace): Better Elemental Knowledge folds the five Brawling Knowledges, or Aegis's three elemental Arrows, into one skill row, and its row's purchase record has to count what was paid for the ones it replaced, so that Skill Removal Payback gives all of it back. In Lua (`src/lua/skills.lua`).
- `rq.chara.set_cost(iic, skill, cost)`: writes the purchase record of a skill the character holds (`rq.ForgetCtx.cost`, `rq.chara.slots`' `cost`); false when the character does not have it.

## 2.52.1

A fix in RQ Browser found by Moru: changing the kind in the Names tab sometimes closed the program. No `rq.*` call changes; the version is raised for the program that ships with this loader, as in 2.43.0.
- Names: the list drew the frame of a change with the kind it had before but the rows of the new one, so a kind longer than the last (Party states, 5, to Skills, 486) read past the end of the shorter one, and the program closed on the text it found there (an access violation in `msvcrt.dll`). Whether it closed depended on what lay in memory past the list, hence "sometimes". The rows now follow the kind they were made for, and the list reads its kind after the dropdown and the search.
- Names: another kind starts at its first row, not where the last one was scrolled to.
- The arrow keys, Page Up, Page Down, Home and End do not move a list while a dropdown is open over it (they moved the row under the Names tab's kind list).

## 2.52.0

The price of a change that erases skills, with what any mod gives back (`notes/plans/plan-new-mods.md` in the workspace, section 18): Loadouts counted only Skill Removal Payback's refunds before a load, through a call between the two mods. In Lua (`src/lua/skills.lua`).
- `rq.chara.forget_points(iic, skill, opts)`: the skill points the `rq.chara.on_forget` callbacks would give back for erasing a skill, without erasing it. Each callback runs with the ctx the erasure would have and `preview` true. `opts.player` as in `forget`; `opts.n`, `cost` and `kept` describe the row as it would be after a plan's steps (a skill not there yet, or one raised first). The `on_forget` wrapper keeps each callback until its remover runs, and returns the remover as before.
- `rq.ForgetCtx.n`: the skill's level in its row (most uses, rank, or 1), as `rq.chara.slots`' `n`.
- `rq.ForgetCtx.preview`: true when `forget_points` asks; false for an erasure. A callback should only count then.

## 2.51.0

An erasure a mod makes for the player (`notes/plans/plan-new-mods.md` in the workspace, section 17): Loadouts' erasures got Skill Removal Payback's points back through a call between the two mods; now any mod that erases for the player says so to `rq.chara.forget`, and any mod that pays back an ERASE sees it.
- `rq.chara.forget(iic, skill, opts)`: `opts.player = true` marks the erasure as the player's own, as the skill window's ERASE. The callbacks see it in `ctx.player`. Without it, a removal is the mod's own (onoha-qol's head start) as before.
- `rq.chara.forget` returns a third value, the skill points the `on_forget` callbacks gave back (already added to the character): counted in C in `roster_forget` while the call runs.
- `rq.ForgetCtx.player`: true for the skill window's ERASE (`caller` "キャラスキル_消去") and for `rq.chara.forget` with `player`; false for the game's other removals and a plain `forget`. `rq.ForgetCtx.mod`: the id of the mod that called `rq.chara.forget` (`rq.mod.id`), nil for the game's removals. In Lua (`src/lua/skills.lua`): `forget` marks its erasure while it runs, and the `on_forget` wrapper reads the mark for `caller` "lua", for that skill of that character only.
- `rq.chara.forget` checks its arguments in Lua: an error now names the mod's line, and `opts` or `opts.player` of the wrong type raises one.
- The reference's `on_forget` example pays back the erasures the player chose (`ctx.player`).

## 2.50.0

The calls Pluepet Rare Contract needs (`notes/plans/plan-rare-contract.md` in the workspace), from a tester's request: Pluepet tracks down a lost Rare Item for 50,000 Gold, the player chooses it in a scene over Frostbuy, and it comes to Rance's Room after three successful exploration quests, shown as the game shows an item from an event, with an autosave after. In Lua over `rq.ain` (`src/lua/item.lua`, `scene.lua`, `savedata.lua`).
- `rq.shop.on_can_buy(fn)`: a callback that can refuse a Frostbuy purchase before the game checks the money and asks "Purchase ...?". A before hook on `T_EquitItem@setItem`, the one place the game buys (the rack's drag onto the vault, index 999, or onto a character's row), for an item whose place is the shop's (6); a refusal skips the method, which returns false, so the drag puts the tile back, and its text shows in the game's notice. `rq.CanBuyCtx`: `ii`, `no`, `id`, `name`, `price`, `to` (`"vault"` or `"character"`).
- `rq.item.buy` runs the `on_can_buy` callbacks after its own checks of the item, and returns false and the refusal's text (shown in the notice when asking).
- `rq.ItemDef.keep`: the vault's DISCARD, SELL and DONATE refuse the item, as the game does for Chaos the Darksword (item 100): an after hook on `アイテム_破棄可能`, which all three ask, for an item number defined with `keep`.
- `rq.scene.item(ii, o)` (`s.item` in a scene): the game's moment for an item from an event, the jingle (`Ｒ８ジングル(1008)`, `o.jingle` another number or false) and `Ｒ８どこかからアイテム(ii)`, `T_ItemComment`'s window with the item's icon, name, level and effects, which waits for a click.
- `rq.saves.autosave()`: the game's own autosave (`自動セーブ(1)`, slot 30, the "Auto-Saving" message held 700 ms), on the hub only (footer mode 10, the SYSTEM menu's Save is on there too) and outside a quest. Rance Quest saves its globals with `system.GroupSave`, not the running code, so the call from Lua saves as the game's own does (the loader refuses only `system.ResumeSave` under a mod's call). Refused while the game saves: its message waits in UPDATE (`T_SaveMessage::wait`), so `rq.on_frame` runs under it.
- `rq.scene.play` and `start` hide the vault's and Frostbuy's item window (`g_sStoreItem`, z 9211 and up, over the message window at 8101 to 8301) while the scene plays, and show it again at its end. `T_StoreItem::setShow(false)` leaves the frame on the shown rack (`m_spLock`, CG 11416), so that one is hidden on its own.
- `rq.scene.start` and `rq.ui.choose` wait while the game saves (`自動セーブ`, `中断セーブ` or `セーブファイル_保存` on `rq.ain.stack`): a scene started from `rq.on_frame` during the game's autosave at a quest's end played inside the save, under its message.
- The Test Lab's `to_hub` goes back from the shop's racks and the vault too (`shop-buy`, `vault`, `vault-storage` in its BACK table): the "right click lost after a mod scene" in the plan was the Lab, not the game. The new scenario `rare-contract`.

## 2.49.0

The calls Frostbuy Bulk Buy needs (`notes/plans/plan-bulk-buy.md` in the workspace), from a tester's request: tick several items at Frostbuy, buy several copies of an item the shop restocks, and pay once. In Lua over `rq.ain` (`src/lua/item.lua`, `uikit.lua`, `uikit_vault.lua`), but for one C call.
- `rq.item.buy` runs the `rq.shop.on_buy` callbacks, as the shop's drag does (`T_Shop@buyItem`); a purchase a mod made was counted by no one before (Return Bonsai's price, Binoculars', Aten Gnu QoL's restock). The C side's `shop_buy` became `run_buy(ii)`, given to item.lua as a private `bought`.
- `rq.shop.restocks(no)`: whether the next visit puts another copy on sale once the one on sale is bought, by `Ｔアイテム屋`'s rules: a restock count (`◆アイテム補充数[no]`) other than 0, Forbidden Talent (304) from the third world on, Forbidden Talent - Weak (305) once quest 20 is cleared. The items sold only while the player owns none, once or never, and a mod's items, are false.
- `rq.shop.restock(no)`: what the next visit would do for that item, now: `rq.shop.stock(no)` when it restocks and none is on sale (the game's `入荷品` raises the count, so a weapon or armor comes a level higher). Returns the instance or 0.
- `rq.shop.next(no, n)`: the copies the shop would sell one after another, the one on sale first (`rq.ShopCopy`: `rq.item.info`'s row data, `ii` on the first, `plus` 1 to 9 for ① to ⑨). Each is read from the game's own creation at the count it would have (a quiet instance, deleted, the count put back); a weapon's or armor's copies go up a level each up to ⑨, and a copy that cannot change (past ⑨, a count of 0, an item whose data does not follow the count) repeats the last one without another instance.
- `rq.shop.restocks`, `restock` and `next` take a mod item's text id too (item.lua's private `no_of`, the C side's `resolve_no`).
- `rq.uikit.stepper`: `h`, the field's height from 18 to 30 (the buttons square, their text smaller), and `ends`: `"max"` (a MAX button after +), `"min"` (MIN before -) or `true` (both), listed as `button-<id>-max` and `-min`.
- `rq.uikit.item_row`: `mark`: false for an empty tick box at the icon's top right, true or a count for a ticked one, the count as "×n" at the icon's bottom right; the cyan cover and `selected` show the mark instead of `current`.
- `rq.uikit.item_list` and `item_picker`: `marks`, a table from a row's instance (or, for a row table without one, its index) to true or a count, which gives each row its `mark`.
- The Test Lab's `aten-qol` and `return-bonsai` buy with `rq.item.buy` alone (they called `T_Shop@buyItem` after it, which would now count twice); the new scenario `bulk-buy`.

## 2.48.0

The calls behind two reports from Moru's friends, for Loadouts 1.1.0 and Skill Removal Payback 1.1.0: a build the game sells only through other skills (Healing 2 once Healing 1 is at 3, Recovery Rain 2 once Healing 3 is learned, those then erased), two Attack Boosts, and the Boosts whose effect stays after they are erased. In Lua over `rq.ain` (`src/lua/skills.lua`).
- `rq.chara.learnable(iic, opts)`: `opts.after`, a list of steps (`rq.SkillStep`: a skill and a level, 0 erases it) set on the character before the list is made and undone after, for the list as it would be after those purchases or erasures. A step sets the level as it is (`ＣＳ追加`, `ＣＳ使用回数最大`, `ＣＳランク`, `ＣＳ初期化`); nil and the step's index when a step needs a new row and none is left. A second value: the free skill rows after the steps, as `skill_room` counts them.
- `rq.LearnableRow`: `step` (3 for skill 384, 1 for the rest), and for a row not for sale `needs` and `level`, read back from the game's text. The game names a skill by its name only: the loader takes the longest skill name that starts a condition, the list's and the character's skills first, and its level from what follows (`+`, ` N+` or stars). `Over LV N` is the level, full-width digits too (Melee Attack 4's `Over LV ４８`).
- `rq.chara.boosts(iic)`: the eleven Boosts (Stamina, Attack and Magic Boost, their second versions 455 to 457, and 279 to 283), each with `kept`: whether the character keeps its effect without the skill. In the third world only (`◆ワールド == 3`), the game's recalculation (`Ｃ再計算`) marks a Boost at rank 4 in `FA[38]` to `FA[45]` (1 for a first version, 2 for a second) and adds its effect while the skill is gone (+800 HP, +300 Attack or Magic, +50 to a rate); the list sells a second version once the first is at rank 4 or marked. `Ｃスキルドレイン` clears the marks, and a recalculation in another world does too. `learnable`'s steps mark a Boost set to rank 4 as the recalculation would.
- `rq.chara.on_forget`: `ctx.kept`, true when the erased skill is a Boost the character keeps.

## 2.47.0

The calls Return Bonsai and Aten Gnu QoL need (`notes/plans/plan-new-mods.md` in the workspace, phase R, step 3): the game's Quest Storage window's tiles, a free appraisal, locked cells in the item window, a picture as a button, an item stocked while the shop shows, and the moment the game sends a character home after a fight. In Lua over `rq.ain` (`src/lua/item.lua`, `basics.lua`, `uikit_hub.lua`, `uikit_windows.lua`), with the tiles listed in C.
- `rq.ui.quest_storage()`: the Quest Storage window (`g_sStoreQuest`, `T_StoreQuest`) while it shows: its `mode` (`"view"` from the map panel, `"give-up"`, `"failure"`), its z, whether the game's question shows over it (`g_sSelect`), and each tile with an item: its place (1 to 15), the instance, its box (100 × 100 from x 482, y 204, 106 apart) and `identified`.
- `rq.ui.quest_storage_refresh()`: builds the window again from the quest storage's items, as `T_StoreQuest::execErase` does after an erase (the list, `createIcon`, `setZ`, `setButtonActive`, `setShow`), for a mod that moved items in or out.
- `rq.ui.get`: the window's tiles are the controls `item-1` to `item-15` of the `quest-storage` screen, with the instance as the value.
- `rq.item.appraise(ii, opts)`: the game's `Ｉ鑑定` on an unidentified instance, where it is (a rare item's quest bonuses, the effects 21 to 25 capped at 99, the item number's name, icon and text); `opts.sound` plays the game's appraisal sound.
- `rq.item.get`: `identified` (false while `未確定` is 1).
- `rq.uikit.icon_button(icon, opts)`: a CG as a button, shrunk to fit its box and centered, with the item tile's yellow frame under the mouse or the keys, the picture moved 1 pixel while held and grey while disabled; a text tip has the label as its title.
- `rq.uikit.item_window`: `capacity`, the cells that hold items. A tile past it is darkened, cannot be clicked and has the vault's lock mark (CG 11419), and so has each empty cell past it on the page shown.
- `rq.shop.stock`: while the shop shows (`g_sStoreItem`'s `m_nStoreType` 3), the item is on its list at once (`アイテム倉庫_再作成`). `T_Shop::buyItem` builds the list before `on_buy` runs, so an item stocked from `on_buy` waited for the next visit.
- `rq.party.on_go_home(fn)`: at `割り込み２／戦闘後`, after each fight, when the game would send Aten (character 40) home (her `RAND(5) == 1`, 20%) or the wearer of item 209 (`ＰＴＡ＿Ｉ有無(209)`, always), both only in a party of two or more. `rq.GoHomeCtx` has the character, the reason (`"aten"`, `"item"`) and the chance; `fn` returns another chance from 0 (stays) to 100, or nil. The game's own roll is replaced only when the chance changed.

## 2.46.0

The calls Athena QoL and Rebecca Copley QoL need (`notes/plans/plan-new-mods.md` in the workspace, phase R, step 2): who can equip an item, a hit's damage limit and element, Athena's Studies, the game's Weakness Search shown from a mod, and the game's reset of a character's skills. In Lua over `rq.ain` (`src/lua/combat_more.lua`, `item.lua`, `skills.lua`).
- `rq.item.on_can_equip(fn)`: at `アイテム_装備可能`, the one check behind the vault, the status page, the shop, the storage screen's filters and `rq.item.buy` with a `chara`. `rq.CanEquipCtx` has the game's answer (`allowed`) and its reasons in its order (`reason`, `reasons`: "level", then "chara" or "class"; the game stops at the level, the loader works out the rest), the item's level and the character's. `fn` returns true, false or nil.
- `rq.combat.on_cap(fn)`: the damage limit of each physical hit and spell, and of the forecast. The game's raise by Damage Maximum (289) in `最終ダメージ計算` is taken out of the game's code (its 289 there patched to 0) and done by the loader at `Ｓダメージ上限`, with the same `倍率計算関数`, before the callbacks: `rq.CapCtx` has the skill's limit (`base`), Damage Maximum's percent (`damage_max`) and the limit so far. `fn` returns a limit, 0 for none. The halving over the limit and the quartering over twice it stay the game's.
- `rq.combat.on_element(fn)`: a physical hit's element, in `物理属性計算`, after the game's weapon, skill and arrows (Fire, Ice and Electric Arrows, and skill 145's five). `rq.ElementCtx` has the element, the weapon's, the defender's weakness, `known`, `guarded` (`FA[77]`), `basic` and `forecast`. A changed element is written to `◆攻撃属性` at the game's second reading of `Ｃ弱点把握`, so the weakness bonus, the log's "(Attribute weakness)", the effect and the knowledges follow it.
- `rq.battle.on_study(fn)`: each of Athena 2.0's Studies (336 to 340) that fired after a fight's EXP (`Ｔ戦闘後の取得経験値算出`), read from her five counters (`FA[176]` to `FA[180]`) before and after it. `rq.StudyCtx` has the stat, the ally she studied, the game's gain and the gain so far; `fn` returns a gain. The counters are written and she is recalculated; her stats keep the game's maximums.
- `rq.battle.reveal_weakness(enemies, opts)`: the game's Weakness Search on the enemies given (or all): each standing one's weakness known (`Ｃ弱点把握(e, 1)`), the effect `全体・弱点サーチ` over the enemies, their weakness marks shown and blinking as `T_BattleMonster@showWeakPointAll` does, and `opts.log` in the battle log. From `rq.battle.on_start` it waits until the fight shows (after `戦闘_奇襲`, the ambush notice); from `rq.on_frame` or a timer itself, until the next turn starts (the loader notes the game's call depth where each frame callback begins); from the fight's own flow it plays at once, also in a fight `rq.battle.start` opened from a frame callback.
- `rq.chara.on_skill_reset(fn)`: after the game resets a character's skills (`Ｃスキルドレイン`: Morurun's reset, equipping Skill Again), which sets the free points to the game's own count. `rq.SkillResetCtx` has the character and the points; a mod gives back the points it gave.

## 2.45.1

A fix found by Moru in Loadouts' menus: the comments of the game's choice menu were cut mid-word.
- `rq.ui.choose`, `rq.ui.ask` and `rq.scene.choice`: a row's `comment` is cut into lines between words, at most 28 half-width letters (14 Japanese) each, before the game gets it. The game's menu (`T_Select::showComment`) cuts a comment at each `@` and then every 28 bytes with no regard for words, and only after that does its window start a line at a `\n` too: so words were cut (`skil` / `ls`), and a `\n` did not restart the count, which gave short lines and stray empty ones. A word longer than a line is still cut where it stops fitting. `@` and `$` in a comment are drawn as `＠` and `＄`, as in `rq.ui.confirm`, since the game's window starts a line at them.
- `rq.uikit.options`: a row's comment shows the same lines as the game's menu.
- The MODS list's tips (`rq.gamebutton`'s `"system-menu"`) are `rq.ui.choose` comments, so they are cut between words too.

## 2.45.0

Skill buying, for Skill Removal Payback and Loadouts (`notes/plans/plan-new-mods.md` in the workspace, phase R, step 1). In Lua over `rq.ain` (`src/lua/skills.lua`), with two private calls in C.
- The purchase record: the game keeps a cost field in each skill row (`Ｃ[iic].スキル[row].コスト`, in the save) but only ever writes 0 there, so `rq.chara.on_forget`'s `cost` was always 0. Now the loader adds the points of each purchase there, after the skill window's buy (`キャラスキル_新規追加`) and upgrade (`キャラスキル_更新`) and each step of `rq.chara.learn`. A row with no record and more than its starting level (bought before this loader) gets its older steps priced by `rq.chara.price` at its next upgrade. -1 marks a skill a mod gave: `rq.chara.grant` and `edit`'s `learn` on a row with no record, `rq.chara.learn` with `pay = false`. The game never reads the field. `on_forget`'s and `rq.chara.forget`'s `cost` are this record.
- `rq.chara.on_learn(fn)`: each purchase, once per step (`rq.LearnCtx`: the row, the points, the record after it, `new`, the level `n`, `by` "game" or "learn").
- `rq.chara.base_skills(iic)`: the skills a character starts with, as Morurun's reset gives them back: the game's `Ｃ生成／キャラデータ(iic, 0, "スキル")` and `Ｃスキルドレイン`'s additions by flag, run on the character itself and put back.
- `rq.chara.skill_points_max(iic)`: the game's `Ｃ最大スキルポイント取得`, with the counter it clears (`FA[33]`) put back.
- `rq.chara.learnable(iic)`: the buy list the game would make (`Ｔ購入スキル登録`, with `on_offer`), read and put back: each skill's price, its level on the character, and the game's reason when it is not for sale.
- `rq.chara.price(iic, skill, from, to)`: the game's price from one level to another, each step read from the list with the skill set to that step on the character, then put back. The game's rules hold: +1 at 3, 5 and 7 most uses, prices that change with the skill (Rance's 147), skill 384's 3 uses a step. nil and why ("not sold", "condition" with the game's text, "max", "room").
- `rq.chara.skill_room(iic)`: how many more skills the character can learn, the game's check before a new skill (`キャラスキル_空き確認`) as a number.
- `rq.chara.slots(iic)`: each row has `cost` (the purchase record) and `n` (its level, as `base_skills` gives it).
- `rq.chara.learn(iic, skill, opts)`: the game's own buy and upgrade, step by step at the list's price, its questions answered Yes, then the recalculation (and the refill outside a quest) the window does. `to` (default one step), `pay` (default true). Checks the whole price, the points and a free row first: false with "points" and the missing points, "room", "not sold", "condition", "max", or "refused" when the game refused a step.
- Private (for the loader's own Lua): `priv.keep(paths, fn)` runs `fn` and puts back a whole character, a whole array or a plain value as they were (writing the values back into the same heap slots); `priv.forget_quiet` keeps `on_forget` from running while the character builder removes skills (Athena's 108) inside it.

## 2.44.0

The calls the first batch of the mods' review needed (`notes/plans/plan-mod-review.md` in the workspace, phase Q): the combat rules as data, recommended ranges on settings rows, a "don't ask again" row ticked from the start, and an item picker for one kind of item with drag and drop.
- `rq.combat.rules(skill)`: what a skill can do in a fight (`rq.CombatRules`): `crit` and `stun` (true, false or "sometimes"), `poison` ("own" with `poison_rate`, "coat", "sometimes" or false), `accuracy` ("ignores" or "rolls") and `set_by`. Worked out at each call from the skill's data as it is then (`rq.skill.get`: action kind, multiplier, function), the game's rules by skill number, which it keeps only in its combat code (now the loader's: the crit's 0 for skill 120, the stun's skip of 120, 448 and 152, the stuns in the special skills' own code, the poison rates in `毒計算`), and what mods set. The game's exceptions are "sometimes": a crit chance the game zeroes (a multiplier over 150, skill 120) that skill 549 or party item 91 still raises.
- `rq.combat.set_rules(skill, rules)`: changes a skill's `crit`, `stun` or `poison` rule in the fight and in `rules` together; "sometimes" changes only `rules`, "game" puts the game's rule back. In the fight: `crit = true` holds the skill's multiplier at 150 while `クリティカル計算` runs (and opens the game's check of skill 120 the first time a mod asks for it), so the game's own chance and rules roll; `crit = false` skips the function. `stun = true` or `false` decides `rq.combat.on_stun`'s `blocked` for the skill ("skill"). `poison = N` is the skill's own chance (the weapon's or the coat's when higher; a target the game shields is not poisoned); `false` none. The callbacks run after a rule and see its chance.
- `rq.config.settings`' rows: `recommend` ({min, max}) on a stepper or a slider draws that range lighter on a slider's track, says "Recommended: a to b" after the control (under the row when the line has no room), and asks with the game's Yes / No when the player leaves it, with the value, the range and `warn`; Yes keeps the value, No puts the range's nearest end, and moving further on the same side does not ask again (`Settings.set` and Reset never ask). A slider shows its value beside the track (`format`, `value = false` to hide it) and writes it when the knob is let go.
- `rq.uikit.slider`: `band` (a part of the track drawn lighter) and a third value, `held` (the knob is being dragged).
- `rq.ui.confirm` and `rq.ui.ask`: `remember_checked` shows the "don't ask again" row ticked from the start, with its words and the game's tick (a picture made from the game's two rows; the game's own ticked row reads "UNDO"). The player's answer with it still ticked turns the question off, whichever button or row they picked; a cancel turns nothing off.
- `rq.uikit.item_picker`: `only` (a function that keeps the items it returns true for), `type` (a category kept picked in the filter column, its rank buttons and Locked / Unlocked still working), `first` (rows put before the rest, unsorted, filtered as the rest, such as the item a character wears) and `drag` (a drag group, as `item_list`'s). With `shown` under 6 the SORT sits at the list's own foot. The current instance is one the list shows: an item used up, sold or filtered out is no longer current.
- `rq.uikit.filters`: `type`, a category kept picked; the others are drawn dim and take no click.
- `rq.uikit.item_dropped`: a fifth value, `at`, the row of the list it was dropped on (for a list whose rows are places, such as slots).
- `rq.item.give`, `remove`, `set`, `transform`, `equip` and `edit` relist `rq.uikit`'s item lists and pickers at once, as the reference said; they waited for the lists' 2-second relisting.
- Docs: `rq.uikit.item_picker`'s second example tests the vault's lock with `rq.uikit.item_data(ii).locked` (`rq.item.get`'s `locked` is "cannot be taken off").

## 2.43.0

RQ Browser (`rq-browser.exe`), a window to look through the game's files and copy the Lua line that replaces or plays each one (`notes/plans/plan-file-browser.md` in the workspace, phase P1 of the priority order). No `rq.*` call changes; the version is raised for the program that ships with this loader.
- Where: `xsystem4\rq-browser.exe`, beside the engine. It opens the game folder above it, else asks for one and remembers it (`rq-browser.json` beside it); `--game DIR` names one. It reads the game's archives and never changes the game's files; the one file it writes is its own `rq-browser.json`.
- Six tabs, each with a search, its details and Save:
  - CGs: the 2,315 CGs in `RanceQuestCG.afa` by folder (English labels, the Japanese folder names in the details), as a list with thumbnails or a grid, a view with zoom (the wheel, sharp pixels from 200 %), drag and a checkerboard under see-through pixels; the `rq.image.replace` line; Save as PNG, and the shown ones as PNG into a folder.
  - Flash: the 412 Flash files in `RanceQuestAFF.afa` (Battle, Monster, System), each one's bitmaps with the `rq.image.flash_bitmap` and `flash_bitmaps` lines (the file's key as those calls take it), and its sounds, played when stored as PCM, with the `rq.sound.play_flash` line. The motion is not played.
  - Music: the 72 tracks in `RanceQuestBA.ald` with the game's names (`rq.ids.music`): play, pause, seek, volume, and the loop from `RanceQuestBA.bgi`, shown on the seek bar and played as the game plays it; the `rq.music.replace` and `rq.music.play` lines; Save as OGG (the file as stored).
  - Sounds: the 140 sounds in `RanceQuestWA.ald`, with the `rq.sound.play` line; Save as OGG.
  - 3D textures: the 5,351 textures in `Data/ReignData.red` by folder (Chara, Map, BG, Etc, Texture) and model; Save as PNG.
  - Names: every `rq.ids` list with each name's key and `rq.ids` line, and the game's picture for it: each character's face (and standing picture, in the CGs tab), each item's icon (`data/ids/pictures.tsv`, 435 lines). A CG a name uses is labelled with it in the CGs tab ("Rance: face").
- Playing music, a sound or a Flash sound stops when another tab opens.
- Sharp on a scaled display: the program is per-monitor DPI aware, so Windows does not stretch it, and it draws its text and layout at the display's scale (1.5 on a 150 % screen), again when the window moves to a screen with another scale. `--scale F` (1 to 4) sets the size by hand.
- The Lua lines the program writes are checked at build time against `dist/lua/rq.lua` (`tools/rq-browser/check_lua_lines.py`): a call that is not there stops the build.
- `--check [--out FILE]` opens every archive, decodes samples of each kind, reads every track's loop and every sound, and checks the names' pictures and the font, then prints a JSON report (exit 0 when all is well); `--shot TAB FILE [--select N] [--size WxH] [--scale F]` saves one tab as a PNG (at scale 1 unless `--scale` says otherwise). `--help` lists them.
- Built with Dear ImGui 1.92.9 through cimgui 1.92.9b (MIT, `third_party/cimgui`, see its README), linked statically; the release zip has `rq-browser.exe` in `xsystem4\` and the two licenses in `xsystem4\licenses`.
- `tools/ids/extract.lua` also writes the names' pictures (`ids-pictures.tsv`), and leaves out quests 303 and up, the mods' own (`rq.quests.define`), such as the Test Lab's.

## 2.42.0

Maps for a mod's own quests (`notes/plans/plan-new-dungeons.md` in the workspace, phase O3 of the priority order). In Lua over `rq.ain` (`src/lua/quests.lua`). The script's hook (before `クエスト処理／基本`) answers moments 8 and 9 of a mod's quest with a map, and a hook before the dispatcher `クエスト処理` answers moment 7: `ＱＭ登録` asks for it from inside moment 8, while the first hook runs, and a hook's callbacks do not run for a nested call of the same function; the hook that ends a quest on the map of a mod that is gone (before `Ｔマップ割り込み`) is placed at the loader's start.
- `rq.quests.define`'s `map` (`rq.QuestMap`): areas 1 to 16 on the game's 4 by 4 grid (`rq.QuestArea`). The quest is the game's kind 0, with the list's map mark; `fights` is refused with it.
  - The map's settings, which an area may give again: `tileset` (a map kind: the rooms' look, the fight background and the music), `name` (the map panel's), `gold`, `loot` (the chests' content: `"C"`, `"B"`, `"A"`, with `+` an item bonus, `"A++"` a superior item, or the game's number; the appraisal fee follows), `music` (by default the track the game's quests on that tileset use most), `background` and `groups` (the game's numbers or a mod's ids, needed). The map's only: `traps` (the four kinds' weights), `bonuses` (the goals of the achievements, placed enemies and level-ups bonuses), `start` (the lowest area by default) and `chatter`.
  - Each area: `exits` (letters N, S, E, W), `room` (a stock room by number: 1, 2, 101, 102, 201 to 204, 301, 302, and 401 to 409 on the Malgrid tilesets) or `fixed` (one of the 87 fixed maps the game's quests load), or neither for the game's draw by the exits; `enemies`, `chests`, `traps` and `feats` placed by the game on drawn spots (a counted chest is the game's draw: a red chest half the time, nothing otherwise); `objects` (`rq.QuestObject`) placed on the area's first entry in a run: the game's kinds of `rq.dungeon.place`, a chest's `item` (a number or a mod's item id), and `"custom"` objects with `id`, `look`, `keep` and `run` (registered as `rq.dungeon.on_object`), at a free spot (`"any"`), the room's wide spot (`"wide"`) or a cell; `setup(ctx)` at each entry, after the area is set up (`rq.QuestAreaCtx`: `id`, `quest`, `area`, `row`, `col`, `first`).
  - Moment 7 (`ＱＭ登録` of each area) writes the settings as the game's quest scripts write theirs (`ＭＡＰ基礎型登録`, `◆ＭＡＰ名前`, `クエスト基本登録`, `トラップ確率登録`, `エンカウント中身登録`, `ボーナス登録`), then `ＭＡＰ読み込み` (the room drawn from the tileset's stock rooms by the exits, or the one asked: the tileset's base number plus the room), then the objects: the game's kinds through `ＭＤランダム` (with priority, as the game's quests place theirs) or `ＭＤ固定`, a custom one on a free spot (`発生ＭＰ`, `広域ＭＰ`) through `ＭＤ固定`.
  - Moment 8: `run`, when given, is the prologue: nil goes on to the map, a result ends the quest without it. Then the first area (`ＱＭ登録(start)`).
  - Moment 9: the game's own answer (`割り込み２`): its party lines after new areas, and its rules after a fight and a warp. `chatter = false` holds the party lines back (the count of new areas they wait on is kept at 0).
  - The rooms drawn are kept in the quest's entry (`Ｑ[n].Ｍ固有番号記憶`), so each try has the same rooms, as the game's quests have. The map's shape (each area's tileset, room or fixed map, and exits) is kept in the loader's part of `rq.savedata` by the quest's id; a new shape draws the rooms anew (`Ｑ初期化／エリア情報`).
  - Checked at `define`: each exit leads to an area of the map that has the way back, none off the grid; every area is reached from `start`; each area has a tileset and groups; a drawn or stock room needs a tileset with stock rooms (13 of the 22), a fixed map the exits asked for; the counted objects and the objects at `"any"` fit the room's spots (17 for a drawn room, the room's own for one asked), the objects at `"wide"` its wide spots.
  - An area the map does not have (a save from another version of the mod) gets a drawn room with the way back and a line in the log. A save made on the map of a mod that is gone (or whose quest has no map any more) ends the quest as with the escape device, the items kept, the first time the map hands over to the quest's script.
- `rq.quests.get` gives `map` for a mod's quest with a map (`rq.QuestMapShape`: `start`, `tileset`, each area's `exits`, `room`, `fixed` and `tileset`).
- `rq.quests.set_run` writes `progress`, the bar on the map panel (0 to 100, up or down).
- `rq.dungeon.on_object`'s function may return `"clear"`, `"fail"`, `"abandon"` or `"escape"`, as `rq.QuestDef.run` does.
- Docs: `rq.DungeonObject.number` of a chest is 10000 + the item instance rolled for it when `rq.loot.install` is in place (Loot Preview). A chest's item may come out unidentified (the game identifies a set item 1 time in 3), and then the appraisal's Finish discards it unless the player pays.

## 2.41.0

Quests of a mod's own with no map (`notes/plans/plan-new-quests.md` in the workspace, phase O2 of the priority order). In Lua over `rq.ain` (`src/lua/quests.lua`). The hooks that number, hide and reset the mods' quests (after `Ｑ起動時登録` and `ワールド切り替え処理`) are placed at the loader's start; the script's hook by the first `define`.
- `rq.quests.define(def)`: a quest of a mod's own (`rq.QuestDef`): the name, the text (up to 5 lines), the place, `fights` (the list's battle mark, the game's kind 2; without it kind 3, no mark), `main` (the main tab, else a side quest), the difficulty with the world's addition, the fame of the first clear (written as `Ｑ初期セット` writes it, only while the quest has no fame and no clear), the conditions and a condition of the mod's own as `rq.quests.edit` takes them, how it opens (`open`, `after` a quest's clear) and `run(q)`, its script.
  - The number: the first free one from 303 to 500 the first time a save has the quest (the game resets only 1 to 301), marked with `rq:` and the id in `Ｑ[n].チェック`, which only the developers' scenario test reads. The mark is in the save, so the number stays with it; no `rq.savedata`. Past 198 quests in one save, a quest is left out with a log line.
  - The data is written after each `Ｑ起動時登録` (a new game, a load, a world transfer), the kit 0.
  - `run(q)` runs at the quest's moment 8, in place of kit 0's script (a hook before `クエスト処理／基本`, so `rq.quests.on_event`'s `start` on the dispatcher runs first). `q` has `id`, `no`, `tries`, `clears` and `first`. It may wait (scenes, fights, choices, dialogs) and returns `"clear"` (or nil), `"fail"`, `"abandon"` or `"escape"`, the game's results 1 to 4: the game's end, result screen, fame and clear count follow. An error or another value is logged and gives the quest up (3); the title passes through.
  - `after`: opened by that quest's clear through `Ｑ状態(no, 1)`, so the victory screen lists it with the game's new quests; at once when a save first has the quest and that one is cleared.
  - A world transfer resets the mods' quests after the game's own reset: the entry as new (`Ｑ初期化`), the data, the state from `open` and `after`.
  - A save holding a quest no loaded mod defines: hidden at each load (state 0, the state kept in the mark as `rq<state>:<id>`), its state back when the mod is loaded again; a world transfer made without the mod frees its number.
- `rq.quests.no(id)`: the number of a mod's quest in the loaded save.
- `rq.quests.get`, `edit`, `state`, `set_state`, `unlock`, `start` and `can_take` take a mod's quest's id. `edit` keeps a patch on a mod's quest by its id, over the definition's fields, in every save.
- `rq.quests.get` gives `text_id` (a mod's quest's id; `id` stays the number) and `main`. The description of `kind`'s `"menu"` was wrong: the game's kind 3 is any quest with no map and no fights (a story, Alice's Mansion), not only a menu entry.
- The ctx of `rq.quests.on_clear`, `on_end`, `on_take`, `on_event` and `on_event_after` has `id` for a mod's quest.
- A mod's own condition (`edit`'s `condition`) joined to an empty special text no longer starts with " / ".
- `rq.ui.get`: the appraisal after a quest's success is the screen `appraisal`, with `finish` and `close` in section `appraisal` (it was not listed, so an agent could not leave it).
- `rq.quests.state`, `set_state` and `unlock` are Lua now: they raise "the game is not running yet" at a mod's top level themselves, and the loader's guard no longer logs them (nor `rq.battle.start`, Lua since 2.36.0).

## 2.40.0

New monsters and enemy groups (`notes/plans/plan-new-monsters.md` in the workspace, phase O1 of the priority order). In Lua over `rq.ain` (`src/lua/monster.lua`, `src/lua/basics.lua`), and the model table in C (`src/hll/MonsterInfo.c`). The hooks that build a monster or a group whose mod is gone are placed at the loader's start; the others by the first call that needs them.
- `rq.monster.define(def)`: a monster of a mod's own on a game monster's data (`base`), with any field of `rq.monster.edit`. Its number is 1000 + an FNV-1a hash of its id modulo 9000, as an item's. The game builds it through its base's block (look, motions, the world's rules), so it fights in `rq.battle.start`, in a mod's group and as a familiar. An edit of the base does not reach it; an edit of its own number or id does. Its kills and whether its weak point is known are kept in the loader's part of `rq.savedata`, by its id, through the game's own accessors (`■Ｍ／撃破数`, `■Ｍ／弱点把握`).
- `capture` on `define`: the game's capture skills (166, 451, 531) catch the monster under the game's rules and give the mod's item, with the scene's CG and text; without `capture` the monster escapes, as one the game has no item for.
- `drops` on `define` and `edit`: up to 8 items with a chance, rolled after a won fight with no item yet, each enemy defeated in rank order, before every mod's `rq.battle.on_end`; the first that rolls is the fight's one item, in the place of the game's later drops.
- `rq.monster.get` and `edit` take a mod's monster by number or text id; `get` gives `id`, `base`, `kills` and `weak_known`; `on_create`'s ctx has `id`.
- `rq.monster.group(def)`: an enemy group of a mod's own: a name for the game's log, the EXP, the rank and 1 to 6 line-ups of up to five monsters (numbers or a mod's ids), drawn as the game draws its own (1 to 5, not the last one twice; the 6th for an enemy standing on the map one time in 3). `rq.encounters.set_groups(list)` writes the area's list with the game's and the mods' groups; `rq.battle.start`'s `group` fights one, with the group's EXP, and `enemies` takes a mod's monster by text id.
- `rq.monster.models()` and `model(def)`: the game's model table (`MonsterInfo`), and a game model at another scale and offset, added after the table and put back each time the game reads it.
- A save holding a number of a mod that is not loaded any more: an unknown monster of 1000 or more is built as the game's Data-less Ghost (`Ｃカスタム登録`), an unknown group in an area's list becomes the area's first game group (135 when it has none), each with one line in the log.

## 2.39.0

Quests and map objects (`notes/plans/plan-quests-map-objects.md` in the workspace, phase N of the priority order). In Lua over `rq.ain` (`src/lua/quests.lua`); the hooks of `edit` and `on_trap` are placed by their first call, those of a mod's objects at the loader's start.
- `rq.quests.get(no)`: a quest's data as the quest list shows it (`rq.QuestData`): the name, the text as lines, the place, the special condition's text, the state, the kind ("quest", "fights" for a quest of fights only, "menu"), the difficulty with the world's addition, the fame the next clear gives, the tries and clears, up to three `conditions` as tables (`rq.QuestCondition`: `party_max`, `member`, `own`, `member_level`, `item`, `special`, each with the list's `text` and `met`), `can_take` and the mods whose patch is on it.
- `rq.quests.edit(no, patch)`: the name, text, place, difficulty and conditions, put back on top each time the game writes its quest data (`Ｑ起動時登録`: a game's start, each load, a world transfer) and its special conditions (`Ｑ特殊な条件の処理`, each time the quest menu opens), never in the save. One patch per mod and quest, `nil` removes it and brings the game's data back, patches in load order. A mod's own condition, `condition = { text, ok }`: while `ok(no)` is not met, the quest has the game's special condition with that text, so the quest list greys Take and shows it.
- `rq.quests.run()` and `set_run(fields)`: the quest being played (`rq.QuestRun`): the progress, fights, placed enemies beaten, the run's EXP, the fame a clear gives, the appraisal fee, the gold base, the EXP bonus, the three bonuses (`feats`, `level_ups`, `enemies`, each `count` and `max`), the party changes ("normal", "none", "free"), AREA DISPLAY and the warps closed. `set_run` writes the fame, the EXP bonus (0 to 50), the bonuses (a `max` turns one on, `false` off), the party changes, AREA DISPLAY and the warps; the quest panel is drawn again and a bonus reaching its maximum shows the game's flash.
- `rq.dungeon.objects()` and `remove(x, z)`: the objects on the current map (`rq.MapObject`, the kinds by name) and one taken away (not a warp).
- `rq.dungeon.place` takes `"trap"`, `"enemy"` (a placed enemy) and `"escape"`, and `"custom"`: a mod's own object, a silent map event whose number comes from `opts.id`, with one of the game's props as its `look` (`rq.dungeon.looks()`) and `keep` to put it back after each step. `rq.dungeon.on_object(id, fn)` runs when the party steps on one (`rq.ObjectCtx`: `id`, the cell, the quest, the area, a `keep` writable for that step, starting as `place`'s, and `remove()`), in place of the quest's own handling; its result ends the quest or not, as a quest moment's does. The look is placed again each time the game writes the cell (entering an area it visited). `rq.quests.on_event` and `on_event_after` do not see these events.
- `rq.dungeon.traps()`, `set_traps(weights)` and `on_trap(fn)`: the trap kinds' weights in the area (`shroom`, `shock`, `alarm`, `pit`, 0 to 10), and a trap stepped on, after the game drew its kind and before the scene (`rq.TrapCtx`: the cell, a writable `kind` and `chance`, `who`, and `cancel` to remove it with no scene). A changed chance is rolled with the game's roll.
- `rq.quests.can_take` and `refresh` ask the mods' own conditions first.

## 2.38.0

What enemies and the familiar choose (`notes/plans/plan-enemy-choices.md` in the workspace, phase M of the priority order). In Lua over `rq.ain` (`src/lua/choices.lua`); the hooks are placed by the first `on_choose`.
- `rq.battle.on_choose(fn)`: on each turn of an enemy or the familiar, after the game drew the skill (`戦闘敵_行動選択`, `戦闘従魔_行動選択`) and rolled its target (`Ｔ戦闘_対象選択`, called by the loader with the same arguments), before it acts. The ctx (`rq.ChooseCtx`) has `iic`, `unit`, `side` ("enemy", "familiar"), `rank`, `turn`, a writable `skill` and `target`, `rolled` and `standby` (the game's Standby rule for a front-row skill from the back row), `charged` (a charged skill released: the target only), `skills` (`rq.ChooseSkill`: the list with its chances as they are now) and `ctx:targets(skill)`.
  - A new skill must act (not an ability), not be Escape (211) or "Relax, relax" (217), and goes through the Standby rule; one the actor does not have is put at the end of its list for the fight (chance 0, the first skill's motion, the skill's own log text). A new skill with the target left gets the game's roll for it, unless a mod set a target that still fits.
  - A new target must be standing, on the side the skill's target kind names, not a hidden ally, and in the front row for melee while one stands there (`ctx:targets`); an attack on the actor's own side is refused. A target a mod set (written by a callback, also the unit the game rolled) takes every hit of a multi-hit skill while it stands.
  - A write that fails a check keeps the value before it and logs a line naming the mod.
- `rq.battle.taunt()` and `set_taunt(iic)`: the game's own taunt (`◆戦闘タゲ取り`, set by its "got the enemy's attention" skill and cleared at a fight's start), which the enemies' target rolls take first.
- The reference of `rq.battle.on_use` and `rq.monster.edit` points to `on_choose`; `rq.MonsterSkill.chance` says how the game draws.

## 2.37.0

The combat formulas and the last hooks the mods placed on the game's code (`notes/plans/plan-combat-hooks.md` in the workspace, phase L of the priority order). In Lua over `rq.ain` (`src/lua/combat.lua`); the hooks are placed by the first call that needs them.
- `rq.combat.on_stun(fn)`: each hit's stun chance in `衝撃計算`, for the battle forecast too (`ctx.forecast`). `fn` returns the chance (0 to 100, true is 100, false is 0) or nil; each callback sees the chance the one before left. It also runs where the game never stuns: the skills 120, Fortune (448) and 152 (`blocked = "skill"`), and a target stunned the turn before (`"repeat"`), with `ctx.base`, the formula's chance, so a mod can let them stun. The forecast and the log's " (Stun rate = N)" show the last chance.
- `rq.combat.on_poison(fn)`: the poison chance of each hit on a target with no status (`毒計算`). Most hits have 0 in the game; when the last chance is above 0 and the game made no roll, the loader rolls it with the game's roll. The log's first line shows " (Poison = N)" as for the game's own poison.
- `rq.combat.on_counter(fn)`: after each hit that leaves the one hit standing (`ダメージ後計算`), whether or not it learned Counter (259), a yellow skill of any class. The ctx has `rate`, `base` (the Counter skill's chance), `damage`, `guarded`, `counter` and `blocked` ("familiar", "area", "stunned", "guard"). A counter is the game's Counter Attack (116) with " (counter)" in the log; after 10 counters in a row the loader grants no more. `rq.counter.on_guard_counter` still decides first.
- `rq.combat.on_heal(fn)`: the HP a support skill's heal or revive gives (`Ｔ補助行動`) and HP absorb from a hit, with `kind` ("skill", "revive", "absorb") and a writable `amount`; the HP, the number shown and the log's " recovered N HP." follow it, a revive gives at least 1.
- `rq.combat.on_escape(fn)`: the chance Escape (211) flees and "Relax, relax" (217) ends the fight, with `blocked` ("enemy", "rank", "quest"). A changed chance is rolled with the game's roll. Not in a boss fight.
- `rq.battle.on_order(fn)` and `on_order_after(fn)`: the turn list (`Ｔ順番生成`, at a fight's start and after a switch, a shuffle or a revive, `rebuild`). `on_order` lists the units (`iic`, `side`, `rank`, `spd`, `out`, and for the familiar `owner`, `item`, `own_spd`) and `ctx:speed(iic, n)` sets a speed for that build only; `on_order_after` reads `ctx.order` and replaces it with `ctx:set_order(list)` (1 to 50 entries).
- `rq.battle.familiar()`: the fight's familiar (`iic`, `no`, `owner`, `item`, `joined`, `spd`, `own_spd`, `growth`).
- `rq.battle.escape()` and `set_escape(n)`: the fight's escape chance, through the game's setter (a boss fight keeps 0).
- `rq.battle.on_start`'s ctx has `ambush` ("none", "surprise", "first_strike", "ambushed") and `first_striker`; `rq.battle.set_ambush(kind, iic)` changes it from `on_start`, before the turn list is built.
- `rq.battle.on_log(fn)`: every line before it goes into the battle log (`戦闘ログ_追加`), with `text`, `color` and `last` (the end message); `fn` drops it (false), replaces it (a string) or keeps it (nil). `rq.battle.log(text)` adds a line, through `on_log`.
- The reference of `rq.combat.on_crit`, `rq.counter.on_guard_counter` and the `log` of `on_turn` and `on_hit` points to the new calls.
- copandon-dot-qol 1.0.4 lets Fortune stun with `rq.combat.on_stun`, nozomi-okita-qol 1.0.4 drops the disease's line with `rq.battle.on_log`, and onoha-qol 1.0.3 sets the two speeds with `rq.battle.on_order`; none of the three hooks or patches the game's code any more (copandon-dot-qol still reads the next Fortune's result, `FA[102]`), and all need loader 2.37.0.

## 2.36.0

Monsters, modes and fights from a mod (`notes/plans/plan-monsters-modes.md` in the workspace, phase K of the priority order).
- `rq.monster.get(no)`: a monster's data from the game's list (`rq.Monster`: the name, model, boss flag, race, type, level, HP, the stats, the weak element and the five resistances with `rq.chara.get`'s names, up to five `skills` with `id`, `text`, `motion` and `chance`, and the `lines` the fight shows), with every mod's edits, before the world's rules. It builds the monster in slot 9, which the game never uses, skips the game's build function so no random number is drawn, and empties the slot. nil for a number the list does not have.
- `rq.monster.edit(no, patch)`: changes a monster each time the game builds it (fights, the familiar, the game's name lookups, `get`). The patch replaces the list's numbers before the world's tiers, race 60 and a boss fight's `strong` scale them; `skills` goes by position (`false` empties one), `lines` by kind. One patch per mod and monster, `nil` removes it, patches in load order.
- `rq.monster.on_create(fn)`: each enemy a fight builds (ranks 1 to 5) and the party's familiar (`familiar` true), after the game's build and before the fight opens. The ctx has the slot, number, rank, world, the fight's kind, group and strength rate and `base` (the data as `get` gives it); `name`, `level`, `hp` and the stats are writable and written to the slot once after the last callback. Returns a remover.
- `rq.game.mode()` and `set_mode(mode)`: "classic" or "tada" (`◆２倍モード`), nil before a save is loaded. The game has no easy mode to report: its flags are a leftover of the first Rance Quest that Magnum never sets.
- `rq.battle.start` is in Lua over `rq.ain` and takes more options: `boss` (the game's boss fight: rank 2, no escape, 999 actions, the boss music and the `boss` moment of `rq.music.on_play`), `strong` and `double_hp` (with `boss`), `names` per rank, `background` (a number or a name, put back after), `music` (a game track or a file in the mod's folder, over the game's choice and `rq.music.on_play`), `escape` (0 to 100, written before every `rq.battle.on_start` callback) and `gold` (`rq.battle.on_reward`'s `ctx.gold` before the mods' callbacks). It returns a second value, `rq.FightResult`: `code` and `how` (won, lost, draw, time, fled), the `exp` and `gold` the fight paid, `kills` and the `fallen` allies. The first value is as before. An unknown option now raises an error; before, it was ignored.
- `rq.battle.backgrounds()`: the game's fight backgrounds, `{ no, name }`.
- onoha-qol 1.0.2 reads the familiar's speed with `rq.monster.on_create`, and custom-tada-mode 1.1.2 reads the mode with `rq.game.mode()`; both need loader 2.36.0.

## 2.35.0

Comfort for creators (`notes/plans/plan-creator-comfort.md` in the workspace, phase J of the priority order): a settings page from a list, no install calls, and the party's places and heals.
- `rq.config.settings{ rows, ... }`: a page in Config's Mods tab built from a list of rows, with no `draw`. The kinds are `checkbox`, `stepper`, `slider`, `choice` and `input`, which keep a value under `key`, and `label` and `space`. Each row may have a `label` (the labels line up in one column), `default`, `note` (dim lines under it), `tip`, `disabled` (a value or a function asked on every update) and its widget's options. A Reset button puts the rows back to their defaults (`reset = false` leaves it out), and `draw` adds more after the rows. The values are kept for the mod in `rq.store.global` (default), `rq.store` (`keep = "profile"`) or `rq.savedata` (`keep = "save"`, the rows greyed until a save is loaded), under each row's key, so a mod that drew its own page keeps its players' settings. It returns an object: `get(key)` (a stored value the row cannot take reads as the default), `set(key, value)`, `on_change(fn(key, value, old))` (returns a remover) and `reset()`. A wrong row, key or default raises an error at the call.
- No install calls. `rq.chest`, `rq.orb`, `rq.skill`, `rq.chara`'s skill and buy-list calls, `rq.combat`, `rq.counter`, `rq.shop` and `rq.battle`'s select and flame calls place their hooks the first time one of them is called (the log names the mod and the call), and raise that call's error when a hook cannot be placed. The calls that do it: `chest.on_attempt`, `on_result`; every `orb` call; `skill.on_describe`, `get`, `define`, `patch`, `sort_as`; `chara.on_recalc`, `on_offer`, `grant`, `rank`, `slots`, `set_slot`, `set_flavor`, `weapon_detail`, `apply_mod`, `offers`, `set_offer`, `max_uses`, `set_uses`, `set_bar`, `clear_slot`; `combat.on_physical`, `on_accuracy`, `on_crit`; `counter.on_guard_counter`; `shop.on_stock`, `in_stock`, `stock`; `battle.on_select_key`, `in_ally_select`, `actor`, `skill_usable`, `set_flame`, `set_mark`. The `install` calls stay and do no harm. Before, a call made without its install often failed in silence: `rq.orb`'s reads gave 0, `rq.skill.define` and `patch` were never applied, `rq.chara`'s skill calls read 0 and wrote nothing, `shop.in_stock` said false and `battle.skill_usable` said true. `rq.loot.install`, `rq.skilllist.install` and `rq.battle.install_states` stay a mod's choice, since they change what the player sees or the game's rules.
- `rq.party.roster(state?)` (every recruited character with `iic`, `state`, `hp`, `hp_max`, `status`), `rq.party.state(iic)`, `rq.party.set_state(iic, state)` (the first army, used in this quest, the second army) and `rq.party.heal{ skills, half, all }`, and `rq.chara.heal(iic, { skills, half })`: the game's own heals, which leave a downed character as it is.
- `rq.ids.party_state`: NONE, PARTY, RESERVE, USED, SECOND, the places of `登録状態`. The reference of `rq.chara.get`'s `state` and `status`, and of `rq.orb`'s, lists every value (the docs said 3 was "spent" and had no 2 for the status), and each `rq.orb` call names the call that does the same anywhere.
- `rq.store.get` and `rq.store.global.get` give a whole number back as an integer (`math.type` "integer"), as `rq.savedata` does; they gave a float (3.0), so a check for an integer failed on every value read back. Kaoru Quincy QoL reset its levels to the defaults after each start for this.
- The engine wraps the calls that need the game with their closures kept (`lua_call`), so a call that installs on first use keeps its upvalues.
- Morurun Items 1.3.1, Kaoru Quincy QoL 1.3.1, Custom TADA Mode 1.1.1 and Game Speed 1.2.2 draw their Config pages with `rq.config.settings`, with the same keys and widget ids and a Reset button; Kaoru Quincy QoL no longer calls the installs.

## 2.34.0

Fight rewards and save data (`notes/plans/plan-rewards-savedata.md` in the workspace, phase I of the priority order). The rewards are Lua over `rq.ain` (`src/lua/basics.lua`); the save data is kept in C beside `rq.store` and written with the game's own save files.
- `rq.battle.on_reward(fn)`: once per fight that pays (results 1 and 4), after the game has summed the gold and EXP and before the result screen shows them. `ctx.gold`, `ctx.exp` (the fight's EXP after the fight's bonuses; writing it scales every ally's EXP at once), each ally's `exp` in `ctx.allies` (with `down` and `capped`, who get none) and `ctx.reserve` (each reserve character's share; until written it follows the game's rule, the smallest ally EXP over 20) can be changed, and the result screen shows them, the party gets them and the gold is paid. Also `result`, `group`, `rank`, `kills`, `bags`, `base`, `enemies`. The quest's EXP total, its level-up bonus and the cheat check's gold count follow; the reserve's share is held during the game's sum and given after the callbacks with the game's free level for a full bar, still reported by `rq.chara.on_level_up` with `battle` and `free`.
- `rq.battle.bags()` and `rq.battle.set_bag(iic, carries)`: the enemies' gold bags (the game gives each a bag at 50%; the bags picked set the gold). `set_bag` in `rq.battle.on_start` is kept and written over the game's roll, which comes after it; during the fight it changes a bag before the enemy falls.
- `rq.savedata`: `get`, `set`, `delete`, `keys`, as `rq.store`, for data that follows the game's save. Kept in memory, written beside the save when the game writes it (`RanceQuestMagnum_030.rqmod.json`, `_930` for the suspend save), read back when the game loads it, emptied at the title, deleted with the save and copied into the game's daily backup. Values are numbers (a whole number comes back an integer), strings, booleans and tables of them. The data of a mod that is not loaded is kept.
- `rq.saves.on_save(fn)` (just before the game writes a save) and `rq.saves.on_load(fn)` (after the game loaded one, with `rq.savedata` in), each with `ctx.suspend`.
- The reference of `rq.store` says it follows the save profile and is written at once, so it can be ahead of the save; `rq.battle.get_drop` and `set_drop` work in `on_reward` too; `rq.on_reset` points to `on_load`.
- `rq.ain.patch_float`, `patch_int`, `patch_int_after` and `set_code_int` reach the game's code of a function hooked with `rq.ain.hook`, before or after the patch: a hook moves the function to a stub that jumps to its code, and the patches read the stub. The loader's new hook on `Ｔ戦闘前初期化` at boot (the gold bags) had hidden Custom TADA Mode's familiar growth from it.
- Binoculars 1.2.1 keeps the pairs that went into a quest and the number bought in `rq.savedata`, taking its old `rq.store` values once.

## 2.33.0

The basics a new creator tries first (`notes/plans/plan-creator-basics.md` in the workspace, phase H of the priority order). Built in Lua over `rq.ain` (`src/lua/basics.lua`, `timers.lua`), so a mod no longer calls the game's functions for these.
- `rq.game`: the money (`gold`, `set_gold`, `add_gold`, kept from 0 to 999,999,999) and charisma (`charisma` gives the rank, the points and the points the rank needs; `add_charisma` goes up one rank at most, as the result screen does; `set_charisma`). Each change redraws the system bar.
- `rq.encounters`: random fights on a quest's map. `info` (the area's groups, the steps that fill the bar, the steps walked, whether fights can happen and which mods hold them off), `hold(true|false)` (one hold per mod; while any holds, no random fight starts, the bar is hidden and the steps do not fill it; an enemy standing on the map still fights), `set_steps` (1 to 999, until the game picks them again), `on_steps` (change the steps each time the game picks them, after a fight and an area change) and `on_encounter` (see a fight from the map, random or placed, and cancel it by returning false: the game's own "no fight" path).
- `rq.chara.add_exp(iic, n)`: EXP as a fight gives it, with the game's level-up for each full bar (stats, skill points, the EXP left carried over); nothing at the level cap or for Athena 2.0, and no level at 0 HP (the game's level-up wants HP), the bar kept full for later. `rq.chara.level_up(iic, n)`: free levels, as the story and training give them. `rq.chara.on_level_up(fn)`: after every level, the game's or a mod's, with `from`, `level`, `battle` (in a fight's result) and `free` (the game's other level-up, which sets the EXP back to 0: the story, training, the reserve's share of a fight).
- `rq.chara.get`'s new field `uncapped`: the game sets no level cap for the character (Rance, Reset Kalar and Dark Rance). The reference of `level_max` says what the cap is and that it lasts.
- `rq.after(ms, fn)` and `rq.every(ms, fn)`: timers on real time, each returning a remover; `every` stops when `fn` returns false. `rq.spawn(fn, ...)` runs a job that can wait with `rq.wait(ms)` and `rq.wait_until(cond, limit)`, and returns a handle (`done`, `ok`, `value`, `values`, `error`, `cancel`). One `rq.on_frame` of the loader's drives them.

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
