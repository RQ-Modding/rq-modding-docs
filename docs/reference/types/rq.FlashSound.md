# rq.FlashSound

A sound inside a Flash file, from `rq.sound.flash_info`.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `rate` | `integer` | The sample rate, in Hz. |
| `channels` | `integer` | 1 or 2. |
| `bits` | `integer` | 8 or 16. |
| `ms` | `integer` | The length, in milliseconds. |
| `playable` | `boolean` | false for a compressed sound (MP3 or ADPCM), which `play_flash` refuses. |

## Used by

[`rq.sound.flash_info`](../api/rq.sound.md#rqsoundflash_info)
