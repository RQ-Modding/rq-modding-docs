# rq.counter

`since 0.2.0`

Lets the Counter skill (259) work after Ally Guard.

The game sets the Counter rate to 0 inside `ダメージ後計算` when Ally Guard redirected the hit
(`FA[77]`). `rq.counter.install` patches only that place; the other effects of `FA[77]` and the
other Counter checks stay as the game has them. Lua decides with `on_guard_counter`.

```lua
rq.counter.install()
rq.counter.on_guard_counter(function(ctx)
  return ctx.guarded == true
end)
```

## Functions

| Name | Summary |
| --- | --- |
| [`rq.counter.install`](#rqcounterinstall) | Installs the patch `on_guard_counter` needs. |

### rq.counter.install

```lua
rq.counter.install() -> boolean
```

`since 0.2.0`

Installs the patch `on_guard_counter` needs.

Raises an error when the AIN is not loaded or the patch cannot be placed.

| Returns | Type | Description |
| --- | --- | --- |
| `ok` | `boolean` | Always true; a failure raises an error. |

## Events

| Name | Summary |
| --- | --- |
| [`rq.counter.on_guard_counter`](#rqcounteron_guard_counter) | Calls `fn` when the game would clear the Counter rate after Ally Guard. |

### rq.counter.on_guard_counter

```lua
rq.counter.on_guard_counter(fn) -> fun()
```

`since 0.2.0` `changed 0.14.0` `changed 0.23.0`

Calls `fn` when the game would clear the Counter rate after Ally Guard.

One callback returning true keeps the rate. With no callback, the game's rule stays. Up to 16
callbacks in all.

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ctx:` [`rq.CounterGuardCtx`](../types/rq.CounterGuardCtx.md) `): boolean\|nil` | Returns true to keep the Counter rate. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

> Changed in 0.14.0: Every mod's callback runs, and one true keeps the rate (before, the last one won).

> Changed in 0.23.0: Returns a remover.
