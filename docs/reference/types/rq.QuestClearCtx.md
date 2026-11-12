# rq.QuestClearCtx

What an `rq.quests.on_clear` callback gets.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `quest` | `integer` | The quest that was just cleared. |
| `clears` | `integer` | How many times it was cleared, this clear included. |
| `first` | `boolean` | This is its first clear. |
| `id` *(optional)* | `string` | The quest's id, for a quest a mod defined (`rq.quests.define`); nil for the game's. Since 2.41.0. |

## Used by

[`rq.quests.on_clear`](../api/rq.quests.md#rqquestson_clear)
