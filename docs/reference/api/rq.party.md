# rq.party

`since 0.22.0`

Reads and changes who is in the party.

The party has five ranks. Each holds a character id (the `id` of an entry in `rq.units()`) or 0
when it is empty.

## Functions

| Name | Summary |
| --- | --- |
| [`rq.party.get`](#rqpartyget) | Returns the character id on each of the five ranks. |
| [`rq.party.set`](#rqpartyset) | Replaces the whole party. |

### rq.party.get

```lua
rq.party.get() -> integer[]
```

`since 0.22.0`

Returns the character id on each of the five ranks.

```lua
for rank, id in ipairs(rq.party.get()) do
  if id ~= 0 then rq.log(rank, id) end
end
```

| Returns | Type | Description |
| --- | --- | --- |
| `ranks` | `integer[]` | Five ids in rank order; 0 for an empty rank. |

See also: [`rq.party.set`](rq.party.md#rqpartyset)

### rq.party.set

```lua
rq.party.set(ranks)
```

`since 0.22.0`

Replaces the whole party.

Raises an error, and changes nothing, during a battle, for a character that is not recruited,
for a character listed twice, or for more than five ranks. A screen that is already open, such
as the Party tab, does not redraw until it is opened again.

```lua
local ranks = rq.party.get()
ranks[1], ranks[2] = ranks[2], ranks[1]   -- swap the first two ranks
rq.party.set(ranks)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `ranks` | `(integer\|false)[]` | Up to five character ids in rank order; 0 or false leaves a rank empty. |

See also: [`rq.party.get`](rq.party.md#rqpartyget)
