# rq.MusicNow

`since 2.4.0`

What `rq.music.current` gives: the track that plays now.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `no` | `integer` | The track number. |
| `name` | `string` | Its name, as in `rq.music.info`. |
| `file` *(optional)* | `string` | The mod's file that plays; nil for the game's. |
| `mod` *(optional)* | `string` | The id of the mod whose file plays. |
| `pos` | `number` | Where it plays, in seconds from the file's start. |
| `seconds` | `number` | The length of what plays, in seconds. |

## Used by

[`rq.music.current`](../api/rq.music.md#rqmusiccurrent)
