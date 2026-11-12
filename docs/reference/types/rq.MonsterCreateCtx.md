# rq.MonsterCreateCtx

What `rq.monster.on_create` callbacks get. Fields marked writable change the enemy in its slot.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The slot: 1 to 5 for an enemy, 10 for the familiar. |
| `no` | `integer` | The monster number. |
| `id` *(optional)* | `string` | The text id, for a monster a mod defined. Since 2.40.0. |
| `rank` | `integer` | The fight rank the enemy stands in, 1 to 5; 0 for the familiar. |
| `familiar` | `boolean` | The familiar of the party's held item, not an enemy. |
| `world` | `integer` | The world, 1 to 3. |
| `boss` | `boolean` | The monster is a boss (its own flag, not the fight's). |
| `fight_rank` | `integer` | The fight's kind (`◆戦闘ランク`): 0 a scripted fight, 1 an enemy on the map, 2 a boss fight. |
| `group` | `integer` | The fight group (`◆戦闘グループ`). |
| `strength` | `integer` | The game's strength rate (`◆敵強化率`): 130 in a boss fight with `strong`, else 0. |
| `base` | [`rq.Monster`](rq.Monster.md) | The monster's data before the world's rules, as `rq.monster.get` gives it (a copy). |
| `name` | `string` | Writable. The name, not empty. |
| `level` | `integer` | Writable. The level. |
| `hp` | `integer` | Writable. The most HP; the current HP is set to it. |
| `spd` | `integer` | Writable. Speed. |
| `atk` | `integer` | Writable. Attack. |
| `def` | `integer` | Writable. Defense. |
| `mag` | `integer` | Writable. Magic. |
| `mdef` | `integer` | Writable. Magic defense. |
| `hit` | `integer` | Writable. Accuracy. |
| `eva` | `integer` | Writable. Evasion. |
| `crit` | `integer` | Writable. Critical rate. |
| `impact` | `integer` | Writable. Impact rate. |
| `resist` | `integer` | Writable. Resistance. |
| `weak_element` | `integer` | Writable. The weak element. |
| `fire_res` | `integer` | Writable. Fire resistance. |
| `ice_res` | `integer` | Writable. Ice resistance. |
| `thunder_res` | `integer` | Writable. Thunder resistance. |
| `light_res` | `integer` | Writable. Light resistance. |
| `dark_res` | `integer` | Writable. Dark resistance. |

## Used by

[`rq.monster.on_create`](../api/rq.monster.md#rqmonsteron_create)
