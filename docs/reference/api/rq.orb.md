# rq.orb

`since 0.2.0`

The blue Recovery Spring on the map (`回復の泉`, object 203).

The engine patches the party heal inside `回復の泉処理`; Lua decides who heals and how with
`on_heal`. The rest of the spring (Carolie, the flash, clearing the cell) stays the game's. The calls
that write raise an error for a slot with no character.

```lua
rq.orb.install()
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
| [`rq.orb.get_state`](#rqorbget_state) | Returns where a character is (`登録状態`). |
| [`rq.orb.set_state`](#rqorbset_state) | Sets where a character is (`登録状態`). |
| [`rq.orb.set_status`](#rqorbset_status) | Sets a character's status (`状態変化`). |
| [`rq.orb.get_hp`](#rqorbget_hp) | Returns a character's HP. |
| [`rq.orb.get_max_hp`](#rqorbget_max_hp) | Returns a character's most HP. |
| [`rq.orb.set_hp`](#rqorbset_hp) | Sets a character's HP. |
| [`rq.orb.full_heal`](#rqorbfull_heal) | Fills a character's HP (`Ｃ補給／体力`). |

### rq.orb.install

```lua
rq.orb.install() -> boolean
```

`since 0.2.0`

Patches the spring's party heal so it calls `on_heal`.

| Returns | Type | Description |
| --- | --- | --- |
| `ok` | `boolean` | true when the patch is in place. |

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

Returns where a character is (`登録状態`).

| Parameter | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The roster slot. |

| Returns | Type | Description |
| --- | --- | --- |
| `state` | `integer` | 1 party, 2 reserve, 3 spent. |

### rq.orb.set_state

```lua
rq.orb.set_state(iic, state)
```

`since 0.2.0`

Sets where a character is (`登録状態`).

| Parameter | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The roster slot. |
| `state` | `integer` | 1 party, 2 reserve, 3 spent. |

### rq.orb.set_status

```lua
rq.orb.set_status(iic, status)
```

`since 0.2.0`

Sets a character's status (`状態変化`).

| Parameter | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The roster slot. |
| `status` | `integer` | The status: 0 none, 1 poison, 3 downed. |

### rq.orb.get_hp

```lua
rq.orb.get_hp(iic) -> integer
```

`since 0.2.0`

Returns a character's HP.

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

Returns a character's most HP.

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

Sets a character's HP.

| Parameter | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The roster slot. |
| `hp` | `integer` | HP. |

### rq.orb.full_heal

```lua
rq.orb.full_heal(iic)
```

`since 0.2.0`

Fills a character's HP (`Ｃ補給／体力`).

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
