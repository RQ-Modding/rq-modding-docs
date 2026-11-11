# rq.EncounterCtx

What `rq.encounters.on_encounter` callbacks get.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `placed` | `boolean` | true for an enemy standing on the map, false for a random fight. |
| `groups` | `integer[]` | The area's enemy groups, by the game's group number. |

## Used by

[`rq.encounters.on_encounter`](../api/rq.encounters.md#rqencounterson_encounter)
