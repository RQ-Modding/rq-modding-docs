# Quests of your own

Since loader 2.41.0 a mod can add quests to the quest list ([`rq.quests.define`](../reference/api/rq.quests.md)).
They have no map: a story, a quest of fights, a menu, a chain of quests. The player takes one from
the list as a game quest, with the autosave and the try counted, and the game's result screen ends
it. Each example on this page is a whole `init.lua`; set `loader` to `2.41.0` in its `mod.json`.

Quests with a map of their own come later (phase O3 on the [Roadmap](../roadmap.md)), on this page.

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
