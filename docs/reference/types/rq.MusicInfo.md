# rq.MusicInfo

`since 2.4.0`

What `rq.music.info` tells about a track.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `no` | `integer` | The track number. |
| `name` | `string` | The game's name for it (`音楽の名前`), or the mod's `name`; "" when it has none. |
| `exists` | `boolean` | Whether the game has this track. |
| `file` *(optional)* | `string` | The mod's file, as the mod gave it; nil when the game's plays. |
| `mod` *(optional)* | `string` | The id of the mod whose file it is. |
| `volume` *(optional)* | `integer` | The file's volume, 0 to 100. |
| `loop_start` *(optional)* | `number` | The file's loop start, in seconds. |
| `loop_end` *(optional)* | `number` | The file's loop end, in seconds. |
| `seconds` *(optional)* | `number` | The length, in seconds: the file's, else the game track's. |

## Used by

[`rq.music.info`](../api/rq.music.md#rqmusicinfo), [`rq.music.replace`](../api/rq.music.md#rqmusicreplace)
