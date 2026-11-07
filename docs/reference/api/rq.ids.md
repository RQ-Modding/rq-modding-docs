# rq.ids

`since 1.15.0` `changed 1.16.0`

The game's numbers by name: characters, items, quests, skills, and the small lists the game names
(classes, states, races, character types, elements, item kinds, skill targets).

Each kind is a table of constants, so `rq.ids.skill.FORTUNE_448` is 448 and `rq.ids.item.SKILL_AGAIN`
is 306. Editors complete them from `lua/rq_ids.lua`, with each entry's number and in-game name. A
key is the English name in upper snake case. A name the game gives to more than one number gets
the number as a suffix on each of them (`FORTUNE_158`, `FORTUNE_448`), and a key that would start
with a digit starts with `N_` (`N_10_TON_HAMMER`). Some repeated names also have a key without the
number, beside the numbered keys: the plain key for the one players know (`FORTUNE` is 448,
`RICK_ADDISON` is 93), or a key of its own for another version (`CAPTURE_EX`, `USE_IBEPROFUN_EX`,
`STAMINA_BOOST_1`). The docs' data tables list every entry and mark those keys.

The tables hold the base game only, not what mods define; use a mod's text id for those. Reading
a key that does not exist raises an error, so a typo stops the mod at once instead of passing
nil along; use `rq.ids.find` for a name that may not be there. Nothing in `rq.ids` can be
changed. It works at the top level of `init.lua`.

| Kind | Numbers |
| --- | --- |
| `chara` | character numbers (`no`), not roster slots |
| `chara_type` | character type values (`タイプ`), as in `rq.chara.get(iic).type`: `HUMANOID` is 22 |
| `class` | class numbers, as in `rq.chara.get(iic).class` |
| `element` | elements (`属性`): `NOTHING`, `LIGHT`, `DARKNESS`, `ELECTRIC`, `ICE`, `FIRE` |
| `item` | item numbers, not instances |
| `item_kind` | item kinds (`種類詳細`), as in an item's `subtype`: `SWORD`, `SHORTSWORD`, `SPEAR`, `CLOTHING`, ... |
| `quest` | quest numbers |
| `race` | races (`種族`), as in `rq.chara.get(iic).race`: `HUMAN`, `HANNY`, ... |
| `skill` | skill numbers |
| `state` | status values (`状態変化`): `NONE`, `POISON`, `STUN`, `DOWNED` |
| `target` | skill target codes (`対象`): `MELEE`, `RANGED`, `ALL_ENEMIES`, `ROW`, `SELF`, `ALLY`, `ALL_ALLIES`, `RANDOM_TARGET` |

```lua
local FORTUNE = rq.ids.skill.FORTUNE  -- 448, also FORTUNE_448
local iic = rq.chara.find(rq.ids.chara.KAORU_QUINCY)
if rq.item.number(ii) == rq.ids.item.POISON_MASK then ... end
if ctx.race == rq.ids.race.HANNY then return nil, 50 end
local no = rq.ids.find("skill", "Spear Knowledge")  -- from a config file or a player
```

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `chara` | `rq.IdsChara` | Characters by name; each key is in the docs' Characters table (Game data). |
| `chara_type` | `rq.IdsCharaType` | Character types by name; each key is in the docs' Character types table (Game data). Since 1.16.0. |
| `class` | `rq.IdsClass` | Classes by name; each key is in the docs' Classes table (Game data). |
| `element` | `rq.IdsElement` | Elements by name; each key is in the docs' Elements table (Game data). Since 1.16.0. |
| `item` | `rq.IdsItem` | Items by name; each key is in the docs' Items table (Game data). |
| `item_kind` | `rq.IdsItemKind` | Item kinds by name; each key is in the docs' Item kinds table (Game data). Since 1.16.0. |
| `quest` | `rq.IdsQuest` | Quests by name; each key is in the docs' Quests table (Game data). |
| `race` | `rq.IdsRace` | Races by name; each key is in the docs' Races table (Game data). Since 1.16.0. |
| `skill` | `rq.IdsSkill` | Skills by name; each key is in the docs' Skills table (Game data). |
| `state` | `rq.IdsState` | States by name; each key is in the docs' States table (Game data). |
| `target` | `rq.IdsTarget` | Skill targets by name; each key is in the docs' Skill targets table (Game data). Since 1.16.0. |

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

