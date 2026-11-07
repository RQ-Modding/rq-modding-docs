# rq.units

`since 0.2.0`

Lists the recruited characters.

`rq.units()` and `rq.units.list()` are the same call. The list is a copy: changing it does not
change the save. Right after boot it holds only the three default characters the game makes
before a save loads; wait until it lists more than 10, or use `rq.saves`.

```lua
for _, u in ipairs(rq.units()) do
  rq.log(u.id, u.name, u.level)
end
```

## Functions

| Name | Summary |
| --- | --- |
| [`rq.units.list`](#rqunitslist) | Returns the recruited characters, as `rq.units()` does. |

### rq.units.list

```lua
rq.units.list() -> rq.Unit[]
```

`since 0.2.0`

Returns the recruited characters, as `rq.units()` does.

| Returns | Type | Description |
| --- | --- | --- |
| `units` | [`rq.Unit`](../types/rq.Unit.md) `[]` | A copy of each recruited character. |
