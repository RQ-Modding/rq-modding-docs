# rq.QuestObject

An object of a mod's quest's area, in `rq.QuestArea.objects`.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `kind` | `"chest"\|"red-chest"\|"enemy"\|"trap"\|"achievement"\|"spring"\|"escape"\|"gold"\|"exp"\|"custom"` | One of the game's objects, as `rq.dungeon.place` places it, or `"custom"`, an object of the mod's own with a function. |
| `spot` *(optional)* | `"any"\|"wide"\|{x: integer, z: integer}` | Where: a free spot of the room (the default); its wide spot, in the open middle of a large room, for a boss or a treasure; or a cell, as `rq.dungeon.grid` counts them (`{ 25, 25 }` or `{ x = 25, z = 25 }`). A cell that is not free floor in the room drawn gives a free spot, with a line in the log. |
| `item` *(optional)* | `integer\|string` | A chest's item: a number, or a mod's item id (`rq.item.define`). Default: the map's `loot`. It may come out unidentified, as any chest's item (the game identifies a set item 1 time in 3, more with a member's skill), and then the appraisal at the end keeps it only when the player pays for it. |
| `id` *(optional)* | `string` | A custom object's id, 1 to 64 bytes. |
| `look` *(optional)* | `string` | A custom object's look, one of `rq.dungeon.looks()`. Default "event". |
| `keep` *(optional)* | `boolean` | A custom object stays on its cell after each step, as `rq.dungeon.place`'s `keep`. |
| `run` *(optional)* | `fun(ctx:` [`rq.ObjectCtx`](rq.ObjectCtx.md) `): ("clear"\|"fail"\|"abandon"\|"escape"\|integer\|nil)` | A custom object's function, registered as `rq.dungeon.on_object` registers one: nil goes on, a result ends the quest. |

## Used by

[`rq.QuestArea`](rq.QuestArea.md)
