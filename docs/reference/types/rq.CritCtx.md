# rq.CritCtx

What `rq.combat.on_crit` gets where the game rolls a critical.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `attacker` | `integer` | The attacker's roster slot. |
| `defender` | `integer` | The defender's roster slot. |
| `skill` | `integer` | The skill number. |
| `rate` | `integer` | The critical chance the game is about to roll, in percent. |
| `defender_type` | `integer` | The defender's type (`Ｃタイプ`); 22 is humanoid. |

## Used by

[`rq.combat.on_crit`](../api/rq.combat.md#rqcombaton_crit)
