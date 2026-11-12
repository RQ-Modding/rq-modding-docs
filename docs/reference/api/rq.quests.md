# rq.quests

`since 0.2.0`

Lists the quests and follows them: clears, endings, quest moments and state.

`rq.quests()` and `rq.quests.list()` list the quests that have a name, up to 512. `state`,
`set_state`, `unlock` and `start` raise an error for a quest number the game does not have. Characters recruited and quests unlocked
from `on_clear` show on the victory screen with the game's own animation, as the game does for
Tomato. Dialogue inside a quest is quest script and is not part of these hooks.

A mod can add quests of its own with no map (`rq.quests.define`): each gets a number from 303 to
500 in the save, and the calls that take a quest number take its id too.

```lua
rq.chara.define{ id = "mymod:alice", name = "Alice", face = "faces/alice.png", class = 5 }
rq.quests.on_clear(function(ctx)
  if ctx.quest == 126 and ctx.first then
    rq.chara.recruit("mymod:alice", { state = 2 }) -- shown on the victory screen
    rq.quests.unlock(207)
  end
end)
```

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `list` | `fun():` [`rq.Quest`](../types/rq.Quest.md) `[]` | Lists the quests, as `rq.quests()` does. |

## Functions

| Name | Summary |
| --- | --- |
| [`rq.quests.state`](#rqquestsstate) | Returns a quest's state. |
| [`rq.quests.set_state`](#rqquestsset_state) | Sets a quest's state, through the game's `Ｑ状態`. |
| [`rq.quests.unlock`](#rqquestsunlock) | Makes a locked quest available. |
| [`rq.quests.current`](#rqquestscurrent) | Returns the quest being played. |
| [`rq.quests.start`](#rqquestsstart) | Starts a quest through the game's own flow, with no click on the quest list. |
| [`rq.quests.new_this_run`](#rqquestsnew_this_run) | Returns what the victory screen will show as new. |
| [`rq.quests.can_take`](#rqquestscan_take) | Returns whether a quest can be taken now: the game's `クエスト_有効`, which lights the quest list's Take button. |
| [`rq.quests.refresh`](#rqquestsrefresh) | Draws the quest list again, with the chosen quest's buttons as the game draws them. |
| [`rq.quests.get`](#rqquestsget) | Returns a quest's data, as the quest list shows it. |
| [`rq.quests.edit`](#rqquestsedit) | Changes a quest's name, text, place, difficulty or conditions while the mod runs. |
| [`rq.quests.define`](#rqquestsdefine) | Adds a quest of the mod's own: a story, fights, a menu, or a map of the game's rooms. |
| [`rq.quests.no`](#rqquestsno) | Returns the number a mod's quest has in the loaded save. |
| [`rq.quests.run`](#rqquestsrun) | Returns the counters, bonuses and rules of the quest being played. |
| [`rq.quests.set_run`](#rqquestsset_run) | Changes the counters, bonuses and rules of the quest being played. |

### rq.quests.state

```lua
rq.quests.state(no) -> integer
```

`since 0.7.0` `changed 2.41.0`

Returns a quest's state.

| Parameter | Type | Description |
| --- | --- | --- |
| `no` | `integer\|string` | The quest number, or the id of a quest a mod defined. |

| Returns | Type | Description |
| --- | --- | --- |
| `state` | `integer` | 0 locked, 1 available, 2 cleared. |

> Changed in 2.41.0: Takes a mod's quest's id.

### rq.quests.set_state

```lua
rq.quests.set_state(no, state)
```

`since 0.7.0` `changed 2.23.0` `changed 2.41.0`

Sets a quest's state, through the game's `Ｑ状態`.

State 2 also records a first clear. State 1 on a locked quest adds it to the "new quests" list of
the victory screen; on a quest already available or cleared, the game's `Ｑ状態` changes nothing, so
the call writes the state itself (a cleared quest can be taken again). Raises an error for a state
other than 0, 1 or 2.

| Parameter | Type | Description |
| --- | --- | --- |
| `no` | `integer\|string` | The quest number, or the id of a quest a mod defined. |
| `state` | `integer` | 0 locked, 1 available, 2 cleared. |

> Changed in 2.23.0: State 1 on a cleared quest is written; before, the call did nothing there.

> Changed in 2.41.0: Takes a mod's quest's id.

See also: [`rq.quests.unlock`](rq.quests.md#rqquestsunlock)

### rq.quests.unlock

```lua
rq.quests.unlock(no) -> boolean
```

`since 0.7.0` `changed 2.41.0`

Makes a locked quest available.

It sets state 1 only when the quest is locked. A quest opened this way joins the "new quests" list
on the victory screen.

| Parameter | Type | Description |
| --- | --- | --- |
| `no` | `integer\|string` | The quest number, or the id of a quest a mod defined. |

| Returns | Type | Description |
| --- | --- | --- |
| `unlocked` | `boolean` | false when the quest was not locked. |

> Changed in 2.41.0: Takes a mod's quest's id.

### rq.quests.current

```lua
rq.quests.current() -> integer
```

`since 0.18.0`

Returns the quest being played.

| Returns | Type | Description |
| --- | --- | --- |
| `no` | `integer` | The quest number, or 0 in town. |

### rq.quests.start

```lua
rq.quests.start(no)
```

`since 0.23.0` `changed 2.41.0`

Starts a quest through the game's own flow, with no click on the quest list.

It returns at once; the game moves on its next update, and `rq.quests.current()` gives the number
once the quest started. Any join dialog or scene of the quest plays as usual, and like a real start
it autosaves and counts as a try. A locked quest starts too, including the game's debug entries
(quest 10 goes straight back to town).

Raises an error for a value that is not a whole number, an unknown quest, a quest this party cannot
take, while a quest runs or another is starting, and on any screen but the hub or the quest list.
The game can still refuse after that with its own message, at 2500 items or more or when its Alice
event is due.

```lua
if rq.ui.get().screen == "hub" then rq.quests.start(126) end
```

| Parameter | Type | Description |
| --- | --- | --- |
| `no` | `integer\|string` | The quest number, or the id of a quest a mod defined. |

> Changed in 2.41.0: Takes a mod's quest's id.

### rq.quests.new_this_run

```lua
rq.quests.new_this_run() -> rq.NewThisRun
```

`since 0.7.0`

Returns what the victory screen will show as new.

Recruiting a character and unlocking a quest add to these lists; the game empties both when a quest
ends.

| Returns | Type | Description |
| --- | --- | --- |
| `new` | [`rq.NewThisRun`](../types/rq.NewThisRun.md) | The new characters and quests. |

### rq.quests.can_take

```lua
rq.quests.can_take(no) -> boolean
```

`since 2.23.0` `changed 2.39.0` `changed 2.41.0`

Returns whether a quest can be taken now: the game's `クエスト_有効`, which lights the quest list's
Take button.

It is true when the party has at least one member, the quest exists and its conditions to take
part are met (an item it needs, a character, and the like). A mod's own condition
(`rq.quests.edit`'s `condition`) is asked first.

Raises an error when `no` is not a quest number.

```lua
if not rq.quests.can_take(80) then rq.log("Gem Lady needs a Jewel") end
```

| Parameter | Type | Description |
| --- | --- | --- |
| `no` | `integer\|string` | The quest number, or the id of a quest a mod defined. |

| Returns | Type | Description |
| --- | --- | --- |
| `ok` | `boolean` | true when Take would be lit for it. |

> Changed in 2.39.0: Asks the mods' own conditions (`rq.quests.edit`) first.

> Changed in 2.41.0: Takes a mod's quest's id.

### rq.quests.refresh

```lua
rq.quests.refresh() -> boolean
```

`since 2.23.0` `changed 2.39.0`

Draws the quest list again, with the chosen quest's buttons as the game draws them.

After a change that the list shows (an item a quest needs, a state), the rows are made again and
the chosen quest's Take is lit or greyed by `rq.quests.can_take`, as the game does after the
favorite button (`T_Quest::remakeList`, then `T_Quest::lock`). With no quest chosen, only the rows.
The mods' own conditions (`rq.quests.edit`'s `condition`) are asked again first.

```lua
rq.item.remove(jewel)
rq.quests.refresh() -- Take greys if that was the last one
```

| Returns | Type | Description |
| --- | --- | --- |
| `done` | `boolean` | false when the quest list is not open. |

> Changed in 2.39.0: Asks the mods' own conditions (`rq.quests.edit`) again first.

### rq.quests.get

```lua
rq.quests.get(no) -> rq.QuestData
```

`since 2.39.0` `changed 2.41.0` `changed 2.42.0`

Returns a quest's data, as the quest list shows it.

It reads the game's data with every mod's `rq.quests.edit` on it. `rq.quests()` stays the short list
of every quest.

Raises an error for a number the game does not have (no quest has it, or it has no name), also
before a save is loaded.

`menu` was corrected: the game's kind 3 is any quest with no map and no fights.

```lua
local q = rq.quests.get(126)
rq.log(q.name, q.difficulty, q.fame, #q.conditions, q.can_take)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `no` | `integer\|string` | The quest number, or the id of a quest a mod defined. |

| Returns | Type | Description |
| --- | --- | --- |
| `data` | [`rq.QuestData`](../types/rq.QuestData.md) | The quest's data. |

> Changed in 2.41.0: Takes a mod's quest's id; gives `text_id` and `main`. The description of `kind`'s

> Changed in 2.42.0: Gives `map` for a mod's quest with a map.

See also: [`rq.quests.edit`](rq.quests.md#rqquestsedit)

### rq.quests.edit

```lua
rq.quests.edit(no, patch)
```

`since 2.39.0` `changed 2.41.0`

Changes a quest's name, text, place, difficulty or conditions while the mod runs.

The game writes every quest's data again when a game starts, after each load and at a world
transfer (`Ｑ起動時登録`), and the story's special conditions each time the quest menu opens
(`Ｑ特殊な条件の処理`). The patch is put back on top after each, and at once when the call is made
with a save loaded; made before (at a mod's top level), it applies when the game first writes its
data. Nothing stays in the save: without the mod, the game's next writing brings its own data back.

Each mod keeps one patch per quest: calling again replaces that mod's patch, and `nil` removes it,
bringing the game's data back. The patches apply in load order, a later mod's field over an
earlier one's. The fame a clear gives is not patched, since the game halves it after each clear;
to change what a run gives, use `rq.quests.set_run{ fame = ... }`.

A mod's own condition (`condition`): `ok(no)` is asked when the quest menu opens, at
`rq.quests.refresh` and at `rq.quests.can_take`. While it is not met, the quest takes the game's
special condition: the first free condition slot holds it, the quest list greys Take and shows
`text`. With the game's special condition already there, or the conditions of several mods, the
texts are joined with " / ". An error in `ok` is logged and counts as met. With the quest list open,
call `rq.quests.refresh` to show a change.

A mod's quest (`rq.quests.define`) is patched by its id the same way, over its definition's fields,
in every save whatever its number there.

Raises an error for an unknown quest (once a save is loaded), an unknown field, a value of the
wrong kind or too long, more than 3 conditions, or `condition` with 3 `conditions`.

no longer starts with " / ".

```lua
-- A harder quest that needs Kanami in the party and the three shrines found.
local function shrines() return rq.store.get("shrines") or 0 end
rq.quests.edit(126, {
  difficulty = 40,
  conditions = { { kind = "member", chara = rq.ids.chara.KANAMI_KENTOU } },
  condition = { text = "Find the three shrines", ok = function() return shrines() >= 3 end },
})
```

| Parameter | Type | Description |
| --- | --- | --- |
| `no` | `integer\|string` | The quest number, or the id of a quest a mod defined. |
| `patch` | [`rq.QuestEdit`](../types/rq.QuestEdit.md) `\|nil` | The fields to change; nil removes this mod's patch. |

> Changed in 2.41.0: Takes a mod's quest's id. A mod's own condition joined to an empty special text

See also: [`rq.quests.get`](rq.quests.md#rqquestsget)

### rq.quests.define

```lua
rq.quests.define(def)
```

`since 2.41.0` `changed 2.42.0`

Adds a quest of the mod's own: a story, fights, a menu, or a map of the game's rooms.

The quest list shows it as one of the game's, and Take starts it through the game's own flow (the
autosave, the try counted, the quest storage emptied). Then `run(q)` runs in place of a game
quest's script: it plays scenes (`rq.scene.play`), fights (`rq.battle.start`), choices
(`rq.scene.choice`, `rq.ui.choose`) and dialogs, gives items into the quest storage
(`rq.item.give` with `place = "quest"`), and returns how the quest ends:
- `"clear"` (or nil): the game's success screen, the fame and the appraisal; the clear is counted,
  the quest stays in the list as cleared, `rq.quests.on_clear` runs;
- `"fail"`: the failure screen, as when the party loses;
- `"abandon"`: given up, the quest storage's items lost;
- `"escape"`: given up with the items kept, as with the escape device.

An error in `run` is written to the log and the quest is given up. `rq.quests.on_event`'s `start`
runs before `run`, and `on_end` after it, with `id` in their ctx.

**A map** (`map`) makes it a quest with the map mark, played as the game's: `run`, if any, is a
prologue; then the party enters the area `start`. Each area is set up as the game's quest scripts
set theirs, at each entry: the tileset, name, gold, loot, music, traps, groups and bonuses, then the
room with its exits and counted objects; on its first entry in a run, its `objects`; then `setup`.
A custom object's `run` is its `rq.dungeon.on_object` function, and the quest ends when one returns
a result, as the boss or the goal of the game's quests do; the escape device and a lost fight end
it too. `rq.quests.set_run`'s `progress` fills the panel's bar. The rooms drawn are kept in the
save, so every try has the same rooms; a new shape of the map (an area's tileset, room or exits)
draws them anew. A save made on the map of a mod that is gone ends the quest as with the escape
device the first time the map hands over to the quest (a fight, a touch, the menu key).

**The number.** The first time a save has the quest (a new game, a load, a world transfer), it
takes the first free number from 303 to 500 and keeps it in that save, marked with its id; another
save can give it another number. `rq.quests.no(id)` gives it. Past 198 quests in one save, a quest
is left out with a line in the log.

**The data** (name, text, place, difficulty, conditions) is written again after each load, so a
new version of the mod shows its new text in an old save; the state, tries, clears and fame are the
save's. Another mod's `rq.quests.edit` works on it by id.

**Opening it**: `open`, `after`, or `rq.quests.unlock(id)` from the mod. A quest opened by a clear
shows on the victory screen with the game's new quests.

**A world transfer** resets the mods' quests as it resets the game's: their tries, clears and
fame, and their state back to what `open` and `after` give.

**Without the mod**: a save that has the quest keeps it hidden (state 0, so the list leaves it
out) with its state kept, and brings it back as it was when the mod is loaded again. A world
transfer made without the mod forgets it: it starts as new when the mod comes back.

Call it at the mod's top level. Calling it again with the same id from the same mod replaces the
definition. Raises an error for an id another mod defined, an unknown field, a value of the wrong
kind or too long, more than 3 conditions, `open` with `after`, or no `run` and no `map`. For a map:
`fights`; an exit off the grid or with no way back; an area `start` does not reach; an area with no
tileset or no groups; a room, fixed map or exit the tileset or the fixed map does not have; more
objects than the room's spots; an object's field of the wrong kind.

```lua
rq.item.define({ id = "mymod:lotion", name = "Dancer's Lotion", price = 200, info = "It smells of roses." })

rq.quests.define({
  id = "mymod:lotion_quest",
  name = "The Lost Lotion",
  text = { "A dancer lost her lotion in the bathhouse.", "She will pay well to get it back." },
  place = "Copan Empire",
  fights = true,
  fame = 5,
  open = true,
  run = function(q)
    rq.scene.play(function(s)
      s.narrate("The bathhouse is dark, and something skitters in the steam.")
    end)
    local r = rq.battle.start({ enemies = { 0, rq.ids.monster.COCKROACH, 0 }, exp = 300 })
    if r ~= "won" then return "fail" end
    rq.item.give("mymod:lotion", { place = "quest" })
    return "clear"
  end,
})

-- A cave of two areas, its queen at the end.
rq.quests.define({
  id = "mymod:bat_cave", name = "The Bat Cave", place = "Leazas", difficulty = 12, fame = 60, open = true,
  map = {
    tileset = rq.ids.map_kind.CAVE, name = "Bat Cave", loot = "B", groups = { 47, 49 },
    areas = {
      [1] = { exits = "E", enemies = 2, chests = 1 },
      [2] = { exits = "W", room = 203, objects = {
        { kind = "custom", id = "mymod:bat_queen", look = "event-4", spot = "wide", run = function(ctx)
          local r = rq.battle.start({ enemies = { 0, rq.ids.monster.COCKROACH, 0 }, boss = true })
          if r ~= "won" then return "fail" end
          return "clear"
        end },
      } },
    },
  },
})
```

| Parameter | Type | Description |
| --- | --- | --- |
| `def` | [`rq.QuestDef`](../types/rq.QuestDef.md) | The quest. |

> Changed in 2.42.0: Takes `map`; `run` is then the prologue and may be left out.

See also: [`rq.quests.no`](rq.quests.md#rqquestsno), [`rq.quests.edit`](rq.quests.md#rqquestsedit)

### rq.quests.no

```lua
rq.quests.no(id) -> integer|nil
```

`since 2.41.0`

Returns the number a mod's quest has in the loaded save.

A quest takes its number when a save first has it, so the number of one id can differ from save to
save; keep the id, not the number. Also the number of a quest whose mod is not loaded, while the save
keeps it.

```lua
rq.quests.on_clear(function(ctx)
  if ctx.quest == rq.quests.no("mymod:lotion_quest") then rq.log("the lotion is back") end
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `string` | The quest's id. |

| Returns | Type | Description |
| --- | --- | --- |
| `no` | `integer\|nil` | The number, or nil when no save is loaded or the save has no such quest. |

See also: [`rq.quests.define`](rq.quests.md#rqquestsdefine)

### rq.quests.run

```lua
rq.quests.run() -> rq.QuestRun|nil
```

`since 2.39.0`

Returns the counters, bonuses and rules of the quest being played.

```lua
local run = rq.quests.run()
if run and run.bonuses.feats then
  rq.log("achievements", run.bonuses.feats.count, "of", run.bonuses.feats.max)
end
```

| Returns | Type | Description |
| --- | --- | --- |
| `run` | [`rq.QuestRun`](../types/rq.QuestRun.md) `\|nil` | nil in town. |

See also: [`rq.quests.set_run`](rq.quests.md#rqquestsset_run)

### rq.quests.set_run

```lua
rq.quests.set_run(fields)
```

`since 2.39.0` `changed 2.42.0`

Changes the counters, bonuses and rules of the quest being played.

The quest panel on the map is drawn again: the EXP bonus, the bonuses, AREA DISPLAY and the PARTY
button follow. A bonus that reaches its maximum shows the game's flash on the map, as a level-up or
a placed enemy does. The progress is written as given, up or down; the game's quests raise it at
their own moments. The fights, the EXP total, the fee and the gold base are read only: the game's
systems make them. The quest's script sets its rules at the start and in some
areas, so a rule written early can be written again by the quest; set it from `rq.dungeon.on_area`
to keep it.

Raises an error outside a quest, for a field it does not write, or a value out of range.

```lua
-- Every quest gives twice the fame and starts with 10 more EXP bonus.
rq.quests.on_event_after(function(ev)
  if ev.kind ~= "start" then return end
  local run = rq.quests.run()
  rq.quests.set_run({ fame = run.fame * 2, exp_bonus = math.min(50, run.exp_bonus + 10) })
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `fields` | [`rq.QuestRunEdit`](../types/rq.QuestRunEdit.md) | The fields to write. |

> Changed in 2.42.0: Writes `progress`.

See also: [`rq.quests.run`](rq.quests.md#rqquestsrun)

## Events

| Name | Summary |
| --- | --- |
| [`rq.quests.on_clear`](#rqquestson_clear) | Registers a function that runs when a quest is cleared. |
| [`rq.quests.on_end`](#rqquestson_end) | Registers a function that runs when a quest ends, however it ends. |
| [`rq.quests.on_event`](#rqquestson_event) | Registers a function that runs before the game handles a quest moment. |
| [`rq.quests.on_event_after`](#rqquestson_event_after) | Registers a function that runs after the game handled a quest moment. |
| [`rq.quests.on_take`](#rqquestson_take) | Registers a function that runs when the player presses Take on the quest list. |

### rq.quests.on_clear

```lua
rq.quests.on_clear(fn) -> fun()
```

`since 0.7.0` `changed 0.23.0` `changed 2.41.0`

Registers a function that runs when a quest is cleared.

It runs only for a clean clear, not for an abandon, an escape or a defeat, at the end of the game's
`クエスト終了処理／クリアフラグ` (wrapped the first time this is used). Characters recruited with
`rq.chara.recruit` and quests opened with `rq.quests.unlock` in the callback join the game's "new
this run" lists, so the victory screen shows them. Up to 16 callbacks; an error in one is written to
the log.

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ctx:` [`rq.QuestClearCtx`](../types/rq.QuestClearCtx.md) `)` | Gets the cleared quest. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

> Changed in 0.23.0: Returns a remover.

> Changed in 2.41.0: The ctx has `id` for a mod's quest.

See also: [`rq.quests.on_end`](rq.quests.md#rqquestson_end)

### rq.quests.on_end

```lua
rq.quests.on_end(fn) -> fun()
```

`since 0.9.0` `changed 0.23.0` `changed 2.41.0`

Registers a function that runs when a quest ends, however it ends.

It runs at the start of the game's `クエスト終了処理` (wrapped the first time this is used). Up to 16
callbacks; an error in one is written to the log.

```lua
rq.quests.on_end(function(ctx)
  if not ctx.cleared then rq.log("quest", ctx.quest, "ended with", ctx.result) end
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ctx:` [`rq.QuestEndCtx`](../types/rq.QuestEndCtx.md) `)` | Gets the quest and how it ended. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

> Changed in 0.23.0: Returns a remover.

> Changed in 2.41.0: The ctx has `id` for a mod's quest.

See also: [`rq.quests.on_clear`](rq.quests.md#rqquestson_clear)

### rq.quests.on_event

```lua
rq.quests.on_event(fn) -> fun()
```

`since 0.18.0` `changed 0.23.0` `changed 2.41.0`

Registers a function that runs before the game handles a quest moment.

It hooks the game's `クエスト処理`. Return nothing to let the game handle it, or a number to skip the
game's handling: 0 continues the quest, other values end it (1 returns to town). Do not play a scene
on `map_load`; the map is not ready. A mod's own map objects (`rq.dungeon.on_object`) do not reach it.
A mod's own quest (`rq.quests.define`) gets `start` before its `run`; a number returned there ends
the quest before `run`.

```lua
rq.quests.on_event(function(ev)
  if ev.kind == "chest" then rq.log("chest at event", ev.no) end
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ev:` [`rq.QuestEvent`](../types/rq.QuestEvent.md) `): integer\|nil` | Returns nil, or the result that replaces the game's handling. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

> Changed in 0.23.0: Returns a remover.

> Changed in 2.41.0: The ev has `id` for a mod's quest.

See also: [`rq.quests.on_event_after`](rq.quests.md#rqquestson_event_after)

### rq.quests.on_event_after

```lua
rq.quests.on_event_after(fn) -> fun()
```

`since 0.18.0` `changed 0.23.0` `changed 2.41.0`

Registers a function that runs after the game handled a quest moment.

`ev.result` is what the game returned. Return a number to change it, or nothing to keep it. A mod's
own map objects (`rq.dungeon.on_object`) do not reach it.

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ev:` [`rq.QuestEvent`](../types/rq.QuestEvent.md) `): integer\|nil` | Returns nil, or the result to use instead. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

> Changed in 0.23.0: Returns a remover.

> Changed in 2.41.0: The ev has `id` for a mod's quest.

See also: [`rq.quests.on_event`](rq.quests.md#rqquestson_event)

### rq.quests.on_take

```lua
rq.quests.on_take(fn) -> fun()
```

`since 2.23.0` `changed 2.41.0`

Registers a function that runs when the player presses Take on the quest list.

It runs before the game's "Take Quest?" question and before the autosave that comes with a Yes.
The callback may wait, for example on `rq.ui.ask` or `rq.ui.confirm`. What it returns decides:
- nil: the game goes on as usual, with its question unless the player turned it off.
- true: the quest is taken, with no question.
- false: the quest is not taken, and the list stays.

Callbacks run in the order they were added (mods in load order); the first one that returns
something other than nil decides, and the rest do not run. An error is logged and counts as nil.
Only the quest list's Take: not `rq.quests.start`, nor a quest the game starts by itself.

```lua
rq.quests.on_take(function(ctx)
  if ctx.quest ~= 80 then return nil end
  return rq.ui.confirm("Pay 100 gold to take it?") == true
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ctx:` [`rq.TakeContext`](../types/rq.TakeContext.md) `): boolean\|nil` | nil for the game's way, true to take the quest, false not to. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

> Changed in 2.41.0: The ctx has `id` for a mod's quest.
