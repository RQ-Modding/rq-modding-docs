# Scenes

A scene is the game's dialogue: lines under a face, narration, pictures behind them, music, and
choices. A mod writes one in two ways:

- **In Lua**, with [`rq.scene.play`](../reference/api/rq.scene.md) and the calls of the scene's
  `s` (since loader 0.18.0).
- **As a file**, a JSON file in the mod's folder that RQ MOD plays (since loader 2.60.0). It needs
  no code for the lines, other programs can read and write it, and the coming scene editor opens it.
  Its Lua calls only what only Lua knows, through functions the mod names.

Both play the same way: over the current screen (the hub, a quest's map, the castle), taking the
clicks, with the game's read flags (skip mode passes only lines the player has read). Faces,
backgrounds and music are the game's CG and music numbers; [Rance Browser](file-browser.md) shows
them with their numbers. A face can also be a picture of the mod's own ([Pictures](pictures.md)).

## A scene in Lua

```lua
rq.scene.play(function(s)
  s.set(0, 5240, 0, 0)                  -- a background
  s.music(72)
  s.say(2310, "\"We are back here again?\"")
  s.say(2000, "\"The loot was good last time.\"")
  s.think(2000, "(This is going to be a long day.)")
  s.say(2310, "\"Which way?\"", { wait = false })
  local pick = s.choice({ "Left", "Right" })
  s.clear_text()
  s.narrate(pick == 1 and "They go left." or "They go right.")
end)
```

`rq.scene.play` waits until the scene ends and returns what the function returns. From
`rq.on_frame`, a callback or anywhere else, `rq.scene.start` plays it at the next frame in a
coroutine of its own and returns at once; `rq.scene.once(flag, fn)` plays it once per save. The
[reference](../reference/api/rq.scene.md) lists every call of `s`.

## A scene as a file

Set `loader` to `2.60.0` in `mod.json`. A scene file goes in the mod's folder, by convention
`scenes/<name>.json`:

```json
{
  "$schema": "https://rq-modding.github.io/rq-modding-docs/schemas/scene.schema.json",
  "format": 1,
  "cast": {
    "pluepet": { "face": 2816 },
    "rance": { "face": 2005 }
  },
  "steps": [
    { "set": { "wallpaper": 5510, "background": 5280 } },
    { "music": 93 },
    { "say": "pluepet", "text": "\"Hellooo! Mr. Rance, the Pluepet Company has found your {item}!\"" },
    { "say": "rance", "text": ["\"About time.\"", "\"Next time, be quicker.\""] },
    { "end": "clear" }
  ]
}
```

```lua
rq.scene.play(rq.scene.file("scenes/delivery.json", { vars = { item = "Lens" } }))
```

`rq.scene.file` takes a path in the mod's folder and gives a scene file, which `rq.scene.play`,
`once` and `start` take in place of a function. It reads nothing: the file is read and checked each
time it plays, so an edit shows at the next play, with no reload.

The `$schema` line points at the format's specification, the
[scene schema](/schemas/scene.schema.json). With it, VS Code checks the file as you type, completes
the steps' names and options, and shows what each one does on hover. A file has:

| Field | |
| --- | --- |
| `format` | `1`. RQ MOD plays every format it knows and refuses a newer one, saying so. |
| `steps` | The scene, played in order. |
| `once` | Optional. An event flag: the scene plays once per save, as `rq.scene.once`. |
| `cast` | Optional. Names for faces ([The cast](#the-cast)). |

### Steps

Each step is an object named by its one step key, which holds its main value; its options sit
beside it. One step per object.

| Step | Example | What it does |
| --- | --- | --- |
| `say`, `think` | `{ "say": 2310, "text": "\"Hey.\"" }` | A character's line, or thought. The face is a CG number, a [cast](#the-cast) name or a picture path. Options: `name` (the name plate), `hide_face`, `page` (the game's E frame), `wait` (false: no click, as above a choice). |
| `narrate` | `{ "narrate": "The bathhouse is quiet." }` | Narration. Options: `paper` (the paper frame), `page`, `wait`. |
| `clear_text` | `{ "clear_text": true }` | Clears the message window. |
| `speed` | `{ "speed": 0 }` | The text speed, in milliseconds per character. |
| `background`, `wallpaper`, `mask_wallpaper`, `portrait`, `mini`, `cg` | `{ "background": 5280, "effect": 1, "time": 500 }` | A picture on that layer: a CG number or a picture path. `effect` is the game's transition, `time` its length in milliseconds. |
| `background_in`, `background_out` | `{ "background_out": true, "time": 800 }` | A background coming in, or going. |
| `set` | `{ "set": { "wallpaper": 5510, "background": 5280 } }` | Several layers at once (`wallpaper`, `background`, `portrait`, `mini`, `cg`), with an `effect`. |
| `black`, `white`, `clear` | `{ "black": true, "time": 800 }` | The screen to black or white, or cleared. |
| `flash`, `shake`, `shake_face`, `shake_portrait` | `{ "shake": true }` | A flash, or a shake (`mode`). |
| `music`, `sound`, `jingle` | `{ "music": 93 }` | Music by number (`effect`, `time` for its fade), a sound, a jingle (`wait`). |
| `wait_click` | `{ "wait_click": true }` | Waits for a click. |
| `world_map` | `{ "world_map": 1 }` | The game's world map with a place's tag, as a quest's start shows it: a place of the game's (1 to 40; 1 is Cidade), or a point of the mod's own, `{ "x": 640, "y": 300, "name": "Our Camp" }`. A click goes on, and the pictures and the message window are cleared after it. Since RQ MOD 2.62.0. |
| `choice` | [Choices](#choices) | The game's choice menu. |
| `if` | [Conditions](#conditions) | Steps that play when a condition holds (`then`), or else (`else`). |
| `flag`, `unflag` | `{ "flag": "mymod:met_mira" }` | Sets or clears an event flag, as `rq.scene.seen`. |
| `call` | `{ "call": "deliver", "args": [1], "into": "item" }` | A function of the mod ([The mod's functions](#the-mods-functions)). |
| `label`, `goto` | `{ "label": "ask" }`, `{ "goto": "ask" }` | A place in the file, and a jump to it, also into or out of nested steps. |
| `end` | `{ "end": "clear" }` | Ends the scene. Its value is what `rq.scene.play` returns. |
| `cmd` | `{ "cmd": "字色", "args": [255, 200, 200] }` | Any game command, as `rq.scene.cmd`. |
| `note` | `{ "note": "A comment." }` | Does nothing: a comment for whoever reads the file. |

### Lines and pages

The game's lines are speech in quotes, so a line in JSON has them escaped: `"\"Hello.\""`. `\n`
breaks a line in the window. A `text` (or `narrate`) that is a list is one page per entry, each
waiting for a click, the way the game writes a long line:

```json
{ "say": "magic", "text": ["\"Fine.\nBut only one more round.\"", "\"Then we go home.\""] }
```

`wait: false` shows the last page without waiting, as the game does for a question above its menu.

### The cast

`cast` gives faces names, so a line reads `{ "say": "mira", ... }`. Each name has a `face` (a CG
number or a picture path) and optionally a `name`, shown on the name plate. A character's other
looks are more names:

```json
"cast": {
  "pluepet": { "face": 2816 },
  "mira": { "face": "faces/mira.png", "name": "Mira" },
  "mira_angry": { "face": "faces/mira_angry.png", "name": "Mira" }
}
```

A step's own `name` replaces the cast's for that line. A picture path is added with `rq.image.add`
under a key of the mod, so each picture takes one of the 256 mod images.

### Choices

```json
{ "say": "pluepet", "text": "\"Which one shall we track down?\"", "wait": false },
{ "choice": [
    { "text": "The steam room", "steps": [ { "narrate": "Hot. Very hot." } ] },
    "-",
    { "text": "The cold pool", "comment": "Brr.", "if": { "seen": "mymod:pool" }, "goto": "pool" },
    { "text": "Leave", "end": "abandon" }
  ], "into": "pick" }
```

A row has a `text`, and optionally a `comment` (shown in the game's comment window), `r`, `g`, `b`
(its color), a `sound`, an `id`, an `if` (the row shows only when the condition holds), and where it
goes: its own `steps` (then the scene goes on after the choice), a `goto`, or an `end`. A row that is
only a text has no way of its own: the scene goes on. `"-"` is a separator line. `into` keeps the
pick's id in a variable; a row's id is its place in the list, from 1, unless it has one. The menu
cannot be cancelled. `x` and `y` place it.

Rows only Lua can build come from a function: `{ "choice": { "call": "lost_items" }, "into":
"pick" }` shows the rows the function returns, as `s.choice` takes them.

### Conditions

```json
{ "if": { "all": [ { "gold": 100 }, { "not": { "seen": "mymod:paid" } } ] },
  "then": [ { "say": "teller", "text": "\"Well, traveller?\"" } ],
  "else": [ { "say": "teller", "text": "\"Come back later.\"" } ] }
```

| Condition | Holds when |
| --- | --- |
| `{ "seen": "mymod:met" }` | The event flag is set (a mod's, or one of the game's). |
| `{ "var": "pick", "is": 2 }` | A variable is that value; `at_least` and `at_most` compare numbers. `"is": null` holds for a variable not set. |
| `{ "call": "owned", "args": [412] }` | The mod's function returns anything but nil and false. |
| `{ "not": c }`, `{ "all": [c, ...] }`, `{ "any": [c, ...] }` | |
| `{ "cleared": 126 }` | A quest was cleared at least once. |
| `{ "recruited": "Kaoru Quincy" }` | A character is in the roster. |
| `{ "in_party": "KAORU_QUINCY" }` | A character is in the party. |
| `{ "has_item": 412 }` | The player has the item: worn, in the vault or in the storage. |
| `{ "gold": 50000 }` | The player has at least that much gold. |
| `{ "chance": 30 }` | A roll of 30 in 100. |

A quest, a character or an item is a number, a name or key as [`rq.ids`](ids.md) gives it, or the
id of one a mod defined (`"mymod:lotion"`). Anything else is a function's job.

### Variables in text

`{name}` in a line, a name plate, a row's text or comment takes the variable `name`: one set by
`into` (a choice's pick, a function's result), or given at the start in `rq.scene.file`'s `vars`. A
variable that is not set shows as written, and the log names the line. <code v-pre>{{</code> and <code v-pre>}}</code> are
braces.

### The mod's functions

A file calls only the functions its mod names, by name:

```lua
rq.scene.functions({
  found_alone = function(ctx) return rq.item.count(contract_item()) > 0 end,
  deliver = function(ctx, s)
    local ii = rq.item.give(contract_item(), { place = "vault" })
    s.item(ii)                                  -- the game's moment for an item
    return rq.item.get(ii).name                 -- into "item"
  end,
  lost_items = function(ctx)
    return { { id = 11, text = "Boots" }, { id = 12, text = "Gloves" } }
  end,
})
```

Each gets `ctx` first: `ctx.vars` (the file's variables; a change shows in the file), `ctx.path`,
`ctx.step` (the step's place, such as `steps[4].then[1]`) and `ctx.mod`. Then the scene's `s`, so it
can play steps of its own, and the step's `args` (JSON's `null` as nil). What it returns goes to the
step's `into`, decides a `call` condition, or is a choice's rows. An error in a function ends the
scene and is logged with the step's place.

### Labels and goto

`goto` jumps to a `label` anywhere in the file, also inside an `if` or a row's steps: after the
nested steps end, the scene goes on after the step that holds them. A loop is a `goto` back to a
label; one that would show nothing at all (no line, choice or wait) is stopped after 10000 steps.
`rq.scene.file`'s `from` starts the file at a label, or at any step by its place as the problems
name it (`steps[4]`, `steps[3].then[0]`, `steps[2].choice[0].steps[1]`, from 0; since 2.61.0). From
a step inside an `if`'s branch or a choice's row, the rest of that list plays, then the steps after
the `if` or the choice, as if the branch had been taken.

### A quest's run

`end`'s value is what `rq.scene.play` returns, so a [quest's](new-quests.md) `run` can end as the
file says:

```lua
rq.quests.define({
  id = "mymod:lotion_quest", name = "The Lost Lotion", open = true,
  run = function(q) return rq.scene.play(rq.scene.file("scenes/bathhouse.json")) end,
})
```

```json
{ "format": 1, "steps": [
  { "narrate": "The bathhouse is quiet. Two doors lead on.", "wait": false },
  { "choice": [
      { "text": "The steam room", "steps": [
          { "narrate": "A small bottle shines on the bench." },
          { "call": "give_lotion" },
          { "end": "clear" } ] },
      { "text": "The cold pool", "steps": [
          { "narrate": "Only cold water here. Nothing to find." },
          { "end": "abandon" } ] }
  ] }
] }
```

A scene file can also play inside a Lua scene: `rq.scene.file("scenes/intro.json")(s)` plays its
steps there and returns its `end` value.

### Problems

A file with problems does not play: each problem is logged with its place, and the scene does not
open (from `rq.scene.play`, it returns nothing). `rq.scene.check(path)` gives them without playing:

```lua
for _, p in ipairs(rq.scene.check("scenes/delivery.json")) do rq.log(p) end
```

```
scenes/delivery.json: steps[4].then[0].say: "pluepett" is not in the file's cast
scenes/delivery.json: steps[6]: "say" has no field "txt"
```

The checks are those of the schema, and what a schema cannot say: each `goto`'s label, each label
once, each function named by `rq.scene.functions`, each game name, and each picture's file.

### Playing a file from outside

`rqmod-ctl playscene MOD FILE [FROM] [name=value ...]` plays a mod's scene file in the running
game, read anew, as `rq.scene.start` would: from FROM when given (a label or a step's place), with
the file's values (`vars`) given as `name=value`, each a whole number, a number with a decimal
point, `true`, `false`, or else the text as written (since 2.61.0). It answers `ok`, `err busy`
while a mod scene plays or waits to, or the file's problems, one per line. `rqmod-ctl playscene stop`
ends it before its next step. The scene editor's Play button and agents use it; the file's functions
run for real, so play on a save you can lose.

```powershell
.\xsystem4\rqmod-ctl.exe playscene mymod scenes/delivery.json
.\xsystem4\rqmod-ctl.exe playscene mymod scenes/delivery.json "steps[2].choice[0].steps[1]" alone=true "item=Iron Sword"
```

`rqmod-ctl playscene status` says what plays (since 2.61.0): `idle`, `waiting MOD FILE` while the
file waits for the game to let it in, or a line per file that plays, the outermost first, as
`playing MOD FILE PLACE`, PLACE the step that plays or waits for a click or a pick:

```
playing mymod scenes/delivery.json steps[2].choice[0].steps[1]
```

`rqmod-ctl scenefunctions MOD` gives `ok`, then the names the mod gave `rq.scene.functions`, one per
line (since 2.61.0).
