# rq.PlayFlashOpts

`since 2.63.0`

Options for `rq.image.play_flash`: the sprite's (`rq.SpriteOpts`, such as `x`, `y`, `z`, `scale`,
`attach` and `sound`) and the play's.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `from` *(optional)* | `integer` | The first frame, from 1. Default 1. |
| `to` *(optional)* | `integer` | The last frame. Default the file's last. |
| `loop` *(optional)* | `boolean` | Plays over and over until the sprite is removed. Default false. |
| `on_end` *(optional)* | `fun(s:` [`rq.Sprite`](rq.Sprite.md) `)` | Runs after the last frame has shown, before the sprite goes. |
| `wait` *(optional)* | `boolean` | In a job from `rq.spawn`: the call returns once the play has ended. Default false. |

## Used by

[`rq.image.play_flash`](../api/rq.image.md#rqimageplay_flash)
