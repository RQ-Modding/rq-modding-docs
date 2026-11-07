# rq.input

`since 0.2.0`

Reads the mouse and keyboard, and drives them for the game.

The read calls see the real buttons, also while `rq.hud.block_game_input` or `rq.hud.block_keys`
hides them from the game, so a modal HUD can still read clicks, Enter and Esc. The `set_*` calls,
`wheel` and `release` act for the player, as a test or an automation would. Typed text is read
with `rq.hud.text_begin`.

## Functions

| Name | Summary |
| --- | --- |
| [`rq.input.mouse`](#rqinputmouse) | Returns the mouse position and buttons on this update. |
| [`rq.input.key`](#rqinputkey) | Returns whether a key is down, by its raw SACT code. |
| [`rq.input.code`](#rqinputcode) | Returns the key code for a key name. |
| [`rq.input.set_key`](#rqinputset_key) | Presses or lets go of a key for the game. |
| [`rq.input.set_mouse`](#rqinputset_mouse) | Moves the game's mouse. |
| [`rq.input.wheel`](#rqinputwheel) | Sends one wheel step to the game. |
| [`rq.input.release`](#rqinputrelease) | Gives the mouse back to the player. |
| [`rq.input.scroll`](#rqinputscroll) | Returns the wheel steps since the last update. |

### rq.input.mouse

```lua
rq.input.mouse() -> integer, integer, boolean, boolean, boolean, boolean
```

`since 0.2.0` `changed 1.6.0`

Returns the mouse position and buttons on this update.

The buttons are the real ones, also while the game's input is blocked. `pressed` and `released`
are true only on the update the left button went down or came up, as a slider needs to start and
end a drag.

```lua
local x, y, left, right, pressed = rq.input.mouse()
if pressed then rq.log("click at", x, y) end
```

| Returns | Type | Description |
| --- | --- | --- |
| `x` | `integer` | Cursor x, in game pixels. |
| `y` | `integer` | Cursor y, in game pixels. |
| `left` | `boolean` | The left button is down. |
| `right` | `boolean` | The right button is down. |
| `pressed` | `boolean` | The left button went down on this update. |
| `released` | `boolean` | The left button came up on this update. |

> Changed in 1.6.0: Added the `pressed` and `released` results.

See also: [`rq.hud.clicked`](rq.hud.md#rqhudclicked)

### rq.input.key

```lua
rq.input.key(code) -> boolean
```

`since 0.2.0`

Returns whether a key is down, by its raw SACT code.

It reads the real key, also while `rq.hud.block_keys` hides it from the game. Get a code from a
name with `rq.input.code`.

```lua
if rq.input.key(rq.input.code("esc")) then close_menu() end
```

| Parameter | Type | Description |
| --- | --- | --- |
| `code` | `integer` | A SACT key code (`VK_LBUTTON` is 1, Enter is 13). |

| Returns | Type | Description |
| --- | --- | --- |
| `down` | `boolean` | true while the key is down. |

### rq.input.code

```lua
rq.input.code(key) -> integer
```

`since 0.20.0`

Returns the key code for a key name.

The names are those `rqmod-ctl` uses, such as `"enter"`, `"esc"`, `"lmb"`, `"f3"` or `"a"`. A number
is returned as it is.

Raises an error for an unknown name.

| Parameter | Type | Description |
| --- | --- | --- |
| `key` | `string\|integer` | A key name, or a code. |

| Returns | Type | Description |
| --- | --- | --- |
| `code` | `integer` | The SACT key code. |

### rq.input.set_key

```lua
rq.input.set_key(key, down)
```

`since 0.20.0`

Presses or lets go of a key for the game.

The key stays down until you let go of it. The decide key is the left button or Enter, and a click
lands when the button comes up, so hold it down for a few updates before letting go.

Raises an error for an unknown key name.

```lua
rq.input.set_key("enter", true)
-- a few updates later:
rq.input.set_key("enter", false)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `key` | `string\|integer` | A key name as for `rq.input.code`, or a code. |
| `down` | `boolean` | true to press it, false to let go. |

### rq.input.set_mouse

```lua
rq.input.set_mouse(x, y)
```

`since 0.20.0`

Moves the game's mouse.

The cursor stays there and the real mouse is ignored until `rq.input.release`.

| Parameter | Type | Description |
| --- | --- | --- |
| `x` | `integer` | Cursor x, in game pixels. |
| `y` | `integer` | Cursor y, in game pixels. |

See also: [`rq.input.release`](rq.input.md#rqinputrelease)

### rq.input.wheel

```lua
rq.input.wheel(dir)
```

`since 0.20.0`

Sends one wheel step to the game.

`rq.input.scroll` counts it too.

| Parameter | Type | Description |
| --- | --- | --- |
| `dir` | `integer` | Positive scrolls up, negative scrolls down. |

### rq.input.release

```lua
rq.input.release()
```

`since 0.20.0`

Gives the mouse back to the player.

Ends `rq.input.set_mouse` and lets go of the mouse buttons. Keys pressed with `set_key` stay as
they are.

### rq.input.scroll

```lua
rq.input.scroll(eat) -> integer
```

`since 1.7.0`

Returns the wheel steps since the last update.

With `eat` true the game does not get them, as for a list that scrolls under the mouse. Steps sent
with `rq.input.wheel` count too.

```lua
if rq.hud.hit(list_x, list_y, list_w, list_h) then
  top = top - rq.input.scroll(true)
end
```

| Parameter | Type | Description |
| --- | --- | --- |
| `eat` *(optional)* | `boolean` | true to keep the steps from the game. Default false. |

| Returns | Type | Description |
| --- | --- | --- |
| `steps` | `integer` | Up is positive, down negative; 0 when the wheel did not move. |
