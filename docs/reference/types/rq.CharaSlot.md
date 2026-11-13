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
| `cost` | `integer` | The row's purchase record, as `rq.ForgetCtx.cost` (since 2.45.0). |
| `n` | `integer` | The skill's level (since 2.45.0): most uses for a use skill (type 10), rank 1 to 4 for a ranked one (20, 30), 1 for the rest. |

## Used by

[`rq.chara.slots`](../api/rq.chara.md#rqcharaslots)
