# rq.orb

`since 0.2.0` `changed 2.35.0`

The blue Recovery Spring on the map (`回復の泉`, object 203).

The engine patches the party heal inside `回復の泉処理`; Lua decides who heals and how with
`on_heal`. The rest of the spring (Carolie, the flash, clearing the cell) stays the game's. The calls
that write raise an error for a slot with no character.

The other calls are older names for what `rq.party` and `rq.chara` do anywhere: `roster`,
`get_state` and `set_state` are `rq.party.roster`, `state` and `set_state`; `full_heal` is
`rq.chara.heal`; the HP and the status are `rq.chara.get` and `rq.chara.set`'s `hp`, `hp_max` and
`status`. They stay. Since 2.35.0 each call places the spring's patch the first time; before, a
call made without `rq.orb.install` read 0 and wrote nothing.

```lua
rq.orb.on_heal(function()
  for _, m in ipairs(rq.orb.roster()) do
    if m.state == 1 or m.state == 2 then
      rq.orb.full_heal(m.iic)
    elseif m.state == 3 then  -- revive the spent at 30%
      rq.orb.set_state(m.iic, 2)
      rq.orb.set_hp(m.iic, math.max(1, math.floor(m.max_hp * 3 / 10)))
    end
  end
end)
```

## Functions

| Name | Summary |
| --- | --- |
| [`rq.orb.install`](#rqorbinstall) | Patches the spring's party heal so it calls `on_heal`. |
| [`rq.orb.roster`](#rqorbroster) | Lists the roster members, slots 20 to 200 with a state other than 0. |
| [`rq.orb.get_state`](#rqorbget_state) | Returns where a character is (`登録状態`). The same as `rq.party.state`. |
| [`rq.orb.set_state`](#rqorbset_state) | Sets where a character is (`登録状態`), with no check. `rq.party.set_state` checks the move. |
| [`rq.orb.set_status`](#rqorbset_status) | Sets a character's status (`状態変化`). The same as `rq.chara.set(iic, { status = n })`. |
| [`rq.orb.get_hp`](#rqorbget_hp) | Returns a character's HP. The same as `rq.chara.get(iic).hp`. |
| [`rq.orb.get_max_hp`](#rqorbget_max_hp) | Returns a character's most HP. The same as `rq.chara.get(iic).hp_max`. |
| [`rq.orb.set_hp`](#rqorbset_hp) | Sets a character's HP. The same as `rq.chara.set(iic, { hp = n })`. |
| [`rq.orb.full_heal`](#rqorbfull_heal) | Fills a character's HP (`Ｃ補給／体力`), also a downed character's. `rq.chara.heal` leaves the downed as they are, as the game's party heals do. |

### rq.orb.install

```lua
rq.orb.install() -> boolean
```

`since 0.2.0` `changed 2.35.0`

Patches the spring's party heal so it calls `on_heal`.

Not needed since 2.35.0: each call that needs it places it the first time, and raises this
call's error there when it cannot. Calling it still does no harm.

| Returns | Type | Description |
| --- | --- | --- |
| `ok` | `boolean` | true when the patch is in place. |

> Changed in 2.35.0: Not needed: every `rq.orb` call makes it.

### rq.orb.roster

```lua
rq.orb.roster(state) -> rq.OrbMember[]
```

`since 0.2.0`

Lists the roster members, slots 20 to 200 with a state other than 0.

| Parameter | Type | Description |
| --- | --- | --- |
| `state` *(optional)* | `integer` | Only members with this state. |

| Returns | Type | Description |
| --- | --- | --- |
| `members` | [`rq.OrbMember`](../types/rq.OrbMember.md) `[]` | The members. |

### rq.orb.get_state

```lua
rq.orb.get_state(iic) -> integer
```

`since 0.2.0`

Returns where a character is (`登録状態`). The same as `rq.party.state`.

| Parameter | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The roster slot. |

| Returns | Type | Description |
| --- | --- | --- |
| `state` | `integer` | 1 in the party, 2 the first army, 3 used in this quest, 4 the second army (`rq.ids.party_state`). |

### rq.orb.set_state

```lua
rq.orb.set_state(iic, state)
```

`since 0.2.0`

Sets where a character is (`登録状態`), with no check. `rq.party.set_state` checks the move.

| Parameter | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The roster slot. |
| `state` | `integer` | 1 in the party, 2 the first army, 3 used in this quest, 4 the second army (`rq.ids.party_state`). |

### rq.orb.set_status

```lua
rq.orb.set_status(iic, status)
```

`since 0.2.0`

Sets a character's status (`状態変化`). The same as `rq.chara.set(iic, { status = n })`.

| Parameter | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The roster slot. |
| `status` | `integer` | The status: 0 none, 1 poison, 2 stun, 3 downed (`rq.ids.state`). |

### rq.orb.get_hp

```lua
rq.orb.get_hp(iic) -> integer
```

`since 0.2.0`

Returns a character's HP. The same as `rq.chara.get(iic).hp`.

| Parameter | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The roster slot. |

| Returns | Type | Description |
| --- | --- | --- |
| `hp` | `integer` | HP. |

### rq.orb.get_max_hp

```lua
rq.orb.get_max_hp(iic) -> integer
```

`since 0.2.0`

Returns a character's most HP. The same as `rq.chara.get(iic).hp_max`.

| Parameter | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The roster slot. |

| Returns | Type | Description |
| --- | --- | --- |
| `max` | `integer` | Most HP. |

### rq.orb.set_hp

```lua
rq.orb.set_hp(iic, hp)
```

`since 0.2.0`

Sets a character's HP. The same as `rq.chara.set(iic, { hp = n })`.

| Parameter | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The roster slot. |
| `hp` | `integer` | HP. |

### rq.orb.full_heal

```lua
rq.orb.full_heal(iic)
```

`since 0.2.0`

Fills a character's HP (`Ｃ補給／体力`), also a downed character's. `rq.chara.heal` leaves the downed
as they are, as the game's party heals do.

| Parameter | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The roster slot. |

## Events

| Name | Summary |
| --- | --- |
| [`rq.orb.on_heal`](#rqorbon_heal) | Calls `fn` when the spring heals, in place of the game's party heal. |

### rq.orb.on_heal

```lua
rq.orb.on_heal(fn) -> fun()
```

`since 0.2.0` `changed 0.14.0` `changed 0.23.0`

Calls `fn` when the spring heals, in place of the game's party heal.

Every callback runs, so two mods that heal both heal. The game's heal runs only with no callback, or
when all of them failed. Up to 16 callbacks.

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun()` | Heals. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

> Changed in 0.14.0: Every mod's callback runs.

> Changed in 0.23.0: Returns a remover.
