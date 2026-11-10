# rq.AccuracyCtx

What `rq.combat.on_accuracy` gets for one accuracy check.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `attacker` | `integer` | The attacker's roster slot. |
| `defender` | `integer` | The defender's roster slot. |
| `skill` | `integer` | The skill number. |
| `forecast` | `boolean` | true when the game only works out the battle forecast (`rq.battle.on_forecast`), not a real hit: count nothing and roll no dice then. Since 2.26.0. |

## Used by

[`rq.StatusDef`](rq.StatusDef.md), [`rq.combat.on_accuracy`](../api/rq.combat.md#rqcombaton_accuracy)
