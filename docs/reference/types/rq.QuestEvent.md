# rq.QuestEvent

What `rq.quests.on_event` and `on_event_after` callbacks get.

`code` 8 is `start` and 7 is `map_load`; otherwise `fg` names the kind: 4 `map_event`, 5 `warp`,
6 `warp_cancel`, 7 `before_battle`, 8 `after_battle`, 9 `chest`, 10 `contact`, 11 `before_warp`;
anything else is `other`.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `quest` | `integer` | The quest being played. |
| `kind` | `"start"\|"map_load"\|"map_event"\|"warp"\|"warp_cancel"\|"before_warp"\|"before_battle"\|"after_battle"\|"chest"\|"contact"\|"other"` | The quest moment. |
| `no` | `integer` | The map event number, or the map number for `map_load`. |
| `code` | `integer` | The first argument of the game's `クエスト処理`. |
| `fg` | `integer` | The third argument of `クエスト処理`. |
| `result` *(optional)* | `integer` | What the game's handling returned; only in `on_event_after`. |

## Used by

[`rq.quests.on_event`](../api/rq.quests.md#rqquestson_event), [`rq.quests.on_event_after`](../api/rq.quests.md#rqquestson_event_after)
