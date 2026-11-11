# rq.encounters

`since 2.33.0`

Random fights on a quest's map.

On a map, each step fills the encounter bar; when it is full, each further step has a 1 in 10
chance of a fight with one of the area's groups. `steps` is how many steps fill the bar: the game
picks it again after each fight and each area change (from 10 to 60, by the area and the party).
An area with no groups has no bar and no random fights. An enemy standing on the map is a fight
too, and `rq.encounters.on_encounter` sees it with `placed` true.

```lua
--- Twice as many steps between fights
rq.encounters.on_steps(function(ctx) return ctx.steps * 2 end)
```

## Functions

| Name | Summary |
| --- | --- |
| [`rq.encounters.info`](#rqencountersinfo) | Returns the random fights of the area the party is in. |
| [`rq.encounters.hold`](#rqencountershold) | Holds random fights off for this mod, or lets them come back. |
| [`rq.encounters.set_steps`](#rqencountersset_steps) | Sets the steps that fill the encounter bar, from now to the next fight or area change. |

### rq.encounters.info

```lua
rq.encounters.info() -> rq.EncounterInfo|nil
```

`since 2.33.0`

Returns the random fights of the area the party is in.

```lua
local e = rq.encounters.info()
if e and e.on then rq.hud.text(10, 10, ("%d / %d"):format(e.walked, e.steps)) end
```

| Returns | Type | Description |
| --- | --- | --- |
| `info` | [`rq.EncounterInfo`](../types/rq.EncounterInfo.md) `\|nil` | nil away from a quest's map. |

### rq.encounters.hold

```lua
rq.encounters.hold(on)
```

`since 2.33.0`

Holds random fights off for this mod, or lets them come back.

While any mod holds them, no random fight starts, the encounter bar is hidden and the steps walked
do not fill it: it keeps its place for when fights come back. Each mod has its own hold, so one mod's `false` does not end another's. An enemy standing on
the map still fights. It may be called at the top level of a mod, and lasts until the game closes:
a load or the title does not end it.

```lua
rq.encounters.hold(true)   -- a peaceful walk
rq.encounters.hold(false)  -- fights again
```

| Parameter | Type | Description |
| --- | --- | --- |
| `on` | `boolean` | true to hold random fights off. |

### rq.encounters.set_steps

```lua
rq.encounters.set_steps(n)
```

`since 2.33.0`

Sets the steps that fill the encounter bar, from now to the next fight or area change.

The game picks the steps again after each fight and each area change: to keep a value, return it
from `rq.encounters.on_steps` instead.

Raises an error for a value that is not a whole number from 1 to 999, and at the top level of a
mod.

| Parameter | Type | Description |
| --- | --- | --- |
| `n` | `integer` | The steps, 1 to 999. |

## Events

| Name | Summary |
| --- | --- |
| [`rq.encounters.on_steps`](#rqencounterson_steps) | Calls `fn` each time the game picks the steps that fill the encounter bar. |
| [`rq.encounters.on_encounter`](#rqencounterson_encounter) | Calls `fn` when a fight from the map is about to start, and can cancel it. |

### rq.encounters.on_steps

```lua
rq.encounters.on_steps(fn) -> fun()
```

`since 2.33.0`

Calls `fn` each time the game picks the steps that fill the encounter bar.

A number returned becomes the steps (rounded down, kept from 1 to 999), and the next callback sees
it in `ctx.steps`. nil keeps them. An error is logged once for each new error text.

```lua
rq.encounters.on_steps(function(ctx)
  if ctx.area_change then return ctx.steps + 20 end
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ctx:` [`rq.StepsCtx`](../types/rq.StepsCtx.md) `): integer\|nil` | Returns the steps, or nil. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

### rq.encounters.on_encounter

```lua
rq.encounters.on_encounter(fn) -> fun()
```

`since 2.33.0`

Calls `fn` when a fight from the map is about to start, and can cancel it.

If any callback returns false, no fight starts and the party walks on, as when the player ignores
the group of adventurers the game offers. For a random fight the bar starts again from 0, and the
steps that fill it stay as they were: the game picks them again only after a fight. Every callback
runs, even after one returned false. An error is logged once for each new error text.

```lua
--- Every other random fight never starts
local skip = false
rq.encounters.on_encounter(function(ctx)
  if ctx.placed then return end
  skip = not skip
  if skip then return false end
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ctx:` [`rq.EncounterCtx`](../types/rq.EncounterCtx.md) `): boolean\|nil` | Returns false to cancel the fight. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |
