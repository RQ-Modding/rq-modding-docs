# rq.MusicListOpts

`since 2.27.0`

What `rq.uikit.music_list` takes.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `x` *(optional)* | `integer` | Left edge; default the layout's. |
| `y` *(optional)* | `integer` | Top edge; default the layout's. |
| `w` *(optional)* | `integer` | The rows' width. Default 700. |
| `id` *(optional)* | `string` | The widgets' id prefix. Default `"music"`. |
| `moments` *(optional)* | [`rq.MusicMoment`](rq.MusicMoment.md) `[]` | Moments with a switch, after the tracks. |

## Used by

[`rq.uikit.music_list`](../api/rq.uikit.md#rquikitmusic_list)
