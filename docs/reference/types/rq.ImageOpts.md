# rq.ImageOpts

Options for `rq.image.add` and `rq.image.replace`.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `fit` *(optional)* | `rq.ImageFit` | How the file fits `w` by `h`. Default "none" for `add`, "stretch" for `replace`. |
| `w` *(optional)* | `integer` | Target width. Default: the file's (for `replace`, the game CG's). |
| `h` *(optional)* | `integer` | Target height. Default: the file's (for `replace`, the game CG's). |
| `keep_size` *(optional)* | `boolean` | `replace` only: keep the file's size instead of the game CG's. |

## Used by

[`rq.image.add`](../api/rq.image.md#rqimageadd), [`rq.image.replace`](../api/rq.image.md#rqimagereplace)
