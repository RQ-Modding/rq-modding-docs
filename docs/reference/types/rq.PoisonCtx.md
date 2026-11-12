# rq.PoisonCtx

`since 2.37.0`

What `rq.combat.on_poison` gets where the game works out a poison.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `attacker` | `integer` | The attacker's roster slot. |
| `defender` | `integer` | The defender's roster slot. |
| `skill` | `integer` | The skill number. |
| `rate` | `integer` | The poison chance about to be rolled, 0 to 100: the game's (from the skill, weapon 118 or Poison Attack, 264; 0 for most hits; with a mod's `rq.combat.set_rules` poison rule, since 2.44.0), then what the callback before left. |

## Used by

[`rq.combat.on_poison`](../api/rq.combat.md#rqcombaton_poison)
