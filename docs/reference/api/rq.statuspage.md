# rq.statuspage

`since 2.20.0`

A character's status page, for mods.

The page is the game's (`T_Status`): a mod reads which character it shows, draws its card again
after changing that character, and hears when it opens, changes character, is drawn again and
closes. Buttons on it are `rq.gamebutton`'s `"status"` group. (`rq.status` is the mod states'
module.)

The card is drawn by the game on open, on a change of character (the scroll bar, the wheel, the
keys), after every equip, skill or profile change, and when the skill window closes; `on_update`
follows each of those.

```lua
rq.statuspage.on_chara(function(chara, old) rq.log("from", old, "to", chara) end)
rq.gamebutton.add({ group = "status", id = "heal", label = "Heal", icon = 11158,
  on_click = function()
    local c = rq.statuspage.chara()
    rq.chara.set(c, { hp = rq.chara.get(c).hp_max })
    rq.statuspage.refresh()
  end })
```

## Functions

| Name | Summary |
| --- | --- |
| [`rq.statuspage.chara`](#rqstatuspagechara) | Returns the character the status page shows. |
| [`rq.statuspage.mode`](#rqstatuspagemode) | Returns how the status page was opened. |
| [`rq.statuspage.refresh`](#rqstatuspagerefresh) | skill window (the game draws the card again when it closes), while a skill is being moved, or when called from inside an `on_update`, `on_open` or `on_chara` callback. |

### rq.statuspage.chara

```lua
rq.statuspage.chara() -> integer?
```

`since 2.20.0`

Returns the character the status page shows.

| Returns | Type | Description |
| --- | --- | --- |
| `chara` | `integer?` | The character number (iic), or nil while the page is closed. |

### rq.statuspage.mode

```lua
rq.statuspage.mode() -> rq.StatusPageMode?
```

`since 2.20.0`

Returns how the status page was opened.

| Returns | Type | Description |
| --- | --- | --- |
| `mode` | `rq.StatusPageMode` `?` | The mode, or nil while the page is closed. |

### rq.statuspage.refresh

```lua
rq.statuspage.refresh()
```

skill window (the game draws the card again when it closes), while a skill is being moved, or when
called from inside an `on_update`, `on_open` or `on_chara` callback.

## Events

| Name | Summary |
| --- | --- |
| [`rq.statuspage.on_open`](#rqstatuspageon_open) | Calls `fn` when the status page opens, once its first character is drawn. |
| [`rq.statuspage.on_chara`](#rqstatuspageon_chara) | Calls `fn` when the status page shows another character. |
| [`rq.statuspage.on_update`](#rqstatuspageon_update) | Calls `fn` after every draw of the status page's card: open, another character, a change of equipment, skills or profile, the skill window closing, `refresh`. |
| [`rq.statuspage.on_close`](#rqstatuspageon_close) | Calls `fn` after the status page closes. |

### rq.statuspage.on_open

```lua
rq.statuspage.on_open(fn) -> fun()
```

`since 2.20.0`

Calls `fn` when the status page opens, once its first character is drawn.

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(chara: integer, mode:` `rq.StatusPageMode` `?)` | Gets the character and how the page was opened. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

### rq.statuspage.on_chara

```lua
rq.statuspage.on_chara(fn) -> fun()
```

`since 2.20.0`

Calls `fn` when the status page shows another character.

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(chara: integer, old: integer)` | Gets the character now shown and the one before. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

### rq.statuspage.on_update

```lua
rq.statuspage.on_update(fn) -> fun()
```

`since 2.20.0`

Calls `fn` after every draw of the status page's card: open, another character, a change of
equipment, skills or profile, the skill window closing, `refresh`.

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(chara: integer)` | Gets the character shown. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

### rq.statuspage.on_close

```lua
rq.statuspage.on_close(fn) -> fun()
```

`since 2.20.0`

Calls `fn` after the status page closes.

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun()` | Runs on close. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |
