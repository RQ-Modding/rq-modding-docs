# rq.scene

`since 0.18.0` `changed 1.3.1` `changed 1.13.0` `changed 2.60.0`

Plays scenes with the game's own commands, so a mod can do anything a game scene does.

The commands block until they end. Run them inside `rq.scene.play` (or `once`, `start`), from a
callback the game runs: a quest event, a hook, or `rq.on_frame` in town. From anywhere else, such
as every frame, use `rq.scene.start`. Not at the top level of a mod: the game is not running yet.

`fn` gets the namespace itself as `s`, so `s.say(...)` and `rq.scene.say(...)` are the same. A CG
number from `rq.image.add` works in every layer and as a face; it is drawn at its own size from the
top-left, so draw a portrait on a full 1024×768 canvas with a transparent background. Times are in
milliseconds. `effect` is the game's transition number; 1 is the default.

Each line of text has its own read flag, by mod and text, so the game's skip mode passes only lines
the player has read. Every line passes through the AIN function `message`, so a hook on it can read
or rewrite any line of the game (`h.args[3]`), as a translation would.

When the player goes to the title during a scene (Config has Return to title), every Lua call that
waits in the game ends with the error "rq: the game went to the title", and `rq.on_reset("title")`
follows.

A scene can also be a JSON file in the mod's folder, played by the same calls: see
`rq.scene.file`.

```lua
rq.quests.on_event(function(ev)
  if ev.kind == "start" and ev.quest == 126 then
    rq.scene.once("my_mod_intro", function(s)
      s.set(0, 5240, 0, 0)  -- a background
      s.music(72)
      s.portrait(1020)
      s.say(2020, "First line.\nSecond line.")
      s.think(2020, "A thought.")
      s.narrate("Narration.")
      s.say(2020, "Pick one.", { wait = false })
      local pick = s.choice({ "Yes", "-", { id = 42, text = "No" } })
      s.clear_text()
      s.say(2020, pick == 42 and "Too bad." or "Good.")
    end)
  end
end)
```

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `cmd` | `table<string, fun(...): any>` | Any game command by its name, called as `rq.ain.call` would. |

## Functions

