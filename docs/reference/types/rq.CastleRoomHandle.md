# rq.CastleRoomHandle

A mod's room, from `rq.castle.room`.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `area` | `fun(): integer` | The game's area number of the room, 30 to 50. |
| `floor` | `fun(): string\|nil` | The floor it was placed on the last time the castle opened, or nil. |
| `where` | `fun():` [`rq.CastleRoomPlace`](rq.CastleRoomPlace.md) `\|nil` | Where it is while the castle shows it; nil when it is not placed. |
| `set` | `fun(opts: {name?: string, shown?: fun(): boolean, new?: boolean\|fun(): boolean, floor?: integer\|string})` | Changes the room from the next time the castle opens. |
| `remove` | `fun()` | Takes the room out from the next time the castle opens. Its area number is not given again. |

## Used by

[`rq.CastleRoomSpec`](rq.CastleRoomSpec.md), [`rq.castle.room`](../api/rq.castle.md#rqcastleroom)
