# rq.MusicPageOpts

`since 2.27.0`

What `rq.music.page` takes.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `title` *(optional)* | `string` | The page's row in the Mods tab and its heading. Default `"<mod id>: music"`. |
| `id` *(optional)* | `string` | The page's id (`rq.config.page`). Default `"<mod id>:music"`. |
| `moments` *(optional)* | [`rq.MusicMoment`](rq.MusicMoment.md) `[]` | Moments of the mod's own `on_play`, each with a switch, after the tracks. |

## Used by

[`rq.music.page`](../api/rq.music.md#rqmusicpage)
