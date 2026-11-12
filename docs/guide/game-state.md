# Gold, encounters and levels

The things a first mod usually wants to change have their own calls since loader 2.33.0: the
money and charisma ([`rq.game`](../reference/api/rq.game.md)), random fights on a quest's map
([`rq.encounters`](../reference/api/rq.encounters.md)), EXP and levels
([`rq.chara.add_exp`](../reference/api/rq.chara.md#rqcharaadd_exp), `level_up` and `on_level_up`),
and timers and jobs that wait ([`rq.after`](../reference/api/rq.md#rqafter), `rq.every`,
`rq.spawn`, `rq.wait`). A fight's gold and EXP came in 2.34.0
([`rq.battle.on_reward`](../reference/api/rq.battle.md#rqbattleon_reward)), and where each
character is and the game's heals in 2.35.0 ([`rq.party`](../reference/api/rq.party.md)). The
monsters ([`rq.monster`](../reference/api/rq.monster.md)), the mode and the fights a mod opens
([`rq.battle.start`](../reference/api/rq.battle.md#rqbattlestart)) came in 2.36.0. Each example on
this page is a whole `init.lua`; set `loader` to `2.33.0` in its `mod.json`, `2.34.0` for the fight
rewards, `2.35.0` for the party, or `2.36.0` for the monsters, the mode and a fight from a mod.

All of these read or change the game, so call them from a callback or `rq.on_frame`, not at the
top level of `init.lua` ([When code runs](sandbox.md#when-code-runs)). `rq.encounters.hold` and the
`on_*` calls are the exception: they can sit at the top level.

## Money and charisma

`rq.game.gold()` gives the money, and `set_gold` and `add_gold` change it. The game keeps it from
0 to 999,999,999: a value past either end stops there. Every change redraws the system bar.

Double the gold of every fight. `rq.battle.on_reward` gets the fight's gold before the result
screen shows it, so the screen shows the new amount and that is what the game pays
([Fight rewards](#fight-rewards)):

```lua
rq.battle.on_reward(function(ctx)
  ctx.gold = ctx.gold * 2
end)
```

Charisma (the game calls it fame) is a rank and the points toward the next one.
`rq.game.charisma()` returns the rank, the points and the points the rank needs. `add_charisma`
works as a quest's result does: points that fill the bar raise the rank once, and the rest waits
for the next one. Taking points away never lowers the rank. `set_charisma(rank, points)` sets both.

```lua
local rank, points, max = rq.game.charisma()
rq.log(("charisma rank %d, %d / %d"):format(rank, points, max))
```

`rq.game.mode()` says whether the save plays in `"classic"` or `"tada"` mode, the choice at the
support menu, and `rq.game.set_mode` changes it. TADA mode doubles a fight's EXP and gold and a
familiar's growth. The game has no easy mode to report: its flags are left over from the first
Rance Quest, and Magnum never sets them.

## Fight rewards

`rq.battle.on_reward(fn)` runs once for every fight that pays: one won, and one the enemies ran
from, which the game pays too (its result 4). It comes after the game has summed the gold and EXP
with all its own rules (TADA mode, skills, items, the quest's bonus) and before the result screen
shows them. What the callbacks leave is what the screen shows, what the party gets and the gold
paid.

- `ctx.gold`: the gold.
- `ctx.exp`: the fight's EXP, the result screen's second number. Writing it scales every ally's EXP
  by the same ratio at once.
- `ctx.allies`: the party, each with its `exp`. Write one ally's `exp` for that ally alone. An ally
  who is `down` or `capped` (at the level cap) gets nothing, whatever is written.
- `ctx.reserve`: what each reserve character gets. Until a callback writes it, it follows the
  allies as they stand: the smallest ally EXP over 20, as the game reckons it.
- To read: `result`, `kills` (the enemies defeated), `bags` (the gold bags picked up), `base` (the
  screen's top number), `group`, `rank` and `enemies`.

Twice the EXP and a tenth more gold:

```lua
rq.battle.on_reward(function(ctx)
  ctx.exp = ctx.exp * 2
  ctx.gold = ctx.gold + ctx.gold // 10
end)
```

The reserve's share follows the doubled EXP. A fixed share for the reserve instead:

```lua
rq.battle.on_reward(function(ctx)
  ctx.reserve = 100
end)
```

Callbacks run in load order, and each reads what the ones before wrote, so two mods that each double
the EXP give four times. The rest follows the new numbers: the quest's EXP total (a twentieth of
which goes to the characters in training when the quest ends), the quest's level-up bonus for an
ally the new EXP levels up, and the reserve's levels, which `rq.chara.on_level_up` reports with
`battle` and `free`.

### Gold bags

The game gives each enemy a gold bag at 50%, and the bags picked up as the enemies fall set the
gold: none gives 1, one a quarter of the quest's gold, two a half, three all of it, four twice and
five four times. `rq.battle.bags()` lists the enemies' bags in a fight (`enemy`, `carries`,
`picked`), and `rq.battle.set_bag(iic, carries)` gives or takes one. In `rq.battle.on_start` the
bags are not rolled yet: a `set_bag` there is kept and written over the game's roll. Every enemy
with a bag:

```lua
rq.battle.on_start(function(ctx)
  for _, e in ipairs(ctx.enemies) do rq.battle.set_bag(e, true) end
end)
```

During the fight `set_bag` changes a bag before its enemy falls; on a fallen enemy it returns false.
The item a fight drops is `rq.battle.get_drop` and `set_drop`, which work in `on_reward` too.

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

## The party

`rq.party.get()` gives the five ranks. `rq.party.roster()` gives every recruited character with
where it is (`state`), its HP and its status, and `rq.party.roster(state)` only those in one place.
The places are named in `rq.ids.party_state`: `PARTY` (one of the five ranks), `RESERVE` (the first
army), `USED` (the first army, switched out in this quest: not placed again until the quest ends,
when the game puts it back) and `SECOND` (the second army). `rq.party.state(iic)` gives one
character's, and `rq.party.set_state(iic, state)` moves a character between `RESERVE`, `USED` and
`SECOND`; into the party is `rq.party.set`.

`rq.party.heal()` heals the five ranks as the game's springs do, with `skills = true` the skill
uses too, `half = true` up to half the HP, and `all = true` everyone recruited. Like the game, it
leaves a downed character (`status` 3, `rq.ids.state.DOWNED`) as it is; set its status to 0 first
to raise it. `rq.chara.heal(iic)` heals one character.

A key on the debug menu that raises the downed to 1 HP and heals everyone:

```lua
rq.debug.action({
  id = "heal-all",
  label = "Heal everyone",
  key = "8",
  onPress = function()
    for _, m in ipairs(rq.party.roster()) do
      if m.status == rq.ids.state.DOWNED then rq.chara.set(m.iic, { status = 0, hp = 1 }) end
    end
    rq.log("healed", rq.party.heal({ all = true, skills = true }))
  end,
})
```

HP and the status are `rq.chara.get(iic).hp`, `hp_max` and `status`, and `rq.chara.set` writes
them. The older `rq.orb` calls do the same and stay.

## Monsters

A monster's data from the game's list, changed each time the game builds it, and each enemy a
fight builds (`rq.monster.get`, `edit`, `on_create`), have their own page since 2.40.0, with a
mod's own monsters, their capture and drops, and enemy groups: [Monsters and enemy
groups](monsters.md).

## A fight from a mod

`rq.battle.start` opens a fight with the current party and waits until it and its result screens
end, so call it from a job (`rq.spawn`). It starts from a quest's map, the town, Rance Castle, the
Party screen or Quests, and the screen comes back after. Its options:

- `enemies` (up to five monster numbers by rank, 0 for an empty rank) and `exp` for the win.
  Since 2.40.0 a mod's monster by its id, or a mod's `group` in place of `enemies`
  ([Enemy groups](monsters.md#enemy-groups)).
- `boss = true` for the game's boss fight: no escape, 999 actions, the boss music. With it,
  `strong` (the "+" boss) and `double_hp`.
- `names` per rank, a `background` (a number or a name from `rq.battle.backgrounds()`), `music` (a
  game track or a file in the mod's folder), the `escape` chance and the `gold` it pays.

It returns `"won"`, `"lost"` or `"other"`, and a second value with how it ended (`how`: won, lost,
draw, time, fled), the `exp` and `gold` it paid, the `kills` and the `fallen` allies.

A key on the debug menu that opens a boss fight against a named Cockroach:

```lua
rq.debug.action({
  id = "shadow-fight",
  label = "Fight the Shadow",
  key = "9",
  onPress = function()
    rq.spawn(function()
      local r, info = rq.battle.start({
        enemies = { 0, rq.ids.monster.COCKROACH }, exp = 500, gold = 1000,
        boss = true, strong = true, names = { [2] = "The Shadow" },
      })
      rq.log(r, info.how, "EXP " .. info.exp, "gold " .. info.gold)
    end)
  end,
})
```

## Not yet

Some of this still needs [the game's own code](game-code.md): which of the area's groups a random
fight brings (the area's list is `rq.encounters.set_groups` since 2.40.0), the 1 in 10 roll, an
event when the money changes, timers on the game's clock, the gold and EXP before the game's own
rules apply, the labels beside each ally's EXP on the result screen, a quest's own reward, and new
3D models for monsters. What an enemy chooses came in 2.38.0 ([Combat rules](combat.md)), and new
monsters in 2.40.0. The [roadmap](../roadmap.md) lists what is planned.
