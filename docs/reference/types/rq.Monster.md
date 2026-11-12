# rq.Monster

A monster's data, as `rq.monster.get` returns it. The names are `rq.chara.get`'s.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `no` | `integer` | The monster number (`rq.ids.monster`). |
| `name` | `string` | The name. |
| `model` | `integer` | The 3D model. |
| `boss` | `boolean` | The monster is a boss. |
| `race` | `integer` | The race (`rq.ids.race`). |
| `type` | `integer` | The type value (`rq.ids.chara_type`). |
| `level` | `integer` | The level. |
| `hp` | `integer` | HP. |
| `spd` | `integer` | Speed. |
| `atk` | `integer` | Attack. |
| `def` | `integer` | Defense. |
| `mag` | `integer` | Magic. |
| `mdef` | `integer` | Magic defense. |
| `hit` | `integer` | Accuracy. |
| `eva` | `integer` | Evasion. |
| `crit` | `integer` | Critical rate. |
| `impact` | `integer` | Impact rate. |
| `resist` | `integer` | Resistance. |
| `weak_element` | `integer` | The weak element (`rq.ids.element`). |
| `fire_res` | `integer` | Fire resistance. |
| `ice_res` | `integer` | Ice resistance. |
| `thunder_res` | `integer` | Thunder resistance. |
| `light_res` | `integer` | Light resistance. |
| `dark_res` | `integer` | Dark resistance. |
| `skills` | [`rq.MonsterSkill`](rq.MonsterSkill.md) `[]` | Up to five, in the game's order; the empty positions are left out. |
| `lines` | `{wait?: string, attack?: string, big?: string, support?: string}` | The lines the fight shows: waiting, attacking, a big move, supporting. A kind the monster has not is nil. |
| `id` *(optional)* | `string` | The text id, for a monster a mod defined (`rq.monster.define`). Since 2.40.0. |
| `base` *(optional)* | `integer` | The game monster it is built on, for a monster a mod defined. Since 2.40.0. |
| `kills` | `integer` | How many the party has defeated, as the game's Monster Info counts them (a mod's monster's in the save, by its id). Since 2.40.0. |
| `weak_known` | `boolean` | The party knows its weak point, as the game marks it once a fight shows it; the next build of the monster shows it from the start. Since 2.40.0. |

## Used by

[`rq.MonsterCreateCtx`](rq.MonsterCreateCtx.md), [`rq.monster.get`](../api/rq.monster.md#rqmonsterget)
