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
| [`rq.dungeon.objects`](#rqdungeonobjects) | Lists the objects on the current map. |
| [`rq.dungeon.remove`](#rqdungeonremove) | Removes the object on a cell of the current map. |
| [`rq.dungeon.looks`](#rqdungeonlooks) | Lists the looks a mod's object can have: the game's props, by name. |
| [`rq.dungeon.traps`](#rqdungeontraps) | Returns the trap kinds' weights in the current area. |
| [`rq.dungeon.set_traps`](#rqdungeonset_traps) | Sets the trap kinds' weights in the current area. |

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

`since 0.25.0` `changed 2.39.0`

Puts an object on a free floor cell of the current map.

Walking onto it works as for the game's own: `trap` is the game's trap (its kind drawn from the
area's weights, `rq.dungeon.traps`), `enemy` a placed enemy (the game picks the fight when it is
touched, and a fight won counts for the placed-enemy bonus; as with the game's own, the touch may
be one of the quest's meetings, such as the adventurers, once a quest), `escape` the escape
device. The game leaves a
used "exp" in `grid().events`.

`custom` puts a mod's own object: a silent map event whose number the loader makes from `opts.id`,
shown with one of the game's props (`opts.look`, `rq.dungeon.looks()`). A step on it runs the
function `rq.dungeon.on_object` registered for that id. It is used once, as the game's events, unless
`opts.keep` is true. It stays for the whole quest, area by area, and in a save made in the quest.

Raises an error for an unknown kind or look, `opts` that is not a table, an id that is not a text of
1 to 64 bytes or that has the number of another id, a cell that is not free floor, or when not on a
map.

```lua
local g = rq.dungeon.grid()
if g then rq.dungeon.place("chest", g.player.x + 1, g.player.z, { content = 120 }) end
```

| Parameter | Type | Description |
| --- | --- | --- |
| `kind` | `"chest"\|"red-chest"\|"spring"\|"achievement"\|"exp"\|"gold"\|"trap"\|"enemy"\|"escape"\|"custom"` | The object. |
| `x` | `integer` | The cell, east. |
| `z` | `integer` | The cell, north. |
| `opts` *(optional)* | `{content?: integer, rank?: integer, id?: string, look?: string, keep?: boolean}` | For a chest: `content`, a fixed item number; `rank`, its rank. For `custom`: `id`, the object's id, such as `"mymod:altar"`; `look`, a name from `rq.dungeon.looks()`, default "event"; `keep`, true to put it back after each step, default false. |

| Returns | Type | Description |
| --- | --- | --- |
| `placed` | `boolean` | true when the object was put down. |

> Changed in 2.39.0: The kinds `trap`, `enemy`, `escape` and `custom`, and `opts.id`, `look` and `keep`.

### rq.dungeon.objects

```lua
rq.dungeon.objects() -> rq.MapObject[]|nil
```

`since 2.39.0`

Lists the objects on the current map.

Every object of the area, also those the player cannot reach yet, north to south, then west to
east.

```lua
for _, o in ipairs(rq.dungeon.objects() or {}) do
  if o.kind == "trap" then rq.dungeon.remove(o.x, o.z) end
end
```

| Returns | Type | Description |
| --- | --- | --- |
| `objects` | [`rq.MapObject`](../types/rq.MapObject.md) `[]\|nil` | nil when not on a map. |

### rq.dungeon.remove

```lua
rq.dungeon.remove(x, z) -> boolean
```

`since 2.39.0`

Removes the object on a cell of the current map.

The object and its prop go at once, as when the game takes away a used one, for the rest of the
quest. A warp cannot be removed: the map would lose its way on.

Raises an error for a cell that is not whole numbers or is off the map, a warp, or when not on a
map.

| Parameter | Type | Description |
| --- | --- | --- |
| `x` | `integer` | The cell, east. |
| `z` | `integer` | The cell, north. |

| Returns | Type | Description |
| --- | --- | --- |
| `removed` | `boolean` | false when the cell has no object. |

### rq.dungeon.looks

```lua
rq.dungeon.looks() -> string[]
```

`since 2.39.0`

Lists the looks a mod's object can have: the game's props, by name.

`chest` (a green chest), `red-chest`, `spring` (blue rings), `achievement` (a yellow flower),
`exp` (a cyan die), `gold` (a coin), `trap` (dark dots on the floor), `enemy` and `enemy-2` (a red
star), `escape` (a green frame), `warp` and `warp-2` (a purple frame), `event` and `event-2` (a
green star with a yellow "!"), `event-3` (a green star), `event-4` (a red star with a "!") and
`hidden` (the game's silent event, which shows nothing). The look is only what is drawn: a step on
the cell runs the object's function whatever its look, also for the props the game would
otherwise take itself (spring, achievement, EXP, gold).

| Returns | Type | Description |
| --- | --- | --- |
| `looks` | `string[]` | The names, sorted. |

### rq.dungeon.traps

```lua
rq.dungeon.traps() -> rq.TrapWeights|nil
```

`since 2.39.0`

Returns the trap kinds' weights in the current area.

A trap stepped on draws its kind with these weights. The area's script sets them when the party
enters it. With all four at 0, every trap is an electric current.

| Returns | Type | Description |
| --- | --- | --- |
| `weights` | [`rq.TrapWeights`](../types/rq.TrapWeights.md) `\|nil` | nil outside a quest. |

### rq.dungeon.set_traps

```lua
rq.dungeon.set_traps(weights)
```

`since 2.39.0`

Sets the trap kinds' weights in the current area.

The area's script writes them again when the party enters an area, so set them from
`rq.dungeon.on_area` to keep them.

Raises an error outside a quest, for an unknown kind, or a weight that is not 0 to 10.

```lua
rq.dungeon.on_area(function() rq.dungeon.set_traps({ shroom = 0, pit = 0 }) end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `weights` | `{shroom?: integer, shock?: integer, alarm?: integer, pit?: integer}` | The weights to change, 0 to 10; one left out stays. |

## Events

| Name | Summary |
| --- | --- |
| [`rq.dungeon.on_map`](#rqdungeonon_map) | Calls `fn` when the dungeon map screen is built. |
| [`rq.dungeon.on_area`](#rqdungeonon_area) | Calls `fn` each time the party enters an area of a quest. |
| [`rq.dungeon.on_object`](#rqdungeonon_object) | Registers the function that runs when the party steps on a mod's own object. |
| [`rq.dungeon.on_trap`](#rqdungeonon_trap) | Registers a function that runs when the party steps on a trap. |

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

### rq.dungeon.on_object

```lua
rq.dungeon.on_object(id, fn) -> fun()
```

`since 2.39.0`

Registers the function that runs when the party steps on a mod's own object.

It runs in place of the quest's own handling of a map event. What it returns ends the quest or not:
nil or 0 go on, 1 clears the quest, 4 ends it as the escape device does (the items kept), 2 and 3
as a defeat and a give-up. The object is taken off its cell before the function runs, as the game
does with its events; with `ctx.keep` it is put back after. The function may wait as a quest moment
does: `rq.ui.confirm`, `rq.ui.notice`, `rq.battle.start`. `rq.quests.on_event` does not see these
events.

One function per id: calling again replaces it. An object whose id has no function logs a line and
does nothing. Register at a mod's top level, so the objects in a save made in a quest answer after
a load.

Raises an error for an id that is not a text of 1 to 64 bytes or that has the number of another
id, or a value that is not a function.

```lua
rq.dungeon.on_object("mymod:altar", function(ctx)
  if rq.ui.confirm("Touch the altar?") then
    local r = rq.battle.start({ enemies = { 0, rq.ids.monster.COCKROACH, 0 }, boss = true })
    if r ~= "won" then ctx.keep = true end
  else
    ctx.keep = true
  end
end)
rq.dungeon.on_area(function(ctx)
  if ctx.quest == 126 and ctx.area == 1 and ctx.first then
    local g = rq.dungeon.grid()
    rq.dungeon.place("custom", g.player.x + 2, g.player.z, { id = "mymod:altar", look = "spring" })
  end
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `string` | The object's id, 1 to 64 bytes, such as `"mymod:altar"`. |
| `fn` | `fun(ctx:` [`rq.ObjectCtx`](../types/rq.ObjectCtx.md) `): integer\|nil` | Returns nil to go on, or how the quest ends. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this function. |

See also: [`rq.dungeon.place`](rq.dungeon.md#rqdungeonplace)

### rq.dungeon.on_trap

```lua
rq.dungeon.on_trap(fn) -> fun()
```

`since 2.39.0`

Registers a function that runs when the party steps on a trap.

It runs after the game drew the trap's kind and before the scene. Callbacks run in load order,
each seeing what the one before left; a value that is not allowed is logged and the one before kept.
A changed chance is rolled with the game's roll; the scene's line still names the game's chance
(20%, 50% or Trap Evasion). Sloth shrooms with one member are always avoided, as in the game. The
trap is gone after, avoided or not. It runs for the game's traps and for those of
`rq.dungeon.place("trap", ...)`.

Raises an error when `fn` is not a function.

```lua
rq.dungeon.on_trap(function(ctx)
  if ctx.kind == "pit" then ctx.kind = "alarm" end
  ctx.chance = math.max(0, ctx.chance - 10)
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ctx:` [`rq.TrapCtx`](../types/rq.TrapCtx.md) `)` | Changes the trap. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |
