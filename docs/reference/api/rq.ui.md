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
| [`rq.ui.shot_result`](#rquishot_result) | Returns how the last `rq.ui.shot` ended, once. |
| [`rq.ui.choose`](#rquichoose) | Opens the game's own choice menu outside a scene, on the hub or any of the game's screens, and calls `fn` with the row the player picks. |
| [`rq.ui.choosing`](#rquichoosing) | Says whether the game's choice menu shows: one of the game's own, `rq.scene.choice` or `rq.ui.choose`. |
| [`rq.ui.confirm`](#rquiconfirm) | Asks the player Yes or No in the game's own dialog, and waits for the answer. |
| [`rq.ui.notice`](#rquinotice) | Tells the player something in the game's own dialog, with one OK button, and waits until it is pressed. |
| [`rq.ui.ask`](#rquiask) | Asks the player a question with any choices in the game's own dialog, and waits for the answer. |

### rq.ui.get

```lua
rq.ui.get() -> table|nil
```

`since 0.20.0` `changed 0.21.0` `changed 2.11.0` `changed 2.12.0` `changed 2.19.0` `changed 2.20.0`

Returns what is on the screen.

The table holds `screen` (the screen's name), `hover`, `controls` (each with `id`, `x`, `y`, `w`,
`h`, `enabled` and more) and the data of the current screen, such as `battle` or `quests`. A
screen with no name, such as a black one during a change of scene, says `other`; `boot` is used
only before the first named screen, and `title` only for the real title screen.

A game control a player cannot click has `covered = true`: every point of it is under a kit widget
of the last update (section `kit`), or a mod's page captures the mouse (`rq.hud.capture_mouse`).
`rqmod-ctl press` refuses it. A page closed on this update still covers until the next one.

A kit control (section `kit`) under the kit's keys cursor has `focused = true` (`rq.uikit.focused`).

On the screen `select` (the game's choice menu and dialogs), `select.message` holds the dialog's
text rows, one a line.

It builds the whole list, so do not call it on every `rq.on_frame`.

```lua
local s = rq.ui.get()
if s and s.screen == "camp" then rq.log(#s.controls, "controls") end
```

| Returns | Type | Description |
| --- | --- | --- |
| `screen` | `table\|nil` | The screen data, or nil before the game is ready. |

> Changed in 0.21.0: A screen with no name says `other`.

> Changed in 2.11.0: `covered`.

> Changed in 2.12.0: `focused` on kit controls.

> Changed in 2.19.0: `select.message`.

> Changed in 2.20.0: `status.chara` is the character shown (it was always 0).

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
rq.ui.shot(path)
```

`since 0.21.0`

Saves what the game draws as a PNG at the next drawn frame.

The shot is taken later, so poll `rq.ui.shot_result` from `rq.on_frame` or a coroutine. The folders
in the path must already exist.

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
| `path` | `string` | A path inside the mod's folder, in ASCII. |

See also: [`rq.ui.shot_result`](rq.ui.md#rquishot_result)

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

`since 2.7.0`

Opens the game's own choice menu outside a scene, on the hub or any of the game's screens, and
calls `fn` with the row the player picks.

The menu opens at the next update, and `fn` runs when it closes. It is modal: the game's screen
under it waits until the player picks, as under the vault's sort menu. It waits to open while the
System menu or Config is open, while a scene plays, and while another choice menu shows. The
menu does not scroll, so it takes at most 20 rows. With fewer than 3 rows it draws the game's tall
buttons.

Under the menu, the HUD still draws (a mod's page stays on the screen, under the menu), but
`rq.uikit` widgets take no input and `rq.hud.capture_mouse` does nothing, so the menu gets the
mouse and the keys. The player cancels with a right click or Space, the game's cancel keys, or
the Return row; `fn` then gets 0. Esc does not cancel the game's menus. For a menu inside a scene
use `rq.scene.choice`; for its look as a widget on a page, `rq.uikit.options`.

Raises an error without a function, with a row without text, with no row to pick, or with more
than 20 rows.

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

`since 2.19.0`

Asks the player Yes or No in the game's own dialog, and waits for the answer.

It is the window of the game's `選択_確認`: the text, then Yes and No as the game's tall buttons.
The call returns when the player picks, as the game's own questions do, so it can answer inside
the game's flow: from an `rq.ain.hook` callback, a kit widget's click (`rq.on_frame`), an
`rq.ui.choose` callback or a scene. While it shows, the HUD draws under it and `rq.uikit` widgets
take no input (`rq.ui.choosing`); every `rq.on_frame` callback still runs, the caller's too.

Only "\n" starts a line in the text; the window wraps it at its width, and gives every 3 lines a row
of their own. `@` and `$`, where the game's own texts break, are drawn as `＠` and `＄` (the game's
font draws them half wide, with a space after) unless `opts.game` is true, for a text that comes
from the game.

With `opts.remember`, the window adds the game's "don't ask again" row. A number 1 to 99 is the
game's own switch (as `選択_確認_拡張`: 10 purchasing, 14 selling, 31 donating, and the others in
Config's Confirmations tab), so the player's setting counts. A text is the mod's own question: once
the player turns it off, the call returns true without asking, in every save. The loader then
lists it on a Confirmations page in Config's Mods tab, where the player can turn it back on, and
Resetting in Config's Confirmations tab turns it back on too.

The game has one list of dialog rows, so the call shows nothing and returns nil while another
dialog is being built or shows (`rq.ui.choosing`, or one of these calls), and logs it once.

Raises an error while `init.lua` loads (the game is not running yet), for an empty text or one that
is not a string, for more than 9 lines, for an option of the wrong type, and for a `remember` that
is neither a text nor 1 to 99.

```lua
if rq.ui.confirm("Swap the absorbed item?\nThe old one goes back to the vault.",
    { remember = "swap", remember_label = "Swapping an absorbed item" }) then
  swap()
end
```

| Parameter | Type | Description |
| --- | --- | --- |
| `text` | `string` | The question. |
| `opts` *(optional)* | `{yes?: string, no?: string, cursor?: "yes"\|"no", sound_yes?: integer, sound_no?: integer, remember?: string\|integer, remember_label?: string, game?: boolean}` | `yes`, `no`: the buttons' labels (default "Yes", "No"). `cursor`: the button the cursor starts on (default "yes"). `sound_yes`, `sound_no`: sound numbers for the buttons (default the game's). `remember`: a key for the mod's own "don't ask again", or 1 to 99 for the game's own. `remember_label`: how the Confirmations page names the mod's question (default the key). `game`: the text is the game's, where `@` and `$` start a line. |

| Returns | Type | Description |
| --- | --- | --- |
| `yes` | `boolean\|nil` | true for Yes (or a question turned off), false for No, nil when it was not shown. |

See also: [`rq.ui.notice`](rq.ui.md#rquinotice), [`rq.ui.ask`](rq.ui.md#rquiask)

### rq.ui.notice

```lua
rq.ui.notice(text, opts) -> boolean|nil
```

`since 2.19.0`

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

### rq.ui.ask

```lua
rq.ui.ask(text, rows, opts) -> any|nil
```

`since 2.19.0`

Asks the player a question with any choices in the game's own dialog, and waits for the answer.

It is the game's window as `選択_確認` builds it, with the rows given: the text, a separator, then
the rows. With fewer than 3 choices they are the game's tall buttons. The text, where it may be
called from, and the one dialog at a time are as for `rq.ui.confirm`. Unlike `rq.ui.choose`, it
waits for the answer, has a text over the rows, and has no Return row and no cancel unless asked.

The window does not scroll: the rows to pick and the lines of text together are at most 20 (two
separators count as one), for example 9 lines and 11 rows, or 20 rows and no text.

Raises an error while `init.lua` loads, for a text that is not a string, for more than 9 lines, for
a row without text, with no row to pick, with more rows and lines than fit, and for an option of the
wrong type.

```lua
local pick = rq.ui.ask("Take Quest@Gem Lady?", {
  { id = "yes", text = "Yes", sound = 5012 }, { id = "trade", text = "Trade a Jewel" }, { id = "no", text = "No" },
}, { game = true, cursor = "yes" })
```

| Parameter | Type | Description |
| --- | --- | --- |
| `text` | `string\|nil` | The question, or nil for rows only. |
| `rows` | `(string\|` [`rq.UiAskRow`](../types/rq.UiAskRow.md) `)[]` | The rows: a text, `"-"` for a separator, or a table. |
| `opts` *(optional)* | `{cursor?: any, cancel?: boolean, x?: integer, y?: integer, game?: boolean}` | `cursor`: the id of the row the cursor starts on. `cancel`: true lets a right click or Space close it, and the call returns 0 (default false, as the game's questions). `x`, `y`: the dialog's top left (default the center). `game`: the text is the game's, where `@` and `$` start a line. |

| Returns | Type | Description |
| --- | --- | --- |
| `id` | `any\|nil` | The picked row's id, 0 when cancelled, nil when it was not shown. |

See also: [`rq.ui.choose`](rq.ui.md#rquichoose)
