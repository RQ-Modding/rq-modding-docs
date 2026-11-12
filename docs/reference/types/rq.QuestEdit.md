# rq.QuestEdit

A patch for `rq.quests.edit`: the fields to change; one left out keeps the game's.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `name` *(optional)* | `string` | The name, 1 to 40 characters. |
| `description` *(optional)* | `string[]` | The text, up to 5 lines, one entry per line with no line break; lines left out are empty. |
| `place` *(optional)* | `string` | Where it takes place, up to 100 characters. |
| `difficulty` *(optional)* | `integer` | The difficulty the list shows, 0 to 999. The game's addition per world is not added to it. |
| `conditions` *(optional)* | [`rq.QuestCondition`](rq.QuestCondition.md) `[]` | Up to 3 conditions, in place of the game's; `{}` for none. |
| `condition` *(optional)* | `{text: string, ok: fun(no: integer): boolean}` | A condition of the mod's own: while `ok(no)` returns false or nil, the quest has the game's special condition with `text` (1 to 50 characters). |

## Used by

[`rq.quests.edit`](../api/rq.quests.md#rqquestsedit)
