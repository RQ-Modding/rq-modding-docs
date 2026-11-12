# rq.HealCtx

`since 2.37.0`

What `rq.combat.on_heal` gets for one heal; `amount` is writable.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `healer` | `integer` | The roster slot of the one who healed. |
| `target` | `integer` | The roster slot that gets the HP. |
| `skill` | `integer` | The skill number. |
| `kind` | `"skill"\|"revive"\|"absorb"` | A support skill's heal, a revive of a downed character, or HP absorb from a hit (the attacker gets the damage). |
| `amount` | `integer` | The HP given, as the game shows it; write it to change it. Rounded down, 0 or more. The HP stops at the most HP. |

## Used by

[`rq.combat.on_heal`](../api/rq.combat.md#rqcombaton_heal)
