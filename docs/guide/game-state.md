# Gold, encounters and levels

The things a first mod usually wants to change have their own calls since loader 2.33.0: the
money and charisma ([`rq.game`](../reference/api/rq.game.md)), random fights on a quest's map
([`rq.encounters`](../reference/api/rq.encounters.md)), EXP and levels
([`rq.chara.add_exp`](../reference/api/rq.chara.md#rqcharaadd_exp), `level_up` and `on_level_up`),
and timers and jobs that wait ([`rq.after`](../reference/api/rq.md#rqafter), `rq.every`,
`rq.spawn`, `rq.wait`). Each example on this page is a whole `init.lua`; set `loader` to `2.33.0`
in its `mod.json`.

All of these read or change the game, so call them from a callback or `rq.on_frame`, not at the
top level of `init.lua` ([When code runs](sandbox.md#when-code-runs)). `rq.encounters.hold` and the
`on_*` calls are the exception: they can sit at the top level.

## Money and charisma

`rq.game.gold()` gives the money, and `set_gold` and `add_gold` change it. The game keeps it from
0 to 999,999,999: a value past either end stops there. Every change redraws the system bar.

Double the gold of every fight on a quest's map. The game pays a fight's gold as its result screen
closes, before `rq.battle.on_end` runs, so the difference is the fight's gold:

```lua
local before = 0

rq.battle.on_start(function()
  before = rq.game.gold()
end)

rq.battle.on_end(function()
  local won = rq.game.gold() - before
  if won > 0 then rq.game.add_gold(won) end
end)
```

The result screen still shows the game's own amount; the system bar shows the money with the
bonus.

Charisma (the game calls it fame) is a rank and the points toward the next one.
`rq.game.charisma()` returns the rank, the points and the points the rank needs. `add_charisma`
works as a quest's result does: points that fill the bar raise the rank once, and the rest waits
for the next one. Taking points away never lowers the rank. `set_charisma(rank, points)` sets both.

```lua
local rank, points, max = rq.game.charisma()
rq.log(("charisma rank %d, %d / %d"):format(rank, points, max))
```

## Random fights

On a quest's map, each step fills the encounter bar. Once it is full, every step has a 1 in 10
chance of a fight with one of the area's enemy groups. How many steps fill the bar is picked again
after each fight and each area change. An area with no groups has no bar and no random fights.
`rq.encounters.info()` gives all of it for the area the party is in, or nil away from a map:

```lua
rq.on_frame(function()
  local e = rq.encounters.info()
  if e and e.on then
    rq.hud.text(10, 40, ("Encounter bar: %d / %d"):format(e.walked, e.steps))
  end
end)
```

No random fights while a setting is on. `rq.encounters.hold(true)` holds them off for this mod: no
random fight starts, the bar is hidden, and the steps walked do not fill it. Each mod has its own
hold, so turning yours off never ends another mod's. An enemy standing on the map still fights.

```lua
local calm = false

rq.debug.action({
  id = "calm-walk",
  label = "Random fights on/off",
  key = "8",
  onPress = function()
    calm = not calm
    rq.encounters.hold(calm)
  end,
})
```

Fights sooner: the bar fills in half the steps. `rq.encounters.on_steps` runs each time the game
picks the steps that fill the bar; a number it returns takes their place (kept from 1 to 999):

```lua
rq.encounters.on_steps(function(ctx)
  return ctx.steps // 2
end)
```

`rq.encounters.set_steps(n)` sets the steps once, until the game picks them again.

No random fights in a quest already cleared. `rq.encounters.on_encounter` runs as a fight from the
map is about to start, and returning false cancels it: the party walks on and the bar starts again
from 0. `ctx.placed` is true for an enemy standing on the map, which this example leaves alone:

```lua
rq.encounters.on_encounter(function(ctx)
  if not ctx.placed and rq.quests.state(rq.quests.current()) == 2 then
    return false
  end
end)
```

## EXP and levels

`rq.chara.add_exp(iic, n)` gives EXP as a fight does. Each time the bar fills, the character goes
up a level with the game's own level-up: the stats grow, a skill point comes, and the EXP left
carries over. It returns the levels gained. A character at 0 HP gets the EXP but no level until it
has HP again, as in the game. `rq.chara.level_up(iic, n)` gives free levels, as the
story and training do, with the EXP back to 0. Neither goes past the character's cap (`level_max`
in [`rq.chara.get`](../reference/api/rq.chara.md#rqcharaget)); Rance, Reset Kalar and Dark Rance
have none for EXP (`uncapped`), and Athena 2.0 stays at level 1, as in the game.

EXP for those who sat a fight out:

```lua
rq.battle.on_end(function(ctx)
  local fought = {}
  for _, iic in ipairs(ctx.allies) do fought[iic] = true end
  for _, u in ipairs(rq.units()) do
    if not fought[u.id] then rq.chara.add_exp(u.id, 50) end
  end
end)
```

`rq.chara.on_level_up` runs after every level, the game's and a mod's, once per level.
`ctx.battle` says whether it came in a fight's result, and `ctx.free` whether it came from the
game's other level-up, which sets the EXP back to 0 (the story, training, the reserve's share of a
fight):

```lua
rq.chara.on_level_up(function(ctx)
  if ctx.level % 10 == 0 then rq.chara.add_skill_points(ctx.iic, 1) end
end)
```

## Waiting and timers

`rq.on_frame` runs on every update of the game, which can be thousands of times a second on a
screen that does not redraw, so counting updates does not measure time. `rq.after(ms, fn)` calls a
function once that many milliseconds have passed, and `rq.every(ms, fn)` calls it again and again
until it returns false. Both return a function that cancels them.

A note for three seconds after each level:

```lua
local note, clear

rq.chara.on_level_up(function(ctx)
  note = rq.chara.get(ctx.iic).short .. " reached level " .. ctx.level
  if clear then clear() end
  clear = rq.after(3000, function() note = nil end)
end)

rq.on_frame(function()
  if note then rq.hud.text(10, 60, note) end
end)
```

For steps with waits between them, run them as a job: `rq.spawn(fn)` runs `fn`, and inside it
`rq.wait(ms)` and `rq.wait_until(cond)` wait while the game goes on. A job may also wait in the
game's own dialogs:

```lua
rq.debug.action({
  id = "gift",
  label = "A gift in town",
  key = "9",
  onPress = function()
    rq.spawn(function()
      rq.wait_until(function()
        local s = rq.ui.get()
        return s and s.screen == "hub"
      end)
      if rq.ui.confirm("Take 1000 gold?") then rq.game.add_gold(1000) end
    end)
  end,
})
```

The times are real milliseconds: `rq.speed` does not change them. Timers and jobs go on after a
load or the title; cancel them in [`rq.on_reset`](../reference/api/rq.md#rqon_reset) when they
belong to one save. `rq.wait` and `rq.wait_until` work only inside a job from `rq.spawn`.

## Not yet

Some of this still needs [the game's own code](game-code.md): which group a random fight brings,
the 1 in 10 roll, an event when the money changes, and timers on the game's clock. The
[roadmap](../roadmap.md) lists what is planned.
