# rq.random

`since 0.22.0`

Controls the random number generator the game and the loader share.

Every roll of the game and of the loader, such as opening a chest or `rq.item` loot, comes from
this one generator. To force the result of one kind of check, a hook is more exact: see
`rq.battle.force_hit`.

## Functions

| Name | Summary |
| --- | --- |
| [`rq.random.seed`](#rqrandomseed) | Starts the generator from a seed. |
| [`rq.random.fix`](#rqrandomfix) | Makes every roll give the same value, or goes back to random rolls. |

### rq.random.seed

```lua
rq.random.seed(n)
```

`since 0.22.0`

Starts the generator from a seed.

The same seed gives the same numbers, but a fight does not replay the same way, because effects
on screen draw from the same generator.

| Parameter | Type | Description |
| --- | --- | --- |
| `n` | `integer` | The seed. |

See also: [`rq.random.fix`](rq.random.md#rqrandomfix)

### rq.random.fix

```lua
rq.random.fix(value)
```

`since 0.22.0`

Makes every roll give the same value, or goes back to random rolls.

The game rolls with `RAND(n)`, which becomes `value % n + 1`: `fix(0)` makes every roll 1 and
`fix(99)` makes `RAND(100)` give 100. It is blunt: `fix(0)` also fires every check written as
`RAND(5) == 1`, good or bad, so it does not guarantee a hit. Use it only for a short time; a
check that rolls until it gets a new number would never end.

```lua
rq.random.fix(0)    -- every roll is 1 for now
rq.random.fix(nil)  -- random again
```

| Parameter | Type | Description |
| --- | --- | --- |
| `value` | `integer\|nil` | The value every roll uses, or nil for random rolls. |

See also: [`rq.battle.force_hit`](rq.battle.md#rqbattleforce_hit)
