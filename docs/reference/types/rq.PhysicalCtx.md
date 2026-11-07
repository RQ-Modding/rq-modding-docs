# rq.PhysicalCtx

What `rq.combat.on_physical` gets for one physical hit.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `attacker` | `integer` | The attacker's roster slot. |
| `defender` | `integer` | The defender's roster slot. |
| `skill` | `integer` | The skill number. |
| `attack` | `integer` | The attack before defense, as the callback before left it. |
| `magic` | `integer` | The attacker's magic. |
| `race` | `integer` | The defender's race; 8 is a hanny. |
| `defender_type` | `integer` | The defender's type (`Ｃタイプ`); 22 is humanoid. |

## Used by

[`rq.combat.on_physical`](../api/rq.combat.md#rqcombaton_physical)
