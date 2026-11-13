# rq.LearnableRow

One row of the skill buy list, from `rq.chara.learnable`.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `skill` | `integer` | The skill number. |
| `points` | `integer` | The price of its next step in skill points; 0 when the list shows it but does not sell it now. |
| `n` | `integer` | The character's level in it now (as `rq.SkillLevel.n`); 0 when the character does not have it. |
| `why` *(optional)* | `string` | The game's reason it is not for sale, as "Cannot learn yet\n・Condition: Over LV 15"; nil when it is. |
| `step` | `integer` | The uses or ranks one purchase adds (since 2.48.0): 3 for skill 384, 1 for the rest. |
| `needs` *(optional)* | [`rq.SkillLevel`](rq.SkillLevel.md) `[]` | For a row not for sale, the skills and levels the game's condition names (since 2.48.0), read from `why`: Healing 3's is `{ { id = 222, n = 3 } }` (Healing 2 at 3 or more); empty when it names no skill. nil for a row for sale. |
| `level` *(optional)* | `integer` | For a row not for sale, the character level the condition asks for (since 2.48.0), read from `why` ("Over LV 25", full-width digits too); nil when it names none. |

## Used by

[`rq.chara.learnable`](../api/rq.chara.md#rqcharalearnable)
