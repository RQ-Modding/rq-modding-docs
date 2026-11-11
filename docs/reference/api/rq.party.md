# rq.party

`since 0.22.0` `changed 2.35.0`

Reads and changes who is in the party.

The party has five ranks. Each holds a character id (the `id` of an entry in `rq.units()`) or 0
when it is empty. `roster`, `state` and `set_state` read and move the other characters (the first
and second armies), and `heal` is the game's heal.

## Functions

| Name | Summary |
| --- | --- |
| [`rq.party.get`](#rqpartyget) | Returns the character id on each of the five ranks. |
| [`rq.party.set`](#rqpartyset) | Replaces the whole party. |
| [`rq.party.roster`](#rqpartyroster) | Returns every recruited character, or those in one place. |
| [`rq.party.state`](#rqpartystate) | Returns where a character is (`登録状態`). |
| [`rq.party.set_state`](#rqpartyset_state) | Moves a character between the first army (2), used in this quest (3) and the second army (4). |
| [`rq.party.heal`](#rqpartyheal) | Heals the party as the game does: HP to the most, and with `skills` the skill uses too. |

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

### rq.party.roster

```lua
rq.party.roster(state) -> rq.PartyMember[]
```

`since 2.35.0`

Returns every recruited character, or those in one place.

It reads the roster's slots in order. The party's ranks are `rq.party.get`.

```lua
for _, m in ipairs(rq.party.roster(rq.ids.party_state.RESERVE)) do
  if m.status == rq.ids.state.DOWNED then rq.log(rq.chara.get(m.iic).name, "is down") end
end
```

| Parameter | Type | Description |
| --- | --- | --- |
| `state` *(optional)* | `integer` | Only characters in this place, 0 to 4 (`rq.ids.party_state`). |

| Returns | Type | Description |
| --- | --- | --- |
| `members` | [`rq.PartyMember`](../types/rq.PartyMember.md) `[]` | The characters. |

### rq.party.state

```lua
rq.party.state(iic) -> integer
```

`since 2.35.0`

Returns where a character is (`登録状態`).

| Parameter | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The roster slot. |

| Returns | Type | Description |
| --- | --- | --- |
| `state` | `integer` | 0 not recruited (also a slot with no character), 1 in the party, 2 the first army, 3 used in this quest, 4 the second army (`rq.ids.party_state`). |

### rq.party.set_state

```lua
rq.party.set_state(iic, state) -> boolean
```

`since 2.35.0`

Moves a character between the first army (2), used in this quest (3) and the second army (4).

A character marked used is not placed again until the quest ends, when the game puts it back in
the first army; 2 gives it back now. Into and out of the party is `rq.party.set`; leaving is
`rq.chara.dismiss`. A screen already open does not redraw until it opens again.

Raises an error for a slot with no character, one not recruited, a character in the party, or a
state other than 2, 3 and 4.

```lua
rq.party.set_state(iic, rq.ids.party_state.SECOND)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The roster slot. |
| `state` | `integer` | 2, 3 or 4 (`rq.ids.party_state`). |

| Returns | Type | Description |
| --- | --- | --- |
| `ok` | `boolean` | true. |

### rq.party.heal

```lua
rq.party.heal(opts) -> integer
```

`since 2.35.0`

Heals the party as the game does: HP to the most, and with `skills` the skill uses too.

A downed character is left as it is, as the game's party heals do (`ＰＴＡ体力回復`): set its
`status` to 0 with `rq.chara.set` first to raise it. `all` heals every recruited character, not
only the five ranks. Each heal is the game's own (`Ｃ補給／体力`, `Ｃ補給／スキル`).

Raises an error for options that are not true or false.

```lua
rq.party.heal({ skills = true })      -- as a spring
rq.party.heal({ half = true })        -- up to half the HP
```

| Parameter | Type | Description |
| --- | --- | --- |
| `opts` *(optional)* | `{skills?: boolean, half?: boolean, all?: boolean}` | `skills` fills the skill uses; `half` heals up to half the most HP (one above it is left as it is); `all` heals the whole roster. |

| Returns | Type | Description |
| --- | --- | --- |
| `count` | `integer` | How many characters were healed. |

See also: [`rq.chara.heal`](rq.chara.md#rqcharaheal)
