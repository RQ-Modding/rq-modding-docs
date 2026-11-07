# rq.ChestInfo

What `rq.chest.on_attempt` and `on_result` get for a red chest.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `x` | `integer` | The chest's cell. |
| `y` | `integer` | The chest's cell. |
| `id` | `integer` | The item locked in the chest by `rq.loot.install`; 0 when none. |
| `base_pct` | `integer` | This chest's chance from the game and the party's skills: 30, or 60, 80 or 100, maybe halved. |
| `kind` | `string` | "red". |
| `pct` *(optional)* | `integer` | `on_attempt`: the percent so far. `on_result`: the chance used. Since 0.14.0. |
| `rolled` *(optional)* | `integer` | `on_result`: the roll, 1 to 100. |
| `success` *(optional)* | `boolean` | `on_result`: it opened. |
| `exploded` *(optional)* | `boolean` | `on_result`: it exploded; a fail always does. |

## Used by

[`rq.chest.on_attempt`](../api/rq.chest.md#rqcheston_attempt), [`rq.chest.on_result`](../api/rq.chest.md#rqcheston_result)
