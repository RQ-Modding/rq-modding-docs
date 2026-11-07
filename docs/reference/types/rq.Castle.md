# rq.Castle

The castle's state, from `rq.castle()`.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `unlocked` | `boolean` | The castle is open. |
| `enabled` | `boolean` | Open, with a room open (or no rooms listed). |
| `used` | `boolean` | A room was already used. |
| `open` | `integer` | The game's raw castle-open flag. |
| `rooms` | [`rq.CastleRoom`](rq.CastleRoom.md) `[]` | The rooms that have a name, an open state or a use, up to 32. |
| `units` | `{id: integer, name: string}[]` | The characters on the castle roster, up to 32. |

## Used by

[`rq.castle.get`](../api/rq.castle.md#rqcastleget)
