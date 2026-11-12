# rq.QuestDef

What `rq.quests.define` takes: a quest of the mod's own, with a map or with none.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `id` | `string` | The quest's id, such as "mymod:lotion", 1 to 64 bytes. The calls that take a quest number take it. |
| `name` | `string` | The name the list shows, 1 to 40 characters. |
| `text` *(optional)* | `string\|string[]` | The quest's text, up to 5 lines: a list of lines, or one text with line breaks. Default none. |
| `place` *(optional)* | `string` | Where it takes place, up to 100 characters. Default "". |
| `fights` *(optional)* | `boolean` | The quest has fights: the list's battle mark (the game's kind 2). false (the default) shows no mark (kind 3, a story or a menu). Not with `map`, which has its own mark. |
| `main` *(optional)* | `boolean` | A main quest, in the list's main tab. false (the default) is a side quest. |
| `difficulty` *(optional)* | `integer` | The difficulty, 0 to 999, before the world's addition (+2 per world after the first, when not 0). Default 0. |
| `fame` *(optional)* | `integer` | The fame of the first clear, 0 to 9999999. The game halves it after each clear, and after the first for a quest with no fights. Default 0. |
| `conditions` *(optional)* | [`rq.QuestCondition`](rq.QuestCondition.md) `[]` | Up to 3 conditions to take part, as `rq.quests.edit` takes them. Default none. |
| `condition` *(optional)* | `{text: string, ok: fun(no: integer): boolean}` | A condition of the mod's own, as `rq.quests.edit`'s: while `ok(no)` returns false or nil, Take is greyed and the list shows `text` (1 to 50 characters). |
| `open` *(optional)* | `boolean` | Available from the moment a save first has the quest. false (the default) keeps it locked until `rq.quests.unlock` or `after`. |
| `after` *(optional)* | `integer\|string` | A quest, by number or id, whose clear opens this one. When a save first has the quest and that one is already cleared, it opens at once. Not with `open`. |
| `run` *(optional)* | `fun(q:` [`rq.QuestRunCtx`](rq.QuestRunCtx.md) `): ("clear"\|"fail"\|"abandon"\|"escape"\|nil)` | The quest's script, run when the quest starts. It may wait: scenes, fights, choices, dialogs. It returns how the quest ends; nil is "clear". Needed for a quest with no map. With a map it is the prologue, played before the map: nil goes on to the map, and a result ends the quest without it. |
| `map` *(optional)* | [`rq.QuestMap`](rq.QuestMap.md) | The quest's map: areas on the game's 4 by 4 grid, set up as the game's quests set theirs. With it the list shows the map mark (`rq.QuestData.kind` `"quest"`). Since 2.42.0. |

## Used by

[`rq.quests.define`](../api/rq.quests.md#rqquestsdefine)
