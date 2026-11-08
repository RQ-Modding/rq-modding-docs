# rq.CastleRoomInfo

A mod's room, as `rq.castle.rooms` lists it.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `id` | `string` | The room's id. |
| `mod` | `string` | The mod that made it. |
| `name` | `string` | Its name. |
| `area` | `integer` | Its area number. |
| `shown` | `boolean` | It was shown the last time the castle opened. |
| `floor` *(optional)* | `string` | Where it is now, while the castle shows it. |
| `col` *(optional)* | `integer` | Its column there, 1 to 3. |

## Used by

[`rq.castle.rooms`](../api/rq.castle.md#rqcastlerooms)
