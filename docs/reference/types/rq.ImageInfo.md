# rq.ImageInfo

What `rq.image.info` returns.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `exists` | `boolean` | The number shows something, from the game or a mod. |
| `mod` | `boolean` | A mod image is on this number. |
| `replaced` *(optional)* | `boolean` | It replaces a game CG. |
| `w` *(optional)* | `integer` | Width. |
| `h` *(optional)* | `integer` | Height. |
| `game_w` *(optional)* | `integer` | The game CG's own width, when replaced. |
| `game_h` *(optional)* | `integer` | The game CG's own height, when replaced. |
| `frames` *(optional)* | `integer` | A moving picture's frames. Since 2.25.0. |
| `ms` *(optional)* | `integer` | A moving picture's loop, in ms. Since 2.25.0. |
| `drawn` *(optional)* | `boolean` | A moving picture was drawn by the game in the last quarter second. Since 2.25.0. |

## Used by

[`rq.image.info`](../api/rq.image.md#rqimageinfo)
