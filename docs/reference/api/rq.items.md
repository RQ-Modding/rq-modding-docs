# rq.items

`since 0.2.0`

Lists the item instances the player owns.

`rq.items()` and `rq.items.list()` are the same call. Instances whose existence value is 0, 6 or 9
are left out. The list is a copy.

## Functions

| Name | Summary |
| --- | --- |
| [`rq.items.list`](#rqitemslist) | Returns the owned item instances, as `rq.items()` does. |

### rq.items.list

```lua
rq.items.list() -> rq.Item[]
```

`since 0.2.0`

Returns the owned item instances, as `rq.items()` does.

| Returns | Type | Description |
| --- | --- | --- |
| `items` | [`rq.Item`](../types/rq.Item.md) `[]` | A copy of each owned item. |
