# rq.BattleTurnCtx

`since 2.1.0`

What `rq.battle.on_turn` gets: the character whose turn starts, and what can change it.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The character's roster slot. |
| `unit` | `integer` | Its battle number: 1 to 5 allies, 11 to 15 enemies. |
| `side` | `"ally"\|"enemy"\|"summon"` | Whose turn it is. |
| `turn` | `integer` | The fight's action count (`◆戦闘ターン`), which every actor's turn raises. |
| `passing` | `boolean` | true when this turn passes: the turn a stun ends, or after `ctx:skip()`. |
| `downed` | `boolean` | true once a lethal `ctx:damage` brought the HP to 0 in this turn start. Since 2.3.0. |

## Functions

| Name | Summary |
| --- | --- |
| [`rq.BattleTurnCtx:damage`](#rqbattleturnctxdamage) | Takes HP at this turn start and shows it as the game's damage number. |
| [`rq.BattleTurnCtx:heal`](#rqbattleturnctxheal) | Gives HP at this turn start, with the game's regeneration effect and number. |
| [`rq.BattleTurnCtx:skip`](#rqbattleturnctxskip) | Makes this turn pass, as a stun does: the character uses no skill. |
| [`rq.BattleTurnCtx:log`](#rqbattleturnctxlog) | Adds text to the battle log line of this turn start. |

### rq.BattleTurnCtx:damage

```lua
rq.BattleTurnCtx:damage(n, opts) -> integer
```

`since 2.1.0` `changed 2.3.0` `changed 2.26.0`

Takes HP at this turn start and shows it as the game's damage number.

The HP stops at 1, as with the game's poison, unless `opts.lethal` is true. Damage from several
callbacks and the game's poison shows as one number; with `opts.apart`, as a number of its own
after it, in the order the calls came. In an `rq.status` state's `on_turn`, `apart` is on.

**Lethal.** With `lethal`, the HP may reach 0. Then the character goes down, as the game shows
a death: the enemy fades or the ally's card turns red, and `rq.battle.on_down` runs. The turn
passes (`ctx.downed` and `ctx.passing` are true), and later `ctx:damage` and `ctx:heal` calls in
this turn start do nothing. The dying character's skills that act at a death run: Hanny Zippo
brings it back at full HP once a fight, and Rich Enemy (438) doubles the gold. Kalar's curse
needs a killer: with a `source` that is in the fight and not down, the game's own death
handling (`死亡計算`) runs with that killer. When the action ends, the game checks for the end
of the fight, as after an attack: the last enemy's death wins it and the last ally's loses it.
A familiar never goes down this way, and shows no number: its damage stops at 1 HP.

**Persevere.** With `opts.persevere`, a lethal damage that would take the last HP meets Persevere
as a hit does: skill 481 always leaves 1 HP, skill 247 does half the time, once a fight (the same
once as for hits), and the log line gets " (Persevere activated)". It is off by default, and on in
a state's `on_turn` unless the definition says `persevere = false`.

Raises an error for a number that is not whole or is below 0, or an option of the wrong type.

```lua
rq.battle.on_turn(function(ctx)
  if doomed[ctx.iic] then
    ctx:damage(999999, { lethal = true, source = doomed[ctx.iic] })
    ctx:log(" " .. rq.chara.get(ctx.iic).short .. "'s time is up.")
  end
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `n` | `integer` | The HP to take, 0 or more. |
| `opts` *(optional)* | `{lethal?: boolean, source?: integer, apart?: boolean, persevere?: boolean}` | `lethal`: may bring the HP to 0, default false (in an `rq.status` state's `on_turn`, the definition's `lethal`). `source`: the killer's roster slot, default 0 (in a state's `on_turn`, the state's `source`). `apart`: its own number, default false (true in a state's `on_turn`). `persevere`: Persevere may save from a lethal damage, default false (in a state's `on_turn`, the definition's `persevere`). |

| Returns | Type | Description |
| --- | --- | --- |
| `taken` | `integer` | The HP taken, after the 1 HP floor when not lethal. |

> Changed in 2.3.0: `opts`, with `lethal` and `source`.

> Changed in 2.26.0: `apart` and `persevere`.

### rq.BattleTurnCtx:heal

```lua
rq.BattleTurnCtx:heal(n, opts) -> integer
```

`since 2.1.0` `changed 2.26.0`

Gives HP at this turn start, with the game's regeneration effect and number.

The HP stops at the most HP. A downed character gets nothing, nor one a lethal `ctx:damage`
downed in this turn start. Healing from several callbacks and the game's regeneration shows as
one number; with `opts.apart`, as a number of its own after it.

Raises an error for a number that is not whole or is below 0, or an option of the wrong type.

| Parameter | Type | Description |
| --- | --- | --- |
| `n` | `integer` | The HP to give, 0 or more. |
| `opts` *(optional)* | `{apart?: boolean}` | `apart`: its own number, default false (true in an `rq.status` state's `on_turn`). |

| Returns | Type | Description |
| --- | --- | --- |
| `healed` | `integer` | The HP given, after the cap. |

> Changed in 2.26.0: `opts.apart`.

### rq.BattleTurnCtx:skip

```lua
rq.BattleTurnCtx:skip()
```

`since 2.1.0`

Makes this turn pass, as a stun does: the character uses no skill.

### rq.BattleTurnCtx:log

```lua
rq.BattleTurnCtx:log(text)
```

`since 2.1.0`

Adds text to the battle log line of this turn start.

The line is empty on most turns, so write a whole sentence, starting with a space as the game's
lines do. Text from several callbacks goes on one line, in the order they ran.

Raises an error for a value that is not a string.

| Parameter | Type | Description |
| --- | --- | --- |
| `text` | `string` | The text to add. |

## Used by

[`rq.StatusDef`](rq.StatusDef.md), [`rq.battle.on_turn`](../api/rq.battle.md#rqbattleon_turn)
