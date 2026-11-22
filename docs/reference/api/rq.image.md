# rq.image

`since 0.6.0` `changed 2.25.0` `changed 2.63.0` `changed 2.64.0`

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

`texture` puts a PNG, or colors by numbers, on one of the game's 3D textures, wherever a model
uses it: a monster, a prop, a room or a fight background in new colours (2.64.0). `textures` lists
a model's textures.

A PNG of any kind works in every call: 16-bit, grey, a palette, 1 to 4 bits, a see-through colour
(`tRNS`) and interlaced files. A broken one is refused with a reason (2.64.0).

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
| [`rq.image.texture`](#rqimagetexture) | Puts a PNG from the mod's folder, or colors by numbers, on one of the game's 3D textures, wherever a model uses it. |
| [`rq.image.textures`](#rqimagetextures) | Lists the textures a game model uses, as the game has them, with what mods put there. |
| [`rq.image.add_flash`](#rqimageadd_flash) | Serves a Flash file from the mod's folder as a game Flash file. |
| [`rq.image.remove_flash`](#rqimageremove_flash) | Undoes `rq.image.add_flash`. New loads play the game's own file again, if there is one. |
| [`rq.image.flash_info`](#rqimageflash_info) | Returns the size, length, pictures and sounds of the Flash file the game plays under a name. |
| [`rq.image.play_flash`](#rqimageplay_flash) | Plays a Flash file once on screen, as the game plays its effects. |

### rq.image.add

```lua
rq.image.add(key, path, opts) -> integer
```

`since 0.6.0` `changed 2.25.0` `changed 2.64.0`

Registers a file from the mod's folder as a new CG number.

The number comes from the key (900000 and up), so it is the same every run and safe to keep in a
save. Without `w` and `h` the file keeps its own size. A GIF or an animated WebP is a moving picture
(see `rq.image`); it is read when it is added, so a bad file is an error here.

Raises an error for a file not in the mod's folder, a path outside it, an unknown fit, a too long
key, a key whose number another key has, or past 256 mod images; for a moving picture also for a bad
`fps` or `clock`, a file it cannot read, a GIF over 1024 pixels a side or a WebP over 4096, and the
limits in `rq.image`. A call that raises an error adds nothing, except that a moving picture that
cannot be read takes away the image the key had.

A still picture is read at its first use. Any kind of PNG works (see `rq.image`); a PNG with a
see-through colour (`tRNS`) shows it see-through. A still picture that cannot be read then, or one
over 16384 pixels a side, is not drawn and the log says why.

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

> Changed in 2.64.0: Every kind of PNG; a see-through colour; at most 16384 pixels a side.

### rq.image.replace

```lua
rq.image.replace(cg, path, opts)
```

`since 0.6.0` `changed 2.25.0` `changed 2.64.0`

Shows a file wherever the game uses one of its CG numbers.

The file is scaled to the game CG's size. Screens already built show it when they next load the CG.
A GIF or an animated WebP is a moving picture, as in `add`.

Raises an error as `rq.image.add` does, and reads the picture as `add` does.

```lua
rq.image.replace(10011, "bg/castle_night.gif", { fit = "cover", clock = "real" })
```

| Parameter | Type | Description |
| --- | --- | --- |
| `cg` | `integer` | The game's CG number. |
| `path` | `string` | A path inside the mod's folder. |
| `opts` *(optional)* | [`rq.ImageOpts`](../types/rq.ImageOpts.md) | Fit (default "stretch") and size. |

> Changed in 2.25.0: A GIF or an animated WebP is a moving picture.

> Changed in 2.64.0: Every kind of PNG; a see-through colour; at most 16384 pixels a side.

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

`since 2.25.0` `changed 2.63.0` `changed 2.64.0`

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
bitmap in it, a GIF or an animated WebP, a fit of "none", a picture as `add` does, a picture that
cannot be read (with the reason) or over 16384 pixels a side, or past 256 bitmaps or 32 million
pixels in all.

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

> Changed in 2.64.0: Every kind of PNG; a picture that cannot be read is refused with its reason.

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

### rq.image.texture

```lua
rq.image.texture(texture, picture)
```

`since 2.64.0`

Puts a PNG from the mod's folder, or colors by numbers, on one of the game's 3D textures, wherever
a model uses it.

`texture` is the texture's path in the game's archive, as Rance Browser's 3D tab and
`rq.image.textures` show it: "Data/PolyData/Chara/gokiburi/gokiburi.png". Slashes either way and
any ASCII case work. It must be a texture its folder's model names, by its base name (a frame such
as `face[1].png` is given in a list on `face.png`), and a file the game has. The folders hold what
the game draws in 3D: `Chara` the fight monsters, the gold bags, the map's player figure and the
girls' room, `Etc` the map's props, `Map` the rooms and `BG` the fight backgrounds.

`picture` is a PNG inside the mod's folder, or, for a colour texture the game animates, a list of
PNGs, one per frame, as many as the game has (`rq.image.textures`' `frames`). Any kind of PNG
works, up to 4096 pixels a side. A picture of another size than the game's is drawn over the same
UVs, so keep the proportions. The game's alpha kind stays: on a texture the game draws solid the
picture is drawn solid, and a picture without alpha on a texture with alpha takes the game's alpha,
so the model's see-through parts stay where they were.

`picture` may also be colors by numbers, `{ hue = 200, saturation = 1.1, lightness = 0.9 }`: the
game's own picture, every frame, with its colors changed in HSL. Grey, white and black stay grey:
hue and saturation move coloured points only, and lightness scales every point; to colour a grey
monster, paint a picture. Colors change colour textures only. With `picture` nil the texture is the
game's own again, whichever mod changed it.

On one path the last call wins, whichever mod made it, and a mod's model's own textures
(`rq.monster.model`'s `textures`) stay over it. The log names each change. A change made at a mod's
top level shows from the first load. A change made while the game runs shows the next time the game
loads a model with that texture and holds no copy of the model: in a fight, from the next fight's
monsters; on a quest's map, from the next area (an area loads every prop on it with the area, seen
or not); in the girls' room, at the next visit. A copy loaded meanwhile beside one the game holds,
such as a chest placed beside another, has the old pictures too. A fight background keeps its
pictures while fights follow on it, until a fight on another background, the quest's end, a load or
a restart. Only the file's name is kept: each load reads the file again, and a file gone or broken
by then logs a warning and the game's picture is drawn.

Raises an error for a path that is not a text or holds a `*`, a folder with no model, a name that is
not one of its model's textures, a frame's name, a file the game lacks, a picture that is neither a
PNG's path, a list of them nor colors, a list with a hole or an item that is not a text, a number of
pictures other than the texture's frames, a picture outside the mod's folder, not found, not a PNG,
that cannot be read or over 4096 pixels a side, colors out of range, an unknown field or none, colors
on a texture that is not a colour texture, or past 4096 changed textures in all (a list counts each
frame, colors count one). A call that raises an error changes nothing.

```lua
-- The Cockroach in the mod's own colours, wherever the game draws it.
rq.image.texture("Data/PolyData/Chara/gokiburi/gokiburi.png", "textures/roach.png")
-- The goldfish's body in blue, by numbers.
rq.image.texture("Data/PolyData/Chara/kingyo/karada.png", { hue = 180 })
```

| Parameter | Type | Description |
| --- | --- | --- |
| `texture` | `string` | The texture's path in the game's archive. |
| `picture` | `string\|string[]\|` [`rq.TextureColors`](../types/rq.TextureColors.md) `\|nil` | A PNG inside the mod's folder, a list of PNGs for a texture with frames, colors by numbers, or nil for the game's own. |

### rq.image.textures

```lua
rq.image.textures(model) -> rq.TextureInfo[]|nil
```

`since 2.64.0`

Lists the textures a game model uses, as the game has them, with what mods put there.

`model` is a folder in the game's archive, such as "Data/PolyData/Map/dk_a01", or a monster model
number from `rq.monster.models` (100122 is the Cockroach, in `Data/PolyData/Chara/gokiburi`). A
mod's model number gives its base's textures with the model's own over them. The rows come in the
model's order, one per texture, a texture's frames folded into it. For a row without `own`,
`rq.image.texture(r.path, r.picture or r.colors)` makes its change again; an `own` row's change is
made again through `rq.monster.model`, with `textures[r.name] = r.picture or r.colors` in its
model's definition.

Returns nil for a folder or a number with no model, so a loop over `rq.monster.models()` works.
Raises an error for a model that is neither a text nor a whole number, or a path that holds a `*`.

```lua
for _, t in ipairs(rq.image.textures(100122) or {}) do
  rq.log(("%s %s %dx%d%s"):format(t.name, t.kind, t.w or 0, t.h or 0, t.mod and (" by " .. t.mod) or ""))
end
-- New colours on every colour texture of a model, wherever the game draws it.
for _, t in ipairs(rq.image.textures("Data/PolyData/Chara/kingyo") or {}) do
  if t.kind == "color" and not t.missing then rq.image.texture(t.path, { hue = 180 }) end
end
```

| Parameter | Type | Description |
| --- | --- | --- |
| `model` | `string\|integer` | A folder in the game's archive, or a monster model number. |

| Returns | Type | Description |
| --- | --- | --- |
| `textures` | [`rq.TextureInfo`](../types/rq.TextureInfo.md) `[]\|nil` | The model's textures, or nil when there is no model. |

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

A file in the place of one of the game's keeps that file's size (`flash_info` gives it): the game
places its files by their own size, and a battle effect's stage, 400 by 400 for most, is placed
over its target with the picture in its middle. A file of another size is drawn off that place, and
the log says so; `rqmod-aff build --size 400x400` puts smaller frames in the middle of the stage.

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
-- A skill's effect replaced, for every fight; made at the game file's 400 by 400:
-- rqmod-aff build fire_frames effects/my_fire.aff --size 400x400
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
