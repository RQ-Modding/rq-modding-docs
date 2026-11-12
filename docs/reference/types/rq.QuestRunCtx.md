# rq.QuestRunCtx

What a quest's `run` gets (`rq.QuestDef.run`).

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `id` | `string` | The quest's id. |
| `no` | `integer` | Its number in this save. |
| `tries` | `integer` | How many times it was taken, this time included. |
| `clears` | `integer` | How many times it was cleared before. |
| `first` | `boolean` | It was never cleared (`clears` is 0). |

## Used by

[`rq.QuestDef`](rq.QuestDef.md)
