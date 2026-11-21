# rq.image

`since 0.6.0` `changed 2.25.0` `changed 2.63.0`

Images from a mod's folder, shown by the game as CGs.

The engine checks these before the game's archives, so sprites, parts and every game call see the
mod image. Paths are inside the mod's folder. Formats: PNG (with alpha), JPEG and WebP, the game's
QNT, AJP and PMS, and since 2.25.0 GIF and animated WebP as moving pictures. Face cards are 196×232
and standing pictures 1024×768. `face` and `portrait` in `rq.chara.define`, `edit` and `set` take a
path too: a base-game character's own CG is replaced, because screens keep the number they read. A
save keeps a mod image's number; without the mod it shows no picture there.

A moving picture's first frame is the CG. The game shows the frames wherever it shows the CG whole:
a scene's background, standing picture, face and event CG, and the faces on character cards (the
town's party bar, the Party screen, the status page, and fights, where `rq.battle.set_face` wins).
Where the game copies part of the CG or draws on it, and in `compose`, `rq.hud` and `rq.sprite`
(`cg`), it is the still; `rq.sprite`'s `gif` plays a file there. Every frame is fitted as the still
is. Up to 64 moving pictures, 1024 frames each and 64 million pixels in all.

`flash_bitmap` puts a still picture on a bitmap inside one of the game's Flash files, such as a
cut-in or a battle effect (2.25.0).

