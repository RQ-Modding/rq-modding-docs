# rq.SoundOpts

How `rq.sound.play` and `play_flash` play a sound.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `volume` *(optional)* | `integer` | The volume, 0 to 100, clamped. Default 100. |
| `loop` *(optional)* | `integer` | How many times it plays; 0 loops until stopped. Default 1. |
| `index` *(optional)* | `integer` | `play_flash` only: which sound of the file, from 1. Default 1. |

## Used by

[`rq.sound.play`](../api/rq.sound.md#rqsoundplay), [`rq.sound.play_flash`](../api/rq.sound.md#rqsoundplay_flash)
