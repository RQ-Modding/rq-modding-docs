# Quests and maps

Loader 2.39.0 lets a mod read and change a quest as the quest list shows it, and change the
counters and rules of the quest being played. On a quest's map, a mod can list, remove and place
objects, put its own objects with Lua behind them, and change the traps. A mod's object looks like
one of the game's own props: a chest, a spring, a marker and so on. Since 2.41.0 a mod can also add
quests of its own with no map: [Quests of your own](new-quests.md).

## A quest's data

`rq.quests.get(no)` returns what the quest list shows: the name, the five lines of text, the
place, the difficulty, the fame a clear gives, the counts and the conditions to take it.

```lua
local q = rq.quests.get(126)
rq.log(q.name .. ": difficulty " .. q.difficulty .. ", " .. #q.conditions .. " conditions")
for _, c in ipairs(q.conditions) do
  rq.log(c.kind, c.text, c.met and "met" or "not met")
end
```

Each condition is a table with a `kind`: `party_max` (`count`), `member` (`chara`), `own` (`charas`,
two characters), `member_level` (`chara`, `level`), `item` (`item`) or `special` (the story's own
rule; its text is in `special`). `text` is the line the list writes, and `met` says whether the
party meets it now. `kind` gives the list's marks: `"quest"` (a quest with a map), `"fights"` (fights
and no map) or `"menu"` (no map and no fights: a story quest, or a menu such as Alice's Mansion).

### Changing a quest

`rq.quests.edit(no, patch)` changes the `name`, `description`, `place`, `difficulty` and
`conditions`. A harder quest 126:

```lua
rq.quests.edit(126, {
  difficulty = 90,
  conditions = { { kind = "member_level", chara = rq.ids.chara.RANCE, level = 60 } },
})
```

The game writes every quest's data again at the start, after a load, at a world transfer and each
time the quest menu opens. The loader puts the patch back on top each time, so call `edit` once, at
the mod's top level: before a save loads, the patch waits for the game's data. Nothing goes in the
save. Without the mod, the game's next writing brings its own data back.

Each mod has one patch per quest. A second call from the same mod replaces it, and `edit(no, nil)`
removes it. Patches from several mods apply in load order, field by field: a later mod's name wins,
and a field it leaves out keeps the earlier mod's. `get(no).edited` names the mods with a patch on
the quest.

The fame a clear gives is not in a patch: the game halves it after each clear, and the save keeps
it. Change what one run gives with `set_run` (below).

### A condition of your own

A patch's `condition` is a text and a function. While the function returns false, the quest shows
the text as the game's special condition: the list writes it and greys Take. The function runs
when the quest menu opens, at `rq.quests.refresh()` and at `rq.quests.can_take`. A quest that needs
three shrines found:

```lua
rq.quests.edit(126, { condition = {
  text = "Find the three shrines",
  ok = function() return rq.store.get("shrines", 0) >= 3 end,
} })
```

The quest's own conditions stay. When it already has a special condition, the texts are joined with
" / ". A quest with three conditions has no room for one more: the call raises an error.

## The quest being played

`rq.quests.run()` returns the counters of the quest being played, or nil in town: the progress,
the fights, the placed enemies beaten, the EXP so far, the fame a clear gives now, the appraisal
fee, the EXP bonus, the bonuses (`feats`, `level_ups`, `enemies`, each `{ count, max }`, nil when
the quest has none) and its rules: `party_change` (`"normal"`, `"none"` or `"free"`),
`no_area_map` and `no_warp`.

`rq.quests.set_run(fields)` writes `fame`, `exp_bonus` (0 to 50, the game's cap), the bonuses,
`party_change`, `no_area_map`, `no_warp` and, since 2.42.0, `progress` (the percent on the map
panel, 0 to 100, also lower than before). The quest panel shows the change at once, and a bonus
that reaches its maximum shows the game's flash. A run that pays double fame:

```lua
rq.quests.on_event_after(function(ev)
  if ev.kind == "start" then
    local r = rq.quests.run()
    rq.quests.set_run({ fame = r.fame * 2 })
  end
end)
```

A bonus the quest does not have is turned on by giving its `max`; `false` turns one off. A count
above the maximum is cut to it. The EXP so far, the gold and the fee are read only: the game's own
systems make them.

## Objects on a map

`rq.dungeon.objects()` lists the objects of the current area: chests, warps, events, springs,
traps, placed enemies and the rest, each with its cell (`x`, `z`) and `kind`.
`rq.dungeon.remove(x, z)` takes one away for the rest of the quest. A warp cannot be removed: the
map would lose its way on. A quest with no traps:

```lua
rq.dungeon.on_area(function()
  for _, o in ipairs(rq.dungeon.objects() or {}) do
    if o.kind == "trap" then rq.dungeon.remove(o.x, o.z) end
  end
end)
```

`rq.dungeon.place` puts the game's own objects on a free floor cell: a chest, a red chest, a
spring, an achievement, EXP, gold, and since 2.39.0 a trap, a placed enemy (the game picks the
fight, and a fight won counts for the placed-enemy bonus; as with the game's own, the touch may be
one of the quest's meetings, such as the adventurers, once a quest) and the escape device.

### An object of your own

`rq.dungeon.place("custom", x, z, { id = ..., look = ... })` puts a mod's own object. A step on it
runs the function `rq.dungeon.on_object` registered for its id. The function may wait: ask with
`rq.ui.confirm`, show `rq.ui.notice`, start a fight with `rq.battle.start`. An altar that starts a
fight, and stays until the party wins:

```lua
rq.dungeon.on_object("mymod:altar", function(ctx)
  if rq.ui.confirm("Touch the altar?") then
    local r = rq.battle.start({ enemies = { 0, rq.ids.monster.COCKROACH, 0 }, boss = true })
    if r ~= "won" then ctx.keep = true end
  else
    ctx.keep = true
  end
end)

rq.dungeon.on_area(function(ctx)
  if ctx.quest == 126 and ctx.area == 1 and ctx.first then
    local g = rq.dungeon.grid()
    rq.dungeon.place("custom", g.player.x + 2, g.player.z, { id = "mymod:altar", look = "event-2" })
  end
end)
```

- **The look** is one of the game's props, by name: `rq.dungeon.looks()` lists them. `hidden` shows
  nothing, as the game's silent events. The look is only what is drawn: a step runs the object's
  function whatever its look, so a `spring` look does not heal and a `gold` look gives no gold.
- **Once or kept.** As the game's events, the object is used once: it is gone before the function
  runs. With `keep = true` in `place` it comes back on its cell after every step, and
  `ctx:remove()` takes it away. `ctx.keep = true` in the function brings it back after this step
  only: at the next step `ctx.keep` starts again as `place`'s `keep`, as in the altar above.
- **The quest's end.** The function returns nil or 0 to go on, `"clear"` (or 1) to clear the quest,
  `"escape"` (4) to end it as the escape device does (the items kept), `"fail"` (2) and `"abandon"`
  (3) as a defeat and a give-up. The words came in 2.42.0, as a mod's own quest's `run` returns them.
- **Areas and saves.** The object stays on its cell for the whole quest, when the party leaves the
  area and comes back, and in a save made on the map. Register `on_object` at the mod's top level, so
  those objects answer after a load. An object whose id has no function logs a line and does nothing.
- `rq.quests.on_event` does not see a mod's objects: each object's function is its own.

Use ids with the mod's name in them, such as `"mymod:altar"`: the loader makes the object's number
from the id, and two ids with the same number raise an error.

## Traps

A trap stepped on draws its kind from the area's weights: sloth shrooms (a member leaves the
party), an electric current (25% of the party's HP), an alarm (a fight) and a pitfall.
`rq.dungeon.traps()` reads the weights, 0 to 10 each, and `rq.dungeon.set_traps` writes them. The
area's script writes them again when the party enters an area, so set them from
`rq.dungeon.on_area`:

```lua
rq.dungeon.on_area(function() rq.dungeon.set_traps({ shroom = 0, alarm = 6 }) end)
```

`rq.dungeon.on_trap` runs after the game drew the kind, before the scene. Write `ctx.kind` and
`ctx.chance` (the chance to avoid the trap: 20, 50 with a ranger in the party, 100 with Trap
Evasion), or set `ctx.cancel` to remove the trap with no scene. Harder traps:

```lua
rq.dungeon.on_trap(function(ctx)
  if ctx.chance < 100 then ctx.chance = ctx.chance // 2 end
end)
```

Callbacks run in turn, each seeing what the one before left. The scene still names the game's
chance. It runs for the game's traps and for those a mod placed.

## Not yet

These are on the [Roadmap](../roadmap.md):

- New 3D models, rooms of a mod's own and warps off the 4 by 4 grid (phase P). New monsters and
  enemy groups for the game's areas came in 2.40.0 ([Monsters and enemy groups](monsters.md)),
  quests of a mod's own in 2.41.0 and their maps of the game's rooms in 2.42.0 ([Quests of your
  own](new-quests.md)).
- A trap with a mod's own text and effect: a custom object does it today.
- Writing the run's EXP so far, its gold and fee.
