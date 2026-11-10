# rq.ImageOpts

Options for `rq.image.add` and `rq.image.replace`.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `fit` *(optional)* | `rq.ImageFit` | How the file fits `w` by `h`. Default "none" for `add`, "stretch" for `replace`. |
| `w` *(optional)* | `integer` | Target width. Default: the file's (for `replace`, the game CG's). |
| `h` *(optional)* | `integer` | Target height. Default: the file's (for `replace`, the game CG's). |
| `keep_size` *(optional)* | `boolean` | `replace` only: keep the file's size instead of the game CG's. |
| `fps` *(optional)* | `number` | A moving picture's frames a second, above 0 and up to 240. Default: the file's own delays. Since 2.25.0. |
| `clock` *(optional)* | `"game"\|"real"` | A moving picture runs on the game's clock, which follows `rq.speed` (default), or on real time. Since 2.25.0. |

## Used by

[`rq.image.add`](../api/rq.image.md#rqimageadd), [`rq.image.replace`](../api/rq.image.md#rqimagereplace)
