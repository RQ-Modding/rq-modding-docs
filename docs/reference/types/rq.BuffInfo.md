# rq.BuffInfo

One mark a card shows, from `rq.battle.buffs`.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `mark` *(optional)* | `integer` | A game mark: 31 flame, 32 guard, 33 berserk, 34 stealth, 35 protect, 36 barrier. |
| `key` *(optional)* | `string` | A mod buff's key. |
| `icon` *(optional)* | `integer` | A mod buff's icon. |
| `rank` *(optional)* | `boolean` | true when the buff belongs to the rank. Since 0.29.0. |
| `pinned` *(optional)* | `boolean` | true when it stays shown, out of the turns. Since 0.30.0. |
| `text` | `string` | The text shown with it. |

## Used by

[`rq.battle.buffs`](../api/rq.battle.md#rqbattlebuffs)
