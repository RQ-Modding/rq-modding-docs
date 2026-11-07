# rq.MarkDef

How `rq.battle.set_mark` shows one of the game's marks.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `hide` *(optional)* | `boolean` | Takes the mark off the screen; the state itself stays. |
| `icon` *(optional)* | `integer` | A CG number shown instead of the game's picture. |
| `anim` *(optional)* | `string` | An `rq.image.add_gif` key shown instead of the game's picture; wins over `icon`. |
| `x` *(optional)* | `integer` | Pixels from the card's left edge. Default: where the game puts it. |
| `y` *(optional)* | `integer` | Pixels from the card's top edge. Default: where the game puts it. |
| `layer` *(optional)* | `integer` | As in `rq.BuffDef`. Marks 1 to 23 sit at layer 1, under an ally's face. |
| `order` *(optional)* | `integer` | Marks 31 to 36 only: as in `rq.BuffDef`. |
| `pinned` *(optional)* | `boolean` | Marks 31 to 36 only: as in `rq.BuffDef`. |

## Used by

[`rq.battle.set_mark`](../api/rq.battle.md#rqbattleset_mark)
