# rq.ids

`since 1.15.0`

The game's numbers by name: characters, classes, items, quests, skills and states.

Each kind is a table of constants, so `rq.ids.skill.FORTUNE_448` is 448 and `rq.ids.item.SKILL_AGAIN`
is 306. Editors complete them from `lua/rq_ids.lua`, with each entry's number and in-game name. A
key is the English name in upper snake case. A name the game gives to more than one number gets
the number as a suffix on each of them (`FORTUNE_158`, `FORTUNE_448`), and a key that would start
with a digit starts with `N_` (`N_10_TON_HAMMER`). Every entry is in the docs' data tables.

The tables hold the base game only, not what mods define; use a mod's text id for those. Reading
a key that does not exist raises an error, so a typo stops the mod at once instead of passing
nil along; use `rq.ids.find` for a name that may not be there. Nothing in `rq.ids` can be
changed. It works at the top level of `init.lua`.

| Kind | Numbers |
| --- | --- |
| `chara` | character numbers (`no`), not roster slots |
| `class` | class numbers, as in `rq.chara.get(iic).class` |
| `item` | item numbers, not instances |
| `quest` | quest numbers |
| `skill` | skill numbers |
| `state` | status values (`状態変化`): `NONE`, `POISON`, `STUN`, `DOWNED` |

```lua
local FORTUNE = rq.ids.skill.FORTUNE_448
local iic = rq.chara.find(rq.ids.chara.KAORU_QUINCY)
if rq.item.number(ii) == rq.ids.item.POISON_MASK then ... end
local no = rq.ids.find("skill", "Spear Knowledge")  -- from a config file or a player
```

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `chara` | `rq.IdsChara` | Characters by name; each key is in the docs' Characters table (Game data). |
| `class` | `rq.IdsClass` | Classes by name; each key is in the docs' Classes table (Game data). |
| `item` | `rq.IdsItem` | Items by name; each key is in the docs' Items table (Game data). |
| `quest` | `rq.IdsQuest` | Quests by name; each key is in the docs' Quests table (Game data). |
| `skill` | `rq.IdsSkill` | Skills by name; each key is in the docs' Skills table (Game data). |
| `state` | `rq.IdsState` | States by name; each key is in the docs' States table (Game data). |

## Functions

| Name | Summary |
| --- | --- |
| [`rq.ids.find`](#rqidsfind) | Returns the number of the thing with this name. |
| [`rq.ids.find_all`](#rqidsfind_all) | Returns the numbers of every entry whose name contains a text. |
| [`rq.ids.name`](#rqidsname) | Returns the in-game name of a number. |

### rq.ids.find

```lua
rq.ids.find(kind, name) -> integer|nil, string?
```

`since 1.15.0`

Returns the number of the thing with this name.

The name is compared without case, spaces or punctuation, and é matches e, so "spear knowledge"
finds Spear Knowledge. A key works too (`"FORTUNE_448"`). When the game uses the name for more
than one number, nothing is returned and the message lists the numbers; `rq.ids.find_all` gives
them all.

Raises an error for an unknown kind or a name that is not a string.

```lua
local no, err = rq.ids.find("item", cfg.item)
if not no then rq.log(err) end  -- such as: more than one skill is named "Fortune": 158, 159, 160, 448
```

| Parameter | Type | Description |
| --- | --- | --- |
| `kind` | `"chara"\|"class"\|"item"\|"quest"\|"skill"\|"state"` | The kind. |
| `name` | `string` | The in-game English name, or a key. |

| Returns | Type | Description |
| --- | --- | --- |
| `no` | `integer\|nil` | The number, or nil when no entry or more than one has that name. |
| `err` | `string?` | Why there is no number. |

See also: [`rq.ids.find_all`](rq.ids.md#rqidsfind_all)

### rq.ids.find_all

```lua
rq.ids.find_all(kind, text) -> integer[]
```

`since 1.15.0`

Returns the numbers of every entry whose name contains a text.

The text is compared as in `rq.ids.find`. An empty text gives every number of the kind.

Raises an error for an unknown kind or a text that is not a string.

```lua
rq.ids.find_all("skill", "fortune")  -- {158, 159, 160, 293, 448, 585}: Fortune, Improve Fortune,
                                     -- 7 Misfortunes, 8 Pains
```

| Parameter | Type | Description |
| --- | --- | --- |
| `kind` | `"chara"\|"class"\|"item"\|"quest"\|"skill"\|"state"` | The kind. |
| `text` | `string` | What the name must contain. |

| Returns | Type | Description |
| --- | --- | --- |
| `numbers` | `integer[]` | The numbers, smallest first; empty when none. |

See also: [`rq.ids.find`](rq.ids.md#rqidsfind)

### rq.ids.name

```lua
rq.ids.name(kind, no) -> string|nil
```

`since 1.15.0`

Returns the in-game name of a number.

It is the base game's English name, as `rq.skill.get` and the like give it. Some names keep the
game's own code for é (`Tomato Pur･e`).

Raises an error for an unknown kind.

```lua
rq.log("used " .. (rq.ids.name("skill", ctx.skill) or "a mod skill"))
```

| Parameter | Type | Description |
| --- | --- | --- |
| `kind` | `"chara"\|"class"\|"item"\|"quest"\|"skill"\|"state"` | The kind. |
| `no` | `integer` | The number. |

| Returns | Type | Description |
| --- | --- | --- |
| `name` | `string\|nil` | The name, or nil when the base game has none for that number. |
