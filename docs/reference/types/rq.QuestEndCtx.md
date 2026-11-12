# rq.QuestEndCtx

What an `rq.quests.on_end` callback gets.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `quest` | `integer` | The quest that ends. |
| `result` | `integer` | How it ends: 1 clean clear, 2 party defeat, 3 abandoned, 4 escape device (abandoned, items kept). |
| `cleared` | `boolean` | `result` is 1. |
| `party` | `integer[]` | The dungeon party's roster slots (iic). |
| `id` *(optional)* | `string` | The quest's id, for a quest a mod defined (`rq.quests.define`); nil for the game's. Since 2.41.0. |

## Used by

[`rq.quests.on_end`](../api/rq.quests.md#rqquestson_end)
