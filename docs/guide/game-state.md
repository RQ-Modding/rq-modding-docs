# Gold, encounters and levels

The things a first mod usually wants to change have their own calls since loader 2.33.0: the money
and charisma ([`rq.game`](../reference/api/rq.game.md)), random fights on a quest's map
([`rq.encounters`](../reference/api/rq.encounters.md)), EXP and levels
([`rq.chara.add_exp`](../reference/api/rq.chara.md#rqcharaadd_exp), `level_up` and `on_level_up`),
and timers and jobs that wait ([`rq.after`](../reference/api/rq.md#rqafter), `rq.every`, `rq.spawn`,
`rq.wait`). A fight's gold and EXP came in 2.34.0
([`rq.battle.on_reward`](../reference/api/rq.battle.md#rqbattleon_reward)), and where each character
is and the game's heals in 2.35.0 ([`rq.party`](../reference/api/rq.party.md)). The monsters
([`rq.monster`](../reference/api/rq.monster.md)), the mode and the fights a mod opens
([`rq.battle.start`](../reference/api/rq.battle.md#rqbattlestart)) came in 2.36.0, and skill buying
with its price and the record of what each skill cost in 2.45.0; Athena's Studies, the game's skill
reset and who can equip an item in 2.46.0; a free appraisal, an item stocked in the open shop and
Go Home in 2.47.0. Each example on this page is a whole `init.lua`; set
`loader` to `2.33.0` in its `mod.json`, `2.34.0` for the fight rewards, `2.35.0` for the party,
`2.36.0` for the monsters, the mode and a fight from a mod, `2.45.0` for skill buying, `2.46.0`
for the Studies, the reset and the equip check, or `2.47.0` for the appraisal, the shop and Go
Home.

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

Athena 2.0 grows by her Studies instead: after a fight, with her in rank 4 or 5, each Study on her
hotbar adds to her stat when the ally diagonally in front of her has more of it.
[`rq.battle.on_study`](../reference/api/rq.battle.md#rqbattleon_study) (2.46.0) runs for each one
that fired, with the stat and the game's gain; return another gain. Athena QoL scales them by the
world:

```lua
local GAINS = { attack = { 100, 500, 2000 }, hp = { 100, 500, 2000 },
  accuracy = { 5, 10, 20 }, speed = { 5, 10, 20 }, critical = { 5, 10, 20 } }
rq.battle.on_study(function(ctx)
  return GAINS[ctx.stat][rq.world.current() or 1]
end)
```

## Skills and their price

Since 2.45.0 the loader keeps a record of what each skill cost in the skill row itself (a field the
game saves but never used), so a mod can tell a bought skill from one the character started with
or one a mod gave. [`rq.chara.slots`](../reference/api/rq.chara.md#rqcharaslots) shows it on each
row as `cost` (the points paid; -1 for a mod's gift; 0 when nothing was recorded), with the skill's
level as `n` (most uses, or the rank). `rq.chara.on_forget`'s `cost` is the same record.

- [`rq.chara.base_skills`](../reference/api/rq.chara.md#rqcharabase_skills): the skills the
  character starts with, as Morurun's reset gives them back.
- [`rq.chara.learnable`](../reference/api/rq.chara.md#rqcharalearnable) and
  [`price`](../reference/api/rq.chara.md#rqcharaprice): the game's buy list and its price from one
  level to another, with its own rules (one more point at 3, 5 and 7 uses, Rance's 147).
- [`rq.chara.learn`](../reference/api/rq.chara.md#rqcharalearn): the game's own buy without its
  questions, paid or free, refused with the reason (`"points"` with how many are missing, `"room"`,
  `"not sold"`, `"condition"` with the game's text).
- [`rq.chara.skill_room`](../reference/api/rq.chara.md#rqcharaskill_room) and
  [`skill_points_max`](../reference/api/rq.chara.md#rqcharaskill_points_max): the free rows for a
  new skill and the most points the character can have had.
- [`rq.chara.on_learn`](../reference/api/rq.chara.md#rqcharaon_learn): each purchase, the skill
  window's or a mod's.
- [`rq.chara.on_skill_reset`](../reference/api/rq.chara.md#rqcharaon_skill_reset) (2.46.0): after
  Morurun's reset or Skill Again, which set the free points to the game's own count, so a mod can
  give back the points it gave.

Half the points back for every erasure the player chose (Skill Removal Payback gives them all):

```lua
rq.chara.on_forget(function(ctx)
  if ctx.player and ctx.cost > 0 then return ctx.cost // 2 end
end)
```

`ctx.player` (2.51.0) is true for the skill window's ERASE and for a mod's erasure made for the
player; the game's other removals (its recalculation, the story, the reset) are not. A mod that
erases for the player, as Loadouts does when it loads a build, says so, and gets the points the
callbacks gave back as a third value; any mod that pays back ERASE then pays it back too. A plain
`rq.chara.forget` is the mod's own removal, and such a mod gives nothing. `ctx.mod` names the mod
that called `forget`.

```lua
local removed, cost, back = rq.chara.forget(iic, skill, { player = true })
```

To show a price before erasing,
[`rq.chara.forget_points`](../reference/api/rq.chara.md#rqcharaforget_points) (2.52.0) asks the
callbacks what an erasure would give back, with nothing erased: each one runs with `ctx.preview`
true, so it should only count then. `n`, `cost` and `kept` ask about the row as a plan would leave
it, which is how Loadouts shows the price of a load less what any mod gives back:

```lua
-- Healing 3, learned on the way to 3 uses for 9 points, then erased: what comes back?
local back = rq.chara.forget_points(iic, 223, { player = true, n = 3, cost = 9 })
```

A mod's skill that takes the place of others writes what they had cost into its own row with
[`rq.chara.set_cost`](../reference/api/rq.chara.md#rqcharaset_cost) (2.53.0), so an erasure later
gives back what was paid for all of them. Better Elemental Knowledge sells one skill for the five
Brawling Knowledges, its price less what the character holds of them; at the purchase it erases
those (nothing back, they came off the price) and adds their records to the points paid:

```lua
rq.chara.on_learn(function(ctx)
  if not ctx.new or ctx.skill ~= ALL_FIVE then return end
  local total = math.max(ctx.cost, 0) -- what the purchase cost
  for _, row in ipairs(rq.chara.slots(ctx.iic)) do
    if SINGLE[row.skill] then
      if row.cost > 0 then total = total + row.cost end
      rq.chara.forget(ctx.iic, row.skill)
    end
  end
  rq.chara.set_cost(ctx.iic, ALL_FIVE, total)
end)
```

Like any purchase, such a skill needs a free row: the game refuses it on a full list (`"room"`)
even when the rows it frees would make room.

A purchase made before loader 2.45.0 has no record (its `cost` is 0): its steps above
`base_skills` at today's `price` are the best guess, as Skill Removal Payback and Loadouts do.
Set `loader` to `2.45.0` in `mod.json` for these.

### Skills sold through others

Some skills are for sale only once others are learned: Healing 2 once Healing 1 is at 3, Recovery
Rain 2 once Healing 3 is learned, the second Attack Boost once the first is at rank 4. The game's
list shows such a skill with its reason (`why`), and since 2.48.0 each of
[`learnable`](../reference/api/rq.chara.md#rqcharalearnable)'s rows also has what that reason
names: `needs` (the skills and their levels) and `level` (the character's level). Its
`opts.after` makes the list as it would be after some steps (a skill set to a level, or erased
with 0) without changing the character, and its second value is the free rows after them.
Loadouts plans a load this way, one step at a time:

```lua
-- Is Healing 3 for sale once Healing 2 is at 3?
local rows = rq.chara.learnable(iic, { after = { { skill = 222, n = 3 } } })
for _, row in ipairs(rows or {}) do -- nil when a new skill found no free row
  if row.skill == 223 then rq.log(row.points > 0 and "for sale" or row.why) end
end
```

In the third world, a Boost raised to rank 4 keeps its effect after an ERASE, until the
character's skills are reset (Morurun's reset, Skill Again).
[`rq.chara.boosts`](../reference/api/rq.chara.md#rqcharaboosts) (2.48.0) tells which ones a
character keeps, and `on_forget`'s `kept` tells it of the skill being erased: Skill Removal
Payback gives nothing back for such a Boost unless its setting says so. Set `loader` to `2.48.0`
for these.

## Who can equip an item

The game asks one question before a character wears an item, in the vault, on the status page, in
the shop and on the storage screen: is the character's level high enough, and is the item for that
character or class. [`rq.item.on_can_equip`](../reference/api/rq.item.md#rqitemon_can_equip)
(2.46.0) runs there with the game's answer and its reasons (`"level"`, then `"chara"` or
`"class"`); return true, false or nil. Athena QoL lifts only the level, for bows:

```lua
rq.item.on_can_equip(function(ctx)
  if ctx.chara == 27 and #ctx.reasons == 1 and ctx.reason == "level"
    and rq.item.get(ctx.ii).subtype == rq.ids.item_kind.BOW then
    return true
  end
end)
```

## Appraisal and the shop

An item found on a quest is often unidentified: `rq.item.get(ii).identified` is false (2.47.0),
and its name, icon and text are the game's "Unidentified item". The game appraises the quest
storage's items after a quest's success, for a price. [`rq.item.appraise`](../reference/api/rq.item.md#rqitemappraise)
(2.47.0) does it at once and for free, wherever the item is: the game's own appraisal, with a rare
item's quest bonuses. Return Bonsai keeps items in the storage during a quest and appraises them
at its end:

```lua
rq.quests.on_end(function(ctx)
  for _, row in ipairs(rq.items()) do
    if row.place == 11 and not rq.item.get(row.id).identified then rq.item.appraise(row.id) end
  end
end)
```

Frostbuy's stock comes from `rq.shop.on_stock`, which runs each time the shop opens, and
`rq.shop.stock`. Since 2.47.0 an item stocked while the shop shows is on its list at once, so an
item that is always on sale can come back in the same visit it was bought (Aten Gnu QoL's Box of
Books):

```lua
local BOOKS = rq.item.define({ id = "my-mod:books", name = "Box of Books", price = 5000,
  effects = { { kind = 14, value = 60 } } })
rq.shop.on_stock(function()
  if not rq.shop.in_stock(BOOKS) then rq.shop.stock(BOOKS) end
end)
rq.shop.on_buy(function(ctx)
  if ctx.no == BOOKS then rq.shop.stock(BOOKS) end
end)
```

`rq.shop.on_buy` runs for a purchase in the shop's own window, and since 2.49.0 for
`rq.item.buy` too, so a mod's purchase counts as the player's. A price that grows with each
purchase goes in `on_stock` with `rq.item.set(ii, { price = ... })` on the stocked instance
(`rq.item.find(no, { place = 6 })`), counted in [`rq.savedata`](save-data.md).

The game refills the stock once a visit, one copy of each item. Since 2.49.0 a mod can sell more in
the same visit, by the game's own rules:
[`rq.shop.restocks`](../reference/api/rq.shop.md#rqshoprestocks) says whether the next visit puts
another copy on sale (most weapons and armor, the special items that come back, Forbidden Talent in
the third world; not Skill Again, which comes back only while the player owns none),
[`rq.shop.restock`](../reference/api/rq.shop.md#rqshoprestock) puts it on sale now, and
[`rq.shop.next`](../reference/api/rq.shop.md#rqshopnext) gives the copies' prices before any is
bought. A weapon's or armor's copies go up a level each (① to ⑨), as the restock count rises, at
the game's prices. Frostbuy Bulk Buy buys a cart this way:

```lua
local function buy_copies(no, n)
  local cost = 0
  for _, copy in ipairs(rq.shop.next(no, n)) do cost = cost + copy.price end
  if cost > rq.game.gold() then return 0 end
  local got = 0
  for _ = 1, n do
    local ii = rq.item.find(no, { place = 6 })[1]
    if not ii or not rq.item.buy(ii, { ask = false }) then break end
    got = got + 1
    rq.shop.restock(no) -- the next copy, a level higher for a weapon
  end
  return got
end
```

A mod can also say no to a purchase. Since 2.50.0
[`rq.shop.on_can_buy`](../reference/api/rq.shop.md#rqshopon_can_buy) runs before the game checks
the money and asks "Purchase ...?", for the player's drag from the rack and for `rq.item.buy`:
return false and a text, and the game's notice shows the text, the item stays on the rack and
nothing is paid. `rq.item.buy` returns the text as its second value. An item that the player keeps
until the mod takes it back, as a receipt, gets `keep = true` in `rq.item.define`: the vault's
DISCARD, SELL and DONATE refuse it, as the game does for Chaos the Darksword. Pluepet Rare Contract
sells one contract at a time this way:

```lua
local TICKET = rq.item.define({ id = "my-mod:ticket", name = "Ticket", type = "none",
  price = 50000, keep = true, info = "Good for one wish." })
rq.shop.on_can_buy(function(ctx)
  if ctx.no ~= TICKET then return end
  if #rq.item.find(TICKET) > 0 then return false, "You already have a ticket." end
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

### Going home after a fight

After each fight the game may send a character out of the party: Aten one time in five when she
is in a party of two or more (her skill Go Home is only its description), and the wearer of item
209 always. [`rq.party.on_go_home`](../reference/api/rq.party.md#rqpartyon_go_home) (2.47.0) runs
at that moment with who (`iic`, `no`), why (`reason`: `"aten"` or `"item"`) and the chance in
percent; return another chance, 0 to keep the character, or nil. Aten Gnu QoL keeps her while she
wears a Box of Books, and gives Go Home's text a line with `rq.skill.patch`:

```lua
rq.skill.patch(369, { desc = "Has a 20% chance of leaving the party after battle.$$I mean...$it's so much work.$...Unless I get books to read." })
rq.party.on_go_home(function(ctx)
  if ctx.reason == "aten" and rq.item.equipped(ctx.iic).item then return 0 end
end)
```

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
