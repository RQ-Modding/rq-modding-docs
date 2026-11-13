# rq.LearnableRow

One row of the skill buy list, from `rq.chara.learnable`.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `skill` | `integer` | The skill number. |
| `points` | `integer` | The price of its next step in skill points; 0 when the list shows it but does not sell it now. |
| `n` | `integer` | The character's level in it now (as `rq.SkillLevel.n`); 0 when the character does not have it. |
| `why` *(optional)* | `string` | The game's reason it is not for sale, as "Cannot learn yet\n・Condition: Over LV 15"; nil when it is. |

## Used by

[`rq.chara.learnable`](../api/rq.chara.md#rqcharalearnable)
