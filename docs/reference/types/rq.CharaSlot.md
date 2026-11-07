# rq.CharaSlot

One row of a character's skill list, from `rq.chara.slots`.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `slot` | `integer` | The row, 1 to 20. |
| `skill` | `integer` | The skill number in the row; 0 when the row is empty. |
| `uses` | `integer` | Uses left. |
| `max` | `integer` | Most uses. |
| `bar` | `integer` | The hotbar position, 1 to 6; 0 when the skill is not on the hotbar. |

## Used by

[`rq.chara.slots`](../api/rq.chara.md#rqcharaslots)
