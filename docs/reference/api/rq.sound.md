# rq.sound

`since 1.4.0`

Plays sounds: a game sound number, a file in the mod folder, or a sound inside a game Flash file.

They play on the game's sound effect mixer, so Config's sound volume applies, and at real time:
`rq.speed` does not change them. A file or Flash sound is read once and kept in memory, so a sound
played on every hit reads the disk once. At most 32 mod sounds play at once; one more raises an
error. Music is not covered: these play beside the game's music.

```lua
-- Berserk's sound, from its Flash file
rq.sound.play_flash("Data/Flash/Battle/狂戦士発動.swf")
-- A sound of your own, looped, then faded out
local h = rq.sound.play("sfx/rain.ogg", { loop = 0, volume = 60 })
rq.sound.stop(h, 500)
```

## Functions

| Name | Summary |
| --- | --- |
| [`rq.sound.play`](#rqsoundplay) | Plays a game sound or a sound file from the mod folder. |
| [`rq.sound.play_flash`](#rqsoundplay_flash) | Plays a sound kept inside a Flash file. |
| [`rq.sound.flash_info`](#rqsoundflash_info) | Lists the sounds in a Flash file. |
| [`rq.sound.stop`](#rqsoundstop) | Stops a sound, at once or with a fade out. |
| [`rq.sound.playing`](#rqsoundplaying) | Returns whether a sound still plays. |
| [`rq.sound.set_volume`](#rqsoundset_volume) | Changes a sound's volume, at once or over a fade. |

### rq.sound.play

```lua
rq.sound.play(src, opts) -> integer|nil
```

`since 1.4.0`

Plays a game sound or a sound file from the mod folder.

A file can be WAV, OGG, FLAC, Opus or MP3, up to 64 MB. Raises an error for a missing file, a path
out of the mod folder, or when 32 mod sounds already play.

```lua
local h = rq.sound.play("sfx/hit.wav", { volume = 80 })
```

| Parameter | Type | Description |
| --- | --- | --- |
| `src` | `integer\|string` | A game sound number (as for `rq.scene.sound`) or a path in the mod folder. |
| `opts` *(optional)* | [`rq.SoundOpts`](../types/rq.SoundOpts.md) | How to play it. |

| Returns | Type | Description |
| --- | --- | --- |
| `handle` | `integer\|nil` | The handle, or nil when the number does not exist or the file is not a sound. |

See also: [`rq.sound.stop`](rq.sound.md#rqsoundstop)

### rq.sound.play_flash

```lua
rq.sound.play_flash(key, opts) -> integer|nil
```

`since 1.4.0`

Plays a sound kept inside a Flash file.

Some game sounds have no number, such as Berserk's in `Data/Flash/Battle/狂戦士発動.swf`. A bare key
means `Data/Flash/System/<key>.swf`, as in `rq.image.add_gif`, and a GIF added under that key is
looked at first. Only uncompressed (PCM) sounds play. Raises an error when the file or that sound
is missing, the sound is compressed, `index` is below 1, or 32 mod sounds already play.

| Parameter | Type | Description |
| --- | --- | --- |
| `key` | `string` | The Flash file's key or path. |
| `opts` *(optional)* | [`rq.SoundOpts`](../types/rq.SoundOpts.md) | How to play it; `index` picks the sound. |

| Returns | Type | Description |
| --- | --- | --- |
| `handle` | `integer\|nil` | The handle, or nil when the sound did not start. |

See also: [`rq.sound.flash_info`](rq.sound.md#rqsoundflash_info)

### rq.sound.flash_info

```lua
rq.sound.flash_info(key) -> rq.FlashSound[]|nil
```

`since 1.4.0`

Lists the sounds in a Flash file.

```lua
for i, s in ipairs(rq.sound.flash_info("Data/Flash/Battle/狂戦士発動.swf") or {}) do
  rq.log(i, s.ms, s.playable)
end
```

| Parameter | Type | Description |
| --- | --- | --- |
| `key` | `string` | The Flash file's key or path, as for `play_flash`. |

| Returns | Type | Description |
| --- | --- | --- |
| `sounds` | [`rq.FlashSound`](../types/rq.FlashSound.md) `[]\|nil` | The sounds, in the order `index` counts them; nil when there is no such file. |

### rq.sound.stop

```lua
rq.sound.stop(handle, fade_ms) -> boolean
```

`since 1.4.0`

Stops a sound, at once or with a fade out.

| Parameter | Type | Description |
| --- | --- | --- |
| `handle` | `integer` | A handle from `play` or `play_flash`. |
| `fade_ms` *(optional)* | `integer` | The fade out, in milliseconds. Default 0: stop at once. |

| Returns | Type | Description |
| --- | --- | --- |
| `stopped` | `boolean` | false when the handle already ended. |

### rq.sound.playing

```lua
rq.sound.playing(handle) -> boolean
```

`since 1.4.0`

Returns whether a sound still plays.

An ended handle stays false, even when its slot plays something new.

| Parameter | Type | Description |
| --- | --- | --- |
| `handle` | `integer` | A handle from `play` or `play_flash`. |

| Returns | Type | Description |
| --- | --- | --- |
| `playing` | `boolean` | true while it plays. |

### rq.sound.set_volume

```lua
rq.sound.set_volume(handle, volume, fade_ms) -> boolean
```

`since 1.4.0`

Changes a sound's volume, at once or over a fade.

| Parameter | Type | Description |
| --- | --- | --- |
| `handle` | `integer` | A handle from `play` or `play_flash`. |
| `volume` | `integer` | The new volume, 0 to 100, clamped. |
| `fade_ms` *(optional)* | `integer` | The fade, in milliseconds. Default 0: at once. |

| Returns | Type | Description |
| --- | --- | --- |
| `changed` | `boolean` | false when the handle already ended. |
