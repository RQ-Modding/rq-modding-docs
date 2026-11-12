# rq.BattleFamiliar

`since 2.37.0`

The familiar of a fight, as `rq.battle.familiar` returns it.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | Its roster slot, 10. |
| `no` | `integer` | Its monster number. |
| `owner` | `integer` | The roster slot of the ally it fights beside. |
| `item` *(optional)* | `integer` | The familiar item's instance: the owner's held item, or the vault's for one that jumped in. nil when it cannot be found. |
| `joined` | `boolean` | true for a strong familiar from the vault that jumped in beside an ally (one fight in 50), false for one its owner called. |
| `spd` | `integer` | Its speed now. |
| `own_spd` | `integer` | Its speed as built, before the game held it to the party's top speed. From a fight that started after the first call to `rq.battle.familiar`, `on_order` or `on_order_after`; before, its speed now. |
| `growth` *(optional)* | `integer` | The item's growth, 0 to 5000 (the game's "LV"); the familiar's attack and magic are 100% plus a tenth of it, at most 600%. |

## Used by

[`rq.battle.familiar`](../api/rq.battle.md#rqbattlefamiliar)
