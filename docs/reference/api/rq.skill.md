# rq.skill

`since 0.2.0` `changed 2.35.0`

Reads, defines and patches skills, and rewrites their hover text.

Skill numbers run 1 to 1000; the game's end near 600. A text id such as `"mymod:slash"` becomes a
stable number from 700 to 999. Strings are UTF-8 in Lua. The calls that write raise an error for a
number outside 1 to 1000. Up to 128 `define` and `patch` calls in all.

Since 2.35.0 each call places the hooks it needs the first time (`rq.skill.install`): before, a
`define` or `patch` without it was never applied, and `get` gave empty names.

## Functions

| Name | Summary |
| --- | --- |
| [`rq.skill.install`](#rqskillinstall) | Wraps `スキル_説明文１`, the hover text on the status and fight screens, so `on_describe` can rewrite it, and the game's skill list at boot, so `define` and `patch` are applied. |
| [`rq.skill.get`](#rqskillget) | Returns a skill's fields. |
| [`rq.skill.define`](#rqskilldefine) | Defines a new skill. |
| [`rq.skill.patch`](#rqskillpatch) | Changes an existing skill, field by field. |
| [`rq.skill.sort_as`](#rqskillsort_as) | Sorts a skill in the known and potential lists as if it were another. |
| [`rq.skill.form_of`](#rqskillform_of) | Declares that two skills are forms of one skill: one takes the other's place in a character's row, keeping its uses or rank, its purchase record and its hotbar place. |
| [`rq.skill.forms`](#rqskillforms) | Returns a skill's forms (`rq.skill.form_of`): the skills that take each other's place in a row. |

### rq.skill.install

```lua
rq.skill.install() -> boolean
```

`since 0.2.0` `changed 2.35.0`

Wraps `スキル_説明文１`, the hover text on the status and fight screens, so `on_describe` can rewrite
it, and the game's skill list at boot, so `define` and `patch` are applied.

Not needed since 2.35.0: each call that needs it places it the first time, and raises this
call's error there when it cannot. Calling it still does no harm.

| Returns | Type | Description |
| --- | --- | --- |
| `ok` | `boolean` | true when the patch is in place. |

> Changed in 2.35.0: Not needed: every `rq.skill` call makes it.

### rq.skill.get

```lua
rq.skill.get(id) -> rq.SkillInfo
```

`since 0.2.0` `changed 0.5.0`

Returns a skill's fields.

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `integer\|string` | A skill number or text id. |

| Returns | Type | Description |
| --- | --- | --- |
| `info` | [`rq.SkillInfo`](../types/rq.SkillInfo.md) | The fields. |

> Changed in 0.5.0: Every field `rq.skill.patch` takes; text ids.

### rq.skill.define

```lua
rq.skill.define(spec) -> integer
```

`since 0.2.0` `changed 0.5.0`

Defines a new skill.

The row is written at the end of every `Ｓ起動時登録`, and at once when boot already ran.

Raises an error for a missing id, a too long id, a text id whose number another has, or past 128
calls.

```lua
local SLASH = rq.skill.define({ id = "mymod:slash", kind = "physical", name = "Slash",
  target = 1, bairitsu = 120, desc = "A quick cut.$Front row." })
```

| Parameter | Type | Description |
| --- | --- | --- |
| `spec` | [`rq.SkillSpec`](../types/rq.SkillSpec.md) | The skill. |

| Returns | Type | Description |
| --- | --- | --- |
| `id` | `integer` | The skill number. |

> Changed in 0.5.0: Text ids; returns the number.

### rq.skill.patch

```lua
rq.skill.patch(id, fields)
```

`since 0.5.0`

Changes an existing skill, field by field.

Fields left out stay as the game made them. Patches apply after `Ｓ起動時登録`, in call order with
the defines, and at once when boot already ran. An unknown field is logged and skipped.

```lua
rq.skill.patch(246, { name = "Quick Start", desc = "Acts first.$Two ranks." })
```

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `integer\|string` | A skill number or text id. |
| `fields` | [`rq.SkillPatch`](../types/rq.SkillPatch.md) | The fields to change. |

### rq.skill.sort_as

```lua
rq.skill.sort_as(id, as_id) -> boolean
```

`since 0.2.0` `changed 0.5.0`

Sorts a skill in the known and potential lists as if it were another.

It wraps `compSkill`.

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `integer\|string` | The skill to place. |
| `as_id` | `integer\|string` | The skill it sorts as; 0 clears it. |

| Returns | Type | Description |
| --- | --- | --- |
| `ok` | `boolean` | false when the compare hook is missing. |

> Changed in 0.5.0: Takes text ids.

### rq.skill.form_of

```lua
rq.skill.form_of(skill, base)
```

`since 2.66.0`

Declares that two skills are forms of one skill: one takes the other's place in a character's
row, keeping its uses or rank, its purchase record and its hotbar place.

The game has five such families: its recalculation (`Ｃ再計算`) turns Melee Attack N into Thrust
Attack N with Spear Knowledge ★★ and a spear, and back with another weapon (100 and 101, 102 and
103, 104 and 105, 106 and 107, 578 and 579). They are built in. A mod whose `rq.chara.on_recalc`
swaps a row for its own skill (`rq.chara.set_slot`) declares that skill a form of the one it
replaces. Families join: declaring A with B and C with B makes one family of A, B and C.

The loader reads the families where a row is matched to a skill:

- the buy list sells the form a character holds: for a skill it does not hold while it holds a form
  of it, the list shows that form, priced from the held row (one more point at 3, 5 and 7 uses), and
  buying raises that row. No list sells a second row of one family.
- `rq.chara.learnable`'s steps, `rq.chara.price` and `rq.chara.learn` reach a skill through the
  row of a form the character holds.

Which form a row shows stays the recalculation's choice (the game's and the mods' `on_recalc`).
The game's checks for a skill (`rq.chara.rank`, `max_uses`, `on_has_skill`) still go by number.

Raises an error for a number outside 1 to 1000, or a skill given as a form of itself. While the mods
load the game's skill table is empty, so only the range is checked; a mod's skill is the number
`rq.skill.define` returned.

```lua
local THRUST = rq.skill.define({ id = "mymod:magic_thrust", kind = "physical", name = "Magic Thrust" })
rq.skill.form_of(THRUST, rq.ids.skill.MELEE_ATTACK_1)
rq.chara.on_recalc(function(iic)
  for _, s in ipairs(rq.chara.slots(iic)) do
    if s.skill == rq.ids.skill.MELEE_ATTACK_1 and rq.chara.weapon_detail(iic) == 2 then
      rq.chara.set_slot(iic, s.slot, THRUST)
      rq.chara.set_flavor(iic, s.slot)
    end
  end
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `skill` | `integer` | The skill number of the form. |
| `base` | `integer` | The skill number whose place it takes. |

See also: [`rq.skill.forms`](rq.skill.md#rqskillforms)

### rq.skill.forms

```lua
rq.skill.forms(skill) -> integer[]
```

`since 2.66.0`

Returns a skill's forms (`rq.skill.form_of`): the skills that take each other's place in a row.

Raises an error for a number outside 1 to 1000.

```lua
local family = rq.skill.forms(rq.ids.skill.MELEE_ATTACK_1)  -- { 100, 101 } in the base game
local key = family[1]  -- the lowest number: one key for the whole family
```

| Parameter | Type | Description |
| --- | --- | --- |
| `skill` | `integer` | The skill number. |

| Returns | Type | Description |
| --- | --- | --- |
| `forms` | `integer[]` | The family, lowest number first, `skill` included; `{ skill }` when it has no forms. |

## Events

| Name | Summary |
| --- | --- |
| [`rq.skill.on_describe`](#rqskillon_describe) | Calls `fn` for a skill's hover text, to rewrite it. |

### rq.skill.on_describe

```lua
rq.skill.on_describe(fn) -> fun()
```

`since 0.2.0` `changed 0.14.0` `changed 0.23.0` `changed 2.35.0`

Calls `fn` for a skill's hover text, to rewrite it.

Each callback gets the text the one before left. Up to 16 callbacks.

```lua
rq.skill.on_describe(function(no, text)
  local s = rq.skill.get(no)
  return text .. " (x" .. s.bairitsu .. ")"
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(skillNo: integer, baseText: string): string` | Returns the new text. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

> Changed in 0.14.0: Every mod's callback runs.

> Changed in 0.23.0: Returns a remover.

> Changed in 2.35.0: Wraps the hover text itself; before, it needed `rq.skill.install`.
