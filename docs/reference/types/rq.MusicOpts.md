# rq.MusicOpts

`since 2.4.0`

How `rq.music.replace` and `ctx:file` play a file.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `loop_start` *(optional)* | `number` | Where the loop goes back to after the end, in seconds. Default the file's `LOOPSTART` tag, else 0. |
| `loop_end` *(optional)* | `number` | Where the loop ends, in seconds. Default the file's `LOOPLENGTH` or `LOOPEND` tag, else the file's end. |
| `volume` *(optional)* | `integer` | The file's own volume, 0 to 200, on top of the game's music volume and fades. Default 100, as loud as the file is; above 100 raises a quiet file, and a loud one clips (0 to 100 before 2.27.0). |
| `name` *(optional)* | `string` | `replace` only: the track's name in the extras' music room and in `rq.music.info`. |

## Used by

[`rq.MusicPlayCtx:file`](rq.MusicPlayCtx.md#rqmusicplayctxfile), [`rq.music.replace`](../api/rq.music.md#rqmusicreplace)