`since 1.15.0` `changed 1.16.0`

Returns the number of the thing with this name.

The name is compared without case, spaces or punctuation, and é matches e, so "spear knowledge"
finds Spear Knowledge. A key works too (`"FORTUNE_448"`, `"CAPTURE_EX"`). When the game uses the
name for more than one number, the number of its plain key is returned ("Fortune" gives 448); a
repeated name with no plain key returns nothing, and the message lists the numbers.
`rq.ids.find_all` gives them all.

Raises an error for an unknown kind or a name that is not a string.

```lua
local no, err = rq.ids.find("item", cfg.item)
if not no then rq.log(err) end  -- such as: more than one skill is named "Attack": 155, 386, ...
```

| Parameter | Type | Description |
| --- | --- | --- |
| `kind` | `"chara"\|"chara_type"\|"class"\|"element"\|"item"\|"item_kind"\|"quest"\|"race"\|"skill"\|"state"\|"target"` | The kind. |
| `name` | `string` | The in-game English name, or a key. |

| Returns | Type | Description |
| --- | --- | --- |
| `no` | `integer\|nil` | The number, or nil when no entry or more than one has that name. |
| `err` | `string?` | Why there is no number. |

> Changed in 1.16.0: Takes the kinds `chara_type`, `element`, `item_kind`, `race` and `target`. A repeated name with a plain key gives that key's number.

See also: [`rq.ids.find_all`](rq.ids.md#rqidsfind_all)

### rq.ids.find_all

```lua
rq.ids.find_all(kind, text) -> integer[]
```

`since 1.15.0` `changed 1.16.0`

Returns the numbers of every entry whose name contains a text.

The text is compared as in `rq.ids.find`. An empty text gives every number of the kind.

Raises an error for an unknown kind or a text that is not a string.

```lua
rq.ids.find_all("skill", "fortune")  -- {158, 159, 160, 293, 448, 585}: Fortune, Improve Fortune,
                                     -- 7 Misfortunes, 8 Pains
```

| Parameter | Type | Description |
| --- | --- | --- |
| `kind` | `"chara"\|"chara_type"\|"class"\|"element"\|"item"\|"item_kind"\|"quest"\|"race"\|"skill"\|"state"\|"target"` | The kind. |
| `text` | `string` | What the name must contain. |

| Returns | Type | Description |
| --- | --- | --- |
| `numbers` | `integer[]` | The numbers, smallest first; empty when none. |

> Changed in 1.16.0: Takes the kinds `chara_type`, `element`, `item_kind`, `race` and `target`.

See also: [`rq.ids.find`](rq.ids.md#rqidsfind)

### rq.ids.name

```lua
rq.ids.name(kind, no) -> string|nil
```

`since 1.15.0` `changed 1.16.0`

Returns the in-game name of a number.

It is the base game's English name, as `rq.skill.get` and the like give it. Some names keep the
game's own code for é (`Tomato Pur･e`).

Raises an error for an unknown kind.

```lua
rq.log("used " .. (rq.ids.name("skill", ctx.skill) or "a mod skill"))
```

| Parameter | Type | Description |
| --- | --- | --- |
| `kind` | `"chara"\|"chara_type"\|"class"\|"element"\|"item"\|"item_kind"\|"quest"\|"race"\|"skill"\|"state"\|"target"` | The kind. |
| `no` | `integer` | The number. |

| Returns | Type | Description |
| --- | --- | --- |
| `name` | `string\|nil` | The name, or nil when the base game has none for that number. |

> Changed in 1.16.0: Takes the kinds `chara_type`, `element`, `item_kind`, `race` and `target`.