A mod's own Flash animations (2.63.0): `add_flash` takes an `.aff` or a SWF from the mod's folder,
under a game file's name to replace it (a skill's effect, a mark) or under a new one, and
`play_flash` plays one on screen. `rqmod-aff build` (in the game's `xsystem4` folder) makes an
`.aff` from PNG frames and WAV sounds, and `rqmod-aff check` says what in a file the game would not
play.

```lua
rq.chara.define({ id = "mymod:alice", name = "Alice", face = "faces/alice.png", class = 1 })
rq.chara.edit(52, { face = "faces/kaoru.gif" })  -- a new, moving face for Kaoru
rq.image.replace(2000, "faces/rance.webp", { fit = "cover" })
```

## Functions

| Name | Summary |
| --- | --- |
| [`rq.image.add`](#rqimageadd) | Registers a file from the mod's folder as a new CG number. |
| [`rq.image.replace`](#rqimagereplace) | Shows a file wherever the game uses one of its CG numbers. |
| [`rq.image.restore`](#rqimagerestore) | Undoes `rq.image.replace` or a `compose` on a game CG. |
| [`rq.image.info`](#rqimageinfo) | Returns what is on a CG number, and its size. |
| [`rq.image.compose`](#rqimagecompose) | Makes a CG from parts of other CGs, fills and text. |
| [`rq.image.add_gif`](#rqimageadd_gif) | Serves a GIF from the mod's folder as a game Flash file. |
| [`rq.image.remove_gif`](#rqimageremove_gif) | Undoes `rq.image.add_gif`. New loads use the game's file again, if there is one. |
| [`rq.image.gif_info`](#rqimagegif_info) | Returns a GIF's size and length. |
| [`rq.image.flash_bitmap`](#rqimageflash_bitmap) | Puts a picture from the mod's folder on one bitmap of a game Flash file. |
| [`rq.image.flash_bitmaps`](#rqimageflash_bitmaps) | Lists the bitmaps of a game Flash file, as the game has them. |
| [`rq.image.add_flash`](#rqimageadd_flash) | Serves a Flash file from the mod's folder as a game Flash file. |
| [`rq.image.remove_flash`](#rqimageremove_flash) | Undoes `rq.image.add_flash`. New loads play the game's own file again, if there is one. |
| [`rq.image.flash_info`](#rqimageflash_info) | Returns the size, length, pictures and sounds of the Flash file the game plays under a name. |
| [`rq.image.play_flash`](#rqimageplay_flash) | Plays a Flash file once on screen, as the game plays its effects. |

### rq.image.add

```lua
rq.image.add(key, path, opts) -> integer
```

`since 0.6.0` `changed 2.25.0`

Registers a file from the mod's folder as a new CG number.

The number comes from the key (900000 and up), so it is the same every run and safe to keep in a
save. Without `w` and `h` the file keeps its own size. A GIF or an animated WebP is a moving picture
(see `rq.image`); it is read when it is added, so a bad file is an error here.

Raises an error for a file not in the mod's folder, a path outside it, an unknown fit, a too long
key, a key whose number another key has, or past 256 mod images; for a moving picture also for a bad
`fps` or `clock`, a file it cannot read, a GIF over 1024 pixels a side or a WebP over 4096, and the
limits in `rq.image`. A call that raises an error adds nothing, except that a moving picture that
cannot be read takes away the image the key had.

```lua
local ICON = rq.image.add("mymod:icon", "icons/star.png", { fit = "contain", w = 56, h = 56 })
local SEA = rq.image.add("mymod:sea", "bg/sea.webp", { fps = 12 })  -- a moving background
```

| Parameter | Type | Description |
| --- | --- | --- |
| `key` | `string` | A key unique to this image, such as "mymod:alice_face". |
| `path` | `string` | A path inside the mod's folder. |
| `opts` *(optional)* | [`rq.ImageOpts`](../types/rq.ImageOpts.md) | Size and fit. |

| Returns | Type | Description |
| --- | --- | --- |
| `cg` | `integer` | The CG number. |

> Changed in 2.25.0: A GIF or an animated WebP is a moving picture; `opts.fps` and `opts.clock`.

### rq.image.replace

```lua
rq.image.replace(cg, path, opts)
```

`since 0.6.0` `changed 2.25.0`

Shows a file wherever the game uses one of its CG numbers.

The file is scaled to the game CG's size. Screens already built show it when they next load the CG.
A GIF or an animated WebP is a moving picture, as in `add`.

Raises an error as `rq.image.add` does.

```lua
rq.image.replace(10011, "bg/castle_night.gif", { fit = "cover", clock = "real" })
```

| Parameter | Type | Description |
| --- | --- | --- |
| `cg` | `integer` | The game's CG number. |
| `path` | `string` | A path inside the mod's folder. |
| `opts` *(optional)* | [`rq.ImageOpts`](../types/rq.ImageOpts.md) | Fit (default "stretch") and size. |

> Changed in 2.25.0: A GIF or an animated WebP is a moving picture.

See also: [`rq.image.restore`](rq.image.md#rqimagerestore)

### rq.image.restore

```lua
rq.image.restore(cg) -> boolean
```

`since 0.6.0`

Undoes `rq.image.replace` or a `compose` on a game CG.

| Parameter | Type | Description |
| --- | --- | --- |
| `cg` | `integer` | The game's CG number. |

| Returns | Type | Description |
| --- | --- | --- |
| `removed` | `boolean` | false when nothing replaced it. |

### rq.image.info

```lua
rq.image.info(cg) -> rq.ImageInfo
```

`since 0.6.0` `changed 2.25.0`

Returns what is on a CG number, and its size.

Use it to read a game CG's size before drawing art for it. A moving picture also has `frames`, `ms`
and `drawn`.

| Parameter | Type | Description |
| --- | --- | --- |
| `cg` | `integer` | The CG number. |

| Returns | Type | Description |
| --- | --- | --- |
| `info` | [`rq.ImageInfo`](../types/rq.ImageInfo.md) | What the number shows. |

> Changed in 2.25.0: `frames`, `ms` and `drawn` for a moving picture.

### rq.image.compose

```lua
rq.image.compose(target, layers, opts) -> integer
```

`since 1.8.0` `changed 2.5.0` `changed 2.11.0`

Makes a CG from parts of other CGs, fills and text.

It is built when it is first shown. A key gives a new number as `add` does; a game CG number
replaces that CG, and `rq.image.restore` undoes it. The size is `opts.w` by `opts.h`, else the game
CG's own, else the first layer's extent. Other CGs are read as they are when it is built, mod images
included. Calling it again with the same key or number rebuilds it.

A text layer with `font = "game"` is drawn by the game when `compose` is called, or, before the
game runs (in `init.lua`), when the CG is first built.

Raises an error for no layers or more than 256, a layer without `cg`, `text` or `fill`, an unknown
`mode`, or a size it cannot work out (then give `opts.w` and `opts.h`, 1 to 4096), and for a text
layer's style as `rq.hud.text` does.

```lua
local TAB = rq.image.compose("mymod:tab", {
  { cg = 40031, src = { 0, 0, 150, 40 } },
  { text = "Mods", w = 150, h = 40, align = "center", valign = "center" },
})
```

| Parameter | Type | Description |
| --- | --- | --- |
| `target` | `string\|integer` | A key, or a game CG number to replace. |
| `layers` | [`rq.ImageLayer`](../types/rq.ImageLayer.md) `[]` | The layers, back to front. |
| `opts` *(optional)* | `{w?: integer, h?: integer}` | The size. |

| Returns | Type | Description |
| --- | --- | --- |
| `cg` | `integer` | The CG number. |

> Changed in 2.5.0: Text layers take `font = "game"`.

> Changed in 2.11.0: A text layer's `shadow.a`.

### rq.image.add_gif

```lua
rq.image.add_gif(key, path, opts) -> string
```

`since 0.19.0`

Serves a GIF from the mod's folder as a game Flash file.

A bare key means `Data/Flash/System/<key>.swf`; a key with a slash is the full file name. A key
named like a game file replaces it everywhere, such as "タメマーク". It loops at the GIF's own
speed, rounded to 30 frames a second. GIF has 256 colors and on or off transparency. Up to 1024
pixels a side, 1024 frames and 32 million pixels in all.

Raises an error for a bad file.

| Parameter | Type | Description |
| --- | --- | --- |
| `key` | `string` | The Flash file's key. |
| `path` | `string` | A GIF file in the mod's folder. |
| `opts` *(optional)* | [`rq.GifOpts`](../types/rq.GifOpts.md) | The size on screen. |

| Returns | Type | Description |
| --- | --- | --- |
| `key` | `string` | The key. |

### rq.image.remove_gif

```lua
rq.image.remove_gif(key) -> boolean
```

`since 0.19.0`

Undoes `rq.image.add_gif`. New loads use the game's file again, if there is one.

| Parameter | Type | Description |
| --- | --- | --- |
| `key` | `string` | The key. |

| Returns | Type | Description |
| --- | --- | --- |
| `removed` | `boolean` | false when no GIF had that key. |

### rq.image.gif_info

```lua
rq.image.gif_info(key) -> rq.GifInfo|nil
```

`since 0.19.0`

Returns a GIF's size and length.

| Parameter | Type | Description |
| --- | --- | --- |
| `key` | `string` | The key. |

| Returns | Type | Description |
| --- | --- | --- |
| `info` | [`rq.GifInfo`](../types/rq.GifInfo.md) `\|nil` | The GIF, or nil when no GIF has that key. |

### rq.image.flash_bitmap

```lua
rq.image.flash_bitmap(file, id, path, opts)
```

`since 2.25.0` `changed 2.63.0`

Puts a picture from the mod's folder on one bitmap of a game Flash file.

The picture is fitted to the bitmap's size, so the file's placement, motion and blends stay: a new
face in a cut-in moves as the old one did. `file` is named as in `add_gif`: a bare name is
`Data/Flash/System/<name>.swf`, and a name with a slash is the full name. Still pictures only.
New loads of the file show it; a Flash that is playing keeps its bitmap until it loads again. A file
that `add_gif`, `add_flash` or `rq.battle.set_mark` replaced plays the mod's file instead, with none
of the game's bitmaps. A mod's file under a name the game does not have (`add_flash`) takes pictures
on its own bitmaps. `rqmod-ctl flashdump` saves a file's bitmaps with their ids. With `path` nil the
bitmap is the file's own again.

Raises an error for a file that is neither the game's nor added with `add_flash`, an id that is no
bitmap in it, a GIF or an animated WebP, a fit of "none", a picture as `add` does, or past 256
bitmaps or 32 million pixels in all.

```lua
-- A new look for Chiha in her cut-in: her picture and her white silhouette.
rq.image.flash_bitmap("カットイン・チハ", 28, "cutin/chiha.png")
rq.image.flash_bitmap("カットイン・チハ", 19, "cutin/chiha_white.png")
```

| Parameter | Type | Description |
| --- | --- | --- |
| `file` | `string` | The Flash file, as in `add_gif`. |
| `id` | `integer` | The bitmap's id, from `flash_bitmaps`. |
| `path` | `string\|nil` | A still picture inside the mod's folder, or nil for the game's bitmap. |
| `opts` *(optional)* | [`rq.FlashBitmapOpts`](../types/rq.FlashBitmapOpts.md) | The fit. |

> Changed in 2.63.0: A mod's own file from `add_flash`.

### rq.image.flash_bitmaps

```lua
rq.image.flash_bitmaps(file) -> rq.FlashBitmap[]
```

`since 2.25.0` `changed 2.63.0`

Lists the bitmaps of a game Flash file, as the game has them.

Read a bitmap's size here before drawing a picture for it. A mod's file under a name the game does
not have (`add_flash`) is listed too.

Raises an error for a file that is neither the game's nor added with `add_flash`.

```lua
for _, b in ipairs(rq.image.flash_bitmaps("毒マーク")) do
  rq.log(("%d: %dx%d%s"):format(b.id, b.w, b.h, b.mod and " (mod)" or ""))
end
```

| Parameter | Type | Description |
| --- | --- | --- |
| `file` | `string` | The Flash file, as in `add_gif`. |

| Returns | Type | Description |
| --- | --- | --- |
| `bitmaps` | [`rq.FlashBitmap`](../types/rq.FlashBitmap.md) `[]` | In the file's order. |

> Changed in 2.63.0: A mod's own file from `add_flash`.

### rq.image.add_flash

```lua
rq.image.add_flash(key, path) -> string
```

`since 2.63.0`

Serves a Flash file from the mod's folder as a game Flash file.

`path` is an `.aff`, the game's own format, or a SWF, plain (FWS) or compressed with zlib (CWS).
The key is named as in `add_gif`: a bare key means `Data/Flash/System/<key>.swf`, a key with a
slash is the full name, and a key named like a game file replaces that file wherever the game plays
it, such as a skill's effect (`"Data/Flash/Battle/<name>.swf"`, as Rance Browser's Flash tab names
them). A new name plays through `play_flash` or `rq.sprite`'s `flash`. Adding a key again replaces
its file.

The file is checked first by the rules of the game's engine, the same as `rqmod-aff check`: 32-bit
pictures, one picture per shape, uncompressed sound, and the placements, blends and actions the
engine knows. A file the game would not play, or that would close it, is refused and nothing of it
reaches the game; the error names the first problem, where it is, and how many more there are. A
file that plays with warnings (a blend mode drawn as normal, say) is added, and the log says the
first warning. The game plays every Flash file at 30 frames a second, whatever its header says.

Up to 64 MB a file, as it is in the folder and uncompressed, 32 million pixels in its pictures, and
256 MB for all the files added together; 1024 keys with the GIFs and the marks' pictures.

Raises an error for a path outside the mod's folder, a missing or empty file, a key of more than
103 bytes, a file the game would not play, or past the limits.

```lua
-- Made with: rqmod-aff build frames effects/pulse.aff --fps 15 --sound chime.wav
rq.image.add_flash("mymod_pulse", "effects/pulse.aff")
-- A skill's effect replaced, for every fight.
rq.image.add_flash("Data/Flash/Battle/ファイヤーレーザー.swf", "effects/my_fire.aff")
```

| Parameter | Type | Description |
| --- | --- | --- |
| `key` | `string` | The Flash file's key. |
| `path` | `string` | An .aff or .swf file in the mod's folder. |

| Returns | Type | Description |
| --- | --- | --- |
| `key` | `string` | The key. |

See also: [`rq.image.play_flash`](rq.image.md#rqimageplay_flash)

### rq.image.remove_flash

```lua
rq.image.remove_flash(key) -> boolean
```

`since 2.63.0`

Undoes `rq.image.add_flash`. New loads play the game's own file again, if there is one.

A sprite showing the file keeps it until it is removed. A GIF that `add_gif` added under the key goes
too.

| Parameter | Type | Description |
| --- | --- | --- |
| `key` | `string` | The key. |

| Returns | Type | Description |
| --- | --- | --- |
| `removed` | `boolean` | false when no file had that key. |

### rq.image.flash_info

```lua
rq.image.flash_info(key) -> rq.FlashInfo|nil
```

`since 2.63.0`

Returns the size, length, pictures and sounds of the Flash file the game plays under a name.

It reads the file the game would load now: a mod's (`add_flash`, `add_gif`, or a mark from
`rq.battle.set_mark`), else the game's own.

```lua
local info = rq.image.flash_info("Data/Flash/Battle/ファイヤーレーザー.swf")
rq.log(("%dx%d, %d frames, %d ms"):format(info.w, info.h, info.frames, info.ms))
```

| Parameter | Type | Description |
| --- | --- | --- |
| `key` | `string` | The file, named as in `add_gif`. |

| Returns | Type | Description |
| --- | --- | --- |
| `info` | [`rq.FlashInfo`](../types/rq.FlashInfo.md) `\|nil` | The file, or nil when the game has none of that name and no mod added one. |

### rq.image.play_flash

```lua
rq.image.play_flash(key, opts) -> rq.Sprite
```

`since 2.63.0`

Plays a Flash file once on screen, as the game plays its effects.

It is a sprite (`rq.sprite.new` with `flash = key`) that plays from `from` to `to` at 30 frames a
second on the game's clock, and is removed after its last frame has shown. The file's own actions
act (a stop ends the play) and its sounds start at their frames. The key is an `add_flash` key or a
game file's name, as in `add_gif`, so the game's own effects play too. The sprite is the calling
mod's, as any sprite it makes: a load and the title remove it.

Raises an error for a key that is no file, a sprite option as `rq.sprite.new` does, a range outside
the frames, an `on_end` that is not a function, or `wait` outside a job.

```lua
rq.image.add_flash("mymod_pulse", "effects/pulse.aff")
rq.battle.on_start(function()
  rq.image.play_flash("mymod_pulse", { attach = { card = 11 }, z = 20 })  -- over the first enemy
end)
rq.spawn(function()
  rq.image.play_flash("mymod_pulse", { x = 448, y = 320, z = "top", wait = true })
  rq.log("the pulse ended")
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `key` | `string` | An `add_flash` key or a game Flash file's name. |
| `opts` *(optional)* | [`rq.PlayFlashOpts`](../types/rq.PlayFlashOpts.md) | Where, and how it plays. |

| Returns | Type | Description |
| --- | --- | --- |
| `sprite` | [`rq.Sprite`](../types/rq.Sprite.md) | The sprite that plays it, removed at the end unless `loop`. |

See also: [`rq.image.add_flash`](rq.image.md#rqimageadd_flash)
