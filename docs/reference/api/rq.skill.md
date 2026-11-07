# rq.skill

`since 0.2.0`

Reads, defines and patches skills, and rewrites their hover text.

Skill numbers run 1 to 1000; the game's end near 600. A text id such as `"mymod:slash"` becomes a
stable number from 700 to 999. Strings are UTF-8 in Lua. The calls that write raise an error for a
number outside 1 to 1000. Up to 128 `define` and `patch` calls in all.

## Functions

| Name | Summary |
| --- | --- |
| [`rq.skill.install`](#rqskillinstall) | Wraps `スキル_説明文１`, the hover text on the status and fight screens, so `on_describe` can rewrite it. |
| [`rq.skill.get`](#rqskillget) | Returns a skill's fields. |
| [`rq.skill.define`](#rqskilldefine) | Defines a new skill. |
| [`rq.skill.patch`](#rqskillpatch) | Changes an existing skill, field by field. |
| [`rq.skill.sort_as`](#rqskillsort_as) | Sorts a skill in the known and potential lists as if it were another. |

### rq.skill.install

```lua
rq.skill.install() -> boolean
```

`since 0.2.0`

Wraps `スキル_説明文１`, the hover text on the status and fight screens, so `on_describe` can rewrite
it.

| Returns | Type | Description |
| --- | --- | --- |
| `ok` | `boolean` | true when the patch is in place. |

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

## Events

| Name | Summary |
| --- | --- |
| [`rq.skill.on_describe`](#rqskillon_describe) | Calls `fn` for a skill's hover text, to rewrite it. |

### rq.skill.on_describe

```lua
rq.skill.on_describe(fn) -> fun()
```

`since 0.2.0` `changed 0.14.0` `changed 0.23.0`

Calls `fn` for a skill's hover text, to rewrite it.

Each callback gets the text the one before left. Needs `rq.skill.install`. Up to 16 callbacks.

```lua
rq.skill.install()
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
