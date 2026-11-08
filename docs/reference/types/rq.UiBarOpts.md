# rq.UiBarOpts

`since 2.14.0`

What `rq.uikit.bar` takes.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `style` *(optional)* | `"hp"\|"mini"\|"monster"\|"exp"\|"charisma"\|"quest"\|"magnum"` | One of the game's bars: `"hp"` (10125, the status and character cards' HP), `"mini"` (10098, the mini cards' HP), `"monster"` (10142, a monster's HP), `"exp"` (10302, EXP on the battle results), `"charisma"` (10013, the hub's), `"quest"` (11303, a quest on the map), `"magnum"` (11316, the Magnum gauge, upright). |
| `cg` *(optional)* | `integer` | Any CG as the bar, a mod image included; it is the bar's size. |
| `dir` *(optional)* | `"right"\|"up"` | "right" (default): it fills from the left. "up": from the bottom. Default "up" for `"magnum"`. |
| `color` *(optional)* | `integer[]\|{r: integer, g: integer, b: integer, a?: integer}` | A bar of one color, `w` by `h` (default 190 by 4, as the battle's). |
| `anim` *(optional)* | `integer` | In ms: a new value is reached in a straight line over this time, as the game's bars move. Default 0, at once. Needs an `id`, or the same call order. |

## Used by

[`rq.uikit.bar`](../api/rq.uikit.md#rquikitbar)
