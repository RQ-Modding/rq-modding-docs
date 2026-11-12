# Pictures

`rq.image` shows pictures from your mod where the game shows its own: a new face or standing picture
for a character, a background for a scene, an icon. Since loader 2.25.0 a GIF or an animated WebP
moves wherever the game shows it, and a picture can go inside one of the game's Flash files, such as
a skill cut-in.

## How the game finds a picture

The game shows pictures by **CG number**. A character has a face number and a standing-picture
number, a scene asks for a background by number, an item has an icon number. RQ MOD looks at the
mod's pictures before the game's archive, so a mod has two ways in:

- **`rq.image.replace(no, path)`** puts a file behind one of the game's numbers. Everything that shows
  that number shows the file. The file is scaled to the game's picture size unless `opts` says
  otherwise.
- **`rq.image.add(key, path)`** gives a file a new number of its own, the same every time the game
  starts, so a save can keep it. Use it for a mod's own character, item or scene.

```lua
local SEA = rq.image.add("mymod:sea", "bg/sea.png", { w = 1024, h = 768, fit = "cover" })
rq.image.replace(2000, "faces/rance.png", { fit = "contain" })  -- Rance's face
```

A character's `face` and `portrait` in `rq.chara.define`, `edit` and `set` take a path too.
Faces are 196×232 and standing pictures 1024×768; the file keeps its proportions inside that size.

```lua
rq.chara.edit(52, { face = "faces/kaoru.png" })  -- 52 is Kaoru (rq.ids.chara)
```

`rq.image.info(no)` gives a number's size and whether a mod's picture is on it. Read the size of a
game picture there before you draw one for it. To find a picture's number, look through them all
in [RQ Browser](./file-browser) (`rq-browser.exe` in the game's `xsystem4` folder): it shows each
CG with its number, size and what uses it, gives the `rq.image.replace` line and saves PNGs. With
the game running, `rqmod-ctl cgdump FROM TO DIR` saves a range of them too.

## Moving pictures

A **GIF** or an **animated WebP** is a moving picture. Give it to `add`, `replace`, `face` or
`portrait` as you would a PNG:

```lua
rq.chara.edit(52, { face = "faces/kaoru_blink.webp" })
local SEA = rq.image.add("mymod:sea", "bg/sea.gif", { w = 1024, h = 768, fit = "cover", fps = 12 })
```

Its first frame is the picture the game reads; the frames play wherever the game shows the picture
whole:

- in scenes: the background, the standing picture, the face beside a line, and event CGs;
- on character cards: the town's party bar, the Party screen, the status page and fights.

Animated WebP has full color and soft edges; GIF has 256 colors and on-or-off transparency. Both play
at the file's own speed, or at `fps` frames a second. `clock = "real"` keeps that speed when the
game runs faster with `rq.speed`.

`rq.image.info(no)` gives `frames`, `ms` (one loop) and `drawn`, which says the game drew the moving
frames in the last quarter second. Use `drawn` to check where your picture moves.

```lua
local i = rq.image.info(SEA)
rq.log(i.frames, i.ms, i.drawn)
```

## Pictures inside the game's Flash files

Skill cut-ins, battle effects and the marks on fight cards are **Flash files**, with their pictures
inside them. `rq.image.flash_bitmap(file, id, path)` puts your picture in place of one of those
pictures. It is fitted to the same size, so the file moves, fades and blends it as it did the old
one: a new face in a cut-in slides in as the old one did.

**1. Find the pictures.** [RQ Browser](./file-browser)'s Flash tab shows every Flash file's pictures
with their ids and sizes, and saves them. With the game running, `rqmod-ctl` saves a file's pictures
with their ids too:

```
rqmod-ctl flashdump カットイン・チハ C:\temp\chiha
```

That writes `<id>_<w>x<h>.png` for each picture (`28_300x170.png` and so on). A bare name is a file in
`Data/Flash/System`; give the full name for others, such as
`Data/Flash/Battle/全体・毒ガスブレス.swf`. In a mod, `rq.image.flash_bitmaps(file)` lists the same ids
and sizes.

**2. Draw yours at the same size**, and put it in place:

```lua
rq.image.flash_bitmap("カットイン・チハ", 28, "cutin/chiha.png")
rq.image.flash_bitmap("カットイン・チハ", 19, "cutin/chiha_white.png")
```

A Flash file is often the same picture several times, once per frame of its motion (the poison mark
has five). Replace each of them.

The game loads a Flash file when it plays it, so the next time the cut-in or mark plays it shows
yours. `rq.image.flash_bitmap(file, id, nil)` gives the game's picture back.

## Things to know

- **A moving picture is still** where the game copies part of the picture or draws on it, such as
  the small faces in a fight's turn order, and in `rq.image.compose`, `rq.hud` and `rq.sprite`'s `cg`.
  `rq.sprite`'s `gif` plays a file on a mod's own sprite.
- **Fight cards** take a face per fight with `rq.battle.set_face`, which wins over the character's
  moving face while it is set.
- **Flash pictures are still pictures.** A GIF for a whole Flash file goes through
  `rq.image.add_gif`, and a mark with `rq.battle.set_mark`; then the game's file, and the pictures you
  put in it, are not played.
- **Enemies and fight backgrounds** are 3D models, not pictures by number. `rq.image` cannot reach them.
- **Limits:** 256 mod pictures; 64 moving pictures, with 1024 frames each and 64 million pixels in
  all; a GIF up to 1024 pixels a side and a WebP up to 4096; 256 Flash pictures and 32 million pixels.
  Past a limit the call raises an error, as it does for a file it cannot read, so you see it when the
  mod loads.
- **A path is looked up in the folder of the mod whose code calls `rq.image`**, as for
  [music](music.md#things-to-know).
