# rq.QuestRunEdit

What `rq.quests.set_run` writes; a field left out stays.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `fame` *(optional)* | `integer` | The fame a clear gives, 0 to 9999999. |
| `exp_bonus` *(optional)* | `integer` | The EXP bonus, 0 to 50 (the game's cap). |
| `progress` *(optional)* | `integer` | The progress bar on the map panel, 0 to 100 (it blinks from 90). Since 2.42.0. |
| `bonuses` *(optional)* | `{feats?: {count?: integer, max?: integer}\|false, level_ups?: {count?: integer, max?: integer}\|false, enemies?: {count?: integer, max?: integer}\|false}` | Each bonus's count and maximum, 0 to 99. A `max` turns on a bonus the quest does not have; `false` turns one off. A count above the maximum is cut to it. |
| `party_change` *(optional)* | `"normal"\|"none"\|"free"` | The party changes during the quest. |
| `no_area_map` *(optional)* | `boolean` | true hides AREA DISPLAY. |
| `no_warp` *(optional)* | `{north?: boolean, south?: boolean, east?: boolean, west?: boolean}` | true closes the warps that way, false opens them. |

## Used by

[`rq.quests.set_run`](../api/rq.quests.md#rqquestsset_run)
