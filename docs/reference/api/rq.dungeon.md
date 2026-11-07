# rq.dungeon

`since 0.2.0`

Reads and changes the dungeon: the map, the player's place, objects on it, and the camera.

On a map grid, `x` runs east and `z` north.

## Functions

| Name | Summary |
| --- | --- |
| [`rq.dungeon.camera`](#rqdungeoncamera) | Patches the dungeon camera's zoom range, fog and slider in memory. |
| [`rq.dungeon.active`](#rqdungeonactive) | Returns whether the dungeon map screen exists. |
| [`rq.dungeon.exploring`](#rqdungeonexploring) | Returns whether the player walks the map. |
| [`rq.dungeon.info`](#rqdungeoninfo) | Returns a copy of the current room. |
| [`rq.dungeon.grid`](#rqdungeongrid) | Returns the current map, as `rqmod-ctl grid` shows it. |
| [`rq.dungeon.place_player`](#rqdungeonplace_player) | Puts the player on a floor cell of the current map at once, as the game does after a portal. |
| [`rq.dungeon.place`](#rqdungeonplace) | Puts an object on a free floor cell of the current map. |

### rq.dungeon.camera

```lua
rq.dungeon.camera(opts) -> boolean
```

`since 0.2.0`

Patches the dungeon camera's zoom range, fog and slider in memory.

Raises an error when `opts` is not a table or the AIN is not loaded.

```lua
rq.dungeon.camera({ max = 160, fog_far = 220 })
```

| Parameter | Type | Description |
| --- | --- | --- |
| `opts` | [`rq.DungeonCamera`](../types/rq.DungeonCamera.md) | The range; a field left out keeps its default. |

| Returns | Type | Description |
| --- | --- | --- |
| `ok` | `boolean` | false when the game lacks one of the camera functions (the log says which). |

### rq.dungeon.active

```lua
rq.dungeon.active() -> boolean
```

`since 0.2.0`

Returns whether the dungeon map screen exists.

It is true between `T_MapParts@create` and `@delete`, so also in a fight, a scene or a menu on the
map. For "the player walks the map", use `rq.dungeon.exploring`.

| Returns | Type | Description |
| --- | --- | --- |
| `active` | `boolean` | true while the map screen exists. |

### rq.dungeon.exploring

```lua
rq.dungeon.exploring() -> boolean
```

`since 0.2.0`

Returns whether the player walks the map.

False when the map is hidden or suspended (a join dialog), and during a fight, a character profile,
Config, the result and appraisal screens, and a scene or choice on the map.

| Returns | Type | Description |
| --- | --- | --- |
| `exploring` | `boolean` | true while the player can walk. |

### rq.dungeon.info

```lua
rq.dungeon.info() -> rq.DungeonInfo
```

`since 0.2.0`

Returns a copy of the current room.

| Returns | Type | Description |
| --- | --- | --- |
| `info` | [`rq.DungeonInfo`](../types/rq.DungeonInfo.md) | The room, the cell and the party. |

### rq.dungeon.grid

```lua
rq.dungeon.grid(opts) -> table|nil, string?
```

`since 0.25.0` `changed 1.5.0`

Returns the current map, as `rqmod-ctl grid` shows it.

The table holds `player` `{x, z}`, `mapNo`, `room` `{minX, minZ, maxX, maxZ, no, whole}`, `rows`
(text, north to south), `legend`, `axes` and `events`, each `{x, z, kind, tt, tz, tv, reach}`. By
default it holds only what the player reaches over plain floor, so a trap, chest or fight across a
corridor hides the rest of the room; `opts.whole` holds every cell, with floor the player cannot
reach shown as `:`. `room.no` is the game's room number (`◆ＢＭＡＰ`). After a portal, `room.no`
changes a moment before the map: wait for `mapNo` to change before reading the new room.

| Parameter | Type | Description |
| --- | --- | --- |
| `opts` *(optional)* | `{whole?: boolean}` | `whole`: every cell of the map. Default false. |

| Returns | Type | Description |
| --- | --- | --- |
| `grid` | `table\|nil` | The map, or nil when not on a map. |
| `reason` | `string?` | Why there is no map. |

> Changed in 1.5.0: Added `opts.whole`, `reach`, `room.no` and `room.whole`.

### rq.dungeon.place_player

```lua
rq.dungeon.place_player(x, z, opts) -> boolean
```

`since 1.5.0`

Puts the player on a floor cell of the current map at once, as the game does after a portal.

Any floor cell works, also one the player cannot walk to. `grid().player` shows the new cell after
the game's next update. Nothing on the cell opens: walk onto it for that.

Raises an error for a cell that is not floor or not whole numbers, an unknown face, or when not on a
map.

| Parameter | Type | Description |
| --- | --- | --- |
| `x` | `integer` | The cell, east. |
| `z` | `integer` | The cell, north. |
| `opts` *(optional)* | `{face?: "north"\|"east"\|"south"\|"west"}` | `face`: where the player looks. Default "south". |

| Returns | Type | Description |
| --- | --- | --- |
| `placed` | `boolean` | true. |

### rq.dungeon.place

```lua
rq.dungeon.place(kind, x, z, opts) -> boolean
```

`since 0.25.0`

Puts an object on a free floor cell of the current map.

Walking onto it works as for the game's own. The game leaves a used "exp" in `grid().events`.

Raises an error for an unknown kind, a cell that is not free floor, or when not on a map.

```lua
local g = rq.dungeon.grid()
if g then rq.dungeon.place("chest", g.player.x + 1, g.player.z, { content = 120 }) end
```

| Parameter | Type | Description |
| --- | --- | --- |
| `kind` | `"chest"\|"red-chest"\|"spring"\|"achievement"\|"exp"\|"gold"` | The object. |
| `x` | `integer` | The cell, east. |
| `z` | `integer` | The cell, north. |
| `opts` *(optional)* | `{content?: integer, rank?: integer}` | For a chest: `content`, a fixed item number; `rank`, its rank. |

| Returns | Type | Description |
| --- | --- | --- |
| `placed` | `boolean` | true when the object was put down. |

## Events

| Name | Summary |
| --- | --- |
| [`rq.dungeon.on_map`](#rqdungeonon_map) | Calls `fn` when the dungeon map screen is built. |

### rq.dungeon.on_map

```lua
rq.dungeon.on_map(fn) -> fun()
```

`since 0.9.0` `changed 0.23.0`

Calls `fn` when the dungeon map screen is built.

On a first visit the game locks the camera at distance 35 until the quest is cleared. Return true
from any callback and the engine reports the quest as cleared for that one check, so the zoom stays
free. The range is whatever is patched at that moment (the game's, or `rq.dungeon.camera`).

```lua
rq.dungeon.on_map(function(ctx)
  return ctx.quest == 126  -- free zoom on quest 126, also the first time
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ctx:` [`rq.MapCtx`](../types/rq.MapCtx.md) `): boolean\|nil` | Returns true to free the zoom. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

> Changed in 0.23.0: Returns a remover.
