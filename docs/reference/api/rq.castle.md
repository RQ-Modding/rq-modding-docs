# rq.castle

`since 0.2.0`

Reads the castle: whether it is open, its rooms and who is in them.

`rq.castle()` and `rq.castle.get()` are the same call.

## Functions

| Name | Summary |
| --- | --- |
| [`rq.castle.get`](#rqcastleget) | Returns the castle's state, as `rq.castle()` does. |
| [`rq.castle.room`](#rqcastleroom) | Adds a room of the mod's own to Rance Castle. |
| [`rq.castle.rooms`](#rqcastlerooms) | Lists every mod's room in Rance Castle. |

### rq.castle.get

```lua
rq.castle.get() -> rq.Castle
```

`since 0.2.0`

Returns the castle's state, as `rq.castle()` does.

| Returns | Type | Description |
| --- | --- | --- |
| `castle` | [`rq.Castle`](../types/rq.Castle.md) | A copy of the castle's state. |

### rq.castle.room

```lua
rq.castle.room(spec) -> rq.CastleRoomHandle
```

`since 2.16.0` `changed 2.22.1`

Adds a room of the mod's own to Rance Castle.

The room is one of the game's own castle areas, numbers 30 to 50, which the game leaves free. The
castle rolls its rooms each time it opens; a mod's room is made each time as well, as the Gal
monsters and Poster rooms are, so the game draws its button, its name in the castle's font, the
face and the NEW mark, and moves the keys to it. It goes in a free cell of its floor; when the floor
is full that time, in the nearest floor with one (the one below first). The game's own rooms never
move. When the player clicks it, `on_enter` runs instead of the game's room code. A mod may open
a page, a choice menu or a scene there.

Make rooms in `init.lua`; 21 at most, from every mod. The area numbers go in load order and are
kept in the save's castle arrays, which the game reads only for 1 to 29.

Raises an error for a spec that is not a table, no name, no `on_enter`, a bad floor, a `shown`
that is not a function, a `new` or `face` of the wrong type, or no area left.

slot, so another character's face showed.

```lua
rq.castle.room({ id = "workshop", name = "Workshop", floor = "B2F", new = true,
  on_enter = function(room)
    rq.ui.choose({ "Craft", "Repair" }, function(id) rq.log("picked", id) end)
  end })
```

| Parameter | Type | Description |
| --- | --- | --- |
| `spec` | [`rq.CastleRoomSpec`](../types/rq.CastleRoomSpec.md) | The room. |

| Returns | Type | Description |
| --- | --- | --- |
| `room` | [`rq.CastleRoomHandle`](../types/rq.CastleRoomHandle.md) | The room, to change or remove it. |

> Changed in 2.22.1: `chara` is a character number, as the reference said: it was read as a roster

### rq.castle.rooms

```lua
rq.castle.rooms() -> rq.CastleRoomInfo[]
```

`since 2.16.0`

Lists every mod's room in Rance Castle.

| Returns | Type | Description |
| --- | --- | --- |
| `rooms` | [`rq.CastleRoomInfo`](../types/rq.CastleRoomInfo.md) `[]` | In the order they were made; removed rooms are left out. |
