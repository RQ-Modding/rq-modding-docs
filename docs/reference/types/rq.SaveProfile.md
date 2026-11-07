# rq.SaveProfile

A save profile, from `rq.saves.list`.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `id` | `string` | "base", or an id the engine made. Show `name` instead. |
| `name` | `string` | The name. |
| `is_base` | `boolean` | The base profile, which can never be deleted. |
| `active` | `boolean` | The game runs on this profile. |
| `created` *(optional)* | `string` | When it was made. |
| `last_saved` *(optional)* | `string` | When it was last saved. |
| `source` *(optional)* | `string` | Where it came from, such as "clone of X" or "imported from the vanilla game". |
| `mods` *(optional)* | [`rq.SaveMod`](rq.SaveMod.md) `[]` | The mods loaded when the game last wrote a slot of this save; nil when it never did under the loader. |
| `mods_ever` *(optional)* | `string[]` | The ids of every mod loaded for any save of this profile. |
| `summary` | [`rq.SaveSummary`](rq.SaveSummary.md) | What the save holds. |

## Used by

[`rq.saves.list`](../api/rq.saves.md#rqsaveslist)
