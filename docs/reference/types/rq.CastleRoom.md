# rq.CastleRoom

A castle room, from `rq.castle()`.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `id` | `integer` | The room's index. |
| `name` | `string` | The name. |
| `state` | `integer` | The game's raw state; above 0 means open. |
| `enabled` | `boolean` | `state` is above 0. |
| `used` | `boolean` | The room was already used. |
| `units` | `{id: integer, name: string}[]` | Always empty for now; the castle's characters are in `rq.Castle.units`. |

## Used by

[`rq.Castle`](rq.Castle.md)
