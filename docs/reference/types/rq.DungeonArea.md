# rq.DungeonArea

One area of `rq.dungeon.areas()`.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `no` | `integer` | The area, 1 to 16. |
| `row` | `integer` | Its row, 1 to 4 from the top. |
| `col` | `integer` | Its column, 1 to 4 from the left. |
| `found` | `boolean` | The area map draws it: the party found it, in this run or an earlier one. |
| `north` | `boolean` | A route to the area north is drawn. |
| `east` | `boolean` | A route to the area east is drawn. |
| `south` | `boolean` | A route to the area south is drawn. |
| `west` | `boolean` | A route to the area west is drawn. |
| `here` | `boolean` | The party is in it. |
| `goal` | `boolean` | It is the quest's goal. The game marks the goal only once the quest was cleared. |

## Used by

[`rq.dungeon.areas`](../api/rq.dungeon.md#rqdungeonareas)
