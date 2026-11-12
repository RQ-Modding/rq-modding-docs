# Monsters and enemy groups

The game's monsters can be read and changed since loader 2.36.0
([`rq.monster`](../reference/api/rq.monster.md)): `get`, `edit` and `on_create`. Since 2.40.0 a mod
can add monsters of its own (`rq.monster.define`), with a capture and drops, and enemy groups of its
own for random fights (`rq.monster.group`, `rq.encounters.set_groups`) and for a fight it opens
(`rq.battle.start`'s `group`). Each example on this page is a whole `init.lua`; set `loader` to
`2.36.0` in its `mod.json` for the first section, `2.40.0` for the rest.

New monsters are built from the game's own pieces: each one wears a game monster's 3D model, at its
size or another (`rq.monster.model`). New models are not part of this.

## The game's monsters

The game builds every enemy from its list each time a fight opens, then applies the world's rules:
in worlds 2 and 3 more HP, attack, defense and magic, a tier from ×2 to ×7 and a marked name; race
60 stronger; a boss fight's `strong` ×1.3.

- `rq.monster.get(no)` gives a monster's data from the list: the name, the stats with
  `rq.chara.get`'s names, its five `skills` and the `lines` the fight shows. These are the list's
  numbers, before the world's rules. Since 2.40.0 also `kills` (how many the party has defeated)
  and `weak_known` (the party knows its weak point).
- `rq.monster.edit(no, patch)` changes a monster each time the game builds it. The world's rules
  still scale the new numbers, as they scale the game's. `skills` goes by position (`false` empties
  one) and `lines` by kind. Each mod keeps one patch per monster; `nil` removes it.
- `rq.monster.on_create(fn)` sees each enemy a fight builds, and the party's familiar, after the
  world's rules and before the fight opens. Its name, level, HP and stats can be changed there.

Cockroaches renamed and tougher everywhere, and every boss a fifth stronger:

```lua
local COCKROACH = rq.ids.monster.COCKROACH
rq.monster.edit(COCKROACH, { name = "Armored Cockroach", def = 50, lines = { attack = "Skitter!" } })

rq.monster.on_create(function(ctx)
  if ctx.familiar or ctx.fight_rank ~= 2 then return end -- 2: a boss fight
  ctx.hp = ctx.hp * 1.2
  ctx.atk = ctx.atk * 1.2
end)
```

`edit` sits at the top level; `get` reads the game, so call it from a callback.

## A monster of your own

`rq.monster.define` makes a new monster from a game monster (`base`) and any field `edit` takes. The
game builds it as it builds the base: the same model and motions, the same world's rules. Its
number is 1000 + a hash of its id, so it is the same every run and safe in a save; the calls that
take a monster take its id too.

```lua
local ROACH = rq.ids.monster.COCKROACH
local KING = rq.monster.define({
  id = "mymod:king_roach", base = ROACH,
  name = "King Roach", hp = 900, atk = 300, level = 20,
  skills = { [2] = false },
  lines = { wait = "The King Roach clicks its mandibles." },
})

rq.debug.action({
  id = "king-fight", label = "Fight the King Roach", key = "9",
  onPress = function()
    rq.spawn(function()
      rq.battle.start({ enemies = { 0, "mymod:king_roach", 0 }, exp = 800 })
    end)
  end,
})
```

What to know:

- An `edit` of the base does not reach the new monster; an `edit` of its own id does.
- The game counts it as its own: its kills and whether its weak point is known are kept in the
  save under its id, and `get` returns them.
- It can be a familiar: an item with `subtype = 20` whose first effect is its number (see
  [`rq.item`](../reference/api/rq.item.md)).
- Two ids can hash to the same number. `define` then raises an error naming both; change one id.

## Capture

The game's capture skills (the two Capture skills, 166 and 451, and Capture Thread, 531) catch a girl monster under the game's rules:
low HP, the chance, room in the quest storage, not in a boss fight. A mod's monster with `capture`
is caught the same way and gives its item, with the scene's picture and text. Without `capture` it
always escapes, as a monster the game has no item for.