| Name | Summary |
| --- | --- |
| [`rq.scene.play`](#rqsceneplay) | Opens a scene, runs `fn(s, ...)`, then clears the text and closes it. |
| [`rq.scene.once`](#rqsceneonce) | Plays a scene once per save. |
| [`rq.scene.start`](#rqscenestart) | Plays a scene at the next frame, in a coroutine of its own, and returns at once. |
| [`rq.scene.active`](#rqsceneactive) | Returns whether a mod scene plays, or `rq.scene.start` waits to play one. |
| [`rq.scene.file`](#rqscenefile) | Returns a scene file of the mod: a scene written as JSON, for `rq.scene.play`, `once` and `start`. |
| [`rq.scene.check`](#rqscenecheck) | Reads and checks a scene file of the mod without playing it, and returns its problems. |
| [`rq.scene.functions`](#rqscenefunctions) | Names the functions the mod's scene files may call, by name. |
| [`rq.scene.seen`](#rqsceneseen) | Reads or sets one of the game's event flags. |
| [`rq.scene.say`](#rqscenesay) | Shows a character's line and waits for a click. |
| [`rq.scene.think`](#rqscenethink) | Shows a character's thought and waits for a click. |
| [`rq.scene.narrate`](#rqscenenarrate) | Shows narration and waits for a click. |
| [`rq.scene.text`](#rqscenetext) | Adds text to the open frame without waiting. |
| [`rq.scene.br`](#rqscenebr) | Breaks the line in the open frame (`R`). |
| [`rq.scene.wait`](#rqscenewait) | Waits for a click, then clears the page (`A`). |
| [`rq.scene.show`](#rqsceneshow) | Shows the text in the frame without waiting (`B`). |
| [`rq.scene.clear_text`](#rqsceneclear_text) | Clears the message frame (`枠消去`). |
| [`rq.scene.speed`](#rqscenespeed) | Sets how fast text appears (`字速度`). |
| [`rq.scene.begin`](#rqscenebegin) | Opens the scene mode (`ADVON`). `rq.scene.play` calls it for you. |
| [`rq.scene.finish`](#rqscenefinish) | Clears the text and closes the scene mode (`枠消去`, `ADVOFF`). `rq.scene.play` calls it for you. |
| [`rq.scene.wallpaper`](#rqscenewallpaper) | Shows a wallpaper, the layer at the back (`壁紙表示`). |
| [`rq.scene.mask_wallpaper`](#rqscenemask_wallpaper) | Shows a masked wallpaper (`マスク壁紙表示`). |
| [`rq.scene.background`](#rqscenebackground) | Shows a background (`背景表示`). |
| [`rq.scene.background_in`](#rqscenebackground_in) | Brings a background in (`背景イン`). |
| [`rq.scene.background_out`](#rqscenebackground_out) | Takes the background out (`背景アウト`). |
| [`rq.scene.portrait`](#rqsceneportrait) | Shows a standing picture (`立ち絵表示`). |
| [`rq.scene.mini`](#rqscenemini) | Shows a small event picture (`ミニイベント表示`). |
| [`rq.scene.cg`](#rqscenecg) | Shows an event CG over the screen (`イベントＣＧ表示`). |
| [`rq.scene.set`](#rqsceneset) | Shows several layers at once (`セット表示`). |
| [`rq.scene.effect_set`](#rqsceneeffect_set) | Shows several layers at once with one transition (`エフェクトセット表示`). |
| [`rq.scene.black`](#rqsceneblack) | Fades the screen to black (`黒画面`). |
| [`rq.scene.white`](#rqscenewhite) | Fades the screen to white (`白画面`). |
| [`rq.scene.flash`](#rqsceneflash) | Flashes the screen (`画面フラッシュ`). |
| [`rq.scene.shake`](#rqsceneshake) | Shakes the whole screen (`全画面揺れ`). |
| [`rq.scene.shake_face`](#rqsceneshake_face) | Shakes the face in the message frame (`顔揺れ`). |
| [`rq.scene.shake_portrait`](#rqsceneshake_portrait) | Shakes the standing picture (`立ち絵揺れ`). |
| [`rq.scene.music`](#rqscenemusic) | Plays a game music track (`音楽`). |
| [`rq.scene.sound`](#rqscenesound) | Plays a game sound effect by number (`効果音`). |
| [`rq.scene.jingle`](#rqscenejingle) | Plays a jingle (`Ｒ８ジングル`). |
| [`rq.scene.world_map`](#rqsceneworld_map) | Shows the game's world map with a place's tag, as a quest's start does (`地図点滅`). |
| [`rq.scene.clear`](#rqsceneclear) | Clears the scene's pictures (`画面消去`). |
| [`rq.scene.wait_click`](#rqscenewait_click) | Waits for a click (`キー待ち_クリック`). |
| [`rq.scene.register_face`](#rqsceneregister_face) | Sets the name plate for one of the game's face numbers (`顔登録`). |
| [`rq.scene.choice`](#rqscenechoice) | Shows a list of choices and waits until the player picks one. |
| [`rq.scene.item`](#rqsceneitem) | Shows an item as the game does when a scene hands one over, and waits for a click. |
| [`rq.scene.before`](#rqscenebefore) | Runs `fn` before a game scene or command. |
| [`rq.scene.after`](#rqsceneafter) | Runs `fn` after a game scene or command. |
| [`rq.scene.replace`](#rqscenereplace) | Replaces a game scene or command: the game's function does not run. |

### rq.scene.play

```lua
rq.scene.play(fn, ...) -> any
```

`since 0.18.0` `changed 2.50.0` `changed 2.60.0`

Opens a scene, runs `fn(s, ...)`, then clears the text and closes it.

An error in `fn` is logged and the scene still closes; then it returns nothing. Its end runs the
game's `ADVOFF`, which clears the scene layer, so inside a game scene (from a hook) that scene's
background and pictures go too; `rq.scene.start` waits for a game scene to end instead.

The vault's and Frostbuy's item window (a rack of the shop, the vault's list) is drawn over the
message window, so the scene hides it and shows it again at its end.

Raises the error "rq: the game went to the title" again when the player went to the title.

`fn` can be a scene file (`rq.scene.file`): it is read and checked first, and a file with problems
logs them and opens no scene. Its `once` flag, when it has one, is checked and set before it opens.

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `(fun(s:` [`rq.scene`](rq.scene.md) `, ...): any)\|` [`rq.SceneFile`](../types/rq.SceneFile.md) | The scene, or a scene file. |
| `...` | `any` | Passed on to `fn` (not to a file). |

| Returns | Type | Description |
| --- | --- | --- |
|  | `any` | ... What `fn` returns; for a file, the value of the `end` step that ended it, else nothing. |

> Changed in 2.50.0: Hides the vault's and the shop's item window while it plays.

> Changed in 2.60.0: Plays a scene file, and returns its `end` value.

### rq.scene.once

```lua
rq.scene.once(id, fn, ...) -> boolean
```

`since 0.18.0` `changed 2.60.0`

Plays a scene once per save.

It marks `id` seen with `rq.scene.seen` before it plays.

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `string` | The event flag that remembers the scene. |
| `fn` | `(fun(s:` [`rq.scene`](rq.scene.md) `, ...))\|` [`rq.SceneFile`](../types/rq.SceneFile.md) | The scene, or a scene file. |
| `...` | `any` | Passed on to `fn`. |

| Returns | Type | Description |
| --- | --- | --- |
| `played` | `boolean` | false when it was already seen. |

> Changed in 2.60.0: Takes a scene file (`rq.scene.file`).

### rq.scene.start

```lua
rq.scene.start(fn, ...) -> boolean
```

`since 1.14.0` `changed 2.50.0` `changed 2.60.0`

Plays a scene at the next frame, in a coroutine of its own, and returns at once.

It returns false, and queues nothing, while a mod scene plays or waits to, so a mod can call it from
anywhere, also every frame. It waits while the System menu or Config is open, while a scene of
the game's own is on screen, and while the game saves (its "Auto-Saving" message holds 700 ms, and
the game draws frames under it). The scene draws over the current screen, takes the clicks, and
leaves the screen as it was, the vault's and Frostbuy's item window too (`rq.scene.play`). An
error that ends it is logged.

Raises an error when `fn` is not a function or a scene file.

```lua
rq.on_frame(function()
  if want_talk then
    if rq.scene.start(function(s) s.say(2020, "Hello.") end) then want_talk = false end
  end
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `(fun(s:` [`rq.scene`](rq.scene.md) `, ...))\|` [`rq.SceneFile`](../types/rq.SceneFile.md) | The scene, or a scene file. |
| `...` | `any` | Passed on to `fn` (not to a file). |

| Returns | Type | Description |
| --- | --- | --- |
| `started` | `boolean` | false when a mod scene plays or waits to. |

> Changed in 2.50.0: Waits for the game's save to end, and hides the vault's and the shop's item window.

> Changed in 2.60.0: Takes a scene file (`rq.scene.file`).

See also: [`rq.scene.active`](rq.scene.md#rqsceneactive)

### rq.scene.active

```lua
rq.scene.active() -> boolean
```

`since 1.14.0`

Returns whether a mod scene plays, or `rq.scene.start` waits to play one.

| Returns | Type | Description |
| --- | --- | --- |
| `active` | `boolean` | true during `play`, `once` and `start`. |

### rq.scene.file

```lua
rq.scene.file(path, opts) -> rq.SceneFile
```

`since 2.60.0` `changed 2.61.0` `changed 2.62.0`

Returns a scene file of the mod: a scene written as JSON, for `rq.scene.play`, `once` and `start`.

The file is a path in the mod's folder, by convention `scenes/<name>.json`. Its format is the docs
site's `schemas/scene.schema.json` (point the file's `$schema` at it, and VS Code checks and
completes it): `format` (1), `steps`, and optionally `once` (an event flag: the scene plays once per
save) and `cast` (names for faces, with their name plates). Each step is an object named by its one
step key, with its options beside it, such as `{ "say": "pluepet", "text": "\"Hello!\"" }`: lines
(`say`, `think`, `narrate`, with a list of pages), pictures, music and sounds, the screen's effects,
`world_map` (the game's map at a place, as a quest's start shows it, `rq.scene.world_map`),
`choice`, `if`, `flag`, `unflag`, `call` (a function the mod names with `rq.scene.functions`),
`label`, `goto`, `end` and `cmd`. `{name}` in a line takes a variable: one set by `into` (a
choice's pick, a call's result) or given in `opts.vars`.

Nothing is read here: the file is read and checked each time it plays, so an edit shows at the next
play. A file with problems does not play; they are logged, each with its place
(`scenes/delivery.json: steps[4].then[1]: ...`). `rq.scene.check` gives them without playing.

The file plays as the mod that called this, wherever it plays from: the read flags of its lines,
its pictures and its log lines are the mod's. A picture path is added with `rq.image.add` under a
key of the mod (`<mod id>:scene:<path>`), so each takes one of the 256 mod images.

A scene file can also be called in a scene that plays already, `rq.scene.file(path)(s)`: its steps
play there, and it returns its `end` value; a file with problems raises an error.

`opts.from` starts the file elsewhere than at its first step: at a label, or at a step's place as
the problems name it (`steps[4]`, `steps[2].choice[0].steps[1]`, `steps[3].then[0]`). From a step
inside an `if`'s branch or a choice's row, the rest of that list plays, then the steps after the
`if` or the choice, as if the branch had been taken.

The preview, `rqmod-ctl playscene MOD FILE [FROM] [name=value ...]`, plays a file of a mod from
outside the game, read anew, through `rq.scene.start`, from FROM (a label or a step's place) with
the values given (`vars`: a whole number, a number with a decimal point, true, false, else the
text); `rqmod-ctl playscene stop` ends it before its next step, `rqmod-ctl playscene status` says
which step of which file plays, and `rqmod-ctl scenefunctions MOD` lists the names the mod gave
`rq.scene.functions`.

Raises an error for a path that is not a text, a bad `opts`, or a call from outside a mod.

```lua
-- scenes/delivery.json:
-- { "format": 1, "cast": { "pluepet": { "face": 2816 } }, "steps": [
--   { "say": "pluepet", "text": "\"Here is your {item}!\"" },
--   { "end": "clear" } ] }
rq.quests.define({ id = "mymod:delivery", name = "A Delivery", open = true, run = function()
  return rq.scene.play(rq.scene.file("scenes/delivery.json", { vars = { item = "Lens" } }))
end })
```

| Parameter | Type | Description |
| --- | --- | --- |
| `path` | `string` | A path in the mod's folder. |
| `opts` *(optional)* | [`rq.SceneFileOpts`](../types/rq.SceneFileOpts.md) | The starting variables and label. |

| Returns | Type | Description |
| --- | --- | --- |
| `file` | [`rq.SceneFile`](../types/rq.SceneFile.md) | The scene file, for `play`, `once`, `start`, or a call in a scene. |

> Changed in 2.61.0: `from` takes a step's place as well as a label.

> Changed in 2.62.0: The `world_map` step.

See also: [`rq.scene.check`](rq.scene.md#rqscenecheck), [`rq.scene.functions`](rq.scene.md#rqscenefunctions)

### rq.scene.check

```lua
rq.scene.check(path) -> string[]
```

`since 2.60.0`

Reads and checks a scene file of the mod without playing it, and returns its problems.

It checks what playing it checks: the JSON, each step's name and options, the cast, each `goto`'s
label, each label once, each function named by `rq.scene.functions`, each game name (a character,
an item, a quest) as `rq.ids` or a mod's id gives it, and each picture's file. A mod's quest by its
id is checked only while a save is loaded, since a quest has its number only in a save.

Raises an error for a path that is not a text, or a call from outside a mod.

```lua
for _, p in ipairs(rq.scene.check("scenes/delivery.json")) do rq.log(p) end
```

| Parameter | Type | Description |
| --- | --- | --- |
| `path` | `string` | A path in the mod's folder. |

| Returns | Type | Description |
| --- | --- | --- |
| `problems` | `string[]` | Each as "path: place: what"; empty for a file that plays. |

See also: [`rq.scene.file`](rq.scene.md#rqscenefile)

### rq.scene.functions

```lua
rq.scene.functions(fns)
```

`since 2.60.0`

Names the functions the mod's scene files may call, by name.

A file's `call` step, a `call` condition and a choice's rows from `{ "call": name }` call them, also
from the preview. Each gets `ctx` (`rq.SceneCtx`), the scene `s` (so it can play steps of its own,
such as `s.item`) and the step's `args`, JSON's null as nil. What it returns goes to the step's
`into`, decides the condition (anything but nil and false holds), or is the list of rows, as
`rq.scene.choice` takes them.

Calling it again adds names and replaces those it names again; `false` in place of a function takes
a name away. An error in a function ends the scene, logged with the step's place.

Raises an error for a key that is not a name (letters, digits and _, not starting with a digit), a
value that is not a function or false, or a call from outside a mod.

```lua
rq.scene.functions({
  owned = function(ctx, s, no) return rq.item.count(no) > 0 end,
  lost_items = function(ctx) return { { id = 11, text = "Boots" }, { id = 12, text = "Gloves" } } end,
  remember = function(ctx, s, name) rq.store.set("last_pick", ctx.vars[name]) end,
})
```

| Parameter | Type | Description |
| --- | --- | --- |
| `fns` | `table<string, (fun(ctx:` [`rq.SceneCtx`](../types/rq.SceneCtx.md) `, s:` [`rq.scene`](rq.scene.md) `, ...): any)\|false>` | The functions by name. |

See also: [`rq.scene.file`](rq.scene.md#rqscenefile)

### rq.scene.seen

```lua
rq.scene.seen(id, set) -> boolean
```

`since 0.18.0`

Reads or sets one of the game's event flags.

The game's own scene names work too.

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `string` | The flag's name. |
| `set` *(optional)* | `boolean` | true or false writes the flag; leave it out to read. |

| Returns | Type | Description |
| --- | --- | --- |
| `seen` | `boolean` | The flag. |

### rq.scene.say

```lua
rq.scene.say(face, text, opts)
```

`since 0.18.0`

Shows a character's line and waits for a click.

A newline in `text` breaks the line.

| Parameter | Type | Description |
| --- | --- | --- |
| `face` | `integer` | The face CG number. |
| `text` | `string` | The line. |
| `opts` *(optional)* | [`rq.SceneTextOpts`](../types/rq.SceneTextOpts.md) | Name plate, frame and wait. |

### rq.scene.think

```lua
rq.scene.think(face, text, opts)
```

`since 0.18.0`

Shows a character's thought and waits for a click.

| Parameter | Type | Description |
| --- | --- | --- |
| `face` | `integer` | The face CG number. |
| `text` | `string` | The thought. |
| `opts` *(optional)* | [`rq.SceneTextOpts`](../types/rq.SceneTextOpts.md) | Name plate, frame and wait. |

### rq.scene.narrate

```lua
rq.scene.narrate(text, opts)
```

`since 0.18.0`

Shows narration and waits for a click.

| Parameter | Type | Description |
| --- | --- | --- |
| `text` | `string` | The narration. |
| `opts` *(optional)* | [`rq.SceneTextOpts`](../types/rq.SceneTextOpts.md) | Frame and wait. |

### rq.scene.text

```lua
rq.scene.text(text)
```

`since 0.18.0`

Adds text to the open frame without waiting.

With `br`, `wait`, `show`, `clear_text` and `speed` it builds a line step by step.

| Parameter | Type | Description |
| --- | --- | --- |
| `text` | `string` | The text. |

### rq.scene.br

```lua
rq.scene.br()
```

`since 0.18.0`

Breaks the line in the open frame (`R`).

### rq.scene.wait

```lua
rq.scene.wait()
```

`since 0.18.0`

Waits for a click, then clears the page (`A`).

### rq.scene.show

```lua
rq.scene.show()
```

`since 0.18.0`

Shows the text in the frame without waiting (`B`).

### rq.scene.clear_text

```lua
rq.scene.clear_text()
```

`since 0.18.0`

Clears the message frame (`枠消去`).

### rq.scene.speed

```lua
rq.scene.speed(ms)
```

`since 0.18.0`

Sets how fast text appears (`字速度`).

| Parameter | Type | Description |
| --- | --- | --- |
| `ms` | `integer` | Time per character: 0 shows it at once, -1 uses the player's setting. |

### rq.scene.begin

```lua
rq.scene.begin()
```

`since 0.18.0`

Opens the scene mode (`ADVON`). `rq.scene.play` calls it for you.

### rq.scene.finish

```lua
rq.scene.finish()
```

`since 0.18.0`

Clears the text and closes the scene mode (`枠消去`, `ADVOFF`). `rq.scene.play` calls it for you.

### rq.scene.wallpaper

```lua
rq.scene.wallpaper(cg, effect, time)
```

`since 0.18.0`

Shows a wallpaper, the layer at the back (`壁紙表示`).

| Parameter | Type | Description |
| --- | --- | --- |
| `cg` | `integer` | The CG number. |
| `effect` *(optional)* | `integer` | The transition. Default 1. |
| `time` *(optional)* | `integer` | The transition time, in ms. Default 500. |

### rq.scene.mask_wallpaper

```lua
rq.scene.mask_wallpaper(cg, effect, time)
```

`since 0.18.0`

Shows a masked wallpaper (`マスク壁紙表示`).

| Parameter | Type | Description |
| --- | --- | --- |
| `cg` | `integer` | The CG number. |
| `effect` *(optional)* | `integer` | The transition. Default 1. |
| `time` *(optional)* | `integer` | The transition time, in ms. Default 500. |

### rq.scene.background

```lua
rq.scene.background(cg, effect, time, name, flag)
```

`since 0.18.0`

Shows a background (`背景表示`).

| Parameter | Type | Description |
| --- | --- | --- |
| `cg` | `integer` | The CG number. |
| `effect` *(optional)* | `integer` | The transition. Default 1. |
| `time` *(optional)* | `integer` | The transition time, in ms. Default 500. |
| `name` *(optional)* | `string` | The game's `szName` argument. Default "". |
| `flag` *(optional)* | `boolean` | The game's `bFlag` argument. Default false. |

### rq.scene.background_in

```lua
rq.scene.background_in(cg, time, name, flag)
```

`since 0.18.0`

Brings a background in (`背景イン`).

| Parameter | Type | Description |
| --- | --- | --- |
| `cg` | `integer` | The CG number. |
| `time` *(optional)* | `integer` | The transition time, in ms. Default 500. |
| `name` *(optional)* | `string` | The game's `szName` argument. Default "". |
| `flag` *(optional)* | `boolean` | The game's `bFlag` argument. Default false. |

### rq.scene.background_out

```lua
rq.scene.background_out(time)
```

`since 0.18.0`

Takes the background out (`背景アウト`).

| Parameter | Type | Description |
| --- | --- | --- |
| `time` *(optional)* | `integer` | The transition time, in ms. Default 500. |

### rq.scene.portrait

```lua
rq.scene.portrait(cg, effect, time)
```

`since 0.18.0`

Shows a standing picture (`立ち絵表示`).

| Parameter | Type | Description |
| --- | --- | --- |
| `cg` | `integer` | The CG number. |
| `effect` *(optional)* | `integer` | The transition. Default 1. |
| `time` *(optional)* | `integer` | The transition time, in ms. Default 200. |

### rq.scene.mini

```lua
rq.scene.mini(cg, effect, time)
```

`since 0.18.0`

Shows a small event picture (`ミニイベント表示`).

| Parameter | Type | Description |
| --- | --- | --- |
| `cg` | `integer` | The CG number. |
| `effect` *(optional)* | `integer` | The transition. Default 1. |
| `time` *(optional)* | `integer` | The transition time, in ms. Default 200. |

### rq.scene.cg

```lua
rq.scene.cg(cg, effect, time)
```

`since 0.18.0`

Shows an event CG over the screen (`イベントＣＧ表示`).

| Parameter | Type | Description |
| --- | --- | --- |
| `cg` | `integer` | The CG number. |
| `effect` *(optional)* | `integer` | The transition. Default 1. |
| `time` *(optional)* | `integer` | The transition time, in ms. Default 500. |

### rq.scene.set

```lua
rq.scene.set(wallpaper, background, portrait, mini)
```

`since 0.18.0`

Shows several layers at once (`セット表示`).

| Parameter | Type | Description |
| --- | --- | --- |
| `wallpaper` *(optional)* | `integer` | The wallpaper CG; 0 leaves the layer empty. Default 0. |
| `background` *(optional)* | `integer` | The background CG; 0 leaves it empty. Default 0. |
| `portrait` *(optional)* | `integer` | The standing picture CG; 0 leaves it empty. Default 0. |
| `mini` *(optional)* | `integer` | The small event picture CG; 0 leaves it empty. Default 0. |

### rq.scene.effect_set

```lua
rq.scene.effect_set(effect, wallpaper, background, portrait, mini, event_cg)
```

`since 0.18.0`

Shows several layers at once with one transition (`エフェクトセット表示`).

| Parameter | Type | Description |
| --- | --- | --- |
| `effect` *(optional)* | `integer` | The transition. Default 1. |
| `wallpaper` *(optional)* | `integer` | The wallpaper CG; 0 leaves the layer empty. Default 0. |
| `background` *(optional)* | `integer` | The background CG. Default 0. |
| `portrait` *(optional)* | `integer` | The standing picture CG. Default 0. |
| `mini` *(optional)* | `integer` | The small event picture CG. Default 0. |
| `event_cg` *(optional)* | `integer` | The event CG. Default 0. |

### rq.scene.black

```lua
rq.scene.black(effect, time)
```

`since 0.18.0`

Fades the screen to black (`黒画面`).

| Parameter | Type | Description |
| --- | --- | --- |
| `effect` *(optional)* | `integer` | The transition. Default 1. |
| `time` *(optional)* | `integer` | The transition time, in ms. Default 500. |

### rq.scene.white

```lua
rq.scene.white(effect, time)
```

`since 0.18.0`

Fades the screen to white (`白画面`).

| Parameter | Type | Description |
| --- | --- | --- |
| `effect` *(optional)* | `integer` | The transition. Default 1. |
| `time` *(optional)* | `integer` | The transition time, in ms. Default 500. |

### rq.scene.flash

```lua
rq.scene.flash(time)
```

`since 0.18.0`

Flashes the screen (`画面フラッシュ`).

| Parameter | Type | Description |
| --- | --- | --- |
| `time` *(optional)* | `integer` | How long, in ms. Default 200. |

### rq.scene.shake

```lua
rq.scene.shake(mode, flag)
```

`since 0.18.0`

Shakes the whole screen (`全画面揺れ`).

| Parameter | Type | Description |
| --- | --- | --- |
| `mode` *(optional)* | `integer` | The game's shake mode (`nMode`). Default 1. |
| `flag` *(optional)* | `boolean` | The game's `bFlag` argument. Default false. |

### rq.scene.shake_face

```lua
rq.scene.shake_face(mode, flag)
```

`since 0.18.0`

Shakes the face in the message frame (`顔揺れ`).

| Parameter | Type | Description |
| --- | --- | --- |
| `mode` *(optional)* | `integer` | The game's shake mode (`nMode`). Default 1. |
| `flag` *(optional)* | `boolean` | The game's `bFlag` argument. Default false. |

### rq.scene.shake_portrait

```lua
rq.scene.shake_portrait(mode, flag)
```

`since 0.18.0`

Shakes the standing picture (`立ち絵揺れ`).

| Parameter | Type | Description |
| --- | --- | --- |
| `mode` *(optional)* | `integer` | The game's shake mode (`nMode`). Default 1. |
| `flag` *(optional)* | `boolean` | The game's `bFlag` argument. Default false. |

### rq.scene.music

```lua
rq.scene.music(no, effect, time)
```

`since 0.18.0`

Plays a game music track (`音楽`).

| Parameter | Type | Description |
| --- | --- | --- |
| `no` | `integer` | The music number. |
| `effect` *(optional)* | `integer` | The fade type; -1 is the game's default. Default -1. |
| `time` *(optional)* | `integer` | The fade time; -1 is the game's default. Default -1. |

### rq.scene.sound

```lua
rq.scene.sound(no)
```

`since 0.18.0`

Plays a game sound effect by number (`効果音`).

`rq.sound.play` also plays files and returns a handle.

| Parameter | Type | Description |
| --- | --- | --- |
| `no` | `integer` | The sound number. |

### rq.scene.jingle

```lua
rq.scene.jingle(no, wait)
```

`since 0.18.0`

Plays a jingle (`Ｒ８ジングル`).

| Parameter | Type | Description |
| --- | --- | --- |
| `no` | `integer` | The sound number. |
| `wait` *(optional)* | `boolean` | true waits for it to end. Default false. |

### rq.scene.world_map

```lua
rq.scene.world_map(place, y, name)
```

`since 2.62.0`

Shows the game's world map with a place's tag, as a quest's start does (`地図点滅`).

The game's jingle 407 plays, the pictures and the message box are cleared, and the map (CG 5530)
fades in over a second. A tag points at the place with its name in it, until a click; then the
screen goes black, with the pictures and the message box cleared, so the scene shows its next
pictures after it.

`place` is one of the game's places, 1 to 40, each with the name and the point the game gives it
(1 is Cidade). With `y` and `name`, the first value is instead the x of a point of the mod's own on
the game's 1024 by 768 screen, and `name` is the text on its tag. The tag opens to the right of a
point left of x 512, and to the left of one right of it.

Raises an error for a place out of 1 to 40, or a point whose x or y is not a whole number or
whose name is not a text.

```lua
rq.scene.play(function(s)
  s.world_map(1)                    -- the game's Cidade
  s.world_map(640, 300, "Our Camp") -- a point of the mod's own
  s.background(5280)
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `place` | `integer` | A place of the game's, 1 to 40; with `y` and `name`, a point's x, 0 to 1023. |
| `y` *(optional)* | `integer` | The point's y, 0 to 767. |
| `name` *(optional)* | `string` | The name on the point's tag. |

### rq.scene.clear

```lua
rq.scene.clear()
```

`since 0.18.0`

Clears the scene's pictures (`画面消去`).

### rq.scene.wait_click

```lua
rq.scene.wait_click() -> any
```

`since 0.18.0`

Waits for a click (`キー待ち_クリック`).

| Returns | Type | Description |
| --- | --- | --- |
| `result` | `any` | What the game's command returns. |

### rq.scene.register_face

```lua
rq.scene.register_face(cg, name, tone)
```

`since 0.18.0`

Sets the name plate for one of the game's face numbers (`顔登録`).

A mod's own face passes `opts.name` to `say` instead.

| Parameter | Type | Description |
| --- | --- | --- |
| `cg` | `integer` | The face CG number, 2000 and up. |
| `name` | `string` | The name on the plate. |
| `tone` *(optional)* | `integer` | The game's tone value (`口調`). Default 1. |

### rq.scene.choice

```lua
rq.scene.choice(items, opts) -> integer
```

`since 0.18.0` `changed 2.56.0`

Shows a list of choices and waits until the player picks one.

A list too tall for the room under its `y` goes up just enough to fit on the screen; one that fits
keeps its place.

could be off the screen.

```lua
local pick = s.choice({ "Yes", "-", { id = 42, text = "No" } })
```

| Parameter | Type | Description |
| --- | --- | --- |
| `items` | `(string\|` [`rq.SceneChoice`](../types/rq.SceneChoice.md) `)[]` | The rows: text, `"-"` for a separator, or a table. |
| `opts` *(optional)* | `{x?: integer, y?: integer, cancel?: boolean}` | `x`, `y`: where the list goes (y default 360). `cancel`: the game's cancel flag for the list. Default false. |

| Returns | Type | Description |
| --- | --- | --- |
| `id` | `integer` | The picked row's id. |

> Changed in 2.56.0: A list too tall for the room under its `y` goes up to fit. Before, its last rows

### rq.scene.item

```lua
rq.scene.item(ii, o)
```

`since 2.50.0`

Shows an item as the game does when a scene hands one over, and waits for a click.

It plays the game's jingle (1008 by default) and opens the game's item window with the item's
icon, name, level and effects (`Ｒ８どこかからアイテム`, as for an event's reward or the dice's
prize). It only shows the item: put it where it goes with `rq.item.give`, `rq.item.set` or
`rq.item.store` first.

Raises an error when `ii` is not a whole number or not an item instance, when `o` is not a table,
or when `jingle` is neither a number nor false.

```lua
rq.scene.start(function(s)
  local ii = rq.item.give("mymod:lens")
  s.say(2020, "Here, take this.")
  s.item(ii)
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `ii` | `integer` | The item instance. |
| `o` *(optional)* | `{jingle?: integer\|false}` | `jingle`: the jingle number, or false for none. Default 1008. |

### rq.scene.before

```lua
rq.scene.before(name, fn)
```

`since 0.18.0`

Runs `fn` before a game scene or command.

Game scenes are AIN functions named like `カオル／出会い`; find names with `rq.ain.find`.

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | The AIN function's name. |
| `fn` | `fun(h:` [`rq.AinHookCtx`](../types/rq.AinHookCtx.md) `)` | Gets the call, as `rq.ain.hook` does. |

See also: [`rq.ain.hook`](rq.ain.md#rqainhook)

### rq.scene.after

```lua
rq.scene.after(name, fn)
```

`since 0.18.0`

Runs `fn` after a game scene or command.

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | The AIN function's name. |
| `fn` | `fun(h:` [`rq.AinHookCtx`](../types/rq.AinHookCtx.md) `)` | Gets the call, as `rq.ain.hook` does. |

### rq.scene.replace

```lua
rq.scene.replace(name, fn)
```

`since 0.18.0`

Replaces a game scene or command: the game's function does not run.

What `fn` returns becomes the call's result.

```lua
rq.scene.replace("カオル／出会い", function(h)
  rq.scene.play(function(s) s.say(2020, "A new first meeting.") end)
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | The AIN function's name. |
| `fn` | `fun(h:` [`rq.AinHookCtx`](../types/rq.AinHookCtx.md) `): any` | Returns the result. |
