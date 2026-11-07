# rq.Unit

A recruited character, from `rq.units()`.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `id` | `integer` | The roster slot (iic), the number the `rq.chara` calls take. |
| `name` | `string` | The name. |
| `class` | `string` | The class's name. |
| `classId` | `integer` | The class number. |
| `level` | `integer` | The level. |
| `stats` | `{hp: integer, hpMax: integer, atk: integer, def: integer, mag: integer, mdef: integer, hit: integer, eva: integer, crit: integer, impact: integer, resist: integer, spd: integer}` | The current stats, as the game stores them. |
| `equipment` | `{special: integer, weapon: integer, armor: integer, item: integer}` | The item instance in each slot, 0 when it is empty. |
| `active` | [`rq.SkillBrief`](rq.SkillBrief.md) `[]` | The skills set for battle, up to 8. |
| `learned` | [`rq.SkillBrief`](rq.SkillBrief.md) `[]` | The skills the character owns, up to 40. |
| `potential` | [`rq.SkillBrief`](rq.SkillBrief.md) `[]` | The skills the character can still learn, up to 40. |

## Used by

[`rq.units.list`](../api/rq.units.md#rqunitslist)
