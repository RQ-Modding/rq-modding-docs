# rq.QuestAreaCtx

What an area's `setup` gets (`rq.QuestArea.setup`).

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `id` | `string` | The quest's id. |
| `quest` | `integer` | The quest's number in this save. |
| `area` | `integer` | The area, 1 to 16. |
| `row` | `integer` | The area's row, 1 (north) to 4. |
| `col` | `integer` | The area's column, 1 (west) to 4. |
| `first` | `boolean` | The party enters the area for the first time in this run. |

## Used by

[`rq.QuestArea`](rq.QuestArea.md)
