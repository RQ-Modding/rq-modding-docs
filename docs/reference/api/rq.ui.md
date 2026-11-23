# rq.ui

`since 0.20.0`

Reads what is on the screen and saves screenshots.

`rq.ui.get` returns the same data as `rqmod-ctl ui`. Raises an error at the top level of a mod.

## Functions

| Name | Summary |
| --- | --- |
| [`rq.ui.get`](#rquiget) | Returns what is on the screen. |
| [`rq.ui.aim`](#rquiaim) | Returns the point a click on a control should land on. |
| [`rq.ui.shot`](#rquishot) | Saves what the game draws as a PNG at the next drawn frame. |
| [`rq.ui.window`](#rquiwindow) | Returns the window's size, the game's picture in it, and how the 3D is drawn. |
| [`rq.ui.set_window_size`](#rquiset_window_size) | Sets the window's inside size, in points, out of full screen. |
| [`rq.ui.shot_result`](#rquishot_result) | Returns how the last `rq.ui.shot` ended, once. |
| [`rq.ui.choose`](#rquichoose) | Opens the game's own choice menu outside a scene, on the hub or any of the game's screens, and calls `fn` with the row the player picks. |
| [`rq.ui.choosing`](#rquichoosing) | Says whether the game's choice menu shows: one of the game's own, `rq.scene.choice` or `rq.ui.choose`. |
| [`rq.ui.confirm`](#rquiconfirm) | Asks the player Yes or No in the game's own dialog, and waits for the answer. |
| [`rq.ui.notice`](#rquinotice) | Tells the player something in the game's own dialog, with one OK button, and waits until it is pressed. |
| [`rq.ui.ask`](#rquiask) | Asks the player a question with any choices in the game's own dialog, and waits for the answer. |
| [`rq.ui.quest_storage`](#rquiquest_storage) | Returns the game's Quest Storage window while it shows, with its item tiles. |
| [`rq.ui.quest_storage_refresh`](#rquiquest_storage_refresh) | Builds the game's Quest Storage window again from the quest storage's items. |

### rq.ui.get

```lua
rq.ui.get() -> table|nil
```

`since 0.20.0` `changed 0.21.0` `changed 2.11.0` `changed 2.12.0` `changed 2.19.0` `changed 2.20.0` `changed 2.20.1` `changed 2.22.1` `changed 2.28.0` `changed 2.31.0` `changed 2.41.0` `changed 2.47.0` `changed 2.56.0` `changed 2.59.1`

Returns what is on the screen.

The table holds `screen` (the screen's name), `hover`, `controls` (each with `id`, `x`, `y`, `w`,
`h`, `enabled` and more) and the data of the current screen, such as `battle` or `quests`. A
screen with no name, such as a black one during a change of scene, says `other`; `boot` is used
only before the first named screen, and `title` only for the real title screen.

The footer's controls (`system`, `vault`, `trivia` in section `system-bar`; the party cards in
section `party`; the money line) are listed on every screen whose own loop takes them: the town,
its tabs, Rance Castle (`castle`), the status page, the vault and a quest's map; in a fight only
`system`. Trivia, CG mode, Music mode and the castle's Gal monsters' and Poster rooms are `other`,
with the footer only: the screen under them is not listed. On `castle` each room is `room-<area>`, with the room's
name as the label and its floor (`B2F`, with ` new` for the NEW mark) as the value.

A game control a player cannot click has `covered = true`: every point of it is under a kit widget
of the last update (section `kit`), or a mod's page captures the mouse (`rq.hud.capture_mouse`).
`rqmod-ctl press` refuses it. A page closed on this update still covers until the next one.

A kit control (section `kit`) under the kit's keys cursor has `focused = true` (`rq.uikit.focused`).

On the screen `select` (the game's choice menu and dialogs), `select.message` holds the dialog's
text rows, one a line. A dialog over Config is `select` too, with Config under it.

On `quests`, while a quest is chosen (`questState.selected` above 0), the rows (`quest-N`) are
not `enabled`: the game reads none of them, with or without a dialog, until Cancel (a right click)
lets the quest go. It stays chosen after its "Take Quest" question is answered No.

On `party-edit`, while the 2nd Army box is open, its cards are `store-N` (N from 0 after the box's
scroll, as `unit-N` on the grid; the character's name as the label, the job and level as the value),
the card under the mouse has its `store-status-N`, and `store-close` closes the box, all in section
`party-store`. `store-drop` (the box) and `grid-drop` (the grid) are where a dragged character is
dropped: `unit-N` dragged onto `store-drop` goes to the 2nd Army, `store-N` dragged onto `grid-drop`
comes back. `storeUnits` lists the whole 2nd Army as `units` lists the roster (`visible` for the
cards shown), and `storeState` has `topIndex` (the box's scroll), `listCount` and `shown` (cards).

After a quest's success, the appraisal of the quest storage's items is the screen `appraisal`:
`finish` (the Finish button, bottom right) and `close`, in section `appraisal`. Its questions (an
item not identified is lost) are `select`. The items' own buttons are not listed.

The Quest Storage window over a quest's map is the screen `quest-storage`: `close`, or `yes` and
`no` for Give Up, and its tiles `item-1` to `item-15` in the window's order, with the item
instance as the value (see `rq.ui.quest_storage`).

`busy` says what the game runs under the screen, when it runs one of these two: `"event"` while one
of a quest's own events runs (its messages, its scenes, its fight, and the map read between them,
`dungeon` with ABANDON, as before a goal's first line), and `"fight-end"` while the game waits for a
click after a fight before it goes on (the map shows under it, and a placed enemy is counted and
removed only after it). The inner one when both run. It is absent otherwise: an idle map has none.
A quest of kind `"menu"` (Advance Worlds) runs as an event too, so its menu has `busy = "event"`.

A character's `level` and `levelLimit` (the level cap) are on `status`, on each of the Party
screen's `party` ranks and on each row of `units` and `storeUnits`. `noLimit` is true where the
game draws ∞ for the cap, on `status` and on a `units` row whose card is shown (Rance, and any
character a mod's hook on `キャラ_レベル上限なし` answers true for), and `levelLimit` is then
absent. The `party` ranks' cards show no cap, and a `units` or `storeUnits` row whose card is not
shown reads the save's data: there `noLimit` stays false and `levelLimit` is the cap the save
holds.

It builds the whole list, so do not call it on every `rq.on_frame`.

every screen that shows it; Rance Castle is the screen `castle`, with its rooms as `room-<area>`
and the town tabs; the town tabs on `quests`; the SYSTEM menu over Quests or the status page is
`system-menu` (it was the screen under it).
`other` with the footer only (they were the town or the castle under them, with its tabs).
chosen (they were, and gave no hover).
`store-drop`, `grid-drop`, `storeUnits` and `storeState` (it was not listed).
`close` (it was not listed).

```lua
local s = rq.ui.get()
if s and s.screen == "camp" then rq.log(#s.controls, "controls") end
if s and s.screen == "dungeon" and not s.busy then rq.log("the map is the player's") end
```

| Returns | Type | Description |
| --- | --- | --- |
| `screen` | `table\|nil` | The screen data, or nil before the game is ready. |

> Changed in 0.21.0: A screen with no name says `other`.

> Changed in 2.11.0: `covered`.

> Changed in 2.12.0: `focused` on kit controls.

> Changed in 2.19.0: `select.message`.

> Changed in 2.20.0: `status.chara` is the character shown (it was always 0).

> Changed in 2.20.1: The footer (`system`, `vault`, `trivia`, the party cards and the money line) on

> Changed in 2.22.1: Trivia, CG mode, Music mode and the castle's Gal monsters' and Poster rooms are

> Changed in 2.28.0: A dialog over Config is `select`; the quest rows are not `enabled` while a quest is

> Changed in 2.31.0: The Party screen's 2nd Army box: `store-N`, `store-status-N`, `store-close`,

> Changed in 2.41.0: The appraisal after a quest's success is the screen `appraisal`, with `finish` and

> Changed in 2.47.0: The Quest Storage window's tiles, `item-1` to `item-15` (they were not listed).

> Changed in 2.56.0: `busy`: a quest's event (`"event"`) or the wait after a fight (`"fight-end"`).

> Changed in 2.59.1: `status.noLimit` is the ∞ the game draws (it was always false, Rance's too).

See also: [`rq.ui.aim`](rq.ui.md#rquiaim)

### rq.ui.aim

```lua
rq.ui.aim(id) -> integer|nil, integer|nil
```

`since 0.20.0` `changed 0.21.0` `changed 2.11.0`

Returns the point a click on a control should land on.

The point is inside the control and not covered by another control. For a game control it is also
away from the kit's widgets over it. It builds the list when nothing did during this update.

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `string` | A control id, as `rq.ui.get` or `rqmod-ctl ui` lists it. |

| Returns | Type | Description |
| --- | --- | --- |
| `x` | `integer\|nil` | Click x in game pixels, or nil when the control is not on screen. |
| `y` | `integer\|nil` | Click y in game pixels. |

> Changed in 0.21.0: Builds the list itself; before, it read the last `rq.ui.get`.

> Changed in 2.11.0: Away from kit widgets over a game control.

### rq.ui.shot

```lua
rq.ui.shot(path, opts)
```

`since 0.21.0` `changed 2.67.0`

Saves what the game draws as a PNG at the next drawn frame.

The shot is taken later, so poll `rq.ui.shot_result` from `rq.on_frame` or a coroutine. The folders
in the path must already exist.

By default the shot is the game's picture, 1024 by 768, whatever the window's size. With
`window = true` it is the window as shown, at its own pixels: the picture enlarged by the chosen
filter, the 3D drawn at the window's size when that setting is on (`rq.ui.window`), without the
bars around it in full screen. While the game is paused from the pipe the window shot is the frame
on screen.

Raises an error before the game runs, when the path leaves the mod's folder, or while another shot
is still waiting.

```lua
rq.ui.shot("shots/camp.png")
rq.on_frame(function()
  local ok = rq.ui.shot_result()
  if ok ~= nil then rq.log("shot saved:", ok) end
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `path` | `string` | A path inside the mod's folder. |
| `opts` *(optional)* | [`rq.UiShotOpts`](../types/rq.UiShotOpts.md) | How to take it. Default: the game's picture. |

> Changed in 2.67.0: `opts.window`.

See also: [`rq.ui.shot_result`](rq.ui.md#rquishot_result), [`rq.ui.window`](rq.ui.md#rquiwindow)

### rq.ui.window

```lua
rq.ui.window() -> rq.UiWindow
```

`since 2.67.0`

Returns the window's size, the game's picture in it, and how the 3D is drawn.

The game draws a 1024 by 768 picture, which the window shows enlarged by the filter chosen on
Config's Other 2. The 3D (a fight's field, a quest's map) is drawn at the window's own pixels when
the window is larger than the game's picture and the setting "3D at the window's size" is on
(Config's Other 2 and the title bar's menu; on by default): `sharp_3d_shown` says whether the last
frame showed it so. It is not when the window is no larger, two 3D views show at once, or a
transition or a movie is drawn.

```lua
local w = rq.ui.window()
rq.log(("window %dx%d, scale %.2f, sharp 3D %s"):format(w.pixels_w, w.pixels_h, w.scale,
  tostring(w.sharp_3d_shown)))
```

| Returns | Type | Description |
| --- | --- | --- |
| `window` | [`rq.UiWindow`](../types/rq.UiWindow.md) | The window now. |

See also: [`rq.ui.set_window_size`](rq.ui.md#rquiset_window_size)

### rq.ui.set_window_size

```lua
rq.ui.set_window_size(w, h) -> boolean
```

`since 2.67.0`

Sets the window's inside size, in points, out of full screen.

The game's picture is fitted again at the next frame. The window may be larger than the screen.
For agents and tests: a mod should leave the window's size to the player.

Raises an error for a size under 64 by 48 or over 16384.

```lua
rq.ui.set_window_size(2048, 1536)  -- twice the game's picture on a monitor at 100%
```

| Parameter | Type | Description |
| --- | --- | --- |
| `w` | `integer` | Width in points. |
| `h` | `integer` | Height in points. |

| Returns | Type | Description |
| --- | --- | --- |
| `ok` | `boolean` | false when there is no window yet. |

See also: [`rq.ui.window`](rq.ui.md#rquiwindow)

### rq.ui.shot_result

```lua
rq.ui.shot_result() -> boolean|nil
```

`since 0.21.0`

Returns how the last `rq.ui.shot` ended, once.

| Returns | Type | Description |
| --- | --- | --- |
| `ok` | `boolean\|nil` | true or false once when the shot ended; nil while it waits, or when no result is left. |

### rq.ui.choose

```lua
rq.ui.choose(items, fn, opts) -> boolean
```

`since 2.7.0` `changed 2.50.0` `changed 2.56.0`

Opens the game's own choice menu outside a scene, on the hub or any of the game's screens, and
calls `fn` with the row the player picks.

The menu opens at the next update, and `fn` runs when it closes. It is modal: the game's screen
under it waits until the player picks, as under the vault's sort menu. It waits to open while the
System menu or Config is open, while a scene plays, while another choice menu shows, and while the
game saves (its "Auto-Saving" message holds 700 ms, and the game draws frames under it). The
menu does not scroll, so it takes at most 20 rows. It opens at the game's place (its top at y 360),
and a menu too tall to fit under it goes up just enough to fit on the screen. With fewer than 3 rows
it draws the game's tall buttons.

Under the menu, the HUD still draws (a mod's page stays on the screen, under the menu), but
`rq.uikit` widgets take no input and `rq.hud.capture_mouse` does nothing, so the menu gets the
mouse and the keys. The player cancels with a right click or Space, the game's cancel keys, or
the Return row; `fn` then gets 0. Esc does not cancel the game's menus. For a menu inside a scene
use `rq.scene.choice`; for its look as a widget on a page, `rq.uikit.options`.

Raises an error without a function, with a row without text, with no row to pick, or with more
than 20 rows.

rows its last rows were off the screen.

```lua
rq.ui.choose({ "Sell all", { id = "keep", text = "Keep the rare ones" }, "-", "Sort first" },
  function(id)
    if id == 0 then return end -- cancelled
    rq.log("picked", id)
  end, { message = "What now?" })
```

| Parameter | Type | Description |
| --- | --- | --- |
| `items` | `(string\|` [`rq.UiChoice`](../types/rq.UiChoice.md) `)[]` | The rows: a text, `"-"` for a separator, or a table. |
| `fn` | `fun(id: any)` | Called once with the picked row's id, or 0 when cancelled. |
| `opts` *(optional)* | `{message?: string, back?: string\|boolean, cancel?: boolean, cursor?: any, x?: integer, y?: integer}` | `message`: text rows over the list ("\n" starts a line). `back`: the Return row's text, or false for none (default "Return"). `cancel`: false turns off the right click and Space (default true). `cursor`: the id of the row the cursor starts on. `x`, `y`: the menu's top left (default the center). |

| Returns | Type | Description |
| --- | --- | --- |
| `opened` | `boolean` | true when the menu will open; false when one is already waiting or open, and then `fn` is not called. |

> Changed in 2.50.0: Waits for the game's save to end.

> Changed in 2.56.0: A menu too tall for the room under y 360 goes up to fit. Before, past about 12

See also: [`rq.ui.choosing`](rq.ui.md#rquichoosing), [`rq.uikit.options`](rq.uikit.md#rquikitoptions)

### rq.ui.choosing

```lua
rq.ui.choosing() -> boolean
```

`since 2.7.0`

Says whether the game's choice menu shows: one of the game's own, `rq.scene.choice` or
`rq.ui.choose`.

While it does, the HUD draws under the menu, and `rq.uikit` widgets take no input until the
mouse buttons are up after it.

| Returns | Type | Description |
| --- | --- | --- |
| `choosing` | `boolean` | true while the menu shows. |

### rq.ui.confirm

```lua
rq.ui.confirm(text, opts) -> boolean|nil
```

`since 2.19.0` `changed 2.28.0` `changed 2.44.0`

Asks the player Yes or No in the game's own dialog, and waits for the answer.

It is the window of the game's `選択_確認`: the text, then Yes and No as the game's tall buttons.
The call returns when the player picks, as the game's own questions do, so it can answer inside
the game's flow: from an `rq.ain.hook` callback, a kit widget's click (`rq.on_frame`), a button on
a mod's Config page, an `rq.ui.choose` callback or a scene. While it shows, the HUD draws under it
and `rq.uikit` widgets take no input (`rq.ui.choosing`); every `rq.on_frame` callback still runs,
the caller's too.

Over Config, on any of its tabs, the dialog draws over it, with a mod's page between them, and
its rows' comments too. The game opens no dialog there itself; before 2.28.0 a mod's opened under
Config, out of sight.

Only "\n" starts a line in the text; the window wraps it at its width, and gives every 3 lines a row
of their own. `@` and `$`, where the game's own texts break, are drawn as `＠` and `＄` (the game's
font draws them half wide, with a space after) unless `opts.game` is true, for a text that comes
from the game.

With `opts.remember`, the window adds the game's "don't ask again" row. A number 1 to 99 is the
game's own switch (as `選択_確認_拡張`: 10 purchasing, 14 selling, 31 donating, and the others in
Config's Confirmations tab), so the player's setting counts. A text is the mod's own question: once
the player turns it off, the call returns true without asking, in every save. The loader then
lists it on a Confirmations page in Config's Mods tab, where the player can turn it back on, and
Resetting in Config's Confirmations tab turns it back on too. The key is the mod's own, found as
`rq.mod.id` finds it (through `return rq.ui.confirm(...)` too, since 2.24.1).

The row starts unticked, as the game's. `opts.remember_checked` shows it ticked, with its words
and the game's tick (the game's own ticked row reads "UNDO"): when the player answers with it still
ticked, the question is turned off, whichever button they pressed. Ticked or not, a tick takes
effect at once, as in the game's own dialogs.

The game has one list of dialog rows, so the call shows nothing and returns nil while another
dialog is being built or shows (`rq.ui.choosing`, or one of these calls), and logs it once.

Raises an error while `init.lua` loads (the game is not running yet), for an empty text or one that
is not a string, for more than 9 lines, for an option of the wrong type, for a `remember` that
is neither a text nor 1 to 99, and for a `remember_checked` without `remember`.

```lua
if rq.ui.confirm("Swap the absorbed item?\nThe old one goes back to the vault.",
    { remember = "swap", remember_label = "Swapping an absorbed item" }) then
  swap()
end
```

| Parameter | Type | Description |
| --- | --- | --- |
| `text` | `string` | The question. |
| `opts` *(optional)* | `{yes?: string, no?: string, cursor?: "yes"\|"no", sound_yes?: integer, sound_no?: integer, remember?: string\|integer, remember_label?: string, remember_checked?: boolean, game?: boolean}` | `yes`, `no`: the buttons' labels (default "Yes", "No"). `cursor`: the button the cursor starts on (default "yes"). `sound_yes`, `sound_no`: sound numbers for the buttons (default the game's). `remember`: a key for the mod's own "don't ask again", or 1 to 99 for the game's own. `remember_label`: how the Confirmations page names the mod's question (default the key). `remember_checked`: the row starts ticked (default false; since 2.44.0). `game`: the text is the game's, where `@` and `$` start a line. |

| Returns | Type | Description |
| --- | --- | --- |
| `yes` | `boolean\|nil` | true for Yes (or a question turned off), false for No, nil when it was not shown. |

> Changed in 2.28.0: Shown over Config.

> Changed in 2.44.0: `remember_checked`.

See also: [`rq.ui.notice`](rq.ui.md#rquinotice), [`rq.ui.ask`](rq.ui.md#rquiask)

### rq.ui.notice

```lua
rq.ui.notice(text, opts) -> boolean|nil
```

`since 2.19.0` `changed 2.28.0`

Tells the player something in the game's own dialog, with one OK button, and waits until it is
pressed.

It is the window of the game's `選択_通知`. The text, where it may be called from, and the one
dialog at a time are as for `rq.ui.confirm`.

Raises an error while `init.lua` loads, for an empty text or one that is not a string, for more
than 9 lines, and for an option of the wrong type.

```lua
rq.ui.notice("The vault cannot take " .. name .. ".")
```

| Parameter | Type | Description |
| --- | --- | --- |
| `text` | `string` | The message. |
| `opts` *(optional)* | `{ok?: string, game?: boolean}` | `ok`: the button's label (default "OK"). `game`: the text is the game's, where `@` and `$` start a line. |

| Returns | Type | Description |
| --- | --- | --- |
| `shown` | `boolean\|nil` | true once the player pressed OK, nil when it was not shown. |

> Changed in 2.28.0: Shown over Config.

### rq.ui.ask

```lua
rq.ui.ask(text, rows, opts) -> any|nil
```

`since 2.19.0` `changed 2.28.0` `changed 2.44.0` `changed 2.56.0`

Asks the player a question with any choices in the game's own dialog, and waits for the answer.

It is the game's window as `選択_確認` builds it, with the rows given: the text, a separator, then
the rows. With fewer than 3 choices they are the game's tall buttons. The text, where it may be
called from, and the one dialog at a time are as for `rq.ui.confirm`. Unlike `rq.ui.choose`, it
waits for the answer, has a text over the rows, and has no Return row and no cancel unless asked.

With `opts.remember`, the window adds the game's "don't ask again" row under the rows, as
`rq.ui.confirm` does, with the same keys: a number 1 to 99 is the game's own switch, a text the
mod's own question. The row stands for one answer, `opts.remember_answer` (default the first row):
once the player turns the question off, the call returns that row's id without asking. Pressing
the row keeps the window open, as in the game's own dialogs; the player then picks a row.
`opts.remember_checked` shows the row ticked: when the player picks a row with it still ticked, the
question is turned off, whichever row they picked (a cancel turns nothing off).

The window does not scroll: the rows to pick and the lines of text together are at most 20 (two
separators count as one), for example 9 lines and 11 rows, or 20 rows and no text. A window too
tall for the room under its place goes up just enough to fit on the screen (since 2.56.0). With
`opts.remember`, the "don't ask again" row and its note count as 2 more, and the separator over
them as one more separator.

Raises an error while `init.lua` loads, for a text that is not a string, for more than 9 lines, for
a row without text, with no row to pick, with more rows and lines than fit, for an option of the
wrong type, for a `remember` that is neither a text nor 1 to 99, for a `remember_answer` that is no
row's id, and for a `remember_answer` or a `remember_checked` without `remember`.

```lua
local pick = rq.ui.ask("Take Quest@Gem Lady?", {
  { id = "yes", text = "Yes", sound = 5012 }, { id = "trade", text = "Trade a Jewel" }, { id = "no", text = "No" },
}, { game = true, cursor = "yes", remember = 11 }) -- the game's "Take Quest" switch

-- Asked once: ticked from the start, and "no" while it is turned off.
local copy = rq.ui.ask("Copy the other save?", { { id = "yes", text = "Yes" }, { id = "no", text = "No" } },
  { remember = "copy", remember_answer = "no", remember_checked = true })
```

| Parameter | Type | Description |
| --- | --- | --- |
| `text` | `string\|nil` | The question, or nil for rows only. |
| `rows` | `(string\|` [`rq.UiAskRow`](../types/rq.UiAskRow.md) `)[]` | The rows: a text, `"-"` for a separator, or a table. |
| `opts` *(optional)* | `{cursor?: any, cancel?: boolean, x?: integer, y?: integer, game?: boolean, remember?: string\|integer, remember_label?: string, remember_answer?: any, remember_checked?: boolean}` | `cursor`: the id of the row the cursor starts on. `cancel`: true lets a right click or Space close it, and the call returns 0 (default false, as the game's questions). `x`, `y`: the dialog's top left (default the center). `game`: the text is the game's, where `@` and `$` start a line. `remember`: a key for the mod's own "don't ask again", or 1 to 99 for the game's own. `remember_label`: how the Confirmations page names the mod's question (default the key). `remember_answer`: the id of the row returned while the question is turned off (default the first row). `remember_checked`: the row starts ticked (default false; since 2.44.0). |

| Returns | Type | Description |
| --- | --- | --- |
| `id` | `any\|nil` | The picked row's id, 0 when cancelled, `remember_answer` while the question is turned off, nil when it was not shown. |

> Changed in 2.28.0: Shown over Config; `remember`, `remember_label` and `remember_answer`.

> Changed in 2.44.0: `remember_checked`.

> Changed in 2.56.0: A window too tall for the room under its place goes up to fit.

See also: [`rq.ui.choose`](rq.ui.md#rquichoose)

### rq.ui.quest_storage

```lua
rq.ui.quest_storage() -> rq.UiQuestStorage|nil
```

`since 2.47.0`

Returns the game's Quest Storage window while it shows, with its item tiles.

The window (`T_StoreQuest`) shows over a quest's map. Its tiles are 100 × 100, five to a row,
106 apart, from x 482, y 204, the same in every mode. A mod draws on them from `rq.on_frame`, such
as a mark or a button in a tile's corner (`rq.uikit.icon_button`); a click on a tile does nothing
in the game, and the game gets no mouse over a kit widget. After a mod moves an item in or out of
the quest storage (`rq.item.set`'s `place`, 8), `rq.ui.quest_storage_refresh` shows the change.
Agents see the tiles as the controls `item-<index>` of the `quest-storage` screen, with the
instance as the value.

```lua
rq.on_frame(function()
  local qs = rq.ui.quest_storage()
  if not qs or qs.mode ~= "view" or qs.dialog then return end
  for _, t in ipairs(qs.tiles) do
    if not t.identified then rq.hud.rect(t.x + 80, t.y + 4, 16, 16, 255, 200, 0, 200) end
  end
end)
```

| Returns | Type | Description |
| --- | --- | --- |
| `qs` | [`rq.UiQuestStorage`](../types/rq.UiQuestStorage.md) `\|nil` | The window, or nil when it does not show. |

See also: [`rq.ui.quest_storage_refresh`](rq.ui.md#rquiquest_storage_refresh)

### rq.ui.quest_storage_refresh

```lua
rq.ui.quest_storage_refresh() -> boolean
```

`since 2.47.0`

Builds the game's Quest Storage window again from the quest storage's items.

It does what the window's erase button does after an erase: the list, the tiles, their z and the
buttons. Call it after moving items in or out of the quest storage while the window shows.

```lua
rq.item.set(ii, { place = 11 })  -- out of the quest storage, into the storage
rq.ui.quest_storage_refresh()
```

| Returns | Type | Description |
| --- | --- | --- |
| `ok` | `boolean` | false when the window does not show, or when the game refused (written to the log). |
