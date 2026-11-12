# rq.QuestCondition

A condition to take part in a quest, from `rq.QuestData.conditions` and for `rq.quests.edit`.

`kind` names the game's condition: `party_max` (at most `count` members in the party), `member`
(character `chara` in the party), `own` (both `charas` recruited), `member_level` (`chara` in the
party at `level` or more), `item` (item `item` owned) and `special` (never met: the quest list
shows the quest's special text, the game's way to keep a quest closed until the story allows it).
`other` is a number the game does not use, which it counts as met. `text` and `met` are read only
and `rq.quests.edit` ignores them, so a condition from `rq.quests.get` can be given back as it is.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `kind` | `"party_max"\|"member"\|"own"\|"member_level"\|"item"\|"special"\|"other"` | The condition. |
| `count` *(optional)* | `integer` | `party_max`: the most members, 1 to 5. |
| `chara` *(optional)* | `integer` | `member` and `member_level`: a character number (`rq.ids.chara`). |
| `charas` *(optional)* | `integer[]` | `own`: two character numbers. |
| `level` *(optional)* | `integer` | `member_level`: the lowest level, 1 or more. |
| `item` *(optional)* | `integer` | `item`: an item number (`rq.ids.item`). |
| `text` *(optional)* | `string` | The line the quest list shows for it. For `special` in `rq.quests.edit`: the special text to show, up to 50 characters; left out, the quest's own stays. |
| `met` *(optional)* | `boolean` | Read only. The condition is met now. |

## Used by

[`rq.QuestData`](rq.QuestData.md), [`rq.QuestEdit`](rq.QuestEdit.md)
