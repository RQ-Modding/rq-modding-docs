# rq.CharaInit

Stat bonuses that each recalculation adds, in `rq.CharaFields.init`.

`hp`, `atk`, `def`, `mag` and `mdef` are percents (`atk = 10` is +10%); the rest are flat points.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `hp` *(optional)* | `integer` | Most HP, in percent. |
| `atk` *(optional)* | `integer` | Attack, in percent. |
| `def` *(optional)* | `integer` | Defense, in percent. |
| `mag` *(optional)* | `integer` | Magic, in percent. |
| `mdef` *(optional)* | `integer` | Magic defense, in percent. |
| `spd` *(optional)* | `integer` | Speed, in points. |
| `hit` *(optional)* | `integer` | Accuracy, in points. |
| `eva` *(optional)* | `integer` | Evasion, in points. |
| `crit` *(optional)* | `integer` | Critical rate, in points. |
| `impact` *(optional)* | `integer` | Impact rate, in points. |
| `resist` *(optional)* | `integer` | Resistance, in points. |
| `sp` *(optional)* | `integer` | Skill points the character starts with. |

## Used by

[`rq.CharaFields`](rq.CharaFields.md)
