# rq.MonsterGroup

A mod's enemy group, as `rq.monster.group` takes it.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `id` | `string` | The text id, such as "mymod:roaches". It becomes the group's number, from 1000 to 9999. |
| `name` *(optional)* | `string` | The name the game's log shows for the group. Default: the id. |
| `exp` *(optional)* | `integer` | The fight's EXP, 0 or more. Default 10. |
| `rank` *(optional)* | `integer` | The fight's rank (the game's `FA[3]`), 0 or more; worlds 2 and 3 add 2 and 4, as to the game's groups. Default 0. |
| `lineups` | `(integer\|string\|false)[][]` | 1 to 6 line-ups, each a list of up to 5 monsters by rank: a monster number, a mod's monster's text id, or 0 or false for an empty rank. Each needs one monster. |

## Used by

[`rq.monster.group`](../api/rq.monster.md#rqmonstergroup)
