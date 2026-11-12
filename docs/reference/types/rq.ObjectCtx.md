# rq.ObjectCtx

What an `rq.dungeon.on_object` function gets.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `id` | `string` | The object's id. |
| `x` | `integer` | The cell, east. |
| `z` | `integer` | The cell, north. |
| `quest` | `integer` | The quest being played. |
| `area` | `integer` | The area, 1 to 16. |
| `look` | `string` | The object's look. |
| `keep` | `boolean` | Writable. true puts the object back on its cell after the function. It starts as `place`'s `keep` at every step: a true written here is for this step only. |
| `remove` | `fun(self:` [`rq.ObjectCtx`](rq.ObjectCtx.md) `)` | Takes the object away for good: the same as `keep = false`. |

## Used by

[`rq.QuestObject`](rq.QuestObject.md), [`rq.dungeon.on_object`](../api/rq.dungeon.md#rqdungeonon_object)
