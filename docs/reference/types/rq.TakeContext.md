# rq.TakeContext

What an `rq.quests.on_take` callback gets.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `quest` | `integer` | The quest the player is taking. |
| `text` | `string` | The game's question, `Take Quest@` and the quest's name and `?` (`@` is its line break). |
| `id` *(optional)* | `string` | The quest's id, for a quest a mod defined (`rq.quests.define`); nil for the game's. Since 2.41.0. |

## Used by

[`rq.quests.on_take`](../api/rq.quests.md#rqquestson_take)
