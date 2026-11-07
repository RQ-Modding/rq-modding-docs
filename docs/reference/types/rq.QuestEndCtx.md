# rq.QuestEndCtx

What an `rq.quests.on_end` callback gets.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `quest` | `integer` | The quest that ends. |
| `result` | `integer` | How it ends: 1 clean clear, 2 party defeat, 3 abandoned, 4 escape device (abandoned, items kept). |
| `cleared` | `boolean` | `result` is 1. |
| `party` | `integer[]` | The dungeon party's roster slots (iic). |

## Used by

[`rq.quests.on_end`](../api/rq.quests.md#rqquestson_end)
