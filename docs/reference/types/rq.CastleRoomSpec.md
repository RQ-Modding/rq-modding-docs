# rq.CastleRoomSpec

A mod's room in Rance Castle, for `rq.castle.room`.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `name` | `string` | The room's name, as the castle shows it on its button. |
| `on_enter` | `fun(room:` [`rq.CastleRoomHandle`](rq.CastleRoomHandle.md) `)` | Runs when the player clicks the room. The castle stays open (it is not closed for cleaning), and the game goes back to the town's tabs after it, as with the Poster room. |
| `id` *(optional)* | `string` | The mod's own name for the room, for `rq.castle.rooms`. Default `name`. |
| `floor` *(optional)* | `integer\|string` | The floor: 1 (Roof) to 9 (B2F), or "Roof", "6F" to "1F", "B1F", "B2F". Default "B2F", beside the Poster room. |
| `shown` *(optional)* | `fun(): boolean` | Asked each time the castle opens; false leaves the room out this time. Default: always shown. |
| `new` *(optional)* | `boolean\|fun(): boolean` | The game's NEW mark on the room. Default false. |
| `face` *(optional)* | `integer\|fun(): integer` | A CG shown beside the name, as a character's face in the game's rooms. Default none. |
| `chara` *(optional)* | `integer` | A character number (`rq.ids.chara`): their face beside the name, as the game shows it (`Ｃ顔ＣＧ` of their roster slot); no face while they are not in the roster. Use this or `face`. Since 2.22.1 a character number; before, the number was read as a roster slot. |

## Used by

[`rq.castle.room`](../api/rq.castle.md#rqcastleroom)
