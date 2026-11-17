# Battle states

`rq.status` (loader 2.2.0, most of this page 2.26.0) holds the states mods make: a burn, a bleed,
a regeneration, an attack-up, a curse. They live beside the game's own poison, stun and ▲▼, in one
list every mod shares, and the game's cures, dispels and screens treat them as their own.

## A burn, from start to end

Define the state once in `init.lua`, then put it on someone from a hit:

```lua
local BURN_ICON = rq.image.add("burn", "icons/burn.png", { fit = "contain", w = 56, h = 56 })

rq.status.define("mymod:burn", {
  name = "Burn",
  turns = 3,                       -- the bearer's own turns
  tags = { "fire" },
  icon = { icon = BURN_ICON },     -- shown on the card, with the turns left
  desc = "Loses 5% of its HP at the start of each turn.",
  on_turn = function(s, ctx)
    ctx:damage(math.max(1, rq.chara.get(s.iic).hp_max * 5 // 100))
    ctx:log(" " .. rq.chara.get(s.iic).short .. " burns.")
  end,
})

rq.battle.on_hit(function(ctx)
  if ctx.skill == FIRE_SLASH and not ctx.missed and not ctx.downed then
    local s, why = rq.status.add(ctx.defender, "mymod:burn", { source = ctx.attacker })
    if s then ctx:log(" (Burn)") elseif why == "immune" then ctx:log(" (No effect)") end
  end
end)
```

`on_turn` runs at the start of each of the bearer's turns. Each state's damage and healing shows as
a number of its own, after the game's poison and regeneration, and the HP bar steps down with each.
The count goes down at the end of the bearer's turn; a state put on during the bearer's own turn
skips that countdown, so a 3-turn burn ticks three times.

The id is `"<your mod id>:<name>"`. Any mod can add, read, cure or remove it by that id, so a
second mod can make a burn salve for your burn.

## Bad states, good states and the game's skills

The game's own skills take mod states by the classes in `cured_by`:

| Class | What takes it |
| --- | --- |
| `"all"` | Status Restore, Encourage and Self-Healing; skill 475 at the start of the bearer's turn (50%); Am Powder when it has nothing else to do |
| `"poison"` | First Aid |
| `"dispel"` | What takes the game's ▲: Pop Pulse, Divine Erosion Wave, Guna Beam (half the time), a Gunner's Erasure Arrows, Electroshock on a target with no protection |
| a skill number | That support skill |

A bad state (`kind = "bad"`, the default) is cured by `"all"`; a good one (`kind = "good"`) is
dispelled by `"dispel"`, as the game's ▲ is. Give `cured_by` to change it: `{ "all", "poison" }`
for a venom First Aid also cures, `{}` for a state nothing of the game takes.

The AUTO button counts mod states too: its Status Restore goes to an ally with a state it cures.

Your own medicine calls `rq.status.cure`, which takes no notice of `cured_by`:

```lua
rq.status.cure(target, { tag = "fire" })  -- every fire state, whichever mod made it
```

## A weaken, and the battle forecast

A state can change damage and accuracy for or against its bearer:

```lua
rq.status.define("mymod:weaken", {
  name = "Weaken", turns = 2,
  physical = function(s, side, ctx) if side == "attacker" then return nil, 70 end end,  -- 70%
  magic = function(s, side, ctx) if side == "attacker" then return 70 end end,
})
```

The battle forecast (with Battle Forecast in the party) counts it: the damage word under the skill
changes. Your callbacks also run for the forecast, every time the player points a skill at an
enemy, with `ctx.forecast` true; one that counts hits or rolls dice should do nothing then. To add
your own part to the forecast line (the game shows one only for a skill aimed at an enemy; for a
support skill it builds nothing, `ctx.text` is "", and your text is the whole line):

```lua
rq.battle.on_forecast(function(ctx)
  if ctx.skill == FIRE_SLASH then return "  Burn 40%" end
end)
```

## A debuff skill with no damage

A skill of action kind 3 (special) does no damage, like the game's taunt and stuns. It reaches
`rq.battle.on_hit` with `kind = "special"`, so a debuff skill puts its state on there:

```lua
rq.skill.patch(MY_HEX, { action = 3 })
rq.battle.on_hit(function(ctx)
  if ctx.kind == "special" and ctx.skill == MY_HEX and not ctx.missed then
    rq.status.add(ctx.defender, "mymod:weaken", { source = ctx.attacker })
  end
end)
```

## A state that can kill

A state's damage stops at 1 HP, as poison's does, unless the definition says `lethal = true`.
Then the bearer can go down at the start of its turn, with the state's `source` as the killer, so
the killer's skills that act on a kill still work.

Persevere acts on it as on a hit: skill 481 always leaves 1 HP, skill 247 half the time once a
fight. `persevere = false` makes a doom nothing stops.

## Who cannot take it

```lua
rq.status.define("mymod:burn", {
  ...
  immune = { boss = true, barrier = true, races = { rq.ids.race.HANNY } },
})
rq.status.set_immune(354, { tag = "fire" })  -- monster 354 takes no fire state, from any mod
```

`rq.status.add` then puts nothing on and returns nil and `"immune"`, and `rq.status.immune(iic, id)`
answers before you try.

## A state that lasts the quest

By default a state ends with the fight. `lasts = "quest"` keeps it on an ally from fight to fight
until the quest ends, however it ends:

```lua
rq.status.define("mymod:curse", { name = "Curse", lasts = "quest", turns = 5, icon = { icon = CURSE_ICON } })

rq.dungeon.on_map(function(ctx)
  if stepped_on_trap then rq.status.add(rq.party.get()[1], "mymod:curse") end
end)
```

It can be put on outside a fight during a quest, shows on the card when the next fight starts,
and counts its turns only in fights. When the quest ends, `on_remove` gets the reason
`"quest_end"`. On an enemy it still ends with the fight.

## When nothing goes on

`rq.status.add` returns the state, or nil and a reason:

| Reason | Why |
| --- | --- |
| `"no_fight"` | Not in a fight (only a `"quest"` state on an ally goes on outside one) |
| `"no_quest"` | A `"quest"` state outside a fight and outside a quest |
| `"down"` | The character is down |
| `"immune"` | `immune` or `set_immune` says no |

## A state that changes the rules

A state can also change the rules of a fight. A state can stand for Haste or Slow by changing the
turn list. It can change a stun or poison chance, give thorns that counter, or curse the healing it
gets. It can also change what the enemies choose. All of these are in [Combat rules](combat.md).

A taunt, with the game's own (2.38.0): while an ally has it, the enemies aim at that ally first.

```lua
rq.status.define("mymod:taunt", {
  name = "Taunt", kind = "good", turns = 3,
  on_add = function(s) rq.battle.set_taunt(s.iic) end,
  on_remove = function(s)
    if rq.battle.taunt() == s.iic then rq.battle.set_taunt(nil) end
  end,
})
```

A state that makes the enemies leave its bearer alone writes another target in
`rq.battle.on_choose` instead:

```lua
rq.battle.on_choose(function(ctx)
  if ctx.target and rq.status.get(ctx.target, "mymod:smoke") then
    for _, iic in ipairs(ctx:targets()) do
      if not rq.status.get(iic, "mymod:smoke") then ctx.target = iic break end
    end
  end
end)
```

## Not yet

- The `desc` text shows nowhere in the game yet; it comes with the card's marks side by side,
  each with its own hover text.
- States that last in the save and states shown between fights are on the
  [Roadmap](../roadmap.md). The enemies choosing by mod states came in 2.38.0
  (`rq.battle.on_choose`).
