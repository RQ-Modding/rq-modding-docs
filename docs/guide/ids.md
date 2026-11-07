# Numbers and ids

The game counts most things twice: once for the kind of thing, once for each copy the player has.
The `rq.*` calls say which one they take. Mixing them up is the most common mistake.

## Characters: number and roster slot

| Name in the docs | What it is | Example |
| --- | --- | --- |
| character number (`no`, or `who`) | Which character: the same in every save. | Rance is 1, Kaoru 52, Onoha 62, Rebecca 81. |
| roster slot (`iic`) | Where a recruited character sits in this save's roster, 20 to 200. | The `id` of an entry in `rq.units()`. |

Most `rq.chara` calls take a roster slot. Calls that say `who` take a character number or a text
id. To go between them:

```lua
local iic = rq.chara.find(52)       -- Kaoru's roster slot, or nil when she is not recruited
local no = rq.chara.number(iic)     -- back to 52
```

In a fight there is also a **battle number**, the card a character stands on: 1 to 5 for allies,
11 to 15 for enemies. Fight events give both (`ev.user` and `ev.unit` in `rq.battle.on_use`).

## Items: number and instance

| Name in the docs | What it is |
| --- | --- |
| item number (`no`, or `who`) | Which item, such as a kind of sword. |
| instance (`ii`) | One copy the player has, up to 3000 in a save. It points to an item number and has its own state, such as who wears it and where it is stored. |

`rq.items()` lists instances; `rq.item.number(ii)` gives an instance's item number. A shop's stock,
the vault and equipped gear are all instances.

## Skills and quests

Skills have one number each (`rq.skill.get(no)`); a character's own copy of a skill (its rank, its
uses) is read through `rq.chara`. Quests have one number each, the index in the game's quest list
(`rq.quests()`).

## Text ids

Things a mod defines get a text id, written `"mymod:name"`:

```lua
rq.chara.define({ id = "mymod:alice", name = "Alice", class = 1 })
rq.item.define({ id = "mymod:lens", name = "Lens", price = 2000 })
```

The calls that take a number also take that text id. The engine turns each text id into a number,
always the same number for the same text, so saves that hold it stay valid:

| Kind | Numbers for text ids |
| --- | --- |
| characters | 1000 to 9999 |
| items | 1000 to 9999 |
| skills | 700 to 999 |

Two text ids can land on the same number; `define` then raises an error, and a new id fixes it.
Never change a text id after players have it in a save. Start the id with your mod's id, so two mods
do not pick the same text.

## Names instead of numbers

`rq.ids` (loader 1.15.0) names the base game's numbers, so the code says what it means:

```lua
local FORTUNE = rq.ids.skill.FORTUNE_448        -- 448
local MASK = rq.ids.item.POISON_MASK            -- 195
local iic = rq.chara.find(rq.ids.chara.KAORU_QUINCY)
if c.class == rq.ids.class.BRAWLER and c.status == rq.ids.state.POISON then ... end
```

There are six kinds: `chara`, `class`, `item`, `quest`, `skill` and `state`. A key is the in-game
English name in upper snake case. When the game gives one name to several numbers, as it does with
four skills called Fortune, each key ends in its number (`FORTUNE_158` ... `FORTUNE_448`); the
[Game data](../data/index.md) tables list every key with its number and name. Editors complete the
keys as you type, with the number and the name beside each.

A key that does not exist raises an error when the line runs, so a typo is caught at once. The
tables hold only the base game; for something a mod defines, use its text id.

For a name from a config file or a player, look it up:

```lua
local no, err = rq.ids.find("item", "Poison Mask")   -- 195; case and punctuation do not matter
rq.ids.find_all("skill", "fortune")                  -- every skill whose name holds "fortune"
rq.ids.name("skill", 448)                            -- "Fortune"
```

`find` returns nil and a message when the name is unknown or belongs to more than one number.

## Finding a number

- The [Game data](../data/index.md) tables, or `rq.ids.find` and `rq.ids.find_all`.
- `rq.units()` and `rq.items()` list what the save has, and `rq.quests()` every quest, with names.
- `rq.skill.get(no).name` and `rq.chara.get(iic).name` give a name for a number, also for things a
  mod defined.
- `rq.ain.find("part of a name")` writes the game functions whose names contain it to the log, for
  `rq.ain.call` and `rq.ain.hook`.
