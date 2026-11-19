# Quests of your own

Since loader 2.41.0 a mod can add quests to the quest list ([`rq.quests.define`](../reference/api/rq.quests.md)):
a story, a quest of fights, a menu, a chain of quests. Since 2.42.0 a quest can also have a map,
built from the game's own rooms ([A quest with a map](#a-quest-with-a-map)). The player takes one
from the list as a game quest, with the autosave and the try counted, and the game's result screen
ends it. Each example on this page is a whole `init.lua`; set `loader` to `2.41.0` in its
`mod.json`, or `2.42.0` for a map.

## A story quest

`run(q)` is the quest's script. It runs when the quest starts, in place of a game quest's own, and
may wait as long as it likes: scenes, fights, choices, dialogs. What it returns ends the quest.

```lua
rq.item.define({ id = "mymod:lotion", name = "Dancer's Lotion", price = 200, info = "It smells of roses." })

rq.quests.define({
  id = "mymod:lotion_quest",
  name = "The Lost Lotion",
  text = { "A dancer lost her lotion in the bathhouse.", "She will pay well to get it back." },
  place = "Copan Empire",
  fame = 5,
  open = true,
  run = function(q)
    local pick = rq.scene.play(function(s)
      s.narrate("The bathhouse is quiet. Two doors lead on.")
      return s.choice({ "The steam room", "The cold pool" })
    end)
    if pick == 2 then
      rq.scene.play(function(s) s.narrate("Only cold water here. Nothing to find.") end)
      return "abandon"
    end
    rq.scene.play(function(s) s.narrate("A small bottle shines on the bench.") end)
    rq.item.give("mymod:lotion", { place = "quest" })
    return "clear"
  end,
})
```

`run` returns how the quest ends, and the game takes it from there:

| `run` returns | The game |
| --- | --- |
| `"clear"`, or nothing | The success screen: the fame, the quest storage's items appraised, the clear counted, the quest shown as cleared. |
| `"fail"` | The failure screen, as when the party loses. |
| `"abandon"` | Given up: the quest storage's items are lost. |
| `"escape"` | Given up with the items kept, as with the escape device. |

