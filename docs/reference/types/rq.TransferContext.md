# rq.TransferContext

What `rq.world.on_transfer` and `on_transfer_after` callbacks get.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `world` | `integer` | The world as the game holds it: the new one, in play. |
| `from` | `integer` | The world before: `world` - 1 (the game goes from 1 to 2 and from 2 to 3). |

## Used by

[`rq.world.on_transfer`](../api/rq.world.md#rqworldon_transfer), [`rq.world.on_transfer_after`](../api/rq.world.md#rqworldon_transfer_after)
