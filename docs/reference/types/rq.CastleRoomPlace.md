# rq.CastleRoomPlace

Where a mod's room is this time, from a room's `where()`.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `floor` | `string` | "Roof", "6F" to "1F", "B1F" or "B2F". |
| `row` | `integer` | 1 (Roof) to 9 (B2F). |
| `col` | `integer` | 1 to 3. |
| `x` | `integer` | The room's button, left edge in screen pixels. |
| `y` | `integer` | Top edge. |
| `w` | `integer` | Width, 207. |
| `h` | `integer` | Height, 30. |

## Used by

[`rq.CastleRoomHandle`](rq.CastleRoomHandle.md)
