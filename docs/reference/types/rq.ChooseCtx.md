# rq.ChooseCtx

`since 2.38.0`

What `rq.battle.on_choose` gets on an enemy's or the familiar's turn.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The actor's roster slot: 1 to 5 for an enemy, 10 for the familiar. |
| `unit` | `integer` | The actor's battle number. |
| `side` | `"enemy"\|"familiar"` | Whose turn it is. |
| `rank` | `integer` | The enemy's rank, 1 to 5; 0 for the familiar. |
| `turn` | `integer` | The fight's action count (`◆戦闘ターン`), as `rq.battle.on_turn`'s. |
| `skill` | `integer` | The skill about to be used: the game's choice, then what the callback before left. Write a skill number to change it. |
| `target` *(optional)* | `integer` | The target's roster slot: the game's roll, then what the callback before left. Write a slot to change it, or nil to let the game pick. nil for a skill with no single target (all, a row, all allies); the actor for a self skill. |
| `rolled` | `integer` | The skill the game's draw gave, before its Standby rule. |
| `standby` | `boolean` | true when `skill` is Standby (384) because of the game's rule: a skill that reaches only the front row, from the back row, while an enemy stands in the front row. |
| `charged` | `boolean` | true on the turn a skill charged the turn before is released: only `target` can change then. |
| `skills` | [`rq.ChooseSkill`](rq.ChooseSkill.md) `[]` | The actor's list as it is now. |

## Functions

| Name | Summary |
| --- | --- |
| [`rq.ChooseCtx:targets`](#rqchoosectxtargets) | The units a skill may aim at from this actor, by the rules `on_choose` checks a target with. |

### rq.ChooseCtx:targets

```lua
rq.ChooseCtx:targets(skill) -> integer[]
```

`since 2.38.0`

The units a skill may aim at from this actor, by the rules `on_choose` checks a target with.

A unit standing on the side the skill's target kind names (the other side for melee, ranged and
random targets; the actor's own for an ally skill), with no hidden ally (a hiding rate, as Stealth
gives) and, for a melee skill, only the front row (ranks 1 to 3) while one stands there. The
actor alone for a self skill; empty for a skill with no single target.

```lua
local t = ctx:targets(FIREBALL)
if #t > 0 then ctx.skill, ctx.target = FIREBALL, t[1] end
```

| Parameter | Type | Description |
| --- | --- | --- |
| `skill` *(optional)* | `integer` | The skill. Default: `ctx.skill`. |

| Returns | Type | Description |
| --- | --- | --- |
| `targets` | `integer[]` | The roster slots, in rank order. |

## Used by

[`rq.battle.on_choose`](../api/rq.battle.md#rqbattleon_choose)
