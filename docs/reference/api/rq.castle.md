# rq.castle

`since 0.2.0`

Reads the castle: whether it is open, its rooms and who is in them.

`rq.castle()` and `rq.castle.get()` are the same call.

## Functions

| Name | Summary |
| --- | --- |
| [`rq.castle.get`](#rqcastleget) | Returns the castle's state, as `rq.castle()` does. |

### rq.castle.get

```lua
rq.castle.get() -> rq.Castle
```

`since 0.2.0`

Returns the castle's state, as `rq.castle()` does.

| Returns | Type | Description |
| --- | --- | --- |
| `castle` | [`rq.Castle`](../types/rq.Castle.md) | A copy of the castle's state. |
