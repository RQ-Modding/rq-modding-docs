# rq.EncounterInfo

What `rq.encounters.info` returns.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `groups` | `integer[]` | The area's enemy groups, by the game's group number or a mod's (`rq.monster.group`), up to 5; empty when the area has none. |
| `steps` | `integer` | The steps that fill the bar. |
| `walked` | `integer` | The steps walked toward it, 0 to `steps`. |
| `on` | `boolean` | Random fights can happen here: the area has groups and no mod holds them off. |
| `held` | `string[]` | The ids of the mods that hold random fights off (`rq.encounters.hold`), sorted. |

## Used by

[`rq.encounters.info`](../api/rq.encounters.md#rqencountersinfo)
