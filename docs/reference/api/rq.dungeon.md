# rq.dungeon

`since 0.2.0`

Reads and changes the dungeon: the map, the player's place, objects on it, and the camera.

On a map grid, `x` runs east and `z` north.

## Functions

| Name | Summary |
| --- | --- |
| [`rq.dungeon.camera`](#rqdungeoncamera) | Patches the dungeon camera's zoom range, fog, view cut and slider in memory. |
| [`rq.dungeon.active`](#rqdungeonactive) | Returns whether the dungeon map screen exists. |
| [`rq.dungeon.exploring`](#rqdungeonexploring) | Returns whether the player walks the map. |
| [`rq.dungeon.info`](#rqdungeoninfo) | Returns a copy of the current room. |
| [`rq.dungeon.areas`](#rqdungeonareas) | Returns the current quest's area map, as the game draws it at the top right of the map screen. |
| [`rq.dungeon.grid`](#rqdungeongrid) | Returns the current map, as `rqmod-ctl grid` shows it. |
| [`rq.dungeon.place_player`](#rqdungeonplace_player) | Puts the player on a floor cell of the current map at once, as the game does after a portal. |
| [`rq.dungeon.place`](#rqdungeonplace) | Puts an object on a free floor cell of the current map. |

### rq.dungeon.camera

```lua
rq.dungeon.camera(opts) -> boolean
```

`since 0.2.0` `changed 2.30.0`

Patches the dungeon camera's zoom range, fog, view cut and slider in memory.

It can be called again, from `rq.dungeon.on_map` too: each call sets the range in place of the last
one, and a field left out takes its default again. A call in `on_map` holds for the map being built;
a call elsewhere holds from the next map the game builds.

The game keeps one zoom distance for every map (in its shared save) and clamps it to the range each
time a map opens, so after a map with a smaller `max` the camera starts nearer.

The 3D view is cut at `far` (the game's 200): with it, a `max` past about 120 shows black at the top
of an outdoor map, and past about 170 loses the far rows of ground. With `far` 400 the ground stays
whole at 180. What is left is the edge of the sky backdrop under outdoor maps, a plane of fixed size,
which shows as black corners in some areas. Caves have a black background.

Raises an error when `opts` is not a table, `far` is 5 or less, or the AIN is not loaded.

```lua
rq.dungeon.camera({ max = 120, fog_far = 160 })
rq.dungeon.on_map(function(ctx)
  local open = ctx.kind == rq.ids.map_kind.FIELD
  rq.dungeon.camera({ max = open and 150 or 120, far = open and 400 or 200 })
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `opts` | [`rq.DungeonCamera`](../types/rq.DungeonCamera.md) | The range; a field left out keeps its default. |

| Returns | Type | Description |
| --- | --- | --- |
| `ok` | `boolean` | false when the game lacks one of the camera functions (the log says which). |

> Changed in 2.30.0: Can be called again. It worked only once: a second call changed nothing but the wheel, whose step it multiplied a second time. New field `far`.

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

`since 0.2.0` `changed 2.24.0`

Returns a copy of the current room.

Outside a quest, `quest`, `area`, `row`, `col` and `kind` are 0 and `stratum` is nil.

| Returns | Type | Description |
| --- | --- | --- |
| `info` | [`rq.DungeonInfo`](../types/rq.DungeonInfo.md) | The room, the cell and the party. |

> Changed in 2.24.0: Added `quest`, `area`, `row`, `col`, `kind` and `stratum`.

### rq.dungeon.areas

```lua
rq.dungeon.areas() -> rq.DungeonArea[]|nil, boolean?
```

`since 2.24.0`

Returns the current quest's area map, as the game draws it at the top right of the map screen.

Areas and routes stay found across runs of the quest. Some quests hide the area map (the Malgrid
Dungeon Xth Stratum without its map item); the second value says so, and a mod that draws a map of
its own can respect it.

```lua
local list, shown = rq.dungeon.areas()
if list and shown then
  for _, a in ipairs(list) do
    if a.found then rq.log(a.row, a.col, a.here and "here" or "") end
  end
end
```

| Returns | Type | Description |
| --- | --- | --- |
| `areas` | [`rq.DungeonArea`](../types/rq.DungeonArea.md) `[]\|nil` | The 16 areas in order, or nil outside a quest. |
| `shown` | `boolean?` | false when the game hides its area map on this quest. |

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
| [`rq.dungeon.on_area`](#rqdungeonon_area) | Calls `fn` each time the party enters an area of a quest. |

### rq.dungeon.on_map

```lua
rq.dungeon.on_map(fn) -> fun()
```

`since 0.9.0` `changed 0.23.0` `changed 2.24.0`

Calls `fn` when the dungeon map screen is built.

On a first visit the game locks the camera at distance 35 until the quest is cleared. Return true
from any callback and the engine reports the quest as cleared for that one check, so the zoom stays
free. The range is whatever is patched at that moment (the game's, or `rq.dungeon.camera`).

The game builds the map screen each time the party enters an area, again when it rebuilds the map
after a save, and for the result screen's background. For "the party entered an area", once, use
`rq.dungeon.on_area`.

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

> Changed in 2.24.0: `ctx` has `area`, `row`, `col`, `name`, `kind`, `first` and `stratum`.

See also: [`rq.dungeon.on_area`](rq.dungeon.md#rqdungeonon_area)

### rq.dungeon.on_area

```lua
rq.dungeon.on_area(fn) -> fun()
```

`since 2.24.0`

Calls `fn` each time the party enters an area of a quest.

It runs once per area entered: at the quest's start, through a portal, and when the quest's own
script moves the party. It runs after the game's `ＱＭ登録`: the area's kind, name and map are set and
the map is loaded, but not shown yet. It does not run when the game builds the map screen again
(after a save, the result screen), as `rq.dungeon.on_map` does.

The game has no floor number. A quest's areas are cells of its 4 by 4 area map; names such as
"Epiphany Cave 2F" are the areas' names, and each stratum of the Malgrid Dungeon is its own quest.

What `fn` returns is ignored. Handlers run in the order they were added; an error in one is written
to the log with the mod's id, and the others still run.

Raises an error when `fn` is not a function.

```lua
rq.dungeon.on_area(function(ctx)
  if ctx.first and ctx.kind == rq.ids.map_kind.CAVE then
    rq.log("a new cave area: " .. ctx.name)
  end
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ctx:` [`rq.AreaCtx`](../types/rq.AreaCtx.md) `)` | Gets the area entered. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

See also: [`rq.dungeon.on_map`](rq.dungeon.md#rqdungeonon_map)
