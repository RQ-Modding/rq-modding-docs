# rq.QuestData

A quest's data as the quest list shows it, from `rq.quests.get`.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `id` | `integer` | The quest number. |
| `name` | `string` | The name. |
| `description` | `string[]` | The quest's text, one entry per line, up to 5; empty lines at the end are left out. |
| `place` | `string` | Where it takes place (`発生場所`, `rq.Quest.map`). |
| `special` | `string` | The text of its special condition, "" when it has none now. |
| `state` | `integer` | 0 locked, 1 available, 2 cleared. |
| `kind` | `"quest"\|"fights"\|"menu"\|"other"` | `quest` a quest; `fights` a quest of fights only, whose fights give a half of their EXP after its first clear, a third after the second and a fifth after that; `menu` an entry of the list that is not a quest (Character Relations, the debug entries). |
| `difficulty` | `integer` | The difficulty the list shows, with the game's addition for the world (2 per world after the first). |
| `fame` | `integer` | The fame the next clear gives, before skill 269 doubles it. The game halves it after each clear. |
| `tries` | `integer` | How many times it was taken. |
| `clears` | `integer` | How many times it was cleared. |
| `conditions` | [`rq.QuestCondition`](rq.QuestCondition.md) `[]` | Its conditions to take part, up to 3; empty for none. |
| `can_take` | `boolean` | Take would be lit for it now (`rq.quests.can_take`). |
| `edited` | `string[]` | The ids of the mods whose `rq.quests.edit` patch is on it, in load order. |

## Used by

[`rq.quests.get`](../api/rq.quests.md#rqquestsget)
