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
