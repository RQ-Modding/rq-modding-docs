# rq.FlashInfo

`since 2.63.0`

What `rq.image.flash_info` returns.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `w` | `integer` | The stage's width: the animation's width on screen, in game pixels. |
| `h` | `integer` | The stage's height, in game pixels. |
| `frames` | `integer` | Frames, as the file's header counts them: the game plays this many. |
| `ms` | `integer` | Its length at the game's 30 frames a second, in ms. |
| `bitmaps` | `integer` | Pictures in the file. |
| `pixels` | `integer` | The pictures' pixels, all together. |
| `sounds` | `integer` | Sounds in the file. |
| `starts` | `integer` | Places where one of its sounds starts. |
| `mod` | `boolean` | true when what the game plays under this name is a mod's file (`add_flash`, `add_gif`, or a mark from `rq.battle.set_mark`). |

## Used by

[`rq.image.flash_info`](../api/rq.image.md#rqimageflash_info)
