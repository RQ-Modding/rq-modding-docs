# rq.SceneChoice

One row of `rq.scene.choice`.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `id` *(optional)* | `integer` | What `choice` returns for this row. Default: its place in the list. |
| `text` | `string` | The text. |
| `r` *(optional)* | `integer` | Red, 0 to 255. Default: the game's color. |
| `g` *(optional)* | `integer` | Green, 0 to 255. Default: the game's color. |
| `b` *(optional)* | `integer` | Blue, 0 to 255. Default: the game's color. |
| `comment` *(optional)* | `string` | The game's comment text for the row. Default "". |
| `sound` *(optional)* | `integer` | A sound number for the row. |

## Used by

[`rq.scene.choice`](../api/rq.scene.md#rqscenechoice)
