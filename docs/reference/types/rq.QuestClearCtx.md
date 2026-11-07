# rq.QuestClearCtx

What an `rq.quests.on_clear` callback gets.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `quest` | `integer` | The quest that was just cleared. |
| `clears` | `integer` | How many times it was cleared, this clear included. |
| `first` | `boolean` | This is its first clear. |

## Used by

[`rq.quests.on_clear`](../api/rq.quests.md#rqquestson_clear)
