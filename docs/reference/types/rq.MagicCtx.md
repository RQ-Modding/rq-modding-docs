# rq.MagicCtx

`since 2.1.0`

What `rq.combat.on_magic` gets for one spell.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `attacker` | `integer` | The attacker's roster slot. |
| `defender` | `integer` | The defender's roster slot. |
| `skill` | `integer` | The skill number. |
| `damage` | `integer` | The final damage the game worked out, before any percent. |
| `magic` | `integer` | The attacker's magic. |
| `race` | `integer` | The defender's race (`rq.ids.race`); 8 is a hanny. |
| `defender_type` | `integer` | The defender's type (`Ｃタイプ`); 22 is humanoid. |
| `forecast` | `boolean` | true when the game only works out the battle forecast (`rq.battle.on_forecast`), not a real hit: count nothing and roll no dice then. Since 2.26.0. |

## Used by

[`rq.StatusDef`](rq.StatusDef.md), [`rq.combat.on_magic`](../api/rq.combat.md#rqcombaton_magic)
