# rq.UiCommentOpts

`since 2.13.0`

What `rq.uikit.comment` takes besides the text.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `header` *(optional)* | `string` | A title over the text, in 22-pixel black (pink in "red"). |
| `sub` *(optional)* | `string` | Red lines under the text, 3 pixels apart from it, as the game's "cannot use" notes. |
| `style` *(optional)* | `"normal"\|"red"` | "normal" (default): the paper window with a cyan border. "red": the game's red one, as for the skills of a character who cannot use them. |
| `x` *(optional)* | `integer` | Left edge, in game pixels. Default: 11 right of the mouse. |
| `y` *(optional)* | `integer` | Top edge, in game pixels. Default: 20 under the mouse. |
| `game` *(optional)* | `boolean` | `@` and `$` break a line too, as in the game's own texts (`rq.ain` strings). Default false: only `\n` does. |
| `id` *(optional)* | `any` | The window's id in `rqmod-ctl ui` (as `"comment-" .. id`). Default "comment". |

## Used by

[`rq.uikit.comment`](../api/rq.uikit.md#rquikitcomment), [`rq.uikit.comment_size`](../api/rq.uikit.md#rquikitcomment_size)
