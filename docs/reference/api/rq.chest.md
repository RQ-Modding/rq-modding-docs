# rq.chest

`since 0.2.0`

The chance of opening a red chest.

Green chests always open and are not touched. A red chest rolls the game's `成功確率` (30, which a
thief or Chest Opening can raise), and a fail explodes (12% damage) and loses the item. The engine
patches only that roll, so Lua can change the chance, for instance to add pity.

```lua
rq.chest.on_attempt(function(info)
  return math.min(100, info.base_pct + (rq.chest.get("pity") or 0))
end)
rq.chest.on_result(function(info)
  if info.success then rq.chest.set("pity", 0)
  else rq.chest.set("pity", (rq.chest.get("pity") or 0) + info.base_pct) end
end)
```

## Functions

| Name | Summary |
| --- | --- |
| [`rq.chest.install`](#rqchestinstall) | Patches the red chest's roll. |
| [`rq.chest.get`](#rqchestget) | Reads a number kept for this session, such as a pity count. |
| [`rq.chest.set`](#rqchestset) | Keeps a number for this session. |

### rq.chest.install

```lua
rq.chest.install() -> boolean
```

`since 0.2.0` `changed 2.35.0`

Patches the red chest's roll.

Not needed since 2.35.0: each call that needs it places it the first time, and raises this
call's error there when it cannot. Calling it still does no harm.

| Returns | Type | Description |
| --- | --- | --- |
| `ok` | `boolean` | true when the patch is in place. |

> Changed in 2.35.0: Not needed: `on_attempt` and `on_result` make it.

### rq.chest.get

```lua
rq.chest.get(key) -> integer|nil
```

`since 0.2.0`

Reads a number kept for this session, such as a pity count.

It is not in the save; use `rq.store` for that.

| Parameter | Type | Description |
| --- | --- | --- |
| `key` | `string` | The key. |

| Returns | Type | Description |
| --- | --- | --- |
| `value` | `integer\|nil` | The number, or nil when not set. |

### rq.chest.set

```lua
rq.chest.set(key, val)
```

`since 0.2.0`

Keeps a number for this session.

| Parameter | Type | Description |
| --- | --- | --- |
| `key` | `string` | The key. |
| `val` | `integer` | The number. |

## Events

| Name | Summary |
| --- | --- |
| [`rq.chest.on_attempt`](#rqcheston_attempt) | Calls `fn` just before a red chest rolls, to set the chance. |
| [`rq.chest.on_result`](#rqcheston_result) | Calls `fn` after a red chest rolled. |

### rq.chest.on_attempt

```lua
rq.chest.on_attempt(fn) -> fun()
```

`since 0.2.0` `changed 0.14.0` `changed 0.23.0` `changed 2.35.0`

Calls `fn` just before a red chest rolls, to set the chance.

Each callback sees the percent the one before left in `info.pct`; nil keeps it. With no callback the
chance is `info.base_pct`, not 100. The chance is written to `成功確率` and to the "(N% chance to
disarm)" line before that choice shows. Up to 16 callbacks. The first call patches the roll.

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(info:` [`rq.ChestInfo`](../types/rq.ChestInfo.md) `): integer\|` [`rq.ChestAttemptResult`](../types/rq.ChestAttemptResult.md) `\|nil` | Returns the percent. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

> Changed in 0.14.0: Every mod's callback runs; added `info.pct`.

> Changed in 0.23.0: Returns a remover.

> Changed in 2.35.0: Patches the roll itself; before, it needed `rq.chest.install`.

### rq.chest.on_result

```lua
rq.chest.on_result(fn) -> fun()
```

`since 0.2.0` `changed 0.14.0` `changed 0.23.0` `changed 2.35.0`

Calls `fn` after a red chest rolled.

Up to 16 callbacks. The first call patches the roll.

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(info:` [`rq.ChestInfo`](../types/rq.ChestInfo.md) `)` | Gets the chest and the roll. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

> Changed in 0.14.0: Every mod's callback runs.

> Changed in 0.23.0: Returns a remover.

> Changed in 2.35.0: Patches the roll itself; before, it needed `rq.chest.install`.
