# rq.StepsCtx

What `rq.encounters.on_steps` callbacks get.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `steps` | `integer` | The steps the game picked, or what an earlier callback returned. |
| `area_change` | `boolean` | true when the party changed area, false after a fight and when a quest starts. |

## Used by

[`rq.encounters.on_steps`](../api/rq.encounters.md#rqencounterson_steps)
