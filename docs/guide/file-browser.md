# Looking through the game's files

RQ Browser (`rq-browser.exe`, with loader 2.43.0) is a window over the game's own files: its
pictures, Flash files, music, sounds and 3D textures, and the names `rq.ids` gives. Find what you
want to change, read its number, copy the Lua line that replaces or plays it, and save the file to
look at or draw over.

![The CGs tab: Rance's face, CG 2000, with its details and the Lua line that replaces it](/browser/cgs.png)

## Opening it

`rq-browser.exe` is in the game's `xsystem4` folder, beside `xsystem4.exe`. Double-click it: it
opens the game folder above it. Run from somewhere else, it asks for the game folder once and
remembers it in `rq-browser.json` beside it. To name a folder:

```
rq-browser.exe --game "D:\Games\Rance Quest Magnum"
```

It only reads the game's archives and never changes the game's files, so the game may run at the
same time. The one file it writes there is its own `rq-browser.json`, beside it.

On a screen that Windows scales (125 %, 150 %), the text and the panels grow with the scale and stay
sharp. For another size, start it with `--scale`, from 1 to 4:

```
rq-browser.exe --scale 1.25
```

## The tabs

| Tab | What it lists | The Lua line it gives |
| --- | --- | --- |
| CGs | The 2,315 pictures by CG number, in the game's folders: faces, standing pictures, scene CGs, backgrounds, the interface | `rq.image.replace(no, "pictures/no.png")` |
| Flash | The 412 Flash files (battle effects, monster attacks, cut-ins, the interface), each with its pictures and sounds | `rq.image.flash_bitmap(file, id, path)`, `rq.image.flash_bitmaps(file)`, `rq.sound.play_flash(file, { index = n })` |
| Music | The 72 tracks with the game's names, played with their loops | `rq.music.replace(no, "music/no.ogg")`, `rq.music.play(no)` |
| Sounds | The 140 sound effects | `rq.sound.play(no)` |
| 3D textures | The 5,351 textures of the 3D models: characters, map rooms, backgrounds | none yet |
| Names | Every `rq.ids` list, with each name's key and the game's picture for it | `rq.ids.chara.RANCE` and so on |

Each Lua line has a **Copy** button. The paths in it are examples: put your file where the path
says, in your mod's folder, or change the path.

**Finding things.** The search box takes a number or a name; English letters match in any case.
In the CGs tab a name is what a picture is used as ("Rance: face", "Alkanese Rize: standing
picture"), so searching *face* or a character's name finds their pictures. The folder list narrows
the CGs and the textures. Up and Down go to the next one, Page Up and Page Down by a page.

**Looking closely.** In the CGs and 3D textures tabs, **Grid** shows thumbnails; double-click one to
view it. In the view the mouse wheel zooms around the pointer, dragging moves the picture, **Fit**
and **100%** set the size. From 200 % each pixel is a sharp square. A checkerboard shows through
the see-through parts.

**Listening.** In the Music and Sounds tabs, double-click a row or press **Space** to play. The
seek bar shades a track's loop: with **Loop as the game does** on, the track goes back to the loop's
start at its end, as in the game. The details give the loop points in seconds and in sample frames.
Opening another tab stops what plays.

![The Music tab: track 3 with its loop on the seek bar and its Lua lines](/browser/music.png)

**Flash files.** A Flash file's pictures have ids; the tab shows each one with its id and size,
which is what [`rq.image.flash_bitmap`](./pictures#pictures-inside-the-game-s-flash-files) needs, and
the file's key as the Lua calls take it (a bare name for a file in `System`, the full path for the
others). Its sounds play when the file stores them plainly; a compressed one is marked so. The
motion itself is not played.

**Names.** The Names tab lists each `rq.ids` kind with its numbers, keys and details. A character
shows its face, an item its icon; **Open in the CGs tab** goes to that picture.

![The Names tab: the characters with their faces](/browser/names.png)

## Saving

- **Save as PNG** (pictures, Flash pictures, textures) or **Save as OGG** (music and sounds, the file
  as the game stores it).
- **Save the N shown as PNG** saves everything the list shows into a folder you pick, with a
  progress bar and Cancel. Narrow the list first: a folder, or a search. Textures go into
  `folder\model\name.png`.
- **Save all N pictures** in the Flash tab saves a file's pictures as `<id>_<w>x<h>.png`, the names
  [`rqmod-ctl flashdump`](./pictures#pictures-inside-the-game-s-flash-files) uses.

The game's files belong to AliceSoft. Keep the saved copies for your own work, and share only what
you made.

## From a script

```
rq-browser.exe --check [--out report.json]
rq-browser.exe --shot cgs shot.png [--select 2000]
rq-browser.exe --help
```

`--check` opens every archive, decodes some of each kind, reads every track's loop and every
sound, and prints a report in JSON; it ends with 0 when all went well. `--shot` saves one tab
(`cgs`, `flash`, `music`, `sounds`, `textures` or `names`) as a PNG, with `--select` choosing the
number, row or kind shown, `--size WxH` the picture's size and `--scale` the layout's (1 unless
given).