The story can also live in a scene file, with the quest's end written in it: see
[A quest's run](scenes.md#a-quests-run) in the Scenes guide.

An error in `run` is written to the log and gives the quest up. `q` holds the quest's `id`, its
number `no`, its `tries` (this one included) and `clears`, and `first` while it was never cleared.

A cleared quest stays in the list and can be taken again. A quest with no fights gives its fame on
its first clear only; one with `fights = true` gives half of it again after each clear, as the
game's quests do.

## An arena

`fights = true` puts the list's battle mark on the quest. A fight from `run` is a fight of the
game's own (`rq.battle.start`), and a loss can end the quest as a failure.

```lua
local ROACH = rq.ids.monster.COCKROACH

rq.quests.define({
  id = "mymod:arena",
  name = "The Roach Pit",
  text = "Three fights in a row.\nNo rest between them.",
  place = "Rance Castle",
  fights = true,
  difficulty = 10,
  fame = 30,
  open = true,
  run = function(q)
    for round = 1, 3 do
      rq.scene.play(function(s) s.narrate("Round " .. round .. "!") end)
      local result = rq.battle.start({ enemies = { ROACH, ROACH, ROACH }, exp = 200 * round })
      if result ~= "won" then return "fail" end
    end
    return "clear"
  end,
})
```

After a lost fight the fallen are out of the party when the quest ends, so the player picks a party
again before the next try.

## A menu

A quest can be a place the player visits: a choice in a loop, left when the player says so. With
no fights it shows no mark, as the game's own menus.

```lua
rq.quests.define({
  id = "mymod:fortune",
  name = "The Fortune Teller",
  text = "She reads your future for 100 gold.",
  place = "Cidade",
  open = true,
  run = function(q)
    while true do
      local pick = rq.scene.play(function(s)
        s.narrate("\"Well, traveller?\"")
        return s.choice({ "Read my future (100 G)", "Leave" })
      end)
      if pick ~= 1 then return "clear" end
      if rq.game.gold() < 100 then
        rq.scene.play(function(s) s.narrate("\"Come back with money.\"") end)
      else
        rq.game.add_gold(-100)
        rq.scene.play(function(s) s.narrate("\"I see... a great many cockroaches.\"") end)
      end
    end
  end,
})
```

## A chain

A quest starts locked (`open` left out). `after` opens it when another quest is cleared, by its
number or its id; the victory screen lists it with the game's new quests. `rq.quests.unlock(id)`
opens one from anywhere in the mod.

```lua
rq.quests.define({
  id = "mymod:lotion_thanks",
  name = "The Dancer's Thanks",
  text = "She has something for you.",
  after = "mymod:lotion_quest",
  run = function(q)
    rq.scene.play(function(s) s.narrate("She hands you a small purse.") end)
    rq.game.add_gold(500)
  end,
})
```

Conditions to take part work as on a game quest (`conditions`, as
[`rq.quests.edit`](quests-maps.md#changing-a-quest) takes them), and so does a condition of the
mod's own, which greys Take with its text until it is met:

```lua
rq.quests.define({
  id = "mymod:night_watch",
  name = "Night Watch",
  conditions = { { kind = "party_max", count = 2 } },
  condition = { text = "Needs the watchman's key", ok = function() return rq.store.get("key") == true end },
  open = true,
  run = function(q) return "clear" end,
})
```

## A quest with a map

`map` gives the quest a dungeon of the game's rooms. The list shows the map mark, and the player
walks it as a game quest's: the areas, the warps between them, random fights, the placed enemies,
chests, traps and achievements, the map panel and the area map. Nothing on it is new 3D: each area
is one of the game's stock rooms in one of its tilesets, or one of its fixed maps.

```lua
rq.quests.define({
  id = "mymod:old_mine",
  name = "The Old Mine",
  text = { "Something glitters at the bottom of the mine.", "Bring it back." },
  place = "Leazas",
  difficulty = 8,
  fame = 40,
  open = true,
  map = {
    tileset = rq.ids.map_kind.CAVE,
    name = "Old Mine",
    gold = 60,
    loot = "B",
    groups = { 47, 49 },
    traps = { shroom = 3, shock = 2, pit = 1 },
    areas = {
      [1] = { exits = "E", enemies = 2, chests = 1 },
      [2] = { exits = "WS", enemies = 3, traps = 2, feats = 1 },
      [6] = { exits = "N", chests = 2, objects = {
        { kind = "custom", id = "mymod:glitter", look = "event-3", spot = "wide", run = function(ctx)
          rq.scene.play(function(s) s.narrate("A vein of gold. Enough for the whole guild.") end)
          return "clear"
        end },
      } },
    },
  },
})
```

The areas sit on the game's 4 by 4 grid: area 1 at the north-west, 4 at the north-east, 16 at the
south-east. An exit `E` leads to the next area (+1), `W` to the one before (−1), `S` to the one
below (+4) and `N` to the one above (−4). Each passage needs both sides: area 1's `E` and area 2's
`W`. `define` refuses a map whose exits lead off the grid or to an area with no way back, and an
area the party cannot reach from the first one.

The map's settings are the quest's; an area may give its own `tileset`, `name`, `gold`, `loot`,
`music`, `background` and `groups`:

| Field | What it sets |
| --- | --- |
| `tileset` | The rooms' look, the fight background and the music (`rq.ids.map_kind`, [the table below](#the-tilesets-and-the-rooms)). |
| `name` | The name on the map panel. |
| `gold` | A fight's gold. Default 50. |
| `loot` | What the chests hold: `"C"`, `"B"`, `"A"` (equipment of that rank), `"C+"`, `"B+"`, `"A+"` (with an item bonus), `"A++"` (rank A with a superior item). Left out: by Rance's level. The appraisal fee follows. |
| `music`, `background` | The map's music and the fight background, when not the tileset's. |
| `traps` | The weights, 0 to 10, of `shroom`, `shock`, `alarm` and `pit` (all 0: every trap is a shock). |
| `groups` | The enemy groups of the random fights and the placed enemies: the game's numbers or a mod's group ids ([Monsters and enemy groups](monsters.md)). |
| `bonuses` | The quest bonuses' goals: `feats`, `enemies`, `level_ups`. |
| `start` | The first area. Default: the lowest one. |
| `chatter` | `false` holds back the party's lines after new areas. |

An area's `enemies`, `chests`, `traps` and `feats` are counts, placed on spots the game draws as for
its own quests. `chests` follows the game's own draw too: each one is a red chest half the time and
nothing the other half, so `chests = 2` gives one red chest on average. A chest that must be there
goes in `objects`. `objects` is a list for anything more: one of the game's objects (`kind` as
[`rq.dungeon.place`](quests-maps.md#objects-on-a-map) names them) with a `spot` (`"any"`, `"wide"`
or a cell `{ x, z }`) and a chest's `item`, or an object of the mod's own (`kind = "custom"`) with an
`id`, a `look`, `keep` and `run(ctx)`. They are placed on the area's first entry in each run.

A custom object's `run` is called when the party steps on it, as an
[`rq.dungeon.on_object`](quests-maps.md#an-object-of-your-own) function. It returns nothing to go on,
or how the quest ends: `"clear"`, `"fail"`, `"abandon"` or `"escape"`, as `run` does on a quest with
no map. There is no goal of the loader's own: an object ends the quest.

`run` is the prologue on a quest with a map. It runs before the first area, and returning nothing
goes on to the map; a result ends the quest there. Left out, the quest goes straight to the map.

## A boss at the end

The boss stands on the room's wide spot, the open middle of a large room. Its fight is a game fight
with the boss's rules (no escape, the boss music), and a loss ends the quest as a failure.

```lua
rq.monster.group({ id = "mymod:queen", enemies = { 0, rq.ids.monster.COCKROACH, 0 } })

rq.quests.define({
  id = "mymod:roach_queen",
  name = "The Roach Queen",
  text = "She rules the cellar.",
  place = "Rance Castle",
  open = true,
  map = {
    tileset = rq.ids.map_kind.BUILDING,
    groups = { 47 },
    bonuses = { enemies = 3 },
    areas = {
      [1] = { exits = "S", enemies = 3 },
      [5] = { exits = "N", room = 203, objects = {
        { kind = "custom", id = "mymod:queen_throne", look = "event-4", spot = "wide", run = function(ctx)
          if rq.battle.start({ group = "mymod:queen", boss = true }) ~= "won" then return "fail" end
          rq.quests.set_run({ progress = 90 })
        end },
        { kind = "custom", id = "mymod:cellar_door", look = "event", keep = true, run = function(ctx)
          return "clear"
        end },
        { kind = "escape" },
      } },
    },
  },
})
```

The queen's object goes after her fight (`keep` left out); the door stays (`keep = true`) and ends
the quest when the party chooses. `set_run`'s `progress` is the percent on the map panel.

## A room of your choice

`room` picks one of the tileset's stock rooms in place of the game's draw, and `fixed` one of the
game's fixed maps, with its own look and layout (its exits must be among the fixed map's). A chest's
`item` holds a given item, the mod's own among them.

```lua
rq.item.define({ id = "mymod:old_key", name = "Old Key", type = "item", price = 10, info = "It opens something." })

rq.quests.define({
  id = "mymod:key_room",
  name = "The Key Room",
  open = true,
  map = {
    tileset = rq.ids.map_kind.CASTLE,
    groups = { 47 },
    areas = {
      [1] = { exits = "E", room = 1 },
      [2] = { exits = "W", room = 302, objects = {
        { kind = "red-chest", item = "mymod:old_key" },
        { kind = "custom", id = "mymod:key_room_exit", keep = true, run = function() return "clear" end },
      } },
    },
  },
})
```

The item found goes into the quest storage, and it may be unidentified, as any chest's item (the
game identifies a set item 1 time in 3). Then the player pays the appraisal fee at the end to keep
it: Finish discards what is not identified. A red chest can
also explode and lose it. Give an item that must not be lost with `rq.item.give` from the object
that ends the quest.

## A lever

`setup(ctx)` runs at each entry to an area, after the game's own setup: for what the fields do not
say. Here a lever opens the way south, with `rq.quests.set_run`'s `no_warp` (the warps refused):

```lua
local pulled = false

local function gate(ctx)
  rq.quests.set_run({ no_warp = { south = ctx.area == 5 and not pulled } })
end

rq.quests.define({
  id = "mymod:lever",
  name = "The Sunken Gate",
  open = true,
  map = {
    tileset = rq.ids.map_kind.WATER_CAVE,
    groups = { 47 },
    areas = {
      [1] = { exits = "S", setup = gate },
      [5] = { exits = "NS", setup = gate, objects = {
        { kind = "custom", id = "mymod:lever_handle", look = "event-3", keep = true, run = function(ctx)
          if pulled then return end
          pulled = true
          rq.quests.set_run({ no_warp = { south = false } })
          rq.scene.play(function(s) s.narrate("Somewhere below, a gate grinds open.") end)
        end },
      } },
      [9] = { exits = "N", setup = gate, chests = 3, objects = {
        { kind = "custom", id = "mymod:lever_exit", keep = true, run = function() return "clear" end },
      } },
    },
  },
  run = function(q)
    pulled = false
  end,
})
```

`ctx` holds the quest's `id` and number `quest`, the `area`, its `row` and `col`, and `first`, true
on the area's first entry in the run. A local such as `pulled` lasts while the game runs; for a
state that must survive a save on the map, keep it in [`rq.savedata`](save-data.md).

## The tilesets and the rooms

The game's stock rooms come in 13 tilesets (`rq.ids.map_kind`):

| Tileset | Number | Rooms |
| --- | --- | --- |
| `CAVE` | 1 | 1, 2, 101, 102, 201 to 204, 301, 302 |
| `FOREST` | 2 | the same |
| `BUILDING` | 3 | the same |
| `SNOW` | 4 | the same |
| `CASTLE` | 5 | the same |
| `FIELD` | 6 | the same |
| `MOUNTAIN` | 7 | the same |
| `WATER_CAVE` | 9 | the same |
| `BURNING_FOREST` | 10 | the same |
| `WATERSIDE` | 13 | the same |
| `MALGRID` | 14 | the same, and 401 to 409 |
| `MALGRID_X` | 20 | the same, and 401 to 409 |
| `MALGRID_X_DEEP` | 21 | the same, and 401 to 409 |

The other tilesets (Ruins, Tower, Road, Camp, Abyss, Dream World, Kaiz Underground, Passageway,
Secret Base) have only fixed maps: an area there needs `fixed`.

Every stock room has the cells of all four exits, so any exits fit any room. The rooms differ in
shape and in their spots:

| Room | Shape | Spots | Wide spots |
| --- | --- | --- | --- |
| 1 | An east–west corridor | 17 | 1 |
| 2 | An east–west corridor | 20 | 2 |
| 101, 102 | North–south rooms | 19, 21 | 1 |
| 201 to 204 | General rooms | 20 | 1 |
| 301, 302 | General rooms | 18, 20 | 1 |
| 401 to 409 | Malgrid's rooms | 24 or 25 (406: 20) | 1 |

With `room` and `fixed` left out, the game draws a room from the exits as for its own quests: one of
the six general rooms; with only an east and a west exit, a corridor half the time; with only a
north and a south exit, room 101 or 102 half the time; on the Malgrid tilesets, one of 401 to 409 a
third of the time. A drawn room has at least 17 spots and 1 wide spot.

What to know:

- **The spots.** The counted objects take the spots first, then `objects` at `"any"`. `define`
  refuses an area with more than its room has (17 for a drawn room), or more objects at `"wide"`
  than its wide spots. A cell `{ x, z }` that is not free floor in the room gives a free spot, with
  a line in the log.
- **The rooms are kept.** The rooms the game drew are kept in the save, so every try of the quest
  has the same ones, as in the game's quests. When a new version of the mod changes the map's shape
  (an area's tileset, room or exits), the rooms are drawn anew. The objects are placed anew on each
  try.
- **The party's lines.** After a few new areas the game plays a party member's line or a special
  event, as on its own quests (never on the Building, Snow, Water Cave, Burning Forest and Waterside
  tilesets). `chatter = false` holds them back.
- **The rest of the run** works as on a game quest: [`rq.quests.run` and
  `set_run`](quests-maps.md#the-quest-being-played), the traps, the random fights
  ([`rq.encounters`](game-state.md#random-fights)), `rq.dungeon.on_area` and `rq.music.on_play`.
- `rq.quests.get` gives the map's shape in `map`: `start`, `tileset` and each area's `exits`
  (in the order N, S, E, W), `room`, `fixed` and `tileset`.

## The number and the save

Each quest takes a number from 303 to 500 the first time a save has it, and keeps it in that save.
Another save can give it another number, so keep the id: the quest calls take it where they take a
number (`get`, `edit`, `state`, `set_state`, `unlock`, `start`, `can_take`), `rq.quests.no(id)`
gives the number, and the callbacks' ctx has `id` (`on_clear`, `on_end`, `on_take`, `on_event`).

```lua
rq.quests.on_clear(function(ctx)
  if ctx.id == "mymod:lotion_quest" and ctx.first then
    rq.log("the lotion is back, after " .. rq.quests.get(ctx.id).tries .. " tries")
  end
end)
```

What to know:

- The name, text, place, difficulty and conditions are written again after each load, so a new
  version of the mod shows its new text in an old save. The state, tries, clears and fame are the
  save's.
- `difficulty` is what the list shows in the first world; the game adds 2 per world after it, as to
  its own quests (not to 0).
- A world transfer starts the mods' quests over with the game's: tries, clears and fame, and the
  state back to what `open` and `after` give.
- A save holds up to 198 quests of mods. Past that, a quest is left out with a line in the log.

## When a mod is gone

A save made with a mod's quests still loads without the mod. Each of its quests is hidden (the list
leaves it out and nothing can take it) and its state kept; when the mod is loaded again, the quest
is back as it was. A world transfer made without the mod forgets it: the quest starts over when the
mod comes back.

A save made on a mod's map loads too. The first time the map hands over to the quest (a step on an
object, a fight, the menu) the quest ends as with the escape device, the quest storage's items kept,
with a line in the log.
