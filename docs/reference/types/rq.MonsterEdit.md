# rq.MonsterEdit

What `rq.monster.edit` changes. Every field is optional; the numbers are whole and 0 or more.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `name` *(optional)* | `string` | The name, not empty. |
| `model` *(optional)* | `integer` | The 3D model. |
| `boss` *(optional)* | `boolean` | The monster is a boss. |
| `race` *(optional)* | `integer` | The race. |
| `type` *(optional)* | `integer` | The type value. |
| `level` *(optional)* | `integer` | The level. |
| `hp` *(optional)* | `integer` | HP. |
| `spd` *(optional)* | `integer` | Speed. |
| `atk` *(optional)* | `integer` | Attack. |
| `def` *(optional)* | `integer` | Defense. |
| `mag` *(optional)* | `integer` | Magic. |
| `mdef` *(optional)* | `integer` | Magic defense. |
| `hit` *(optional)* | `integer` | Accuracy. |
| `eva` *(optional)* | `integer` | Evasion. |
| `crit` *(optional)* | `integer` | Critical rate. |
| `impact` *(optional)* | `integer` | Impact rate. |
| `resist` *(optional)* | `integer` | Resistance. |
| `weak_element` *(optional)* | `integer` | The weak element. |
| `fire_res` *(optional)* | `integer` | Fire resistance. |
| `ice_res` *(optional)* | `integer` | Ice resistance. |
| `thunder_res` *(optional)* | `integer` | Thunder resistance. |
| `light_res` *(optional)* | `integer` | Light resistance. |
| `dark_res` *(optional)* | `integer` | Dark resistance. |
| `skills` *(optional)* | `table<integer,` [`rq.MonsterSkillEdit`](rq.MonsterSkillEdit.md) `\|false>` | By position, 1 to 5: a table changes the fields it gives; `false` empties the position. |
| `lines` *(optional)* | `{wait?: string\|false, attack?: string\|false, big?: string\|false, support?: string\|false}` | By kind: a text replaces the line; `false` removes it. |
| `drops` *(optional)* | [`rq.MonsterDrop`](rq.MonsterDrop.md) `[]` | Up to 8 items the monster may leave after a won fight, rolled in order; the first that rolls is given. `{}` gives none. Since 2.40.0. |

## Used by

[`rq.monster.edit`](../api/rq.monster.md#rqmonsteredit)