```lua
local CAN_CAN = rq.ids.monster.CAN_CAN
local JELLY = rq.monster.define({
  id = "mymod:jelly", base = CAN_CAN, name = "Blue Jelly", hp = 300,
  capture = {
    item = "mymod:jelly_familiar",
    cg = rq.image.add("mymod:jelly_cg", "cg/jelly.png"),
    text = "【Blue Jelly】$\"You caught me...\"",
  },
})

rq.item.define({
  id = "mymod:jelly_familiar", name = "Blue Jelly", type = "item", subtype = 20, icon = 6500,
  info = "A familiar.$It wobbles.",
  effects = { { kind = 0, value = JELLY }, { kind = 0, value = 1 }, { kind = 0, value = 100 } },
})
```

The item's three effects are the monster, the class (1 to 4) and the growth. Its icon must be one
of the game's familiar icons (6500 to 6516, or 6632), or the familiar never takes a turn.

## Drops

`drops` gives a monster up to 8 items with a chance from 1 to 100, on `define` or on `edit` of any
monster. After a won fight with no item yet and room in the quest storage, each enemy defeated, in
rank order, rolls its drops; the first that rolls is the fight's one item. The roll is the game's
own, so `rq.random.fix` fixes it.

```lua
rq.item.define({ id = "mymod:shell", name = "Roach Shell", price = 50, info = "Hard and shiny." })
rq.monster.edit(rq.ids.monster.COCKROACH, { drops = { { item = "mymod:shell", chance = 25 } } })
```

The drop is rolled before every mod's `rq.battle.on_end`, so `rq.battle.get_drop()` sees it and
`set_drop` can change it. A fight that already has an item (a capture, a `set_drop` in `on_start`)
rolls none, and a drop that rolls takes the place of the game's own later drops.

## Enemy groups

On a quest's map the game draws random fights, and the enemies standing on the map, from the area's
groups: up to five per area. A group is a line-up of up to five enemies, the fight's EXP and its
rank. `rq.monster.group` makes one:

```lua
local ROACH = rq.ids.monster.COCKROACH
local SWARM = rq.monster.group({
  id = "mymod:swarm", name = "Roach Swarm", exp = 120, rank = 5,
  lineups = {
    { 0, ROACH, 0 },
    { ROACH, ROACH },
    { ROACH, "mymod:king_roach", ROACH },
  },
})
```

The line-up is drawn as the game draws its own: a number from 1 to 5 (not the last fight's twice)
picks one of `lineups` in turn, so 5 line-ups are drawn evenly and fewer repeat. A 6th line-up is
only for an enemy standing on the map, one time in 3. `name` is what the game's log shows; worlds 2
and 3 add 2 and 4 to `rank`, as they do to the game's groups.

`rq.encounters.set_groups(list)` writes the area's list, as the area's script does. The game writes
each area's own list when the party enters it, so set yours from `rq.dungeon.on_area`. The game's
groups (2 to 135) and a mod's mix:

```lua
rq.dungeon.on_area(function(ctx)
  if ctx.quest == 126 then
    rq.encounters.set_groups({ "mymod:swarm", 47 })
  end
end)
```

`{}` leaves the area with no random fights. A fight a mod opens can take a group too:
`rq.battle.start({ group = "mymod:swarm" })` draws a line-up and pays the group's EXP, unless `exp`
is given.

## A bigger model

`rq.monster.model` adds a game model at another size or place, for a monster's `model` field.
`rq.monster.models()` lists the game's model table (the model numbers `get` gives) with the ones
mods made.

```lua
local ROACH = rq.ids.monster.COCKROACH
local BIG = rq.monster.model({ id = "mymod:big_roach", base = 100122, scale = 0.8 }) -- the Cockroach's at twice its size
rq.monster.define({ id = "mymod:big_roach", base = ROACH, name = "Giant Roach", model = BIG, hp = 1500 })
```

The number `model` returns comes from the order of the calls in a run: give it to a monster, but
do not keep it in a save.

## When a mod is gone

A save made with a mod's monsters and groups still loads without the mod. A monster number of 1000
or more that no mod defines is built as the game's Data-less Ghost (a familiar item, a line-up), and
a group no mod defines in an area's list becomes the area's first game group (group 135 when it has
none). Each is logged once.
