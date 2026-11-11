# rq.game

`since 2.33.0`

The player's money and charisma, as the system bar shows them.

Every call that changes a value redraws the system bar. Not at the top level of a mod: the game is
not running yet.

```lua
--- Money and charisma for every level a character gains
rq.chara.on_level_up(function(ctx)
  rq.game.add_gold(ctx.level * 100)
  rq.game.add_charisma(5)
end)
```

## Functions

| Name | Summary |
| --- | --- |
| [`rq.game.gold`](#rqgamegold) | Returns the player's money. |
| [`rq.game.set_gold`](#rqgameset_gold) | Sets the player's money. |
| [`rq.game.add_gold`](#rqgameadd_gold) | Adds to the player's money, or takes from it. |
| [`rq.game.charisma`](#rqgamecharisma) | Returns the charisma rank and its points, as the system bar shows them. |
| [`rq.game.add_charisma`](#rqgameadd_charisma) | Adds charisma points, or takes them away. |
| [`rq.game.set_charisma`](#rqgameset_charisma) | Sets the charisma rank, and its points when given. |
| [`rq.game.mode`](#rqgamemode) | Returns the game's mode: Classic or TADA. |
| [`rq.game.set_mode`](#rqgameset_mode) | Sets the game's mode, as the choice at the support menu does. It stays in the save. |

### rq.game.gold

```lua
rq.game.gold() -> integer
```

`since 2.33.0`

Returns the player's money.

| Returns | Type | Description |
| --- | --- | --- |
| `gold` | `integer` | 0 to 999,999,999. |

### rq.game.set_gold

```lua
rq.game.set_gold(n) -> integer
```

`since 2.33.0`

Sets the player's money.

The game keeps it between 0 and 999,999,999; a value outside is cut to that range.

| Parameter | Type | Description |
| --- | --- | --- |
| `n` | `integer` | The money, a whole number. |

| Returns | Type | Description |
| --- | --- | --- |
| `gold` | `integer` | The money now. |

### rq.game.add_gold

```lua
rq.game.add_gold(n) -> integer
```

`since 2.33.0`

Adds to the player's money, or takes from it.

The result stays between 0 and 999,999,999, as the game's own shop keeps it.

```lua
if rq.game.gold() >= 500 then rq.game.add_gold(-500) end
```

| Parameter | Type | Description |
| --- | --- | --- |
| `n` | `integer` | The amount; negative takes away. |

| Returns | Type | Description |
| --- | --- | --- |
| `gold` | `integer` | The money now. |

### rq.game.charisma

```lua
rq.game.charisma() -> integer, integer, integer
```

`since 2.33.0`

Returns the charisma rank and its points, as the system bar shows them.

The game calls it fame (`名声`). The points fill toward `max`; at `max` the rank goes up after the
next quest's result.

| Returns | Type | Description |
| --- | --- | --- |
| `rank` | `integer` | The rank. |
| `points` | `integer` | The points in this rank. |
| `max` | `integer` | The points the rank needs to go up. |

### rq.game.add_charisma

```lua
rq.game.add_charisma(n) -> integer, integer, integer
```

`since 2.33.0`

Adds charisma points, or takes them away.

Points added go up one rank at most, as the result screen does: when they fill the bar, the rank
rises once and the rest is kept for the next one. Points taken never go below 0 and never lower
the rank.

```lua
local rank = rq.game.add_charisma(100)
rq.log("rank now " .. rank)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `n` | `integer` | The points; negative takes away. |

| Returns | Type | Description |
| --- | --- | --- |
| `rank` | `integer` | The rank now. |
| `points` | `integer` | The points now. |
| `max` | `integer` | The points the rank now needs. |

### rq.game.set_charisma

```lua
rq.game.set_charisma(rank, points) -> integer, integer, integer
```

`since 2.33.0`

Sets the charisma rank, and its points when given.

The points the rank needs (`max`) follow from the rank, as the game sets them at a world transfer.

| Parameter | Type | Description |
| --- | --- | --- |
| `rank` | `integer` | The rank, 0 or more. |
| `points` *(optional)* | `integer` | The points, 0 or more. Default: keep them. |

| Returns | Type | Description |
| --- | --- | --- |
| `rank` | `integer` | The rank now. |
| `points` | `integer` | The points now. |
| `max` | `integer` | The points the rank now needs. |

### rq.game.mode

```lua
rq.game.mode() -> "classic"|"tada"|nil
```

`since 2.36.0`

Returns the game's mode: Classic or TADA.

TADA mode is the choice at the support menu (`◆２倍モード`). It doubles a fight's EXP and gold
and a familiar's growth; Custom TADA Mode changes those numbers.

There is no easy mode to report. Its flags (`◆ｅａｓｙモード`) are a leftover of the first Rance
Quest: Magnum never sets them, and the quest menu clears them each time it opens.

```lua
if rq.game.mode() == "tada" then rq.log("TADA mode") end
```

| Returns | Type | Description |
| --- | --- | --- |
| `mode` | `"classic"\|"tada"\|nil` | nil before a save is loaded. |

### rq.game.set_mode

```lua
rq.game.set_mode(mode)
```

`since 2.36.0`

Sets the game's mode, as the choice at the support menu does. It stays in the save.

Raises an error for another text, or before a save is loaded.

```lua
rq.game.set_mode("classic")
```

| Parameter | Type | Description |
| --- | --- | --- |
| `mode` | `"classic"\|"tada"` | The mode. |
