# rq.combat

`since 0.2.0`

Changes physical damage, accuracy and criticals.

Physical attacks keep the game's own path: defense, variance, cap, then the usual multipliers. Lua
can replace the attack before defense, scale the final damage, add to the hit chance at the same
place as the game's own -5 and -10 for some skills, and force or deny a critical. The callbacks
hold up to 16 each, and the first one places the hooks (`rq.combat.install`, needed before 2.35.0).

They also run when the game works out the battle forecast, so the forecast shows what they
change; `ctx.forecast` is then true (since 2.26.0), and a callback that counts hits or rolls dice
should do nothing.

```lua
rq.combat.on_physical(function(ctx)
  if ctx.race == 8 then return nil, 50 end  -- half damage to a hanny
end)
```

## Functions

| Name | Summary |
| --- | --- |
| [`rq.combat.install`](#rqcombatinstall) | Installs the hooks the combat callbacks need. |

### rq.combat.install

```lua
rq.combat.install() -> boolean
```

`since 0.2.0` `changed 2.35.0`

Installs the hooks the combat callbacks need.

It is the same call as `rq.chara.install`; calling either again does nothing more.

Not needed since 2.35.0: each call that needs it places it the first time, and raises this
call's error there when it cannot. Calling it still does no harm.

Raises an error when the AIN is not loaded or a hook cannot be placed.

| Returns | Type | Description |
| --- | --- | --- |
| `ok` | `boolean` | Always true; a failure raises an error. |

> Changed in 2.35.0: Not needed: the callbacks make it.

## Events

| Name | Summary |
| --- | --- |
| [`rq.combat.on_physical`](#rqcombaton_physical) | Calls `fn` for each physical hit, to change the attack and the final damage. |
| [`rq.combat.on_accuracy`](#rqcombaton_accuracy) | Calls `fn` for each accuracy check, to add to the hit chance. |
| [`rq.combat.on_crit`](#rqcombaton_crit) | Calls `fn` where the game rolls a critical (the `確率演算` call in `クリティカル計算`). |
| [`rq.combat.on_magic`](#rqcombaton_magic) | Calls `fn` for each magic hit, to change its final damage by a percent. |

### rq.combat.on_physical

```lua
rq.combat.on_physical(fn) -> fun()
```

`since 0.2.0` `changed 0.13.0` `changed 0.23.0`

Calls `fn` for each physical hit, to change the attack and the final damage.

`fn` returns nothing to keep the game's numbers, a new attack before defense, or an attack (nil
keeps it) and a percent of the final damage, applied after `最終ダメージ計算` (100 is unchanged, 50
half). Each callback sees the attack the one before left, and the percents multiply.

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ctx:` [`rq.PhysicalCtx`](../types/rq.PhysicalCtx.md) `): integer\|nil,` | integer\|nil Returns the attack, then the percent. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

> Changed in 0.13.0: Every mod's callback runs (before, the last one won).

> Changed in 0.23.0: Returns a remover.

### rq.combat.on_accuracy

```lua
rq.combat.on_accuracy(fn) -> fun()
```

`since 0.2.0` `changed 0.13.0` `changed 0.23.0`

Calls `fn` for each accuracy check, to add to the hit chance.

The returned numbers of every callback add up; nil counts as 0. The game's own limits come after
them: the chance is at most 100; an ally's attack hits at least 20% of the time; an enemy's at
least 40% (20% or 60% by the target's class, more after the target dodged several times in a
row) and at most 80% to 100% by the target's evasion.

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ctx:` [`rq.AccuracyCtx`](../types/rq.AccuracyCtx.md) `): integer\|nil` | Returns points to add to the hit chance; negative lowers it. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

> Changed in 0.13.0: Every mod's callback runs and the numbers add up (before, the last one won).

> Changed in 0.23.0: Returns a remover.

### rq.combat.on_crit

```lua
rq.combat.on_crit(fn) -> fun()
```

`since 0.12.0` `changed 0.13.0` `changed 0.23.0`

Calls `fn` where the game rolls a critical (the `確率演算` call in `クリティカル計算`).

Return true to force the critical, false to deny it, nil to roll as the game does. The first
callback that returns a boolean decides. A forced critical still adds the game's +30 to the damage
multiplier, and it also happens for skills whose multiplier is above 150, which never roll one in
the game.

```lua
rq.combat.on_crit(function(ctx)
  if ctx.defender_type == 22 then return true end  -- humanoids always take a critical
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ctx:` [`rq.CritCtx`](../types/rq.CritCtx.md) `): boolean\|nil` | Returns true, false, or nil to roll. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

> Changed in 0.13.0: Every mod's callback runs until one decides.

> Changed in 0.23.0: Returns a remover.

### rq.combat.on_magic

```lua
rq.combat.on_magic(fn) -> fun()
```

`since 2.1.0` `changed 2.26.0`

Calls `fn` for each magic hit, to change its final damage by a percent.

`fn` returns a percent of the final damage (100 is unchanged, 50 half, 0 none) or nil to keep it.
The percents of every callback multiply, and the damage is rounded down. It runs after the game's
last damage step (`最終ダメージ計算`), so the barrier, immunities and the game's magic resistance
are already in `damage`; a spell that does 0 is not reported. It also runs for the battle
forecast, with `ctx.forecast` true, so the forecast's damage word shows the percent. It is the
magic twin of the final percent of `rq.combat.on_physical`.

Raises an error, logged, for a return that is not a whole number of 0 or more.

```lua
rq.combat.on_magic(function(ctx)
  if weakened[ctx.attacker] then return 70 end  -- a weakened caster does 70%
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ctx:` [`rq.MagicCtx`](../types/rq.MagicCtx.md) `): integer\|nil` | Returns the percent, or nil. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

> Changed in 2.26.0: Runs for the battle forecast too, with `ctx.forecast`.

See also: [`rq.combat.on_physical`](rq.combat.md#rqcombaton_physical)
