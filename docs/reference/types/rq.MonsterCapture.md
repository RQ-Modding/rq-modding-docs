# rq.MonsterCapture

A mod's monster's capture (`rq.MonsterDef.capture`): what the game's capture skills (the two
Capture skills, 166 and 451, and Capture Thread, 531) give when they catch it.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `item` | `integer\|string` | The item given, by number or text id: a familiar item the mod defines (`subtype = 20`, see `rq.item`). An item that does not exist when the capture rolls lets the monster escape, with a line in the log. |
| `cg` *(optional)* | `integer` | The CG of the scene the game shows (`rq.image.add` gives one). Without it, no scene: the item is picked up as any other. |
| `text` *(optional)* | `string` | The scene's text, as the game writes it (`$` a line break). |

## Used by

[`rq.MonsterDef`](rq.MonsterDef.md)
