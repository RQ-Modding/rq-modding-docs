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

## Functions

| Name | Summary |
| --- | --- |
| [`rq.BattleTurnCtx:damage`](#rqbattleturnctxdamage) | Takes HP at this turn start and shows it as the game's damage number. |
| [`rq.BattleTurnCtx:heal`](#rqbattleturnctxheal) | Gives HP at this turn start, with the game's regeneration effect and number. |
| [`rq.BattleTurnCtx:skip`](#rqbattleturnctxskip) | Makes this turn pass, as a stun does: the character uses no skill. |
| [`rq.BattleTurnCtx:log`](#rqbattleturnctxlog) | Adds text to the battle log line of this turn start. |

### rq.BattleTurnCtx:damage

```lua
rq.BattleTurnCtx:damage(n) -> integer
```

`since 2.1.0`

Takes HP at this turn start and shows it as the game's damage number.

The HP stops at 1, as with the game's poison, so this never downs anyone. Damage from several
callbacks, and the game's poison, show as one number.

Raises an error for a number that is not whole or is below 0.

| Parameter | Type | Description |
| --- | --- | --- |
| `n` | `integer` | The HP to take, 0 or more. |

| Returns | Type | Description |
| --- | --- | --- |
| `taken` | `integer` | The HP taken, after the 1 HP floor. |

### rq.BattleTurnCtx:heal

```lua
rq.BattleTurnCtx:heal(n) -> integer
```

`since 2.1.0`

Gives HP at this turn start, with the game's regeneration effect and number.

The HP stops at the most HP. A downed character gets nothing.

Raises an error for a number that is not whole or is below 0.

| Parameter | Type | Description |
| --- | --- | --- |
| `n` | `integer` | The HP to give, 0 or more. |

| Returns | Type | Description |
| --- | --- | --- |
| `healed` | `integer` | The HP given, after the cap. |

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
