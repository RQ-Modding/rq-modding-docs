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

### rq.ui.get

```lua
rq.ui.get() -> table|nil
```

`since 0.20.0` `changed 0.21.0`

Returns what is on the screen.

The table holds `screen` (the screen's name), `hover`, `controls` (each with `id`, `x`, `y`, `w`,
`h`, `enabled` and more) and the data of the current screen, such as `battle` or `quests`. A
screen with no name, such as a black one during a change of scene, says `other`; `boot` is used
only before the first named screen, and `title` only for the real title screen.

It builds the whole list, so do not call it on every `rq.on_frame`.

```lua
local s = rq.ui.get()
if s and s.screen == "camp" then rq.log(#s.controls, "controls") end
```

| Returns | Type | Description |
| --- | --- | --- |
| `screen` | `table\|nil` | The screen data, or nil before the game is ready. |

> Changed in 0.21.0: A screen with no name says `other`.

See also: [`rq.ui.aim`](rq.ui.md#rquiaim)

### rq.ui.aim

```lua
rq.ui.aim(id) -> integer|nil, integer|nil
```

`since 0.20.0` `changed 0.21.0`

Returns the point a click on a control should land on.

The point is inside the control and not covered by another control. It builds the list when
nothing did during this update.

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `string` | A control id, as `rq.ui.get` or `rqmod-ctl ui` lists it. |

| Returns | Type | Description |
| --- | --- | --- |
| `x` | `integer\|nil` | Click x in game pixels, or nil when the control is not on screen. |
| `y` | `integer\|nil` | Click y in game pixels. |

> Changed in 0.21.0: Builds the list itself; before, it read the last `rq.ui.get`.

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
